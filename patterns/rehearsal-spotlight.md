---
name: "Rehearsal Spotlight"
scale: iteration
type: orchestration-pattern
status: working
forces:
  - "Convergence Imperative"
  - "Finite Resources"
generators:
  - "Measure Convergence Character"
problem: "Iteration is expensive; reworking entire outputs wastes resources when only parts need refinement."
signals:
  - "iteration cycles are expensive"
  - "only specific sections need rework"
  - "most output is good but a few parts are weak"
  - "need to focus rework effort on problem areas"
fan_out:
  rehearse: 3
config_features:
  - "self_chaining"
  - "fan_out"
  - "capture_files"
script_dependencies:
  - "check_quality.py"
stages:
  - name: evaluate
    sheets: 1
    instrument_guidance: "score-author's choice — must reason about section quality; sonnet or opus recommended"
    fallback_friendly: true
    purpose: "Read output, score each section for quality, and identify targets for rework."
    artifacts: ["spotlight-targets.yaml"]
  - name: rehearse
    sheets: "fan_out(3)"
    instrument_guidance: "score-author's choice — must match the task being reworked (code, prose, analysis, etc.); capability is load-bearing for quality"
    fallback_friendly: false
    purpose: "Rework the targeted weak sections based on evaluation feedback."
    artifacts: []
  - name: check-done
    sheets: 1
    instrument_guidance: "cli — executes shell-based quality validation checks"
    fallback_friendly: false
    purpose: "Verify that reworked sections meet quality threshold; trigger self-chain if quality is insufficient."
    artifacts: []
composes_with:
  - pattern: "Echelon Repair"
    how: "Echelon Repair allocates effort by difficulty tier; Rehearsal Spotlight focuses rework effort on specific weak sections within one score iteration."
  - pattern: "Soil Maturity Index"
    how: "Soil Maturity Index measures convergence readiness of context; Rehearsal Spotlight applies convergence measurement to identify which sections need another rehearsal."
  - pattern: "CEGAR Loop"
    how: "CEGAR Loop iteratively refines through abstraction phases; Rehearsal Spotlight structures the refinement cycle to rework only sections that failed the previous quality check."
---

## Rehearsal Spotlight

`Status: Working` · **Source:** Theater rehearsal. **Forces:** Convergence Imperative + Finite Resources.

### Core Dynamic

After each iteration, identify the weakest sections and re-run ONLY those. Focuses expensive iteration on the parts that need it most.

### When to Use / When NOT to Use

Use when iteration is expensive and only parts of the output need rework. Not when the whole output needs rework each time.

### Marianne Score Structure

```yaml
sheets:
  - name: evaluate
    prompt: "Read output. Score each section. Write spotlight-targets.yaml: sections needing rework."
    capture_files: ["output/**"]
  - name: rehearse
    instances: 3
    prompt: "Rework the targeted section. Write improved version."
    capture_files: ["spotlight-targets.yaml", "output/**"]
  - name: check-done
    instrument: cli
    validations:
      - type: command_succeeds
        command: "python3 {{ workspace }}/check_quality.py --min-score 8"
on_success:
  action: self
  inherit_workspace: true
  max_chain_depth: 5
```

### Failure Mode

Spotlight always targets the same sections. Track which sections have been rehearsed and escalate persistent weaknesses.

### Composes With

Echelon Repair, Soil Maturity Index, CEGAR Loop
