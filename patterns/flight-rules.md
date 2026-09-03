---
name: Flight Rules
scale: adaptation
status: working
forces:
- Exponential Defect Cost
- Accumulated Signal
generators:
- Incremental Exposure
- Accumulate Knowledge
problem: 'Under failure, deliberation is the enemy: the response is re-derived under duress instead of looked up from pre-negotiated, versioned condition-action bindings.'
signals:
- the same failures recur and the correct response is knowable in advance
- incident response, failure recovery, go/no-go criteria
- a responder who reasons for ten minutes where reading for ten seconds would do
stages:
- name: rule-corpus
  sheets: 1
  instrument_guidance: claude-code or codex-cli — any AI instrument — authors one YAML per rule under change control
  fallback_friendly: true
  purpose: 'Maintain the rule corpus: id, machine-checkable condition, action, rationale, effectivity, revision history.'
  artifacts: []
- name: handler
  sheets: 1
  instrument_guidance: claude-code or codex-cli — AI matching confined to signature PROPOSAL; deterministic selection for high-risk classes
  fallback_friendly: true
  purpose: Match the failure signature; execute; CITE rule IDs in output.
  artifacts: []
- name: change-board
  sheets: 1
  instrument_guidance: any-wrapped CLI profile — serialized board applies deltas as new versions
  fallback_friendly: false
  purpose: Rule deltas from every incident; never edit history.
  artifacts: []
dependencies:
  handler:
  - rule-corpus
  change-board:
  - handler
composes_with:
- pattern: The Black-Box Ledger
  how: prerequisite — the packet's failure signature feeds the matcher
- pattern: The MIST Card
  how: prerequisite — a rule action colliding with a recorded failed remedy is a rule-delta signal
- pattern: After-Action Review (v4 archive)
  how: prerequisite — the AAR's output artifact becomes the delta
type: orchestration-pattern
---

## Flight Rules


**Status:** Working. **Source:** NASA flight rulebook; Apollo 12 "SCE to AUX"; launch commit criteria; nuclear symptom-based procedures.

**Core Dynamic.** The move relocates the decision: **negotiate condition→action bindings while everyone is calm and informed, review them formally, version them — and at failure time look up rather than reason.** Authority flows from the rule's provenance (reviewed, signed, numbered), not from the responder's confidence. The rulebook is a living document under change control: the output of every After-Action Review is not a resolution, it is a **rule delta** through a board. Not an escalation ladder (the ladder routes *who* decides; the rule pre-decided *what*), not a gate (a gate checks work; a rule binds a response to a condition).

**Deterministic selection (Review 2):** for high-risk incident classes, rule selection must be deterministic — the runtime path may use an AI handler to *propose* signatures, but the binding `condition → rule` is matched by the rule engine (machine-checkable conditions: error class, stage, retry count), never by judgment under duress.

**When to use:** incident response, failure recovery, go/no-go criteria — anywhere the same failures recur and the correct response is knowable in advance.

**When NOT to use:** rules are ambiguous or contradictory — two matched rules at failure time is worse than none (contradiction review at the change board is mandatory). Coverage gaps force improvisation anyway — every gap found in an incident must become a rule or it stays. The responder reasons past the rule — mitigate by making the rule's action deterministic where possible. Rules rot against a config that moved on — version-pin rules to the configuration they were written against.

**Marianne Score Structure**

```yaml
spec:
  spec_dir: "{score_dir}/rules"
  spec_tags: { 2: [flight-rules] }        # only the applicable subset enters the responder's context

movements:
  1: { name: rule-corpus }
  2: { name: handler }
  3: { name: change-board, instrument: cli }

sheet:
  total_items: 3
  dependencies: { 2: [1], 3: [2] }
  per_sheet_fallbacks: { 3: [] }

prompt:
  template: |
    {% if stage == 1 %}
    Author rule YAML into {{ workspace }}/rules/: {id: FR-114, condition:
    {error_class, stage, retry_count}, action: <deterministic command>, rationale,
    effectivity: <config/score version>, revision}. One file per rule.
    {% elif stage == 2 %}
    The flight-rules corpus is in your context. Match the failure signature in
    {{ workspace }}/failure-packet/ to rules. Execute the matched action. CITE rule IDs
    verbatim in your output — a fabricated citation fails the run (see validations).
    {% elif stage == 3 %}
    bash "{score_dir}/scripts/rule-board.sh" "{{ workspace }}/rule-deltas/" \
      --apply-as-new-versions --contradiction-review
    {% endif %}

validations:
  # THE source-validation, shown concretely (Review 3): every cited rule ID must
  # exist verbatim in the rule corpus — a fabricated rule citation fails the run.
  - type: command_succeeds
    command: 'grep -hoE "FR-[0-9]+" {workspace}/handler-output.md | sort -u | while read id; do grep -rq "id: $id" {score_dir}/rules/ || exit 1; done'
    condition: "stage == 2"
  - type: content_regex
    pattern: "FR-[0-9]+"
    path: "{workspace}/handler-output.md"
    condition: "stage == 2"
  - type: command_succeeds
    command: 'bash {score_dir}/scripts/rule-board.sh {workspace}/rule-deltas --check-only'
    condition: "stage == 3"
```

**Near-miss:** a wiki page of best practices — unversioned, unmatched, uncited; prose where a rulebook should be.

**Example.** An e-commerce release concert with pre-negotiated rollback rules: "if checkout conversion drops >15% for 10 minutes post-deploy → auto-rollback; if payments latency p99 > 2s → freeze rollout, escalate." The 3 AM responder executes FR-207; nobody debates thresholds at 3 AM.

### Review Integration

Review 2 confined AI to signature proposal and made high-risk rule selection deterministic. Review 3 required a concrete source check for every cited rule ID. During split curation, the monolith's G1–G6 draft label was mapped to the nearest generator in forces.md, and every stage now names a current profile: deterministic stages use an any-wrapped CLI profile; judgment stages name claude-code, codex-cli, or opencode as appropriate.
