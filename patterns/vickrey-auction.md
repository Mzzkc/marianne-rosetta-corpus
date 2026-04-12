---
name: "Vickrey Auction"
scale: instrument-strategy
type: orchestration-pattern
status: approximation
forces:
  - "Instrument-Task Fit"
generators:
  - "Match Instrument to Grain"
problem: "Selecting an instrument without evidence wastes resources or produces inferior results when multiple candidates are viable."
signals:
  - "multiple instruments are available and it's unclear which performs best"
  - "instrument choice is based on guesswork, not evidence"
  - "cost or quality varies significantly across instruments for the same task"
approximation_note: "The YAML covers competitive probing and evaluation but not dynamic instrument selection for the full run. Using the winning instrument requires a two-score concert or human-in-the-loop step, which cannot be expressed in a single score."
stages:
  - name: probe-haiku
    sheets: 1
    instrument_guidance: "haiku — one of the candidate instruments being competitively evaluated"
    fallback_friendly: false
    purpose: "Process a sample item using haiku to produce a probe output for comparison."
    artifacts: ["probe-haiku.md"]
  - name: probe-sonnet
    sheets: 1
    instrument_guidance: "sonnet — one of the candidate instruments being competitively evaluated"
    fallback_friendly: false
    purpose: "Process the same sample item using sonnet to produce a probe output for comparison."
    artifacts: ["probe-sonnet.md"]
  - name: evaluate
    sheets: 1
    instrument_guidance: "score-author's choice — needs judgment capability to compare outputs and recommend an instrument; sonnet or opus recommended"
    fallback_friendly: true
    purpose: "Compare probe outputs and write an instrument recommendation with rationale."
    artifacts: ["instrument-recommendation.yaml"]
composes_with:
  - pattern: "Echelon Repair"
    how: "Vickrey Auction's probe results inform which instrument tiers to assign in Echelon Repair's classification-based routing."
  - pattern: "Canary Probe"
    how: "Canary Probe tests pipeline viability on a data subset; Vickrey Auction tests instrument fitness on the same task, combining to validate both pipeline and instrument choice before full commitment."
---

## Vickrey Auction

`Status: Working (two-run approximation)` · **Source:** Vickrey auction theory. **Forces:** Instrument-Task Fit.

### Core Dynamic

Competitive probing: run the same task on multiple instruments, evaluate which performed best, use that instrument for the full run. The probing informs the NEXT run, not this one — dynamic instrument selection requires either a two-score concert or human-in-the-loop step.

### When to Use / When NOT to Use

Use when multiple instruments are available and it's unclear which performs best. Not when one instrument is clearly superior.

### Marianne Score Structure

```yaml
sheets:
  - name: probe-haiku
    instrument: haiku
    prompt: "Process the sample item. Write probe-haiku.md."
  - name: probe-sonnet
    instrument: sonnet
    prompt: "Process the same sample item. Write probe-sonnet.md."
  - name: evaluate
    prompt: "Compare probe outputs. Write instrument-recommendation.yaml: {winner, rationale}."
    capture_files: ["probe-haiku.md", "probe-sonnet.md"]
```

### Failure Mode

Probe item isn't representative of the full workload. Use multiple probe items.

### Composes With

Echelon Repair, Canary Probe
