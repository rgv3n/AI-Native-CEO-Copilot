# Tool Contracts

## Purpose

Tool contracts define how agents access enterprise systems safely and predictably.

A tool is not just a function call. In an executive AI system it is a governed interface to business data or business actions. Each tool must therefore declare its purpose, inputs, outputs, permissions, failure modes and audit metadata.

---

## Design principles

1. **Read and write paths are separate** — analytical access must not imply permission to change business state.
2. **Least privilege by default** — agents receive only the tools required for the current task.
3. **Typed inputs and outputs** — avoid ambiguous free-form calls where structured contracts are possible.
4. **Every call is traceable** — tool invocations carry task and trace identifiers.
5. **Failures are explicit** — timeout, authorization, validation and upstream failures must be distinguishable.
6. **Evidence is first-class** — read tools should return source metadata that can be attached to findings.

---

## Canonical tool definition

```json
{
  "tool_name": "erp.get_project_margin",
  "version": "1.0",
  "mode": "read",
  "domain": "finance",
  "description": "Returns revenue, direct cost and gross margin for one or more projects",
  "required_permissions": ["erp:finance:read"],
  "input_schema": {},
  "output_schema": {},
  "timeout_ms": 5000,
  "pii": false,
  "audit_required": true
}
```

---

## Canonical invocation

```json
{
  "tool_call_id": "tc_01J...",
  "trace_id": "tr_01J...",
  "task_id": "task_01J...",
  "agent": "finance",
  "tool": "erp.get_project_margin",
  "arguments": {
    "project_ids": ["PRJ-1042"],
    "period": "2026-09"
  }
}
```

---

## Canonical result

```json
{
  "tool_call_id": "tc_01J...",
  "status": "success",
  "data": {
    "project_id": "PRJ-1042",
    "revenue": 184000,
    "direct_cost": 146000,
    "gross_margin": 38000,
    "gross_margin_pct": 20.65
  },
  "source": {
    "system": "erp",
    "dataset": "project_financials",
    "record_ids": ["PRJ-1042:2026-09"],
    "retrieved_at": "2026-09-15T12:40:00Z"
  },
  "execution": {
    "latency_ms": 214,
    "cache": "miss"
  }
}
```

---

## Tool modes

### `read`

Retrieves data without modifying external state.

Examples:

- query ERP revenue,
- read CRM opportunities,
- fetch project status,
- retrieve documents.

### `prepare`

Builds an action payload but does not execute it.

Examples:

- draft a customer message,
- prepare a CRM update,
- generate an approval request.

### `write`

Changes external state.

Examples:

- update an opportunity,
- trigger a workflow,
- send a communication,
- change a record.

Public reference workflows should default to `read`; `write` tools require an explicit approval mechanism.

---

## Permission model

Tool availability is the intersection of:

```text
User permission
    AND
Agent permission
    AND
Task policy
    AND
Tool policy
    AND
Approval state
```

No single layer should be able to bypass the others.

---

## Evidence metadata

Read tools should return enough provenance to answer:

- Which system produced this data?
- Which records were used?
- When was the data retrieved?
- Was the result transformed or aggregated?
- Can the evidence be reproduced?

Example evidence object:

```json
{
  "evidence_id": "ev_004",
  "source_type": "structured_system",
  "system": "erp",
  "dataset": "invoice_lines",
  "record_ids": ["INV-9811", "INV-9824"],
  "retrieved_at": "2026-09-15T12:40:00Z",
  "freshness": "current",
  "transformation": "sum(direct_material_cost) grouped by month"
}
```

---

## Failure model

Standard statuses:

- `success`
- `validation_error`
- `unauthorized`
- `not_found`
- `timeout`
- `upstream_error`
- `rate_limited`
- `policy_blocked`

A failure response should never be silently converted into fabricated data.

```json
{
  "tool_call_id": "tc_01J...",
  "status": "unauthorized",
  "error": {
    "code": "ERP_FINANCE_SCOPE_REQUIRED",
    "message": "The current execution context does not have access to project cost details",
    "retryable": false
  }
}
```

---

## Idempotency and write safety

Write tools should support an idempotency key where the underlying system allows it.

```json
{
  "idempotency_key": "approval_01J...:crm.update_opportunity:OPP-882"
}
```

Before executing a consequential write, the system should verify:

1. the approval is valid,
2. the approval matches the exact action,
3. the target record has not materially changed,
4. the request has not already been executed,
5. the action is included in the audit trail.

---

## Example tool catalog

```text
finance
  erp.get_project_margin
  erp.get_receivables
  erp.get_payables
  finance.get_budget_variance

sales
  crm.get_pipeline
  crm.get_opportunity
  crm.get_account_activity

operations
  projects.get_status
  inventory.get_material_availability
  suppliers.get_delivery_performance

knowledge
  docs.search
  docs.fetch
  knowledge.retrieve
```

The catalog should remain small and composable. A clear tool with a stable contract is preferable to a generic tool that exposes an entire enterprise system.
