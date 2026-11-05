---
name: "The Fleet Receipt Ledger"
scale: concert-level
type: orchestration-pattern
status: working
iteration_added: "discover pass 1, cycle 7"
forces:
  - "Partial Failure"
generators:
  - "Exploit Failure as Signal"
problem: "Every fleet member ends in one of four states — completed, failed, never-started, unaccounted — and only the fourth is invisible without a ledger."
signals:
  - "every fleet run that matters enough to audit — which is every fleet run, because unaccounted members are how partial failure hides at fleet scale"
  - "non-waiting children without receipts (the unaccounted-member generator)"
execution_path: "out-of-band auditor child score, spawned non-waiting at fleet launch — NOT a depends_on-all terminal group, which may never run when a group fails"
stages:
  - name: collect
    sheets: 1
    instrument_guidance: "instrument: cli — in the auditor child score; polls the shared workspace for receipts regardless of child outcome"
    fallback_friendly: false
    purpose: "Gather every receipt into receipts/ — no judgment."
    artifacts: ["receipts/"]
  - name: reconcile
    sheets: 1
    instrument_guidance: "instrument: cli — the bijection as a jq program; accounting that is a set operation cannot be argued with"
    fallback_friendly: false
    purpose: "Roster set == receipt set; mismatches become typed exceptions: unaccounted / duplicate / orphan."
    artifacts: ["reconciliation.json"]
  - name: disposition
    sheets: 1
    instrument_guidance: "strong reasoner — one disposition per exception row, each citing evidence"
    fallback_friendly: false
    purpose: "Write dispositions.jsonl; row count == exception count, no omissions."
    artifacts: ["dispositions.jsonl"]
dependencies:
  reconcile: ["collect"]
  disposition: ["reconcile"]
composes_with:
  - pattern: "The Non-Waiting Hand"
    how: "mandatory companion — unclosed spawn rows are unaccounted members; the auditor is itself spawned by this hand"
  - pattern: "Demobilization Checkout"
    how: "this is that pattern lifted from a concert's terminal score to fleet authority"
  - pattern: "Rejoinder Ledger"
    how: "dispositions map one-to-one onto exceptions — no omitted, no duplicated"
config_features:
  - "instrument: cli"
  - "csv_unique_key"
  - "concert trigger (auditor spawn, UNPROVEN)"
---

## The Fleet Receipt Ledger

`Status: Working` · **Source:** discover pass 1, cycle 7 — Expedition 4 (military change-of-command inventory; DoDI 7730.66's prohibition on unverified reports); collision §1.2, one of five dual-enumeration arrivals. Both reviews called the concept strongest and the wiring fatal; the wiring is rebuilt. **Force:** Partial Failure.

### Core Dynamic

Exceptions fall into exactly three typed classes: *unaccounted* (roster member, no receipt), *duplicate* (one member, several receipts), and *orphan* (receipt, no roster member — the most interesting class: **something ran that the composer never declared**). Then, and only then, judgment enters: dispositions, one per row, each citing evidence. The ledger is the fleet layer's proof of work — the artifact that lets someone who was not present reconstruct what actually happened, member by member. Receipts are machine-checkable or they are stories: `{member, status, digest, timestamp, validation_set}`.

**The rebuilt execution path:** an accounting group that `depends_on` all working groups may never run when a group fails — the exact case it must account for. The auditor is therefore an **out-of-band child score**, spawned non-waiting at fleet launch, polling the shared workspace and reading terminal state regardless of child outcome; it runs to completion even when the fleet partially fails — that is its entire reason to exist.

### Marianne Score Structure

```yaml
# In the auditor child score (spawned at fleet launch, non-waiting):
  - name: reconcile
    instrument: cli
    command: "python3 scripts/reconcile.py roster.jsonl receipts/ --out reconciliation.json"
    validations:
      - type: command_succeeds
      - type: csv_unique_key
        path: "receipts/"
        key: "member"
  - name: disposition
    capture_files: ["reconciliation.json"]
    prompt: "For each exception row, write ONE disposition citing evidence: {exception, disposition, evidence}."
    response_format: { type: json_object }
    validations:
      - type: command_succeeds
        command: "test $(jq 'length' reconciliation.json) -eq $(jq 'length' dispositions.jsonl)"
```

**Negative control:** delete one member's receipt before reconciliation — the bijection gate must fail and the disposition sheet must record an unaccounted-member disposition. **A ledger that cannot catch a missing receipt is a receipt.**

### When to Use

Every fleet run that matters enough to audit; mandatory companion to the Non-Waiting Hand.

### When NOT to Use

Single-score work (the conductor already accounts for sheets); prose receipts; a reconciliation that has never once reported an exception in rehearsal — a fleet that has not rehearsed its failures.

### Composes With

The Non-Waiting Hand (unclosed rows), Demobilization Checkout (fleet authority), Rejoinder Ledger (one disposition per exception)
