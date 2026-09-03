---
name: "Relay Zone"
scale: score-level
type: orchestration-pattern
status: working
forces:
  - "Producer-Consumer Mismatch"
  - "Information Asymmetry"
generators: []
problem: "Cumulative outputs across pipeline stages exceed context window limits, degrading downstream agent performance."
signals:
  - "pipeline outputs growing too large for downstream context windows"
  - "later stages receiving more context than they can effectively use"
  - "information from early stages drowning out recent findings"
  - "need to preserve key findings while discarding volume"
stages:
  - name: relay
    sheets: 1
    instrument_guidance: "score-author's choice — needs strong enough comprehension to identify key findings and compress without losing critical information; codex-cli (gpt-5.5) recommended for cost-effective compression"
    fallback_friendly: true
    purpose: "Read all prior stage outputs and compress to a relay brief preserving key findings, open questions, and critical data at ~20% of original size."
    artifacts: ["relay-brief.md"]
dependencies: {}
composes_with:
  - pattern: "Fan-out + Synthesis"
    how: "Relay Zone compresses fan-out outputs before synthesis, preventing context window overflow when many parallel streams merge."
  - pattern: "Forward Observer"
    how: "Forward Observer summarizes large input for a single expensive stage; Relay Zone compresses accumulated outputs between any pipeline stages."
  - pattern: "Screening Cascade"
    how: "Relay Zone compresses accumulated results between screening stages, preventing context bloat as items escalate through the cascade."
---
## Relay Zone

`Status: Working` · **Source:** Track relay (athletics). **Forces:** Producer-Consumer Mismatch.

### Core Dynamic

Context compression between pipeline stages. A dedicated relay sheet reads the full output of the previous stage and produces a compressed summary for the next stage. Prevents context window bloat across long pipelines.

### When to Use / When NOT to Use

Use when cumulative outputs exceed context limits. Not when all information must survive compression.

### Marianne Score Structure

```yaml
sheets:
  - name: relay
    prompt: >
      Read all prior outputs. Compress to relay-brief.md:
      key findings, open questions, critical data only. Target 20% of original size.
    capture_files: ["full-output/**"]
    validations:
      - type: file_exists
        path: "{{ workspace }}/relay-brief.md"
      - type: command_succeeds
        command: "test $(wc -w < '{{ workspace }}/relay-brief.md') -lt 2000"
```

### Failure Mode

Relay loses critical information. Downstream stages produce incorrect results because the relay omitted a key finding. Validate relay completeness by checking key terms survive compression.

### Composes With

Fan-out + Synthesis, Forward Observer, Screening Cascade
