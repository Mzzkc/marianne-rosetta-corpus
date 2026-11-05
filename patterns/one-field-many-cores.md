---
name: "One Field, Many Cores"
scale: within-stage
type: orchestration-pattern
status: working
iteration_added: "discover pass 1, cycle 7"
forces:
  - "Finite Resources"
  - "Progressive Commitment"
generators:
  - "Incremental Exposure"
problem: "Survey-the-territory tasks are sized by feel — either 400 full reviews or one spot-check dressed as a survey — when the load-bearing decision is the sampling plan authored before any sampling."
signals:
  - "scan a codebase / review a document set / triage an inbox / probe a UI"
  - "fan-out width currently chosen by intuition"
  - "between-cell differences matter more than any single core's findings"
stages:
  - name: grid
    sheets: 1
    instrument_guidance: "instrument: cli — reads the committed manifest, partitions into cells, assigns K disjoint core slices"
    fallback_friendly: false
    purpose: "The sampling plan is an authored artifact with its own digest."
    artifacts: ["grid-plan.json", "grid-plan.sha"]
  - name: core
    sheets: "fan_out(cells × K, STATIC from the committed plan)"
    instrument_guidance: "cheapest instrument that can notice the phenomenon"
    fallback_friendly: true
    purpose: "Probe only your slice; emit {cell, findings, confidence}."
    artifacts: ["core-{{ instance_id }}.json"]
  - name: composite
    sheets: 1
    instrument_guidance: "instrument: cli — mechanical per-cell merge (dedup + confidence aggregation)"
    fallback_friendly: false
    purpose: "Emit field-map.yaml with per-cell composites and between-cell deltas."
    artifacts: ["field-map.yaml"]
  - name: heterogeneity-check
    sheets: 1
    instrument_guidance: "instrument: cli — flags cells whose cores disagree beyond the declared band"
    fallback_friendly: false
    purpose: "A cell containing both swamp and knoll composites into a lie — flag it for re-partition."
    artifacts: ["repartition-needed.txt"]
dependencies:
  core: ["grid"]
  composite: ["core"]
  heterogeneity-check: ["composite"]
composes_with:
  - pattern: "Immune Cascade"
    how: "the priced variant's cell map decides which cells earn tier-2 money"
  - pattern: "First Article Characterization"
    how: "the composite is the field's first article — characterize it, not each core"
config_features:
  - "fan_out (static width)"
  - "instrument: cli"
---

## One Field, Many Cores

`Status: Working` · **Source:** discover pass 1, cycle 7 — Expedition 2 (precision-agriculture soil sampling: Clemson/UNL/ISU extension protocols). **Forces:** Finite Resources + Progressive Commitment.

### Core Dynamic

You cannot assay a whole field and you cannot trust one core. The agronomists' protocol: divide into cells; at each grid point take 10–15 cores in a small radius; **composite into one labeled sample per cell**. Compositing deliberately averages out arm's-length jitter and keeps cell-level difference — two composites differing means something. Translate: **the fan-out's design — cell count, cores per cell, core radius — is the load-bearing decision, made BEFORE sampling**, sized by a declared variance budget, with the merge a mechanical composite and the *cell map*, not any single core, as the artifact.

The grid is **static and committed** (authored or generated at authorship time, digest-recorded). Runtime-discovered partitioning is a different (unproven) pattern's ground. Missing cores are a hard refusal by default; a quorum (proceed with K−1) must be explicitly declared in the grid manifest. The heterogeneity check catches non-stationary cells before their composite lies.

### Marianne Score Structure

```yaml
sheets:
  - name: grid
    instrument: cli
    command: "python3 scripts/make_grid.py manifest.yaml --cells 20 --cores 3 --out grid-plan.json && sha256sum grid-plan.json > grid-plan.sha"
    validations:
      - type: command_succeeds
  - name: core
    instances: 60            # cells × cores, STATIC, from the committed plan
    capture_files: ["grid-plan.json"]
    prompt: "Your slice is listed in grid-plan.json under core-{{ instance_id }}. Probe ONLY your slice. Write core-{{ instance_id }}.json {cell, findings[], confidence}."
    response_format: { type: json_object }
    validations:
      - type: file_exists
        path: "core-{{ instance_id }}.json"
  - name: composite
    instrument: cli
    command: "python3 scripts/composite.py grid-plan.json core-*.json --out field-map.yaml --missing refuse"
    validations:
      - type: command_succeeds
      - type: csv_unique_key
        path: "field-map.yaml"
        key: "cell, slice"
  - name: heterogeneity-check
    instrument: cli
    command: "python3 scripts/heterogeneity.py field-map.yaml --band 0.25 --out repartition-needed.txt"
```

**Negative controls:** delete one core file — composite must fail for missing coverage under `--missing refuse`; a seeded heterogeneous cell must land in `repartition-needed.txt`, not silently averaged into the map.

### When to Use

Any survey-the-territory task, partitionable on the axis the phenomenon varies on, with between-cell differences as the deliverable.

### When NOT to Use

Non-stationary cells without the heterogeneity check; correlated cores reading identical bytes (you bought one core five times); between-cell differences never read (you built a field map and framed one core).

### Composes With

Immune Cascade (priced tier-2 spend on flagged cells), First Article Characterization (composite as first article)
