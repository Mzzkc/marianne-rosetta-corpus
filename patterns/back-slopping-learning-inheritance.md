---
name: "Back-Slopping (Learning Inheritance)"
scale: iteration
type: orchestration-pattern
status: working
forces:
  - "Convergence Imperative"
generators:
  - "Accumulate Knowledge"
problem: "Iterative processes lose hard-won insights because each iteration starts from scratch without accumulated learning."
signals:
  - "later iterations repeat mistakes from earlier ones"
  - "valuable insights discovered during work are lost between iterations"
  - "iterative process plateaus because it cannot build on prior discovery"
config_features:
  - self_chaining
stages:
  - name: work
    sheets: 1
    instrument_guidance: "claude-code or codex-cli — score-author's choice — instrument must be capable enough for the primary task and able to read and update structured culture artifacts"
    fallback_friendly: true
    purpose: "Execute the primary task informed by accumulated culture, then update the culture artifact with new learning."
    artifacts: ["culture.yaml"]
dependencies: {}
composes_with:
  - pattern: "Cathedral Construction"
    how: "Cathedral Construction's incremental building uses Back-Slopping's culture artifact to carry integration lessons and architectural decisions across iterations."
  - pattern: "CDCL Search"
    how: "CDCL Search's learned clauses are a specialized form of culture; Back-Slopping generalizes the inheritance mechanism beyond failure-specific constraints to all accumulated learning."
  - pattern: "Systemic Acquired Resistance"
    how: "Systemic Acquired Resistance broadcasts defense primers across scores in a concert; Back-Slopping carries learning forward across iterations within a single self-chaining score."
---

## Back-Slopping (Learning Inheritance)

`Status: Working` · **Source:** Sourdough bread making. **Forces:** Convergence Imperative.

### Core Dynamic

Each iteration inherits a "culture" artifact from the previous iteration containing accumulated learning. The culture grows and refines over iterations, carrying forward what worked and what to avoid.

### When to Use / When NOT to Use

Use when later iterations should benefit from earlier learning. Not when each iteration is independent.

### Marianne Score Structure

```yaml
sheets:
  - name: work
    prompt: "Read culture.yaml for accumulated learning. Do the work. Update culture.yaml with new insights."
    capture_files: ["culture.yaml"]
    validations:
      - type: file_exists
        path: "{{ workspace }}/culture.yaml"
on_success:
  action: self
  inherit_workspace: true
  max_chain_depth: 10
```

### Failure Mode

Culture grows without pruning. Old lessons that no longer apply accumulate. Include a pruning step that removes stale entries.

### Composes With

Cathedral Construction, CDCL Search, Systemic Acquired Resistance
