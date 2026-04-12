---
name: "Dormancy Gate"
scale: score-level
type: orchestration-pattern
status: working
forces:
  - "Finite Resources"
generators:
  - "Gate on Environmental Readiness"
problem: "External prerequisites are not immediately available, but work cannot safely proceed without them."
signals:
  - "downstream work depends on external system state"
  - "prerequisites will eventually be satisfied but are not immediate"
  - "need to wait and retry, not fail outright"
stages:
  - name: check-conditions
    sheets: 1
    instrument_guidance: "cli — lightweight condition testing via command execution; no LLM reasoning required"
    fallback_friendly: true
    purpose: "Verify that external conditions are satisfied by testing workspace state or running verification commands."
    artifacts: []
  - name: proceed
    sheets: 1
    instrument_guidance: "score-author's choice — instrument selection depends on the task being performed"
    fallback_friendly: true
    purpose: "Proceed with the actual work once external conditions are confirmed ready."
    artifacts: []
composes_with:
  - pattern: "Read-and-React"
    how: "Dormancy Gate pauses until conditions warrant re-evaluation, enabling Read-and-React to dynamically re-run the score."
  - pattern: "Shipyard Sequence"
    how: "Dormancy Gate ensures each shipyard phase waits for its external prerequisites before proceeding."
---

## Dormancy Gate

`Status: Working` · **Source:** Seed dormancy in botany. **Forces:** Finite Resources.

### Core Dynamic

A gate that waits for external conditions before proceeding. The gate checks workspace state — if conditions aren't met, the score self-chains and checks again. Unlike a validation (which fails the score), dormancy gates pause and retry.

### When to Use / When NOT to Use

Use when work depends on external conditions that will eventually be met. Not when conditions are already known.

### Marianne Score Structure

```yaml
sheets:
  - name: check-conditions
    instrument: cli
    validations:
      - type: command_succeeds
        command: "test -f {{ workspace }}/external-data-ready.flag"
  - name: proceed
    prompt: "Conditions met. Begin processing."
    capture_files: ["external-data/**"]
```

### Failure Mode

External condition never materializes. `max_chain_depth` provides a safety bound.

### Composes With

Read-and-React, Shipyard Sequence
