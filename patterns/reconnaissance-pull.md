---
name: "Reconnaissance Pull"
scale: score-level
type: orchestration-pattern
status: working
forces:
  - "Information Asymmetry"
generators:
  - "Accumulate Knowledge"
problem: "Planning without prior exploration risks misaligned approaches and wasted effort."
signals:
  - "task structure and complexity are unclear"
  - "initial exploration costs are low relative to execution"
  - "approach is not obvious from requirements alone"
config_features:
  - capture_files
stages:
  - name: recon
    sheets: 1
    instrument_guidance: "sonnet — balanced cost and capability; sufficient for landscape discovery without deep reasoning"
    fallback_friendly: true
    purpose: "Discover and document the landscape of the input: structure, complexity, and risks."
    artifacts: ["recon-report.md"]
  - name: plan
    sheets: 1
    instrument_guidance: "score-author's choice — planning complexity depends on task and landscape complexity; stronger instruments benefit from comprehensive recon"
    fallback_friendly: true
    purpose: "Analyze reconnaissance findings and synthesize a detailed execution plan."
    artifacts: ["execution-plan.md"]
  - name: execute
    sheets: 1
    instrument_guidance: "score-author's choice — execution capability must match task requirements; recon and plan inform instrument selection"
    fallback_friendly: false
    purpose: "Execute the work as specified in the execution plan."
    artifacts: []
composes_with:
  - pattern: "Mission Command"
    how: "Reconnaissance Pull provides landscape discovery before Mission Command agents begin execution within their intent envelope."
  - pattern: "Canary Probe"
    how: "Reconnaissance Pull informs Canary Probe's incremental exposure strategy by discovering the landscape before probing begins."
---

## Reconnaissance Pull

`Status: Working` · **Source:** Military reconnaissance doctrine. **Forces:** Information Asymmetry.

### Core Dynamic

A cheap, fast reconnaissance stage discovers the landscape before committing to a plan. The recon output is advisory — downstream stages read it and adapt. Different from Forward Observer (which compresses). Reconnaissance discovers.

### When to Use / When NOT to Use

Use when the approach isn't obvious and exploration is cheap. Not when the task is well-understood.

### Marianne Score Structure

```yaml
sheets:
  - name: recon
    instrument: sonnet
    prompt: "Survey the input. Write recon-report.md: structure, complexity, risks, recommended approach."
    validations:
      - type: file_exists
        path: "{{ workspace }}/recon-report.md"
  - name: plan
    prompt: "Read recon-report.md. Write execution plan."
    capture_files: ["recon-report.md"]
  - name: execute
    prompt: "Execute per plan."
    capture_files: ["execution-plan.md"]
```

### Failure Mode

Recon is too shallow to inform planning. Use a more capable instrument for recon if the domain is complex.

### Composes With

Mission Command, Canary Probe
