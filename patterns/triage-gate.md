---
name: "Triage Gate"
scale: score-level
type: orchestration-pattern
status: working
forces:
  - "Finite Resources"
  - "Partial Failure"
generators:
  - "Exploit Failure as Signal"
problem: "Fan-out produces mixed-quality outputs but synthesis processes all outputs regardless of quality, wasting resources."
signals:
  - "fan-out produces wildly varying output quality"
  - "synthesis stage is expensive and shouldn't process garbage"
  - "some outputs need rework, others are ready"
  - "structural quality checks are definable"
config_features:
  - "capture_files"
stages:
  - name: triage
    sheets: 1
    instrument_guidance: "opencode recommended — classification task dominated by structural checks (schema, sections, word count); semantic assessment is secondary and doesn't require strong reasoning"
    fallback_friendly: true
    purpose: "Classify each fan-out output as RED (forward to synthesis), YELLOW (rework with targeted prompt), GREEN (supplementary), or BLACK (discard with logged reason)."
    artifacts: ["triage-manifest.yaml"]
dependencies: {}
composes_with:
  - pattern: "Immune Cascade"
    how: "Triage Gate provides coarse filtering that precedes Immune Cascade's graduated verification stages."
  - pattern: "Fan-out + Synthesis"
    how: "Triage Gate filters fan-out outputs before synthesis, preventing synthesis from processing low-quality or unusable outputs."
  - pattern: "Relay Zone"
    how: "Triage Gate classifies fan-out outputs by quality; Relay Zone compresses the classified results to prevent context overflow in downstream processing stages."
---

## Triage Gate

`Status: Working` · **Source:** Emergency medicine START protocol, military command. **Forces:** Finite Resources + Partial Failure.

### Core Dynamic

Coarse classification before expensive processing. A fast classifier reads fan-out outputs and routes: **RED** (forward to synthesis), **YELLOW** (rework with targeted prompt), **GREEN** (supplementary), **BLACK** (discard with logged reason). Structural checks first (schema compliance, required sections, word count), then semantic if needed. This is the convergence ranked #1 across all domains.

### When to Use / When NOT to Use

Use when fan-out produces mixed quality, downstream processing is expensive, and structural quality checks are definable. Not when all outputs must be incorporated or fan-out is narrow (2-3 agents).

### Marianne Score Structure

```yaml
sheets:
  - name: triage
    prompt: >
      Read each output in fan-out-results/. For each, write a line in triage-manifest.yaml:
      {id, category: RED|YELLOW|GREEN|BLACK, reason, rework_prompt}.
      Use structural checks first: required sections present, word count > 200.
    capture_files: ["fan-out-results/*.md"]
    validations:
      - type: command_succeeds
        command: "python3 -c \"import yaml; m=yaml.safe_load(open('{{ workspace }}/triage-manifest.yaml')); assert all(e['category'] in ['RED','YELLOW','GREEN','BLACK'] for e in m)\""
```

### Failure Mode

If YELLOW count is 0, the rework stage still executes but produces nothing — guard with a Read-and-React conditional. If everything is BLACK, synthesis gets no inputs; the score should fail explicitly.

### Composes With

Immune Cascade, Fan-out + Synthesis, Relay Zone
