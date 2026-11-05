---
name: "The Priced Verification Ladder with Budget-Forced Degradation"
scale: instrument-strategy
status: approximation
forces: [Finite Resources, Exponential Defect Cost]
generators: [Graduate & Filter]
problem: "Verification spend compounds unbounded when every artifact gets the deepest affordable check, and degradation under budget pressure is silent."
signals:
  - "verification is a real fraction of total cost across long runs or concert chains"
  - "N× adversarial review for every artifact would kill the run's economics"
  - "budget pressure has quietly downgraded review quality with no record"
stages:
  - name: produce-and-classify
    sheets: fan_out(N)
    instrument_guidance: "work instruments; every artifact's risk_class (low|standard|critical) comes from the COMPOSER-AUTHORED class map keyed on artifact type, never producer self-classification"
    fallback_friendly: true
    purpose: "Produce typed units carrying a declared risk class assigned at creation."
  - name: ledger-update
    sheets: 1
    instrument_guidance: "any-wrapped CLI, per_sheet_fallbacks: [] — computes estimated spend from captured output token counts / character lengths and appends to budget-ledger.jsonl BEFORE the next tier's skip_when evaluates"
    fallback_friendly: false
    purpose: "The explicit spend-capture mechanism the draft lacked; the ledger is not writable by the agents whose work it meters."
  - name: tier-1
    sheets: 1
    instrument_guidance: "CLI validation only (schema, lint, structure) for everything"
    fallback_friendly: false
    purpose: "The cheap tier that is always already running."
  - name: tier-2
    sheets: fan_out(M)
    instrument_guidance: "single-instrument review sheets; skip_when guard: risk_class == low"
    fallback_friendly: true
    purpose: "Bought only for standard-and-above artifacts."
  - name: tier-3
    sheets: fan_out(2)
    instrument_guidance: "adversarial pair, opposing mandates, different vendors — vendor diversity IS the adversarial value; skip_when guard: remaining_budget_below_threshold (reads budget-ledger.jsonl)"
    fallback_friendly: false
    purpose: "The expensive tier; when the envelope thins, it collapses — receipted."
dependencies:
  tier-1: [produce-and-classify, ledger-update]
  tier-2: [tier-1]
  tier-3: [tier-2]
composes_with:
  - pattern: "Echelon Repair"
    how: "its before-failure dual — Repair tiers responses after failure; this prices verification before"
  - pattern: "Immune Cascade"
    how: "tier skeleton (the Skeptic's fold objection answered: the skeleton is shared, the economics are new — descent-on-envelope is the distinct claim, and it is flagged approximation until proven)"
  - pattern: "Rent-Then-Commit"
    how: "the rent/buy decision at each rung transition"
  - pattern: "Dispatch with Declared Penalty"
    how: "the ladder supplies the prices; the CDL supplies the aggregate admission check"
type: orchestration-pattern
---

## The Priced Verification Ladder with Budget-Forced Degradation

**Status:** approximation — **the mid-score degradation behavior is unverified** and says so on its face (the Skeptic: `skip_when` is fail-open, the budget ledger's integrity and timing were unspecified, and `cost_limit_usd` is not evidence of a readable remaining-budget value). What is proven: the guards evaluate; the ledger is an ordinary file; the tiers are ordinary sheets.

**Core Dynamic.** Verification depth is a purchase, and the currency is finite. The immune system never escalates everything: innate response is the cheap tier always already running; antibodies and clonal expansion are bought only when cheap-tier receipts come back "not clearing." Three moves: **declared prices on every rung**; **risk-classed entry** (set at creation by the composer's class map, never at review time by the thing being judged — the Skeptic's capture fix); **envelope-forced descent** — when remaining budget thins, rungs collapse downward and the collapse is *receipted*. The pattern's soul: **when it degrades, the organism does not silently skip the top tier — it records the fever it did not mount.** A logged degradation is a risk consciously accepted; a silent skip is a lie the ledger will eventually bill (C5).

**The repair (the Practitioner's missing mechanism):** the draft read "remaining budget" from a ledger nothing wrote. Now an explicit `ledger-update` CLI step runs between tiers: it computes estimated spend from the run's captured output token counts / character lengths and appends to `budget-ledger.jsonl` — a workspace file the metered agents cannot write — *before* the tier-3 guard reads it. `cost_limit_usd` rides at job level as the hard brake.

**Sentinel pair (both polarities, unexecuted until the prove path lands them):** a fat-budget run must produce *zero* degradation receipts (a sentinel script fails if any receipt exists); a thin-budget run must produce receipts naming the rung skipped and the budget at decision time. Until this pair has executed, budget-forced descent is doctrine, not fact — and the pattern's status line says exactly that.

**Example.** Legal-doc processing: bulk standard contracts get tier-1 structural validation only; anything touching indemnity enters at tier 3; when the month's API budget is 80% spent, tier-3 collapses to tier-2 for everything and the receipts say which documents got the weaker look.

### Review Integration

Integrated from discover pass 2 (cycle 7) after three adversarial reviews (Practitioner, Skeptic, Newcomer); this pattern's specific repairs are itemized in `discover-pass-2/06-the-corpus.md` § Review Integration and the Reconciliation Appendix.
