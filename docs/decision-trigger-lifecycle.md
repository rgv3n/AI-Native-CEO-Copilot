# Decision Trigger Lifecycle

## Purpose

A Decision Trigger is the point at which a monitored business change becomes important enough to enter a decision workflow.

It connects continuous monitoring with the Executive Decision Engine.

## Lifecycle

```text
signal_detected
   |
   v
validated
   |
   v
materiality_assessed
   |
   +---- immaterial ----> observed / aggregated / closed
   |
   v
investigation_opened
   |
   v
cross_functional_evidence_reconciled
   |
   v
decision_triggered
   |
   v
decision_packet_built
   |
   v
routed_to_authority
   |
   +---- autonomous policy ----> execute -> verify
   |
   +---- human authority ------> approve/reject/revise
   |
   v
outcome_measured
   |
   v
learning_recorded
```

## Trigger conditions

A decision trigger may occur when one or more of the following is true:

- a policy threshold is breached,
- a company objective becomes materially at risk,
- expected economic value changes enough to reorder priorities,
- new evidence invalidates an existing management assumption,
- a previously acceptable risk becomes unacceptable,
- delay materially increases downside or destroys opportunity value,
- an autonomous workflow reaches its delegated authority limit,
- conflicting cross-functional objectives require executive judgment.

## Trigger contract

```json
{
  "trigger_id": "DT-2026-0915-007",
  "signal_refs": ["SIG-042", "SIG-047"],
  "objective_refs": ["OBJ-GM-2026-Q3"],
  "policy_refs": ["POL-MARGIN-01"],
  "business_scope": "project:P001",
  "decision_required": true,
  "decision_deadline": "2026-09-17T12:00:00+02:00",
  "reason": "Forecast margin below tolerance with unresolved commercial scope",
  "materiality": "executive_attention",
  "required_authority": "executive",
  "trace_id": "TRACE-CEO-0915-104"
}
```

## State changes matter

The system should not keep reopening the same decision unless the decision state materially changes.

Examples of meaningful change:

- exposure increases,
- confidence changes materially,
- a new option appears,
- an assumption is invalidated,
- deadline moves closer,
- policy boundary is crossed,
- expected value ranking changes.

## Decision closure

A trigger is not complete merely because a human clicked approve or reject.

Closure should include:

- chosen option,
- authority and timestamp,
- execution status,
- expected outcome,
- verification criteria,
- actual outcome when available,
- variance from expected outcome,
- lessons for future routing or recommendation logic.

## Learning loop

Decision history can improve future executive intelligence by helping the system understand:

- which signals actually mattered,
- which recommendations created value,
- which thresholds were too sensitive,
- where decisions arrived too late,
- which assumptions repeatedly failed,
- which interventions were reversible or costly.

This learning should inform future prioritization without silently changing governance policy.

Policy changes remain explicit and auditable.

## Executive principle

A mature agentic system should not optimize for the number of insights produced.

It should optimize for **how early it can identify a decision that matters, how well it can prepare that decision, and how little unnecessary management attention it consumes**.
