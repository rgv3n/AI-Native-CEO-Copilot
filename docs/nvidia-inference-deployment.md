# NVIDIA Inference Deployment Reference

## Purpose

This document describes how the AI-Native CEO Copilot can map onto an NVIDIA-based private or hybrid inference stack.

It is a reference architecture, not a fixed bill of materials. The correct design depends on workload, concurrency, latency targets, model size, context length, privacy requirements and total cost of ownership.

---

## 1. Start with the workload

Do not start with the GPU.

Start with the executive workload:

- how many executive tasks per hour,
- how many agents can run in parallel,
- how many model calls each workflow creates,
- expected prompt and output token volumes,
- context size,
- latency target,
- model size and precision,
- concurrency,
- data sensitivity,
- availability requirements.

The GPU architecture is selected after these requirements are understood.

---

## 2. Reference inference stack

A representative NVIDIA-oriented deployment can be expressed as:

```text
Executive Applications
        ↓
Agent Orchestrator
        ↓
Model Router / Inference Gateway
        ↓
NVIDIA NIM / Approved Inference Runtime
        ↓
Kubernetes or Managed Container Platform
        ↓
NVIDIA GPU Operator
        ↓
NVIDIA GPU Driver + Container Runtime
        ↓
NVIDIA GPU Infrastructure
```

Supporting layers may include:

- NVIDIA AI Enterprise,
- NVIDIA NIM,
- NVIDIA GPU Operator,
- NVIDIA NIM Operator,
- NVIDIA DCGM / DCGM Exporter,
- Prometheus-compatible monitoring,
- NVIDIA Run:ai where workload orchestration and GPU sharing are required,
- NVIDIA networking components where scale-out performance justifies them.

---

## 3. NVIDIA AI Enterprise role

NVIDIA AI Enterprise provides an enterprise software stack spanning application and infrastructure layers.

For this architecture, relevant capabilities include:

- supported AI frameworks,
- NIM microservices,
- GPU infrastructure software,
- Kubernetes operators,
- lifecycle management,
- enterprise support.

A production team should validate software-version compatibility as a stack rather than upgrading drivers, operators and runtimes independently.

The compatibility chain remains:

**DRIVER → CUDA / runtime → inference framework → model service → application**

---

## 4. NVIDIA NIM role

NVIDIA NIM can provide packaged inference microservices for supported models.

Architecturally, NIM fits behind the model-routing layer:

```text
Agent workflow
    ↓
Capability request
    ↓
Model router
    ↓
NIM endpoint
```

The business agents should not depend directly on NIM-specific implementation details.

This preserves portability while allowing optimized NVIDIA-backed inference where appropriate.

---

## 5. Kubernetes deployment pattern

For Kubernetes-based environments, a common pattern is:

```text
Kubernetes Cluster
│
├── Agent / application workloads
├── Inference gateway
├── NIM services
├── NVIDIA GPU Operator
├── GPU scheduling
├── DCGM telemetry
└── Observability stack
```

The NVIDIA GPU Operator manages the GPU software lifecycle inside Kubernetes environments, reducing manual node-by-node configuration.

NIM services can be deployed through supported Kubernetes mechanisms such as Helm or the NVIDIA NIM Operator.

---

## 6. Model caching and startup behavior

Large model artifacts can make pod startup expensive.

A production design should consider:

- persistent model caches,
- local NVMe where appropriate,
- shared storage throughput,
- image pull latency,
- model-load time,
- warm capacity,
- autoscaling thresholds.

The system should distinguish between:

**container startup latency**

and

**model readiness latency**.

They are not the same operational problem.

---

## 7. GPU allocation strategy

The main allocation patterns are:

### Full GPU

Use when:

- the model requires most of the device memory,
- predictable performance matters,
- throughput is high enough to justify dedicated capacity.

### Multi-GPU model deployment

Use when:

- the model does not fit efficiently on one GPU,
- tensor or pipeline parallelism is required,
- throughput justifies the communication overhead.

### MIG

Where supported by the GPU and workload, Multi-Instance GPU can partition a compatible GPU into isolated GPU instances.

Potential use cases include:

- smaller inference workloads,
- isolation between services,
- improved utilization for predictable workloads.

MIG should not be assumed to improve every LLM workload. Partitioning reduces the resources available to each instance and must be validated against model memory and throughput requirements.

---

## 8. Capacity planning

Capacity should be modeled from request behavior rather than nominal model size alone.

Important inputs:

- model weights,
- KV cache requirements,
- context length,
- batch size,
- concurrent sequences,
- precision,
- speculative decoding configuration where used,
- tensor parallel degree,
- expected input/output token mix.

For agentic workloads, the number of model calls per executive task can matter as much as the size of any individual request.

A workflow may create:

```text
1 executive question
→ planner call
→ 3 specialist-agent calls
→ 4 retrieval / tool interpretation calls
→ synthesis call
→ validation call
```

Infrastructure sizing should therefore use **tokens and model calls per executive task**, not only requests per second.

---

## 9. Latency metrics

For interactive executive use, track at minimum:

- request queue time,
- time to first token,
- output token throughput,
- total inference latency,
- total workflow latency.

A fast model endpoint does not guarantee a fast executive response if tool calls, retrieval or agent fan-out dominate the workflow.

