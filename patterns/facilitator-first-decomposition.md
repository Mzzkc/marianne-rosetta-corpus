---
name: "Facilitator-First Decomposition"
scale: score-level
status: working
forces: [Producer-Consumer Mismatch, Instrument-Task Fit]
generators: [Contract at Interfaces]
problem: "Dependency edges are unclassified, so wave-1 artifacts that prepare the environment, wave-2 artifacts that coexist with it, and early commitments that BLOCK later designs all look identical in the DAG."
signals:
  - "two-wave scores: scaffolding before implementation, fixtures before adversarial testing, ground truth before evaluation"
  - "refactor/rebuild work where the first act must be REMOVING an existing commitment"
  - "a premature schema freeze is silently inhibiting the better late design"
stages:
  - name: classify-edges
    sheets: 1
    instrument_guidance: "strong reasoner — every planned dependency declared in edges.yaml: facilitate | tolerate | inhibit; an UNDECLARED edge fails validation (this is the enforcement point)"
    fallback_friendly: false
    purpose: "The three-way classification each dependency edge must declare; undeclared defaults to tolerance, and that assumption is where scores rot."
  - name: wave-1
    sheets: fan_out(N)
    instrument_guidance: "mid-tier instruments; artifacts typed and validated for USABILITY BY WAVE 2, not final quality"
    fallback_friendly: true
    purpose: "Facilitators: environmental modification, not deliverables."
  - name: inhibit-release
    sheets: 1
    instrument_guidance: "custom git CLI instrument, conditional (skip_when: no inhibit edges) — formally retires the blocking artifact (moves schema-v1.yaml to retired/, writes a release receipt); a receipt you can forge with prose is not a receipt"
    fallback_friendly: false
    purpose: "The deliberate, receipted disturbance that releases inhibition."
  - name: wave-2
    sheets: fan_out(M)
    instrument_guidance: "mixed by risk class; prelude-injected with wave-1 artifacts per the manifest"
    fallback_friendly: true
    purpose: "The tolerant main body, establishing on prepared soil."
dependencies:
  wave-1: [classify-edges]
  inhibit-release: [wave-1]
  wave-2: [inhibit-release]
composes_with:
  - pattern: "Keystone-First Sequencing"
    how: "shares the wave-1 discipline; keystone output is the point, facilitator output is the soil — fold refused at collision, different decision authority"
  - pattern: "The Attested Merge Gate"
    how: "receipts feed it"
  - pattern: "The Change-Order Ledger"
    how: "a release receipt is an authorization-shaped mutation, recorded"
type: orchestration-pattern
---

## Facilitator-First Decomposition

**Status:** working · primitives-proven (alongside Keystone-First, the prove path's easiest new pair). **Repair applied (the Skeptic's polarity catch, same as Watchman's Gate):** the inhibit-release gate's `skip_when` is now the *refusal* predicate — it succeeds (skips the blocked sheet) when the release receipt is absent or invalid; the draft's form proceeded on checker failure. **Limitation stated honestly (also the Skeptic's):** edge labels constrain *gating and injection* (which sheets run, what their preludes carry) — they are not runtime semantics the engine enforces; the audit enforces consumption (`grep` check that no `retired/` file was read after retirement, exit code named).

**Core Dynamic.** Connell–Slatyer succession has three models, and pass 1's dual-enumeration generator had one: *tolerance* — independent agents colonize in parallel, coexistence settled downstream. **Facilitation**: wave-1 sheets' artifacts are *environmental modification* — test fixtures, stubs, adversarial examples, data schemas — preparing soil so wave-2 establishes at higher probability; the quality bar is usability, not brilliance. **Inhibition** — the dark third: early occupants hold space and block latecomers until disturbed. The orchestration reading: early commitments (a premature schema freeze, a keystone artifact churned into a contract) *inhibit* later better designs; the disturbance that releases inhibition is a deliberate, receipted decommitment step. Facilitation theater is the failure mode: a wave-1 fixture set nothing tests against is discard, and the score paid for the fiction.

**Example.** Legacy-system modernization: wave 1 builds the strangler-fig scaffolding (routing shims, characterization tests around the legacy module); the inhibition-release step formally retires the legacy interface contract; wave 2 rebuilds each module. Without classification, teams run wave 2 against interfaces wave 1 silently locked in place — inhibition by accident.

### Review Integration

Integrated from discover pass 2 (cycle 7) after three adversarial reviews (Practitioner, Skeptic, Newcomer); this pattern's specific repairs are itemized in `discover-pass-2/06-the-corpus.md` § Review Integration and the Reconciliation Appendix.
