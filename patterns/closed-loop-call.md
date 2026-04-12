---
name: "Closed-Loop Call"
scale: score-level
type: orchestration-pattern
status: working
forces:
  - "Producer-Consumer Mismatch"
  - "Partial Failure"
generators:
  - "Contract at Interfaces"
  - "Exploit Failure as Signal"
problem: "Semantic drift across pipeline stages when consumers misunderstand producer outputs."
signals:
  - "handoff fidelity is critical"
  - "semantic drift is a real risk"
  - "stages have non-obvious dependencies"
  - "previous stage outputs are ambiguous"
stages:
  - name: produce
    sheets: 1
    instrument_guidance: "score-author's choice — any instrument capable of writing structured output with key decisions listed"
    fallback_friendly: true
    purpose: "Write output with a manifest listing key decisions."
    artifacts: ["manifest.yaml"]
  - name: consume
    sheets: 1
    instrument_guidance: "score-author's choice — instrument must be capable of reading and comprehending the produce output"
    fallback_friendly: true
    purpose: "Read output and write a readback confirming comprehension of each decision."
    artifacts: ["readback.yaml"]
  - name: verify
    sheets: 1
    instrument_guidance: "cli — Python validation script comparing manifest.yaml and readback.yaml for structural alignment"
    fallback_friendly: false
    purpose: "Validate that the readback matches the manifest structure, catching semantic drift."
    artifacts: []
composes_with:
  - pattern: "Prefabrication"
    how: "Prefabrication defines strict output contracts that Closed-Loop Call verifies are correctly understood."
  - pattern: "Relay Zone"
    how: "Relay Zone compresses accumulated outputs between stages; Closed-Loop Call verifies the compressed handoff preserved semantic meaning."
  - pattern: "Succession Pipeline"
    how: "Succession Pipeline chains execution stages; Closed-Loop Call ensures each handoff maintains semantic fidelity."
---

## Closed-Loop Call

`Status: Working` · **Source:** Aviation CRM callout-response protocol. **Forces:** Producer-Consumer Mismatch + Partial Failure.

### Core Dynamic

Explicit handoff verification between stages. Stage A produces output. Stage B reads it and writes back a confirmation of what it understood. A CLI validation compares the two. Prevents semantic drift across pipeline stages.

### When to Use / When NOT to Use

Use when handoff fidelity is critical and semantic drift is a real risk. Not when stages are trivially compatible.

### Marianne Score Structure

```yaml
sheets:
  - name: produce
    prompt: "Write output with manifest.yaml listing key decisions."
  - name: consume
    prompt: "Read output. Write readback.yaml confirming your understanding of each decision."
    capture_files: ["manifest.yaml", "output/**"]
  - name: verify
    instrument: cli
    validations:
      - type: command_succeeds
        command: "python3 -c \"import yaml; m=yaml.safe_load(open('{{ workspace }}/manifest.yaml')); r=yaml.safe_load(open('{{ workspace }}/readback.yaml')); assert set(m.keys())==set(r.keys()), f'Key mismatch: {set(m.keys())-set(r.keys())}'\""
```

### Failure Mode

Readback is verbatim copy, not comprehension check. The validation should check structural understanding, not string matching.

### Composes With

Relay Zone, Prefabrication, Succession Pipeline
