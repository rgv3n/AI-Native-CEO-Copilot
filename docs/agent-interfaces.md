# Agent Interfaces

## Purpose

This document defines the contract between the Executive Orchestrator and specialized domain agents.

The objective is to make agents bounded, inspectable and replaceable. Each agent should behave like a typed service with an explicit responsibility, tool boundary, evidence obligation and output contract.

---

## Core interface

```json
{
  "agent": "finance",
  "task_id": "task_01J...",
  "trace_id": "tr_01J...",
  "objective": "Explain the drivers of gross-margin decline for the current month",
  "business_scope": {},
  "time_scope": {},
  "inputs": {},
  "allowed_tools": [],
  "evidence_requirements": {},
  "constraints": {},
  "deadline_ms": 15000
}
```

Agents return a structured result rather than a free-form answer.

```json
{
  "task_id": "task_01J...",
  "agent": "finance",
  "status": "completed",
  "findings": [],
  "evidence": [],
  "assumptions": [],
  "risks": [],
  "recommended_followups": [],
  "confidence": 0.88,
  "execution": {
    "tool_calls": 4,
    "latency_ms": 3280
  }
}
```

---

## Shared requirements

Every agent should:

- stay inside its domain scope,
- use only explicitly permitted tools,
- prefer evidence over unsupported inference,
- distinguish facts from hypotheses,
- expose assumptions,
- return confidence as a calibrated signal rather than decoration,
- avoid consequential actions unless an approval event exists,
- and return enough provenance for the orchestrator to audit the result.

---

## Finance Agent

### Responsibilities

- gross margin and contribution margin,
- profitability,
- revenue and direct cost analysis,
- receivables and payables,
- cash conversion,
- project economics,
- budget variance,
- customer concentration,
- and financial risk.

### Typical tools

- ERP read APIs,
- accounting database queries,
- invoice and receivables data,
- project-cost data,
- finance warehouse views.

### Must not

- modify ledger entries,
- initiate payments,
- change budgets,
- or execute financial actions without a separate approved-action workflow.

---

## Sales Agent

### Responsibilities

- pipeline analysis,
- opportunity quality,
- conversion and velocity,
- account prioritization,
- sales forecast quality,
- discounting patterns,
- customer activity,
- and commercial risk.

### Typical tools

- CRM read APIs,
- sales activity data,
- pricing and quote data,
- customer history,
- pipeline snapshots.

### Must not

- change opportunity stages,
- send messages to prospects,
- change pricing,
- or commit forecasts without approval.

---

## Operations Agent

### Responsibilities

- project delivery,
- capacity and utilization,
- delays,
- materials,
- suppliers and subcontractors,
- process bottlenecks,
- operational cost drivers,
- and delivery risk.

### Typical tools

- project-management systems,
- ERP operational modules,
- inventory systems,
- supplier data,
- scheduling systems.

---

## Strategy Agent

### Responsibilities

- cross-functional synthesis,
- scenario comparison,
- executive prioritization,
- goal alignment,
- trade-off analysis,
- and strategic implications.

The Strategy Agent should consume grounded findings from other agents rather than recreate domain analysis from scratch when evidence already exists.

---

## Research Agent

### Responsibilities

- external market intelligence,
- competitor research,
- regulatory context,
- technology shifts,
- and macro or sector context.

External evidence should be clearly separated from internal company facts.

---

## Agent status model

Allowed status values:

- `completed`
- `partial`
- `blocked`
- `failed`

`partial` means the agent produced useful findings but could not satisfy all evidence requirements.

`blocked` means the task cannot proceed safely or correctly without missing context, access or approval.

---

## Finding contract

Each finding should be atomic and evidence-linked.

```json
{
  "finding_id": "f_001",
  "statement": "Direct material cost increased 11.8% month over month",
  "type": "fact",
  "impact": "high",
  "evidence_refs": ["ev_004", "ev_005"],
  "confidence": 0.98
}
```

Supported types:

- `fact`
- `inference`
- `hypothesis`
- `risk`
- `opportunity`

The orchestrator should not present a hypothesis as a fact.

---

## Coordination pattern

For a cross-functional question, the orchestrator may dispatch agents in parallel:

```text
Executive Orchestrator
       |
       +--> Finance Agent ------+
       +--> Sales Agent --------+--> Evidence reconciliation
       +--> Operations Agent ---+
```

The orchestrator owns conflict resolution. Specialized agents do not silently overwrite one another's findings.

---

## Failure behavior

An agent should fail explicitly when:

- a required system is unavailable,
- the requested operation exceeds its permission scope,
- required evidence cannot be obtained,
- inputs are internally inconsistent,
- or a safety/policy boundary is reached.

A useful failure response includes what failed, what evidence is missing and whether a narrower analysis is still possible.
