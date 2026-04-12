---
name: "Forward Observer"
scale: instrument-strategy
type: orchestration-pattern
status: working
forces:
  - "Finite Resources"
  - "Information Asymmetry"
generators:
  - "Match Instrument to Grain"
problem: "Expensive instruments waste resources reading raw input; cheap summarization can preserve actionable information."
signals:
  - "input exceeds available context window"
  - "expensive instrument required for main task"
  - "token costs dominate total cost"
  - "most input is redundant or low-value"
stages:
  - name: observe
    sheets: 1
    instrument_guidance: "haiku — fast, cheap observation; sufficient for compression and extraction of key items"
    fallback_friendly: true
    purpose: "Read large input and extract key findings and actionable items into observer-brief.md."
    artifacts: ["observer-brief.md"]
  - name: operate
    sheets: 1
    instrument_guidance: "opus — full reasoning capability required for detailed analysis on compressed input"
    fallback_friendly: false
    purpose: "Execute main analysis and detailed work based on the observer-brief.md summary."
    artifacts: []
composes_with:
  - pattern: "Relay Zone"
    how: "Forward Observer produces a formatted brief that Relay Zone can reliably relay between stages."
  - pattern: "Screening Cascade"
    how: "Screening Cascade filters volume before Forward Observer compresses the remainder for expensive instruments."
  - pattern: "Immune Cascade"
    how: "Immune Cascade escalates difficult items to expensive instruments; Forward Observer compresses large items for those same instruments."
---

## Forward Observer

`Status: Working` · **Source:** Military forward observation. **Forces:** Finite Resources + Information Asymmetry.

### Core Dynamic

A cheap, fast observer (instrument: haiku or sonnet) reads large input and produces a compressed brief for the expensive operator (instrument: opus). Reduces context window pressure and cost. The observer cost must save more tokens downstream than it consumes.

### When to Use / When NOT to Use

Use when input is too large for the main instrument or when cheap summarization preserves actionable information. Not when all information is critical.

### Marianne Score Structure

```yaml
sheets:
  - name: observe
    instrument: haiku
    prompt: "Read the full input. Write observer-brief.md: key findings, actionable items only."
    validations:
      - type: file_exists
        path: "{{ workspace }}/observer-brief.md"
  - name: operate
    instrument: opus
    prompt: "Read observer-brief.md. Execute the detailed analysis."
    capture_files: ["observer-brief.md"]
```

### Failure Mode

Observer discards critical information. Validate by checking brief covers all major topics from the input.

### Composes With

Relay Zone, Screening Cascade, Immune Cascade
