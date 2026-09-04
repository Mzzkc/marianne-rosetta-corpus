---
name: "Vintage Overlay"
scale: adaptation
type: orchestration-pattern
status: working
forces:
  - "Instrument-Task Fit"
  - "Finite Resources"
generators:
  - "Gate on Environmental Readiness"
problem: "A canonical pipeline re-runs on a cadence under external conditions that vary, and each run improvises tuning instead of selecting from pre-authored condition-bound parameter sets."
signals:
  - "the pipeline is stable; the conditions are not"
  - "conditions are mechanically measurable (versions, rate climates, volatility)"
  - "per-vintage tuning would beat per-run improvisation"
config_features:
  - "file_sha256"
  - "cadenzas"
  - "instrument: cli"
stages:
  - name: conditions
    sheets: 1
    instrument_guidance: "instrument: cli — the weather station has no opinions; records resolved model families, not instrument names"
    fallback_friendly: false
    purpose: "Emit conditions.yaml with per-condition digests."
    artifacts: ["conditions.yaml"]
  - name: select
    sheets: 1
    instrument_guidance: "instrument: cli — TOTAL lookup with refusal on unknown vectors"
    fallback_friendly: false
    purpose: "Emit vintage-manifest.yaml binding overlay ids to the selecting condition digests."
    artifacts: ["vintage-manifest.yaml"]
  - name: execute
    sheets: 1
    instrument_guidance: "any — receives base spec plus the manifest by required cadenza"
    fallback_friendly: true
    purpose: "Run under base+overlay; mid-run re-tuning is a different vintage pretending to be the same bottle."
    artifacts: []
  - name: archive-record
    sheets: 1
    instrument_guidance: "instrument: cli — the vintage record is the Write-Time Record's run-level instance"
    fallback_friendly: false
    purpose: "Archive conditions + digests + overlay ids as this run's vintage record."
    artifacts: ["vintage-record/"]
dependencies:
  select: ["conditions"]
  execute: ["select"]
  archive-record: ["execute"]
composes_with:
  - pattern: "Effectivity Blocks"
    how: "the vintage manifest is a run-level effectivity block"
  - pattern: "The Write-Time Record"
    how: "the vintage record is its archival instance"
  - pattern: "Season Bible"
    how: "contrast — mutable continuity within a campaign vs immutable condition-binding per run"
---

## Vintage Overlay

`Status: Working` · **Source:** iteration 6 (Expedition 2 — viticulture: growing-degree-day regions, vintage reports, pre-tuned intervention sets). **Scale:** adaptation. **Forces:** Instrument-Task Fit, Finite Resources.

### Core Dynamic

The mature grower's discipline is refusing to write a new score every year. The canonical cycle — prune, budbreak, canopy, veraison, harvest — is stable knowledge; what varies is *which pre-tuned parameter set manifests*, selected by a measurement stage at the top of the run. That selection is a **lookup**, not judgment. Three review-driven corrections are constitutive: **totality with refusal** — the condition-map is total over its declared axes; an unknown condition vector exits non-zero, no defaults, no nearest-neighbor guessing. **Manifest as data** — runtime-measured conditions cannot re-route already-resolved spec tags, so the manifest reaches consumers as a **required cadenza** (data the sheets read), not dynamic spec routing. **Pin what is pinnable** — the overlay files are authored artifacts, pinned with literal `file_sha256` digests known at authorship; the manifest additionally records the condition digests that did the selecting, so any result's recipe is reproducible months later. The overlay is frozen for the run's duration: mid-run re-tuning is not adaptation, it is a different vintage pretending to be the same bottle.

### When to Use / When NOT to Use

Use: a canonical pipeline re-run on a cadence where external conditions materially vary and are mechanically measurable — vendor API versions, rate-limit climate, market-data volatility, upstream model availability — with enough runs that per-vintage tuning beats improvisation.

Not: first run (no history — author, don't overlay); conditions actually constant (ceremony); conditions can't be measured deterministically (a judgment call in costume).

### Marianne Score Structure

```yaml
movements:
  1: { name: conditions, instrument: cli, instrument_fallbacks: [] }
  2: { name: select, instrument: cli, instrument_fallbacks: [] }
  3: { name: execute }
  4: { name: archive-record, instrument: cli, instrument_fallbacks: [] }
sheet:
  size: 1
  total_items: 4
  dependencies: { 2: [1], 3: [2], 4: [3] }
  cadenzas:
    3:
      - file: "{{ workspace }}/vintage-manifest.yaml"
        as: context
        required: true
  per_sheet_fallbacks: { 1: [], 2: [], 4: [] }
prompt:
  template: |
    {% if stage == 1 %}
    bash "{score_dir}/scripts/conditions.sh" --probe versions,rates,volatility --emit "{{ workspace }}/conditions.yaml"
    {% elif stage == 2 %}
    bash "{score_dir}/scripts/overlay.sh" select --conditions "{{ workspace }}/conditions.yaml" \
      --map "{score_dir}/condition-map.yaml" --emit "{{ workspace }}/vintage-manifest.yaml"
    {% elif stage == 3 %}
    Execute under base spec plus the overlay named in your manifest. Mid-run re-tuning is forbidden.
    {% else %}
    bash "{score_dir}/scripts/overlay.sh" archive --manifest "{{ workspace }}/vintage-manifest.yaml" \
      --conditions "{{ workspace }}/conditions.yaml" --out "{{ workspace }}/vintage-record/"
    {% endif %}
validations:
  - type: file_sha256
    path: "{score_dir}/overlays/vendor-v3-drift.yaml"
    sha256: "b1c2d3e4f5a6b7c8d9e0f1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2"
    condition: "stage == 2"
  - type: command_succeeds
    command: 'bash {score_dir}/scripts/overlay.sh select --self-test'
    condition: "stage == 2"
```

Self-test: an unknown condition vector must be refused — proving the lookup's totality-by-refusal.

### Example

A quarterly SEC-filing extraction pipeline: one canonical score, four runs a year. The 2026-Q3 weather station reads the filing portal's schema version, the data vendor's API generation, and this quarter's document-volume volatility; the manifest binds the `vendor-v3-drift` overlay with the selecting digests; extraction receives base + overlay. The vintage record answers, months later, *which* recipe produced the Q3 numbers.

### Review Integration

Iteration 6: survived Review 3's cut motion ("Effectivity Blocks + spec overlays + a probe stage + Write-Time Record archival") 2–1, with the merge critique answered structurally: pinned overlay digests, total-with-refusal lookup, manifest-as-cadena (Reviews 1 and 2's finding that the draft never configured the spec routing its prose relied on and implied dynamic `spec_tags` re-routing the engine cannot do).
