# Security Principles

CEO Copilot is intended for environments where business data can be sensitive and decisions can be consequential.

This public repository documents security principles, not production secrets.

## Core principles

### Least privilege

Agents and tools should receive only the permissions required for their task.

### Explicit tool boundaries

Every external system should be accessed through a defined tool or connector with clear inputs, outputs and permissions.

### Human approval for high-impact actions

Actions that can move money, alter contracts, modify records, send external communications or materially affect operations should require explicit approval unless a company has intentionally delegated that authority.

### Data minimization

Only the data needed for a task should enter the model context.

### Source traceability

Executive outputs should preserve provenance so users can inspect the evidence behind a conclusion.

### Tenant isolation

Multi-company deployments must keep customer data, memory, credentials and execution traces isolated.

### Secret management

Credentials must never be committed to source control. Production deployments should use a dedicated secret-management mechanism and short-lived credentials where possible.

### Auditability

Tool calls, approvals, failures and consequential actions should be logged in a way that supports investigation and governance.

## Prompt injection and untrusted data

Documents, email, CRM text and external content should be treated as untrusted input. Retrieval does not make content trustworthy.

The system should distinguish between:

- instructions from authorized users,
- system policies,
- retrieved business facts,
- and text that merely attempts to issue instructions.

## Public vs private implementation

The public repository intentionally excludes:

- production credentials,
- customer configuration,
- private prompts,
- proprietary decision logic,
- production connector implementations,
- internal security controls,
- customer data,
- private deployment topology.

Security claims in this repository describe design direction. They should not be interpreted as certification of a specific production deployment.
