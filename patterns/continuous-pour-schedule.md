---
name: "The Continuous Pour Schedule"
scale: instrument-strategy
status: approximation
forces: [Finite Resources, Partial Failure]
generators: [Gate on Environmental Readiness]
problem: "A homogeneous fan-out against a rate-limited vendor hits the limit mid-wave, and the interruption (a cold joint) leaves partial generation of inconsistent vintage."
signals:
  - "bulk generation where 'how fast we can dispatch' hits 'how fast the vendor can absorb'"
  - "a mid-wave 429 would leave half a wave at one vintage and half at another"
  - "the run's own rate-limit receipts show interruptions nobody planned for"
stages:
  - name: pour-plan
    sheets: 1
    instrument_guidance: "any-wrapped CLI, per_sheet_fallbacks: [] — computes zones → waves from the work manifest; per-instrument concurrency and DOCUMENTED rate limits are authoring-time inputs (a score cannot derive vendor limits from an alias declaration)"
    fallback_friendly: false
    purpose: "The supply-continuity plan; writes pour-plan.yaml (wave assignments, per-wave stagger, joint plan)."
  - name: wave-N
    sheets: fan_out(K) per wave
    instrument_guidance: "work instruments; stagger_delay_ms matched to the vendor's documented rate limit — same-instrument spacing (V4)"
    fallback_friendly: true
    purpose: "Dependency-ordered waves; each wave bonds to its predecessor's prepared joint."
  - name: wave-N-joint
    sheets: 1 per wave
    instrument_guidance: "any-wrapped CLI — the SINGLE NAMED WRITER of joints.jsonl: wave id, members, output digests"
    fallback_friendly: false
    purpose: "The planned joint: a prepared, keyed, doweled surface — the DAG position serializes the write."
  - name: cure-audit
    sheets: 1
    instrument_guidance: "any-wrapped CLI, per_sheet_fallbacks: [] — every planned joint has a receipt, no wave launched before its joint predecessor's receipt existed"
    fallback_friendly: false
    purpose: "Cold-joint detection is the absence of a receipt at a wave boundary."
dependencies:
  wave-1: [pour-plan]
  wave-1-joint: [wave-1]
  wave-2: [wave-1-joint]
  cure-audit: [wave-N-joint]
composes_with:
  - pattern: "The Rostered Watch"
    how: "stagger claim corrected (V4) — this pattern carries the corrected doctrine; the watch bill's wave/handoff half survives on dependency ordering"
  - pattern: "The Watch Rollover"
    how: "the joint receipt is a watch-boundary pass-down specialized to wave seams"
  - pattern: "Circuit Breaker"
    how: "a wave's cold joint is the trip condition at fan-out granularity"
  - pattern: "Firing the Pass"
    how: "clock-arithmetic cousin at the pass (permanent-corpus side)"
type: orchestration-pattern
---

## The Continuous Pour Schedule

**Status:** approximation — `stagger_delay_ms` native-unproven (V4 semantics: per-instrument spacing); one minimal verification score serves this pattern and the benched Ramp Meter's shared flag. Differentiation from Rostered Watch/Watch Rollover stated: those own the watch bill and handover; this owns *supply continuity under a rate limit* — paced dispatch plus joint receipts.

**Core Dynamic.** A mat pour fails not because the concrete is bad but because the trucks stopped coming: an interruption mid-pour creates a **cold joint** — fresh against partially hardened — a structural defect, not a cosmetic one. So the plan is a *supply-continuity plan*: zoned pours in deliberate sequence, guaranteed truck spacing, pour rate matched to crew capacity — and where the pour must stop, *planned* construction joints (prepared, keyed, doweled surfaces) instead of accidental ones. The V4-corrected core: `stagger_delay_ms` is a **same-instrument spacing rule** (dispatch.py:65-66) — exactly a truck-spacing rule for one batching plant. Mixed-instrument fan-outs have as many independent pour sequences as instruments; with `select: balance` on a multi-vendor alias, balance spreads across plants while stagger spaces each plant's trucks — they compose.

**Repairs applied (the Skeptic's two):** joint receipts have a **single named writer** — each wave ends in its own `wave-N-joint` CLI sheet that writes the receipt after the wave's members complete; "last-completing sheet appends" was not an owner and invited concurrent writes. And the alias-derived rate-limit claim is **cut**: documented limits are an authoring-time input to `pour-plan`; the score cannot read a vendor's mind. The stagger negative control is honest about its own limits: set stagger 0 against a venue with a *documented* rate limit and the run's own 429 receipts must show the cold joint; *if the venue has no rate limit, the negative control is untestable there and the pattern says so* — a negative control you cannot run is a confession, not a control.

**Example.** 500-document summarization fan-out against one vendor alias: pour-plan splits 25/wave with stagger 1500ms (tier allows 20 rpm); wave 3 loses two members to a vendor incident → the joint receipt records the gap → wave 4's prompts carry the gap notice (the keyed surface) → cure-audit names the two missing documents in the final report instead of the summary silently covering 498.

### Review Integration

Integrated from discover pass 2 (cycle 7) after three adversarial reviews (Practitioner, Skeptic, Newcomer); this pattern's specific repairs are itemized in `discover-pass-2/06-the-corpus.md` § Review Integration and the Reconciliation Appendix.
