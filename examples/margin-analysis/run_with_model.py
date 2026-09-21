#!/usr/bin/env python3
"""Run the public margin workflow with an optional OpenAI-compatible model.

This script performs real model calls against an explicitly configured endpoint
and records measured latency plus provider-reported token usage when available.

Required environment variables:
  AI_BASE_URL   e.g. https://api.openai.com/v1
  AI_API_KEY
  AI_MODEL

Optional:
  AI_INPUT_EUR_PER_MILLION
  AI_OUTPUT_EUR_PER_MILLION
  AI_CACHED_EUR_PER_MILLION

No vendor pricing is hard-coded.
"""

from __future__ import annotations

import json
import os
import time
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "demo-data"
OUT = ROOT / "examples" / "observability" / "measured-margin-model-trace.json"


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def call_model(base_url: str, api_key: str, model: str, messages: list[dict[str, str]]) -> tuple[dict[str, Any], float]:
    url = base_url.rstrip("/") + "/chat/completions"
    payload = json.dumps({
        "model": model,
        "messages": messages,
        "temperature": 0.1,
    }).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=payload,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    started = time.perf_counter()
    with urllib.request.urlopen(req, timeout=120) as resp:
        body = resp.read()
    latency_ms = (time.perf_counter() - started) * 1000
    return json.loads(body.decode("utf-8")), latency_ms


def usage_from(response: dict[str, Any]) -> dict[str, int]:
    u = response.get("usage") or {}
    prompt = int(u.get("prompt_tokens") or u.get("input_tokens") or 0)
    completion = int(u.get("completion_tokens") or u.get("output_tokens") or 0)
    details = u.get("prompt_tokens_details") or u.get("input_tokens_details") or {}
    cached = int(details.get("cached_tokens") or 0)
    return {
        "input_tokens": prompt,
        "output_tokens": completion,
        "cached_tokens": cached,
        "total_tokens": int(u.get("total_tokens") or (prompt + completion)),
    }


def text_from(response: dict[str, Any]) -> str:
    choices = response.get("choices") or []
    if not choices:
        return ""
    return str((choices[0].get("message") or {}).get("content") or "")


def rate(name: str) -> float | None:
    value = os.getenv(name)
    return float(value) if value else None


def main() -> None:
    base_url = os.environ["AI_BASE_URL"]
    api_key = os.environ["AI_API_KEY"]
    model = os.environ["AI_MODEL"]

    financials = read_text(DATA / "monthly_financials.csv")
    projects = read_text(DATA / "projects.csv")
    events = read_text(DATA / "events.csv")

    calls = [
        [
            {"role": "system", "content": "You are the Finance Agent. Use only supplied evidence. Separate facts from inference."},
            {"role": "user", "content": "Question: Why did gross margin fall this month?\n\nMONTHLY FINANCIALS:\n" + financials},
        ],
        [
            {"role": "system", "content": "You are the Operations Agent. Rank material project-level margin risks using only supplied evidence."},
            {"role": "user", "content": "Question: Which projects are contributing most to margin pressure?\n\nPROJECTS:\n" + projects + "\n\nEVENTS:\n" + events},
        ],
    ]

    call_records = []
    outputs = []
    totals = {"input_tokens": 0, "output_tokens": 0, "cached_tokens": 0, "total_tokens": 0}
    workflow_started = time.perf_counter()

    for idx, messages in enumerate(calls, start=1):
        response, latency = call_model(base_url, api_key, model, messages)
        usage = usage_from(response)
        for k in totals:
            totals[k] += usage[k]
        outputs.append(text_from(response))
        call_records.append({
            "call": idx,
            "model": model,
            "latency_ms": round(latency, 3),
            "usage": usage,
        })

    synthesis_messages = [
        {
            "role": "system",
            "content": (
                "You are the Executive Orchestrator. Reconcile the specialist findings. "
                "Return: Situation, Evidence, Competing explanations, What matters most, "
                "Options, Trade-offs, Recommended next move, What would change the recommendation. "
                "Do not invent facts."
            ),
        },
        {
            "role": "user",
            "content": "FINANCE FINDING:\n" + outputs[0] + "\n\nOPERATIONS FINDING:\n" + outputs[1],
        },
    ]
    response, latency = call_model(base_url, api_key, model, synthesis_messages)
    usage = usage_from(response)
    for k in totals:
        totals[k] += usage[k]
    final_answer = text_from(response)
    call_records.append({
        "call": 3,
        "model": model,
        "latency_ms": round(latency, 3),
        "usage": usage,
    })

    workflow_latency_ms = (time.perf_counter() - workflow_started) * 1000

    input_rate = rate("AI_INPUT_EUR_PER_MILLION")
    output_rate = rate("AI_OUTPUT_EUR_PER_MILLION")
    cached_rate = rate("AI_CACHED_EUR_PER_MILLION") or 0.0
    estimated_cost = None
    if input_rate is not None and output_rate is not None:
        uncached = max(totals["input_tokens"] - totals["cached_tokens"], 0)
        estimated_cost = (
            uncached / 1_000_000 * input_rate
            + totals["cached_tokens"] / 1_000_000 * cached_rate
            + totals["output_tokens"] / 1_000_000 * output_rate
        )

    trace = {
        "measured": True,
        "generated_at_unix": time.time(),
        "question": "Why did our gross margin fall this month?",
        "model": model,
        "endpoint": base_url,
        "workflow": {
            "model_calls": len(call_records),
            "workflow_latency_ms": round(workflow_latency_ms, 3),
        },
        "usage": totals,
        "economics": {
            "estimated_cost_eur": None if estimated_cost is None else round(estimated_cost, 6),
            "pricing_source": "environment_variables" if estimated_cost is not None else None,
            "note": "No vendor prices are hard-coded.",
        },
        "model_calls": call_records,
        "final_answer": final_answer,
        "limitations": [
            "This measures model/API latency, not GPU telemetry unless the endpoint operator correlates the trace with infrastructure metrics.",
            "Provider token usage fields vary; unsupported fields are recorded as zero.",
        ],
    }

    OUT.write_text(json.dumps(trace, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps(trace, indent=2, ensure_ascii=False))
    print(f"\nSaved measured trace to: {OUT}")


if __name__ == "__main__":
    try:
        main()
    except KeyError as exc:
        raise SystemExit(f"Missing required environment variable: {exc.args[0]}")
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        raise SystemExit(f"HTTP {exc.code}: {body}")
