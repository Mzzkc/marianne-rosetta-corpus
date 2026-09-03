---
name: The Fencing Token
scale: adaptation
status: working
forces:
- Partial Failure
- Progressive Commitment
generators:
- Exploit Failure as Signal
- Incremental Exposure
problem: A paused or retried executor cannot observe its own expiry and silently overwrites newer work with older, slower work.
signals:
- a shared mutable surface two sequenced executors may touch
- workspace regions republished by a retry after timeout
- scheduled jobs whose lease lapsed while the job kept running
stages:
- name: grant
  sheets: 1
  instrument_guidance: any-wrapped CLI profile — atomically increments the counter and stamps run identity
  fallback_friendly: false
  purpose: Issue the monotonic token as a workspace file.
  artifacts: []
- name: guarded-work
  sheets: 1
  instrument_guidance: claude-code or codex-cli — any AI instrument; reads the token FILE and embeds it in every artifact manifest
  fallback_friendly: true
  purpose: Do the work with the token embedded in outputs.
  artifacts: []
- name: admit-gate
  sheets: 1
  instrument_guidance: any-wrapped CLI profile — compares embedded token against the current counter
  fallback_friendly: false
  purpose: Reject stale writes at the boundary.
  artifacts: []
dependencies:
  guarded-work:
  - grant
  admit-gate:
  - guarded-work
composes_with:
- pattern: Self-Stabilizing Custody
  how: layering — bounds the convergence window's misbehavior
- pattern: Replication Licensing
  how: 'substitution — same family (physical authority), different primitive: ordering defense vs exactly-once consumption (seam stated in both)'
type: orchestration-pattern
---

## The Fencing Token


**Status:** Working. **Source:** Kleppmann's distributed-locking analysis; ZooKeeper zxid; Chubby sequencers; K8s resourceVersion. **Restated per Review 1:** the token reaches the sheet as a **file the grant stage writes and the prompt cites** — not "runtime variables."

**Core Dynamic.** A lease grants authority for *time*, not forever — and the holder is structurally incapable of knowing when its authority died, because a paused process cannot observe its own expiry. The fencing token moves the correctness burden from the holder (who cannot know) to the shared substrate (who can count): every grant carries a monotonically increasing number, and the storage all writers must touch *rejects any write bearing a token lower than the highest it has seen*. Zombies exist — GC pauses, rate-limit stalls, retries, context compaction — but zombie *writes* need not. The proof-theoretic move: make an unsound inference inadmissible rather than trying to prevent the prover from committing it.

**The seam against Replication Licensing (Review 3's don't-duplicate demand, justified):** fencing defends *ordering* on a shared mutable surface — many writes may be attempted, stale ones are rejected; licensing defends *exactly-once side-effect authorization* per cycle — the authority is consumed by the act of beginning, and recovery can tell never-started from started-died. One counters zombies; the other counters re-execution. They compose; they are not the same word.

**When to use:** any shared mutable surface two sequenced executors may touch. In AI orchestration, a holder paused while its replacement starts is the *normal* case, not the exception.

**When NOT to use:** no shared point of serialization can check tokens (pure peer-to-peer side effects); no monotonic counter authority exists; work is read-only or commutative so a zombie write is harmless; single-writer serial stages whose DAG position already excludes overlap by construction.

**Marianne Score Structure**

```yaml
movements:
  1: { name: grant, instrument: cli }
  2: { name: guarded-work }
  3: { name: admit-gate, instrument: cli }

sheet:
  total_items: 3
  dependencies: { 2: [1], 3: [2] }
  per_sheet_fallbacks: { 1: [], 3: [] }

prompt:
  template: |
    {% if stage == 1 %}
    bash "{score_dir}/scripts/token-grant.sh" "{{ workspace }}/lease.token" --increment --stamp-run-id
    {% elif stage == 2 %}
    Your token is in {{ workspace }}/lease.token (written by the grant stage — read the FILE).
    Embed "token: <number>" in every output manifest you write. Mutations without a token
    are inadmissible downstream.
    {% elif stage == 3 %}
    bash "{score_dir}/scripts/token-admit.sh" "{{ workspace }}/lease.token" "{{ workspace }}/out/" \
      --reject-stale    # exit nonzero on any artifact whose token < current counter
    {% endif %}

validations:
  - type: content_regex
    pattern: "token: [0-9]+"
    path: "{workspace}/out/manifest.json"
    condition: "stage == 2"
  - type: command_succeeds
    command: 'bash {score_dir}/scripts/token-admit.sh {workspace}/lease.token {workspace}/out --check-only'
    condition: "stage == 3"
```

`max_wall_seconds` on the guarded-work movement acts as the lease TTL — expiry enforced by the envelope, staleness by the gate.

**Near-miss:** checking "am I still the leader?" before writing — the holder cannot observe its own expiry; that inability is precisely the bug the token moves elsewhere.

**Example.** A pricing-catalog pipeline: sheet A regenerates the catalog, stalls on a rate limit; the retry spawns A′ which republishes. When A wakes and writes, the publish directory's gate finds token 33 against current 34 and rejects A's copy — no silent overwrite of newer work by older, slower work.

### Review Integration

Review 1 replaced fictional runtime-variable delivery with a workspace token file embedded in every output. Review 3 separated stale-write ordering from Replication Licensing's single-use authority. Timekeeper's Ledger is absorbed as the epoch-fenced pulse form of the same family: the counter advances monotonically and every pulse carries the epoch that authorized it. During split curation, the monolith's G1–G6 draft label was mapped to the nearest generator in forces.md, and every stage now names a current profile: deterministic stages use an any-wrapped CLI profile; judgment stages name claude-code, codex-cli, or opencode as appropriate.
