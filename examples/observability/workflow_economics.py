#!/usr/bin/env python3
"""Calculate cost per executive workflow from a trace and explicit pricing inputs.

No vendor price is hard-coded. The operator supplies the commercial assumptions
appropriate to the deployment being evaluated.

Examples:
  python3 examples/observability/workflow_economics.py \
    --trace examples/observability/margin-analysis-trace.json \
    --input-eur-per-million 0.50 \
    --output-eur-per-million 1.50

  python3 examples/observability/workflow_economics.py \
    --trace examples/observability/margin-analysis-trace.json \
    --gpu-hour-eur 3.00 \
    --gpu-seconds 5.2 \
    --fixed-overhead-eur 0.02
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


def load_trace(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def managed_cost(
    input_tokens: int,
    output_tokens: int,
    cached_tokens: int,
    input_rate: float,
    output_rate: float,
    cached_rate: float,
) -> dict[str, float]:
    billable_input = max(input_tokens - cached_tokens, 0)
    input_cost = billable_input / 1_000_000 * input_rate
    cached_cost = cached_tokens / 1_000_000 * cached_rate
    output_cost = output_tokens / 1_000_000 * output_rate
    return {
        "uncached_input_cost_eur": input_cost,
        "cached_input_cost_eur": cached_cost,
        "output_cost_eur": output_cost,
        "inference_cost_eur": input_cost + cached_cost + output_cost,
    }


def private_gpu_cost(gpu_seconds: float, gpu_hour_eur: float) -> dict[str, float]:
    cost = gpu_seconds / 3600 * gpu_hour_eur
    return {
        "gpu_seconds": gpu_seconds,
        "effective_gpu_hour_eur": gpu_hour_eur,
        "inference_cost_eur": cost,
    }


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Calculate cost per executive workflow using explicit deployment assumptions."
    )
    parser.add_argument("--trace", required=True, type=Path)
    parser.add_argument("--input-eur-per-million", type=float)
    parser.add_argument("--output-eur-per-million", type=float)
    parser.add_argument("--cached-eur-per-million", type=float, default=0.0)
    parser.add_argument("--gpu-hour-eur", type=float)
    parser.add_argument("--gpu-seconds", type=float)
    parser.add_argument("--fixed-overhead-eur", type=float, default=0.0)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    trace = load_trace(args.trace)
    eco = trace.get("economics", {})
    input_tokens = int(eco.get("input_tokens", 0))
    output_tokens = int(eco.get("output_tokens", 0))
    cached_tokens = int(eco.get("cached_tokens", 0))

    managed_requested = (
        args.input_eur_per_million is not None
        or args.output_eur_per_million is not None
    )
    private_requested = args.gpu_hour_eur is not None or args.gpu_seconds is not None

    if managed_requested and private_requested:
        parser.error("Choose either token-priced managed inference or GPU-time pricing, not both.")

    if managed_requested:
        if args.input_eur_per_million is None or args.output_eur_per_million is None:
            parser.error("Managed mode requires both input and output token rates.")
        detail = managed_cost(
            input_tokens,
            output_tokens,
            cached_tokens,
            args.input_eur_per_million,
            args.output_eur_per_million,
            args.cached_eur_per_million,
        )
        mode = "managed_token_pricing"
        assumptions = {
            "input_eur_per_million_tokens": args.input_eur_per_million,
            "output_eur_per_million_tokens": args.output_eur_per_million,
            "cached_eur_per_million_tokens": args.cached_eur_per_million,
        }
    elif private_requested:
        if args.gpu_hour_eur is None or args.gpu_seconds is None:
            parser.error("Private GPU mode requires both --gpu-hour-eur and --gpu-seconds.")
        detail = private_gpu_cost(args.gpu_seconds, args.gpu_hour_eur)
        mode = "private_gpu_time"
        assumptions = {
            "effective_gpu_hour_eur": args.gpu_hour_eur,
            "gpu_seconds_attributed_to_workflow": args.gpu_seconds,
        }
    else:
        parser.error(
            "Provide managed token rates or private GPU-hour + GPU-seconds assumptions."
        )

    total = detail["inference_cost_eur"] + args.fixed_overhead_eur
    result = {
        "trace_id": trace.get("trace_id"),
        "question_id": trace.get("question_id"),
        "pricing_mode": mode,
        "workload": {
            "model_calls": trace.get("workflow", {}).get("model_calls", 0),
            "input_tokens": input_tokens,
            "output_tokens": output_tokens,
            "cached_tokens": cached_tokens,
            "workflow_latency_ms": trace.get("workflow", {}).get("workflow_latency_ms"),
        },
        "assumptions": assumptions,
        "cost": {
            **{k: round(v, 6) for k, v in detail.items()},
            "fixed_overhead_eur": round(args.fixed_overhead_eur, 6),
            "cost_per_executive_workflow_eur": round(total, 6),
        },
        "warning": (
            "This result is an allocation model, not a vendor quote. Include utilization, "
            "idle capacity, software, power, cooling and operations in the effective GPU-hour "
            "rate when evaluating owned infrastructure."
        ),
    }

    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        print("\nExecutive Workflow Economics")
        print("=" * 28)
        print(f"Trace: {result['trace_id']}")
        print(f"Mode: {mode}")
        print(f"Model calls: {result['workload']['model_calls']}")
        print(
            "Tokens: "
            f"{input_tokens:,} input / {output_tokens:,} output / {cached_tokens:,} cached"
        )
        print(f"Inference allocation: €{detail['inference_cost_eur']:.6f}")
        print(f"Fixed overhead: €{args.fixed_overhead_eur:.6f}")
        print(f"COST PER EXECUTIVE WORKFLOW: €{total:.6f}")


if __name__ == "__main__":
    main()
