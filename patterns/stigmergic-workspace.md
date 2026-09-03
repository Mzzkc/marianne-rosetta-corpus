---
name: "Stigmergic Workspace"
scale: communication
type: orchestration-pattern
status: working
forces:
  - "Information Asymmetry"
  - "Finite Resources"
generators: []
problem: "Parallel agents duplicate effort or produce conflicts because they lack visibility into each other's progress and decisions."
signals:
  - "parallel agents need loose coordination without direct messaging"
  - "workspace files already capture meaningful state other agents need"
  - "real-time coordination would create bottlenecks"
  - "agents react to each other's outputs, not each other's messages"
config_features:
  - "fan_out"
  - "capture_files"
fan_out:
  work: 8
stages:
  - name: work
    sheets: "fan_out(8)"
    instrument_guidance: "claude-code or codex-cli — score-author's choice — this is a communication mechanism, not an execution prescription; instrument depends entirely on the actual task the workers perform"
    fallback_friendly: true
    purpose: "Read workspace for current state, perform assigned work, write results and signals to shared directories for other workers to discover."
    artifacts: ["shared/signals/"]
dependencies: {}
composes_with:
  - pattern: "Barn Raising"
    how: "Barn Raising establishes shared workspace conventions (naming, directory structure, file formats) that prevent Stigmergic Workspace's failure mode of conflicting writes."
  - pattern: "Lines of Effort"
    how: "Lines of Effort organizes sustained parallel campaigns that use Stigmergic Workspace as their coordination mechanism — each line reads and writes to shared workspace state."
---

## Stigmergic Workspace

`Status: Working` · **Source:** Ant colony optimization. **Forces:** Information Asymmetry + Finite Resources.

### Core Dynamic

Agents coordinate through workspace artifacts, not direct communication. Agent A writes a file; Agent B reads it. No messages, no coordination protocol — the workspace IS the communication channel.

### When to Use / When NOT to Use

Use when agents need loose coordination and the workspace captures state. Not when real-time coordination is needed.

### Marianne Score Structure

```yaml
sheets:
  - name: work
    instances: 8
    prompt: >
      Read workspace for current state. Do your work. Write results.
      If you find something relevant to other workers, write it to shared/signals/.
    capture_files: ["shared/signals/**"]
```

### Failure Mode

Conflicting writes to the same file. Use namespaced output directories per instance.

### Composes With

Barn Raising, Lines of Effort
