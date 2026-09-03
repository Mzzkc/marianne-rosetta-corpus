---
name: "Source Triangulation"
scale: score-level
type: orchestration-pattern
status: working
proof_score: "source-triangulation.yaml"
forces:
  - "Information Asymmetry"
  - "Structured Disagreement"
generators:
  - "Verify through Diverse Observers"
  - "Frame Multiplication"
problem: "Single-source analysis cannot detect contradictions between what code does, documentation says, and tests prove."
signals:
  - "technical claims need independent verification"
  - "multiple source types exist (code, docs, tests, benchmarks)"
  - "single perspective might miss contradictions"
  - "need to categorize claims as corroborated vs uncorroborated"
stages:
  - name: extract
    sheets: 1
    instrument_guidance: "opencode or similar cheap instrument — claim extraction is straightforward identification work, doesn't require deep reasoning"
    fallback_friendly: true
    purpose: "Extract and structure claims that need verification, defining verification criteria for each."
    artifacts: ["01-claims.md"]
  - name: investigate
    sheets: "fan_out(3)"
    instrument_guidance: "codex-cli (gpt-5.5) or similar mid-tier instrument — each voice needs code/doc/test reading and analysis capability to find supporting or contradicting evidence"
    fallback_friendly: false
    purpose: "Analyze from assigned source (code/docs/tests) to find evidence supporting or contradicting each claim."
    artifacts: ["02-code-findings.md", "02-docs-findings.md", "02-test-findings.md"]
  - name: triangulate
    sheets: 1
    instrument_guidance: "claude-code or codex-cli (gpt-5.5) — deep cross-referencing synthesis requires strong reasoning to categorize claims across all source evidence"
    fallback_friendly: false
    purpose: "Cross-reference all investigation results to categorize each claim as CORROBORATED, UNCORROBORATED, or CONTRADICTED."
    artifacts: ["03-triangulation.md"]
dependencies:
  investigate: [extract]
  triangulate: [investigate]
fan_out:
  investigate: 3
composes_with:
  - pattern: "Rashomon Gate"
    how: "Rashomon Gate applies different analytical frames to the same evidence; Source Triangulation divides the evidence itself across structurally different source types."
  - pattern: "Triage Gate"
    how: "Triage Gate filters incoming claims before Source Triangulation's multi-source investigation, preventing waste on obviously true or false claims."
  - pattern: "Sugya Weave (Editorial Synthesis)"
    how: "Source Triangulation's three investigation voices (code, docs, tests) feed into Sugya Weave (Editorial Synthesis)'s dialectical synthesis when claims require interpretive layering beyond fact-checking."
---

## Source Triangulation

`Status: Working` · **Source:** Journalism, intelligence analysis. **Forces:** Information Asymmetry.

### Core Dynamic

Multiple agents analyze the SAME problem from DIFFERENT sources. The synthesis identifies: corroborated (multiple sources agree), uncorroborated (single source), and contradicted (sources disagree). Different from Rashomon Gate (which uses different frames on same evidence). Source Triangulation divides the evidence itself.

### When to Use / When NOT to Use

Use when claims need independent verification and multiple source types exist. Not when a single authoritative source suffices.

### Marianne Score Structure

```yaml
sheets:
  - name: investigate
    instances: 3
    cadenza:
      - "source-code.md"
      - "source-docs.md"
      - "source-tests.md"
    prompt: "Analyze from your assigned source. Write findings-{{ instance_id }}.md."
    validations:
      - type: file_exists
        path: "{{ workspace }}/findings-{{ instance_id }}.md"
  - name: triangulate
    prompt: >
      Read all findings. Categorize each claim: CORROBORATED (2+ sources),
      UNCORROBORATED (1 source), CONTRADICTED (sources disagree).
    capture_files: ["findings-*.md"]
```

### Failure Mode

Sources too similar produce trivially corroborated results. Ensure sources are structurally independent.

### Composes With

Rashomon Gate, Triage Gate, Sugya Weave (Editorial Synthesis)
