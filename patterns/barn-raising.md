---
name: "Barn Raising"
scale: score-level
type: orchestration-pattern
status: working
forces:
  - "Producer-Consumer Mismatch"
  - "Finite Resources"
generators:
  - "Contract at Interfaces"
problem: "Parallel work streams produce inconsistent structure and style when each agent makes independent convention choices."
signals:
  - "parallel agents will work on similar types of artifacts"
  - "consistency in naming, structure, or style matters for integration"
  - "each agent might make reasonable but incompatible choices"
  - "prefabrication contracts aren't enough — need broader standards"
fan_out:
  build: 6
config_features:
  - "fan_out"
  - "capture_files"
stages:
  - name: conventions
    sheets: 1
    instrument_guidance: "score-author's choice — needs strong reasoning to anticipate integration needs and write comprehensive but not overly rigid conventions; sonnet or opus recommended"
    fallback_friendly: true
    purpose: "Write a conventions document defining naming, structure, and stylistic standards for parallel work streams."
    artifacts: ["conventions.md"]
  - name: build
    sheets: "fan_out(6)"
    instrument_guidance: "score-author's choice — depends on task complexity; instrument must be capable of the actual work being coordinated"
    fallback_friendly: true
    purpose: "Build assigned component following the shared conventions."
    artifacts: []
dependencies:
  build: ["conventions"]
composes_with:
  - pattern: "Prefabrication"
    how: "Prefabrication defines strict interface contracts (input/output schemas), while Barn Raising establishes broader conventions (naming, style, structure) that complement those contracts."
  - pattern: "Mission Command"
    how: "Mission Command provides the intent envelope defining what to achieve, while Barn Raising provides the implementation conventions defining how to structure the work."
  - pattern: "Lines of Effort"
    how: "Lines of Effort separates parallel streams of work; Barn Raising ensures those streams remain consistent through shared conventions."
---

## Barn Raising

`Status: Working` · **Source:** Community barn raising (Amish). **Forces:** Producer-Consumer Mismatch + Finite Resources.

### Core Dynamic

Shared conventions established before parallel work. A conventions document defines naming, structure, interfaces. All parallel tracks read it. Different from Prefabrication (which defines interfaces). Barn Raising defines conventions — broader scope, softer constraints.

### When to Use / When NOT to Use

Use when parallel agents need consistency beyond interface contracts. Not when a single agent does all work.

### Marianne Score Structure

```yaml
sheets:
  - name: conventions
    prompt: "Write conventions.md: naming rules, file structure, code style."
    validations:
      - type: file_exists
        path: "{{ workspace }}/conventions.md"
  - name: build
    instances: 6
    prompt: "Read conventions.md. Build component {{ instance_id }}."
    capture_files: ["conventions.md"]
```

### Failure Mode

Conventions too vague to enforce consistency. Too rigid to allow agent judgment. Strike the balance based on integration requirements.

### Composes With

Prefabrication, Mission Command, Lines of Effort
