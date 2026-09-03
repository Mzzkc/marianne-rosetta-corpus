---
name: "Immune Cascade"
scale: instrument-strategy
type: orchestration-pattern
status: working
proof_score: "rosetta-proof-immune-cascade.yaml"
forces:
  - "Finite Resources"
  - "Exponential Defect Cost"
generators:
  - "Graduate & Filter"
problem: "Expensive instruments waste resources on broad scanning when cheap preliminary work could narrow scope first."
signals:
  - "broad scanning is expensive but most issues are benign"
  - "don't know which findings warrant expensive investigation"
  - "need to narrow findings before expensive deep analysis"
stages:
  - name: broad-sweep
    sheets: "fan_out(8)"
    instrument_guidance: "opencode — fast, cheap scanning across partitions; capability sufficient for breadth-first issue discovery"
    fallback_friendly: true
    purpose: "Parallelize broad scanning to identify findings efficiently at low cost."
    artifacts: ["sweep-{{ instance_id }}.md"]
  - name: triage-handoff
    sheets: 1
    instrument_guidance: "claude-code or codex-cli — score-author's choice — requires judgment to triage findings and prioritize targets; stronger instruments produce better targeting"
    fallback_friendly: false
    purpose: "Deduplicate broad findings and create prioritized targeting brief for expensive investigation."
    artifacts: ["targeting-brief.md"]
  - name: deep-investigation
    sheets: 1
    instrument_guidance: "claude-code — deep code analysis and remediation requiring full reasoning capability; critical for thorough investigation"
    fallback_friendly: false
    purpose: "Deep-dive on prioritized targets with thorough analysis and remediation design."
    artifacts: []
  - name: learning
    sheets: 1
    instrument_guidance: "claude-code or codex-cli — score-author's choice — documents methodology and learnings; can use cheaper instrument"
    fallback_friendly: true
    purpose: "Document methodology and learnings for future audit iterations."
    artifacts: ["doctrine.md"]
dependencies: {}
composes_with:
  - pattern: "Triage Gate"
    how: "The triage-handoff stage implements Triage Gate logic, filtering broad findings to identify investigation targets."
  - pattern: "After-Action Review"
    how: "After-Action Review processes Immune Cascade's findings and learning stage outputs to extract methodology improvements."
  - pattern: "Relay Zone"
    how: "Relay Zone compresses the high-volume broad-sweep outputs before triage-handoff, preventing context overflow when parallel scans produce results."
fan_out:
  broad-sweep: 8
config_features:
  - "fan_out"
  - "capture_files"
---

## Immune Cascade

`Status: Working` · **Source:** Immunology (innate/adaptive response). Absorbs Kill Chain F2T2EA. **Forces:** Finite Resources + Exponential Defect Cost.

### Core Dynamic

Escalating tiers: fast/cheap/broad first for intelligence, slow/expensive/precise targeting what tier 1 found, then learning persistence. Three structural moves: graduated response, intelligence forwarding, learning persistence. **Strict Sequential Variant (from Kill Chain):** When the problem is pure narrowing, collapse to a linear pipeline where `command_succeeds verifying count decreased` validates each gate.

### When to Use / When NOT to Use

Use when the problem requires broad search before targeted work and cheap scanning methods exist. Not when the problem is narrow enough for direct attack.

### Marianne Score Structure

```yaml
sheets:
  - name: broad-sweep
    instances: 8
    instrument: haiku
    prompt: "Scan {{ partition }} for issues. Write raw findings."
    validations:
      - type: file_exists
        path: "{{ workspace }}/sweep-{{ instance_id }}.md"
  - name: triage-handoff
    prompt: "Read all sweep files. Deduplicate. Prioritize. Write targeting-brief.md."
    capture_files: ["sweep-*.md"]
  - name: deep-investigation
    instrument: opus
    prompt: "Deep-dive on prioritized targets. Write remediation."
    capture_files: ["targeting-brief.md"]
  - name: learning
    prompt: "Write doctrine.md: what scanning missed, what triage misjudged, rules for next run."
    validations:
      - type: content_regex
        pattern: "RULE:\\s+.+"
```

### Failure Mode

The learning stage is useless if it doesn't write persistent, structured output. Specify the artifact: `doctrine.md` with `RULE:` entries that the next iteration's broad sweep reads via prelude.

### Composes With

Triage Gate (handoff IS triage), After-Action Review (coda), Relay Zone (relay between tiers)
