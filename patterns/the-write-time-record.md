---
name: "The Write-Time Record"
scale: foundational
type: orchestration-pattern
status: working
forces:
  - "Partial Failure"
  - "Information Asymmetry"
generators:
  - "Accumulate Knowledge"
problem: "Obligations and provenance are reconstructed by archaeology at end-of-life, after the people and context that created them are gone."
signals:
  - "provisioning creates removal obligations nobody writes down"
  - "a teardown plan that begins with 'figure out what we created'"
  - "a manifest written from memory at the end of a campaign"
config_features:
  - "instrument: cli"
  - "per_sheet_fallbacks"
stages:
  - name: plan-effects
    sheets: 1
    instrument_guidance: "any — plans effects as typed rows with stable effect ids"
    fallback_friendly: true
    purpose: "Emit effects-plan.jsonl: {effect_id, kind, command, decommission_cmd}."
    artifacts: ["effects-plan.jsonl"]
  - name: transact
    sheets: 1
    instrument_guidance: "instrument: cli — ONE process writes intent row, executes effect, appends receipt"
    fallback_friendly: false
    purpose: "Atomic per-effect transaction; idempotent by effect_id; fail-closed on open rows."
    artifacts: ["disposal-ledger.jsonl"]
  - name: audit
    sheets: 1
    instrument_guidance: "instrument: cli — three-way join with empty residue"
    fallback_friendly: false
    purpose: "row ↔ receipt ↔ settlement join; open rows or unmatched receipts fail."
    artifacts: []
dependencies:
  transact: ["plan-effects"]
  audit: ["transact"]
composes_with:
  - pattern: "Demobilization Checkout"
    how: "its consumption side — the demob census reads the record as its work list"
  - pattern: "Fork-Evident History"
    how: "payload/substrate — the record rides the append-only chain"
  - pattern: "Vintage Overlay"
    how: "the vintage record is its run-level instance"
---

## The Write-Time Record

`Status: Working` · **Source:** iteration 6. **Scale:** foundational law. **Forces:** Partial Failure, Information Asymmetry.

### Core Dynamic

Obligations and provenance are recorded at the moment the obligation is created — not discovered by archaeology at the end. The ship carries its Inventory of Hazardous Materials from keel-laying, so the demolition contractor's work list is written by the builder years before the dismantler exists.

The atomicity rule: intent row, effect, and receipt commit inside **one CLI process**, keyed by a stable `effect_id` — the transact wrapper appends the intent row, executes the command, and appends the receipt `{effect_id, exit_code, settled_at}` in a single invocation. A crash between intent and receipt leaves an **open row**, and open rows fail the audit (fail-closed, never silently carried). A re-run with the same `effect_id` refuses double-execution: unstarted rows re-run; started-unsettled rows stop for inspection; settled rows are joined, never repeated. Recovery semantics per transition.

This is disk-over-memory discovered independently by every mature coordination domain: the only honest moment to record a promise is the moment it is made, and a manifest written at end-of-life from memory is exactly the survivor-testimony failure the record exists to prevent.

### When to Use / When NOT to Use

Use: every effect-bearing score — provisioning (secret created → destruction obligation; DNS record → removal command; queue → drain procedure), every removal (provenance rides the removal), every aggregation (guarantees ride the output), every handoff into an unknown future consumer.

Not: effects cheaply enumerable after the fact (a pure workspace with no external reach — archaeology is cheaper than bookkeeping); the record's write cost competes with the work itself for trivial, reversible effects.

### Marianne Score Structure

```yaml
movements:
  1: { name: plan-effects }
  2: { name: transact, instrument: cli, instrument_fallbacks: [] }
  3: { name: audit, instrument: cli, instrument_fallbacks: [] }
sheet:
  size: 1
  total_items: 3
  dependencies: { 2: [1], 3: [2] }
  per_sheet_fallbacks: { 2: [], 3: [] }
prompt:
  template: |
    {% if stage == 1 %}
    Plan the effects. Write {{ workspace }}/effects-plan.jsonl, one row per effect:
    {effect_id, kind, command, decommission_cmd}. effect_id is stable and unique.
    {% elif stage == 2 %}
    bash "{score_dir}/scripts/effects.sh" transact --plan "{{ workspace }}/effects-plan.jsonl" \
      --ledger "{{ workspace }}/disposal-ledger.jsonl"
    {% else %}
    bash "{score_dir}/scripts/effects.sh" audit --ledger "{{ workspace }}/disposal-ledger.jsonl" --require-empty-residue
    {% endif %}
validations:
  - type: command_succeeds
    command: 'bash {score_dir}/scripts/effects.sh --self-test'
    condition: "stage == 2"
  - type: command_succeeds
    command: 'bash {score_dir}/scripts/effects.sh audit --ledger {workspace}/disposal-ledger.jsonl --require-empty-residue'
    condition: "stage == 3"
```

### Example

A two-year research campaign provisions buckets, service accounts, webhooks, and model artifacts across four clouds, each through the transact wrapper. Funding ends: the decommission score reads the ledger as its sole work list — newest-first, by `effect_id` — drains, deletes, and revokes every row, and emits a completion certificate the day the grant closes.

### Review Integration

Iteration 6: Reviews 1 and 2 found the draft's three loosely sequenced stages allowed a manifest row to exist while the effect failed, changed target, or ran twice. The atomic transact wrapper (one process per effect, idempotency key, fail-closed audit on open rows) is the fix; line-count decorations are gone — the audit is a three-way join with empty residue.
