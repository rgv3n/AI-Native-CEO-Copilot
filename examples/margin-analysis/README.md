# Margin Analysis Demo

## Executive question

> **Why did our gross margin fall this month?**

This workflow demonstrates how AI-Native CEO Copilot should investigate a cross-functional executive question using the synthetic Northstar Industrial Systems S.L. dataset.

The objective is not to generate a plausible explanation from a single financial metric. The system must gather evidence across finance, project delivery and commercial context, distinguish facts from inference, rank the drivers by business impact and return a decision-oriented answer.

---

## Golden Question

- **Benchmark:** GQ-01
- **Intent:** `diagnose_change`
- **Difficulty:** Level 2 — cross-functional diagnosis
- **Primary domains:** finance, operations, sales
- **Action mode:** `analysis_only`

---

## Normalized executive question

```json
{
  "original_question": "Why did our gross margin fall this month?",
  "intent": "diagnose_change",
  "decision_domain": ["finance", "operations", "sales"],
  "business_scope": {
    "company": "Northstar Industrial Systems S.L."
  },
  "time_scope": {
    "period": "2026-09",
    "comparison_period": "2026-08",
    "trend_window": "2026-04_to_2026-09",
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
  }
}
```

---

## Why this requires orchestration

The financial statement shows **that** margin is deteriorating. It does not fully explain **why**.

The orchestrator therefore needs evidence from multiple domains:

```text
CEO question
    |
    v
Executive Orchestrator
    |
    +--> Finance Agent
    |      - quantify margin trend
    |      - identify size of deterioration
    |      - identify whether revenue or cost is the primary movement
    |
    +--> Operations Agent
    |      - inspect project forecast margins
    |      - inspect overtime and rework
    |      - inspect procurement and delivery risk
    |      - identify unbilled scope changes
    |
    +--> Sales / Commercial context
           - inspect discounting and commercial approval gaps
           - identify scope accepted before pricing or billing
    |
    v
Evidence reconciliation
    |
    v
Ranked causal drivers
    |
    v
Source-grounded executive answer
```

---

## Required data sources

### `demo-data/monthly_financials.csv`

Used to establish the company-level trend.

Relevant signals:

- April gross margin: **36.0%**
- August gross margin: **29.5%**
- September estimate: **27.5%**
- revenue continues to increase while gross profit declines
- direct costs are growing materially faster than revenue

The deterioration is therefore not primarily a demand problem. The first-order signal is worsening delivery economics and cost absorption.

### `demo-data/projects.csv`

Used to identify project-level sources of margin erosion.

Important projects include:

#### P001 — Helios Line 7 Automation

- planned margin: **32%**
- current forecast margin: **24%**
- unbilled scope change: **€62k**
- overtime: **€38k**
- rework: **€24k**
- delivery risk: high

#### P002 — Orion EV Component Cell

- planned margin: **33%**
- current forecast margin: **19%**
- unbilled scope change: **€88k**
- overtime: **€52k**
- rework: **€31k**
- delivery risk: high

This is the strongest individual project-level margin warning in the dataset.

#### P005 — NovaGlass Furnace Controls

- planned margin: **29%**
- current forecast margin: **21%**
- unbilled scope change: **€27k**
- overtime: **€29k**
- rework: **€18k**

#### P007 — Delta Water SCADA Retrofit

- planned margin: **18%**
- current forecast margin: **11%**
- unbilled scope change: **€16k**
- overtime: **€25k**
- rework: **€22k**

P007 also demonstrates a portfolio-mix problem: even the planned economics were weak before execution deterioration.

### `demo-data/events.csv`

Used for current evidence and causal confirmation.

Relevant recent events include:

- P001 margin forecast cut from 27% to 24% after updated drive pricing and overtime forecast.
- P002 received additional engineering work while commercial approval remained unresolved.
- P005 continued implementation while a scope change remained unbilled.
- P007 recorded another rework incident.
- component pricing from a critical supplier increased 11% year on year.

---

## Investigation plan

