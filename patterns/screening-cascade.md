---
name: "Screening Cascade"
scale: instrument-strategy
type: orchestration-pattern
status: working
forces:
  - "Instrument-Task Fit"
  - "Finite Resources"
generators:
  - "Graduate & Filter"
  - "Match Instrument to Grain"
problem: "Difficulty emerges during processing; fixed upfront instruments waste expensive resources on simple work or fail on complex work."
signals:
  - "work items vary in difficulty but this only becomes clear during processing"
  - "cheap instruments can screen routine items but some need escalation to stronger capabilities"
  - "costs are high because you're using expensive instruments for work that doesn't warrant them"
  - "difficult work emerges during execution, not from upfront inspection"
stages:
  - name: screen-1
    sheets: 1
    instrument_guidance: "haiku — fast, cost-effective initial screening; sufficient to identify items requiring stronger instruments"
    fallback_friendly: true
    purpose: "Process all items with cheap instrument; mark uncertain items for escalation."
    artifacts: ["screen-1-results.yaml"]
  - name: screen-2
    sheets: 1
    instrument_guidance: "sonnet — stronger reasoning than haiku; handles items that exceed haiku's capability but don't require opus"
    fallback_friendly: false
    purpose: "Screen items escalated from stage 1 with improved capability; further escalate remaining uncertain items."
    artifacts: ["screen-2-results.yaml"]
  - name: screen-3
    sheets: 1
    instrument_guidance: "opus — full reasoning capability for items that exceeded both cheaper instruments; required for the most difficult work"
    fallback_friendly: false
    purpose: "Process items escalated from stage 2 with maximum reasoning capability."
    artifacts: []
composes_with:
  - pattern: "Echelon Repair"
    how: "Screening Cascade discovers difficulty progressively through escalating screens; Echelon Repair pre-classifies items upfront, providing alternative approaches to matching work with instruments."
  - pattern: "Immune Cascade"
    how: "Screening Cascade escalates through capability tiers; Immune Cascade provides fallback processing when escalation fails, with items flowing to Immune Cascade's recovery paths."
  - pattern: "Dead Letter Quarantine"
    how: "Dead Letter Quarantine captures items that exceed all screening stages' capabilities, isolating unprocessable work from the main pipeline."
---

## Screening Cascade

`Status: Working` · **Source:** Medical screening. **Forces:** Instrument-Task Fit + Finite Resources.

### Core Dynamic

Batch processing with escalating instruments at each stage. Stage 1 screens with cheap instrument, passes ambiguous cases to Stage 2 with more capable instrument, and so on. Different from Echelon Repair (which classifies upfront): Screening Cascade discovers difficulty through progressive screening.

### When to Use / When NOT to Use

Use when difficulty isn't classifiable upfront but emerges during processing. Not when all items need the same treatment.

### Marianne Score Structure

```yaml
sheets:
  - name: screen-1
    instrument: haiku
    prompt: "Process all items. Mark items you're uncertain about as ESCALATE. Write screen-1-results.yaml."
    validations:
      - type: file_exists
        path: "{{ workspace }}/screen-1-results.yaml"
  - name: screen-2
    instrument: sonnet
    prompt: "Process ESCALATE items from screen-1. Mark remaining uncertain as ESCALATE-2."
    capture_files: ["screen-1-results.yaml"]
  - name: screen-3
    instrument: opus
    prompt: "Process ESCALATE-2 items."
    capture_files: ["screen-2-results.yaml"]
```

### Failure Mode

Stage 1 escalates everything (no screening value). Validate escalation rates: if >50% escalate, the screening threshold is too conservative.

### Composes With

Echelon Repair, Immune Cascade, Dead Letter Quarantine
