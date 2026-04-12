---
name: "Cathedral Construction"
scale: iteration
type: orchestration-pattern
status: working
forces:
  - "Convergence Imperative"
  - "Finite Resources"
generators:
  - "Accumulate Knowledge"
problem: "Large artifacts cannot be produced in a single pass and require iterative construction toward a known target."
signals:
  - "artifact is too large to complete in one pass"
  - "work must be built incrementally toward a target"
  - "each iteration adds structural elements"
  - "need to track progress toward a known endpoint"
config_features:
  - "self_chaining"
stages:
  - name: plan-iteration
    sheets: 1
    instrument_guidance: "score-author's choice — planning benefits from strong reasoning (sonnet/opus recommended), but the iteration cycle provides correction opportunities so mid-tier instruments are viable"
    fallback_friendly: true
    purpose: "Read current state and plan what to add this iteration."
    artifacts: []
  - name: build
    sheets: 1
    instrument_guidance: "score-author's choice — depends entirely on what is being built (code, documentation, analysis); match instrument capability to the construction task complexity"
    fallback_friendly: true
    purpose: "Execute the plan and add to the cathedral."
    artifacts: ["cathedral/**"]
  - name: inspect
    sheets: 1
    instrument_guidance: "score-author's choice — review and critique work; sonnet-level reasoning typically sufficient since this is evaluation rather than primary construction"
    fallback_friendly: true
    purpose: "Review what was built and write inspection report."
    artifacts: ["inspection-report.md"]
composes_with:
  - pattern: "After-Action Review"
    how: "After-Action Review extracts lessons from the iteration history that Cathedral Construction accumulates, turning execution record into doctrine."
  - pattern: "Back-Slopping (Learning Inheritance)"
    how: "Back-Slopping (Learning Inheritance) carries forward patterns and learnings from previous iterations; Cathedral Construction's inherit_workspace provides the substrate for this knowledge transfer."
  - pattern: "Memoization Cache"
    how: "Memoization Cache stores previously-built components to avoid rebuilding; Cathedral Construction's incremental additions benefit from cached artifacts across iterations."
---

## Cathedral Construction

`Status: Working` · **Source:** Medieval cathedral building. **Forces:** Convergence Imperative + Finite Resources.

### Core Dynamic

Long-running iterative refinement where each iteration adds structural elements. Different from Fixed-Point (which converges to stability). Cathedral Construction builds toward a known target through incremental addition.

### When to Use / When NOT to Use

Use for large artifacts that can't be produced in one pass. Not when the work is convergent (use Fixed-Point).

### Marianne Score Structure

```yaml
sheets:
  - name: plan-iteration
    prompt: "Read current state. Plan what to add this iteration."
    capture_files: ["cathedral/**"]
  - name: build
    prompt: "Execute the plan. Add to the cathedral."
  - name: inspect
    prompt: "Review what was built. Write inspection-report.md."
on_success:
  action: self
  inherit_workspace: true
  max_chain_depth: 20
```

### Failure Mode

Each iteration adds but never integrates. Include integration checks in the inspection stage.

### Composes With

After-Action Review, Back-Slopping (Learning Inheritance), Memoization Cache
