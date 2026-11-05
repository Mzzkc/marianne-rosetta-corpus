---
name: "The Watchman's Gate"
scale: score-level
status: working
forces: [Exponential Defect Cost, Partial Failure]
generators: [Threshold-Triggered Switch]
problem: "Destructive execution must never depend on a check that fails open, so the veto must live in a dedicated, deterministic, independently-instrumented sheet."
signals:
  - "any AI → destructive-action seam: deploys, mass rewrites, publication, external sends"
  - "a broken predicate would otherwise admit unvetted work silently (V1)"
  - "the thing being gated and the thing deciding are the same instrument"
stages:
  - name: declare
    sheets: 1
    instrument_guidance: "producer sheet, response_format: json_schema — emits the typed intent (what will be touched, how, declared blast radius)"
    fallback_friendly: true
    purpose: "Make the intent machine-checkable before it is checkable."
  - name: watchman
    sheets: 1
    instrument_guidance: "any-wrapped CLI, per_sheet_fallbacks: [] — MUST be a different instrument class than declare; validates the declaration against standing rules (path scope, declared reversibility, digest match) and writes pick.json (GO/NO-GO + declaration sha256)"
    fallback_friendly: false
    purpose: "The pick instruction IS a validation; refusal is loud, here."
  - name: execute
    sheets: 1
    instrument_guidance: "the destructive sheet; skip_when is the REFUSAL predicate: test ! -f pick.json || ! jq -e '.verdict == \"GO\"' pick.json — succeeds (skips) when GO is absent or invalid"
    fallback_friendly: false
    purpose: "Proceed only under a present, valid GO."
dependencies:
  watchman: [declare]
  execute: [watchman]
composes_with:
  - pattern: "Readback Before Commit"
    how: "this is its placement law given V1"
  - pattern: "The Cue Light"
    how: "pick.json is a one-bit cue with a digest"
  - pattern: "The Hold-Point Witness"
    how: "same placement law, different scale — within-score vs score-to-human"
  - pattern: "Capability Census"
    how: "the census roster is what qualifies the watchman instrument"
type: orchestration-pattern
---

## The Watchman's Gate

**Status:** working · primitives-proven, verified seam with engine citations attached (V1: `skip.py:13-19`; V5 for the typed declaration). Ranked #5 by the collision; the Newcomer called its delete-the-watchman negative "the draft's best falsifiable claim." The Newcomer also ranked it top-tier *for its citation discipline* — and it survives the Skeptic's kill only because its own law was right and its example was wrong.

**The polarity inversion, fixed (the Skeptic's catch — the most important single correction of the pass).** The draft's `skip_when: 'test -f pick.json && grep -q GO pick.json'` succeeds exactly when the GO exists — under Marianne semantics (skip on command success), it would **skip authorized execution and proceed on unauthorized execution**, with V1 evaluation errors *also* proceeding. The pattern's core doctrine survived untouched — the load-bearing check never lived in `skip_when`; it lives in the watchman sheet's own fail-closed validation — but the consent echo was inverted. Corrected form in the frontmatter and here: `skip_when: 'test ! -f pick.json || ! jq -e ''.verdict == "GO"'' pick.json'`. Absent/invalid GO → command succeeds → the sheet refuses; present GO → command fails → the sheet proceeds; and even a V1 evaluation error only ever risks a refusal, never an unauthorized execution, because the refusal already happened loudly one sheet earlier. This inversion is now **Composition Doctrine #1**, corpus-wide: always write the refusal predicate.

**Core Dynamic.** On a real pick, the operator does not take instructions from the crowd: one qualified signal person exclusively owns the channel to the crane, and is *not the rigger who set the load* — independence at the channel level (C3). Translation to the verified seams: a `response_format: json_schema` producer emits its typed declaration of intent; a separate deterministic gate sheet is the only thing the executing sheet listens to; the gate CANNOT live in the executing sheet's own `skip_when` (fail-open, V1), so the watchman is a real sheet whose validation IS the pick instruction.

**Negative controls.** The dry-run fixture includes a declaration violating path scope — the watchman MUST emit NO-GO (`grep -c NO-GO pick-negative.json` returns 1, else exit 1). **The load-bearing negative:** delete the watchman sheet → execute's refusal predicate finds no `pick.json` → skips → the downstream consumer's validation fails on the missing artifact. The gate is load-bearing *by construction*, and the failure is visible at the consumer, not silent.

**Example.** Database-migration concert: declare emits the migration manifest as json_schema; watchman (pure CLI: jq + a scope checker) verifies the table list against the change-freeze file and writes GO with the manifest digest; the migration sheet's refusal predicate consumes GO. A broken scope checker fails open — and the migration still refuses, because the artifact it needs was never written.

### Review Integration

Integrated from discover pass 2 (cycle 7) after three adversarial reviews (Practitioner, Skeptic, Newcomer); this pattern's specific repairs are itemized in `discover-pass-2/06-the-corpus.md` § Review Integration and the Reconciliation Appendix.
