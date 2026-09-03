---
name: "Commissioning Cascade"
scale: instrument-strategy
type: orchestration-pattern
status: working
forces:
  - "Instrument-Task Fit"
  - "Exponential Defect Cost"
generators:
  - "Match Instrument to Grain"
  - "Graduate & Filter"
problem: "Different validation scopes require different tools; single-pass validation misses issues or wastes resources."
signals:
  - "unit tests pass but integration fails"
  - "validation is slow because all scopes use expensive instruments"
  - "can't diagnose failures because all tests run together"
  - "need different rigor levels for different scopes"
stages:
  - name: unit-check
    sheets: 1
    instrument_guidance: "any-wrapped CLI profile — required for reliable shell command execution; capability is running shell commands"
    fallback_friendly: true
    purpose: "Run unit tests against the codebase."
    artifacts: []
  - name: integration-check
    sheets: 1
    instrument_guidance: "any-wrapped CLI profile — required for reliable shell command execution; capability is running shell commands"
    fallback_friendly: true
    purpose: "Run integration tests against deployed services."
    artifacts: []
  - name: acceptance-review
    sheets: 1
    instrument_guidance: "score-author's choice — needs strong reasoning to evaluate test results against requirements; codex-cli (gpt-5.5) or claude-code recommended"
    fallback_friendly: false
    purpose: "Read test results and write acceptance report."
    artifacts: []
dependencies: {}
composes_with:
  - pattern: "Echelon Repair"
    how: "Echelon Repair classifies work items by difficulty; Commissioning Cascade validates each echelon's output using tier-appropriate validation instruments."
  - pattern: "Shipyard Sequence"
    how: "Shipyard Sequence progresses through launch stages; Commissioning Cascade validates each stage with scope-appropriate instruments."
  - pattern: "The Tool Chain"
    how: "The Tool Chain chains tools together; Commissioning Cascade validates the output of each tool using scope-appropriate instruments."
---

## Commissioning Cascade

`Status: Working` · **Source:** Marine vessel commissioning. **Forces:** Instrument-Task Fit + Exponential Defect Cost.

### Core Dynamic

Validate at multiple scopes using different tools at each level. Unit → integration → acceptance, each with scope-appropriate validation instruments. Split chained validations into separate checks so failures are diagnosable.

### When to Use / When NOT to Use

Use when different validation scopes require different tools. Not when a single validation pass suffices.

### Marianne Score Structure

```yaml
sheets:
  - name: unit-check
    instrument: cli
    validations:
      - type: command_succeeds
        command: "cd {{ workspace }} && python -m pytest tests/unit/ -q"
  - name: integration-check
    instrument: cli
    validations:
      - type: command_succeeds
        command: "cd {{ workspace }} && python -m pytest tests/integration/ -q"
  - name: acceptance-review
    prompt: "Read test results. Write acceptance report against the original requirements."
    capture_files: ["test-results/**"]
```

### Failure Mode

Unit tests pass but integration fails — the cascade catches this. If all validation is at one level, cascading adds no value.

### Composes With

Echelon Repair, Shipyard Sequence, The Tool Chain
