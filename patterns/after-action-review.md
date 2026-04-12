---
name: "After-Action Review"
scale: iteration
type: orchestration-pattern
status: working
forces:
  - "Information Asymmetry"
  - "Partial Failure"
generators:
  - "Accumulate Knowledge"
  - "Exploit Failure as Signal"
problem: "Execution insights are lost between iterations because no systematic reflection captures what worked, what failed, and why."
signals:
  - "same mistakes happen repeatedly across iterations"
  - "execution insights disappear after completion"
  - "teams don't know what actually worked or why it worked"
  - "improvement recommendations don't reach subsequent iterations"
config_features:
  - "capture_files"
stages:
  - name: aar
    sheets: 1
    instrument_guidance: "sonnet or opus recommended — must synthesize multiple execution outputs, identify concrete deltas between intent and reality, extract actionable lessons with specific references; cheaper instruments risk the documented failure mode (generic platitudes without specific output references)"
    fallback_friendly: false
    purpose: "Analyze execution outcomes against original intent, identify concrete deltas, extract what to sustain and what to improve for next iteration."
    artifacts: ["aar.md"]
composes_with:
  - pattern: "Immune Cascade"
    how: "AAR analyzes which items graduated through Immune Cascade's tier gates and extracts lessons about gate criteria effectiveness for refinement."
  - pattern: "Cathedral Construction"
    how: "AAR captures lessons from each Cathedral Construction iteration and feeds improvements into the next cycle's prelude as accumulated knowledge."
  - pattern: "Back-Slopping (Learning Inheritance)"
    how: "AAR generates the aar.md artifact that Back-Slopping (Learning Inheritance) propagates forward as starter culture to seed the next iteration with learning inheritance."
---

## After-Action Review

`Status: Working` · **Source:** US Army AAR protocol. **Forces:** Information Asymmetry + Partial Failure.

### Core Dynamic

Dedicated review stage after execution. Not quality checking (that's validation). AAR asks: what was supposed to happen, what actually happened, why the difference, what to change. The AAR output feeds the next iteration's prelude.

### When to Use / When NOT to Use

Use after any significant execution to capture learning. Not for trivial tasks.

### Marianne Score Structure

```yaml
sheets:
  - name: aar
    prompt: >
      Read all execution outputs. Write aar.md:
      INTENDED: what the score was supposed to produce.
      ACTUAL: what was actually produced.
      DELTA: why the difference.
      SUSTAIN: what worked.
      IMPROVE: what to change next time.
    capture_files: ["**"]
    validations:
      - type: content_contains
        content: "SUSTAIN:"
      - type: content_contains
        content: "IMPROVE:"
```

### Failure Mode

AAR is generic platitudes. Validate specific references to actual outputs and concrete improvement recommendations.

### Composes With

Immune Cascade, Cathedral Construction, Back-Slopping (Learning Inheritance)
