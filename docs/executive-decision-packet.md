# Executive Decision Packet

## Purpose

The Executive Decision Packet is the standard output produced when an issue requires leadership attention.

It should be compact enough for an executive to act on, but structured enough to remain traceable and auditable.

## Required fields

```yaml
decision_id:
trace_id:
trigger:
decision_class:
decision_owner:
decision_deadline:

executive_question:
observed_state:
materiality:

objective:
constraints:

options:
  - option_id:
    description:
    expected_upside:
    expected_downside:
    key_risks:
    dependencies:
    reversibility:
    estimated_time_to_effect:
    confidence:
    evidence_refs:

recommended_option:
recommendation_reason:

no_action_scenario:
uncertainties:
assumptions:

approval_required:
required_approver_role:
next_step_if_approved:
verification_metric:
```

## Executive view

The human-facing packet should normally fit this pattern:

### DECISION REQUIRED
What must be decided and by when.

### WHY NOW
The material change or risk that triggered the decision.

### OBJECTIVE
What the company is optimizing for.

### OPTIONS
Two to four realistic alternatives.

### RECOMMENDATION
The preferred option and why.

### TRADE-OFFS
What improves and what is sacrificed.

### IF WE DO NOTHING
Expected consequence of maintaining the current path.

### UNCERTAINTY
What is not yet known and what could change the recommendation.

### APPROVAL
Who has authority to decide or execute.

## Design rules

- Do not manufacture alternatives merely to produce a list.
- Do not hide a dominant option if the evidence strongly favors it.
- Do not express false precision in financial outcomes.
- Separate observed facts from modeled scenarios.
- Every material recommendation should link back to evidence.
- Confidence should reflect evidence quality and scenario uncertainty, not model confidence.
- If the evidence is insufficient, return a decision-deferral recommendation and specify what evidence is missing.

## Example packet

### DECISION REQUIRED
Should Northstar continue accepting additional unapproved scope on Orion project P002?

### WHY NOW
P002 is forecast at 19% gross margin versus 33% planned, has unresolved scope, €88k of unbilled changes and material schedule slippage.

### OBJECTIVE
Protect project economics and cash conversion without unnecessarily damaging a strategic customer relationship.

### OPTIONS

**A — Continue current operating behavior**

Low immediate relationship friction, but continued exposure to margin erosion and unbilled work.

**B — Require commercial approval before additional discretionary scope**

Improves economic control and creates a forcing function for scope resolution, with some customer-friction risk.

**C — Full commercial escalation and temporary scope freeze**

Strongest financial protection, but higher relationship and delivery risk.

### RECOMMENDATION
Prepare Option B for executive approval, with a joint Finance + Sales + Operations customer plan.

### IF WE DO NOTHING
The current evidence suggests further work may increase unbilled exposure and deepen project-margin deterioration.

### UNCERTAINTY
The exact customer response and recoverability of current scope changes remain uncertain.

### APPROVAL
Any customer-facing scope restriction, pricing change or contract interpretation requires an authorized human approver.

## Relationship to observability

Each Decision Packet should be linked to its workflow trace so an authorized reviewer can inspect:

- source data,
- agent findings,
- tool calls,
- scenario assumptions,
- model invocations,
- cost and latency,
- approval events,
- final execution and verification.
