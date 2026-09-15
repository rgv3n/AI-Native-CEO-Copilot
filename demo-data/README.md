# Synthetic Company Dataset

## Purpose

This dataset provides a small, coherent synthetic company for testing AI-Native CEO Copilot.

The dataset is intentionally designed from the Executive Golden Questions backwards. It contains enough interconnected financial, sales and operational signals to require real cross-functional reasoning rather than simple lookup.

All companies, customers, projects, opportunities, suppliers, amounts and events are fictional.

---

## Synthetic company

**Company:** Northstar Industrial Systems S.L. (Synthetic company with realistic synthetic dataset)  
**Business:** B2B engineering and industrial automation projects  
**Headquarters:** Madrid, Spain  
**Employees:** 78  
**Annual revenue run rate:** approximately €11M  
**Business model:** project-based engineering, implementation and recurring support  
**Primary markets:** Spain, Portugal and France

The company sells industrial automation, systems integration and maintenance services to mid-market and enterprise customers.

---

## Dataset files

- `customers.csv` — customer economics and relationship signals
- `projects.csv` — active and recently completed project performance
- `invoices.csv` — receivables, collections and payment behavior
- `opportunities.csv` — CRM pipeline and forecast quality
- `suppliers.csv` — supplier dependency, delays and cost pressure
- `monthly_financials.csv` — company-level monthly financial performance
- `management_assumptions.csv` — management beliefs and operating-plan assumptions
- `events.csv` — recent business events and weak signals

---

## Embedded business conditions

The dataset intentionally contains several overlapping conditions.

### Margin deterioration

Gross margin is declining, but there is no single cause. The relevant contributors include:

- material cost inflation,
- unbilled scope changes,
- discounting on selected deals,
- overtime and rework,
- and an unfavorable project mix.

### Cash trapped in working capital

Cash is constrained by:

- two materially overdue customers,
- milestone invoices that have not yet been issued,
- one large project with slower-than-planned collections,
- and supplier payment terms that are shorter than customer payment terms.

### Pipeline quality risk

The CRM contains opportunities that look healthy at headline level but have conflicting signals such as:

- repeated close-date movement,
- long inactivity,
- weak buyer engagement,
- unusually optimistic probabilities,
- and concentration in one large deal.

### Project delivery risk

Some projects are reported as broadly on track while underlying data indicates:

- procurement delays,
- rising overtime,
- material shortages,
- unresolved scope changes,
- and margin erosion.

### Supplier concentration

One supplier has strong spend concentration and worsening delivery performance, creating both schedule and cost exposure.

### Management assumptions under pressure

Several operating-plan assumptions are no longer fully supported by current data.

The benchmark expects the Copilot to challenge those assumptions with evidence rather than simply repeat management beliefs.

---

## Design principles

1. **Cross-functional links matter.** A customer may appear in invoices, projects, opportunities and events.
2. **The obvious answer is not always the correct answer.** Some records are deliberately noisy or stale.
3. **Current state and historical trend both matter.** Monthly data provides context for recent changes.
4. **Grounding is required.** Important conclusions should cite specific records or sources.
5. **Uncertainty should remain visible.** Not every risk is fully proven.
6. **The dataset is a benchmark asset, not a production model.** Real deployments require organization-specific schemas and controls.

---

## Public and private evaluation layers

This public dataset is deliberately compact and understandable.

A richer enterprise evaluation layer may include larger datasets, hidden benchmark cases, adversarial conditions, production observability, customer-specific schemas and infrastructure performance tests.

For enterprise implementation or evaluation design, contact **Rubén García / [companiesautomation.com/en](https://companiesautomation.com/en)**.
