---
name: "Fermentation Relay"
scale: instrument-strategy
type: orchestration-pattern
status: working
forces:
  - "Instrument-Task Fit"
generators:
  - "Match Instrument to Grain"
problem: "Expensive instruments waste resources fixing quality issues that cheap instruments created during initial processing."
signals:
  - "cheap instruments produce output too noisy for expensive stages to use directly"
  - "expensive instruments waste budget on noise filtering instead of core work"
  - "early outputs require multiple refinement steps before quality is acceptable"
  - "no single instrument choice works well across all pipeline stages"
stages:
  - name: extract
    sheets: 1
    instrument_guidance: "haiku — fast, cheap initial processing; sufficient for raw information extraction from input"
    fallback_friendly: true
    purpose: "Extract raw information from input."
    artifacts: ["extraction.md"]
  - name: refine
    sheets: 1
    instrument_guidance: "sonnet — moderate reasoning to resolve ambiguities from raw extraction; capability tier between haiku and opus"
    fallback_friendly: false
    purpose: "Refine extraction by resolving ambiguities and inconsistencies."
    artifacts: ["refined.md"]
  - name: polish
    sheets: 1
    instrument_guidance: "opus — highest reasoning capability for final quality pass; capable of catching subtle issues the refinement stage may miss"
    fallback_friendly: false
    purpose: "Perform final quality pass and produce polished output."
    artifacts: []
composes_with:
  - pattern: "Echelon Repair"
    how: "Fermentation Relay defines the multi-tier instrument cost progression that Echelon Repair routes classified difficult items through for remediation."
  - pattern: "Succession Pipeline"
    how: "Both use sequential refinement stages; Fermentation Relay optimizes for cost-graduated instruments while Succession Pipeline emphasizes early defect detection."
  - pattern: "Screening Cascade"
    how: "Screening Cascade pre-filters items before input to Fermentation Relay's pipeline, improving extraction quality and reducing noise for refinement stages."
---

## Fermentation Relay

`Status: Working` · **Source:** Fermentation microbiology. **Forces:** Instrument-Task Fit.

### Core Dynamic

Cheap instruments do initial processing; expensive instruments refine. The pipeline is fixed in YAML. "Substrate-driven" refers to how you design the gate between stages, not runtime switching.

### When to Use / When NOT to Use

Use when early stages benefit from fast/cheap processing and later stages need precision. Not when all stages need the same capability.

### Marianne Score Structure

```yaml
sheets:
  - name: extract
    instrument: haiku
    prompt: "Extract raw information. Write extraction.md."
    validations:
      - type: file_exists
        path: "{{ workspace }}/extraction.md"
  - name: refine
    instrument: sonnet
    prompt: "Refine extraction. Resolve ambiguities."
    capture_files: ["extraction.md"]
  - name: polish
    instrument: opus
    prompt: "Final quality pass. Produce polished output."
    capture_files: ["refined.md"]
```

### Failure Mode

Early cheap stages produce such poor output that expensive stages spend all their budget fixing garbage. Validate intermediate quality.

### Composes With

Echelon Repair, Succession Pipeline, Screening Cascade
