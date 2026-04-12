---
name: "Composting Cascade"
scale: score-level
type: orchestration-pattern
status: working
forces:
  - "Accumulated Signal"
  - "Instrument-Task Fit"
generators:
  - "Threshold-Triggered Switch"
  - "Match Instrument to Grain"
problem: "Phase transitions in iterative work need measurable readiness signals rather than time-based or manual progression decisions."
signals:
  - "phase transitions are time-based or manual, not metrics-driven"
  - "unclear when simple work is complete and should escalate to complex restructuring"
  - "churn rates don't drive phase changes, even when they indicate ongoing work"
  - "workspace readiness isn't observable"
stages:
  - name: simple-work
    sheets: 1
    instrument_guidance: "score-author's choice — simple cleanup (renaming, type hints, extraction) is cost-sensitive but needs reasoning; haiku recommended"
    fallback_friendly: true
    purpose: "Execute simple cleanup tasks (renaming, type hints, function extraction)."
    artifacts: []
  - name: temperature-check
    sheets: 1
    instrument_guidance: "cli — shell script measuring workspace metrics (type coverage, test pass rate, etc.); must support --threshold argument"
    fallback_friendly: false
    purpose: "Check if workspace metrics meet threshold for phase transition."
    artifacts: []
  - name: complex-work
    sheets: 1
    instrument_guidance: "opus — complex restructuring (abstractions, algorithm rewrites) requires full reasoning capability; haiku or sonnet insufficient"
    fallback_friendly: false
    purpose: "Execute complex restructuring (abstractions, algorithm rewrites)."
    artifacts: []
  - name: cooling-check
    sheets: 1
    instrument_guidance: "cli — shell script measuring change rate (code churn, diff magnitude); must support --max-churn argument"
    fallback_friendly: false
    purpose: "Check if work is cooling (change rate below exhaustion threshold)."
    artifacts: []
  - name: maturation
    sheets: 1
    instrument_guidance: "haiku — documentation writing is cost-sensitive; cheaper instrument sufficient for guides and changelogs"
    fallback_friendly: true
    purpose: "Write documentation (migration guide, changelog)."
    artifacts: ["migration-guide.md", "changelog.md"]
composes_with:
  - pattern: "The Tool Chain"
    how: "Composting Cascade uses CLI instruments (Tool Chain) as workspace thermometers to measure readiness for phase transitions."
  - pattern: "Succession Pipeline"
    how: "Composting Cascade IS succession with metric-driven phase gates rather than time-based progression."
  - pattern: "Echelon Repair"
    how: "Composting Cascade escalates instruments per phase; complex-work uses opus while simple-work and maturation use cheaper instruments."
script_dependencies:
  - "temperature.py"
  - "exhaustion.py"
---

## Composting Cascade

`Status: Working` · **Source:** Four-phase composting microbiology, Expedition 2. **Scale:** score-level + instrument strategy. **Iteration:** 4. **Force:** Threshold Accumulation.

### Core Dynamic

The work's own output drives phase transitions. CLI instruments measure workspace state ("temperature") and threshold crossings trigger phase changes. The agents don't know they're transitioning — the thermometer knows. CLI instruments are in the control loop; AI instruments are the workers.

**"Temperature" defined:** Workspace metrics that indicate readiness for the next phase. Examples: type coverage percentage (for refactoring), test pass rate (for code generation), function count per file (for extraction work). The metric must be measurable by a CLI script and meaningfully indicate phase readiness.

**Script dependencies:** `temperature.py` and `exhaustion.py` are user-supplied. Interface contract: `temperature.py --threshold N` exits 0 if temperature meets threshold, exits 1 otherwise. `exhaustion.py --max-churn N` exits 0 if change rate is below threshold (work is cooling), exits 1 otherwise.

### When to Use / When NOT to Use

Use for multi-phase projects where work nature should change based on measurable workspace state, codebase refactoring where simple cleanup enables complex restructuring, or documentation campaigns where raw generation enables consolidation. Not when workspace metrics don't reflect work state, phase transitions need human judgment, or the work is single-phase.

### Marianne Score Structure

```yaml
sheets:
  - name: simple-work
    prompt: "Execute simple cleanup tasks. Rename variables, add type hints, extract functions."
  - name: temperature-check
    instrument: cli
    validations:
      - type: command_succeeds
        command: "python3 {{ workspace }}/temperature.py --threshold 60"
  - name: complex-work
    instrument: opus
    prompt: "Execute complex restructuring. Introduce abstractions, rewrite algorithms."
    capture_files: ["temperature-report.yaml"]
  - name: cooling-check
    instrument: cli
    validations:
      - type: command_succeeds
        command: "python3 {{ workspace }}/exhaustion.py --max-churn 5"
  - name: maturation
    instrument: haiku
    prompt: "Write documentation, migration guide, changelog."
```

### Failure Mode

Temperature metric doesn't correlate with actual readiness — complex-work fires too early and fails because the codebase isn't ready. Calibrate thresholds empirically: run the pipeline once, observe when complex-work succeeds, set the threshold there. If temperature never rises (simple-work doesn't change the measured metric), the cascade stalls at the temperature check.

### Composes With

The Tool Chain (CLI instruments as thermometers), Succession Pipeline (composting IS succession with metric-driven gates), Echelon Repair (instrument escalation per phase)
