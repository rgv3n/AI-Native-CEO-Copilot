# Executive Golden Questions

## Purpose

The Executive Golden Questions are the stable benchmark set for AI-Native CEO Copilot.

They are designed to evaluate whether the system can transform fragmented company data into grounded, decision-oriented executive intelligence.

The benchmark tests more than answer quality. It exercises orchestration, tool selection, evidence coverage, prioritization, uncertainty, forecasting and cross-functional synthesis.

## Evaluation dimensions

Each question should eventually be scored on:

1. Correctness
2. Grounding and provenance
3. Relevant data coverage
4. Prioritization
5. Causal discipline
6. Actionability
7. Uncertainty handling
8. Data freshness
9. Execution efficiency
10. Executive clarity

## Difficulty

- **Level 1 — Single-domain intelligence:** primarily one business function.
- **Level 2 — Cross-functional diagnosis:** requires evidence from multiple functions.
- **Level 3 — Executive synthesis:** requires trade-offs, ranking, forecasting or scenario reasoning across the company.

## Golden Question Set

| ID | Executive question | Intent | Level | Primary domains |
|---|---|---|---:|---|
| GQ-01 | Why did our gross margin fall this month? | `diagnose_change` | 2 | finance, operations, sales |
| GQ-02 | Where is cash getting trapped? | `identify_risk` | 2 | finance, sales, operations |
| GQ-03 | Which customers are generating revenue but destroying profitability? | `identify_risk` | 2 | finance, sales, operations |
| GQ-04 | Where are we deviating materially from budget, and why? | `diagnose_change` | 2 | finance, operations |
| GQ-05 | What will our cash position look like in 30, 60 and 90 days if current behavior continues? | `forecast` | 3 | finance, sales, operations |
| GQ-06 | Which sales opportunities deserve executive attention today? | `prioritize` | 2 | sales |
| GQ-07 | Why did our win rate decline this quarter? | `diagnose_change` | 2 | sales, strategy |
| GQ-08 | Which opportunities in the pipeline are most likely overstated? | `identify_risk` | 2 | sales |
| GQ-09 | Which customers show early signs of churn or relationship deterioration? | `identify_risk` | 2 | sales, finance, operations |
| GQ-10 | Are we likely to hit this quarter's revenue target, and what could cause us to miss it? | `forecast` | 3 | sales, finance |
| GQ-11 | Which projects are most likely to miss their margin targets? | `identify_risk` | 2 | operations, finance |
| GQ-12 | Which projects are most likely to miss their delivery dates? | `forecast` | 2 | operations |
| GQ-13 | Where are the main operational bottlenecks hurting the business right now? | `identify_risk` | 2 | operations, finance |
| GQ-14 | Where are scope changes creating margin leakage? | `diagnose_change` | 2 | operations, finance, sales |
| GQ-15 | Which suppliers create the greatest operational or financial risk? | `identify_risk` | 2 | operations, finance |
| GQ-16 | If we had an additional €1M to invest, where would it create the highest expected business value? | `scenario_analysis` | 3 | strategy, finance, sales, operations |
| GQ-17 | Which products or services should we consider stopping, fixing or repricing? | `prioritize` | 3 | strategy, finance, sales, operations |
| GQ-18 | What would likely happen if we increased prices by 10%? | `scenario_analysis` | 3 | strategy, sales, finance |
| GQ-19 | Which assumptions in our current operating plan are being contradicted by the latest data? | `identify_risk` | 3 | strategy, finance, sales, operations |
| GQ-20 | Are we growing in a way that actually improves enterprise value? | `diagnose_change` | 3 | strategy, finance, sales |
| GQ-21 | What deserves my attention today? | `prioritize` | 3 | cross-functional |
| GQ-22 | What changed in the business since yesterday that actually matters? | `summarize_state` | 3 | cross-functional |
| GQ-23 | What are the three biggest threats to this quarter's EBITDA? | `identify_risk` | 3 | finance, sales, operations, strategy |
| GQ-24 | Where are we losing money without realizing it? | `identify_risk` | 3 | cross-functional |
| GQ-25 | Which management assumptions are contradicted by the data? | `diagnose_change` | 3 | cross-functional |
| GQ-26 | What should the leadership team discuss first this week? | `prioritize` | 3 | cross-functional |
| GQ-27 | If nothing changes, what is most likely to hurt us in the next 90 days? | `forecast` | 3 | finance, sales, operations, strategy |
| GQ-28 | What important opportunity are we currently underestimating? | `identify_risk` | 3 | strategy, sales, finance, research |
| GQ-29 | Which unresolved management decisions are currently costing us the most? | `prioritize` | 3 | cross-functional |
| GQ-30 | Give me the five things I need to know before I start the week. | `summarize_state` | 3 | cross-functional |

## Benchmark contract

A Golden Question is not successfully answered merely because the prose sounds plausible.

Each benchmark case should progressively define:

```text
Question
  -> required data sources
  -> expected relevant facts
  -> acceptable inferences
  -> unsupported claims that must not be made
  -> expected risks/opportunities surfaced
  -> confidence requirements
  -> source-grounded executive response
```

## Dataset-first evaluation

The synthetic company dataset is built backwards from these questions.

The data should therefore contain:

- multiple competing explanations for important changes,
- cross-functional dependencies,
- leading and lagging indicators,
- stale or incomplete records,
- misleading but plausible signals,
- real business trade-offs,
- and irrelevant noise.

The objective is not to reward keyword matching. The objective is to require evidence-driven executive reasoning.

## Public vs. private benchmark

This repository contains the public benchmark and a representative synthetic company.

A richer enterprise evaluation layer may remain private or be made available selectively through **Rubén García / [companiesautomation.com/en](https://companiesautomation.com/en)**. That layer may include additional hidden cases, adversarial scenarios, production evaluation criteria, customer-specific datasets and infrastructure benchmarks.
