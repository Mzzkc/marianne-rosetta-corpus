---
name: "The Mock-Up Bay"
scale: iteration
status: approximation
forces: [Exponential Defect Cost, Progressive Commitment]
generators: [Incremental Exposure, Gate on Environmental Readiness]
problem: "The cost of discovering a detail defect at unit N=400 exceeds one observed unit N=1, but volume production starts without a representative first article under independent inspection."
signals:
  - "mass content generation, template instantiation, codegen rollout, migration waves"
  - "a detail defect would replicate silently across the whole volume"
  - "acceptance criteria are being negotiated after candidates exist"
stages:
  - name: rubric-press
    sheets: 1
    instrument_guidance: "strong reasoner + CLI digest pin — pre-registers the rubric BEFORE any candidate exists; rubric.yaml digest-pinned"
    fallback_friendly: false
    purpose: "Pre-registration is what makes the inspection a test rather than a negotiation (C1)."
  - name: build-candidate
    sheets: 1
    instrument_guidance: "production instrument, production prompt — produces exactly ONE representative artifact"
    fallback_friendly: true
    purpose: "The actual assembly, executed once, under observation."
  - name: inspect
    sheets: 1
    instrument_guidance: "DIFFERENT instrument family; reads the artifact against the pre-registered rubric; writes verdict.json via response_format (typed: pass/fail + defect classes)"
    fallback_friendly: false
    purpose: "Independent sign-off; the builder's own sign-off is a paint sample, not a mock-up."
  - name: refine-brief
    sheets: 1
    instrument_guidance: "reads verdict defects; writes the next iteration's correction memo into the builder's input slot"
    fallback_friendly: true
    purpose: "Feed the loop; rounds are bounded by count."
dependencies:
  inspect: [build-candidate]
  refine-brief: [inspect]
composes_with:
  - pattern: "The Serial Troponin"
    how: "Troponin owns the monotone serial-test spine; this owns the representative-first-article loop with independent sign-off"
  - pattern: "The Unprimed Falsifier"
    how: "its reader panels are this pattern's inspector tier at full adversarial depth"
  - pattern: "First Article Characterization"
    how: "compose its measurement half with this loop's approval half"
  - pattern: "The Wordless Manual (via Prefabrication)"
    how: "production fan-out consumes the approved pattern as template"
  - pattern: "Unison Drift"
    how: "the drift check before the volume spend this pattern gates"
type: orchestration-pattern
---

## The Mock-Up Bay

**Status:** approximation — `sheet.loops` and `response_format` native-unproven (zero proof executions corpus-wide for either); this and Serial Troponin are the two natural first proofs of the loop primitive. **The Newcomer's designation stands: this is the newcomer's first score** — five sheets, one unproven primitive, concrete syntax in Composition Doctrine #6.

**Core Dynamic.** Nobody replicates a facade detail forty stories up before the architect, the waterproofing consultant, and sometimes the AHJ have signed off on a full-scale mock-up — one representative section, production materials, production crews, standing on the ground where everyone can interrogate it. The mock-up is not a drawing review; it is *the actual assembly, executed once, under observation, before commitment to volume.* The deep structure: **the loop's exit condition must be an artifact written by someone other than the builder** — a mock-up the builder signs off themselves is a paint sample, not a mock-up. And the rubric is pre-registered BEFORE any candidate exists (C1). V6 arms the negative discipline: an `until` expression that errors kills the span E999 (fail-closed), so the verdict-file schema is load-bearing validation, not decoration.

**The reduction (the Skeptic's):** the minimal loop proof is rubric-press → build → inspect → refine under the Composition Doctrine #6 loop block; the post-loop production fan-out (width N) is composition, not proof burden — it rides *after* loop exit and is ordinary proven fan-out.

**Sentinels.** A: a seeded defective candidate must produce verdict fail and the loop must iterate (round odometer ≥ 2; exit 1 if production ran after round 1). B: remove the `until` clause → the count-bound loop still terminates but the fixture's defective candidate ships to production → production's own validation fails on the seeded defect marker — proving the exit condition, not the count, is the gate.

**Example.** Brand-voice content farm: one representative article built, inspected against a pre-registered voice rubric by a different instrument, correction memos looped (max 3 rounds), then 400 articles fanned out from the approved pattern.

### Review Integration

Integrated from discover pass 2 (cycle 7) after three adversarial reviews (Practitioner, Skeptic, Newcomer); this pattern's specific repairs are itemized in `discover-pass-2/06-the-corpus.md` § Review Integration and the Reconciliation Appendix.
