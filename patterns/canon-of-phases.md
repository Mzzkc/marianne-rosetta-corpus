---
name: Canon of Phases
scale: concert-level
status: working
forces:
- Partial Failure
- Finite Resources
generators:
- Exploit Failure as Signal
- Contract at Interfaces
problem: A continuous stream of work outlives any single worker's endurance — context, budget, or lease — and restarts from zero at every boundary.
signals:
- an always-on triage queue, rolling literature watch, moderation across a day, long migrations in shifts
- the stream must never restart from zero
- no single score should run for a day straight
stages:
- name: accept
  sheets: 1
  instrument_guidance: claude-code or codex-cli — interchangeable with the other phases — the SAME part; instrument diversity is a DEFECT here
  fallback_friendly: true
  purpose: Read the latest handoff packet; verify beat continuity; write accepted-through. No packet and not rotation zero = STOP.
  artifacts: []
- name: work
  sheets: 1
  instrument_guidance: claude-code or codex-cli — same instrument as every other phase — interchangeability is the design
  fallback_friendly: true
  purpose: Process queue items from the packet's cursor to this phase's soft stop.
  artifacts: []
- name: hand-off
  sheets: 1
  instrument_guidance: claude-code or codex-cli — same instrument; writes the packet
  fallback_friendly: true
  purpose: Write open items, in-flight state, last beat, cursor, incident notes.
  artifacts: []
dependencies:
  work:
  - accept
  hand-off:
  - work
composes_with:
- pattern: Positive Transfer
  how: layering — the boundary contains the transfer dialogue compressed into one packet
- pattern: Replication Licensing
  how: layering — the packet boundary carries license state
type: orchestration-pattern
---

## Canon of Phases


**Status:** Working. **Source:** canon/round form; follow-the-sun operations; nursing shift change. Resurrects v4's Stretto Entry from Awaiting Primitives — executable now precisely because leased recurrence, `overlap: skip`, and IANA timezones exist. **Kept per Review 1 (buildable) with the independence argument Review 2 demanded stated outright, and the deployment topology Review 1 asked for written down.**

**Independence from its parts:** this is not merely Positive Transfer plus leased recurrence. Positive Transfer is a *pairwise executor handoff with an overlap dialogue* — two known counterparties negotiate at a boundary. Canon of Phases is *scheduled rotation of an unbounded stream* by *interchangeable* workers: phases never meet, there is no overlap dialogue, and the packet — not a conversation — is the entire inter-phase channel, deliberately, so the seam is inspectable. Uniquely, this pattern *forbids* instrument diversity: the canon's voices are the same part; divergence is a defect (the one sign-flip in the corpus — every other convergence harvests heterogeneity; the rotating stream needs interchangeability).

**Deployment topology (Review 1):** three *deployments* of one score — each with its own IANA timezone, its own workspace, sharing one packet path — not three instances of one job. The score and its deployment are different objects; the regional fleet is the latter.

**When to use:** continuous work with mortal workers.

**When NOT to use:** the work is finite (a canon for a 40-minute task is two musicians for one chair). Phases cannot be made near-interchangeable — if phase 2's work is genuinely different work, this is a pipeline wearing a costume, and the pipeline should say so.

**Marianne Score Structure**

```yaml
schedule:
  cron: "0 */8 * * *"
  timezone: "Europe/Amsterdam"       # per-deployment: the boundary lands at the LOCAL shift start
  overlap: skip                      # the lease is the fence: the same phase cannot doubly instantiate
  misfire: skip

movements:
  1: { name: accept }
  2: { name: work }
  3: { name: hand-off }

sheet:
  total_items: 3
  dependencies: { 2: [1], 3: [2] }   # NO dependencies between phases — they are scheduled
                                     # apart, not DAG-ordered; the packet is the only channel
prompt:
  template: |
    {% if stage == 1 %}
    Read {{ workspace }}/handoff-packet.json. Verify integrity: beat continuity, queue cursor.
    If no packet exists and this is NOT rotation zero (see {{ workspace }}/rotation-state.json),
    STOP — an undocumented empty queue is a lost cue, not a fresh start.
    Else write accepted-through with your timestamp. Custody before work.
    {% elif stage == 2 %}
    Process queue items from the packet's cursor to your soft stop. Do not exceed the beat.
    {% elif stage == 3 %}
    Write {{ workspace }}/handoff-packet.json: open items, in-flight state, last beat,
    cursor, incident notes. Append-only across rotations — a phase that rewound the cursor halts.
    {% endif %}

validations:
  - type: command_succeeds
    # custody before work: packet exists AND accepted-through predates this phase's results
    command: 'bash {score_dir}/scripts/packet-gate.sh {workspace}/handoff-packet.json --accepted-before-results --monotonic-beat'
    condition: "stage == 1"
  - type: file_exists
    path: "{workspace}/handoff-packet.json"
    condition: "stage == 3"
```

**Near-miss:** a shared directory with no packet — phases that share a filesystem but not state restart the melody nightly and call it continuity.

**Example.** Round-the-clock alert triage: phase EU works 08:00–16:00 Europe/Amsterdam, NA and APAC likewise — three deployments of one score, each leased 8h, each accepting the packet before working. A 03:00 incident is worked continuously, and the morning report is written by a phase that *knows what the night phase saw* — not by one that merely shares a directory with it.

### Review Integration

Review 1 required an executable three-deployment topology. Reviews 2 and 3 required the independence argument: positive transfer plus recurrence creates rotation across deployments, not merely three instances in one job. Stretto Entry is the awaiting-era ancestor. During split curation, the monolith's G1–G6 draft label was mapped to the nearest generator in forces.md, and every stage now names a current profile: deterministic stages use an any-wrapped CLI profile; judgment stages name claude-code, codex-cli, or opencode as appropriate.
