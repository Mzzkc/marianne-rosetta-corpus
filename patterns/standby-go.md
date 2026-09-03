---
name: Standby–GO
scale: communication
status: working
forces:
- Progressive Commitment
- Exponential Defect Cost
generators:
- Incremental Exposure
problem: A one-phase cue discovers receiver readiness at the moment of irreversible execution.
signals:
- preparation must overlap live performance and the switch must be atomic
- content freeze to publish cutover; staging to production rotation; cache rebuild under traffic
- build buffer B while buffer A serves
stages:
- name: serve-A
  sheets: 1
  instrument_guidance: claude-code or codex-cli — the live consumer — pinned to the buffer named by current
  fallback_friendly: true
  purpose: Keep serving from frozen buffer A.
  artifacts: []
- name: prep-B
  sheets: fan_out(4)
  instrument_guidance: claude-code or codex-cli — N departments, any instruments; each builds into buffer-B/ and writes ready-{dept}.json
  fallback_friendly: true
  purpose: Build the replacement in parallel; each completion is an ack.
  artifacts: []
- name: arm-gate
  sheets: 1
  instrument_guidance: any-wrapped CLI profile — verifies the COMPLETE ack set and every B-artifact validating
  fallback_friendly: false
  purpose: Write armed-{cue}.json only when every department has armed.
  artifacts: []
- name: go
  sheets: 1
  instrument_guidance: any-wrapped CLI profile — the atomic switchover; refuses unless armed, refuses on duplicate cue
  fallback_friendly: false
  purpose: Flip the current pointer in one mv-class operation; log GO {cue}.
  artifacts: []
dependencies:
  prep-B:
  - serve-A
  arm-gate:
  - prep-B
  go:
  - arm-gate
composes_with:
- pattern: First Article Characterization
  how: prerequisite — characterize buffer B before arming
- pattern: Hutchinson's Warning
  how: substitution — the hold is degradation rung zero
type: orchestration-pattern
---

## Standby–GO


**Status:** Working. **Source:** stage-management calling discipline; cue lights; scene-change double buffers. **Structure per Review 2** (theatre color demoted): two-phase cueing — arm with complete ack set, then one irreversible addressed fire.

**Core Dynamic.** The arm (standby) is collective and acknowledged: it does not proceed until every department that must move has said so. The fire (GO) is individual, unacknowledged, and irreversible — all uncertainty is spent during the arm so the trigger can be instant. A missing acknowledgement does not fire a partial cue: the system *holds* — the current scene keeps running, degraded but alive — until the ack set completes or the hold escalates. A GO cannot be duplicated because it is addressed: the cue log already contains GO 45; a second GO 45 halts rather than re-executes.

**When to use:** anywhere preparation must overlap live performance and the switch must be atomic.

**When NOT to use:** the switch is cheap and reversible — the ceremony is overhead; just swap. Departments cannot report readiness truthfully: an arm answered by reflex spends the safety margin on a lie.

**Marianne Score Structure**

```yaml
movements:
  1: { name: serve-A }
  2: { name: prep-B }
  3: { name: arm-gate, instrument: cli }
  4: { name: go, instrument: cli }
  5: { name: serve-B }

sheet:
  total_items: 5
  fan_out: { 2: 4 }                        # four departments: extraction, assets, links, index
  dependencies: { 2: [1], 3: [2], 4: [3], 5: [4] }
  per_sheet_fallbacks: { 3: [], 4: [] }    # the gates never degrade
  skip_when:
    5: { command: 'test "$(readlink {workspace}/current)" != "{workspace}/buffer-B"' }
                                           # the consumer cannot race ahead of the pointer
                                           # (skip_when takes a COMMAND — the expression form
                                           # was never evaluated and is rejected by the engine)

prompt:
  template: |
    {% if stage == 1 %}
    Serve from {{ workspace }}/buffer-A (now frozen). Report health.
    {% elif stage == 2 %}
    Department {{ instance }}: build your artifact into {{ workspace }}/buffer-B/dep{{ instance }}/.
    On completion write {{ workspace }}/buffer-B/ready-{{ instance }}.json. If you cannot complete,
    write nothing — a missing ack holds the cue.
    {% elif stage == 3 %}
    bash "{score_dir}/scripts/arm-gate.sh" "{{ workspace }}/buffer-B" --cue 45 \
      --require-ready 4 --validate-artifacts
    {% elif stage == 4 %}
    bash "{score_dir}/scripts/go.sh" "{{ workspace }}" --cue 45 \
      # refuses unless armed-45.json exists with the full ack list;
      # refuses if GO 45 already appears in cue-log.jsonl; else: mv current.next current
    {% elif stage == 5 %}
    Serve from {{ workspace }}/buffer-B (now frozen). Report health.
    {% endif %}

validations:
  - type: command_succeeds
    command: 'test "$(ls {workspace}/buffer-B/ready-*.json | wc -l)" -eq 4'
    condition: "stage == 3"
  - type: file_exists
    path: "{workspace}/armed-45.json"
    condition: "stage == 3"
  - type: command_succeeds
    command: 'grep -c "GO 45" {workspace}/cue-log.jsonl | grep -qx 1'
    condition: "stage == 4"                # the GO fired exactly once
```

**Failure wiring:** hold timeout is `max_wall_seconds` on the arm gate — if the ack set never completes, the score fails *with A still serving*: degraded, safe, escalated.

**Near-miss:** a "ready?" poll in chat then a manual deploy — the arm without a deterministic ack gate is a shout with typing indicators.

**Example.** A documentation site rebuild under live traffic. A failing link checker holds the GO (old site keeps serving); at hold timeout the operator learns which department never armed. No half-rebuilt site is ever served.

### Review Integration

Review 2 reduced the metaphor to a two-phase arm/fire protocol. Review 3 required runnable score dialect and command-form readiness checks; Sighted Versions survives as the promotion-authority and visibility-ledger seam. During split curation, the monolith's G1–G6 draft label was mapped to the nearest generator in forces.md, and every stage now names a current profile: deterministic stages use an any-wrapped CLI profile; judgment stages name claude-code, codex-cli, or opencode as appropriate.
