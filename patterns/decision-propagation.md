---
name: "Decision Propagation"
scale: within-stage
type: orchestration-pattern
status: working
forces:
  - "Information Asymmetry"
generators: []
problem: "Downstream agents contradict upstream decisions because constraints are buried in prose rather than structured, parseable briefs."
signals:
  - "early decisions have compounding effects on later stages"
  - "downstream agents unknowingly violate upstream constraints"
  - "decisions are buried in prose output rather than structured artifacts"
  - "agents cannot tell which upstream decisions are load-bearing"
fan_out:
  implement: 4
config_features:
  - "fan_out"
  - "capture_files"
stages:
  - name: decide
    sheets: 1
    instrument_guidance: "score-author's choice — needs strong reasoning to identify load-bearing decisions and write concrete constraint briefs; codex-cli (gpt-5.5) or claude-code recommended"
    fallback_friendly: false
    purpose: "Make the architecture decision and write a structured constraint-brief with decision, rationale, implications, and downstream constraints."
    artifacts: ["constraint-brief.yaml"]
  - name: implement
    sheets: "fan_out(4)"
    instrument_guidance: "claude-code or codex-cli — score-author's choice — must be capable enough for the implementation task; constraints are externalized in the brief so instrument follows them"
    fallback_friendly: true
    purpose: "Read the constraint brief, build one component per instance, and acknowledge which constraints were incorporated."
    artifacts: []
dependencies: {}
composes_with:
  - pattern: "CDCL Search"
    how: "When propagated decisions lead to failure, CDCL Search extracts the failure reason as a learned clause that prevents the same bad decision propagation in future iterations."
  - pattern: "CEGAR Loop"
    how: "CEGAR Loop's refinement iterations generate decisions at progressively finer abstraction levels; Decision Propagation structures each level's decisions for downstream consumption."
  - pattern: "Commander's Intent Envelope"
    how: "Commander's Intent Envelope defines the decision space boundaries (constraints and freedoms) within which Decision Propagation's structured briefs specify concrete downstream constraints."
---
## Decision Propagation

`Status: Working` · **Source:** Constraint satisfaction (renamed from Arc Consistency Propagation). **Forces:** Information Asymmetry.

### Core Dynamic

When a sheet makes a decision that constrains downstream sheets, it writes a structured constraint brief rather than embedding the decision in prose. The brief has: decision, rationale, implications, and constraints-for-downstream. Each downstream sheet reads the brief and acknowledges which constraints it incorporated. Writing the brief requires judgment — the agent must identify which decisions are load-bearing.

### When to Use / When NOT to Use

Use when decisions in early stages have compounding effects. Not when stages are independent or constraints are simple enough for the prompt alone.

### Marianne Score Structure

```yaml
sheets:
  - name: decide
    prompt: >
      Make the architecture decision. Write constraint-brief.yaml:
      {decision, rationale, implications: [], constraints_for_downstream: []}.
    validations:
      - type: command_succeeds
        command: "python3 -c \"import yaml; b=yaml.safe_load(open('{{ workspace }}/constraint-brief.yaml')); assert 'constraints_for_downstream' in b\""
  - name: implement
    instances: 4
    prompt: "Read constraint-brief.yaml. Build component {{ instance_id }}. Acknowledge constraints."
    capture_files: ["constraint-brief.yaml"]
```

### Failure Mode

Constraint briefs too abstract to constrain. The brief should name specific artifacts and interfaces, not just abstract goals. Validate with `command_succeeds` checking brief has concrete entries.

### Composes With

CDCL Search, CEGAR Loop, Commander's Intent Envelope
