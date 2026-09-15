# Objective & Policy Contract

## Purpose

The Objective & Policy Contract is the machine-readable layer that converts executive intent into operational constraints for the agent system.

It answers four questions:

1. What is the company trying to optimize?
2. What must never be violated?
3. What trade-offs are acceptable?
4. When must the system escalate to a human?

---

## Canonical contract

Illustrative structure:

```json
{
  "objective_id": "OBJ-2026-Q3-001",
  "name": "Protect near-term liquidity",
  "owner": "CEO",
  "priority": 1,
  "status": "active",
  "time_horizon": "90_days",
  "target": {
    "metric": "cash_balance_eur",
    "operator": ">=",
    "value": 600000
  },
  "supporting_metrics": [
    "accounts_receivable_eur",
    "days_sales_outstanding",
    "overdue_receivables_eur",
    "unbilled_scope_eur"
  ],
  "allowed_tradeoffs": [
    "defer_low_priority_capex",
    "increase_collection_attention"
  ],
  "prohibited_tradeoffs": [
    "breach_customer_contract",
    "misrepresent_financial_information"
  ],
  "autonomy_policy": {
    "observe": "A3",
    "investigate": "A3",
    "recommend": "A3",
    "prepare_action": "A2",
    "execute_financial_commitment": "A0"
  },
  "escalation": {
    "cash_below_eur": 600000,
    "forecast_cash_below_eur": 500000,
    "single_customer_overdue_exposure_eur": 150000,
    "confidence_below": 0.70
  }
}
```

This is a reference pattern, not a universal enterprise schema.

---

## Objective types

Useful objective classes include:

- financial resilience,
- profitable growth,
- margin protection,
- cash conversion,
- customer retention,
- operational delivery,
- supplier resilience,
- working-capital optimization,
- strategic initiative execution,
- risk reduction.

Each objective should have an explicit owner and time horizon.

---

## Priority model

Priority should reflect executive importance, not merely alert severity.

A recommended approach is:

```text
Priority = Strategic importance
         + Time sensitivity
         + Expected business impact
         + Reversibility
         + Executive attention required
```

The system should avoid pretending this is mathematically precise where leadership judgment is required.

Priority values are governance inputs, not model-generated truth.

---

## Policy categories

### Financial policy

Examples:

- payment authority,
- discount limits,
- credit terms,
- cash-buffer rules,
- write-off authority,
- procurement approval thresholds.

### Commercial policy

Examples:

- approved pricing bands,
- minimum margin,
- strategic-account treatment,
- proposal approval,
- contract exceptions.

### Operational policy

Examples:

- project tolerance bands,
- schedule-risk thresholds,
- supplier substitution limits,
- quality escalation rules.

### Data policy

Examples:

- sources an agent may access,
- sensitive fields,
- geographic boundaries,
- retention,
- export restrictions.

### Communication policy

Examples:

- what can remain internal,
- what can be drafted,
- what may be sent autonomously,
- which external messages require review.

---

## Conflicting objectives

Real companies have conflicting objectives.

For example:

```text
Protect cash
vs
Preserve strategic customer

Maximize gross margin
vs
Win strategic market share

Reduce inventory
vs
Protect delivery reliability
```

The system must not hide these conflicts.

If policy does not resolve the trade-off, it should escalate the decision explicitly.

Recommended output:

```text
OBJECTIVE CONFLICT
Protecting liquidity favors accelerated collection.
Protecting the strategic account favors a softer commercial approach.

Decision required from: CEO / CFO
Reason: no governing policy defines which objective dominates for this account.
```

---

## Policy inheritance

Policies can be hierarchical:

```text
Company policy
   |
   +-- Finance policy
   |
   +-- Sales policy
   |
   +-- Operations policy
   |
   +-- Business-unit policy
   |
   +-- Workflow-specific policy
```

The effective policy should be the intersection of all applicable constraints.

A lower-level policy may be more restrictive, but should not silently override a higher-level prohibition.

---

## Expiration and review

Objectives and policies should not live forever by default.

Recommended metadata:

- effective_from,
- review_date,
- expires_at,
- policy_owner,
- approved_by,
- version,
- change_reason.

This matters because an agent acting under stale policy can be more dangerous than an agent with no autonomy.

---

## Decision principle

Agents should optimize only inside declared objectives and policies.

When those instructions are missing, contradictory or stale, the system should reduce autonomy and escalate rather than invent governance.