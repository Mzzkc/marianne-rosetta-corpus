---
name: "The Non-Waiting Hand"
scale: concert-level
type: orchestration-pattern
status: working
iteration_added: "discover pass 1, cycle 7"
forces:
  - "Partial Failure"
  - "Information Asymmetry"
generators:
  - "Contract at Interfaces"
problem: "A parent that waits on N sequential children lives N lifetimes, and its cadence — the thing downstream consumers depend on — breaks; but spawning without a contract is fire-and-forget."
signals:
  - "continuous producers with derivative work: monitoring spawning investigations, digests spawning deep-dives, builds spawning releases"
  - "the parent's rhythm is the product and children are consequences"
stages:
  - name: spawn
    sheets: 1
    instrument_guidance: "instrument: cli — appends the ledger row THEN carries the concert trigger; single writer (the parent is the only appender)"
    fallback_friendly: false
    purpose: "Append spawn-ledger.jsonl {child_id, score, ts, lease_until, trigger_digest}; submit child via concert trigger, CONTINUE."
    artifacts: ["spawn-ledger.jsonl"]
  - name: child-work
    sheets: 1
    instrument_guidance: "the child score's work sheets — a full score, not a fan-out sheet"
    fallback_friendly: true
    purpose: "Do the derivative work."
    artifacts: []
  - name: receipt
    sheets: 1
    instrument_guidance: "instrument: cli — the child's terminal act; writes into the shared workspace under its own child_id path (collision-proof)"
    fallback_friendly: false
    purpose: "Write receipts/{child_id}.json {status, digest, ts}. Closes the ledger row."
    artifacts: ["receipts/"]
  - name: reconcile
    sheets: 1
    instrument_guidance: "instrument: cli — next cycle; unclosed rows are the visible failure state"
    fallback_friendly: false
    purpose: "List every spawn: closed, running (lease live), or lost (past lease, no receipt — investigate)."
    artifacts: []
dependencies:
  child-work: ["spawn"]
  receipt: ["child-work"]
  reconcile: ["receipt"]
composes_with:
  - pattern: "The Fleet Receipt Ledger"
    how: "unclosed rows are unaccounted members — the auditor consumes this ledger"
  - pattern: "Is-Line-Clear"
    how: "before each spawn, check the receipt lane is clear"
  - pattern: "Canon of Phases"
    how: "compose when a rotating parent spawns non-waiting children"
config_features:
  - "triggers.on_success.concert (UNPROVEN as non-waiting handoff — appears in proof scores only as self-chain)"
  - "inherit_workspace: true"
  - "instrument: cli"
---

## The Non-Waiting Hand

`Status: Working` · **Source:** discover pass 1, cycle 7 — Expedition 4 (mission command's intent-based tasking; OFRP surge semantics). **Forces:** Partial Failure + Information Asymmetry.

### Core Dynamic

Waiting is a coupling; this pattern is a **decoupling with a contract instead**. The parent submits a child via `concert` (submit without waiting; `inherit_workspace: true` shares lineage) and continues — the parent may finish, fail, or spawn again before the child completes. What keeps this from fire-and-forget negligence is the interface: the parent writes a **spawn ledger** (append-only JSONL), and the child, as its terminal act, writes a **receipt**. The pair — spawn row and receipt — is the complete communication between generations, deliberately inspectable. **Unclosed rows are the pattern's visible failure state** — not an error, a reconciliation gap. The hand is *typed*: the child knows from its prelude which ledger row spawned it, and its receipt closes that row.

Strengthenings built in: **single-writer ledger** (the parent is the only appender; children write receipts, never ledger rows — no locks needed); **stable child ids** (the parent-minted `child_id` is the receipt's filename — collision-proof by construction under `inherit_workspace`); **leases** (each row carries `lease_until`; a row past lease without receipt is *lost*, not *running* — reconcile distinguishes closed / running / lost mechanically).

### Marianne Score Structure

```yaml
# Parent score:
  - name: spawn
    instrument: cli
    command: "CID=\"child-$(date +%s)-$$\"; printf '{child_id: %s, score: investigate.yaml, ts: %s, lease_until: %s}\\n' \"$CID\" \"$(date -Is)\" \"$(date -d '+2 hours' -Is)\" >> spawn-ledger.jsonl"
    validations:
      - type: command_succeeds
    triggers:
      on_success:
        - concert: { score: investigate.yaml, inherit_workspace: true }
# Child score (terminal sheet):
  - name: receipt
    instrument: cli
    command: "printf '{child_id: %s, status: done, digest: %s, ts: %s}\\n' \"$MARIANNE_CHILD_ID\" \"$(sha256sum findings.md | cut -c1-12)\" \"$(date -Is)\" > \"receipts/$MARIANNE_CHILD_ID.json\""
    validations:
      - type: file_exists
        path: "receipts/{{ child_id }}.json"
```

**Negative control:** remove the child's receipt sheet — the parent's next-cycle reconciliation must report the row unclosed and escalate (or the Fleet Receipt Ledger flags it). **If nothing anywhere can notice the unclosed row, the contract is decorative** — that control is the proof.

### When to Use

Continuous producers with derivative work; anywhere the parent's rhythm is the product and children are consequences.

### When NOT to Use

When the parent's next step genuinely needs the child's output — that is a dependency; non-waiting is malpractice. And it dies without the ledger/receipt contract: a bare concert trigger with no spawn record is fire-and-forget, which this pattern explicitly refuses.

### Composes With

The Fleet Receipt Ledger (mandatory companion), Is-Line-Clear (lane check), Canon of Phases (rotating parents)