---

## 10. GPU telemetry

DCGM and DCGM Exporter can expose GPU telemetry for operational monitoring.

Relevant metrics may include:

- GPU utilization,
- memory utilization,
- framebuffer memory used,
- power draw,
- temperature,
- clocks,
- PCIe activity,
- NVLink-related telemetry where applicable,
- error and health indicators.

These infrastructure metrics should be correlated with the executive workflow trace.

Example:

```text
trace_id
  ↓
agent task
  ↓
model invocation
  ↓
inference endpoint
  ↓
GPU workload telemetry
```

This allows the organization to calculate the infrastructure cost of an actual business decision workflow.

---

## 11. Observability architecture

A practical monitoring flow is:

```text
NVIDIA GPU / inference runtime
        ↓
DCGM / inference metrics
        ↓
Metrics collector
        ↓
Observability platform
        ↑
Agent workflow traces
        ↑
Executive task IDs
```

The valuable unit of measurement is not only GPU utilization.

It is:

**business outcome per unit of inference infrastructure**.

Examples:

- GPU-seconds per executive question,
- tokens per successful decision workflow,
- cost per grounded answer,
- latency per decision class,
- infrastructure cost by tenant,
- GPU utilization by agent workload.

---

## 12. Scale-up vs scale-out

### Scale-up

Prefer larger or more capable GPU nodes when:

- models require tight GPU-to-GPU communication,
- a single model spans multiple GPUs,
- low inter-GPU latency matters.

### Scale-out

Prefer additional inference replicas or nodes when:

- models fit inside a node,
- workload is highly concurrent,
- horizontal replication improves throughput,
- fault-domain separation matters.

Do not automatically distribute a model across nodes if independent replicas provide better economics and simpler operations.

---

## 13. Networking

Networking becomes increasingly important when:

- inference uses multiple nodes,
- large model artifacts are loaded frequently,
- retrieval systems move substantial data,
- distributed inference or training is involved,
- storage traffic competes with model traffic.

At smaller scales, networking may not be the bottleneck.

At larger scales, NVIDIA networking technologies and RDMA-capable architectures can become part of the design.

Networking should therefore be sized from measured communication patterns rather than added by default.

---

## 14. Storage

AI inference storage requirements differ from transactional application storage.

Consider:

- model artifact size,
- startup read bandwidth,
- cache hit rate,
- container image distribution,
- retrieval-index performance,
- logging and trace retention.

Fast local storage can improve model startup, but shared storage may simplify fleet management.

The design should optimize for the actual deployment lifecycle.

---

## 15. Availability pattern

A resilient private inference architecture may include:

- multiple inference replicas,
- health-checked routing,
- reserved warm capacity,
- node failure detection,
- graceful model-router fallback,
- admission control when capacity is exhausted.

The model router should know the difference between:

- endpoint unhealthy,
- endpoint overloaded,
- model unavailable,
- policy-ineligible endpoint.

These states require different responses.

---

## 16. Security boundary

Private inference should still enforce:

- authenticated model access,
- network segmentation,
- encrypted traffic,
- secrets isolation,
- container-image governance,
- model artifact provenance,
- least-privilege service accounts,
- audit logging.

Running inference on owned GPUs does not automatically make the system secure.

---

## 17. Cost model

Owned GPU infrastructure should be compared against managed inference using total cost of ownership.

### CAPEX

- GPU servers,
- networking,
- storage,
- racks,
- power and cooling infrastructure.

### OPEX

- electricity,
- cooling,
- support,
- software subscriptions,
- operations staff,
- hardware replacement,
- idle capacity.

### Cloud / managed inference

- token or endpoint charges,
- reserved capacity,
- data transfer,
- managed service premiums.

The economically correct decision depends on utilization.

A GPU that is technically fast but mostly idle can be more expensive than an external service.

The repository models this at the business-workload level through **Cost per Executive Workflow**. See [`executive-workflow-economics.md`](executive-workflow-economics.md). The private-GPU calculator accepts an effective GPU-hour rate plus measured or allocated GPU-seconds, so hardware economics can be compared against managed token pricing without hard-coding vendor prices.

---

## 18. Recommended architecture evolution

### Stage 1 — External / managed inference

Validate executive workflows quickly.

### Stage 2 — Hybrid routing

Move sensitive or high-volume workloads to controlled private endpoints.

### Stage 3 — Private NVIDIA inference platform

Introduce dedicated GPU capacity when workload volume, privacy, latency or economics justify it.

### Stage 4 — Optimized AI factory

At sufficient scale, optimize scheduling, networking, storage, model placement, observability and capacity as a coordinated infrastructure system.

---

## 19. Key architectural rule

The Copilot should never require a particular GPU architecture to function.

The business architecture remains stable:

```text
Executive question
→ Agents
→ Tools and evidence
→ Model routing
→ Inference infrastructure
```

NVIDIA infrastructure is used where it provides the best combination of:

- performance,
- privacy,
- throughput,
- operational control,
- economics.

That is an infrastructure decision, not an application dependency.

---

## 20. Production note

Specific GPU selection, NIM compatibility, operator versions and software lifecycle choices should always be validated against the current NVIDIA support and compatibility documentation before deployment.

Do not upgrade the production stack component-by-component without validating the complete compatibility chain.
