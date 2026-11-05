---
name: "The Negative Ledger"
scale: iteration
type: orchestration-pattern
status: working
iteration_added: "discover pass 1, cycle 7"
forces:
  - "Partial Failure"
  - "Accumulated Signal"
generators:
  - "Exploit Failure as Signal"
problem: "Falsified approaches are forgotten between runs, so later scores re-burn full runs to rediscover known incompatibilities."
signals:
  - "long-lived workspaces where runs accumulate"
  - "the same vendor/tool/endpoint incompatibility rediscovered by a new score"
  - "integration scouting that should take minutes and takes a run"
stages:
  - name: attempt
    sheets: 1
    instrument_guidance: "score-author's choice — the work sheet whose failure is informative"
    fallback_friendly: true
    purpose: "Attempt the approach; failure evidence is captured, not discarded."
    artifacts: []
  - name: falsify-record
    sheets: 1
    instrument_guidance: "instrument: cli — on_fail post-step; writes the canonical signature, never prose"
    fallback_friendly: false
    purpose: "Append to ledger/negative.md: {signature_code, tool, endpoint, error_class, digest, ts}."
    artifacts: ["ledger/negative.md"]
  - name: consult
    sheets: 1
    instrument_guidance: "instrument: cli — matches canonical signature codes only; zero AI"
    fallback_friendly: false
    purpose: "At the moment of decision, grep the planned approach's signature codes; non-empty match escalates to override-with-reason."
    artifacts: []
dependencies:
  falsify-record: ["attempt"]
  consult: ["falsify-record"]
composes_with:
  - pattern: "The Sealed Dissent"
    how: "the within-run, exact-id face of the same discipline"
  - pattern: "Dead Letter Quarantine"
    how: "DLQ learns within a batch; the ledger fences across runs"
  - pattern: "Fork-Evident History"
    how: "the ledger is append-only; overrides append to the same entry, growing a dissent of its own"
config_features:
  - "instrument: cli"
  - "on_fail post-steps"
---

## The Negative Ledger

`Status: Working` · **Source:** discover pass 1, cycle 7 — split from the draft's compound Sealed Dissent entry (two lifetimes, two lookup semantics). **Forces:** Partial Failure + Accumulated Signal.

### Core Dynamic

Cross-run fence: **canonical approach identity or it does not exist.** Prose signatures are not identity — "rate-limited" does not match "429," and prose greps both miss synonyms and block materially changed approaches. Every entry carries a **closed-vocabulary signature code** (e.g., `AUTH-INCOMPAT`, `RATE-LIMITED`, `SCHEMA-BREAK`) plus the tool/endpoint pair — the things the deciding sheet can state before attempting. Consult matches signature codes, never prose.

Override semantics: an override appends its reason **to the same entry** — the ledger grows a dissent of its own, and repeated overrides against an unchanged world are themselves a signal. Entries carry an expiry/generation stamp: a tool upgrade legitimately re-opens fenced ground (pair with the Validity Window's failure-evidence profile).

### Marianne Score Structure

```yaml
sheets:
  - name: attempt
    prompt: "Integrate vendor X per integration-plan.md."
    on_fail:
      - run: "printf 'SIG: AUTH-INCOMPAT | tool: vendor-x | endpoint: oauth2 | ts: %s\\n' \"$(date -Is)\" >> ledger/negative.md"
  - name: consult
    instrument: cli
    command: "! grep -q 'SIG: AUTH-INCOMPAT.*tool: vendor-x' ledger/negative.md || (echo 'FENCED: vendor-x AUTH-INCOMPAT — override requires a reason appended to this entry' && exit 1)"
    validations:
      - type: command_succeeds
```

**Negative control:** pre-seed the ledger with the planned approach's signature; consult must exit non-zero. **Sentinel:** variant with the ledger write removed — a later score re-attempts vendor X, the consult gate cannot match, runs, and the sentinel validator fails on the known-bad string reappearing.

### When to Use

Long-lived workspaces; multi-score campaigns over the same vendors/endpoints; anywhere "we tried that and it failed" is currently answered by archaeology.

### When NOT to Use

Vocabulary drift across runs without the closed code set; write-only ledgers gating nothing; entries with no expiry (a fence that never re-opens fences out the truth too).

### Composes With

The Sealed Dissent (within-run face), Dead Letter Quarantine (batch vs. cross-run), Fork-Evident History (append-only, overrides visible)
