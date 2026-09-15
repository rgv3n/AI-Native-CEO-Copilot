# Scenario and Trade-off Model

## Purpose

The Scenario and Trade-off Model gives the Executive Decision Engine a disciplined way to compare plausible courses of action without pretending to predict the future with certainty.

The goal is decision support, not false forecasting precision.

## Scenario structure

Each option should be tested against at least three practical scenarios when material uncertainty exists:

- **Expected case** — the most plausible outcome under current evidence.
- **Upside case** — a favorable but credible outcome.
- **Downside case** — a material adverse outcome that leadership should understand.

Optional scenario dimensions may include:

- cash impact,
- gross-margin impact,
- revenue impact,
- customer relationship impact,
- delivery risk,
- operational load,
- strategic value,
- reversibility,
- time to effect,
- execution complexity,
- regulatory or governance risk.

## Trade-off principle

A recommendation should not only say what is best.

It should explain what the company is accepting in exchange.

Example:

> Requiring commercial approval before additional Orion scope is likely to improve economic control, but may increase short-term customer friction and could slow delivery.

That sentence is more useful than a single numeric score because it exposes the management trade-off.

## Option comparison model

A normalized option record can include:

```yaml
option_id:
name:

business_effects:
  cash:
  margin:
  revenue:
  customer:
  delivery:
  strategic_value:

execution:
  time_to_effect:
  complexity:
  reversibility:
  dependencies:

risk:
  downside_severity:
  downside_probability_band:
  policy_conflicts:

scenario_assumptions:
  - assumption:
    evidence_ref:
    confidence:

expected_case:
upside_case:
downside_case:
```

## Probability discipline

The public reference should prefer probability bands over invented point estimates where data does not justify precision.

Recommended bands:

- very low,
- low,
- medium,
- high,
- very high.

If a calibrated statistical model exists in a production deployment, numeric probabilities may be used, but they should remain traceable to that model and its validation history.

## No-action scenario

Every material Decision Packet should include a **no-action scenario**.

This is important because maintaining the current path is itself a decision.

The engine should explicitly compare:

```text
Act now
vs
Delay
vs
Do nothing
```

## Sensitivity analysis

The recommendation should identify which assumptions matter most.

Example:

- If Orion accepts commercial approval within 10 days, Option B remains preferred.
- If the customer rejects the scope reconciliation and threatens cancellation, Option C may become preferable.
- If the disputed work is contractually unrecoverable, the economic case changes materially.

The point is not to generate every possible future.

The point is to tell the executive:

**What would have to change for the recommendation to change?**

## Strategic objective alignment

Scenario evaluation should reference the active objectives in the Company Control Plane.

An option can therefore be attractive financially while ranking poorly overall if it violates a higher-priority objective or policy.

Example:

```text
Option: aggressive credit hold
Cash protection: high
Customer impact: high negative
Strategic-account policy conflict: yes
Overall recommendation: not preferred without executive override
```

## Anti-patterns

Avoid:

- fabricated ROI,
- precise probabilities without a calibrated model,
- scoring systems whose weights are invisible,
- treating all criteria as equally important,
- burying downside scenarios,
- optimizing one department at the expense of company objectives,
- recommending an action without considering doing nothing.

## Executive output

The CEO should be able to see the decision as a compact comparison:

| Option | Upside | Main trade-off | Downside risk | Reversible? | Alignment |
|---|---|---|---|---|---|
| A | Low friction | Continued exposure | High | Yes | Weak |
| B | Better economic control | Customer friction | Medium | Mostly | Strong |
| C | Maximum protection | Relationship / delivery risk | High | Partly | Conditional |

The engine can recommend B while still making clear why A or C could become preferable under different assumptions.