### Step 1 — Confirm the financial movement

The Finance Agent should answer:

- How large is the margin decline?
- Is revenue falling?
- Is gross profit falling?
- Are direct costs increasing faster than revenue?
- Is this a one-month anomaly or a multi-month trend?

Expected conclusion:

> Gross margin deterioration is a multi-month trend, not a September-only anomaly.

---

### Step 2 — Identify projects with material margin variance

The Operations Agent should compare:

```text
planned gross margin
vs.
current forecast gross margin
```

It should prioritize large projects and absolute economic impact rather than simply listing every negative variance.

Expected high-priority projects:

1. P002 — Orion EV Component Cell
2. P001 — Helios Line 7 Automation
3. P005 — NovaGlass Furnace Controls
4. P007 — Delta Water SCADA Retrofit

---

### Step 3 — Decompose the drivers

The system should group causes into reusable business categories rather than returning a project-by-project dump.

Expected categories:

#### A. Unpriced / unbilled scope expansion

Several delivery teams are performing customer-requested work before full commercial approval or billing.

This creates direct margin leakage and may also delay cash collection.

#### B. Overtime and rework

High-risk projects are absorbing significant additional labor and quality costs.

#### C. Material and supplier cost inflation

P001 and P003 contain procurement pressure, and recent supplier events confirm higher component pricing.

#### D. Portfolio mix

P007 started with only an 18% planned margin. More revenue from structurally low-margin work can reduce aggregate company margin even before execution problems appear.

---

## Causal discipline

The workflow must not say:

> "Supplier inflation caused the entire margin decline."

The evidence does not support a single-cause conclusion.

The correct framing is closer to:

> Margin deterioration appears to be driven by a combination of unbilled scope expansion, overtime/rework, material cost pressure and unfavorable project mix, concentrated in a small number of projects.

The workflow should clearly distinguish:

- **verified facts** from the data,
- **supported inference** from cross-source evidence,
- **unknown contribution** where exact cost attribution is not available.

---

## Expected executive structure

The final response should contain:

1. **Executive answer** — one concise conclusion.
2. **Magnitude** — how much margin changed.
3. **Top drivers** — ranked, not merely enumerated.
4. **Projects requiring attention** — focus on economically material cases.
5. **Business impact** — what happens if no action is taken.
6. **Recommended actions** — specific management actions.
7. **Confidence and limitations** — what is known and what still needs verification.
8. **Evidence** — traceable dataset sources.

See [`expected-output.md`](expected-output.md) for the benchmark reference response.

---

## Recommended executive actions

The workflow should be able to support recommendations such as:

1. **Commercially resolve P002 scope immediately.** Stop accepting additional engineering work without signed commercial treatment.
2. **Recover or explicitly write off unbilled change work.** P001, P002, P005 and P007 deserve immediate review.
3. **Run margin recovery plans on P001 and P002.** These are large projects with material forecast-margin deterioration.
4. **Review low-margin contract acceptance.** P007 indicates a structural pricing / contract-quality problem as well as an execution problem.
5. **Separate material inflation from execution leakage.** Procurement cost pressure and internal rework should not be managed as the same problem.

These are recommendations, not automatically executable actions.

---

## Evaluation checks

A successful implementation should:

- detect the multi-month margin decline,
- not misdiagnose falling revenue as the cause,
- identify P002 and P001 as major drivers,
- identify unbilled scope, overtime/rework and cost inflation,
- recognize portfolio mix as an additional factor,
- avoid claiming exact causal percentages without evidence,
- produce traceable evidence,
- and prioritize actions economically.

A response that only says "costs increased" should fail the benchmark.

---

## Enterprise implementation

This public example demonstrates the architectural pattern using synthetic data.

Real margin intelligence requires mapping each company's project accounting, revenue recognition, change-order process, procurement data and commercial definitions.

For production implementation, agentic architecture or NVIDIA AI infrastructure design: **Rubén García / [companiesautomation.com/en](https://companiesautomation.com/en)**.
