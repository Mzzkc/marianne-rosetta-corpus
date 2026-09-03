---
name: Proof-Carrying Artifact
scale: communication
status: working
forces:
- Information Asymmetry
- Structured Disagreement
- Exponential Defect Cost
generators:
- Verify through Diverse Observers
- Incremental Exposure
problem: Consumers must either trust producer claims across a trust boundary or re-derive the work at full cost.
signals:
- any handoff where the cost of being wrong exceeds the cost of checking
- claims like 'tests pass' or 'this number came from the source'
- a downstream sheet about to build on an upstream assertion
stages:
- name: produce
  sheets: 1
  instrument_guidance: claude-code or codex-cli — the expensive producer — any AI instrument matched to the work
  fallback_friendly: true
  purpose: Do the work AND write the admissibility evidence beside it.
  artifacts: []
- name: extract
  sheets: 1
  instrument_guidance: any-wrapped CLI profile — deterministic anchor extraction and directory preparation
  fallback_friendly: false
  purpose: Build the typed claim ledger and the verdicts directory.
  artifacts: []
- name: verify
  sheets: fan_out(10)
  instrument_guidance: claude-code or codex-cli — vendor-diverse AI checkers, one claim each; static worst-case width (data-driven width does not exist in the substrate)
  fallback_friendly: true
  purpose: Verify one claim against its source anchor; verdict ADMITTED or CUT.
  artifacts: []
- name: admit
  sheets: 1
  instrument_guidance: any-wrapped CLI profile — re-hash every digest; exit nonzero on mismatch
  fallback_friendly: false
  purpose: Mechanically refuse any artifact whose evidence does not re-hash.
  artifacts: []
- name: consume
  sheets: 1
  instrument_guidance: claude-code or codex-cli — any AI instrument; receives only admitted evidence as a required cadenza
  fallback_friendly: true
  purpose: Work only from admitted artifacts; DEBT-listed claims ship visibly unanchored.
  artifacts: []
dependencies:
  extract:
  - produce
  verify:
  - extract
  admit:
  - verify
  consume:
  - admit
composes_with:
- pattern: Fork-Evident History
  how: payload/substrate — sidecars become journal links over the digest chain
- pattern: Flight Rules
  how: substitution — rule citations source-validated; a fabricated citation fails the run
- pattern: Skeptical Oracle
  how: substitution — the oracle's reconstruction stage is this pattern applied to peer review
- pattern: Fan-out + Synthesis
  how: layering — wraps the fan-out so synthesis consumes only admitted evidence
type: orchestration-pattern
---

## Proof-Carrying Artifact


**Status:** Working. **Source:** proof-carrying code, LCF kernels (iteration 5, Reasoner expedition). Absorbs the Annotated Galley (claim form) and Traceability Chain (pedigree form), seams stated below per the merge law.

