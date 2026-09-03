---
name: "Nurse Log"
scale: score-level
type: orchestration-pattern
status: working
forces:
  - "Finite Resources"
generators: []
problem: "Downstream stages waste resources redoing common preparation work because no shared substrate exists."
signals:
  - "multiple stages need the same research or data collection"
  - "agents are duplicating preparation work"
  - "downstream work is blocked waiting for common prerequisites"
config_features:
  - "fan_out"
fan_out:
  work: 4
stages:
  - name: prepare-substrate
    sheets: 1
    instrument_guidance: "score-author's choice — needs capability for thorough research, data collection, and organization; codex-cli (gpt-5.5) or claude-code recommended because substrate quality is load-bearing for all downstream instances"
    fallback_friendly: false
    purpose: "Research the domain, collect reference material, and organize it into shared substrate."
    artifacts: ["substrate/"]
  - name: work
    sheets: "fan_out(4)"
    instrument_guidance: "claude-code or codex-cli — score-author's choice — depends on component-building task complexity; substrate reading requires minimal capability, but actual component construction may require more reasoning"
    fallback_friendly: true
    purpose: "Build component using the prepared substrate."
    artifacts: []
dependencies: {}
composes_with:
  - pattern: "Fermentation Relay"
    how: "Fermentation Relay can escalate the substrate preparation stage if initial research proves insufficient for downstream work."
  - pattern: "Fan-out + Synthesis"
    how: "Nurse Log's work stage uses fan-out to build components in parallel; Fan-out + Synthesis adds a synthesis stage to combine those parallel outputs."
---

## Nurse Log

`Status: Working` · **Source:** Forest ecology (nurse logs). **Forces:** Finite Resources.

### Core Dynamic

A preparation stage creates general-purpose substrate (research, data collection, organization) that makes downstream stages more productive. Different from Reconnaissance Pull (which discovers the approach). Nurse Log prepares the ground regardless of approach.

### When to Use / When NOT to Use

Use when downstream stages share common preparation needs. Not when preparation is stage-specific.

### Marianne Score Structure

```yaml
sheets:
  - name: prepare-substrate
    prompt: "Research the domain. Collect reference material. Organize into substrate/."
    validations:
      - type: file_exists
        path: "{{ workspace }}/substrate/"
  - name: work
    instances: 4
    prompt: "Read substrate/. Build component {{ instance_id }}."
    capture_files: ["substrate/**"]
```

### Failure Mode

Substrate too generic to help. Make preparation specific to the downstream work, not a generic research dump.

### Composes With

Fermentation Relay, Fan-out + Synthesis

---

# Concert-Level Patterns
