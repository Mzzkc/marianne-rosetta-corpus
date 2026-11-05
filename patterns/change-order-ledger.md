---
name: "The Change-Order Ledger"
scale: communication
status: working
forces: [Information Asymmetry, Progressive Commitment, Typed Force]
generators: [Contract at Interfaces]
problem: "Mid-run plan mutations are reconstructible only by diffing prompts, so no sheet can know what it was authorized to do."
signals:
  - "cadenza injections, escalation dispositions, or redlines change scope mid-run"
  - "sheets run under a version of the plan that no longer exists"
  - "'the plan changed mid-run' has ever been answered by archaeology"
stages:
  - name: baseline
    sheets: 1
    instrument_guidance: "mid-tier or CLI — transcribes declared config into ledger.jsonl's opening entry (authorized scope, tolerances, datum digest)"
    fallback_friendly: true
    purpose: "Exhibit A: the authorized state at launch."
  - name: work
    sheets: fan_out(N)
    instrument_guidance: "work instruments; each writes ONLY into outputs/{sheet_id}/ — isolation is what makes the scope check deterministic"
    fallback_friendly: true
    purpose: "Do authorized work; per-sheet outputs are attributable by construction."
  - name: scope-check
    sheets: 1
    instrument_guidance: "any-wrapped CLI, per_sheet_fallbacks: [] — per completed sheet: every file under outputs/{sheet_id}/ ⊆ authorized-set under the latest entry whose effective_from precedes that sheet's recorded start"
    fallback_friendly: false
    purpose: "Deterministic scope enforcement; exits 1 naming the unauthorized path."
  - name: append
    sheets: 1
    instrument_guidance: "CLI, per_sheet_fallbacks: [] — appends change orders {id, authority, effective_from, before/after digests, reason}; digest-chained (prev_entry_sha256)"
    fallback_friendly: false
    purpose: "The only writer to the ledger; authority is authorship-time configuration, never interpreted at runtime."
dependencies:
  work: [baseline]
  scope-check: [work]
composes_with:
  - pattern: "The Negative Ledger"
    how: "duals — the Negative Ledger owns refusals, this owns authorizations"
  - pattern: "Configuration Control Board"
    how: "the ledger is the CCB's runtime enforcement face"
  - pattern: "Commander's-Intent Envelope"
    how: "intent envelopes the run; change orders are its authorized deltas"
  - pattern: "The Midseason Pivot Ledger"
    how: "nearest kin, fold-refused — the change order executes an authorized delta, the pivot executes an interpretation under canon constraints; distinct data model and checker"
type: orchestration-pattern
---

## The Change-Order Ledger

**Status:** working · primitives-proven. **Repairs applied:** the Practitioner's two catches are structural. First, "files touched by a specific sheet" is unknowable in a shared workspace — so each work sheet writes an isolated `outputs/{sheet_id}/` directory and the scope check asserts over that directory alone (never `git status` over a workspace concurrent sheets are also writing). Second, "run-trigger side effects" that "deterministically append" authority were hand-waving: the ledger has exactly one writer stage, and *authority is authorship-time configuration* — an append records a disposition already made by a configured authority (a cadenza directive, a hold-point signature); the append itself never grants authority. Chain-walk integrity (jq + sha256, exit 1 on any break) is checkable by any consumer via ordinary file facts.

**Core Dynamic.** The architect's napkin sketch is not a change order. A change order is a typed, priced, signed instrument naming the scope delta, the authority that ordered it, and an `effective_from` boundary — written *before* downstream sheets consume the change. A sheet executing behavior not covered by the current ledger state is out of scope, full stop. The ledger is for changes that alter *what work is authorized* (scope, tolerance, datum version, target set) — not observations; scope it or drown in it.

**Sentinels.** A: a sheet writing a file authorized only under a *future* `effective_from` fails, naming the file and the not-yet-effective entry id. B: delete a mid-sequence entry → the chain walk breaks at the gap, exits 1 naming the orphan.

**Example.** Data-pipeline remediation score: mid-run, a cadenza narrows the authorized table set after a privacy finding; the change order (authority: the composer, effective_from: sheet 14) means sheet 17's touch of a now-unauthorized table fails its scope check loudly — instead of quietly doing what it was told three days ago by a version of the plan that no longer exists.

### Review Integration

Integrated from discover pass 2 (cycle 7) after three adversarial reviews (Practitioner, Skeptic, Newcomer); this pattern's specific repairs are itemized in `discover-pass-2/06-the-corpus.md` § Review Integration and the Reconciliation Appendix.
