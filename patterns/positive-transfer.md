---
name: Positive Transfer
scale: communication
status: working
forces:
- Partial Failure
- Information Asymmetry
generators:
- Exploit Failure as Signal
problem: Work moving between executors passes through moments with no owner, and a failed handoff silently drops custody.
signals:
- work crossing a trust boundary — different instruments, scores, or teams
- the cost of a moment without an owner exceeds the cost of a moment with two
- shift boundaries, score-to-score chains, escalation from worker to human
stages:
- name: offer
  sheets: 1
  instrument_guidance: claude-code or codex-cli — the sender — any AI instrument; must prepare the offer while CONTINUING to own the item
  fallback_friendly: true
  purpose: Write handoff-{id}.json in state offered; retain ownership.
  artifacts: []
- name: accept
  sheets: 1
  instrument_guidance: claude-code or codex-cli — the receiver — different instrument or score; writes acceptance, may inspect but NOT mutate until release
  fallback_friendly: true
  purpose: Positively accept; keyed to the handoff's identity so a duplicate cue is a no-op.
  artifacts: []
- name: gate
  sheets: 1
  instrument_guidance: any-wrapped CLI profile — the ledger state machine IS the pattern's enforcement
  fallback_friendly: false
  purpose: Assert release > acceptance > offer, no regressions, no released-without-accepted.
  artifacts: []
dependencies:
  accept:
  - offer
  gate:
  - accept
composes_with:
- pattern: Canon of Phases
  how: layering — the rotation's boundary contains this dialogue compressed
- pattern: Black-Box Ledger
  how: prerequisite — unaccepted offers feed the failure packet
type: orchestration-pattern
---

## Positive Transfer


**Status:** Working. **Source:** FAA JO 7110.65 radar handoff; AORN relief counts; follow-the-sun handoff.

**Core Dynamic.** A relay baton is a bad idea: there is a measurable moment when neither runner owns it. Positive transfer refuses that moment structurally. The sender *offers*; the receiver must positively *accept*; until acceptance completes, the sender still owns the item and still works it. The item always has at least one owner and, during overlap, exactly two. The deadline is a place, not a number — the sector boundary the aircraft reaches on its own schedule. When the cue is lost entirely, the system holds the last acknowledged state conservatively and degrades loudly rather than guessing. Acceptance is keyed to the handoff's identity, so a duplicated cue is a no-op.

**The overlap write rule (Review 2):** during `offered`/`accepted` overlap, **the outgoing owner retains operational authority; the incoming owner may inspect and acknowledge only** — or both write to separate ledger fields. "Exactly two owners" with two writers is a corruption window, not a safety property.

**The sender-survives precondition, answered structurally (Review 3):** a finished sheet is gone, but ownership is a property of the *ledger*, not the liveness of the executor. The offer lives in workspace state; the hold is bounded by `max_wall_seconds` and the leased schedule; a hold timeout routes to `on_failure` escalation; and the release write is made by the sender score's next invocation (self-chain) or by a deterministic gate observing acceptance. The ledger tolerates `offered`-without-`release` indefinitely without ever having zero owners — that is the point.

**When to use:** whenever work moves between executors that are not the same trust domain and the cost of a moment without an owner exceeds the cost of a moment with two.

**When NOT to use:** both parties share one mutable state and see each other's writes directly — the dialogue becomes theater. The sender cannot hold in any sense (ephemeral workspace, no escalation route) — positive acceptance degrades back to baton-throwing.

**Marianne Score Structure**

```yaml
movements:
  1: { name: work-and-offer }
  2: { name: receive-and-accept }
  3: { name: handoff-gate, instrument: cli }

sheet:
  total_items: 3
  dependencies: { 2: [1], 3: [2] }
  per_sheet_fallbacks:
    3: []

cross_sheet:
  capture_files: ["handoff-*.json"]     # the ledger is the only inter-stage channel

prompt:
  template: |
    {% if stage == 1 %}
    Work the item. Then write {{ workspace }}/handoff-item17.json:
    {id, state: offered, payload, offered_utc}. You RETAIN ownership until acceptance
    is observed. Do not delete or mutate the payload after offering.
    {% elif stage == 2 %}
    Read {{ workspace }}/handoff-item17.json. You may INSPECT the payload but may NOT
    mutate it until release. If you take the item, append {state: accepted, accepted_utc}
    to the same file.
    {% elif stage == 3 %}
    bash "{score_dir}/scripts/handoff-gate.sh" "{{ workspace }}/handoff-item17.json"
    {% endif %}

validations:
  - type: command_succeeds
    # fails unless: release_ts > acceptance_ts > offer_ts, no regressions,
    # no released-without-accepted, exactly one acceptance row per handoff id
    command: 'bash {score_dir}/scripts/handoff-gate.sh --state-machine "{workspace}/handoff-item17.json"'
    condition: "stage == 3"
```

**Near-miss:** an "FYI" handoff note — notification without acceptance is baton-throwing with paperwork.

**Example.** A drafting score produces an article; a separate compliance score must take it over. Without positive transfer, the article sits in a directory between jobs, owned by no one, silently rotting when compliance fails to launch. With the ledger, a failed compliance launch leaves the article in `offered`, the drafting score's hold timeout fires, and a human gets a custody report instead of a gap.

### Review Integration

Review 2 imposed a single-writer overlap rule. Review 3 required the durable handoff ledger, lease expiry, and timeout escalation so sender completion cannot erase custody. During split curation, the monolith's G1–G6 draft label was mapped to the nearest generator in forces.md, and every stage now names a current profile: deterministic stages use an any-wrapped CLI profile; judgment stages name claude-code, codex-cli, or opencode as appropriate.
