# Project Risk Demo

## Executive question

**Which projects are most likely to miss margin or delivery targets?**

This demo tests whether the CEO Copilot can combine schedule, cost, scope, supplier and customer signals into a ranked project-risk view.

## Executive intent

```json
{
  "intent": "identify_risk",
  "decision_domain": ["operations", "finance", "sales"],
  "action_policy": {"mode": "analysis_only", "requires_human_approval": true}
}
```

## Primary data sources

- `demo-data/projects.csv`
- `demo-data/suppliers.csv`
- `demo-data/events.csv`
- `demo-data/invoices.csv`
- `demo-data/customers.csv`

## Workflow

```text
Executive question
      |
      v
Executive Orchestrator
      |
      +--> Operations Agent
      |      - schedule variance
      |      - completion progress
      |      - supplier dependencies
      |      - rework / overtime
      |
      +--> Finance Agent
      |      - forecast margin
      |      - cost-to-date
      |      - unbilled scope
      |
      +--> Sales Agent
             - customer escalation
             - commercial approval blockers
      |
      v
Risk reconciliation
      |
      v
Ranked intervention list
```

## Expected investigation

The workflow should rank risk by business impact rather than simply by the `delivery_risk` field.

It should identify:

- P002 as the most severe combined economic and execution risk because forecast margin has deteriorated sharply, scope expansion remains commercially unresolved, overtime and rework are high, and delivery is slipping,
- P001 as a major margin and schedule risk with material cost pressure, overtime and unbilled changes,
- P005 as a customer-relationship and margin risk because late design changes, a delivery complaint and unbilled scope are interacting,
- P007 as a structurally weak contract with very low forecast margin, repeated rework and customer payment issues,
- P003 as a schedule risk driven by a critical supplier dependency, with margin pressure but better economics than the four cases above,
- P004, P006 and P008 as relatively healthy comparators.

## Supplier dependency

The workflow should connect P003 to S003, where machine-vision components have:

- 68% on-time delivery,
- 19 average delay days,
- 11% year-on-year price inflation,
- and critical dependency status.

This is a useful example of a project risk whose root cause partly sits outside the project team.

## Reasoning discipline

The system should separate:

- **schedule risk**,
- **margin risk**,
- **customer relationship risk**,
- **cash-conversion risk**,
- and **supplier dependency risk**.

A project may be severe on one dimension but not all of them.

## Executive output

The result should provide a ranked intervention list with:

1. project,
2. main risk,
3. financial impact,
4. operational driver,
5. evidence,
6. recommended management action,
7. confidence.

## Approval boundary

The Copilot may recommend recovery actions, resource shifts, supplier escalation or commercial scope resolution. It must not change project commitments, authorize spend, alter contractual terms, replace suppliers or communicate revised delivery dates externally without human approval.
