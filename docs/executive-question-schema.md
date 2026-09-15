# Executive Question Schema

## Purpose

The Executive Question Schema defines the normalized input passed from the executive experience layer to the orchestration layer.

The goal is to avoid treating every CEO request as unstructured chat. A production-grade executive system should convert natural language into an explicit task contract that can be routed, traced, governed and evaluated.

---

## Design principles

1. **Preserve the original question** — never lose the executive's wording.
2. **Separate intent from execution** — the interface captures what the executive wants; the orchestrator decides how to investigate it.
3. **Make business scope explicit** — entity, period, business unit and decision context should be machine-readable where possible.
4. **Declare action boundaries** — analysis and recommendation are different from consequential action.
5. **Carry evidence requirements forward** — the system should know when a claim must be source-grounded.
6. **Support uncertainty** — missing context should be represented explicitly rather than silently invented.

---

## Canonical schema

```json
{
  "question_id": "eq_01J...",
  "original_question": "Why did our gross margin fall this month?",
  "intent": "diagnose_change",
  "decision_domain": ["finance", "operations", "sales"],
  "business_scope": {
    "company": "example_company",
    "business_unit": null,
    "region": null,
    "customer": null,
    "project": null,
    "product": null
  },
  "time_scope": {
    "period": "current_month",
    "comparison_period": "previous_month",
    "as_of": "2026-09-15"
  },
  "requested_output": {
    "type": "executive_analysis",
    "depth": "decision_ready",
    "include_recommendations": true,
    "include_sources": true,
    "include_confidence": true
  },
  "action_policy": {
    "mode": "analysis_only",
    "requires_human_approval": true
  },
  "evidence_policy": {
    "minimum_source_count": 2,
    "allow_external_sources": false,
    "require_structured_data_for_financial_claims": true
  },
  "known_context": {},
  "missing_context": [],
  "priority": "executive",
  "trace_id": "tr_01J..."
}
```

---

## Intent taxonomy

The first implementation should keep the taxonomy small and operationally useful.

### `diagnose_change`

Explain why a business metric changed.

Examples:

- Why did gross margin fall?
- Why did conversion improve?
- Why did project delivery slow down?

### `identify_risk`

Find emerging or material business risks.

Examples:

- Which customers are becoming financially risky?
- Which projects are likely to miss margin targets?
- Where is cash getting trapped?

### `prioritize`

Rank entities or opportunities for executive attention.

Examples:

- Which sales opportunities deserve attention today?
- Which projects should I review first?

### `compare`

Compare periods, business units, customers, projects or scenarios.

### `forecast`

Estimate likely future outcomes with explicit assumptions and uncertainty.

### `scenario_analysis`

Evaluate alternative decisions or operating assumptions.

### `summarize_state`

Produce an executive view of what changed, what matters and what needs attention.

---

## Decision domains

A question may involve one or more domains:

- `finance`
- `sales`
- `operations`
- `strategy`
- `research`
- `cross_functional`

Domains are routing hints, not permission grants. Tool access remains controlled by the agent and policy layers.

---

## Action policy

Every normalized question should declare an action mode.

### `analysis_only`

Read data, reason and recommend. No external state changes.

### `prepare_action`

The system may prepare a draft action, such as a message, workflow payload or approval request, but must not execute it.

### `approved_action`

Execution is allowed only after a separate authorization event has been recorded.

The public reference implementation should default to `analysis_only`.

---

## Missing context

The schema must represent uncertainty explicitly.

Example:

```json
{
  "missing_context": [
    {
      "field": "business_scope.project",
      "reason": "Question refers to 'the project' but no active project is resolved",
      "blocking": true
    }
  ]
}
```

A non-blocking gap may be handled with a documented assumption. A blocking gap should stop the workflow or request clarification.

---

## Example: cash-flow risk

```json
{
  "original_question": "Where is cash getting trapped?",
  "intent": "identify_risk",
  "decision_domain": ["finance", "operations", "sales"],
  "time_scope": {
    "period": "rolling_90_days",
    "comparison_period": "previous_90_days"
  },
  "requested_output": {
    "type": "executive_analysis",
    "depth": "decision_ready",
    "include_recommendations": true,
    "include_sources": true,
    "include_confidence": true
  },
  "action_policy": {
    "mode": "analysis_only",
    "requires_human_approval": true
  }
}
```

---

## Orchestrator handoff

The orchestrator receives the normalized schema and is responsible for:

1. validating required context,
2. selecting agents,
3. building an execution plan,
4. assigning evidence requirements,
5. enforcing permissions,
6. reconciling results,
7. and producing the source-grounded executive response.

The schema does **not** tell the model how to reason. It defines the business task that the system must execute safely and observably.
