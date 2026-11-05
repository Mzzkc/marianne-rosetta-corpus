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

### Discover Pass 1, Cycle 7 — Prevention by Desk Design (Wordless Manual Fold)

This pass dissolved the draft's **Wordless Manual** (Review 2: "a bundle of three techniques — least-context manifests, output scaffolds, negative examples — not one state machine"; Review 1: compile-time `spec_tags` cannot be authored by a runtime sheet). The techniques distribute to their real owners: output scaffolds → Readback Before Commit and The Attested Merge Gate; negative examples refreshed from failure receipts → Dead Letter Quarantine's curriculum fold (the curriculum teaches the sheet; the crossed-out examples teach the desk — same `failure_history` substrate). What lands *here* is the ex-ante discipline — recorded because Review 3 dissented: "the only pattern in the draft that reduces error ex ante rather than policing it ex post."

**The worker packet as the contract's worker face.** Prefabrication's interface contract, instantiated per worker, is: (a) a **manifest** — the exact input files this instance needs, checked by hash, nothing else in view; (b) a **fixture** whose shape admits only the intended output (schema, strict scaffold); (c) **negative examples** — two or three crossed-out artifacts showing the characteristic wrong answers, drawn from real prior failures and refreshed by loop iteration, never boilerplate (a crossed-out drawing of a failure nobody makes anymore wastes attention while the *new* failure ships uncrossed).

The IKEA discipline this encodes: design the *parts and the page* so the wrong assembly is hard to attempt — the Allen key fits one way; each step shows exactly its stage's components; impossible configurations are preemptively crossed out. Every gate pattern polices error *after* the attempt; the worker packet removes the attempt. Wire it honestly: stage 1 emits packets into `workspace/workers/{id}/packet.json` (a runtime artifact), and stage 2 sheets bind to those paths — never to compile-time context filters.

```yaml
  - name: manual-press
    prompt: "Author the worker packet: manifest with sha256 per input, output scaffold, 2-3 crossed-out negative examples sourced from the previous iteration's failure receipts. Write workers/{{ instance_id }}/packet.json."
  - name: assembly
    capture_files: ["workers/{{ instance_id }}/packet.json"]
    prompt: "Work ONLY from your packet manifest. Write into your scaffold exactly."
```

Failure mode: the packet goes stale — negative examples rot exactly as suppressions do. The refresh loop is not optional; a QC sweep that has never caught a seeded bad scaffold is a receipt.
