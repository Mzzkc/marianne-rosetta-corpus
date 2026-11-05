---
name: "Unison Drift"
scale: within-stage
status: working
forces: [Structured Disagreement, Exponential Defect Cost]
generators: [Verify through Diverse Observers]
problem: "Replicas that should be identical diverge silently, and the divergence point — the actual defect location — is never localized."
signals:
  - "an expensive fan-out is about to be spent on an untested prompt+toolchain"
  - "instrument or vendor swaps may have changed behavior invisibly"
  - "reproducibility of the pipeline is assumed but never measured"
stages:
  - name: mark-plan
    sheets: 1
    instrument_guidance: "any-wrapped CLI — declares rehearsal marks (per-stage output digests expected identical across replicas) and the comparison mode per mark"
    fallback_friendly: false
    purpose: "Define where divergence will be measured and how (byte-digest or normalized-semantic)."
  - name: replicas
    sheets: fan_out(N)
    instrument_guidance: "IDENTICAL instrument, profile, prompt, and seed across replicas — that is the experiment; 2 proves drift exists, 3 names the odd one out"
    fallback_friendly: true
    purpose: "Run the same sequence N times; write per-mark digest artifacts."
  - name: differ
    sheets: 1
    instrument_guidance: "any-wrapped CLI, per_sheet_fallbacks: [] — sha256sum + comm over mark digests; writes drift-ledger.csv (mark, replicas-in-agreement, first-divergent-pair)"
    fallback_friendly: false
    purpose: "Localize the first divergent mark; quarantine everything downstream of it."
dependencies:
  differ: [replicas]
composes_with:
  - pattern: "Rashomon Gate"
    how: "the routing rule this entry adds — unison → drift-diff; Rashomon → compare"
  - pattern: "Readback Before Commit"
    how: "typed echoes make marks comparable; prose marks cannot be diffed"
  - pattern: "The Independence Law"
    how: "the one place instruments must NOT differ — the negative image of family separation"
type: orchestration-pattern
---

## Unison Drift

**Status:** working · primitives-proven — **the first proof of the pass** (fan-out, `capture_files`, `file_sha256`, CLI differ; zero blocked machinery; ranked #1 by the collision and #1 or top-tier in all three reviews).

**Core Dynamic.** Run replicas that *should* be identical and let them diverge naturally; the divergence is not noise, it is a **measurement**. Where Rashomon Gate fans out expecting disagreement (different lenses, compare conclusions), Unison Drift fans out expecting *identity* — so the first divergence point localizes the fault with cycle-resolution: a nondeterministic tool at step k, an underspecified prompt clause two readers take differently, a dependency that resolved to different versions. Brown's additive law is the localization mechanism: the loop grows one element per cycle, so any divergence is arithmetically locatable to the cycle it entered.

**Repairs applied (the Skeptic's three):** (1) *Deterministic vs probabilistic modes, declared per mark.* "Identical instrument and profile" does not imply byte identity for stochastic agents. Deterministic toolchains compare raw `file_sha256` at each mark; probabilistic agents compare **normalized semantic marks** — digests over parsed structure (the AST, the extracted-term set, the normalized JSON) with temperature and sampling declared — and a mark that cannot be normalized is marked `localization: coarse` on the plan. (2) *The N=2/N=3 tie-break rule (the Newcomer's demand):* N=2 proves drift exists but cannot say which replica is the odd one out — there is no majority; N=3 disambiguates by majority vote. State which question you are asking before choosing N. (3) *Quarantine is a gate, not prose:* the consumer gate's `skip_when` succeeds (skips) on any input downstream of the ledger's first-divergent mark — polarity-correct refusal, checkable.

**Sentinel.** Perturb replica 2 (a seeded stochastic tool where replicas 1 and 3 pin a fixed seed) → the ledger's `first-divergent-mark` equals the seeded tool's stage, and downstream-of-mark outputs are refused by the consumer gate. If the ledger blames an earlier mark, the differ is wrong and the proof fails.

**Example.** Before a 12-instance documentation-translation fan-out, run 3 replicas through the prompt+toolchain once each; the ledger shows first divergence at the terminology-extraction mark — "extract key terms" is underspecified. Fix the clause, rerun, divergence gone, *then* spend on 12.

### Review Integration

Integrated from discover pass 2 (cycle 7) after three adversarial reviews (Practitioner, Skeptic, Newcomer); this pattern's specific repairs are itemized in `discover-pass-2/06-the-corpus.md` § Review Integration and the Reconciliation Appendix.
