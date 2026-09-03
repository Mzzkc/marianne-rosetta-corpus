---
name: "Mission Command"
scale: score-level
type: orchestration-pattern
status: working
forces:
  - "Information Asymmetry"
generators:
  - "Contract at Interfaces"
problem: "Centralized instruction-following breaks when agents face conditions the planner didn't anticipate."
signals:
  - "tasks require agent judgment and conditions may vary"
  - "validation should check outcomes, not methods"
  - "multiple agents must coordinate around shared intent"
  - "top-down instructions are too brittle for variable conditions"
fan_out:
  execute: 4
stages:
  - name: mission-brief
    sheets: 1
    instrument_guidance: "score-author's choice — needs strong reasoning to write a clear intent envelope with testable end-state; codex-cli (gpt-5.5) or claude-code recommended"
    fallback_friendly: false
    purpose: "Write the mission brief defining PURPOSE, KEY TASKS, and END STATE."
    artifacts: ["mission-brief.md"]
  - name: execute
    sheets: "fan_out(4)"
    instrument_guidance: "claude-code or codex-cli — score-author's choice — must be capable enough for the actual task (code refactoring, analysis, etc.); instrument depends on task complexity"
    fallback_friendly: false
    purpose: "Execute the mission by reading the brief and working autonomously within the intent envelope."
    artifacts: []
dependencies: {}
composes_with:
  - pattern: "After-Action Review"
    how: "After-Action Review evaluates whether decentralized execution achieved the mission brief's end state and extracts lessons."
  - pattern: "Barn Raising"
    how: "Barn Raising establishes shared conventions before Mission Command's parallel execution, preventing convention drift across agents."
  - pattern: "Prefabrication"
    how: "Prefabrication defines strict interface contracts that constrain Mission Command agents' output format while preserving freedom of method."
---

## Mission Command

`Status: Working` · **Source:** Auftragstaktik (Prussian military doctrine). **Forces:** Information Asymmetry.

### Core Dynamic

Separate "what and why" (centralized) from "how" (decentralized). The intent envelope has three layers: **purpose** (why), **key tasks** (what), **end state** (what done looks like). Agents adapt freely within the decision space. Validate end-state achievement, never method compliance. The structural distinction: Mission Command scores have a *specific, named intent document* that replaces per-agent context acquisition, plus end-state-only validation.

### When to Use / When NOT to Use

Use when tasks require agent judgment and conditions may differ from expectations. Not for mechanical tasks or constraints so tight only one approach is valid.

### Marianne Score Structure

```yaml
sheets:
  - name: mission-brief
    prompt: >
      Write mission-brief.md with three sections:
      PURPOSE: why this refactoring matters.
      KEY TASKS: the 4 modules that must be decoupled.
      END STATE: all 340 tests pass, public API unchanged, coupling metric < 0.3.
    validations:
      - type: content_contains
        content: "PURPOSE:"
      - type: content_contains
        content: "END STATE:"
  - name: execute
    instances: 4
    prompt: "Read mission-brief.md. Decouple module {{ instance_id }}."
    capture_files: ["mission-brief.md"]
    validations:
      - type: command_succeeds
        command: "cd {{ workspace }} && python -m pytest --tb=no -q"
```

### Failure Mode

Intent briefs too vague produce incoherent decisions. Too specific collapses the decision space. The end state must be testable with `command_succeeds`.

### Composes With

After-Action Review, Barn Raising, Prefabrication
