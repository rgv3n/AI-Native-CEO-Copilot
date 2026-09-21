# Use This Repository With ChatGPT or Claude

## Purpose

This repository is not only a reference architecture to read.

A CEO, founder or executive team can use the repository as a **knowledge and decision framework inside a general-purpose AI assistant** such as ChatGPT or Claude.

The idea is simple:

```text
AI-Native CEO Copilot repository
        +
your company context / data
        ↓
ChatGPT or Claude
        ↓
executive answers grounded in the repository framework
```

The assistant can use the repository to understand:

- how executive questions should be structured,
- which business domains may need to be reconciled,
- how evidence should be treated,
- how uncertainty should be surfaced,
- how options and trade-offs should be presented,
- when an issue deserves executive attention,
- how autonomy and approval boundaries should work,
- how AI infrastructure decisions should be linked to workload,
- and how executive workflows can be measured economically.

---

## What you can ask

You are not limited to a predefined question list.

You can ask questions such as:

- What deserves my attention today?
- What am I missing in this situation?
- Where could margin be leaking?
- Which customers may be destroying profitability?
- What data should I examine before making this decision?
- What are my realistic options?
- What are the trade-offs between these options?
- What happens if I do nothing?
- Which assumptions should I challenge?
- Which decisions should remain human?
- Which parts of this process could be automated?
- What information would you need from my company to answer this reliably?
- How should I structure this problem?
- Which workflows from the repository are relevant to my situation?
- How could this be implemented in my company?
- What AI architecture would fit this use case?
- Should this workload stay in managed inference or move to private infrastructure?
- What would need to be measured before considering NVIDIA infrastructure?

The repository should be treated as the **operating framework**.

Your own company information provides the situation being analyzed.

---

## How to use it

### Option 1 — Give the assistant the repository URL

Provide the public repository URL and ask the assistant to use it as reference context.

Then add your company situation.

Example:

```text
Use the AI-Native CEO Copilot repository as the operating framework for this conversation.

Here is our current situation:

- Revenue is growing.
- Gross margin has fallen for 3 months.
- Accounts receivable are increasing.
- Two large projects are behind schedule.
- Sales says the pipeline is healthy.

Based on the repository's executive intelligence framework:

1. What should I investigate first?
2. What are the most likely competing explanations?
3. What information do you need from me?
4. What decisions may be required?
5. What should I not conclude yet?
```

### Option 2 — Add repository files to a ChatGPT Project / Claude Project

Add the relevant public repository documents as project knowledge.

Recommended starting files:

- `README.md`
- `docs/executive-overview.md`
- `docs/executive-golden-questions.md`
- `docs/executive-question-schema.md`
- `docs/executive-decision-packet.md`
- `docs/materiality-engine.md`
- `docs/company-control-plane.md`
- `docs/autonomy-matrix.md`
- `docs/observability.md`
- `docs/executive-workflow-economics.md`
- `docs/nvidia-inference-deployment.md`

Then provide company context as needed.

### Option 3 — Use the repository plus company files

For deeper analysis, combine repository context with approved company data such as:

- P&L,
- balance sheet,
- cash-flow data,
- accounts receivable,
- CRM exports,
- pipeline,
- project portfolio,
- project margins,
- delivery milestones,
- customer data,
- supplier data,
- operational KPIs,
- management assumptions,
- budgets and forecasts.

The assistant can then use the repository to structure the analysis rather than answering as a generic chatbot.

---

## Default operating rules for the assistant

When using this repository as context, the assistant should:

1. **Start from the executive objective or problem.**
2. **Identify the domains involved** — Finance, Sales, Operations, Strategy, Research.
3. **Separate known facts from inference.**
4. **Do not invent missing company data.**
5. **State what evidence is missing.**
6. **Consider multiple explanations before selecting one.**
7. **Prioritize by materiality, urgency and business impact.**
8. **Present realistic options and trade-offs.**
9. **Include the no-action scenario when relevant.**
10. **Preserve human authority for consequential decisions.**
11. **Recommend the smallest next step that reduces uncertainty.**
12. **Use infrastructure recommendations only after the workload is understood.**

---

## Default answer modes

The CEO can ask the assistant to respond in different modes.

### Executive answer

Short and decision-oriented.

```text
What is happening?
Why does it matter?
What are the options?
What should I do next?
What remains uncertain?
```

### Deep investigation

Cross-functional analysis with evidence requirements, competing hypotheses and next data requests.

### Decision packet

Use the repository's Executive Decision Packet:

```text
ISSUE
WHY IT MATTERS
EVIDENCE
OPTIONS
TRADE-OFFS
RECOMMENDATION
AUTHORITY
URGENCY
```

### Challenge mode

Ask the assistant:

```text
Challenge my current interpretation using the AI-Native CEO Copilot framework.
What assumptions may be wrong?
What evidence contradicts me?
What would change the decision?
```

### Implementation mode

Ask:

```text
How would this problem be implemented as a production AI workflow?
```

The assistant should map:

```text
Executive question
→ required data
→ tools / integrations
→ deterministic logic
→ agents
→ model calls
→ governance
→ observability
→ infrastructure
```

---

## Important limitation

The repository gives the assistant a **decision architecture and operating framework**.

It does not magically give the assistant access to your company.

The quality of the answer depends on the evidence provided or connected.

The correct behavior when evidence is incomplete is:

> "Here is what can be concluded now, here is what remains uncertain, and here is the smallest additional information that would materially improve the decision."

---

## From AI conversation to production system

Using ChatGPT or Claude with this repository is the fastest evaluation path.

```text
Phase 1
Repository + CEO + uploaded context
        ↓
AI-assisted executive analysis
```

If that becomes useful repeatedly, the production opportunity is:

```text
Phase 2
ERP / CRM / Finance / Projects / BI
        ↓
AI-Native CEO Copilot
        ↓
continuous investigation
        ↓
material exceptions
        ↓
decision-ready intelligence
```

That transition removes the need for the CEO to manually provide the right data and ask the right question every time.

---

## Enterprise implementation

For organization-specific integration, governance, agentic workflows and AI infrastructure:

**[CompaniesAutomation.com](https://companiesautomation.com/en)**

See also:

- [Enterprise AI Architecture Assessment](enterprise-ai-architecture-assessment.md)
- [Executive Golden Questions](executive-golden-questions.md)
- [Executive Decision Packet](executive-decision-packet.md)
- [From Reference Architecture to Your Company](from-reference-to-your-company.md)
