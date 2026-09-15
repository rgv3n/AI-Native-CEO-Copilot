# Materiality Engine

## Purpose

The Materiality Engine decides whether a detected change deserves further investigation, autonomous handling, aggregation, or executive escalation.

It is the main defense against alert fatigue.

## Core question

**Is this change important enough, urgent enough, uncertain enough, or irreversible enough to deserve attention now?**

## Materiality dimensions

A materiality assessment may consider:

- financial impact,
- cash impact,
- margin impact,
- revenue exposure,
- strategic importance,
- customer impact,
- operational disruption,
- legal or regulatory exposure,
- reversibility,
- urgency,
- confidence in the evidence,
- persistence of the signal,
- cross-functional propagation,
- deviation from executive objectives or policy.

## Materiality is contextual

Materiality should not be based on one universal threshold.

Examples:

- EUR25k may be immaterial at company level but material for a small project.
- A 2-day delay may be routine in one workflow but critical for a regulated delivery.
- A small margin decline may become material if it appears across multiple projects simultaneously.

Thresholds therefore belong to the Objective & Policy Contract and business context.

## Evaluation sequence

```text
Detected change
   |
   v
Data quality / freshness check
   |
   v
Objective and policy comparison
   |
   v
Impact + urgency + uncertainty + reversibility
   |
   v
Cross-functional amplification check
   |
   v
Materiality classification
```

## Suggested classifications

- `observe` — retain the signal, no action required.
- `aggregate` — combine with related signals before further evaluation.
- `investigate` — initiate agent investigation.
- `operational_action` — eligible for policy-bounded autonomous handling.
- `management_attention` — requires management review but not necessarily CEO attention.
- `executive_attention` — material enough for executive review or decision.
- `critical_escalation` — immediate escalation due to severity, irreversibility, regulatory exposure, or policy breach.

## Illustrative contract

```json
{
  "signal_id": "SIG-2026-0915-042",
  "business_scope": "project:P001",
  "signal_type": "forecast_margin_deterioration",
  "observed_change": {
    "from": 0.27,
    "to": 0.24
  },
  "materiality": {
    "financial_impact": "high",
    "urgency": "medium",
    "strategic_importance": "high",
    "reversibility": "medium",
    "evidence_confidence": 0.91,
    "cross_functional": true
  },
  "classification": "executive_attention",
  "policy_refs": ["POL-MARGIN-01", "OBJ-GM-2026-Q3"]
}
```

## Avoiding false urgency

The system should explicitly distinguish:

- large but already understood events,
- transient anomalies,
- stale-data artifacts,
- repeated signals already under active management,
- genuinely new changes that alter the decision state.

Repeated notifications without meaningful new evidence should normally be suppressed or summarized.

## Executive principle

The CEO should not be interrupted because something changed.

The CEO should be interrupted because **something changed enough to alter a business decision, risk posture, or strategic objective**.
