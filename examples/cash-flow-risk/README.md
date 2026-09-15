# Cash-Flow Risk Demo

## Executive question

**Where is cash getting trapped?**

This demo exercises the CEO Copilot's ability to connect receivables, collections, project execution and commercial disputes rather than treating cash as a finance-only problem.

## Executive intent

```json
{
  "intent": "identify_risk",
  "decision_domain": ["finance", "sales", "operations"],
  "action_policy": {"mode": "analysis_only", "requires_human_approval": true}
}
```

## Primary data sources

- `demo-data/monthly_financials.csv`
- `demo-data/invoices.csv`
- `demo-data/projects.csv`
- `demo-data/customers.csv`
- `demo-data/events.csv`

## Workflow

```text
Executive question
      |
      v
Executive Orchestrator
      |
      +--> Finance Agent
      |      - AR trend
      |      - overdue balances
      |      - expected collections
      |      - cash trajectory
      |
      +--> Sales Agent
      |      - customer relationship signals
      |      - disputes / payment commitments
      |
      +--> Operations Agent
             - unbilled scope
             - delayed milestones
             - delivery issues affecting collections
      |
      v
Evidence reconciliation
      |
      v
Ranked cash traps + confidence + actions
```

## Expected investigation

The Finance Agent should establish that cash is deteriorating while receivables rise. It should identify the largest overdue or disputed balances and distinguish between normal open invoices and genuinely trapped cash.

The Sales Agent should determine whether delayed collections are purely administrative or linked to customer dissatisfaction, commercial disputes or weak payment behavior.

The Operations Agent should inspect whether delivery issues, scope changes or unbilled work are preventing invoicing or collection.

## Key evidence patterns

The workflow should surface, at minimum:

- cash balance declining from €1.18M in April to €680k in September while AR rises from €980k to €1.51M,
- Orion exposure across I003 and I004, with €500k unpaid and scope reconciliation involved,
- Delta Water exposure across I009 and I010, with €215k overdue and repeated missed promises,
- Helios I001 with €100k still outstanding and linked to change-order discussion,
- NovaGlass I007 with €80k outstanding while a delivery complaint remains open,
- unbilled scope changes in active projects that delay conversion of work into cash.

## Reasoning discipline

The Copilot should distinguish:

**Fact:** an invoice is overdue or partially paid.

**Inference:** the associated operational or commercial issue is likely contributing to delayed collection.

**Not justified:** claiming a customer will default unless supported by stronger evidence.

## Executive output

The answer should rank cash traps by materiality and urgency, explain the operational/commercial causes where supported, and recommend actions without automatically contacting customers or changing payment terms.

## Approval boundary

The system may recommend or prepare:

- a collections escalation,
- a customer meeting,
- accelerated commercial approval for scope changes,
- or revised invoicing actions.

It must not send communications, renegotiate terms, suspend a customer or alter accounting records without explicit human approval.
