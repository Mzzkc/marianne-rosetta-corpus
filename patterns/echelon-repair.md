---
name: "Echelon Repair"
scale: instrument-strategy
type: orchestration-pattern
status: working
proof_score: "echelon-repair.yaml"
forces:
  - "Instrument-Task Fit"
  - "Finite Resources"
generators:
  - "Match Instrument to Grain"
problem: "Expensive instruments waste resources on work that cheaper instruments could handle."
signals:
  - "work items vary wildly in difficulty"
  - "expensive instrument is wasted on trivial tasks"
  - "costs are high but most work is simple"
  - "need to triage before processing"
stages:
  - name: classify
    sheets: 1
    instrument_guidance: "opencode — fast, cheap classification; capability is sufficient for difficulty labeling"
    fallback_friendly: true
    purpose: "Read each work item and classify difficulty as E1/E2/E3."
    artifacts: ["echelon-manifest.yaml"]
  - name: e1-repair
    sheets: 1
    instrument_guidance: "opencode — simple items; speed and cost matter more than depth"
    fallback_friendly: true
    purpose: "Process items classified as E1 (simple)."
    artifacts: []
  - name: e2-repair
    sheets: 1
    instrument_guidance: "codex-cli (gpt-5.5) — moderate items; needs more reasoning than opencode provides"
    fallback_friendly: false
    purpose: "Process items classified as E2 (moderate complexity)."
    artifacts: []
  - name: e3-repair
    sheets: 1
    instrument_guidance: "claude-code — complex items; full reasoning capability required"
    fallback_friendly: false
    purpose: "Process items classified as E3 (high complexity)."
    artifacts: []
dependencies: {}
composes_with:
  - pattern: "Commissioning Cascade"
    how: "Commissioning Cascade verifies the output quality of each echelon tier."
  - pattern: "Fermentation Relay"
    how: "Fermentation Relay provides the instrument tier escalation that Echelon Repair's classification routes into."
  - pattern: "Screening Cascade"
    how: "Screening Cascade pre-filters items before echelon classification to remove obvious non-candidates."
  - pattern: "Circuit Breaker"
    how: "Circuit Breaker halts escalation to expensive echelons when failure rates spike."
---

## Echelon Repair

`Status: Working` · **Source:** Military echelon maintenance. **Forces:** Instrument-Task Fit + Finite Resources.

### Core Dynamic

Graduated instrument assignment. Easy work goes to cheap/fast instruments. Hard work escalates to expensive/capable instruments. The classification stage determines difficulty BEFORE assignment.

### When to Use / When NOT to Use

Use when work items vary in difficulty and instruments vary in cost/capability. Not when all work is equally complex.

### Marianne Score Structure

```yaml
sheets:
  - name: classify
    instrument: haiku
    prompt: "Read each item. Classify difficulty: E1 (simple), E2 (moderate), E3 (complex). Write echelon-manifest.yaml."
    validations:
      - type: command_succeeds
        command: "python3 -c \"import yaml; m=yaml.safe_load(open('{{ workspace }}/echelon-manifest.yaml')); assert all(e['echelon'] in ['E1','E2','E3'] for e in m)\""
  - name: e1-repair
    instrument: haiku
    prompt: "Process E1 items from echelon-manifest.yaml."
    capture_files: ["echelon-manifest.yaml"]
  - name: e2-repair
    instrument: sonnet
    prompt: "Process E2 items."
    capture_files: ["echelon-manifest.yaml"]
  - name: e3-repair
    instrument: opus
    prompt: "Process E3 items."
    capture_files: ["echelon-manifest.yaml"]
```

### Failure Mode

Misclassification: E3 items assigned to E1. Validate E1 output quality; escalate failures to E2.

### Composes With

Commissioning Cascade, Fermentation Relay, Screening Cascade, Circuit Breaker
