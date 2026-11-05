---
name: "The Poisoned-Artifact Advisory"
scale: communication
type: orchestration-pattern
status: working
iteration_added: "discover pass 1, cycle 7"
forces:
  - "Partial Failure"
  - "Information Asymmetry"
generators:
  - "Exploit Failure as Signal"
problem: "Upstream failure contaminates artifacts that already propagated, and downstream agents treat the workspace as ground truth because no channel tells them what is poisoned."
signals:
  - "a DAG with shared artifacts and a validation gate that runs after consumers may have started"
  - "a subtle early-sheet failure surfaces three stages later"
  - "quality gates that cannot economically run before every consumer"
stages:
  - name: produce
    sheets: 1
    instrument_guidance: "score-author's choice — writes artifact A"
    fallback_friendly: true
    purpose: "Produce the shared artifact."
    artifacts: ["data/extract.json"]
  - name: consumers
    sheets: "fan_out(2)"
    instrument_guidance: "score-author's choice — each reads A and derives a downstream artifact"
    fallback_friendly: true
    purpose: "Consume A (these may complete before the gate runs — that is the point)."
    artifacts: ["report-{{ instance_id }}.md"]
  - name: late-gate
    sheets: 1
    instrument_guidance: "instrument: cli — validation of A; its FAIL path is the load-bearing half"
    fallback_friendly: false
    purpose: "On fail, write advisories/poisoned.yaml naming artifact, typed failure class, timestamp."
    artifacts: ["advisories/poisoned.yaml"]
  - name: containment
    sheets: 1
    instrument_guidance: "strong reasoner — identifies which consumer outputs derived from the poisoned field"
    fallback_friendly: false
    purpose: "Write rework manifest: which outputs are tainted, which clean."
    artifacts: ["rework-manifest.json"]
  - name: rework
    sheets: 1
    instrument_guidance: "score-author's choice — re-derives ONLY tainted outputs"
    fallback_friendly: true
    purpose: "Repair the blast radius the advisory made visible."
    artifacts: []
dependencies:
  consumers: ["produce"]
  late-gate: ["produce"]
  containment: ["consumers", "late-gate"]
  rework: ["containment"]
composes_with:
  - pattern: "Dead Letter Quarantine"
    how: "quarantine is the artifact-side move; the advisory is the prompt-side move — compose both at a late gate"
  - pattern: "The Validity Window"
    how: "advisories age — a fresh advisory is quarantine-now, a stale one is history (failure-evidence profile)"
  - pattern: "The Sealed Dissent"
    how: "a poisoned-artifact event is a first-class entry in the negative ledger"
config_features:
  - "fan_out"
  - "instrument: cli"
  - "capture_files"
---

## The Poisoned-Artifact Advisory

`Status: Working` · **Source:** discover pass 1, cycle 7 — Expedition 6 (Swiss cheese model / latent-failure investigation, Reason; Wiegmann 2022). Named by the v6 review as the fix for "gates running after downstream work has begun." **Forces:** Partial Failure + Information Asymmetry.

### Core Dynamic

The Swiss cheese insight: the holes are in the *layers*, so the advisory must reach agents **after** they may have consumed the poison. The advisory is a **cadenza inverted** — anti-context: "the thing that looks like context and will poison your reasoning." It must be *typed* (hard-failed / superseded / stale) because the downstream response differs: re-derive, discard, or re-verify.

No retroactive un-reading exists: an advisory cannot rewind completed consumers. The honest structure is an explicit **containment + rework DAG** — invalidation lineage, the list of affected consumers, and a compensating rerun — running after the late gate and the consumers converge.

### Marianne Score Structure

```yaml
sheets:
  - name: produce
    prompt: "Write data/extract.json per the spec."
  - name: consumers
    instances: 2
    capture_files: ["data/extract.json"]
    prompt: "Read data/extract.json. Write report-{{ instance_id }}.md deriving your figures from it."
  - name: late-gate
    instrument: cli
    command: "python3 scripts/units_check.py data/extract.json || (mkdir -p advisories && printf 'artifact: data/extract.json\\nclass: hard-failed\\nts: %s\\n' \"$(date -Is)\" > advisories/poisoned.yaml && exit 1)"
    validations:
      - type: command_succeeds
  - name: containment
    capture_files: ["advisories/poisoned.yaml", "report-1.md", "report-2.md"]
    prompt: "Artifact data/extract.json is POISONED (units). Identify which report fields derived from it. Write rework-manifest.json listing tainted report fields only."
    validations:
      - type: file_exists
        path: "rework-manifest.json"
  - name: rework
    capture_files: ["rework-manifest.json"]
    prompt: "Re-derive ONLY the fields in rework-manifest.json from the corrected source (corrected-extract.json). Do not touch clean fields."
    validations:
      - type: content_regex
        pattern: "REWORKED-FROM: corrected-extract"
```

**Negative control:** with advisory generation removed, containment cannot name the tainted fields. **Sentinel:** a final CLI validator asserts the rework output does NOT contain the poisoned field's signature value (e.g., the 1000× unit error) — with the pattern removed, it does, and the sentinel fails.

### When to Use

Any DAG with shared artifacts and late validation; long scores where an early sheet's subtle failure surfaces three stages later; gates that cannot economically run before every consumer.

### When NOT to Use

Transient failures where the retry succeeded — crying wolf burns the channel (pair with the Validity Window's failure-evidence aging); advisories that cannot name the artifact precisely (poison the whole workspace and every downstream agent re-derives everything — paranoid halt).

### Composes With

Dead Letter Quarantine (artifact-side quarantine), The Validity Window (advisory aging), The Sealed Dissent (ledger entry)
