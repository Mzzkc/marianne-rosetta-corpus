---
name: "The Watch Rollover"
scale: iteration
type: orchestration-pattern
status: working
iteration_added: "discover pass 1, cycle 7"
forces:
  - "Partial Failure"
  - "Information Asymmetry"
generators:
  - "Accumulate Knowledge"
problem: "State that must cross an iteration boundary survives only as an external, typed, bounded artifact — context windows die and ledgers persist."
signals:
  - "long self-chaining improvement loops"
  - "bounded loops whose iterations are expensive enough that losing in-flight state at a restart matters"
  - "any score where 'how did the last period end' should have a durable answer"
stages:
  - name: period-work
    sheets: 1
    instrument_guidance: "score-author's choice — the period's work, in a sheet.loops bound or a self-chain cycle"
    fallback_friendly: true
    purpose: "Do the period's work."
    artifacts: []
  - name: rollover
    sheets: 1
    instrument_guidance: "instrument: cli — writes the four-section ledger under advisory lock with atomic rename; assembled from workspace facts, never the working sheet's self-summary"
    fallback_friendly: false
    purpose: "Write watch-ledger.md: COMPLETED / IN-FLIGHT / POISONED / NEXT-PLAN."
    artifacts: ["watch-ledger.md"]
  - name: relief
    sheets: 1
    instrument_guidance: "next period's first sheet — echoes open exceptions before any new work (Readback's discipline at the seam)"
    fallback_friendly: true
    purpose: "Receive the watch: echo in-flight and poisoned items first."
    artifacts: []
  - name: audit
    sheets: 1
    instrument_guidance: "instrument: cli — diff check; the ledger grows monotonically, no period rewrites another's entries"
    fallback_friendly: false
    purpose: "Append-only enforcement, mechanically."
    artifacts: ["ledger-hist.sha"]
dependencies:
  rollover: ["period-work"]
  relief: ["rollover"]
  audit: ["relief"]
composes_with:
  - pattern: "Transfer of Command"
    how: "the rollover is scheduled transfer of command with the same ledger discipline"
  - pattern: "Cathedral Construction"
    how: "Cathedral persists the artifact across self-chains; this persists the operational exception set — compose both on long campaigns"
  - pattern: "checkpoint_persistence"
    how: "the carrier that survives restarts (engine primitive, unproven in any proof score — flagged)"
config_features:
  - "instrument: cli"
  - "file_exists as dependency"
  - "sheet.loops or concert self-chain (UNPROVEN as first-class loop carrier)"
---

## The Watch Rollover

`Status: Working` · **Source:** discover pass 1, cycle 7 — Expedition 3 (ICS operational periods, watch relief at sea). Split from the draft's compound Watch Rollover × Rolling Continuity entry (their data-loss policies are opposites: rollover preserves the complete exception set; continuity samples and expires a bounded subset). **Forces:** Partial Failure + Information Asymmetry.

### Core Dynamic

Each period ends with a durable ledger — completed / in-flight / poisoned / next-plan — and the next period begins by *reading* it, its first act an echo of the open exceptions. **A handoff nobody receives is a diary.** The ledger refuses the self-authored summary: assembled by a CLI from workspace facts; append-only enforced by diff.

### The carry file (Rolling Continuity's surviving mechanics, as a section)

For bounded carried state across generations — distinct from the exception ledger, which is complete: each cycle's carry is capped at a **declared ratio** (K entries, size-capped, every entry generation-stamped); entries not re-confirmed for G generations are dropped **by script, not by sentiment**; drift against a frozen anchor digest routes to review with the carry quarantined instead of another generation. Carry too much and acid accumulates until the culture sours itself; carry too little and the character is lost. Independent promotion of Continuity as its own pattern is deferred to candidates, owed the metric: why this ratio preserves useful state better than a capped priority queue.

### Marianne Score Structure

```yaml
  - name: rollover
    instrument: cli
    command: "python3 scripts/rollover.py workspace-facts/ --out watch-ledger.md --atomic && flock advisory.lock sha256sum watch-ledger.md >> ledger-hist.sha"
    validations:
      - type: content_contains
        path: "watch-ledger.md"
        pattern: "IN-FLIGHT:"
      - type: content_contains
        path: "watch-ledger.md"
        pattern: "POISONED:"
  - name: relief
    capture_files: ["watch-ledger.md"]
    prompt: "FIRST ACT: echo every IN-FLIGHT and POISONED item from watch-ledger.md as {item, blocking_reason}. Then begin this period's plan."
    validations:
      - type: content_contains
        pattern: "ECHO:"
  - name: audit
    instrument: cli
    command: "python3 scripts/append_only_check.py watch-ledger.md ledger-hist.sha"
```

**Negative controls:** two periods with the rollover removed — the second must fail its prelude dependency (`file_exists` on the ledger) rather than silently starting fresh; the proof asserts on the *state*, catching exactly the loss. An audit seeded with a rewritten prior entry must fail the diff.

### When to Use

Long self-chaining improvement loops; expensive iterations where restart state loss matters; any score where the period's ending should have a durable answer.

### When NOT to Use

Short scores (no watch to relieve); ledgers written but never read (theater); non-continuous state in the carry (noise, not culture).

### Composes With

Transfer of Command (scheduled succession), Cathedral Construction (artifact vs. exception persistence), checkpoint_persistence (restart carrier)
