# Executive Signal Routing

## Purpose

Executive Signal Routing determines who should receive a material signal, in what form, and at what urgency.

The system should not route every important event to the CEO.

It should route each signal to the lowest appropriate level of authority that can resolve it safely.

## Routing hierarchy

```text
Signal
  |
  v
Can an agent resolve it inside delegated policy?
  | yes
  v
Autonomous handling + audit
  |
  no
  v
Can functional management resolve it?
  | yes
  v
Manager / functional owner
  |
  no
  v
Does it require cross-functional executive judgment?
  | yes
  v
Executive Decision Packet
  |
  no
  v
Observe / aggregate / close
```

## Routing dimensions

Routing may depend on:

- materiality classification,
- business scope,
- required authority,
- financial threshold,
- legal or regulatory constraints,
- customer or supplier importance,
- reversibility,
- urgency,
- owner availability,
- current decision state,
- whether the issue is already being managed.

## Signal destinations

Possible destinations include:

- autonomous agent workflow,
- Finance owner,
- Sales owner,
- Operations owner,
- Strategy owner,
- cross-functional management review,
- CEO / executive committee,
- restricted human authority such as Legal, HR or Treasury.

## Executive attention budget

Executive attention is scarce.

The routing layer should therefore optimize for:

- fewer but better escalations,
- consolidation of related signals,
- suppression of duplicates,
- prioritization by economic and strategic consequence,
- explicit deadlines when delay destroys value.

## Executive inbox concept

Instead of a chronological alert feed, the executive experience should resemble a prioritized decision queue.

Each item should show:

- what changed,
- why it matters,
- estimated exposure,
- urgency,
- confidence,
- what has already been investigated,
- available options,
- recommended next action,
- approval or decision required.

## Example

```text
PRIORITY 1 — Cash exposure
Orion Mobility Components
EUR500k unpaid across two invoices.
One invoice is 48 days overdue.
Commercial scope reconciliation remains unresolved.

Why now:
Cash balance has fallen from EUR1.18M to EUR680k while receivables increased to EUR1.51M.

System action already completed:
Finance, Sales and Operations evidence reconciled.

Decision required:
Approve joint executive collection intervention or maintain current process.
```

## Routing principle

**Do not route information upward merely because it is interesting. Route it upward when higher authority or judgment is required to change the outcome.**
