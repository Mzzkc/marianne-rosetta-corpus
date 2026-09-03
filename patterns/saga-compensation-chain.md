---
name: "Saga Compensation Chain"
scale: concert-level
type: orchestration-pattern
status: working
forces:
  - "Partial Failure"
  - "Exponential Defect Cost"
generators:
  - "Exploit Failure as Signal"
  - "Contract at Interfaces"
problem: "Partial completion of a multi-score concert leaves inconsistent shared state unless each committed effect has durable, reverse-ordered compensation authority."
signals:
  - "concert scores produce externally visible side effects"
  - "partial completion is worse than a compensating forward action"
  - "manual cleanup after failure is expensive or error-prone"
  - "each effect can name an idempotent compensating operation"
stages:
  - name: prepare-effect
    sheets: 1
    instrument_guidance: "codex-cli or claude-code — designs the domain action and its idempotent compensation before either can execute"
    fallback_friendly: false
    purpose: "Append a PREPARED saga row containing effect identity, compensation command, and input digest before the side effect."
    artifacts: ["saga-log.jsonl"]
  - name: commit-effect
    sheets: 1
    instrument_guidance: "any-wrapped CLI profile — performs the exact prepared operation and atomically marks the row COMMITTED"
    fallback_friendly: false
    purpose: "Execute one forward effect whose compensation is already durably named."
    artifacts: ["saga-log.jsonl", "forward-receipt.json"]
  - name: compensate
    sheets: 1
    instrument_guidance: "any-wrapped CLI profile — the durable on_failure hook launches the compensation score, which walks committed rows in reverse order"
    fallback_friendly: false
    purpose: "Apply idempotent compensations newest-first and record every settlement without changing the original failed status."
    artifacts: ["compensation-results.jsonl"]
dependencies:
  commit-effect: [prepare-effect]
  compensate: [commit-effect]
composes_with:
  - pattern: "After-Action Review"
    how: "payload/substrate — the immutable saga and compensation results supply the factual execution record"
  - pattern: "The Black-Box Ledger"
    how: "layering — terminal packet evidence explains why compensation began and what had committed"
  - pattern: "Replication Licensing"
    how: "layering — single-use licenses prevent duplicate forward effects while compensation remains idempotent"
---

## Saga Compensation Chain

`Status: Working` · **Source:** Garcia-Molina & Salem (1987), distributed sagas; iteration 4, unblocked in iteration 5.1 by durable terminal `on_failure` hooks.

### Problem Depth

A concert can commit effects that cannot be rolled back transactionally: a deployment becomes visible, a notification leaves the system, or a remote record changes. If a later score fails, restoring a checkpoint does not undo those effects. Manual cleanup is also not a protocol: it loses ordering, duplicates work after restart, and cannot prove which effects were neutralized.

The pattern therefore uses forward-acting compensation. Before each effect, the score durably records the exact compensating action. After terminal failure, Marianne's top-level `on_failure` hook launches a compensation score once under a durable claim. That score walks only `COMMITTED` rows in reverse commit order and appends settlement results.

### Core Dynamic

For forward effects `T1 … Tk`, a failure after `Tk` invokes compensations `Ck … C1`. Compensation does not erase history and does not pretend the original action never happened. It produces a new effect that restores an acceptable business state.

The write order is constitutive:

1. Append `PREPARED` with stable effect ID, input digest, and compensation identity.
2. Execute the effect using that identity as its idempotency key where the boundary supports one.
3. Atomically append or transition to `COMMITTED` with a receipt.
4. On terminal failure, compensate committed rows newest-first.
5. Record `COMPENSATED`, `NOOP_ALREADY_COMPENSATED`, or `COMPENSATION_FAILED`; never rewrite the original rows.

The gap between effect execution and a durable commit receipt cannot be wished away. For boundaries without an idempotency/readback mechanism, the row remains `UNCERTAIN` and requires human resolution rather than an automatic second effect.

