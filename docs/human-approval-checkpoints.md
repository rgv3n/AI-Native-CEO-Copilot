# Human Approval Checkpoints

## Purpose

AI-Native CEO Copilot is designed to investigate, synthesize and recommend autonomously while preserving human authority over consequential business actions.

The system therefore separates three operating modes:

1. `analysis_only`
2. `prepare_action`
3. `approved_action`

The default public reference behavior is `analysis_only`.

---

## Core principle

> **AI may investigate broadly. Authority to change business state remains explicit.**

A recommendation is not an authorization.

A generated draft is not an executed action.

A high-confidence conclusion is not permission to modify a system of record.

---

## Approval classes

### Class A — No approval required

Read-only investigation and synthesis.

Examples:

- query ERP, CRM or project data within granted permissions,
- calculate financial or operational metrics,
- retrieve supporting documents,
- compare actuals against plan,
- identify anomalies,
- rank risks and opportunities,
- produce an executive briefing,
- recommend next steps.

These actions do not change external business state.

### Class B — Human review before preparation becomes operational

The Copilot may create a draft or proposed change but must not execute it.

Examples:

- draft a customer escalation email,
- draft a supplier escalation,
- propose revised CRM probability,
- prepare a collections plan,
- propose project resource changes,
- prepare a change-order request,
- generate a meeting agenda or decision memo.

The artifact should be clearly marked as proposed and remain outside the system of record until approved.

### Class C — Explicit approval required before execution

Actions that materially change business state, financial exposure, contractual obligations or external commitments.

Examples:

- send customer or supplier communications,
- change payment terms,
- place or remove a credit hold,
- modify CRM forecast category or committed revenue,
- authorize discounts,
- approve change orders,
- authorize spend,
- reallocate material project resources,
- change delivery commitments,
- replace a supplier,
- create or modify accounting records,
- trigger payments,
- sign or accept contractual terms.

### Class D — Restricted / outside autonomous scope

Actions that should remain outside autonomous execution even if technically possible unless an enterprise governance model explicitly permits them.

Examples:

- executive hiring or termination decisions,
- binding legal commitments,
- bank transfers or treasury movements,
- material financing decisions,
- irreversible production-system changes,
- regulatory filings,
- decisions involving sensitive employee matters.

---

## Approval contract

A proposed consequential action should carry an explicit approval object.

```json
{
  "action_id": "act_01J...",
  "action_type": "customer_collection_escalation",
  "requested_by_workflow": "cash_flow_risk",
  "target": {
    "entity_type": "customer",
    "entity_id": "C003"
  },
  "proposed_action": "Escalate the €500k Orion receivable through a joint Finance and Commercial review.",
  "business_reason": "Material overdue exposure linked to unresolved scope reconciliation.",
  "evidence_refs": ["I003", "I004", "P002", "E006"],
  "risk_level": "high",
  "reversible": true,
  "approval_required": true,
  "required_approver_role": "authorized_executive",
  "approval_status": "pending"
}
```

---

## Approval state machine

```text
analysis
   |
   v
recommendation
   |
   v
prepare_action
   |
   v
pending_approval
   |
   +--> rejected --------> closed
   |
   +--> revision_requested --> prepare_action
   |
   +--> approved
            |
            v
       execute action
            |
            v
       verify outcome
            |
            v
          audit
```

Approval must be tied to the specific action payload. Material changes after approval should invalidate the approval and require re-authorization.

---

## Required information before approval

The approver should see:

- proposed action,
- target system or stakeholder,
- expected business impact,
- supporting evidence,
- known uncertainty,
- financial or contractual exposure,
- reversibility,
- and what will happen if no action is taken.

The goal is informed approval, not a generic confirmation button.

---

## Workflow examples

### Margin analysis

Allowed automatically:

- diagnose margin deterioration,
- identify projects contributing to leakage,
- recommend commercial and operational actions.

Approval required:

- approve change-order pricing,
- alter customer terms,
- authorize additional project spend,
- commit to a revised delivery plan.

### Cash-flow risk

Allowed automatically:

- rank overdue receivables,
- identify collection blockers,
- prepare an escalation plan.

Approval required:

- contact customers,
- alter payment terms,
- apply a credit hold,
- modify accounting records.

### Sales prioritization

Allowed automatically:

- challenge CRM probabilities,
- rank executive-attention opportunities,
- recommend forecast adjustments.

Approval required:

- change CRM commit status,
- change pricing,
- send executive outreach,
- approve concessions.

### Project risk

Allowed automatically:

- rank project risks,
- identify cost and schedule drivers,
- recommend recovery actions.

Approval required:

- move significant resources,
- authorize additional spend,
- replace a supplier,
- modify contractual commitments,
- communicate a new delivery date externally.

---

## Audit requirements

Every approved action should record:

- who approved it,
- when it was approved,
- the exact payload approved,
- evidence visible at approval time,
- execution result,
- any execution error,
- verification result,
- and trace ID linking the action to the originating executive question.

---

## Failure behavior

If approval status is unclear, missing or expired, the system must fail closed and remain in `prepare_action` mode.

If the requested action exceeds the user's permissions, the system must not attempt execution even if another agent recommends it.

If evidence materially changes after approval but before execution, the system should pause and request re-approval.

---

## Enterprise implementation

Real organizations should map these approval classes to their own RBAC, delegation-of-authority, financial controls and regulatory requirements.

Production approval workflows, system-of-record integrations and governance design may form part of a private enterprise implementation through **Rubén García / [companiesautomation.com/en](https://companiesautomation.com/en)**.
