---
name: "The Torque-Verify Pass"
scale: within-stage
status: working
forces: [Exponential Defect Cost, Instrument-Task Fit]
generators: [Match Instrument to Grain]
problem: "Schema-valid garbage propagates silently because schemas cannot express the semantic invariants (arithmetic, entailment, domain constraints) that make output true."
signals:
  - "structured-output producers at volume where a wrong number looks exactly like a right one"
  - "a sampled deep check over a systematically mis-generated population is confident nonsense"
  - "cheap complete coverage is possible but unclaimed"
stages:
  - name: produce
    sheets: fan_out(N)
    instrument_guidance: "work instruments; response_format: json_schema per unit (V5 engine gate)"
    fallback_friendly: true
    purpose: "Produce typed units whose schema the engine itself validates."
  - name: torque-verify
    sheets: fan_out(N)
    instrument_guidance: "cheap, fast, DIFFERENT instrument family (local ollama or pure CLI — for deterministic invariants CLI IS the second wrench); width 1:1 with produce units, one declared invariant set per unit"
    fallback_friendly: true
    purpose: "Re-check the semantic invariants schemas cannot express; write marks/{unit}.json (unit id, checks run, pass/fail)."
  - name: walk-the-steel
    sheets: 1
    instrument_guidance: "any-wrapped CLI, per_sheet_fallbacks: [] — audit: every produced unit has a mark, every mark passes, marks count = units count"
    fallback_friendly: false
    purpose: "Enforce the bijection; unmarked units are audit failures by definition."
dependencies:
  torque-verify: [produce]
  walk-the-steel: [torque-verify]
composes_with:
  - pattern: "Immune Cascade"
    how: "owns the depth-tiering AFTER this pass"
  - pattern: "Concurrent Count"
    how: "the audit is its dual enumeration institutionalized"
  - pattern: "Readback Before Commit"
    how: "V5's schema gate is the readback; this is the semantic hearback the schema cannot do"
  - pattern: "The Mock-Up Bay"
    how: "units that fail here enter its loop"
type: orchestration-pattern
---

## The Torque-Verify Pass

**Status:** working · primitives-proven (`response_format` schema-validated per V5; the semantic-recheck composition itself unexecuted).

**Core Dynamic.** The ironworker torques the bolt and *marks it* — and on critical joints a second qualified person independently verifies with their own wrench. The mark does not make the bolt tight; it makes the verification **visible and auditable without re-doing it**. **The invariant, stated generically (the Skeptic's demand): total-domain cheap verification + producer-to-mark bijection.** Uniform depth, complete coverage, receipted — *before* any sampling, because a sampled deep check of a systematically mis-torqued population is confident nonsense. The verify pass consumes the producer's engine-validated structured output (V5) and re-checks what schemas cannot express: does the number add up? is the claim entailed by the cited source?

**Repair applied (the Skeptic's):** the draft's "calibration negative" — proving a same-family reviewer must *miss* a seeded entailment flaw — is demoted from validation control to documented limitation. A control whose pass condition depends on a correlated reviewer happening to miss a specific flaw is not a control; it is a hope with a fixture. The Independence Law remains the design rule (a second wrench from the same toolbox is the painter's mark); the *proof* of the pass is the bijection audit, not the correlated failure.

**Sentinels.** A seeded arithmetic-flawed unit must fail its mark and the audit names it (exit 1). A seeded plan mismatch (a unit with no verify instance) must fail the bijection.

**Example.** Financial-data extraction: 1,000 filings → structured records; torque-verify re-checks each record's arithmetic (segments sum to total, percents ≤ 100, dates parse and order) with a cheap deterministic instrument; 7 fail, are named, and go to the adversarial tier while 993 proceed — complete cheap coverage first, sampled expensive depth second, each tier doing what it alone can do.

### Review Integration

Integrated from discover pass 2 (cycle 7) after three adversarial reviews (Practitioner, Skeptic, Newcomer); this pattern's specific repairs are itemized in `discover-pass-2/06-the-corpus.md` § Review Integration and the Reconciliation Appendix.
