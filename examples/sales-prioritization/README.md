# Sales Prioritization Demo

## Executive question

**Which sales opportunities deserve executive attention today?**

The demo tests whether the Copilot can challenge CRM probabilities and prioritize opportunities using engagement, strategic value, recency and forecast quality rather than sorting only by deal size.

## Executive intent

```json
{
  "intent": "prioritize",
  "decision_domain": ["sales", "strategy"],
  "action_policy": {"mode": "analysis_only", "requires_human_approval": true}
}
```

## Primary data sources

- `demo-data/opportunities.csv`
- `demo-data/customers.csv`
- `demo-data/events.csv`
- `demo-data/projects.csv`

## Workflow

```text
Executive question
      |
      v
Executive Orchestrator
      |
      +--> Sales Agent
      |      - stage and amount
      |      - buyer engagement
      |      - activity recency
      |      - close-date movement
      |      - CRM probability
      |
      +--> Strategy Agent
             - strategic value
             - customer context
             - concentration / relationship implications
      |
      v
Forecast-quality challenge
      |
      v
Executive attention ranking
```

## Expected investigation

The workflow should not equate high CRM probability with high-quality opportunity.

It should identify:

- O007 as a strong near-term opportunity because procurement is active, engagement is high and the close date has not moved,
- O001 as strategically important with strong sponsor engagement,
- O005 as potentially valuable because technical validation has progressed and engagement is high, while noting procurement maturity,
- O002 as the clearest overstated commit because its 75% probability conflicts with low engagement, stale activity and four close-date moves,
- O006 as stale and probably overvalued relative to its activity history,
- O004 as requiring caution because an existing delivery complaint may affect the new sale.

## Prioritization logic

Executive attention should be based on a combination of:

1. economic value,
2. probability quality rather than CRM probability alone,
3. urgency / close timing,
4. strategic importance,
5. executive intervention value,
6. downside or relationship risk.

## Reasoning discipline

The Copilot should distinguish between:

**High-value opportunity:** large potential contract.

**High-quality opportunity:** evidence supports progression.

**Executive-attention opportunity:** CEO involvement could materially change the outcome.

Those are not necessarily the same deals.

## Approval boundary

The system may recommend executive outreach or prepare meeting briefs, but it must not change CRM probability, commit category, commercial terms or customer communication without authorization.
