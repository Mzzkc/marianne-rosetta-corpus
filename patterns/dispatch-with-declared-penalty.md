---
name: "Dispatch with Declared Penalty (CDL)"
scale: score-level
status: working
forces: [Finite Resources, Partial Failure]
generators: [Threshold-Triggered Switch]
problem: "Deviations are checked per-row, so two individually tolerable deviations jointly breach a margin without anyone seeing the sum."
signals:
  - "a cheap instrument down lowers guarantees without canceling the run"
  - "fleet members accumulate small deviations that must be summed, not listed"
  - "the individually-tolerable-jointly-not check is currently nobody's job"
stages:
  - name: margin-gate
    sheets: 1
    instrument_guidance: "any-wrapped CLI, per_sheet_fallbacks: [] — enumerates open deviations from the census, joins against the authoring-time penalty-table, combines per each margin's declared combination law, compares against margins.yaml (composer-owned file permissions as authority); fails closed on any breached margin even if every individual deviation is inside its own row's bounds"
    fallback_friendly: false
    purpose: "The aggregate admission check — the sum matters, not the rows."
  - name: ledger-update
    sheets: 1
    instrument_guidance: "any-wrapped CLI, per_sheet_fallbacks: [] — appends MEASURED actuals to penalty-actuals.jsonl at run end"
    fallback_friendly: false
    purpose: "Close the loop for the next composition's price revision."
dependencies:
  ledger-update: [margin-gate]
composes_with:
  - pattern: "The Dispatch Catalogue (MEL)"
    how: "side-by-side decision tables — MEL owns procedural compensation, CDL owns the aggregate sum"
  - pattern: "The Priced Verification Ladder"
    how: "the ladder supplies the price tags; this supplies the admissible-sum check"
  - pattern: "Capability Census"
    how: "census says what is down; the table says what it costs; the gate says whether the mission still flies"
  - pattern: "Rent-Then-Commit"
    how: "per-instance rent/buy vs aggregate admission — different objects"
type: orchestration-pattern
---

## Dispatch with Declared Penalty (CDL)

**Status:** working · primitives-proven. The Practitioner: "Crisp and actionable… the jq aggregation script is trivial to write, the gate is fail-closed, and the aggregate breach sentinel is clearly specified."

**Core Dynamic.** MEL says "fly despite the broken thing, *compensating* procedurally." CDL says "fly despite the missing thing, *paying* quantitatively" — and the payment is checked **in aggregate**: dispatch is authorized iff the mission's declared margins absorb the *total* declared penalty of all open deviations. Two deviations each individually benign can jointly breach a margin; the CDL discipline is what makes that visible, because the gate's arithmetic is over the sum — the individually-tolerable-jointly-not check that naive per-row checking passes, which is the pattern's entire reason to exist.

**The penalty algebra (the Skeptic's demand — without it, jq produces precise nonsense):** every penalty is declared in **named units** (`coverage_pct`, `confidence_delta`, `cost_usd`, `latency_p95_ms`); every margin declares its **combination law** — sum for additive units, max for latencies, product for probabilities — and the combination is computed in the margin's declared unit; **correlated deviations must be declared co-priced** (two deviations from one vendor share a correlation entry, else the sum double-discounts the same underlying failure — the ETOPS caveat: independence assumptions are defeated by same-batch engines); **margins are owned** by the composer's `margins.yaml`, written with the score and never writable by the run — file permissions as an authority mechanism (the same authority-by-file-permission doctrine as the Hold-Point roster and the pulse keeper, stated once in Composition Doctrine). A unit that cannot be declared honestly (quality "points" with no defined combination law) is a MEL compensation row instead, not a CDL penalty.

**Sentinel — the aggregate breach:** two individually-bounded deviations summing past a margin must exit nonzero with `margin-report.json` showing both rows, the combined value, and the breached `margin_key`. Named artifact, named command, named exit code.

**Example.** Market-intelligence pipeline: three of seven sources down (each: coverage −4%, confidence −0.1); sentiment model on fallback tier. Individually fine. The gate combines: coverage 83% — below the client's declared 85% floor for the "comprehensive" tier. The run dispatches *downgraded to standard with a typed downgrade notice* or waits for a source — the client contract, not a runtime judgment, decides. The actuals ledger records what the downgrade really cost; next quarter's margins are repriced from evidence.

### Review Integration

Integrated from discover pass 2 (cycle 7) after three adversarial reviews (Practitioner, Skeptic, Newcomer); this pattern's specific repairs are itemized in `discover-pass-2/06-the-corpus.md` § Review Integration and the Reconciliation Appendix.
