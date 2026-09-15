# Escalation & Exception Handling

## Purpose

An agentic company should not escalate everything.

It should escalate only when business impact, uncertainty, policy, authority or timing make human attention valuable.

This document defines a reference model for deciding what becomes an executive exception.

---

## Exception criteria

A signal should be considered for escalation when one or more of the following is true:

- material financial impact,
- strategic objective at risk,
- policy threshold breached,
- delegated authority exceeded,
- cross-functional conflict detected,
- evidence materially disagrees,
- confidence falls below policy minimum,
- issue is time-sensitive,
- issue is difficult to reverse,
- external legal or reputational exposure exists.

---

## Severity is not enough

High severity does not always mean high executive priority.

A useful exception score should consider:

```text
Expected impact
+ Strategic importance
+ Urgency
+ Irreversibility
+ Cross-functional scope
+ Authority gap
+ Uncertainty
```

The output should remain interpretable rather than pretending to produce mathematically perfect priority.

---

## Escalation levels

### E0 — No escalation

The agent can resolve or monitor inside policy.

### E1 — Informational

The issue is visible to management but requires no immediate decision.

### E2 — Management attention

A manager should review the recommendation or prepared action.

### E3 — Executive decision

A material trade-off, authority boundary or strategic issue requires executive judgment.

### E4 — Critical executive intervention

Immediate attention is required because delay may materially damage liquidity, legal position, strategic relationships, safety or business continuity.

---

## Exception packet

Every E2+ escalation should contain:

```text
EXCEPTION
What changed?

IMPACT
What is the estimated business exposure?

OBJECTIVE AT RISK
Which executive objective or policy is affected?

ROOT CAUSE
What is known versus inferred?

OPTIONS
What realistic actions exist?

RECOMMENDATION
What is the preferred option and why?

AUTHORITY GAP
Why can the agent not complete the action autonomously?

DEADLINE
By when does a decision retain most of its value?

EVIDENCE
Which sources support the conclusion?
```

---

## Deduplication

The same underlying business problem may trigger multiple agents.

Example:

- Finance detects overdue receivables.
- Operations detects unapproved scope.
- Sales detects customer friction.

If all three relate to P002 / C003, the control plane should generate one coordinated exception rather than three disconnected alerts.

---

## Escalation suppression

Repeated alerts can destroy trust.

The system should suppress or aggregate exceptions when:

- nothing material has changed,
- the issue is already assigned,
- leadership has explicitly accepted the risk,
- the next useful review point has not arrived,
- new evidence does not change the recommendation.

Suppression must remain auditable.

---

## Re-escalation

An accepted or deferred exception should re-escalate if:

- impact crosses a new threshold,
- expected resolution date is missed,
- confidence changes materially,
- new contradictory evidence appears,
- a previously independent issue becomes correlated,
- a policy or objective changes.

---

## Example: Northstar

Illustrative exception:

```text
Exception: P002 Orion EV Component Cell
Level: E3 — Executive decision

Observed:
- forecast margin has fallen from 33% to 19%,
- EUR 88k of scope remains unbilled,
- EUR 260k is 48 days overdue,
- additional engineering work continues without resolved commercial approval.

Objectives at risk:
- protect liquidity,
- recover project margin,
- preserve strategic accounts.

Conflict:
- stopping work protects margin,
- aggressive collection may damage account relationship,
- continuing work without scope approval increases economic exposure.

Decision required:
Choose the commercial recovery posture and define whether additional unapproved scope should pause.
```

This is what the CEO should see — not a dashboard with five red indicators.

---

## Core principle

The purpose of escalation is not to keep leadership informed about everything.

The purpose is to route scarce human judgment to the small number of situations where human authority produces the highest value.