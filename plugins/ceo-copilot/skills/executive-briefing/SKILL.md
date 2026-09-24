---
name: executive-briefing
description: Produce a one-page CEO briefing of what deserves attention today across margin, cash, pipeline, projects, suppliers and challenged management assumptions, ranked by materiality. Use when an executive asks what to focus on, for a daily or weekly business briefing, or for a company health check ("¿qué merece mi atención hoy?", "resumen ejecutivo", "briefing para el CEO", "estado de la empresa").
---

# Executive Briefing

Answer **"What deserves my attention today?"** in one scannable page. This skill runs a light pass of the four domain skills and merges the results into a single materiality ranking.

## 1. Find the data

Use the user's own data or connected tools first. Otherwise use `../../demo-data/` (relative to this skill's directory) and say the briefing uses synthetic data. Load every available file with code.

## 2. Light pass per domain

Use the logic from the sibling skills, abbreviated:

- **Margin** (`../margin-analysis/SKILL.md`): trend in points; top eroding projects in €.
- **Cash** (`../cash-flow-risk/SKILL.md`): cash vs AR trend; largest overdue or disputed balances.
- **Pipeline** (`../sales-prioritization/SKILL.md`): overstated commits; the one or two deals where CEO involvement matters.
- **Projects** (`../project-risk/SKILL.md`): the top intervention.
- **Suppliers:** critical dependencies with degrading delivery or price.
- **Assumptions:** every row in `management_assumptions.csv` (or equivalent) that current evidence contradicts or puts at risk.

## 3. Rank by materiality

Score each candidate item on:
1. **€ exposure** (margin, cash or revenue at stake)
2. **Urgency** (does waiting a week make it worse or irreversible?)
3. **Executive leverage** (can the CEO personally change the outcome?)
4. **Evidence strength** (Observed > Likely > Needs verification)

Keep the **top 5 only**. Everything else goes into a single "Monitored, no action needed" line.

## 4. Output

Keep it to one screen:

```text
CEO BRIEFING · <company> · as of <date>

THE ONE THING
<single most important item and the decision it needs>

TOP 5 ATTENTION ITEMS
1. <item> · €<exposure> · <urgency> · <move>          [Observed]
...

ASSUMPTIONS UNDER PRESSURE
- "<assumption>" (<owner>) → <status>, because <evidence>

MONITORED, NO ACTION NEEDED
<one line>

CONFIDENCE · SOURCES
```

Offer to drill down with the specific domain skill on any item.

## Approval boundary

A briefing is decision support. Do not execute, send or change anything.
