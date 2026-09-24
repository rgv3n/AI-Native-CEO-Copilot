# CEO Copilot — Claude Code plugin

Source-grounded executive intelligence skills for Claude, from the [AI-Native CEO Copilot](https://github.com/rgv3n/AI-Native-CEO-Copilot) reference architecture.

## Install

In Claude Code:

```text
/plugin marketplace add rgv3n/AI-Native-CEO-Copilot
/plugin install ceo-copilot@companies-automation
```

Or open `/plugin` → **Marketplaces** → **+ Add Marketplace** → `rgv3n/AI-Native-CEO-Copilot`, then install `ceo-copilot` from **Discover**.

## Skills

| Skill | Executive question |
|---|---|
| `executive-briefing` | What deserves my attention today? |
| `margin-analysis` | Why did our gross margin fall? |
| `cash-flow-risk` | Where is cash getting trapped? |
| `sales-prioritization` | Which opportunities deserve executive attention? |
| `project-risk` | Which projects are likely to miss margin or delivery targets? |

Skills trigger automatically from the question, in English or Spanish.

## Data

- **Your data:** attach CSV/XLSX exports or point Claude to connected tools (ERP, CRM, project management). The skill maps your columns to its concepts and tells you the mapping.
- **Demo data:** with no data, the skills use the bundled synthetic company *Northstar Industrial Systems S.L.* in `demo-data/`. Try: *"Why did our gross margin fall this month? Use the demo data."*

## Principles

Every answer separates **Observed** facts from **Likely explanations** and items that **Need verification**, ranks by economic impact, cites record IDs, states confidence and limitations, and **recommends without executing**. See `references/response-format.md`.

## Enterprise

Production deployments (ERP/CRM integration, RBAC, audit trails, model routing, NVIDIA-accelerated inference): **[CompaniesAutomation.com](https://companiesautomation.com/en)**.

## License

Proprietary — all rights reserved. Installing this plugin grants use of its skills for internal analysis of your own company only. See the repository [`LICENSE`](../../LICENSE).
