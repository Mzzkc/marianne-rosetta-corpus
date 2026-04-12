---
name: "Lines of Effort"
scale: concert-level
type: orchestration-pattern
status: approximation
forces:
  - "Information Asymmetry"
  - "Finite Resources"
generators: []
problem: "Parallel campaign workstreams drift apart without convergence mechanisms connecting distinct efforts toward a unified end state."
signals:
  - "campaign has distinct workstreams with different objectives"
  - "parallel efforts must converge toward a shared end state"
  - "workstreams need autonomy but unified direction"
  - "coordination should happen through shared state, not message passing"
approximation_note: "The YAML demonstrates a single-score approximation using fan-out sheets for parallel lines. True Lines of Effort requires concert-level orchestration where each line is its own score with independent instruments, success criteria, and lifecycle, coordinated through shared workspace state."
config_features:
  - fan_out
fan_out:
  line-work: 3
stages:
  - name: define-lines
    sheets: 1
    instrument_guidance: "score-author's choice — needs strong reasoning to define distinct objectives and measurable convergence criteria for each line"
    fallback_friendly: false
    purpose: "Define lines of effort with objectives and convergence criteria."
    artifacts: ["lines-definition.md"]
  - name: line-work
    sheets: "fan_out(3)"
    instrument_guidance: "score-author's choice — each line may need different capability depending on its objective; instrument should match the line's task complexity"
    fallback_friendly: true
    purpose: "Execute each line of effort per its defined objectives, working independently within shared workspace."
    artifacts: []
  - name: convergence-check
    sheets: 1
    instrument_guidance: "score-author's choice — needs strong synthesis capability to assess convergence across all lines toward unified end state"
    fallback_friendly: false
    purpose: "Read all line outputs and assess convergence toward the unified end state."
    artifacts: []
composes_with:
  - pattern: "Season Bible"
    how: "Season Bible maintains the mutable reference document that tracks evolving state across lines, ensuring continuity as each line progresses."
  - pattern: "After-Action Review"
    how: "After-Action Review evaluates each line's execution against its objectives, feeding lessons into subsequent convergence checks."
  - pattern: "Barn Raising"
    how: "Barn Raising establishes shared conventions across all lines before parallel execution begins, preventing convention drift between independent workstreams."
---

## Lines of Effort

`Status: Working (single-score approximation)` · **Source:** Military operational design (JP 5-0). **Forces:** Information Asymmetry + Finite Resources.

### Core Dynamic

Sustained parallel campaigns with different objectives converging toward a unified end state. Each line has its own scores, instruments, and success criteria. Coordination through shared workspace state, not message passing. Requires concert-level orchestration with multiple scores.

### When to Use / When NOT to Use

Use for large campaigns with distinct workstreams that must converge. Not when workstreams are independent or campaign is short.

### Marianne Score Structure

```yaml
# Single-score approximation — true Lines of Effort requires a concert
sheets:
  - name: define-lines
    prompt: "Define 3 lines of effort with objectives and convergence criteria."
  - name: line-work
    instances: 3
    prompt: "Execute line {{ instance_id }} per the defined objectives."
    capture_files: ["lines-definition.md"]
  - name: convergence-check
    prompt: "Read all line outputs. Assess convergence toward unified end state."
    capture_files: ["line-*/**"]
```

### Failure Mode

Lines diverge without convergence checks. Regular synchronization points are essential.

### Composes With

Season Bible, After-Action Review, Barn Raising
