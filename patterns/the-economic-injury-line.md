---
name: "The Economic Injury Line"
scale: adaptation
type: orchestration-pattern
status: working
forces:
  - "Finite Resources"
  - "Accumulated Signal"
generators:
  - "Threshold-Triggered Switch"
problem: "Defensive recurring work responds to felt damage instead of a threshold computed from unit economics before the season began."
signals:
  - "real unit costs on both sides — intervening and damage"
  - "most intervals honestly deserve NO action"
  - "a bounded sampling protocol can estimate the pressure cheaply"
config_features:
  - "file_sha256"
  - "skip_when"
  - "spec"
stages:
  - name: verify-threshold
    sheets: 1
    instrument_guidance: "instrument: cli — re-derives from the PINNED spec inputs; never re-authors"
    fallback_friendly: false
    purpose: "Diff the re-derivation against the digest-pinned table authored before the season."
    artifacts: []
  - name: scout
    sheets: 1
    instrument_guidance: "instrument: cli — bounded statistical sampling, seeded"
    fallback_friendly: false
    purpose: "Append sampled pressure to the scout ledger."
    artifacts: ["scout-ledger.jsonl"]
  - name: verdict
    sheets: 1
    instrument_guidance: "instrument: cli — one boolean from arithmetic against the frozen table"
    fallback_friendly: false
    purpose: "Emit verdict.json: {not-yet | treat-tier-n, table_digest}."
    artifacts: ["verdict.json"]
  - name: treat
    sheets: 1
    instrument_guidance: "executor for the authorized tier; skip_when not-yet; broad tier barred while incremental retains efficacy"
    fallback_friendly: true
    purpose: "Execute exactly the authorized tier."
    artifacts: []
dependencies:
  scout: ["verify-threshold"]
  verdict: ["verify-threshold", "scout"]
  treat: ["verdict"]
composes_with:
  - pattern: "Rent-Then-Commit"
    how: "contrast — known damage model vs unknown horizon; the two adaptation arithmetics"
  - pattern: "Hutchinson's Warning"
    how: "contrast — no trend, no EMA: a standing threshold and a one-bit question per sample"
  - pattern: "Immune Cascade"
    how: "contrast — tiers chosen by triage judgment vs a line computed from unit economics"
---

## The Economic Injury Line

`Status: Working` · **Source:** iteration 6 (Expedition 2 — integrated pest management; Stern et al. 1959, EIL = C/(V·I·D·K)). **Scale:** adaptation. **Forces:** Finite Resources, Accumulated Signal.

### Core Dynamic

Everything turns on *when* the threshold is made. The farmer does not discover the tripwire by watching the crop feel bad — she computes it in February from the price of the grain, the price of the spray, and last season's damage curves, writes it on the shed wall, and spends the whole season doing almost nothing except counting bugs on a sampling plan. The runtime decision is one boolean produced by arithmetic against a number frozen before the season began. **Judgment is pre-paid.**

The February fix: the inputs and the derived table are **authored into the spec corpus before the season** and digest-pinned with literal `file_sha256`; the run's first movement *verifies* the re-derivation matches the pinned table and refuses to run on a mismatch. The line sits one response-lag *below* the injury level — act at the density where acting now prevents arrival, not at "damage is visible" (too late by construction). The conservation clause is an **executable tier ordering**: the broad-spectrum tier is barred while an efficacy check on the incremental tier passes — you do not destroy the wasps doing free pest control unless the cheap insurance is already lost. The season's default outcome is *visibly skipped sheets*: a below-threshold season treats nothing and still exits green — that negative control is the proof.

### When to Use / When NOT to Use

Use: recurring defensive work with real unit costs on both sides where a bounded sampling protocol can estimate pressure cheaply and most intervals honestly deserve no action — content-drift remediation, dependency-CVE triage, quality sweeps, rate-limit-aware re-scraping.

Not: either price is unmeasurable (no C, no V); the damage curve is discontinuous (one instance destroys everything — sampling arithmetic is pointless); scouting becomes continuous monitoring (you have reinvented a sensor dashboard and the pre-computation saves nothing).

### Marianne Score Structure

```yaml
spec:
  spec_dir: "{score_dir}/specs"
movements:
  1: { name: verify-threshold, instrument: cli, instrument_fallbacks: [] }
  2: { name: scout, instrument: cli, instrument_fallbacks: [] }
  3: { name: verdict, instrument: cli, instrument_fallbacks: [] }
  4: { name: treat }
sheet:
  size: 1
  total_items: 4
  dependencies: { 2: [1], 3: [1, 2], 4: [3] }
  skip_when:
    4: { command: 'jq -e ".action == \"not-yet\"" {workspace}/verdict.json' }
  per_sheet_fallbacks: { 1: [], 2: [], 3: [] }
prompt:
  variables: { run_seed: 11 }
  template: |
    {% if stage == 1 %}
    bash "{score_dir}/scripts/eil.sh" verify --inputs "{score_dir}/specs/eil-inputs.yaml" \
      --pinned-table "{score_dir}/specs/eil-table.yaml"
    {% elif stage == 2 %}
    bash "{score_dir}/scripts/eil.sh" scout --sample 5pct --seed {{ run_seed }} --ledger "{{ workspace }}/scout-ledger.jsonl"
    {% elif stage == 3 %}
    bash "{score_dir}/scripts/eil.sh" verdict --table "{score_dir}/specs/eil-table.yaml" \
      --ledger "{{ workspace }}/scout-ledger.jsonl" --emit "{{ workspace }}/verdict.json"
    {% else %}
    Execute exactly the tier the verdict authorizes. The broad-spectrum tier is barred
    while the incremental tier retains efficacy.
    {% endif %}
validations:
  - type: file_sha256
    path: "{score_dir}/specs/eil-table.yaml"
    sha256: "a0b1c2d3e4f5a6b7c8d9e0f1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2"
    condition: "stage == 1"
  - type: command_succeeds
    command: 'bash {score_dir}/scripts/eil.sh verify --inputs {score_dir}/specs/eil-inputs.yaml --pinned-table {score_dir}/specs/eil-table.yaml'
    condition: "stage == 1"
```

The verdict carries the table digest it was computed against — a re-derived threshold mid-run is inadmissible. Fan-out is actively wrong here: the protocol is bounded *statistical* sampling, not exhaustive partition sweep.

### Example

A stale-listing remediation loop: re-scrape cost C = $0.004/listing; listing value V = expected margin; injury I and damage D fitted from last quarter's A/B data; efficacy K = 0.8. The February stage — run once, before the season — computes and pins the line; a weekly scout samples 5% of categories; remediation sheets stay skipped until sampled staleness crosses the lag-adjusted line — and the broad rebuild tier is barred while the incremental tier handles 80% for free.

### Review Integration

Iteration 6: Reviews 1 and 2 found "February" was rhetorical — the draft derived the threshold at movement 1 of the same run from mutable inputs. Pre-observation custody is now structural: inputs and table authored into the spec corpus, digest-pinned, and only *verified* by the run. Review 1's no-action negative control and generic cost/damage schema are implemented; `run_seed` is a declared variable.
