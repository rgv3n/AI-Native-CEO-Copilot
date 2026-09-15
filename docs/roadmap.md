# Public Roadmap

This roadmap describes the public reference implementation, not the private production roadmap.

## v0.1 — Positioning and architecture

- [x] Project thesis
- [x] Reference architecture
- [x] Executive use cases
- [x] Security principles
- [x] Public roadmap

## v0.2 — Demo intelligence layer

- [x] Synthetic company dataset
- [x] Executive question schema
- [x] Finance agent interface
- [x] Sales agent interface
- [x] Operations agent interface
- [x] Tool contracts
- [x] Source-grounded response format

Documentation and benchmark assets:

- [`executive-question-schema.md`](executive-question-schema.md)
- [`executive-golden-questions.md`](executive-golden-questions.md)
- [`agent-interfaces.md`](agent-interfaces.md)
- [`tool-contracts.md`](tool-contracts.md)
- [`source-grounded-response-format.md`](source-grounded-response-format.md)
- [`../demo-data/README.md`](../demo-data/README.md)

## v0.3 — Working executive workflows

- [x] Margin analysis demo
- [x] Cash-flow risk demo
- [x] Sales prioritization demo
- [x] Project risk demo
- [x] Human approval checkpoints

Workflow examples:

- [`../examples/margin-analysis/README.md`](../examples/margin-analysis/README.md)
- [`../examples/margin-analysis/expected-output.md`](../examples/margin-analysis/expected-output.md)
- [`../examples/cash-flow-risk/README.md`](../examples/cash-flow-risk/README.md)
- [`../examples/cash-flow-risk/expected-output.md`](../examples/cash-flow-risk/expected-output.md)
- [`../examples/sales-prioritization/README.md`](../examples/sales-prioritization/README.md)
- [`../examples/sales-prioritization/expected-output.md`](../examples/sales-prioritization/expected-output.md)
- [`../examples/project-risk/README.md`](../examples/project-risk/README.md)
- [`../examples/project-risk/expected-output.md`](../examples/project-risk/expected-output.md)
- [`human-approval-checkpoints.md`](human-approval-checkpoints.md)

## v0.4 — Observability

- [x] Tool-call tracing
- [x] Latency and cost metrics
- [x] Source coverage
- [x] Failure handling
- [x] Confidence and evidence views

Observability reference:

- [`observability.md`](observability.md)
- [`../examples/observability/margin-analysis-trace.json`](../examples/observability/margin-analysis-trace.json)

The public v0.4 layer defines the observability contracts and reference telemetry model. Production instrumentation, dashboards and infrastructure-specific collectors remain implementation-specific.

## v0.5 — Enterprise deployment patterns

- [ ] Role-based access patterns
- [ ] Private deployment reference
- [ ] Model-routing architecture
- [ ] GPU inference deployment notes
- [ ] Multi-tenant isolation principles

## Direction

The goal is not to maximize feature count.

The goal is to build a clear reference for a new class of enterprise system: an AI-native executive intelligence layer that can reason over company data, coordinate specialized agents and keep humans in control of consequential actions.
