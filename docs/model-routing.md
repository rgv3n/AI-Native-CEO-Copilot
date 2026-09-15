# Model Routing Architecture

## Purpose

AI-Native CEO Copilot should not bind executive workflows to a single model.

Different tasks have different requirements for reasoning depth, latency, context size, privacy, structured output and cost. Model routing allows the system to choose the most appropriate inference endpoint for each task while preserving the same agent and tool contracts.

---

## 1. Routing principle

Route by workload requirements, not by model popularity.

A routing decision should consider:

- task type,
- business criticality,
- data sensitivity,
- expected context size,
- reasoning complexity,
- latency target,
- structured-output requirements,
- modality,
- availability,
- cost budget,
- infrastructure load.

---

## 2. Example routing request

```json
{
  "trace_id": "trace-2026-09-15-001",
  "task_class": "executive_margin_diagnosis",
  "data_sensitivity": "confidential",
  "reasoning_class": "high",
  "context_class": "large",
  "latency_class": "interactive",
  "structured_output": true,
  "preferred_deployment": "private",
  "max_cost_class": "standard"
}
```

Agents should not directly select a provider-specific model identifier.

---

## 3. Routing policy

A model router evaluates eligible endpoints against policy.

Conceptually:

```text
Eligible endpoints =
  Capability match
  AND Security policy
  AND Data residency policy
  AND Availability
  AND Cost policy
  AND Performance policy
```

The router then selects the best eligible endpoint.

---

## 4. Representative task classes

### Lightweight classification

Examples:

- intent detection,
- entity extraction,
- document classification,
- routing decisions.

Preferred characteristics:

- low latency,
- low cost,
- smaller model,
- high concurrency.

### Evidence extraction

Examples:

- extracting values from contracts,
- identifying project risks in status notes,
- summarizing CRM activity.

Preferred characteristics:

- strong structured output,
- moderate context,
- predictable latency.

### Executive diagnosis

Examples:

- why gross margin fell,
- where cash is trapped,
- which projects require intervention.

Preferred characteristics:

- stronger reasoning,
- larger context,
- evidence-aware synthesis,
- reliable structured output.

### Strategic synthesis

Examples:

- capital allocation,
- scenario analysis,
- cross-functional executive prioritization.

Preferred characteristics:

- highest reasoning quality,
- broad context,
- lower tolerance for unsupported claims.

---

## 5. Private vs external routing

A hybrid system may expose several endpoint classes:

```text
PRIVATE_FAST
PRIVATE_REASONING
EXTERNAL_GENERAL
EXTERNAL_FRONTIER
SPECIALIZED_EMBEDDING
SPECIALIZED_VISION
```

Routing rules can then express policies such as:

- confidential finance data → private endpoint only,
- public market research → approved external endpoint allowed,
- embeddings → specialized embedding service,
- high-impact executive recommendation → stronger reasoning tier,
- high-volume extraction → efficient private model.

---

## 6. Fallback behavior

Fallbacks must preserve policy.

A private endpoint failure must not automatically route confidential data to an external API.

Safe fallback order:

1. another policy-equivalent endpoint,
2. reduced-capability private endpoint,
3. partial response,
4. explicit failure.

Security constraints override availability convenience.

---

## 7. Load-aware routing

Routing can also consider live infrastructure conditions:

- queue depth,
- time to first token,
- token throughput,
- GPU memory pressure,
- endpoint health,
- request concurrency,
- recent error rate.

This allows the same executive workload to use different eligible capacity pools without changing business logic.

---

## 8. Cost-aware routing

Cost should be measured per executive outcome rather than only per token.

Useful metrics include:

- inference cost per executive task,
- cost per successful grounded answer,
- cost per decision domain,
- cost per tenant,
- cost by agent,
- cost of retries and failed tool chains.

A cheaper model is not cheaper if it creates more retries, weaker evidence or more human review.

---

## 9. Quality-aware routing

Model selection should be evaluated against the Executive Golden Questions benchmark.

For each route, measure:

- correctness,
- evidence coverage,
- factual consistency,
- prioritization quality,
- confidence calibration,
- latency,
- cost.

A production router can then choose the lowest-cost endpoint that still satisfies the quality threshold for a task class.

---

## 10. Routing observability

Each model invocation should record:

```json
{
  "trace_id": "trace-...",
  "task_class": "executive_margin_diagnosis",
  "route_policy": "confidential_high_reasoning",
  "selected_endpoint": "private_reasoning_pool",
  "selection_reason": [
    "confidential_data",
    "high_reasoning_required",
    "endpoint_healthy"
  ],
  "fallback_used": false
}
```

This makes model selection auditable rather than invisible.

---

## 11. Architectural outcome

The most important property is separation of concerns:

```text
Executive question
      ↓
Agent workflow
      ↓
Capability request
      ↓
Model router
      ↓
Eligible inference endpoint
```

Business workflows remain stable while models and infrastructure can evolve independently.
