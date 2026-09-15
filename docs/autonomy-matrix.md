# Agent Autonomy Matrix

## Purpose

An agentic company should not treat autonomy as binary.

Different activities require different levels of authority, evidence and human control.

This reference defines four autonomy levels.

---

## Level A0 — Observe

The agent may:

- read authorized data,
- monitor metrics,
- detect anomalies,
- compare trends,
- and generate internal findings.

No external action is permitted.

Typical examples:

- detect falling project margin,
- identify overdue receivables,
- flag pipeline stagnation,
- detect supplier deterioration.

Human approval: **not required**.

---

## Level A1 — Investigate and recommend

The agent may:

- coordinate with other agents,
- retrieve additional evidence,
- perform analysis,
- rank risks and opportunities,
- prepare scenarios,
- and recommend next actions.

It may not commit the company to an external action.

Typical examples:

- explain why margin is falling,
- rank collections by expected cash impact,
- recommend which deals need executive attention,
- propose project recovery priorities.

Human approval: **not required for analysis; required before consequential execution**.

---

## Level A2 — Prepare action

The agent may prepare an operational action but not execute it without approval.

Examples:

- draft a customer collection message,
- prepare a revised forecast classification,
- generate a supplier escalation,
- create a proposed project recovery plan,
- prepare a pricing change,
- assemble a management decision package.

Human approval: **required before execution**.

This is often the highest-value autonomy level for early enterprise deployments because it removes coordination work while preserving human authority.

---

## Level A3 — Execute within delegated policy

The agent may execute actions only when all policy conditions are satisfied.

Examples may include:

- create internal tasks,
- request non-sensitive status updates,
- update internal risk flags,
- trigger approved workflow steps,
- send low-risk internal notifications,
- refresh forecasts according to governed rules.

Human approval: **not required per action when authority has already been explicitly delegated**.

The action must still be:

- permissioned,
- traceable,
- reversible where practical,
- observable,
- and bounded by thresholds.

---

## Actions that should normally remain human-controlled

Even in a highly autonomous organization, some decisions should generally remain under explicit human authority.

Examples:

- signing contracts,
- changing strategic pricing,
- approving material expenditure,
- moving significant cash,
- hiring or terminating employees,
- making legal commitments,
- changing credit policy for strategic customers,
- sending sensitive external communications,
- approving acquisitions or major investments,
- overriding governance controls.

The exact boundary depends on the organization, regulation and risk tolerance.

---

## Example functional matrix

| Activity | Finance Agent | Sales Agent | Operations Agent | Strategy Agent | Default autonomy |
|---|---|---|---|---|---|
| Monitor KPIs | Yes | Yes | Yes | Yes | A0 |
| Detect anomalies | Yes | Yes | Yes | Yes | A0 |
| Investigate cause | Yes | Yes | Yes | Yes | A1 |
| Cross-functional synthesis | Yes | Yes | Yes | Yes | A1 |
| Recommend action | Yes | Yes | Yes | Yes | A1 |
| Draft customer communication | Limited | Yes | Limited | No | A2 |
| Prepare forecast correction | Yes | Yes | Limited | Yes | A2 |
| Create internal task | Yes | Yes | Yes | Yes | A3 if delegated |
| Change customer pricing | No | Prepare only | No | Recommend | Human approval |
| Commit company funds | No | No | No | Recommend | Human approval |
| Sign contract | No | No | No | No | Human only |

---

## Decision gates

Before any A2 or A3 action, the system should evaluate a policy intersection such as:

**User authority AND agent authority AND task policy AND tool policy AND business threshold AND approval state**

If any required condition fails, the action is blocked or downgraded to recommendation-only.

---

## Risk dimensions for autonomy

Autonomy should be lower when an action has high:

- financial impact,
- legal impact,
- customer sensitivity,
- irreversibility,
- data sensitivity,
- regulatory exposure,
- ambiguity,
- or reputational risk.

Autonomy can be higher when an action is:

- internal,
- reversible,
- low-value,
- deterministic,
- well-observed,
- policy-bounded,
- and supported by strong evidence.

---

## Recommended adoption path

A practical enterprise progression is:

**A0 → A1 → A2 → selective A3**

Do not begin by maximizing autonomous execution.

Begin by maximizing reliable observation and decision preparation.

Once the organization trusts the evidence, controls, observability and failure behavior, selected workflows can move into delegated execution.

---

## Executive principle

The strategic goal is not a company where AI can do everything without people.

The strategic goal is a company where **human attention is reserved for the decisions where human authority and judgment create the most value**.