### When to Use / When NOT to Use

Use this for multi-score concerts with real side effects where partial completion is materially worse than explicit neutralization. Do not use it for workspace-only, cheaply recreated artifacts; ordinary cleanup or a fresh workspace is simpler. Do not use it when no safe compensating action exists, or when compensation would itself cause irreversible harm without human authorization.

### Marianne Score Structure

Forward score:

```yaml
name: migrate-customer-state
instrument: codex-cli

sheet:
  size: 1
  total_items: 2
  dependencies: { 2: [1] }
  per_sheet_fallbacks:
    1: []
    2: []

movements:
  1: { name: prepare-effect }
  2: { name: commit-effect }

prompt:
  template: |
    {% if stage == 1 %}
    python "{{ score_dir }}/scripts/saga.py" prepare \
      "{{ workspace }}/saga-log.jsonl" customer-schema-v3 \
      --compensation revert-customer-schema-v3
    {% elif stage == 2 %}
    python "{{ score_dir }}/scripts/saga.py" execute \
      "{{ workspace }}/saga-log.jsonl" customer-schema-v3
    {% endif %}

validations:
  - type: command_succeeds
    command: 'python "{score_dir}/scripts/saga.py" check "{workspace}/saga-log.jsonl" --state PREPARED'
    condition: "stage == 1"
  - type: command_succeeds
    command: 'python "{score_dir}/scripts/saga.py" check "{workspace}/saga-log.jsonl" --state COMMITTED'
    condition: "stage == 2"

on_failure:
  - type: run_job
    job_path: "{score_dir}/compensate-customer-state.yaml"
    job_workspace: "{workspace}"
    fresh: true
    detached: false
    on_failure: abort
    timeout_seconds: 900
    description: "Compensate committed saga effects newest-first"
```

The compensation score uses the same workspace, reads `saga-log.jsonl`, and delegates deterministic reverse traversal to the wrapper:

```yaml
name: compensate-customer-state
instrument: codex-cli

sheet: { size: 1, total_items: 1 }

prompt:
  template: |
    python "{{ score_dir }}/scripts/saga.py" compensate \
      "{{ workspace }}/saga-log.jsonl" \
      --results "{{ workspace }}/compensation-results.jsonl"

validations:
  - type: command_succeeds
    command: 'python "{score_dir}/scripts/saga.py" verify-settled "{workspace}/saga-log.jsonl"'
```

### Failure Modes

- **Log-after-effect:** a crash leaves an effect with no compensating identity. Prepare before execution.
- **Blind replay:** the hook repeats a non-idempotent compensation after restart. Bind each result to the stable effect ID and treat settled IDs as no-ops.
- **Forward-order undo:** compensating oldest-first violates dependencies introduced by newer effects.
- **False rollback language:** the audit trail disappears even though external observers saw the original effect. Append; never erase.
- **Compensation laundering:** hook failure replaces or hides the original terminal error. The failed job stays failed, and compensation results remain a separate durable record.
- **Unbounded recursive failure:** a compensation score carries the same automatic compensation hook and chains indefinitely. Compensation scores must terminate, quarantine failures, and escalate.

### Review Integration

The v4 split file was aspirational because Marianne did not expose failure actions. Current source at `10f1c8220307211ea646781454825a95bb3b79e3` defines a top-level `on_failure` list using the existing `run_job`/`run_command`/`run_script` hook contract; the daemon durably claims and settles the sequence and recovers unfinished claims after restart. Iteration 5.1 therefore promotes the pattern to working and removes the obsolete `blocked_by` field.

The durable hook is trigger custody, not transactional magic. The score still owns prepare-before-effect logging, stable identities, idempotent compensation, reverse ordering, and quarantine of ambiguous state. This correction uses the real hook syntax and does not claim that the hook can infer missing compensation data.

### Composes With

After-Action Review, The Black-Box Ledger, Replication Licensing
