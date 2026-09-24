---
name: cash-flow-risk
description: Find where cash is trapped across receivables, unbilled work, disputes and supplier terms, rank the cash traps by amount and urgency, and recommend collection or invoicing actions. Use when an executive asks about cash flow, liquidity, overdue invoices, DSO or working capital ("¿dónde se queda atrapada la caja?", "tesorería", "cobros pendientes", "flujo de caja").
---

# Cash-Flow Risk

Answer **"Where is cash getting trapped?"** by connecting finance, customer and delivery signals. Cash problems are rarely only a finance problem.

## 1. Find the data

Use the user's own data first (attached AR ageing, invoice exports, bank or ERP data, connected tools). State how their columns map to the concepts below.

If no company data is available, or the user asks for a demo, use `../../demo-data/` (relative to this skill's directory) and say the answer uses synthetic data.

| Concept | Demo file | Key fields |
|---|---|---|
| Cash trajectory | `monthly_financials.csv` | cash_balance, accounts_receivable, accounts_payable |
| Receivables | `invoices.csv` | amount, amount_paid, status, days_overdue, expected_collection_date, notes |
| Unbilled work | `projects.csv` | unbilled_scope_change_eur, completion_pct |
| Customer behaviour | `customers.csv` | payment_terms_days, avg_payment_delay_days, relationship_health |
| Supplier terms | `suppliers.csv` | payment_terms_days |
| Signals | `events.csv` | missed payment promises, disputes, complaints |

Compute everything with code.

## 2. Investigate

1. **Trajectory.** Cash and AR trend over the window. Is cash falling while AR rises?
2. **Outstanding by customer.** Group unpaid amount (amount − amount_paid) by customer. Separate *normal open, not yet due* from *overdue* from *disputed*.
3. **Root cause per trap.** Link each overdue balance to its project and events: a scope dispute, a delivery complaint, repeated missed promises, or a purely administrative delay.
4. **Unbilled work.** Work performed but not invoiced is cash that hasn't started its collection clock yet.
5. **Terms mismatch.** Compare customer payment terms (plus actual delay) with supplier payment terms. If the company pays suppliers faster than it collects, it is financing its customers.

## 3. Reasoning discipline

- **Fact:** an invoice is overdue or partially paid.
- **Inference:** a linked operational or commercial issue is likely delaying collection.
- **Not justified:** predicting a customer default without strong evidence. Flag the risk, don't declare it.

## 4. Output

Follow `../../references/response-format.md`. The core is a **ranked cash-trap table**:

| # | Customer / source | € trapped | Type (overdue / disputed / unbilled / terms) | Root cause | Urgency | Confidence |

Then add business impact (e.g. the cash runway effect if collections slip another month), recommended actions and evidence.

Recommended actions may include: a collections escalation, a customer meeting, faster commercial approval for scope changes so they can be invoiced, issuing pending milestone invoices, and reviewing terms on new contracts.

## Approval boundary

Prepare and recommend only. Do **not** send communications, renegotiate terms, suspend customers or change accounting records without explicit human approval.

## Demo benchmark (Northstar)

A correct answer shows cash falling from €1.18M to €680k while AR rises from €980k to €1.51M. It surfaces Orion (I003/I004, ~€500k unpaid, scope reconciliation), Delta Water (I009/I010, €215k overdue, repeated missed promises), Helios I001 (€100k, change-order dispute), NovaGlass I007 (€80k, open delivery complaint) and unbilled scope in active projects.
