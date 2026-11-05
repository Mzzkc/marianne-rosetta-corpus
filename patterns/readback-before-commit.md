---
name: "Readback Before Commit"
scale: communication
type: orchestration-pattern
status: working
iteration_added: "discover pass 1, cycle 7"
forces:
  - "Information Asymmetry"
  - "Exponential Defect Cost"
generators:
  - "Contract at Interfaces"
problem: "A sender cannot observe whether a receiver understood an instruction, so misreads surface at commit time when they cost the whole downstream subtree."
signals:
  - "every fan-in that consumes AI output"
  - "cross-stage contracts where the producer reasons and the consumer executes"
  - "fan-outs with differentiated instructions where each instance must understand ITS lens"
  - "handoffs between instrument types (reasoner → CLI → reasoner)"
stages:
  - name: instructor
    sheets: 1
    instrument_guidance: "score-author's choice — emits the task spec as a structured file with declared fields"
    fallback_friendly: true
    purpose: "Write spec.json: operation, target, constraints as typed fields."
    artifacts: ["spec.json"]
  - name: echo
    sheets: 1
    instrument_guidance: "the receiver instrument — emits ONLY the echo artifact, no work yet"
    fallback_friendly: true
    purpose: "Restate spec fields in normalized form under response_format: json_schema."
    artifacts: ["echo.json"]
  - name: echo-gate
    sheets: 1
    instrument_guidance: "instrument: cli — pure field comparison; instrument_fallbacks: []"
    fallback_friendly: false
    purpose: "Diff echo against spec field-by-field; exit code IS the hearback."
    artifacts: []
  - name: execute
    sheets: 1
    instrument_guidance: "the receiver instrument — main work, unlocked only by the gate"
    fallback_friendly: true
    purpose: "Do the actual task, having demonstrably understood it."
    artifacts: []
dependencies:
  echo: ["instructor"]
  echo-gate: ["echo"]
  execute: ["echo-gate"]
composes_with:
  - pattern: "Fan-out + Synthesis"
    how: "the echo schema is the fan-in contract; N receivers each close their own loop before subtrees unlock"
  - pattern: "The Poisoned-Artifact Advisory"
    how: "the echo is prevention; the advisory is containment after the fact"
  - pattern: "Closed-Loop Call"
    how: "Closed-Loop Call checks semantic drift across stages by re-reading outputs; this checks understanding of inputs before work begins"
config_features:
  - "response_format (native, UNPROVEN in any proof score — probe instrument support first)"
  - "fan_out"
  - "instrument: cli"
---

## Readback Before Commit

`Status: Working` · **Source:** discover pass 1, cycle 7 — Expeditions 1+3+6 (ATC readback/hearback per ICAO; Talmud/peer-review), triple collision, the hardest merge of the pass. **Forces:** Information Asymmetry + Exponential Defect Cost.

### Core Dynamic

A one-way transmission is not an instruction; it is a hope. Only a **typed echo from the receiver, checked by the sender, converts "I said it" into "we agree."** The echo is typed, not prose ("roger closes nothing"); the verification is deterministic, never an AI nod; the echo is selective — load-bearing fields only, as ATC reads back altitude, not weather; the economics are Exponential Defect Cost — a mismatch at echo-time costs one round trip, at commit-time the whole subtree.

The echo schema is restricted to **normalized, machine-checkable fields**: action enums, exact target resource identifiers, integer/string bounds echoed exactly. Paraphrase lives only in an optional `understanding` prose field that no gate diffs — schema conformance is necessary, never sufficient; compose with content-bearing gates, never replace them. The graph is four nodes: an echo-only receiver cannot also be the executor inside one atomic sheet.

### Marianne Score Structure

```yaml
sheets:
  - name: instructor
    prompt: "Read the task. Write spec.json with fields: operation (enum), target (exact path/id), constraints (string)."
    validations:
      - type: file_exists
        path: "spec.json"
  - name: echo
    capture_files: ["spec.json"]
    prompt: "FIRST ACT ONLY: restate spec.json as echo.json with the SAME operation enum, the SAME target string, and constraints copied field-wise. Emit nothing else."
    response_format: { type: json_schema, schema: { type: object, required: [operation, target, constraints] } }
    validations:
      - type: file_exists
        path: "echo.json"
  - name: echo-gate
    instrument: cli
    instrument_fallbacks: []
    command: "jq -e --argfile a spec.json --argfile b echo.json '$a.operation==$b.operation and $a.target==$b.target'"
    validations:
      - type: command_succeeds
    on_fail: { action: retry, max_retries: 2 }   # bounded correction loop
  - name: execute
    capture_files: ["spec.json", "echo.json"]
    prompt: "Execute the task exactly as specified in spec.json."
```

**Negative control:** seed the echo sheet's context with a subtle misreading (spec says `staging_users_v2`, a planted note says `staging_users`); the gate must exit non-zero. **Sentinel:** a variant with the echo-gate removed; a final CLI validator greps the executor's output for the wrong-table string and fails — proving the misread reaches the main stage when the gate is absent. Both directions must fail for the proof to count.

**Instrument note:** `response_format: json_schema` support varies by instrument and has zero proof-score exercise — probe it on your panel before relying on the echo gate (first in this pass's proof order).

### When to Use

Every fan-in; every gate consuming AI output; cross-stage contracts; differentiated fan-outs; instrument-type handoffs.

### When NOT to Use

Human-readable deliverables nobody machine-reads; instructions trivial enough that the readback outprices the misread (don't readback `mkdir`); sheets whose output no gate consumes.

### Composes With

Fan-out + Synthesis (schema as fan-in contract), The Poisoned-Artifact Advisory (prevention vs. containment), Closed-Loop Call (input understanding vs. output drift)
