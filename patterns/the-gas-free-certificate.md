---
name: "The Gas-Free Certificate"
scale: score-level
type: orchestration-pattern
status: working
forces:
  - "Partial Failure"
  - "Exponential Defect Cost"
generators:
  - "Gate on Environmental Readiness"
problem: "Destructive operations run on the strength of a check that passed earlier, against a world that has since moved."
signals:
  - "rm, force-push, schema-drop, secret-revoke, teardown ahead"
  - "'the check passed earlier' is load-bearing for something irreversible"
  - "a retried or resumed run about to reuse yesterday's verification"
config_features:
  - "instrument: cli"
  - "per_sheet_fallbacks"
stages:
  - name: plan-destruction
    sheets: 1
    instrument_guidance: "any — plans what to destroy and why; never executes"
    fallback_friendly: true
    purpose: "Emit plan.json: target path, exact destructive command, rollback posture."
    artifacts: ["plan.json"]
  - name: certify
    sheets: 1
    instrument_guidance: "instrument: cli, separately-committed certifier/ dir — independence is authored provenance"
    fallback_friendly: false
    purpose: "Write permit {target_digest, issued_at, expires_at, certifier_digest}."
    artifacts: ["permit.json"]
  - name: destroy
    sheets: 1
    instrument_guidance: "instrument: cli wrapper — permit check AND destruction in ONE transaction"
    fallback_friendly: false
    purpose: "Refuse on stale/mismatched permit; execute only inside the process that checked."
    artifacts: ["receipts.jsonl"]
  - name: record
    sheets: 1
    instrument_guidance: "instrument: cli — ledger append, permit↔receipt join"
    fallback_friendly: false
    purpose: "The Write-Time Record's consumption side at the destructive boundary."
    artifacts: []
dependencies:
  certify: ["plan-destruction"]
  destroy: ["certify"]
  record: ["destroy"]
composes_with:
  - pattern: "The Validity Window"
    how: "the destructive-boundary specialization — window + independence + digest binding"
  - pattern: "The Fencing Token"
    how: "substitution — pre-flight and cheap instead of rejection at the write boundary"
  - pattern: "Standby–GO"
    how: "contrast — the cue confirms receiver readiness; the permit confirms environment safety, and it decays"
---

## The Gas-Free Certificate

`Status: Working` · **Source:** iteration 6 (Expedition 1 — ship-breaking's Gas-Free for Hot Work certification). **Scale:** score-level. **Forces:** Partial Failure, Exponential Defect Cost.

### Core Dynamic

Before any torch touches steel near a tank, the yard obtains a certificate from a *competent person who is not the crew doing the burning* — and the certificate expires, and any interruption invalidates it, and resumption demands re-certification. Three load-bearing properties: **independence** (a separately-committed `certifier/` directory whose digest is recorded in the permit — independence is provenance, not a pathname); **freshness** (bounded validity from issuance — the Validity Window at its sharpest); **binding** (the permit names the exact target state by digest, so it cannot be replayed against different bytes). And the property the reviews forced: **check-and-act atomicity** — the destroy movement is a single CLI wrapper that verifies the permit and executes the destruction in the same process; a failed check refuses with exit non-zero and nothing is destroyed. The AI sheet plans what to destroy and why; it never presses the button, and no validation-after-the-fact pretends otherwise.

A retried or resumed run re-certifies, because interruption is itself evidence the world may have moved. A retry that reuses yesterday's gas-free check is the explosion.

### When to Use / When NOT to Use

Use: every destructive or irreversible stage whose safety depends on environment state that can change underneath you — deletions of shared state, force-pushes, schema-dropping migrations, secret revocation, quarantine purges.

Not: cheap, local, reversible operations (a worktree delete with a fresh clone as backstop); the certifier not genuinely independent in authorship; the digest binding dropped (then the certificate certifies "some state was once fine," which certifies nothing).

### Marianne Score Structure

```yaml
movements:
  1: { name: plan-destruction }
  2: { name: certify, instrument: cli, instrument_fallbacks: [] }
  3: { name: destroy, instrument: cli, instrument_fallbacks: [] }
  4: { name: record, instrument: cli, instrument_fallbacks: [] }
sheet:
  size: 1
  total_items: 4
  dependencies: { 2: [1], 3: [2], 4: [3] }
  per_sheet_fallbacks: { 2: [], 3: [], 4: [] }
prompt:
  variables: { ttl_minutes: 30 }
  template: |
    {% if stage == 1 %}
    Plan the destruction. Write {{ workspace }}/plan.json: target path, exact
    destructive command, rollback posture. Do NOT execute anything.
    {% elif stage == 2 %}
    bash "{score_dir}/certifier/gas-free.sh" --plan "{{ workspace }}/plan.json" \
      --ttl-minutes {{ ttl_minutes }} --emit "{{ workspace }}/permit.json"
    {% elif stage == 3 %}
    bash "{score_dir}/certifier/execute.sh" --permit "{{ workspace }}/permit.json" --plan "{{ workspace }}/plan.json"
    {% else %}
    bash "{score_dir}/scripts/ledger.sh" append-permit "{{ workspace }}/permit.json" \
      --receipts "{{ workspace }}/receipts.jsonl"
    {% endif %}
validations:
  - type: command_succeeds
    command: 'bash {score_dir}/certifier/execute.sh --self-test'
    condition: "stage == 3"
  - type: command_succeeds
    command: 'bash {score_dir}/scripts/ledger.sh append-permit {workspace}/permit.json --receipts {workspace}/receipts.jsonl --require-join'
    condition: "stage == 4"
```

Self-test: a stale-permit fixture and a mismatched-target fixture must both fail `execute.sh` with nothing destroyed — the negative control reaches the real gate.

### Example

A nightly maintenance score force-pushes a regenerated `gh-pages` site. The certify movement verifies branch head, worktree cleanliness, and build reproducibility, and writes a permit naming the exact tree hash. A human's emergency merge at 2 AM invalidates the permit silently and correctly — morning's run re-certifies instead of force-pushing over the emergency fix.

### Review Integration

Iteration 6: Review 1's most dangerous finding — the draft told the destructive AI sheet to run the permit check "as its first action" with validation only after the sheet, so destruction could precede or ignore the check ("this pattern teaches false safety"). The fix is structural: destruction is a command, so the pattern is CLI-native end to end — one wrapper, one transaction, check-and-act atomic. Review 2's authored-provenance independence (separately-committed certifier directory with its digest in the permit) replaced the draft's directory-name hand-wave.
