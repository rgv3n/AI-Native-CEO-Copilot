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

- [x] Role-based access patterns
- [x] Private deployment reference
- [x] Model-routing architecture
- [x] GPU inference deployment notes
- [x] Multi-tenant isolation principles

Enterprise deployment references:

- [`enterprise-deployment-patterns.md`](enterprise-deployment-patterns.md)
- [`model-routing.md`](model-routing.md)
- [`nvidia-inference-deployment.md`](nvidia-inference-deployment.md)

The public v0.5 layer defines deployment boundaries, access-control patterns, private and hybrid inference, workload-aware model routing, NVIDIA-oriented GPU inference patterns and tenant-isolation principles. Production implementation remains organization-specific.

## v0.6 — Agentic operating model

- [x] Agentic operating model
- [x] Executive operating loop
- [x] Management-by-exception pattern
- [x] Agent autonomy levels
- [x] Human decision boundaries

Operating-model references:

- [`agentic-operating-model.md`](agentic-operating-model.md)
- [`executive-operating-loop.md`](executive-operating-loop.md)
- [`autonomy-matrix.md`](autonomy-matrix.md)

The public v0.6 layer translates the technical architecture into an executive operating model: specialized agents continuously observe, investigate, coordinate and prioritize company signals; humans retain authority for consequential decisions; selected low-risk workflows can progress toward policy-bounded autonomous execution.

## Direction

The goal is not to maximize feature count.

The goal is to build a clear reference for a new class of enterprise system: an AI-native executive intelligence and operating layer that can reason over company data, coordinate specialized agents, reduce manual organizational coordination and keep humans in control of consequential decisions.
