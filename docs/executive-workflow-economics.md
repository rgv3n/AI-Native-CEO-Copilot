# Cost per Executive Workflow

## Why this metric matters

Traditional inference economics often starts with infrastructure units:

- price per GPU-hour,
- price per million tokens,
- requests per second,
- tokens per second.

Those metrics are necessary, but they are not the business unit consumed by a CEO.

For AI-Native CEO Copilot, the useful economic unit is:

> **Cost per Executive Workflow**

An executive workflow may contain planning, specialist agents, retrieval, tool calls, reconciliation, validation and final synthesis. One question can therefore create many model invocations and many infrastructure events.

The architecture should preserve the chain:

```text
Executive question
    ↓
Agent workflow
    ↓
Model + tool calls
    ↓
Inference endpoints
    ↓
GPU / managed inference consumption
    ↓
Cost per executive workflow
```

---

## 1. Workload metrics

For each workflow, capture at least:

- model calls,
- input tokens,
- output tokens,
- cached tokens,
- workflow latency,
- retries,
- tool calls,
- sources used,
- GPU-seconds where private infrastructure is used.

This repository includes an illustrative trace:

`examples/observability/margin-analysis-trace.json`

The trace is synthetic. It defines the measurement contract; it is not a production benchmark.

---

## 2. Managed inference calculation

For token-priced inference:

```text
uncached input cost
  = uncached input tokens / 1,000,000 × input token rate

cached input cost
  = cached tokens / 1,000,000 × cached token rate

output cost
  = output tokens / 1,000,000 × output token rate

cost per executive workflow
  = input cost
  + cached input cost
  + output cost
  + allocated platform/tool overhead
```

Rates must come from the deployment being evaluated. The public repository deliberately does not hard-code provider prices because pricing changes over time.

---

## 3. Private NVIDIA infrastructure calculation

For owned, reserved or dedicated GPU capacity, token prices are not the native cost unit.

A simple allocation model is:

```text
inference infrastructure cost
  = GPU-seconds attributed to workflow / 3,600
  × effective GPU-hour cost

cost per executive workflow
  = inference infrastructure cost
  + allocated platform/tool overhead
```

The phrase **effective GPU-hour cost** is important.

For owned infrastructure it should eventually include, as appropriate:

- hardware amortization,
- utilization / idle capacity,
- electricity,
- cooling,
- software subscriptions,
- support,
- operations,
- storage and networking allocation.

Using purchase price divided by theoretical lifetime while assuming 100% utilization will understate real cost.

---

## 4. Why GPU utilization matters

Consider two identical executive workloads.

One is served on a GPU fleet running near an economically healthy utilization range.

The other is served on dedicated capacity that spends most of the day idle.

The second environment can have excellent latency and still have worse economics.

This is why the architecture correlates:

```text
trace_id
→ model invocation
→ inference endpoint
→ GPU telemetry
→ cost allocation
```

With NVIDIA infrastructure, DCGM / DCGM Exporter and serving-layer metrics can contribute GPU utilization, memory use, power, queueing and throughput signals.

---

## 5. Business economics

The goal is not always to minimize workflow cost.

A more useful comparison is:

```text
Cost per Executive Workflow
versus
Business Value / Risk Addressed
```

Examples:

- cost to investigate a margin anomaly,
- cost to identify cash trapped in receivables,
- cost to validate a large sales opportunity,
- cost to investigate an operational risk,
- cost to produce a grounded executive decision packet.

A €1 workflow that saves hours of analyst time or exposes a six-figure risk may be economically excellent.

A €0.05 workflow that produces unreliable conclusions may be expensive in business terms.

---

## 6. Executable calculator

The repository includes:

```bash
python3 examples/observability/workflow_economics.py --help
```

### Managed/token-priced example

Pass the rates you are actually evaluating:

```bash
python3 examples/observability/workflow_economics.py \
  --trace examples/observability/margin-analysis-trace.json \
  --input-eur-per-million <RATE> \
  --output-eur-per-million <RATE> \
  --cached-eur-per-million <RATE>
```

### Private GPU example

Pass an effective GPU-hour cost and measured/allocated GPU-seconds:

```bash
python3 examples/observability/workflow_economics.py \
  --trace examples/observability/margin-analysis-trace.json \
  --gpu-hour-eur <EFFECTIVE_RATE> \
  --gpu-seconds <MEASURED_GPU_SECONDS> \
  --fixed-overhead-eur <ALLOCATED_OVERHEAD>
```

Use `--json` for machine-readable output.

---

## 7. From workflow economics to capacity planning

Once enough traces exist, aggregate them by executive workflow class.

For example:

| Workflow class | Workflows/day | Model calls/workflow | Tokens/workflow | p95 latency | GPU-seconds/workflow | Cost/workflow |
|---|---:|---:|---:|---:|---:|---:|
| Margin diagnosis | measured | measured | measured | measured | measured | calculated |
| Cash investigation | measured | measured | measured | measured | measured | calculated |
| Pipeline validation | measured | measured | measured | measured | measured | calculated |

From this, infrastructure planning becomes grounded in actual business demand:

```text
executive workflows/day
× inference demand/workflow
× concurrency profile
× latency target
→ required inference capacity
```

Only then should GPU selection become the primary question.

---

## 8. Architectural principle

> **Do not optimize GPU cost in isolation. Optimize the cost, latency, reliability and quality of the complete executive workflow.**

This is the bridge between executive AI and AI Factory economics.

For production workload sizing, private/hybrid inference architecture and NVIDIA infrastructure design, see [CompaniesAutomation.com](https://companiesautomation.com/en).
