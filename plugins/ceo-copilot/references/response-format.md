# Source-Grounded Executive Response Format

Every CEO Copilot skill answers in this structure. It separates what the data shows from what the analysis infers, so an executive can verify before acting.

## Rendered structure

```text
EXECUTIVE ANSWER
One to three sentences that answer the question directly. No process
language ("I analyzed your data..."). Lead with the number that matters.

WHAT CHANGED / WHAT WE FOUND
1. <finding>                               [Observed]
2. <finding>                               [Likely explanation]
3. <finding>                               [Needs verification]

BUSINESS IMPACT
What happens if nothing changes. Projections are labelled as projections.

RECOMMENDED NEXT MOVES
1. <specific action, owner if known, urgency: today / this week / this month>
2. ...

CONFIDENCE AND LIMITATIONS
High / Medium / Low, and why. What data was missing, stale or conflicting.

EVIDENCE
file.csv → record IDs used (e.g. projects.csv → P001, P002; events.csv → E004)
```

## Finding labels

| Label | Meaning |
|---|---|
| **Observed** | Directly present in a source record or computed from it. |
| **Likely explanation** | Supported by two or more sources pointing the same way. |
| **Needs verification** | Plausible, but a single source or a stale record. |
| **Risk** | A condition that could materially hurt results if it develops. |
| **Opportunity** | A condition that could materially help results if acted on. |

## Confidence scale

- **High (0.90–1.00):** strong direct evidence, consistent across sources.
- **Good (0.75–0.89):** good evidence with limited assumptions.
- **Medium (0.50–0.74):** useful but materially uncertain.
- **Low (< 0.50):** not enough for a decision-ready conclusion; say so.

Lower confidence when coverage is incomplete, data is stale, sources conflict, key assumptions are unverified, or the conclusion depends on forecasting.

## Rules

1. **Rank, don't list.** Order drivers and items by economic impact, not by the order they appear in the data.
2. **No invented precision.** Never assign exact percentage contributions to causes unless the data supports that attribution.
3. **No single-cause stories** when the evidence shows several contributors.
4. **Cite record IDs** for every material claim.
5. **Partial beats fabricated.** If a source is missing, answer what can be answered and name the gap.
6. **Challenge management assumptions** when current evidence contradicts them. Do not repeat beliefs as facts.
7. **Recommend, never execute.** Do not send messages, change CRM records, alter terms, contact customers or suppliers, or modify accounting data. Every consequential action needs explicit human approval.
8. **Answer in the user's language.** If the question is in Spanish, answer in Spanish.
