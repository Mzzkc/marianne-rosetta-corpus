---
name: "Read-and-React"
scale: adaptation
type: prompt-technique
status: working
forces:
  - "Partial Failure"
  - "Information Asymmetry"
generators:
  - "Gate on Environmental Readiness"
problem: "Downstream agents follow fixed behavior regardless of upstream results because their prompts don't instruct them to inspect and adapt to workspace state."
signals:
  - "downstream behavior should change based on upstream results"
  - "adaptation path is not known before execution begins"
  - "workspace state determines which work is needed next"
  - "agents proceed with default behavior ignoring what previous stages produced"
config_features:
  - "capture_files"
stages:
  - name: work
    sheets: 1
    instrument_guidance: "score-author's choice — any instrument capable of reading workspace files and adapting its approach; instrument depends on the actual task being adapted"
    fallback_friendly: true
    purpose: "Read workspace state from previous stages and adapt behavior based on what exists — conditionally varying approach within the prompt based on workspace artifacts."
    artifacts: []
composes_with:
  - pattern: "Triage Gate"
    how: "Triage Gate classifies fan-out outputs into quality categories that Read-and-React sheets then detect and adapt their processing strategy around."
  - pattern: "Fragmentary Order (FRAGO)"
    how: "FRAGO writes correction documents into the workspace that Read-and-React sheets detect and incorporate, adjusting behavior based on the presence and content of the FRAGO."
  - pattern: "Dormancy Gate"
    how: "Dormancy Gate waits for external conditions; Read-and-React adapts behavior based on the workspace state that exists once conditions are met and the gate opens."
---
## Read-and-React

`Status: Working` · **Source:** Basketball read-and-react offense. **Forces:** Partial Failure + Information Asymmetry.

### Core Dynamic

Downstream stages read workspace state and adapt their behavior. Not conditional branching (which requires conductor support) but workspace-driven behavioral adaptation within a sheet's prompt.

### When to Use / When NOT to Use

Use when downstream behavior should adapt to upstream results. Not when the adaptation path is known upfront.

### Marianne Score Structure

```yaml
sheets:
  - name: work
    prompt: >
      Read previous outputs. Based on what you find:
      - If analysis-complete.yaml exists: proceed to synthesis.
      - If analysis-complete.yaml is missing: extend analysis first.
    capture_files: ["analysis-*.md", "analysis-complete.yaml"]
```

### Failure Mode

Agent ignores the workspace state and proceeds with default behavior. Validate that the expected adaptation actually occurred.

### Composes With

Triage Gate, FRAGO, Dormancy Gate
