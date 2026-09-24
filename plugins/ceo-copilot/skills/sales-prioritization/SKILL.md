---
name: sales-prioritization
description: Rank sales opportunities by where executive attention changes the outcome, challenging CRM probabilities with engagement, activity recency, close-date slippage and strategic value. Use when an executive asks which deals to focus on, whether the forecast or pipeline is real, or which commits are overstated ("¿qué oportunidades priorizo?", "pipeline", "forecast de ventas", "CRM").
---

# Sales Prioritization

Answer **"Which opportunities deserve executive attention?"** without sorting by deal size or trusting CRM probability at face value.

## 1. Find the data

Use the user's CRM export or connected CRM first. State the column mapping. Otherwise use `../../demo-data/` (relative to this skill's directory) and say the answer uses synthetic data.

| Concept | Demo file | Key fields |
|---|---|---|
| Pipeline | `opportunities.csv` | stage, amount, crm_probability, last_activity_date, expected_close_date, close_date_moves, buyer_engagement, strategic_value, forecast_category |
| Account context | `customers.csv` | relationship_health, strategic_importance, avg_payment_delay_days |
| Delivery context | `projects.csv` | open problems with the same customer |
| Signals | `events.csv` | procurement activity, complaints |
| Plan beliefs | `management_assumptions.csv` | pipeline-coverage assumptions |

Compute with code. Use the dataset's as-of date (latest event date) for recency, not today's date, unless the data is live.

## 2. Score probability quality

For each opportunity, compute an **evidence-adjusted probability** that starts from CRM probability and is adjusted by:

- **Buyer engagement:** high raises it, low lowers it sharply
- **Activity recency:** more than 21 days without meaningful activity lowers it; more than 42 days is stale
- **Close-date moves:** each move lowers confidence; 3 or more is a strong warning
- **Stage vs probability consistency:** a high probability at an early stage is suspect
- **Account health:** an open complaint or delivery issue with the same customer is a downside risk

Show the adjustment logic transparently. It is a heuristic, not a statistical model, so say so.

## 3. Separate three different things

- **High-value:** a large contract.
- **High-quality:** the evidence supports progression.
- **Executive-attention:** CEO involvement could materially change the outcome, whether to close a deal, rescue it, or stop wasting forecast on it.

These are often different deals. The ranking is for the third.

## 4. Output

Follow `../../references/response-format.md`. Core table:

| # | Opportunity | € | CRM prob. | Evidence-adjusted | Why it matters | Executive move | Confidence |

Also add:
- **Overstated commits:** deals whose CRM probability is contradicted by evidence, with the forecast € at risk.
- **Pipeline coverage reality check:** weighted pipeline at CRM probability vs at evidence-adjusted probability, compared with the target if known.
- Management assumptions the evidence now contradicts.

## Approval boundary

Recommend outreach or prepare meeting briefs only. Do **not** change CRM probability, forecast category, commercial terms or customer communication without authorisation.

## Demo benchmark (Northstar)

A correct answer puts O007 as a strong near-term close (procurement active, high engagement, date stable), O001 as strategically important with strong sponsor engagement, and O005 as valuable but procurement-immature. It flags **O002** as the clearest overstated commit (75% CRM vs low engagement, ~6 weeks of inactivity, 4 close-date moves), O006 as stale and overvalued, and O004 as a caution because of an existing delivery complaint.
