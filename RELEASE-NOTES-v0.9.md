# v0.9 — Continuous Executive Intelligence

## Summary

v0.9 moves AI-Native CEO Copilot from a static architecture showcase toward an executable, evaluation-oriented public reference.

## Highlights

- Continuous Executive Intelligence operating model
- Executive Decision Engine and Decision Packet
- CEO Discovery Interview
- ChatGPT / Claude usage path with preferred-language selection
- Synthetic Northstar Industrial Systems dataset
- Executable deterministic margin-analysis workflow
- Executive workflow observability contracts
- Cost per Executive Workflow model and calculator
- NVIDIA-oriented inference deployment reference
- Enterprise AI Architecture Assessment
- Live executive demo on Vercel

## Executable examples

Deterministic public workflow:

```bash
python3 examples/margin-analysis/run.py
python3 examples/margin-analysis/run.py --json
```

Optional measured model workflow:

```bash
AI_BASE_URL=<OPENAI_COMPATIBLE_BASE_URL> \
AI_API_KEY=<KEY> \
AI_MODEL=<MODEL> \
python3 examples/margin-analysis/run_with_model.py
```

The model runner records actual API latency and provider-reported token usage. Pricing is optional and must be passed explicitly through environment variables; no provider pricing is hard-coded.

## Important scope note

The public repository is a reference and evaluation layer. Production enterprise implementations, private integrations, governance, model routing and infrastructure deployment remain organization-specific.
