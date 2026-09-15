# Source-Grounded Executive Response Format

## Purpose

The CEO Copilot should not return an unstructured model answer for material business questions.

This document defines a response contract that separates facts, interpretation, recommendations, uncertainty and evidence so an executive can understand not only **what the system thinks**, but **why**.

---

## Design goals

A strong executive response should be:

- concise enough to scan,
- deep enough to support a decision,
- grounded in traceable evidence,
- explicit about uncertainty,
- clear about business impact,
- and separated from any consequential action.

---

## Canonical response

```json
{
  "response_id": "resp_01J...",
  "question_id": "eq_01J...",
  "trace_id": "tr_01J...",
  "status": "completed",
  "executive_summary": "Gross margin fell primarily because direct material costs increased and two large projects absorbed unplanned subcontractor expense.",
  "key_findings": [],
  "business_impact": [],
  "recommendations": [],
  "risks_and_uncertainty": [],
  "evidence": [],
  "confidence": 0.89,
  "freshness": {},
  "approval_required": false
}
```

---

## Executive summary

The executive summary should answer the question directly in one to three sentences.

It should not begin with process language such as:

> I analyzed your data...

Prefer:

> Gross margin fell 4.2 points this month. Roughly two-thirds of the decline is explained by higher direct material costs and subcontractor overruns in Projects A17 and B04.

The summary should distinguish measured facts from interpretation.

---

## Key findings

Each finding is atomic and evidence-linked.

```json
{
  "finding_id": "f_001",
  "statement": "Direct material cost increased 11.8% month over month",
  "type": "fact",
  "impact": "high",
  "direction": "negative",
  "evidence_refs": ["ev_004", "ev_005"],
  "confidence": 0.98
}
```

Supported finding types:

- `fact`
- `inference`
- `hypothesis`
- `risk`
- `opportunity`

A user-facing renderer may label these as **Observed**, **Likely explanation**, **Needs verification**, **Risk** and **Opportunity**.

---

## Business impact

Findings should be translated into decision-relevant consequences where possible.

```json
{
  "impact_id": "bi_001",
  "statement": "If the current cost pattern continues, full-quarter gross margin would finish approximately 2.6 points below plan",
  "basis": "scenario_projection",
  "evidence_refs": ["ev_004", "ev_009"],
  "confidence": 0.76
}
```

Forecasts and scenarios must not be presented as observed facts.

---

## Recommendations

Recommendations should be prioritized, bounded and connected to evidence.

```json
{
  "recommendation_id": "rec_001",
  "priority": 1,
  "action": "Review subcontractor overruns in Projects A17 and B04 before approving additional scope",
  "expected_value": "high",
  "urgency": "this_week",
  "evidence_refs": ["ev_011", "ev_012"],
  "requires_approval": false
}
```

Recommendations are decision support. They are not authorization to execute external actions.

---

## Evidence object

```json
{
  "evidence_id": "ev_004",
  "label": "September direct material cost",
  "source_type": "structured_system",
  "system": "erp",
  "dataset": "project_costs",
  "record_ids": ["A17:2026-09", "B04:2026-09"],
  "retrieved_at": "2026-09-15T12:40:00Z",
  "freshness": "current",
  "transformation": "monthly aggregation"
}
```

Evidence references should be stable within the response so every material claim can point back to its support.

---

## Confidence

Confidence should reflect evidence quality and analytical certainty, not model self-assurance.

Recommended interpretation:

- `0.90–1.00` — strong direct evidence with high consistency,
- `0.75–0.89` — good evidence with limited assumptions,
- `0.50–0.74` — useful but materially uncertain,
- `<0.50` — insufficient for a decision-ready conclusion.

Confidence should be reduced when:

- source coverage is incomplete,
- data is stale,
- sources conflict,
- important assumptions are unverified,
- or the conclusion depends heavily on forecasting.

---

## Freshness

```json
{
  "freshness": {
    "as_of": "2026-09-15T12:40:00Z",
    "oldest_material_source": "2026-09-14T23:59:00Z",
    "stale_sources": []
  }
}
```

Executives should be able to tell whether an answer represents the business now, yesterday or last month.

---

## Partial answers

A partial response is preferable to fabricated completeness.

```json
{
  "status": "partial",
  "executive_summary": "Receivables indicate that cash is increasingly concentrated in three overdue accounts, but supplier-payment timing could not be validated because the payables system was unavailable.",
  "risks_and_uncertainty": [
    {
      "type": "missing_evidence",
      "statement": "Accounts payable data was unavailable",
      "impact": "Cash-conversion analysis is incomplete"
    }
  ]
}
```

---

## Human-readable rendering

A user interface can render the structured response as:

```text
EXECUTIVE ANSWER
Gross margin fell 4.2 points this month...

WHAT CHANGED
1. Material cost +11.8%                [Observed]
2. Subcontractor overruns in A17/B04  [Observed]
3. Customer mix contributed ~0.7 pts  [Likely]

BUSINESS IMPACT
Quarter margin is at risk of finishing ~2.6 pts below plan.

RECOMMENDED NEXT MOVE
1. Review A17/B04 scope and subcontractor overruns this week.
2. Validate purchasing variance on the top five material categories.

UNCERTAINTY
September contains two days of unposted supplier invoices.

SOURCES
ERP project costs · CRM contracts · Operations project status
```

This format is intentionally different from a generic chat answer. It is designed for executive consumption, verification and follow-up action.

---

## Evaluation criteria

A response can be evaluated on:

- answer relevance,
- evidence coverage,
- factual consistency,
- source freshness,
- separation of fact and inference,
- recommendation usefulness,
- confidence calibration,
- latency,
- and cost per executive workflow.

These metrics provide the bridge between application quality and infrastructure observability.
