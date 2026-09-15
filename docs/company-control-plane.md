# Autonomous Company Control Plane

## Purpose

The Autonomous Company Control Plane is the governance layer that translates executive intent into policy-bounded agent behavior.

It is not another chatbot and it is not a scheduler that assigns individual tasks manually.

Its job is to let leadership define:

- what the company is trying to achieve,
- what must be protected,
- what trade-offs are acceptable,
- what risks can be tolerated,
- what actions agents may take autonomously,
- what decisions require human authority,
- and what conditions should trigger escalation.

The control plane then gives specialized agents a shared operating context.

---

## Strategic shift

Traditional management often works like this:

```text
CEO sets direction
        |
Managers translate direction into tasks
        |
Teams collect information
        |
People coordinate dependencies
        |
Problems move upward through meetings and reports
        |
Leadership decides
```

The agentic control-plane model looks different:

```text
Leadership defines objectives + policies + constraints
        |
        v
Autonomous Company Control Plane
        |
        +------------------------------+
        |              |               |
        v              v               v
   Finance Agent   Sales Agent   Operations Agent
        |              |               |
        +--------------+---------------+
                       |
                       v
            Shared evidence + state
                       |
                       v
        Detect -> Investigate -> Coordinate
                       |
                       v
              Prioritize exceptions
                       |
          +------------+------------+
          |                         |
          v                         v
Policy-bounded action       Human decision required
```

Leadership no longer needs to explicitly dispatch every analytical task.

Instead, agents operate continuously against a shared set of company objectives and governance rules.

---

## What the control plane contains

### 1. Executive objectives

Examples:

- protect gross margin above a defined threshold,
- prevent cash balance from falling below a minimum buffer,
- prioritize profitable growth over unqualified pipeline volume,
- reduce delivery-risk exposure,
- protect strategic customer relationships,
- improve recurring-revenue mix.

Objectives should be measurable where possible.

### 2. Priorities

Not every objective has equal importance at every moment.

A priority layer allows leadership to say, for example:

1. protect liquidity,
2. recover project margin,
3. preserve critical customer relationships,
4. improve sales conversion,
5. optimize lower-priority operating efficiency.

Agents should use those priorities when allocating attention.

### 3. Policies

Policies define what agents may and may not do.

Examples:

- do not approve discounts above 8%,
- do not change customer payment terms autonomously,
- do not initiate payments,
- do not commit company funds above a delegated threshold,
- do not terminate supplier or customer relationships,
- do not send external communications involving legal exposure without approval.

### 4. Risk tolerances

A control plane should make acceptable risk explicit.

Examples:

```text
maximum project margin deterioration: 5 percentage points
maximum overdue exposure per customer: EUR 150k
minimum treasury buffer: EUR 600k
maximum supplier concentration: 60% of category spend
maximum forecast confidence gap before escalation: 20 percentage points
```

These are organization-specific examples, not universal thresholds.

### 5. Autonomy boundaries

The control plane consumes the autonomy model defined in [`autonomy-matrix.md`](autonomy-matrix.md).

A policy may grant one agent A3 autonomy for a low-risk workflow while restricting another action to A1 or A2.

Example:

```text
Agent: Sales
Action: identify stale opportunities
Autonomy: A3
Allowed: reduce internal priority score
Not allowed: change contractual terms

Agent: Finance
Action: overdue receivable follow-up
Autonomy: A2
Allowed: prepare collection communication
Not allowed: send without approval above defined exposure
```

### 6. Escalation rules

The control plane defines when management should be interrupted.

Examples:

- margin risk exceeds EUR 100k,
- treasury forecast falls below policy buffer,
- a strategic customer becomes high risk,
- multiple agents detect a correlated issue,
- confidence is too low for autonomous action,
- evidence sources materially disagree,
- action would exceed delegated authority.

---

## Company state

The control plane should maintain a compact shared state rather than force every agent to reconstruct the company from scratch.

Illustrative state:

```json
{
  "company_state": {
    "period": "2026-09",
    "strategic_priorities": [
      "protect_liquidity",
      "recover_project_margin",
      "protect_strategic_accounts"
    ],
    "risk_posture": "conservative",
    "cash_buffer_eur": 600000,
    "margin_floor_pct": 0.30,
    "critical_exceptions": [
      "cash_pressure",
      "project_margin_erosion",
      "supplier_dependency"
    ]
  }
}
```

This state does not replace source systems.

It provides a governed executive context for prioritization and routing.

---

## Cross-agent coordination

A major purpose of the control plane is to prevent agents from optimizing their own function in isolation.

Example:

A Sales Agent may prefer to preserve a large account.

A Finance Agent may detect serious payment risk.

An Operations Agent may detect margin erosion caused by scope creep.

The correct executive decision cannot be derived from only one domain.

The control plane therefore allows the orchestrator to evaluate the issue against shared objectives:

```text
Revenue importance
        +
Payment risk
        +
Project margin
        +
Strategic account value
        +
Cash priority
        |
        v
Executive trade-off
```

The purpose is not consensus between agents.

The purpose is evidence-driven resolution against company priorities.

---

## Management by exception

The control plane enables a management-by-exception model.

Leadership should not receive every observation.

A signal becomes an executive exception when one or more conditions are met:

- expected business impact is material,
- policy threshold is breached,
- strategic objective is threatened,
- cross-functional conflict exists,
- autonomous authority is insufficient,
- uncertainty is too high,
- timing makes intervention valuable.

The result should be a smaller number of better executive decisions.

---

## Control-plane decision packet

When an exception reaches leadership, it should arrive as a decision packet rather than a raw alert.

Recommended structure:

```text
ISSUE
What changed?

WHY IT MATTERS
Business impact and objective at risk.

EVIDENCE
What facts support the conclusion?

OPTIONS
What realistic actions are available?

TRADE-OFFS
What does each option improve or damage?

RECOMMENDATION
What should happen next and why?

AUTHORITY
Can agents execute, prepare, or only recommend?

URGENCY
When does the value of intervention begin to decay?
```

---

## Example: Northstar Industrial Systems S.L.

For the synthetic Northstar company, leadership could define:

```text
Priority 1: protect liquidity
Priority 2: recover project margin
Priority 3: preserve strategically valuable customers
Priority 4: improve quality of sales forecast
```

Current evidence then creates correlated exceptions:

- cash declines while receivables rise,
- several active projects show margin erosion,
- unbilled scope contributes to both margin and cash pressure,
- some large opportunities have weak forecast quality,
- supplier concentration creates delivery exposure.

Rather than generate five unrelated reports, the control plane should connect them.

Example executive escalation:

> Liquidity deterioration is becoming the dominant near-term constraint. The fastest controllable levers are collection recovery and conversion of unbilled scope on P001, P002 and P005. P002 also requires commercial intervention because unresolved scope is simultaneously damaging project margin and delaying customer payment.

That is closer to executive control than dashboard reporting.

---

## What the control plane does not mean

It does not mean agents become corporate officers.

It does not mean unrestricted autonomous action.

It does not mean removing legal accountability from humans.

It does not mean every management role disappears.

The design goal is narrower and more practical:

> move recurring observation, investigation, coordination and low-risk execution into a governed machine layer, while preserving human authority where judgment, accountability or material risk requires it.

---

## Architecture principle

The CEO should not have to manage the agents individually.

The CEO should manage:

- objectives,
- policies,
- constraints,
- authority,
- and exceptions.

The control plane manages the operational translation of those instructions into agent behavior.

That is the core idea behind an agentic company operating layer.