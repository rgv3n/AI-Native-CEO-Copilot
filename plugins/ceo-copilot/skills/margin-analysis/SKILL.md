---
name: margin-analysis
description: Diagnose why gross margin changed, rank the causal drivers by economic impact and recommend recovery actions with cited evidence. Use when a CEO, CFO or founder asks why margin fell or rose, where profitability is leaking, or which projects or customers are eroding margin ("¿por qué ha caído el margen?", "margen bruto", "rentabilidad").
---

# Margin Analysis

Answer **"Why did our gross margin change?"** with a ranked, source-grounded diagnosis, not a generic "costs went up".

## 1. Find the data

Use the user's own data first: attached files, paths they give, or connected finance/ERP/project tools. Map their columns to the concepts below and state the mapping in one line.

If no company data is available, or the user asks for a demo, use the synthetic company in `../../demo-data/` (relative to this skill's directory): Northstar Industrial Systems S.L. Say clearly that the answer uses synthetic demo data.

| Concept | Demo file | Key fields |
|---|---|---|
| Company trend | `monthly_financials.csv` | revenue, direct_costs, gross_profit, gross_margin_pct |
| Project economics | `projects.csv` | planned vs current_forecast_margin_pct, unbilled_scope_change, overtime_cost, rework_cost, contract_value |
| Commercial context | `opportunities.csv`, `customers.csv` | discounting, customer gross_margin_pct |
| Supplier cost | `suppliers.csv` | price_change_yoy_pct, dependency_level |
| Recent signals | `events.csv` | entity_id, severity, summary |
| Management beliefs | `management_assumptions.csv` | assumption, status |

Load files with code (Python/pandas) and compute the numbers. Do not estimate figures by eye.

## 2. Investigate in this order

1. **Confirm the movement.** Margin change in points over the period and the trend window. Is revenue falling, or are direct costs growing faster than revenue? Is this a one-month anomaly or a multi-month trend?
2. **Find material project variance.** For each project, compute margin-point erosion (planned minus forecast) and the absolute euro impact (erosion × contract value). Prioritise by euros, not by percentage alone.
3. **Decompose into business drivers** (group causes, don't dump projects):
   - A. Unpriced or unbilled scope expansion
   - B. Overtime and rework
   - C. Material and supplier cost inflation
   - D. Portfolio mix (work that was low-margin even at plan)
   - E. Discounting or pricing concessions, if the data shows it
4. **Cross-check with events** to confirm causes and find what changed recently.
5. **Challenge assumptions.** If a management assumption (e.g. "margin will stay above 32%") is contradicted, say so with the evidence.

## 3. Causal discipline

- Never state a single cause when several contribute.
- Never assign exact % contribution per driver unless cost attribution data supports it. Say "a material portion" and explain what data would allow exact attribution.
- Label every finding: Observed / Likely explanation / Needs verification.

## 4. Output

Follow `../../references/response-format.md`. Include:

1. Executive answer (margin change in points plus the top 2–3 drivers)
2. A "What changed" table (start, previous and current period: revenue, direct costs, gross profit, margin)
3. Ranked drivers
4. Projects needing attention: project, planned → forecast margin, unbilled scope, overtime + rework, € at risk
5. Business impact if nothing changes
6. Recommended actions, e.g. resolve unapproved scope commercially, recover or explicitly write off unbilled change work, run margin-recovery plans on the top projects, review acceptance of low-margin contracts, and manage supplier inflation separately from execution leakage
7. Confidence and limitations
8. Evidence (file → record IDs)

## Demo benchmark (self-check on Northstar data)

A correct answer on the demo data detects the multi-month decline (36.0% in April → 27.5% September estimate) while revenue *rises*. It ranks P002 Orion and P001 Helios as the main drivers, names P005 and P007, identifies unbilled scope, overtime/rework, supplier inflation and portfolio mix, and does **not** blame falling revenue or claim exact percentages.

Recommend only. Do not change records or contact anyone.
