---
name: "Talmudic Page"
scale: score-level
type: orchestration-pattern
status: working
forces:
  - "Information Asymmetry"
generators:
  - "Accumulate Knowledge"
problem: "Multiple perspectives on an artifact produce disconnected analyses when commentaries reference only the source, not each other."
signals:
  - "primary artifact needs multi-layer annotation"
  - "analysis requires multiple perspectives anchored to one text"
  - "commentaries should reference both source and each other"
  - "single-perspective analysis is insufficient"
fan_out:
  commentary: 3
stages:
  - name: central-text
    sheets: 1
    instrument_guidance: "score-author's choice — needs reasoning capability to produce substantive core analysis that anchors all commentary"
    fallback_friendly: false
    purpose: "Write the core analysis that serves as the central reference text."
    artifacts: ["core-analysis.md"]
  - name: commentary
    sheets: "fan_out(3)"
    instrument_guidance: "score-author's choice — each instance provides a perspective on the central text; cheaper instruments acceptable if commentary task is straightforward"
    fallback_friendly: true
    purpose: "Read the core analysis and write commentary from a specific perspective."
    artifacts: ["commentary-1.md", "commentary-2.md", "commentary-3.md"]
  - name: interlink
    sheets: 1
    instrument_guidance: "score-author's choice — must track and cross-reference multiple sources (core + all commentaries); sonnet or opus recommended for synthesis work"
    fallback_friendly: false
    purpose: "Synthesize the core analysis and all commentaries, highlighting cross-references and inter-commentary connections."
    artifacts: ["synthesis.md"]
composes_with:
  - pattern: "Sugya Weave (Editorial Synthesis)"
    how: "Sugya Weave extends Talmudic Page's multi-layer commentary structure with editorial synthesis that extracts themes across all layers."
  - pattern: "Fan-out + Synthesis"
    how: "Talmudic Page is Fan-out + Synthesis with the constraint that all fan-out instances must reference a shared central text, creating hub-and-spoke commentary structure."
---

## Talmudic Page

`Status: Working` · **Source:** Talmudic commentary layout (Mishnah + Gemara + commentaries). **Forces:** Information Asymmetry.

### Core Dynamic

A central text surrounded by commentary layers at different levels of abstraction. The central text anchors all commentary; each layer responds to the text AND to other layers. Produces interlinked multi-perspective analysis without losing the central thread.

### When to Use / When NOT to Use

Use when a primary artifact needs multi-layer annotation. Not when commentaries are independent (use plain Fan-out).

### Marianne Score Structure

```yaml
sheets:
  - name: central-text
    prompt: "Write the core analysis."
  - name: commentary
    instances: 3
    prompt: "Read the core analysis. Write commentary from your perspective."
    capture_files: ["core-analysis.md"]
  - name: interlink
    prompt: "Read core + all commentaries. Write cross-referenced synthesis."
    capture_files: ["core-analysis.md", "commentary-*.md"]
```

### Failure Mode

Commentaries ignore each other and respond only to the central text. The interlink stage must reference cross-commentary connections.

### Composes With

Sugya Weave, Fan-out + Synthesis