**Core Dynamic.** The producer does the expensive work and ships the artifact *with its admissibility evidence*; the consumer checks rather than trusts, and checking is orders of magnitude cheaper than producing. Trust shifts from the producer's identity or confidence to the checker's smallness (the de Bruijn criterion: the checker must be small enough to audit by reading). A claim without its evidence bundle is not *wrong* — it is *inadmissible*: it cannot even be considered. One mechanism, three forms, each with a **different admission check** (Review 2's split — they are not the same bundle):

- **Proof form** (canonical): the bundle is `{command, exit_code, stdout_digest, input_digests[], outputs[]}` — the means of re-checking the property itself. *Admission check: re-run / re-hash.*
- **Pedigree form** (absorbed Traceability Chain): the bundle is a provenance block — source hashes, upstream sheet IDs, spec versions, uncertainty statement. *Admission check: digest presence + spec-version match.* **Seam: pedigree answers where it came from; proof answers why it should be admitted. Pedigree alone never admits.**
- **Claim form** (absorbed Annotated Galley): the bundle is an inline anchor — `[[C7: claim text | source: evidence/report.pdf#p12]]` — extracted into a typed claim ledger before verification. *Admission check: anchor extractable + source addressable.* A claim that cannot name its source does not get weakly verified; it is structurally inadmissible.

**When to use:** every handoff across a trust boundary — sheet to sheet, score to score via `on_success`, agent to human reviewer.

**When NOT to use:** properties not cheaply decidable — taste, tone, "is this a good design" has no checker, and pretending to verify it produces theater. When the checker grows as complex as the producer, the asymmetry that made the pattern worth having is gone. Ephemeral artifacts never re-consumed downstream. In the claim form: evaluative claims cannot anchor; private or perishable sources rot the anchor (needs Negative-Treatment Watch downstream).

**Marianne Score Structure**

```yaml
movements:
  1: { name: produce }
  2: { name: extract, instrument: cli }
  3: { name: verify }
  4: { name: admit, instrument: cli }
  5: { name: consume }

sheet:
  total_items: 5
  fan_out: { 3: 10 }                  # STATIC worst-case width: one checker per claim,
  dependencies: { 2: [1], 3: [2], 4: [3], 5: [4] }   # capped at 10; a bigger claim set
  per_sheet_fallbacks:                # splits into batches of scores, not wider fan-out
    2: []
    4: []                             # extraction and admission never degrade
  cadenzas:
    10:
      - file: "{{ workspace }}/claim-ledger.json"
        as: context
        required: true                # no verdict without the ledger in context

prompt:
  variables:
    claims: 10
  template: |
    {% if stage == 1 %}
    Do the work. Write {{ workspace }}/deliverable.md. EVERY load-bearing claim carries
    an inline anchor [[Cn: text | source: path#locator]]. Also write
    {{ workspace }}/evidence/produce.json recording {command, exit_code, digests, outputs}.
    {% elif stage == 2 %}
    mkdir -p "{{ workspace }}/verdicts" && python3 "{score_dir}/scripts/anchor-extractor.py" \
      "{{ workspace }}/deliverable.md" > "{{ workspace }}/claim-ledger.json"
    {% elif stage == 3 %}
    Verify ONLY claim {{ instance }} against its source anchor in claim-ledger.json.
    Verdict ADMITTED or CUT. Quote the claim verbatim and cite the anchor ID.
    Write {{ workspace }}/verdicts/C{{ instance }}.md and stop.
    {% elif stage == 4 %}
    bash "{score_dir}/scripts/evidence-gate.sh" "{{ workspace }}/evidence/" \
      "{{ workspace }}/claim-ledger.json" "{{ workspace }}/verdicts/"
    {% elif stage == 5 %}
    Work only from admitted artifacts. DEBT-listed claims ship visibly unanchored.
    {% endif %}

validations:
  - type: command_succeeds
    command: 'test -s "{workspace}/evidence/produce.json"'      # the produce stage is INSTRUCTED to write it
    condition: "stage == 1"
  - type: command_succeeds
    command: 'test -s "{workspace}/claim-ledger.json" && test -d "{workspace}/verdicts"'  # extract stage creates the dir
    condition: "stage == 2"
  - type: content_regex
    pattern: "ADMITTED|CUT"
    path: "{workspace}/verdicts/C{instance}.md"
    condition: "stage == 3"
  - type: command_succeeds
    command: 'bash {score_dir}/scripts/evidence-gate.sh --check "{workspace}/evidence/"'  # re-hash; nonzero on mismatch
    condition: "stage == 4"
```

**Near-miss:** attaching a confidence score to each claim — pedigree theater; confidence is not a checker, and 0.9 twice is not evidence once.

**Example.** A contract-review pipeline: every extracted clause claim ("the liability cap is $1M") ships with file path + byte-range digest; the synthesis stage mechanically refuses claims whose digests do not re-hash against the corpus it was given. The paralegal-level claim never enters the memo unverified — not because the extractor is trusted, but because unverified claims are inadmissible.

### Review Integration

Review 2 separated proof, pedigree, and claim forms because each has a different admission check. Reviews 1 and 3 replaced data-driven fan-out with bounded static fan-out and required named producer, ledger, verdict, and gate artifacts. The Package Is the Permission is absorbed across this pattern and Designation Is Authorization: required cadenzas fail closed at attachment time, then this pattern audits the received package before admission. During split curation, the monolith's G1–G6 draft label was mapped to the nearest generator in forces.md, and every stage now names a current profile: deterministic stages use an any-wrapped CLI profile; judgment stages name claude-code, codex-cli, or opencode as appropriate.
