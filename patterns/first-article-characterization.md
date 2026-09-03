---
name: First Article Characterization
scale: score-level
status: working
forces:
- Exponential Defect Cost
- Instrument-Task Fit
generators:
- Incremental Exposure
- Match Instrument to Grain
problem: Validating each item of a large homogeneous fan-out from first principles is unaffordable, and validating none is unacceptable.
signals:
- fan-out volume work under a new or changed configuration
- N report instances, N translations, N generated artifacts of one kind
- a genuine shared configuration across the population
stages:
- name: first-article
  sheets: 1
  instrument_guidance: claude-code or codex-cli — the production instrument — produces ONE instance under current configuration
  fallback_friendly: true
  purpose: Produce the unit that will become the reference.
  artifacts: []
- name: characterize
  sheets: 1
  instrument_guidance: claude-code or codex-cli — a DIFFERENT instrument family if available — an instrument calibrating itself is not calibration
  fallback_friendly: false
  purpose: 'Produce the characterization manifest: every expected property, keyed, each with its check.'
  artifacts: []
- name: reference-freeze
  sheets: 1
  instrument_guidance: any-wrapped CLI profile — stamp the manifest with the configuration hash
  fallback_friendly: false
  purpose: Store the golden reference bound to the config it certified.
  artifacts: []
- name: volume
  sheets: fan_out(200)
  instrument_guidance: claude-code or codex-cli — any instruments; each instance validated by executing the manifest's checks
  fallback_friendly: true
  purpose: 'Grounded volume: validate against the reference, not from principles.'
  artifacts: []
dependencies:
  characterize:
  - first-article
  reference-freeze:
  - characterize
  volume:
  - reference-freeze
composes_with:
- pattern: Standby–GO
  how: prerequisite — characterize buffer B, then arm
- pattern: Skeptical Oracle
  how: layering — the characterization fan-out behind a trust fence
- pattern: Attested Merge Gate
  how: prerequisite — the manifest checks are the sweep's content
type: orchestration-pattern
---

## First Article Characterization


**Status:** Working. **Source:** AS9102 First Article Inspection; golden units; pharmacopoeia reference standards. **The manifest-runner idiom is now named (Review 1):** 200 instances × N keyed checks is not a static validation list — the buildable form is ONE deterministic manifest-runner script that loops over the keyed checks internally per instance. The source-validation property lives in that script; it is a named Script Library entry, not an opacity.

**Core Dynamic.** Before volume production runs, the first unit under the new configuration is characterized *completely and independently* — every property keyed and numbered, each with the check that verifies it. **The characterized article becomes the law:** volume is not re-validated from first principles; it is validated against the reference, and disputes are settled against the retained golden unit, not re-derivation. When configuration changes, a *delta* characterizes only what changed.

**Hard exclusions (Review 2 made them exclusions, not warnings):** instances that are not actually of one kind — checking the many against a reference requires a *genuine shared configuration*, or the first article certifies a population of one. Reference rot — a golden unit whose underlying config silently changed poisons every validation that trusted it; the reference must be bound to its configuration manifest.

**When to use:** fan-out volume work under a new or changed configuration where validating each from scratch is unaffordable but validating none is unacceptable.

**Marianne Score Structure**

```yaml
movements:
  1: { name: first-article }
  2: { name: characterize }
  3: { name: reference-freeze, instrument: cli }
  4: { name: volume }

sheet:
  total_items: 4
  fan_out: { 4: 200 }
  dependencies: { 2: [1], 3: [2], 4: [3] }
  per_sheet_fallbacks: { 3: [] }
  skip_when:
    2: { command: 'test "$(sha256sum {workspace}/config-fingerprint.json | cut -d" " -f1)" = "$(jq -r .config_hash {workspace}/reference/manifest.json 2>/dev/null || echo none)"' }
                                         # unchanged config reuses the reference;
                                         # changed config forces re-characterization

prompt:
  template: |
    {% if stage == 1 %}
    Produce ONE instance of the artifact under the current configuration.
    {% elif stage == 2 %}
    Characterize the first article COMPLETELY: every expected property in
    {{ workspace }}/characterization.json as {key, property, check} — keyed like balloon numbers.
    You are the independent measurer; a different instrument family from the producer.
    {% elif stage == 3 %}
    python3 "{score_dir}/scripts/reference-freeze.py" "{{ workspace }}" \
      --config-fingerprint config-fingerprint.json --manifest characterization.json
    {% elif stage == 4 %}
    Produce instance {{ instance }}. Then run the manifest checks against your own output:
    python3 "{score_dir}/scripts/manifest-runner.py" "{{ workspace }}/reference/manifest.json" \
      "{{ workspace }}/out-{{ instance }}/" --emit-report
    {% endif %}

validations:
  - type: file_exists
    path: "{workspace}/reference/manifest.json"
    condition: "stage == 3"
  - type: command_succeeds
    # the manifest-runner: the ONE deterministic loop over keyed checks per instance
    command: 'python3 {score_dir}/scripts/manifest-runner.py {workspace}/reference/manifest.json {workspace}/out-{instance}/ --check-only'
    condition: "stage == 4"
```

**Near-miss:** spot-checking 5% of volume randomly — sampling where a reference manifest would be total; you learn the population's mood, not its conformance.

**Example.** Generating 200 localized versions of a product page: one version is deeply characterized (terminology, tone, layout, legal lines — each keyed); the manifest becomes the acceptance suite; the remaining 199 are validated by executing those keyed checks. Source copy changes → hash check forces delta characterization of exactly the changed lines.

### Review Integration

Review 1 required one deterministic manifest runner rather than imaginary dynamic validation expansion. Review 2 made heterogeneous populations a hard exclusion because one article cannot characterize unlike instances. During split curation, the monolith's G1–G6 draft label was mapped to the nearest generator in forces.md, and every stage now names a current profile: deterministic stages use an any-wrapped CLI profile; judgment stages name claude-code, codex-cli, or opencode as appropriate.
