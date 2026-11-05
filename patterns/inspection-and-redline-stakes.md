---
name: "The Inspection and Redline Stakes"
scale: concert-level
status: working
forces: [Partial Failure, Exponential Defect Cost]
generators: [Threshold-Triggered Switch]
problem: "'All upstream fully green' (the engine's only fleet dependency semantics, V3) is stricter than downstream work often needs, so partial evidence is either silently starved or silently consumed."
signals:
  - "multi-score workflows where downstream wants to begin on partial upstream evidence"
  - "crawl-then-summarize, migration-then-verification chains"
  - "starved groups are logged as a warning and moved on (fleet.py:314-319) — and nobody surfaces it"
stages:
  - name: upstream-fleet
    sheets: fan_out(N)
    instrument_guidance: "member scores of group A; each writes receipt-{member}.json (digest + status)"
    fallback_friendly: true
    purpose: "Produce receipts; arrival is asynchronous."
  - name: admit
    sheets: 1
    instrument_guidance: "any-wrapped CLI, per_sheet_fallbacks: [] — jq over the receipt set vs the AUTHORING-TIME tolerance.yaml (required receipts, per-receipt digest expectations, degrade policy, AND a readiness deadline); bounded by max_wall_seconds; emits admission.json: FULL, PARTIAL (with skip list), or HALT"
    fallback_friendly: false
    purpose: "The downstream score's first breath: stakes driven before the concrete truck arrives."
  - name: body
    sheets: fan_out(M)
    instrument_guidance: "downstream sheets 2+; per-sheet skip_when is the refusal predicate consulting admission.json's skip list"
    fallback_friendly: true
    purpose: "Work on what was admitted; skip-listed work is visibly absent, not silently missing."
dependencies:
  admit: [upstream-fleet]
  body: [admit]
composes_with:
  - pattern: "Admission by First Cycle"
    how: "pass-1 pattern DEMOTED after V3 — this is its honest successor; the permanent corpus's DAG edge is rewritten"
  - pattern: "Fleet Receipt Ledger"
    how: "the ledger owns bijection accounting; this owns tolerance-declared partial admission"
  - pattern: "The Validity Window"
    how: "receipt TTLs are the stakes' expiry dates"
  - pattern: "The Dispatch Catalogue (MEL)"
    how: "different questions, different table owners: MEL = may WE run degraded (ex-ante authorization); CDL = can the margins absorb the sum (economics); Stakes = what may DOWNSTREAM consume (partial admission across the boundary)"
type: orchestration-pattern
---

## The Inspection and Redline Stakes

**Status:** working · primitives-proven (artifact gates); the fleet face rides the `fleet` proof debt. Ranked #19 by the collision; the Practitioner called it "superb," the Newcomer "demotion done right" and ranked it top-tier.

**Core Dynamic.** The inspector does not write prose reports; they *redline the artifact itself* — deviations marked on the drawing, bound to the exact location they correct — and the tolerance stakes are driven into the ground *before* the concrete truck arrives, so acceptance is observable by anyone, not adjudicated at pour time. Two load-bearing ideas: deviation expressed **against** the artifact, not about it; tolerance **physical and pre-placed**. V3's refutation made this pattern necessary: `fleet.depends_on` waits on full successful completion (fleet.py:337-360), so "admission by first cycle" is dead — but the need it served is real. The honest replacement: the dependent score's admission condition is a **staked tolerance file** — written at authorship, checked by the downstream score's OWN first sheet, degrading explicitly: partial receipt sets produce a visible, receipted **"admitted-with-redlines"** state listing what is missing, never a silent AND-starvation.

**The race, fixed (the Skeptic's):** absent fleet dependencies, admit could run before optional receipts arrive and call temporary absence a legitimate PARTIAL. Now `tolerance.yaml` declares a **readiness deadline**: absence is not legible as PARTIAL until the deadline passes — missing-vs-not-yet is a typed transition with a timestamp, and admit is bounded by `max_wall_seconds` so the deadline is real.

**Sentinels.** Full fixture set → FULL. Seeded missing receipt after deadline → PARTIAL with the right skip list. **The failure-class distinction:** corrupt one receipt's *digest* → admit must emit HALT, not PARTIAL — a digest mismatch is tampering, not absence; different failure class, different verdict. And the stakes written by the upstream producer die on contact — stakes set by the grading crew are not inspection, they're ambition.

**Example.** Market-research concert: 8 regional crawl scores write receipts; the synthesis score's tolerance declares 5 critical regions + 3 nice-to-have; two crawls fail → admission is PARTIAL, synthesis runs with the two regions marked data-absent in its output's caveats, and the concert log carries the redline — anyone reading knows exactly what the synthesis did not see.

### Review Integration

Integrated from discover pass 2 (cycle 7) after three adversarial reviews (Practitioner, Skeptic, Newcomer); this pattern's specific repairs are itemized in `discover-pass-2/06-the-corpus.md` § Review Integration and the Reconciliation Appendix.
