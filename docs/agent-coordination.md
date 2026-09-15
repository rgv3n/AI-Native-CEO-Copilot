# Cross-Agent Coordination

## Purpose

Specialized agents should not behave as independent departmental bots.

The company control plane needs a coordination model that lets Finance, Sales, Operations, Strategy and Research work from shared objectives while preserving domain boundaries.

---

## Coordination principle

An agent owns analysis inside its domain.

The orchestrator owns:

- task decomposition,
- dependency management,
- evidence reconciliation,
- conflict detection,
- priority resolution against company objectives,
- escalation.

No individual agent should silently resolve a material cross-functional trade-off outside its authority.

---

## Shared coordination object

Illustrative structure:

```json
{
  "coordination_id": "COORD-2026-09-015",
  "trigger": "project_margin_and_cash_exception",
  "objective_ids": [
    "OBJ-PROTECT-LIQUIDITY",
    "OBJ-RECOVER-MARGIN"
  ],
  "lead_agent": "finance",
  "participating_agents": [
    "finance",
    "operations",
    "sales"
  ],
  "entities": [
    "P002",
    "C003"
  ],
  "questions": [
    "What is the current financial exposure?",
    "What operational work is unapproved?",
    "What commercial action is blocking billing and collection?"
  ],
  "status": "investigating",
  "human_owner": null
}
```

---

## Coordination patterns

### 1. Parallel investigation

Multiple agents investigate the same exception from different domains.

Example:

```text
Finance -> quantify cash exposure
Operations -> quantify scope and delivery impact
Sales -> inspect customer relationship and commercial approvals
```

Useful when the business problem is inherently cross-functional.

### 2. Sequential dependency

One agent's result becomes input to another.

Example:

```text
Operations identifies unapproved scope
        |
        v
Finance estimates margin/cash impact
        |
        v
Sales prepares commercial recovery options
```

### 3. Challenge pattern

A second agent is asked to test a material conclusion.

Example:

```text
Finance hypothesis:
"cash problem is mainly collections"

Operations challenge:
"part of exposure is actually unbilled completed work"
```

The purpose is to reduce single-agent tunnel vision.

### 4. Conflict pattern

Agents reach recommendations that optimize different objectives.

Example:

```text
Sales: protect account relationship
Finance: accelerate payment recovery
Operations: stop additional unapproved work
```

The orchestrator maps the conflict to company priorities and policies.

If the trade-off is not governed, it escalates.

---

## Evidence reconciliation

The system should distinguish:

- corroborating evidence,
- complementary evidence,
- contradictory evidence,
- stale evidence,
- missing evidence.

A cross-agent synthesis should never flatten disagreement into false certainty.

Recommended pattern:

```text
Observed:
P002 has EUR 88k unbilled scope.

Observed:
EUR 260k invoice is 48 days overdue pending scope reconciliation.

Inference:
Commercial scope resolution is likely contributing to delayed collection.

Uncertainty:
The dataset does not prove what fraction of the overdue amount depends directly on the scope dispute.
```

---

## Attention allocation

Agents should not consume unlimited compute or organizational attention.

The orchestrator should allocate investigation depth according to:

- expected business impact,
- strategic priority,
- urgency,
- uncertainty,
- reversibility,
- marginal value of additional evidence,
- inference cost.

A EUR 5k low-risk anomaly should not automatically receive the same investigation depth as a EUR 500k liquidity exposure.

---

## Coordination completion

A coordination task should close only when it reaches one of these states:

- `resolved_autonomously`
- `recommendation_ready`
- `approval_required`
- `blocked_missing_evidence`
- `policy_conflict`
- `failed`

The state should be observable and traceable.

---

## Executive principle

The CEO should not receive five agent outputs.

The CEO should receive one reconciled decision packet that explains:

- what happened,
- why it matters,
- where agents agree,
- where they disagree,
- what the trade-off is,
- what should happen next,
- and whether human authority is required.