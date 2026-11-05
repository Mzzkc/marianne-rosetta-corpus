---
name: "The Cue Light"
scale: communication
status: working
forces: [Information Asymmetry, Partial Failure, Progressive Commitment]
generators: [Threshold-Triggered Switch, Incremental Exposure]
problem: "A parent score must change the behavior of already-running or later-starting siblings without blocking them on a decision that is not yet made."
signals:
  - "a late decision (human sign-off, slow validation) must stall commits but not work"
  - "already-running siblings need a mode switch (degraded mode, budget-red, publish-authorized), not a briefing"
  - "consumers must be provably aware of the cue before the irreversible step fires"
stages:
  - name: arm
    sheets: 1
    instrument_guidance: "any-wrapped CLI profile — writes the cue artifact when the upstream condition fires"
    fallback_friendly: false
    purpose: "Publish standby + cue_id + cycle (monotone counter) without firing."
  - name: draft
    sheets: fan_out(N)
    instrument_guidance: "consumer instruments per the work; each writes drafts/{sheet}/ and its own acks/{sheet}.ack"
    fallback_friendly: true
    purpose: "Produce and hold work warm; ack readiness without committing."
  - name: go-gate
    sheets: 1
    instrument_guidance: "any-wrapped CLI profile — jq counts acks/{consumer}.ack against the named cue set; flips state to go only on completeness"
    fallback_friendly: false
    purpose: "The complete-ack gate; absent or incomplete ack set holds standby and exits nonzero."
  - name: commit
    sheets: fan_out(N)
    instrument_guidance: "consumer instruments; commit wrappers run after the go flip"
    fallback_friendly: true
    purpose: "Finalize held drafts once the cue is GO."
dependencies:
  go-gate: [arm, draft]
  commit: [go-gate]
composes_with:
  - pattern: "Standby–GO"
    how: "parent — the Cue Light is Standby–GO's arm/ack/hold/fire machine; see inheritance note"
  - pattern: "The Watchman's Gate"
    how: "pick.json is a one-bit cue with a digest; same polarity law"
  - pattern: "The Graded Ladder"
    how: "a cue that times out on its ack set escalates — the light supplies the ladder's non-blocking trigger surface"
  - pattern: "The Contamination Wire"
    how: "a poison verdict rides the cue artifact for deterministic consumers"
  - pattern: "The Sealed Dissent"
    how: "a consumer may ack under protest; dissent rides the ack channel"
type: orchestration-pattern
---

## The Cue Light

**Status:** working · primitives-proven (pattern-unproven). **Inheritance (the Newcomer's finding, now on the face):** this pattern is a **confirmation + extension of Standby–GO** (`patterns/standby-go.md`, permanent since Sep 3). Inherited: collective acknowledged arm; deterministic complete-ack gate; missing ack holds the cue; then fire. Extended: (1) the monotone `cycle` counter — the freshness fact, so a consumer can never act on a stale light; (2) broadcast-polled semantics — the light changes what *already-running siblings* do, versus Standby–GO's addressed irreversible fire; (3) non-blocking consumers — work proceeds under standby; only commits wait.

**Core Dynamic.** One bit, broadcast, polled — a schema so small it cannot be misread, and an ack set so structured it cannot be forged by prose. The publisher writes `{workspace}/cue/{name}.yaml` with `state ∈ {arm, standby, go, clear}`, `cue_id`, and `cycle`. Consumers ack by writing their **own file** (`acks/{consumer}.ack`, containing sheet id + cycle observed) — never by appending to a shared array, which is a lost-update race under concurrent writers (the Practitioner's structural fix). The go-gate is a CLI sheet whose *validation* is the ack-completeness count: a cue with a missing ack stays `standby` and the gate exits nonzero — the GO must not fire on an incomplete ack set.

**Marianne Score Structure.** Four stages as in frontmatter. The go flip is atomic: write `cue.next.yaml`, then `mv` over the current file (write-temp-then-rename — the concurrency doctrine). Consumers do **not** poll inside a running sheet (a sheet is a discrete execution unit; an in-sheet poll burns timeout budget — the Practitioner's catch): the protocol is draft-stage consumers that finish, ack, and exit; commit-stage wrappers whose `skip_when` is a refusal predicate (`skip_when: 'jq -e ''.state == "standby" or .state == "clear"'' {workspace}/cue/{name}.yaml'` — skip while not GO; V1-fail-open is survivable because the gate already refused loudly). Validations: `content_regex` on the state field `^(arm|standby|go|clear)$` (the draft's regex omitted `arm` — fixed, the Newcomer's catch); `command_succeeds` on the go-gate's ack count. **Sentinel:** a cue whose consumer never acks must leave `state: standby`, the consumer absent from `acks/`, and the go-gate exiting nonzero — no GO ever written.

**Example.** Product-launch pipeline: 8 sheets produce materials concurrently; legal sign-off is the cue. Materials finish, write their ack files, hold publication; legal's approval lands; the go-gate verifies all 8 acks and flips GO; all 8 commit within their own cadence — the launch waits for legal, legal waits for no one.

### Review Integration

Integrated from discover pass 2 (cycle 7) after three adversarial reviews (Practitioner, Skeptic, Newcomer); this pattern's specific repairs are itemized in `discover-pass-2/06-the-corpus.md` § Review Integration and the Reconciliation Appendix.
