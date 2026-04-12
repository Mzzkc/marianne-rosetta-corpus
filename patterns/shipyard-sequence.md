---
name: "Shipyard Sequence"
scale: score-level
type: orchestration-pattern
status: working
proof_score: "shipyard-sequence.yaml"
forces:
  - "Exponential Defect Cost"
  - "Finite Resources"
generators:
  - "Graduate & Filter"
  - "Gate on Environmental Readiness"
problem: "Expensive fan-out proceeds on a broken foundation, wasting resources on downstream work that will fail."
signals:
  - "downstream fan-out is expensive"
  - "foundation must be solid before scaling work"
  - "need real validation tools, not LLM judgment"
  - "costs multiply when defects reach later stages"
fan_out:
  outfitting: 4
stages:
  - name: construct-schema
    sheets: 1
    instrument_guidance: "score-author's choice — needs code generation for schema/migrations; sonnet or opus for complex domains, haiku for simple schemas"
    fallback_friendly: true
    purpose: "Generate the database schema and migration files."
    artifacts: ["schema.sql"]
  - name: launch-gate
    sheets: 1
    instrument_guidance: "any instrument with command execution — validation is deterministic tool-based (command_succeeds), not LLM judgment; even haiku suffices"
    fallback_friendly: true
    purpose: "Validate the schema using real tools (migrate --check, test suite) before expensive fan-out."
    artifacts: []
  - name: outfitting
    sheets: "fan_out(4)"
    instrument_guidance: "score-author's choice — builds services/modules on validated foundation; capability depends on service complexity"
    fallback_friendly: true
    purpose: "Build services or modules in parallel against the validated schema."
    artifacts: []
composes_with:
  - pattern: "Succession Pipeline"
    how: "Succession Pipeline graduates candidates through quality tiers; Shipyard Sequence validates foundation quality before expensive fan-out investment."
  - pattern: "Dormancy Gate"
    how: "Dormancy Gate waits for external environmental conditions; Shipyard Sequence gates on foundation validation readiness before proceeding."
  - pattern: "Triage Gate"
    how: "Triage Gate filters work items before processing; Shipyard Sequence validates foundation before expensive downstream fan-out."
dependencies:
  launch-gate: [construct-schema]
  outfitting: [launch-gate]
config_features:
  - "fan_out"
  - "command_succeeds"
---

## Shipyard Sequence

`Status: Working` · **Source:** Shipbuilding hull block method. **Forces:** Exponential Defect Cost + Finite Resources.

### Core Dynamic

Validate foundational work under realistic conditions before investing in expensive fan-out. The launch gate uses `command_succeeds` exclusively — real execution, not LLM judgment. Construction has 1-3 stages; outfitting fans out only after launch passes.

### When to Use / When NOT to Use

Use when downstream fan-out is expensive, foundation must be solid, and real validation tools exist. Not when work is naturally parallel from the start.

### Marianne Score Structure

```yaml
sheets:
  - name: construct-schema
    prompt: "Generate the database schema and migration files."
  - name: launch-gate
    validations:
      - type: command_succeeds
        command: "cd {{ workspace }} && python manage.py migrate --check"
      - type: command_succeeds
        command: "cd {{ workspace }} && python manage.py test db_schema --verbosity=0"
  - name: outfitting
    instances: 4
    prompt: "Build {{ service_name }} against the validated schema."
    capture_files: ["schema.sql"]
```

### Failure Mode

If launch validation is too lenient, expensive fan-out proceeds on a broken foundation. The gate must use `command_succeeds`, never `content_contains`.

### Composes With

Succession Pipeline, Dormancy Gate, Triage Gate
