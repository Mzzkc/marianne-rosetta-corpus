---
name: "Soil Maturity Index"
scale: iteration
type: orchestration-pattern
status: working
forces:
  - "Convergence Imperative"
generators:
  - "Measure Convergence Character"
problem: "Iterative processes lack domain-specific termination conditions beyond structural equality."
signals:
  - "iterative improvement plateaus on structural metrics but output lacks qualitative maturity"
  - "need to distinguish real convergence from mere structural stability"
  - "process converges structurally but hasn't achieved expected coherence or readiness"
  - "domain-specific maturity assessment required before proceeding to next phase"
stages:
  - name: iterate
    sheets: 1
    instrument_guidance: "score-author's choice — any instrument capable of reading and improving content based on domain-specific maturity criteria"
    fallback_friendly: true
    purpose: "Read the output and refine it based on domain-specific maturity criteria, iteratively improving toward qualitative convergence."
    artifacts: ["output.md"]
  - name: maturity-check
    sheets: 1
    instrument_guidance: "cli — executes the maturity assessment script to determine if output has reached target maturity state"
    fallback_friendly: false
    purpose: "Execute the maturity assessor script to determine if output has achieved desired maturity; exit code controls self-chaining termination."
    artifacts: []
composes_with:
  - pattern: "Fixed-Point Iteration"
    how: "Soil Maturity Index provides domain-specific convergence detection where Fixed-Point Iteration uses only structural no-change metrics."
  - pattern: "Back-Slopping (Learning Inheritance)"
    how: "Back-Slopping (Learning Inheritance) extracts learnings from iterations; Soil Maturity Index determines when iterations have produced sufficient signal for learning."
  - pattern: "Delphi Convergence"
    how: "Delphi Convergence measures consensus across independent attempts; Soil Maturity Index assesses convergence within a single iterative stream."
script_dependencies:
  - "maturity_assessor.py"
config_features:
  - "self_chaining"
---

## Soil Maturity Index

`Status: Working` · **Source:** Soil science maturity metrics. **Forces:** Convergence Imperative.

### Core Dynamic

Domain-specific termination condition for iterative processes. Instead of "nothing changed" (Fixed-Point) or "all sections pass" (Rehearsal Spotlight), the maturity index measures a qualitative shift — the output has changed CHARACTER, not just improved. A script-driven exit code determines termination.

### When to Use / When NOT to Use

Use when convergence is qualitative (the writing style matured, the architecture became cohesive). Not when convergence is structural.

### Marianne Score Structure

```yaml
sheets:
  - name: iterate
    prompt: "Read output. Improve based on maturity criteria."
    capture_files: ["output/**"]
  - name: maturity-check
    instrument: cli
    validations:
      - type: command_succeeds
        command: "python3 {{ workspace }}/maturity_assessor.py --output {{ workspace }}/output.md"
on_success:
  action: self
  inherit_workspace: true
  max_chain_depth: 10
```

### Failure Mode

Maturity metric doesn't capture the intended qualitative shift. Iterate on the assessor, not just the output.

### Composes With

Fixed-Point Iteration, Back-Slopping (Learning Inheritance), Delphi Convergence
