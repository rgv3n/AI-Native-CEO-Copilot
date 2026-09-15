# Recommendation Ranking

## Purpose

Recommendation Ranking defines how the Executive Decision Engine prioritizes options without reducing executive judgment to a hidden score.

The preferred option should be explainable in business terms.

## Ranking inputs

The engine should consider:

- strategic-objective alignment,
- expected business impact,
- cash and margin effects,
- downside severity,
- reversibility,
- time to effect,
- execution complexity,
- customer or stakeholder impact,
- evidence quality,
- uncertainty,
- policy compatibility,
- authority requirements.

## Hard constraints before scoring

Options that violate hard policy constraints should not compete normally with permitted options.

Examples:

- unauthorized spend,
- prohibited data movement,
- credit actions outside delegated authority,
- legal commitments without approval,
- actions that conflict with explicit executive policy.

The sequence should be:

```text
Generate options
      |
      v
Apply hard constraints
      |
      v
Remove / escalate prohibited options
      |
      v
Compare permitted options
      |
      v
Rank against active objectives
      |
      v
Explain recommendation
```

## Ranking model

A production system may use weighted scoring, optimization or decision-analysis methods, but the public architecture requires the reasoning to remain visible.

A conceptual form is:

```text
Recommendation value =
objective alignment
+ expected business benefit
+ reversibility value
+ speed value
- downside exposure
- execution burden
- uncertainty penalty
- policy conflict
```

The exact weights should be organization-specific and governed by the Company Control Plane.

## Recommendation statuses

- **preferred** — strongest option under current objectives and evidence.
- **viable_alternative** — reasonable option with different trade-offs.
- **conditional** — attractive only if a stated condition becomes true.
- **not_recommended** — permitted but materially inferior under current evidence.
- **policy_blocked** — conflicts with a hard constraint.
- **insufficient_evidence** — cannot be ranked responsibly yet.

## Recommendation explanation

Every preferred recommendation should answer:

1. Why this option ranks first.
2. Which objective it best supports.
3. What its biggest downside is.
4. Which assumption matters most.
5. What event would cause the recommendation to change.
6. Whether approval is required.

## Example

For Orion project P002:

### Preferred — Option B
Require commercial approval before additional discretionary scope and prepare a joint Finance + Sales + Operations intervention.

**Why it ranks first**

It addresses both margin leakage and cash conversion while preserving more relationship flexibility than a full scope freeze.

**Primary objective alignment**

Protect project economics and near-term cash without unnecessarily damaging a strategic account.

**Main downside**

The customer may perceive the new control as friction and delivery may slow while scope is reconciled.

**Critical assumption**

The customer remains willing to negotiate outstanding scope changes.

**Recommendation changes if**

The customer rejects commercial reconciliation or additional work materially increases financial exposure.

**Approval**

Required before customer-facing restrictions or contractual changes.

## Avoid false objectivity

A numerical score can be useful internally, but executives should never receive a recommendation that appears objective merely because it has a decimal number attached to it.

The system should expose:

- the criteria,
- material assumptions,
- trade-offs,
- uncertainty,
- and policy context.

## Learning loop

After an approved action is executed, the system should compare actual outcomes against the Decision Packet:

```text
Decision
  -> action
  -> measured outcome
  -> assumption validation
  -> recommendation-quality review
  -> future calibration
```

This creates a path from static decision support toward an enterprise system that learns which recommendations actually produce better business outcomes.
