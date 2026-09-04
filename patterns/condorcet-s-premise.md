---
name: "Condorcet's Premise"
scale: communication
type: orchestration-pattern
status: working
forces:
  - "Structured Disagreement"
generators:
  - "Verify through Diverse Observers"
problem: "Voting authority is assumed from panel size, but correlated panels ratify errors with majority confidence instead of averaging them out."
signals:
  - "a fan-in that will vote, over claims that cannot be mechanically reconstructed"
  - "a 'vendor-diverse' claim never family-probed"
  - "n reviewers from what turns out to be one model family"
config_features:
  - "fan_out"
  - "per_sheet_instruments"
  - "instrument: cli"
stages:
  - name: calibrate
    sheets: "fan_out(3)"
    instrument_guidance: "three instruments on three expanded sheets via per_sheet_instruments; one per vendor family"
    fallback_friendly: true
    purpose: "Answer pre-authored calibration items with known ground truth."
    artifacts: ["calibration/answers-{{ instance }}.jsonl"]
  - name: census
    sheets: 1
    instrument_guidance: "instrument: cli — computes the co-occurrence matrix, design effect, family census, and demotion"
    fallback_friendly: false
    purpose: "Emit panel-manifest.yaml: {rho_bar, n_eff, family_census[], aggregation_rule_demoted_to}."
    artifacts: ["panel-manifest.yaml"]
  - name: panel
    sheets: "fan_out(3)"
    instrument_guidance: "same three instruments, same assignment rule as calibration"
    fallback_friendly: true
    purpose: "Work the real task under the demoted aggregation rule."
    artifacts: []
  - name: audit
    sheets: 1
    instrument_guidance: "instrument: cli — joins the verdict's cited rule against the manifest's demoted rule"
    fallback_friendly: false
    purpose: "No vote ships before its own audit passes."
    artifacts: []
dependencies:
  census: ["calibrate"]
  panel: ["census"]
  audit: ["panel"]
composes_with:
  - pattern: "The Skeptical Oracle"
    how: "complement — reconstruct when possible; audit the jury when not"
  - pattern: "Rashomon Gate"
    how: "layering — frames are jurors; the gate's synthesis demotes by measured dependence"
  - pattern: "The Dropped Axiom"
    how: "the demotion ladder is Typed Force's shared enum"
---

## Condorcet's Premise (Independence Audit)

`Status: Working` · **Source:** iteration 6 (Expedition 4 — Condorcet jury tradition, Kish design effect, self-consistency literature). **Scale:** communication. **Force:** Structured Disagreement.

### Core Dynamic

The jury theorem is a contract with two clauses and people only ever read one: majority voting converges on truth as the panel grows **if** each juror is better than a coin flip **and** their errors are independent. The second clause is load-bearing — correlated voters do not average out their errors, they *ratify* them with the confidence of a majority. AI ensembles fail exactly here: same vendor family, same training blind spots, same prompt scaffold — prompt correlation is juror correlation.

The estimator, defined and bounded: over K calibration items with known answers, compute the full pairwise error co-occurrence matrix M(i,j) = P(jurors i and j both wrong); report ρ̄ = mean of off-diagonal entries and the design effect n/(1+(n−1)ρ̄) as an **equicorrelation upper bound** — a heterogeneous matrix is not safely reducible to one number, so M rides the manifest as data. Missing answers count as errors, declared. Calibration ground truth is pre-authored in the score directory at authorship — seeded items whose answers the run cannot influence. The family census (`family_source` stamped from a live `mzt config` probe) is **provenance evidence, not independence**: instrument-name inequality proves nothing on this host, where claude-code and opencode both default through GLM/Z.AI-family routes; only measured error behavior selects the rule.

The demotion ladder — majority → weighted-correlation → editorial-with-dissents → refusal — is selected by the measured bound; the audit joins the verdict's *cited* rule against the manifest's *demoted* rule. A silent majority over a correlated panel is the failure; the demotion is not.

### When to Use / When NOT to Use

Use: any review/verdict fan-out whose claims are not mechanically reconstructible (the Skeptical Oracle's excluded territory — strategy calls, style judgments, risk assessments); any "vendor-diverse" claim that has not been family-probed.

Not: reconstruction is possible (re-derive, do not vote); no ground truth and no family census (ρ unmeasurable — the pattern honestly refuses to certify); one juror; the decision is binary, cheap, and demonstrably independent (the audit would cost more than the vote).

### Marianne Score Structure

```yaml
instruments:
  a: { profile: claude-code }
  b: { profile: codex-cli }
  c: { profile: opencode, config: { model: "zai-coding-plan/glm-5.3-flash" } }
movements:
  1: { name: calibrate, voices: 3 }
  2: { name: census, instrument: cli, instrument_fallbacks: [] }
  3: { name: panel, voices: 3 }
  4: { name: audit, instrument: cli, instrument_fallbacks: [] }
sheet:
  size: 1
  total_items: 4                  # expansion: calibrate 1-3, census 4, panel 5-7, audit 8
  fan_out: { 1: 3, 3: 3 }
  dependencies: { 2: [1], 3: [2], 4: [3] }
  per_sheet_instruments:          # expanded-sheet-keyed; one sheet, one instrument
    1: a
    2: b
    3: c
    5: a
    6: b
    7: c
  per_sheet_fallbacks: { 4: [], 8: [] }
prompt:
  template: |
    {% if stage == 1 %}
    Answer the calibration items at "{score_dir}/calibration/items.jsonl". Write
    {{ workspace }}/calibration/answers-{{ instance }}.jsonl. Ground truth is NOT available to you.
    {% elif stage == 2 %}
    bash "{score_dir}/scripts/census.sh" --answers "{{ workspace }}/calibration/" \
      --ground-truth "{score_dir}/calibration/ground-truth.jsonl" --emit "{{ workspace }}/panel-manifest.yaml"
    {% elif stage == 3 %}
    Work the panel task. The aggregation rule in {{ workspace }}/panel-manifest.yaml governs; cite it.
    {% else %}
    bash "{score_dir}/scripts/demote.sh" --manifest "{{ workspace }}/panel-manifest.yaml" --verdict "{{ workspace }}/verdict.md"
    {% endif %}
validations:
  - type: command_succeeds
    command: 'bash {score_dir}/scripts/census.sh --self-test'
    condition: "stage == 2"
  - type: command_succeeds
    command: 'bash {score_dir}/scripts/demote.sh --manifest {workspace}/panel-manifest.yaml --verdict {workspace}/verdict.md'
    condition: "stage == 4"
```

Self-test: a synthetic three-juror panel with planted co-occurring errors must demote to editorial-with-dissents or refusal; a verdict citing `majority` over it must fail the audit.

### Example

A hospital quality committee fans an incident summary to three external review services for severity verdicts. Two quietly run the same underlying model. The census on ten seeded incidents shows errors co-occurring at ρ̄ ≈ 0.5 — three letterheads, one review — and the aggregation is demoted to argued editorial with recorded dissents before anyone votes on anything real.

### Review Integration

Iteration 6: Review 3 found the draft's `instrument_map` assigned the same sheets to three instruments — invalid at load (job.py rejects duplicate assignment); routing is now `per_sheet_instruments` on expanded numbers. Review 1 demanded calibration sourcing and demoted family census to provenance; Review 2 demanded the estimator be defined and its equicorrelation simplification bounded. All three fixes are constitutive.
