---
name: "Prefabrication"
scale: score-level
type: orchestration-pattern
status: working
proof_score: "prefabrication.yaml"
forces:
  - "Producer-Consumer Mismatch"
  - "Finite Resources"
generators:
  - "Contract at Interfaces"
problem: "Parallel tracks produce incompatible outputs because no shared interface contract exists before work begins."
signals:
  - "parallel work must produce compatible outputs"
  - "integration fails due to interface mismatches"
  - "tracks can't communicate during development"
  - "neither track depends on the other's code"
fan_out:
  build: 4
stages:
  - name: interface-spec
    sheets: 1
    instrument_guidance: "score-author's choice — needs strong reasoning to write a precise, unambiguous interface contract; contract quality determines integration success. Proof score uses contract-designer (claude-code with extended timeout)."
    fallback_friendly: false
    purpose: "Define the shared interface contract before parallel work begins. Contract must be precise enough to prevent incompatible implementations but not so restrictive it eliminates parallelization benefits."
    artifacts: ["interface-spec.yaml"]
  - name: build
    sheets: "fan_out(4)"
    instrument_guidance: "score-author's choice — capability depends on what's being built (code generation, document creation, etc.); proof score uses code-builder (claude-code). Each instance builds independently against the contract."
    fallback_friendly: true
    purpose: "Build components in parallel according to the interface contract. Each track works independently without seeing other tracks' code."
    artifacts: ["component-*/**"]
  - name: integrate
    sheets: 1
    instrument_guidance: "score-author's choice — verification and assembly work; does not need highest capability if contract is solid. Proof score uses verifier (claude-code)."
    fallback_friendly: true
    purpose: "Assemble all pre-validated components and verify all interfaces match the contract. Integration is mechanical if the contract is precise."
    artifacts: []
dependencies: {}
composes_with:
  - pattern: "The Attested Merge Gate"
    how: "The Attested Merge Gate supersedes Prefabrication when integration crosses a trust boundary: it retains the frozen interface contract but adds producer attestations, a deterministic byte sweep, and one serialized merge authority."
  - pattern: "Barn Raising"
    how: "Barn Raising establishes shared conventions before Prefabrication's parallel tracks begin, providing the foundation that the interface contract builds upon."
  - pattern: "Clash Detection"
    how: "Clash Detection verifies no conflicts exist between assembled components after Prefabrication's integration stage completes."
  - pattern: "Mission Command"
    how: "Both patterns coordinate independent parallel work through shared intent artifacts — Prefabrication uses an interface contract, Mission Command uses a mission brief with intent envelope."
---

## Prefabrication

`Status: Working` · **Source:** Construction industry (offsite fabrication). **Forces:** Producer-Consumer Mismatch + Finite Resources.

### Core Dynamic

Define interface contracts before parallel work begins. Each parallel track gets a shared interface definition and builds to it. Integration only assembles pre-validated pieces. Different from Fan-out + Synthesis: prefabrication has an explicit interface specification stage before fan-out.

### When to Use / When NOT to Use

Use when parallel tracks must produce compatible outputs. Not when outputs are independent (use plain Fan-out) or when the interface can't be defined upfront.

### Marianne Score Structure

```yaml
sheets:
  - name: interface-spec
    prompt: "Define the shared API contract. Write interface-spec.yaml."
    validations:
      - type: file_exists
        path: "{{ workspace }}/interface-spec.yaml"
  - name: build
    instances: 4
    prompt: "Build component {{ instance_id }} according to interface-spec.yaml."
    capture_files: ["interface-spec.yaml"]
  - name: integrate
    prompt: "Assemble all components. Verify all interfaces match."
    capture_files: ["component-*/**"]
```

### Failure Mode

Interface spec too loose allows incompatible implementations. Too tight eliminates the benefits of parallel work.

### Review Integration

Iteration 5.1 narrows this pattern's authority. Prefabrication remains sufficient when the parallel producers and merger share one trust domain and ordinary contract validation is enough. It is obsolete as guidance for untrusted or independently failing producers: use The Attested Merge Gate, which preserves the interface freeze while requiring attestations, a deterministic sweep over actual bytes, and one serialized merge authority. Job-level worktree isolation must not be described as per-sheet isolation; parallel voices instead write to instance-tagged namespaces for later integration.

### Composes With

The Attested Merge Gate, Barn Raising, Clash Detection, Mission Command
