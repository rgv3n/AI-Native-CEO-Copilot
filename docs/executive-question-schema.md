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

The first implementation should keep the taxonomy small and operationally useful. The goal is to support many executive questions through a compact set of reusable intents rather than creating one intent per use case.

### `diagnose_change`

Explain why a business metric changed.

Examples:

- Why did gross margin fall?
- Why did conversion improve?
- Why did project delivery slow down?
- Why did customer acquisition cost increase?
- Why did cash conversion deteriorate?

### `identify_risk`

Find emerging or material business risks.

Examples:

- Which customers are becoming financially risky?
- Which projects are likely to miss margin targets?
- Where is cash getting trapped?
- Which suppliers are creating delivery exposure?
- Which accounts show early signs of churn?

### `prioritize`

Rank entities or opportunities for executive attention.

Examples:

- Which sales opportunities deserve attention today?
- Which projects should I review first?
- Which overdue invoices should finance escalate first?
- Which customers deserve an executive intervention?
- Which operational bottlenecks have the highest business impact?

### `compare`

Compare periods, business units, customers, projects or scenarios.

Examples:

- Which business unit improved profitability the most this quarter?
- How does customer profitability differ by segment?
- Which projects are materially underperforming their original assumptions?

### `forecast`

Estimate likely future outcomes with explicit assumptions and uncertainty.

Examples:

- What will month-end cash look like if collections continue at the current pace?
- Are we likely to hit the quarterly revenue target?
- Which projects are likely to exceed budget before completion?

### `scenario_analysis`

Evaluate alternative decisions or operating assumptions.

Examples:

- What happens to EBITDA if supplier costs increase by 8%?
- What happens to cash runway if the top three overdue invoices slip by 30 days?
- What is the expected impact of hiring five additional salespeople?

### `summarize_state`

Produce an executive view of what changed, what matters and what needs attention.

Examples:

- What changed in the business since yesterday?
- What are the three issues I should care about this morning?
- Give me a weekly executive summary of margin, cash, pipeline and delivery risk.

---

## Representative executive use cases

The schema should support a broad set of executive decisions without changing its core structure.

### Finance

| Executive question | Primary intent | Typical domains |
|---|---|---|
| Why did gross margin fall this month? | `diagnose_change` | finance, operations, sales |
| Where is cash getting trapped? | `identify_risk` | finance, operations, sales |
| Which customers are hurting profitability? | `identify_risk` | finance, sales |
| Which invoices are most likely to become overdue? | `forecast` | finance, sales |
| What will our cash position look like in 30, 60 and 90 days? | `forecast` | finance |
| Which cost categories are growing faster than revenue? | `diagnose_change` | finance |
| Where are we deviating materially from budget? | `compare` | finance, operations |

### Sales and customer intelligence

| Executive question | Primary intent | Typical domains |
|---|---|---|
| Which opportunities deserve executive attention today? | `prioritize` | sales |
| Why did our win rate decline? | `diagnose_change` | sales |
| Which accounts show early churn risk? | `identify_risk` | sales, finance |
| Which pipeline opportunities are overstated? | `identify_risk` | sales |
| Which customers have the highest expected lifetime value? | `prioritize` | sales, finance |
| Which customer segments are becoming less profitable? | `diagnose_change` | sales, finance |
| Are we likely to hit the quarter's revenue target? | `forecast` | sales, finance |

### Operations and delivery

| Executive question | Primary intent | Typical domains |
|---|---|---|
| Which projects are likely to miss margin targets? | `identify_risk` | operations, finance |
| Which projects are likely to miss delivery dates? | `forecast` | operations |
| Where are our main operational bottlenecks? | `identify_risk` | operations |
| Which suppliers are creating the most risk? | `identify_risk` | operations, finance |
| Why did delivery performance deteriorate this month? | `diagnose_change` | operations |
| Which projects need executive intervention? | `prioritize` | operations, finance |
| Where are scope changes creating margin leakage? | `diagnose_change` | operations, finance, sales |

### Strategy

| Executive question | Primary intent | Typical domains |
|---|---|---|
| Which business unit is creating the most enterprise value? | `compare` | strategy, finance |
| Where should we allocate the next €1M of investment? | `scenario_analysis` | strategy, finance |
| Which products or services should we stop selling? | `prioritize` | strategy, finance, sales |
| Which markets offer the best risk-adjusted growth opportunity? | `scenario_analysis` | strategy, research |
| What assumptions in our current plan are becoming invalid? | `identify_risk` | strategy, research |
| What is the expected impact of a 10% price increase? | `scenario_analysis` | strategy, sales, finance |

### Cross-functional executive intelligence

These are especially important because they demonstrate why an executive copilot needs orchestration across multiple specialized agents rather than a single-domain assistant.

| Executive question | Primary intent | Typical domains |
|---|---|---|
| What deserves my attention today? | `prioritize` | cross_functional |
| What changed in the business since yesterday? | `summarize_state` | cross_functional |
| What are the three biggest threats to this quarter's EBITDA? | `identify_risk` | finance, sales, operations, strategy |
| Where are we losing money without realizing it? | `identify_risk` | finance, operations, sales |
| Which problems are locally small but strategically dangerous? | `identify_risk` | strategy, cross_functional |
| Which management assumptions are contradicted by the data? | `diagnose_change` | cross_functional |
| What should the leadership team discuss first this week? | `prioritize` | cross_functional |
| If nothing changes, what is most likely to hurt us in the next 90 days? | `forecast` | finance, sales, operations, strategy |

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

## Example: cross-functional executive priority

```json
{
  "original_question": "What deserves my attention today?",
  "intent": "prioritize",
  "decision_domain": ["cross_functional"],
  "time_scope": {
    "period": "current_state",
    "comparison_period": "previous_business_day"
  },
  "requested_output": {
    "type": "executive_briefing",
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
    "allow_external_sources": false
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
