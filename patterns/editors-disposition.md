---
name: "The Editor's Disposition"
scale: score-level
status: approximation
forces: [Structured Disagreement, Partial Failure]
generators: [Threshold-Triggered Switch]
problem: "Multi-advisory fan-ins fail by advice-drowning or advice-collapse because 'what did the reviewers think?' and 'what do we do?' are conflated into one act."
signals:
  - "multiple independent evaluations must produce ONE action, not one document"
  - "reviewers negotiate into a mushy consensus no one endorses"
  - "authors optimize for appeasement across incompatible reviewer standards"
stages:
  - name: advise
    sheets: fan_out(2-4)
    instrument_guidance: "mixed-family reviewers; each produces a typed report (json_schema: findings[], overall_recommendation from a closed enum, confidence)"
    fallback_friendly: true
    purpose: "Independent answers to 'what is wrong?'"
  - name: respond
    sheets: 1
    instrument_guidance: "optional; Rejoinder Ledger composition — findings frozen with IDs, typed rejoinders written"
    fallback_friendly: true
    purpose: "The author's engagement with findings, typed and joinable."
  - name: dispose
    sheets: 1
    instrument_guidance: "ONE editor sheet (the unitary authority IS the pattern; fan-out there would dissolve it); response_format: json_schema forces {disposition: enum[accept, minor, major, reject], rationale citing finding-IDs, required_changes[]}"
    fallback_friendly: false
    purpose: "One accountable routing decision from a closed vocabulary — not a vote, not synthesis."
  - name: route
    sheets: 1
    instrument_guidance: "any-wrapped CLI, per_sheet_fallbacks: [] — deterministic dispatch on the disposition"
    fallback_friendly: false
    purpose: "accept → publish/merge gate; reject → dead-letter quarantine with advisories attached; minor/major → AWAITING sheet.loops proof (do not invent the loop)"
dependencies:
  respond: [advise]
  dispose: [respond]
  route: [dispose]
composes_with:
  - pattern: "Rejoinder Ledger"
    how: "findings-freeze and bijection supply the respond stage wholesale"
  - pattern: "Condorcet's Premise"
    how: "the decision-table entry this pattern owes the corpus: vote when you want the crowd's aggregated judgment; dispose when you want one accountable routing decision"
  - pattern: "Dead Letter Quarantine"
    how: "reject's destination — advisories preserved verbatim; a rejected-with-receipts artifact is curriculum, not garbage"
  - pattern: "The Dialectical Pair"
    how: "the cheap first line underneath"
type: orchestration-pattern
---

## The Editor's Disposition

**Status:** approximation — `response_format` native-unproven (V5 schema-validated per attempt, zero end-to-end executions); this is arguably the **minimal exercise** of the corpus's most-cited never-executed primitive (short outputs, closed enum, immediate mechanical check), and the prove queue's #1 item. The `minor`/`major` routes additionally await `sheet.loops` (the Skeptic: one closed route proven first — `accept` and `reject` route deterministically today; the loop routes are named as awaiting, not invented).

**Core Dynamic.** Reviewers ADVISE; the editor DISPOSES. A single agent with different authority reads the reports and issues one of a closed set of dispositions: **accept / minor revision / major revision / reject**. Not a vote (Condorcet), not content synthesis (Sugya Weave), not consensus (Delphi): a **unitary decision authority over typed advisory inputs, with a closed disposition vocabulary and a mandatory rationale citing the advisories.** The closed vocabulary is load-bearing — it prevents the editor from synthesizing a new position or averaging scores; it forces a *routing* decision. The failure semantics are distinctive: a rejected paper with excellent reviews is not a failure — it is a disposition (the Typed-Draw family, C8).

**Sentinel.** One reviewer's finding is objectively fatal and the editor disposes `accept` citing that finding-ID as "addressed" → `disposition-check.py` requires every cited-and-addressed finding to appear in rejoinders as accept+change; missing → exit 1 with `disposition-report.json` carrying `"violations": [{"type": "uncited_acceptance"}]`. This catches the capture failure — an editor laundering a fatal finding through vague rationale. The editor must be a different instrument family than reviewers AND authors (Independence Law at composition time).

**Example.** Content-release gate: three reviewers assess a draft (factual accuracy, brand voice, legal risk) with typed findings; the editor disposes — major revision (legal findings load-bearing) — and the route sends only the legal-flagged sections to re-review, not the whole draft. Without the disposition split, the draft oscillates between three reviewers' incompatible standards for three cycles.

### Review Integration

Integrated from discover pass 2 (cycle 7) after three adversarial reviews (Practitioner, Skeptic, Newcomer); this pattern's specific repairs are itemized in `discover-pass-2/06-the-corpus.md` § Review Integration and the Reconciliation Appendix.
