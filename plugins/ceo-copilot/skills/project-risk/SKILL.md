---
name: project-risk
description: Rank active projects by likelihood and business impact of missing margin or delivery targets, combining schedule, cost, scope, supplier and customer signals into an intervention list. Use when an executive asks which projects are at risk, which will run late or over budget, or where to intervene ("¿qué proyectos están en riesgo?", "riesgo operativo", "retrasos", "sobrecostes").
---

# Project Risk

Answer **"Which projects are most likely to miss margin or delivery targets?"** Rank by business impact, not by the self-reported `delivery_risk` flag.

## 1. Find the data

Use the user's project/PMO/ERP exports or connected tools first, and state the column mapping. Otherwise use `../../demo-data/` (relative to this skill's directory) and say the answer uses synthetic data.

| Concept | Demo file | Key fields |
|---|---|---|
| Projects | `projects.csv` | contract_value, planned vs actual cost, completion_pct, planned vs forecast margin, planned vs forecast end date, unbilled_scope_change, overtime, rework, delivery_risk |
| Suppliers | `suppliers.csv` | on_time_delivery_pct, avg_delay_days, price_change_yoy_pct, dependency_level |
| Customer | `customers.csv`, `invoices.csv` | relationship_health, overdue amounts on the project |
| Signals | `events.csv` | procurement delays, rework incidents, complaints, unresolved approvals |

Compute with code.

## 2. Score five separate risk dimensions per project

A project can be severe on one dimension and fine on others. Keep them separate:

1. **Margin risk:** forecast margin erosion in points and €; cost-to-date vs completion (burn ahead of progress?)
2. **Schedule risk:** days of slip (forecast end − planned end)
3. **Customer relationship risk:** complaints, escalations, relationship health
4. **Cash-conversion risk:** unbilled scope and overdue invoices tied to the project
5. **Supplier dependency risk:** critical suppliers with poor on-time delivery or strong price inflation. Link project → supplier through notes and events.

Then produce an overall ranking weighted by € impact. Show the weighting.

## 3. Output

Follow `../../references/response-format.md`. Core **ranked intervention list**:

| # | Project | Main risk | € impact | Operational driver | Evidence | Recommended management action | Confidence |

Also add:
- A short "healthy comparators" line naming projects that look fine, so the CEO knows they were checked.
- Root causes that sit *outside* the project team (e.g. a supplier), called out separately.

## Approval boundary

Recommend recovery plans, resource shifts, supplier escalation or commercial scope resolution. Do **not** change project commitments, authorise spend, alter contracts, replace suppliers or communicate revised dates externally without human approval.

## Demo benchmark (Northstar)

A correct answer ranks P002 Orion as the most severe (margin 33% → 19%, unresolved scope, heavy overtime/rework, slipping delivery), then P001 Helios (margin and schedule, material cost, unbilled change), P005 NovaGlass (late design changes plus a complaint plus unbilled scope) and P007 Delta Water (structurally weak contract, repeated rework, payment issues). It flags P003 as a schedule risk driven by supplier **S003** (68% on-time, 19-day average delay, +11% YoY price, critical dependency). P004, P006 and P008 are the healthy comparators.
