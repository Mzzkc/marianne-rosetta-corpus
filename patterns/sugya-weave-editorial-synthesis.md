---
name: "Sugya Weave (Editorial Synthesis)"
scale: within-stage
type: orchestration-pattern
status: working
forces:
  - "Information Asymmetry"
  - "Convergence Imperative"
generators: []
problem: "Diverse inputs need synthesis into an authoritative position with argued support, not neutral aggregation."
signals:
  - "multiple perspectives exist but need editorial judgment"
  - "summary isn't sufficient — need a supported position"
  - "inputs are diverse and require interpretation"
  - "neutrality would hide necessary judgment calls"
stages:
  - name: weave
    sheets: 1
    instrument_guidance: "score-author's choice — needs strong reasoning for position-taking and argument construction; codex-cli (gpt-5.5) or claude-code recommended for editorial depth"
    fallback_friendly: false
    purpose: "Read diverse inputs, take an argued position, and produce editorial synthesis with supporting evidence and acknowledged counterarguments."
    artifacts: ["editorial-synthesis.md"]
dependencies: {}
composes_with:
  - pattern: "Fan-out + Synthesis"
    how: "Fan-out produces diverse inputs; Sugya Weave synthesizes them with an editorial position rather than neutral aggregation."
  - pattern: "Source Triangulation"
    how: "Source Triangulation provides multiple perspectives; Sugya Weave adjudicates between them with an argued position on which is most credible."
  - pattern: "Rashomon Gate"
    how: "Rashomon Gate produces multiple interpretations; Sugya Weave takes a supported position on which interpretation best fits the evidence."
---

## Sugya Weave (Editorial Synthesis)

`Status: Working` · **Source:** Talmudic sugya structure. **Forces:** Information Asymmetry + Convergence Imperative.

### Core Dynamic

Not just synthesis — editorial synthesis. The weaver takes a POSITION on the inputs, arguing for one interpretation while acknowledging alternatives. Produces an opinionated conclusion, not a summary. Requires structured validation that the position is supported.

### When to Use / When NOT to Use

Use when diverse inputs need an authoritative position, not just aggregation. Not when neutrality is required.

### Marianne Score Structure

```yaml
sheets:
  - name: weave
    prompt: >
      Read all inputs. Take a position. Write editorial-synthesis.md with:
      POSITION, SUPPORTING EVIDENCE, COUNTERARGUMENTS, CONCLUSION.
    capture_files: ["input-*.md"]
    validations:
      - type: content_contains
        content: "POSITION:"
      - type: content_contains
        content: "COUNTERARGUMENTS:"
```

### Failure Mode

Position is unsupported assertion. Validate that supporting evidence references specific inputs.

### Composes With

Fan-out + Synthesis, Source Triangulation, Rashomon Gate
