---
name: "Fixed-Point Iteration"
scale: iteration
type: orchestration-pattern
status: working
forces:
  - "Convergence Imperative"
generators:
  - "Measure Convergence Character"
problem: "Iterative refinement requires explicit convergence detection to avoid wasting iterations."
signals:
  - "repeated application produces improvements but stopping criterion is unclear"
  - "iterations are expensive and need measurable termination beyond fixed counts"
  - "output stabilizes after refinement but manual convergence checking is tedious"
config_features:
  - "self_chaining"
stages:
  - name: iterate
    sheets: 1
    instrument_guidance: "claude-code or codex-cli — score-author's choice — the improvement task itself determines required instrument capability; Fixed-Point Iteration prescribes no specific tier"
    fallback_friendly: true
    purpose: "Read the previous iteration's output and improve it."
    artifacts:
      - "output.md"
  - name: convergence-check
    sheets: 1
    instrument_guidance: "claude-code or codex-cli — cli instrument is required — the convergence validation uses actual shell commands (diff) to measure iteration deltas"
    fallback_friendly: false
    purpose: "Check if output has converged by comparing current iteration to previous."
    artifacts: []
dependencies: {}
composes_with:
  - pattern: "CDCL Search"
    how: "CDCL Search instantiates fixed-point iteration as a SAT solver, iteratively refining clause sets toward satisfiability."
  - pattern: "Cathedral Construction"
    how: "Cathedral Construction applies fixed-point iteration to progressively refine and layer architectural components."
  - pattern: "Memoization Cache"
    how: "Memoization Cache optimizes fixed-point iteration by caching intermediate results across refinement cycles."
---

## Fixed-Point Iteration

`Status: Working` · **Source:** Numerical analysis, compiler dataflow. **Forces:** Convergence Imperative.

### Core Dynamic

Repeat the same operation until the output stops changing. Convergence is structural: diff the output of iteration N against iteration N-1. When the diff is empty (or below threshold), stop.

### When to Use / When NOT to Use

Use when the task naturally converges (each pass finds fewer issues). Not when convergence isn't guaranteed.

### Marianne Score Structure

```yaml
sheets:
  - name: iterate
    prompt: "Read previous output. Improve. Write output."
    capture_files: ["output.md"]
  - name: convergence-check
    instrument: cli
    validations:
      - type: command_succeeds
        command: "diff {{ workspace }}/output-prev.md {{ workspace }}/output.md | wc -l | xargs test 5 -gt"
on_success:
  action: self
  inherit_workspace: true
  max_chain_depth: 10
```

### Failure Mode

Never converges. `max_chain_depth` provides the safety bound.

### Composes With

CDCL Search, Cathedral Construction, Memoization Cache
