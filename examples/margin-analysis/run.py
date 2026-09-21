#!/usr/bin/env python3
"""Deterministic margin-leakage workflow for the public Northstar demo.

This script intentionally uses only Python's standard library. It reads the
synthetic company CSVs, calculates company-level margin deterioration, ranks
project-level margin leakage indicators, and emits a machine-readable executive
packet plus reproducible runtime telemetry.

It does NOT call an LLM. Production deployments can replace or extend the
deterministic analysis with governed model calls and record token/cost metrics.
"""

from __future__ import annotations

import argparse
import csv
import json
import time
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = ROOT / "demo-data"


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def euro(value: float) -> str:
    return f"€{value:,.0f}".replace(",", " ")


def pct(value: float) -> str:
    return f"{value * 100:.1f}%"


def build_packet() -> dict[str, Any]:
    started = time.perf_counter()

    financials = read_csv(DATA_DIR / "monthly_financials.csv")
    projects = read_csv(DATA_DIR / "projects.csv")

    first = financials[0]
    latest = financials[-1]

    first_margin = float(first["gross_margin_pct"])
    latest_margin = float(latest["gross_margin_pct"])
    margin_change_pp = (latest_margin - first_margin) * 100

    first_revenue = float(first["revenue_eur"])
    latest_revenue = float(latest["revenue_eur"])
    revenue_change_pct = (latest_revenue / first_revenue - 1) * 100

    project_findings: list[dict[str, Any]] = []
    for row in projects:
        planned_margin = float(row["planned_gross_margin_pct"])
        forecast_margin = float(row["current_forecast_margin_pct"])
        contract_value = float(row["contract_value_eur"])
        unbilled_scope = float(row["unbilled_scope_change_eur"])
        overtime = float(row["overtime_cost_eur"])
        rework = float(row["rework_cost_eur"])

        margin_drop = planned_margin - forecast_margin
        implied_margin_value_at_risk = max(margin_drop, 0.0) * contract_value
        observable_leakage = unbilled_scope + overtime + rework
        priority_score = implied_margin_value_at_risk + observable_leakage

        project_findings.append(
            {
                "project_id": row["project_id"],
                "project_name": row["project_name"],
                "planned_margin_pct": round(planned_margin * 100, 1),
                "forecast_margin_pct": round(forecast_margin * 100, 1),
                "margin_drop_pp": round(margin_drop * 100, 1),
                "unbilled_scope_eur": round(unbilled_scope, 2),
                "overtime_eur": round(overtime, 2),
                "rework_eur": round(rework, 2),
                "implied_margin_value_at_risk_eur": round(implied_margin_value_at_risk, 2),
                "observable_leakage_eur": round(observable_leakage, 2),
                "priority_score_eur": round(priority_score, 2),
                "delivery_risk": row["delivery_risk"],
            }
        )

    ranked = sorted(project_findings, key=lambda item: item["priority_score_eur"], reverse=True)
    top = ranked[:4]

    total_unbilled = sum(item["unbilled_scope_eur"] for item in project_findings)
    total_overtime = sum(item["overtime_eur"] for item in project_findings)
    total_rework = sum(item["rework_eur"] for item in project_findings)

    elapsed_ms = (time.perf_counter() - started) * 1000

    executive_answer = (
        "Gross margin is deteriorating despite revenue growth. The strongest public-demo "
        "signals point to project execution and commercial leakage concentrated in a small "
        "number of projects, especially Orion and Helios."
    )

    return {
        "question": "Why did our gross margin fall this month?",
        "company": "Northstar Industrial Systems S.L. (synthetic)",
        "status": "completed",
        "executive_answer": executive_answer,
        "company_metrics": {
            "gross_margin_start": pct(first_margin),
            "gross_margin_latest": pct(latest_margin),
            "gross_margin_change_percentage_points": round(margin_change_pp, 1),
            "revenue_change_pct": round(revenue_change_pct, 1),
            "latest_revenue_eur": round(latest_revenue, 2),
            "latest_gross_profit_eur": round(float(latest["gross_profit_eur"]), 2),
        },
        "portfolio_signals": {
            "total_unbilled_scope_eur": round(total_unbilled, 2),
            "total_overtime_eur": round(total_overtime, 2),
            "total_rework_eur": round(total_rework, 2),
        },
        "priority_projects": top,
        "recommended_actions": [
            "Resolve Orion commercial scope before further unapproved work accumulates.",
            "Put Orion and Helios on formal margin-recovery plans.",
            "Review all active unbilled scope across the portfolio.",
            "Separate supplier inflation from overtime and rework in management reporting.",
        ],
        "limitations": [
            "Priority score is a transparent demo heuristic, not an accounting attribution model.",
            "Exact causal contribution to company margin cannot be proven from this compact dataset alone.",
            "No external LLM or inference endpoint is called by this public executable workflow.",
        ],
        "observability": {
            "workflow_type": "deterministic_public_demo",
            "data_files_read": 2,
            "project_records_analyzed": len(projects),
            "financial_periods_analyzed": len(financials),
            "runtime_ms": round(elapsed_ms, 3),
            "model_calls": 0,
            "input_tokens": 0,
            "output_tokens": 0,
            "estimated_inference_cost_eur": 0.0,
            "note": (
                "Production implementations should record model calls, token counts, cache hits, "
                "endpoint latency, GPU utilization and cost per executive workflow."
            ),
        },
    }


def print_human(packet: dict[str, Any]) -> None:
    cm = packet["company_metrics"]
    ps = packet["portfolio_signals"]

    print("\nAI-Native CEO Copilot — Margin Leakage Demo")
    print("=" * 47)
    print(packet["executive_answer"])
    print()
    print(
        f"Company GM: {cm['gross_margin_start']} -> {cm['gross_margin_latest']} "
        f"({cm['gross_margin_change_percentage_points']:+.1f} pp)"
    )
    print(f"Revenue change over the same window: {cm['revenue_change_pct']:+.1f}%")
    print(
        "Observable portfolio signals: "
        f"{euro(ps['total_unbilled_scope_eur'])} unbilled scope, "
        f"{euro(ps['total_overtime_eur'])} overtime, "
        f"{euro(ps['total_rework_eur'])} rework"
    )

    print("\nPriority projects")
    for index, item in enumerate(packet["priority_projects"], start=1):
        print(
            f"{index}. {item['project_id']} — {item['project_name']}: "
            f"{item['planned_margin_pct']:.1f}% -> {item['forecast_margin_pct']:.1f}% GM, "
            f"priority signal {euro(item['priority_score_eur'])}"
        )

    obs = packet["observability"]
    print("\nObservability")
    print(
        f"{obs['project_records_analyzed']} projects | "
        f"{obs['financial_periods_analyzed']} financial periods | "
        f"{obs['runtime_ms']:.3f} ms | "
        "0 model calls"
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="Run the public deterministic margin-leakage workflow.")
    parser.add_argument("--json", action="store_true", help="Emit JSON instead of the human-readable summary.")
    args = parser.parse_args()

    packet = build_packet()
    if args.json:
        print(json.dumps(packet, indent=2, ensure_ascii=False))
    else:
        print_human(packet)


if __name__ == "__main__":
    main()
