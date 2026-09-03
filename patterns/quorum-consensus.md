---
name: "Quorum Consensus"
scale: "score-level"
type: "orchestration-pattern"
status: "working"
forces:
  - "Partial Failure"
  - "Finite Resources"
generators:
  - "Threshold-Triggered Switch"
problem: "Partial agent failure should not block the pipeline when majority agreement is sufficient."
signals:
  - "fan-out agents may fail unpredictably"
  - "partial failure shouldn't block downstream stages"
  - "need to proceed with majority agreement"
  - "some agents' failures are acceptable if quorum reached"
fan_out:
  analyze: 5
stages:
  - name: analyze
    sheets: "fan_out(5)"
    instrument_guidance: "claude-code or codex-cli — score-author's choice — any instrument capable of analyzing the artifact; quorum is based on count, not quality"
    fallback_friendly: true
    purpose: "Execute analysis in parallel across 5 agents, each producing a workspace file."
    artifacts: ["analysis-*.md"]
  - name: quorum-check
    sheets: 1
    instrument_guidance: "claude-code or codex-cli — cli instrument — executes validation command to verify that at least 3 analyses were produced"
    fallback_friendly: false
    purpose: "Verify that at least 3 of 5 agents produced valid outputs."
    artifacts: []
  - name: synthesize
    sheets: 1
    instrument_guidance: "claude-code or codex-cli — score-author's choice — instrument should be capable of reading multiple analyses and synthesizing consensus; stronger instruments produce higher-quality synthesis"
    fallback_friendly: true
    purpose: "Synthesize consensus from successful analyses, noting which agents' outputs were missing."
    artifacts: []
dependencies: {}
composes_with:
  - pattern: "Triage Gate"
    how: "Triage Gate pre-filters candidates before Quorum Consensus's fan-out, reducing unnecessary agent invocations."
  - pattern: "Source Triangulation"
    how: "Source Triangulation enforces diversity across fan-out agents, preventing systematic bias that would corrupt the quorum validity."
  - pattern: "Fan-out + Synthesis"
    how: "Quorum Consensus is a specific implementation of Fan-out + Synthesis that adds a quorum check to handle partial failure, synthesizing results only from the successful majority."
---

## Quorum Consensus

`Status: Working` · **Source:** Distributed systems quorum. **Forces:** Partial Failure + Finite Resources.

### Core Dynamic

Accept results when a quorum (majority) of fan-out agents agree, even if some fail. N agents run; the synthesis stage proceeds when M of N produce valid output. The remaining agents' failures are logged but don't block the pipeline.

### When to Use / When NOT to Use

Use when fan-out may have partial failure and majority agreement is sufficient. Not when every agent's output is critical.

### Marianne Score Structure

```yaml
sheets:
  - name: analyze
    instances: 5
    prompt: "Analyze the artifact. Write analysis-{{ instance_id }}.md."
  - name: quorum-check
    instrument: cli
    validations:
      - type: command_succeeds
        command: "test $(ls {{ workspace }}/analysis-*.md 2>/dev/null | wc -l) -ge 3"
  - name: synthesize
    prompt: "Read available analyses. Note which are missing. Synthesize from quorum."
    capture_files: ["analysis-*.md"]
```

### Failure Mode

Quorum reached but the surviving agents all made the same error. Use Source Triangulation to ensure diversity.

### Composes With

Triage Gate, Source Triangulation, Fan-out + Synthesis
