---
name: "The Contamination Wire"
scale: communication
status: working
forces: [Information Asymmetry, Partial Failure, Exponential Defect Cost]
generators: [Exploit Failure as Signal]
problem: "A warning cannot travel backward to consumers who already ran, so contamination evidence must travel forward on the channel every future consumer already reads."
signals:
  - "a multi-consumer artifact fails validation after some consumers have built on it"
  - "one consumer's validation failure is evidence about the artifact, not just about the consumer"
  - "rerouting or halting must remain possible — alternate sources or degraded modes exist"
stages:
  - name: produce
    sheets: fan_out(N)
    instrument_guidance: "work instruments; each writes artifacts/{producer}.json"
    fallback_friendly: true
    purpose: "Produce the fan-out artifacts that will be gated."
  - name: gate
    sheets: 1
    instrument_guidance: "any-wrapped CLI, per_sheet_fallbacks: [] — verification-only; SUCCEEDS and writes typed verdicts, one per artifact"
    fallback_friendly: false
    purpose: "Emit verdicts/{artifact}.json (PASS or CONTAMINATED + defect class + evidence digest). Contamination is gate output, not validation failure."
  - name: consume
    sheets: fan_out(M)
    instrument_guidance: "AI consumers receive the verdict path via prelude and apply a pre-registered routing table; deterministic consumers' commit wrappers carry a refusal skip_when on their input's verdict"
    fallback_friendly: true
    purpose: "Consume clean inputs; reroute or halt-with-receipt on contaminated ones."
dependencies:
  gate: [produce]
  consume: [gate]
composes_with:
  - pattern: "Dead Letter Quarantine"
    how: "division of labor — DLQ owns the item, the wire owns the warning; compose, never merge"
  - pattern: "The Validity Window"
    how: "a verdict older than the window is stale contamination"
  - pattern: "Readback Before Commit"
    how: "the typed verdict is the readback whose absence started this pattern"
  - pattern: "The Cue Light"
    how: "a poison verdict is a one-bit cue for deterministic consumers"
type: orchestration-pattern
---

## The Contamination Wire

**Status:** working · primitives-proven (rewritten post-review). **The rewrite (the Practitioner's hard kill and the Skeptic's DAG catch):** the draft carried the warning on `failure_history`, which is sheet-local retry state — it does not broadcast from a gate into downstream prompts. And the draft's DAG was self-defeating: a *failing* gate blocks its dependents; a *succeeding* gate has no validation failure to carry. The resolution: **the gate never fails on contamination.** It succeeds and writes a typed verdict per artifact; CONTAMINATED is data on the happy path, so consumers dispatch and read it.

**Core Dynamic.** The warning travels forward on the channel every future consumer already reads — the workspace file tree — and the *consumer*, not the sender, holds routing authority. AI consumers get the verdict path via `prelude` and apply a pre-registered routing table (`IF verdict for input X is CONTAMINATED with code C → emit refusal.json and consume alternate source Y`). Deterministic (CLI) consumers cannot interpret prompts by construction — they are **gated, not warned**: their commit wrapper's `skip_when` succeeds (skips) when the input's verdict says CONTAMINATED, refusing without interpreting anything. Refusals land in `refusals/{consumer}.json` naming artifact, code, chosen alternate. Dual fingerprints: mycorrhizal defense signaling (Barto et al., PMC4497361) and hazmat placarding on the ICS routing channel — the collision's strongest cross-kingdom co-derivation (C6).

**Marianne Score Structure.** Three stages as in frontmatter; produce → gate → consume is load-bearing (the verification-only-stage discipline). Validations: `content_regex` on each AI consumer's output requiring it to cite its input's verdict path or emit the refusal artifact — the third state (built on ungated input, silently) is what the regex kills. **Sentinel:** a seeded artifact planted with a known defect must produce `refusals/consumer-3.json`; `test -f` exits 1 if absent — the run FAILS if the consumer built on poison. **Inverse control:** a clean run shows no refusals (the warning doesn't fire on silence). **Flagged extension, not core:** `failure_history` transport for the *retry-local* case (same sheet re-attempting) is unproven and named on the pattern's face; the Severity Gate, Computed Signature, and Fighting the Last War (benched) queue behind its proof.

**Example.** Due-diligence concert: a fetch sheet pulls filings; three analysts build on it; the gate validates completeness mid-run and writes CONTAMINATED (code V012) on the partial artifact. The analysts see the verdict at consume time; two reroute to the cached prior-quarter filing and say so in their refusals; one halts with a receipt. No rewinding, no silent stale analysis.

### Review Integration

Integrated from discover pass 2 (cycle 7) after three adversarial reviews (Practitioner, Skeptic, Newcomer); this pattern's specific repairs are itemized in `discover-pass-2/06-the-corpus.md` § Review Integration and the Reconciliation Appendix.
