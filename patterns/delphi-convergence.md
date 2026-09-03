---
name: "Delphi Convergence"
scale: iteration
type: orchestration-pattern
status: working
forces:
  - "Convergence Imperative"
  - "Information Asymmetry"
generators:
  - "Measure Convergence Character"
problem: "Multiple independent agents must converge without anchoring on early opinions."
signals:
  - "expert opinions vary widely and need to converge"
  - "agents anchor on initial assessments and won't update"
  - "single-round synthesis isn't achieving consensus"
fan_out:
  assess: 3
script_dependencies:
  - "check_convergence.py"
config_features:
  - "fan_out"
  - "self_chaining"
  - "command_succeeds"
stages:
  - name: assess
    sheets: "fan_out(3)"
    instrument_guidance: "score-author's choice — needs strong reasoning capability for expert assessment; codex-cli (gpt-5.5) or claude-code recommended"
    fallback_friendly: false
    purpose: "Each assessor independently evaluates the problem and documents their position, reading prior-round assessments if available."
    artifacts: []
  - name: check-convergence
    sheets: 1
    instrument_guidance: "any-wrapped CLI profile — convergence validation via user-supplied script that analyzes assessment variance"
    fallback_friendly: true
    purpose: "Run the convergence check script to determine if assessments have sufficiently converged."
    artifacts: []
dependencies: {}
composes_with:
  - pattern: "Source Triangulation"
    how: "Source Triangulation verifies consistency across one-pass multi-perspective views; Delphi Convergence extends to iterative rounds where perspectives update toward consensus."
  - pattern: "Rashomon Gate"
    how: "Rashomon Gate captures multiple conflicting perspectives; Delphi Convergence iterates those perspectives toward measurable convergence."
---

## Delphi Convergence

`Status: Working` · **Source:** Delphi method (RAND Corporation). **Forces:** Convergence Imperative + Information Asymmetry.

### Core Dynamic

Multiple agents independently assess, then converge through structured rounds. Different from Fan-out + Synthesis (one round). Delphi iterates until convergence — each round shares anonymized prior assessments, allowing agents to update positions.

### When to Use / When NOT to Use

Use when independent expert judgment needs convergence. Not when a single assessment suffices.

### Marianne Score Structure

```yaml
sheets:
  - name: assess
    instances: 3
    prompt: "Read prior round results if they exist. Write your independent assessment."
    capture_files: ["round-*/**"]
  - name: check-convergence
    instrument: cli
    validations:
      - type: command_succeeds
        command: "python3 {{ workspace }}/check_convergence.py --threshold 0.8"
on_success:
  action: self
  inherit_workspace: true
  max_chain_depth: 5
```

### Failure Mode

Agents anchor on first-round assessments and never genuinely update. Validate that positions actually change between rounds.

### Composes With

Source Triangulation, Rashomon Gate
