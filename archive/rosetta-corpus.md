# The Rosetta Pattern Corpus — v5.1 (Final, post-adversarial-review)

**Iteration:** 5, revision 1 — the v5 draft after three adversarial reviews (Practitioner, Skeptic, Newcomer), all three of which returned **Needs revision**; this document is the integration.
**Core patterns:** 21 (down from the draft's 25 — see Review Integration).
**Foundational primitives:** 2 (Fan-out + Synthesis; The Tool Chain, restated as the Etiquette Law).
**Candidate pool:** 47 patterns from six disjoint iteration-5 expeditions (Builder, Gardener, Dancer, Reasoner, Commander, Storyteller), collided; plus the 56-pattern v4 bestiary, all of which appear in this document (Appendix A) with frontmatter.
**Convergences:** 10 structural moves (C1–C10), each now with a structural identity table (state variables, authority, medium, deterministic check, failure transition, non-example).
**Generators:** 6 (G1–G6), subsuming v4's Ten Forces.
**Status of this document:** FINAL for iteration 5. Every curation decision below was attacked by three reviewers and either survived, was cut, or was strengthened; the disposition of each is recorded in Review Integration. Score structures are written in the dialect the engine actually accepts (see The Real Dialect).

---

## Review Integration

Three adversarial reviews attacked `04-draft-corpus.md`. Review 1 (The Practitioner) verified every load-bearing YAML field against the engine source. Review 2 (The Skeptic) applied a structural-identity test: a pattern survives only if it states state variables, authority holder, communication medium, deterministic check, and failure transition. Review 3 (The Newcomer) asked whether someone who just ran `hello.yaml` could use the document. All three verdicts: **Needs revision.** Here is what changed.

### Cut from core → Patterns Awaiting Primitives (2)

**Zeitgeber Entrainment** — cut by consensus. Review 1: "`ScheduleConfig` (orchestration.py:34) supports cron/interval/timezone/overlap/misfire/jitter. There is no offset-from-artifact scheduling." Review 3: "no such primitive exists. This is precisely the 'Awaiting Primitives' sin v4 was purged for, smuggled back into the core." The pattern collapses onto real primitives: a leased `schedule`, a heartbeat artifact, a staleness gate (`skip_when` command form), and skip-to-next-cue — never a catch-up burst. That collapsed form is documented under Awaiting Primitives with its different failure modes and costs stated, exactly as Review 1 required. The name and the biology lecture go with it.

**The Accountability Board** — cut from core by Review 1 ("no score-facing export of the claim table with PIDs exists or is named... Stage 3's reconciliation sweep has nothing to sweep"), reclassified by Review 3 as "substrate documentation dressed as score patterns." Review 2's structural reframing is adopted and preserved: the pattern is a **registry-plus-probe loop** — claimed resources periodically reconciled against physical handles and semantic completion predicates — and its three conflated concerns (human roll call, process-table reconciliation, semantic result custody) are now separated. It lives in two places: the substrate-documentation section (the engine's own claim custody, stated as the law the substrate already earned in blood), and Awaiting Primitives (the score-facing sweep, blocked on claim-table export). The authorable approximation — a CLI process-probe PAR over physical handles — is documented. Its five-failure-class table survives inside The Black-Box Ledger, where Review 3 asked for it.

### Reclassified (4)

**Fan-out + Synthesis** → *Foundational Primitive*. Review 2: "It should be treated as a primitive, not a peer of the more specific mechanisms." It keeps full treatment (it is iteration 1–4 load-bearing and iteration-5-confirmed — all six expeditions were forbidden from returning it, and the ban is the confirmation), but it no longer sits beside Replication Licensing pretending to be the same kind of thing. Its "composes with everything" claim is replaced by the composition contracts (below).

**The Tool Chain** → *The Etiquette Law*. Review 2: "It is a substrate rule... It belongs in glossary or law, not beside Replication Licensing and Fencing Token." The content survives in full — the 74 independent empty-fallback-chain attestations remain the strongest empirical result in the corpus — as the corpus's first law, stated once, that every gate in every pattern cites.

**Fork-Evident History** → *core, reframed as the substrate layer*. Review 2: "Fork-evidence is the substrate; errata and proof sidecars are payloads." Review 3: "Admits 'the simplest robust form is `git` itself.' Then the pattern is: use git." Kept (Review 1 ranked it fourth-strongest, composable in minutes), but its prose is demoted to the substrate role, its git-canonical implementation is named outright, and its payload patterns (Errata Ledger, Proof-Carrying Artifact sidecars) now inline the supersession discipline they ride on — Review 3's fold, executed without deletion.

**Metered Merge** — *absorption reversed*. The draft absorbed Metered Merge into Hutchinson's Warning; Review 2 reversed it: "Metered Merge has a specific rate-control equation and queue-spill behavior; Hutchinson is delayed-feedback damping. They are related but not safely identical." Metered Merge returns to the archive with its ALINEA equation (`admit = k + gain × (target − measured)`, clamped), queue-spill override, and pretimed degradation intact, and the seam stated in both directions. Consequence for the grammar: C7 (lagged feedback oscillates) now honestly carries **one core pattern** — the defect Review 1 found in the draft ("C7 is a part of speech with one word") is not papered over: C7 is flagged as the thinnest convergence, with Metered Merge (archive) as its second family member, and v6 must either find a third carrier or demote C7 to a law of controller design.

### Strengthened (every survivor, with the review that forced it)

- **Proof-Carrying Artifact** — the strongest concept, previously hobbled by an impossible verify stage. Now: the canonical **proof form** is primary; **pedigree** and **claim** are named sub-forms with *different admission checks* (Review 2: "pedigree does not prove admissibility; it only traces origin"); the data-driven `instances: "{{ claims }}"` fabrication is gone — fan-out is static (`fan_out: {3: 10}` worst-case bound, Review 1); the produce stage's prompt now *instructs* writing `evidence/produce.json`, and the verdicts directory is created by the extract stage (Review 1's dangling-validation finding); the phantom scripts are named entries in the Script Library with interface contracts (Reviews 1 and 3).
- **Positive Transfer** — overlap write rule added (Review 2: "outgoing retains operational authority; incoming may inspect and acknowledge only"); the sender-outlives-its-offer precondition, which Review 3 found unverified ("a finished Marianne sheet is gone"), is answered structurally: ownership is a property of the ledger, not the liveness of the executor — the offer holds in workspace state, the hold is bounded by `max_wall_seconds`/lease semantics, `on_failure` escalates unaccepted offers, and the release write is made by the sender score's next invocation or a deterministic gate. The ledger tolerates `offered`-without-`release` indefinitely without ever having zero owners.
- **The MIST Card** — status: **approximation**. Review 1 found the feeding mechanism fabricated ("There are no retry hooks in the substrate"). Scope narrowed honestly: the card governs *score-authored* retry and recovery chains, where the retry path can be wrapped in a deterministic shell that appends the ledger row — conductor-internal retries are out of scope until per-attempt hooks exist. The fingerprint function Review 2 and Review 3 both demanded is now defined (below).
- **The Errata Ledger** — atomic pair commit and the propagation watermark are now the load-bearing mechanism (Review 2's condition for survival); the serialization Review 3 found "asserted, not wired" is wired: ONE deterministic writer movement, a gate that fails the cycle on ledger-written-but-canon-unwritten, and the hash-join validation that makes the pair unable to diverge.
- **Standby–GO** — full runnable YAML in the real dialect with the arm-gate as a CLI movement (Review 3); structure restated without theatre color: two-phase cueing, arm with complete ack set, one irreversible addressed fire (Review 2); `skip_when` corrected to command form (Review 3's finding that the draft assumed a buffer-name expression).
- **The Attested Merge Gate** — the per-sheet `isolation: git-worktree` fabrication removed (Review 1: isolation is job-level; job.py:937 warns `parallel.enabled` + `isolation.enabled` is a hazard). Restated on job-level chaining (N isolated jobs, one merge job) or shared-workspace instance-tagged namespaces, with the deterministic sweep as the real gate. The Prefabrication obsolescence clause Review 2 asked for is explicit: Prefabrication without attestation, grounded sweep, and single merge authority is obsolete.
- **Join-Semilattice Merge** — per-sheet isolation claim removed; the instance-tagged namespace scheme is what makes concurrent numbering collision-free by construction (Review 1). The idempotence probe (join twice, `diff` empty) survives as the corpus's best property-checking validation.
- **Behavioral Pre-Mortem** — the dry-render is no longer phantom: `mzt validate` performs three validation layers and renders the DAG visualization; the pattern's render stage is that command plus a programmatic JobConfig render (Review 3's "name the actual dry-render command"). A typed graph schema and a mandatory counterexample artifact on violation are required (Review 2).
- **First Article Characterization** — the manifest-runner idiom is named explicitly: one deterministic runner script loops over keyed manifest checks internally, because 200 instances × N keyed checks is not a static validation list (Review 1). Inhomogeneous populations are now a hard exclusion, not a warning (Review 2).
- **The Skeptical Oracle** — the two-AI-family interpretation stage is demoted to an optional consumer, not part of the oracle proper (Review 2: "The pattern should stop at proposal plus deterministic reconstruction plus quarantine"); the reproduction pointer is a schema, not prose; a single-family degraded mode is defined so the pattern does not price out a free-local run (Review 3) — N runs of one family with disjoint question ownership, honestly labeled weaker independence.
- **Canon of Phases** — kept (Review 1 found it buildable; Reviews 2 and 3 wanted it demoted unless independence was proven). The independence argument is now stated against its parts: Positive Transfer is a pairwise executor handoff with an overlap dialogue; Canon of Phases is *scheduled rotation of an unbounded stream* by interchangeable workers where the packet is the only inter-phase channel and the overlap dialogue does not exist. The deployment topology Review 1 asked for is written down: three *deployments* of one score — distinct IANA timezone, distinct workspace, same packet path — not three instances of one job.
- **Negative-Treatment Watch** — the claim graph with source anchors and dependent edges is required, because without dependent edges the pattern cannot enumerate blast radius (Review 2); the flag-rate trip is enforced by the deterministic sweep script comparing counts, not by `circuit_breaker`, which accepts failure counts only (Review 1).
- **The Fencing Token** — "receives the token via runtime variables" replaced with the real mechanism: the grant movement writes the token to a workspace file; the work template cites it; artifacts embed `token: NNN` (Review 1). The seam against Replication Licensing, which Review 3 flagged under the draft's own don't-duplicate law, is stated in both bodies: fencing defends *ordering* on a shared mutable surface (many writes, reject stale); licensing defends *exactly-once side-effect authorization* per cycle (single-use consumption, never-started vs started-died).
- **The Black-Box Ledger** — fate separation is explicit (Review 2: "the recorder must not share fate with the thing logging"): the conductor outlives the sheets and is the independent power bus; workspace state is the crash-protected medium and workspace archival the secondary recorder; the honest limits (`auto_capture_stdout` alone is not a flight recorder; bounded overwrite is a feature) are stated. The engine-supplied half is acknowledged (Review 3): the durable `on_failure` hook assembles the packet — the score author wires capture and the correlated readout, and benefits from the rest.
- **Flight Rules** — the grep grounding validation is shown concretely (a fabricated rule citation fails the run); deterministic rule selection for high-risk incident classes, with the AI handler confined to signature proposal (Review 2).
- **Self-Stabilizing Custody** — monotone local correction rules required (two corrections must not delegitimize each other); a convergence test (kill-injection at each physical interruption point) specified; pairing with the Fencing Token mandatory wherever side effects exist (Review 2).
- **Hutchinson's Warning** — narrowed to what Review 2 called its real identity: *damped delayed-feedback control with asymmetric shed/restore*. The `circuit_breaker` misattribution Review 1 found in three patterns is fixed here and everywhere: the breaker accepts **sheet-failure counts**; spend ceilings belong to `cost_limits` (which pauses the job — a different, and correct, observable); the rung ladder is score-level routing that reads a written `capacity-state.yaml`, and the rung is declared in that file — which the prompt cites — not in prompt text (Review 1: "the rung declared in prompt should be a written file the prompt cites"). A worked example with real numbers replaces the control-theory essay (Review 3).
- **Replication Licensing** — unchanged in mechanism (Review 1 ranked it first: fully expressible today, `mv`-as-consumption with the both-ways file assertion, owning exactly-once-under-crash outright), with the Fencing Token seam stated per Review 3.
- **Designation Is Authorization** — the distinction Review 2 demanded is load-bearing: conductor-mediated designation scopes **context and attachment** (what enters the sheet's world: spec corpora via `spec_tags`, techniques, cadenza directories); it is *not* OS-level capability confinement of filesystem/tool access. Prompt-injection defense by absence-of-naming is context scoping; true confinement needs engine/runtime work, and the pattern now says so.
- **Immune Checkpoint** — the >80%-rejection recalibration rule is enforced by a deterministic count gate comparing actionable vs tolerated findings, not `circuit_breaker` (Review 1); framed in plain structural language first — *a precision gate on the critic* — with the immunology as illustration, not argument (Review 2: "the mechanism is stronger than the metaphor").

### Systemic changes

1. **Every score structure rewritten in the real dialect.** Review 3's headline finding: "not one of the 25 'Marianne Score Structure' blocks is written in a schema Marianne accepts." The draft used a fictional `sheets:` list with `- name:`, `instances:`, sheet-level `capture_files`, and a data-driven lens. The real substrate — verified this iteration against `examples/getting-started/hello.yaml` and `src/marianne/core/config/` — is `movements:` + `sheet: {total_items, fan_out, dependencies}` + one Jinja template keyed `{% if stage == N %}` + `per_sheet_fallbacks`/`cadenzas` keyed by *expanded sheet number* + validations as a flat list with `condition: "stage == N"` and `{workspace}` format-string placeholders. The Real Dialect section below states the canonical skeleton once; every pattern's structure is now an excerpt from it.
2. **Substrate Availability Matrix** — per pattern: real keys today / scripts required / engine work needed. Demanded by all three reviews (their single point of unanimous agreement). The five fabrications Review 1 caught would have been caught mechanically by this table; it is now impossible to ship a pattern without declaring its substrate reality.
3. **Structural identity table for every convergence** (Review 2): state variables, authority holder, communication medium, deterministic check, failure transition, non-example. "Same move in four domains" is no longer enough.
4. **One near-miss per core pattern** (Review 2's negative-example section): each pattern now names the thing that looks like it and fails the structural test.
5. **Composition contracts** (Review 2: "'Composes with everything' is not useful"): four relations defined — layering, substitution, prerequisite, payload/substrate — and every `composes_with` entry in the new frontmatter uses one.
6. **Problem→pattern selection table and pattern index** (Review 3): the missing on-ramp, rebuilt for the v5.1 core and joined to the v4 selection guide.
7. **The Script Library promoted to a core deliverable** (Reviews 1 and 3): twelve-plus patterns previously rested on user-supplied scripts that were "an unnamed file on the reader's machine" (Review 3). The library is now an inventory with interface contracts and a named owner for v6. It is the corpus's largest single debt and it is now visible in the core document, not an appendix of regrets.
8. **Proof Program with dispositions** (all three reviews): the six legacy proof scores all prove v4 patterns — zero of the v5 core — cluster into two overrepresented shapes (security-audit ×2, codegen-with-gates ×3), every one resolves to a single instrument (vendor diversity has never been exercised by any proof in corpus history), one still recommends the retired gemini-cli, and one is a documented-flawed proof left standing. Each now has an explicit disposition (repair, re-instrument, or archive) and the v6 proof queue is prioritized. Proof debt is a **blocking requirement for v6**, not an open question (Review 1).
9. **Instrument freshness dating** (Reviews 1 and 3): instrument recommendations now carry a freshness date and a standing rule — an undated recommendation rots. Current as of 2026-09-03: opus / codex-cli / glm (paid Z.AI coding-plan profile) / free OpenRouter / local Ollama. gemini-cli is retired product-wide.
10. **The draft's own arithmetic fixed, and recorded** (Review 1: "a corpus whose Open Question 2 is about catching misnumbering misnumbers its own ledger in its closing sentence"): the draft claimed "18 absorbed-with-seam or archived iteration-5 candidates dispositioned"; the Merge Ledger contains 6 absorbed + 18 archived = **24**. This document's Merge Ledger is corrected and the error is recorded here rather than silently patched — the corpus applies its own Errata Ledger discipline to itself. C7's single-carrier count and Zeitgeber's "fourth temporal primitive" (against C6's list of six) are corrected with it.
11. **Expedition mythology removed from pattern bodies** (Review 3: "process archaeology leaking into user docs"). The Dancer/Reasoner/collision narrative lives in Review Integration and the Merge Ledger — the provenance record — not inside the patterns a newcomer reads to get work done.
12. **Human-in-the-loop vocabulary promoted to a named v6 requirement** (Review 1): escalation-to-human is the terminal state inside at least four patterns and no pattern governs the seam. Recorded as open question 1 with the v4 Andon Cord named as the archive ancestor.
13. **Self-application commitment** (Review 1): this document's corrections are recorded as errata (item 10); the next iteration must run Fork-Evident History over its own versions — the sibling-citation misnumbering found by luck in the collision must become structurally impossible.

---

## The Real Dialect

The substrate as verified against the engine this iteration (`examples/getting-started/hello.yaml`, `src/marianne/core/config/{job,execution,workspace,orchestration,techniques,spec}.py`, `instruments/builtins/cli.yaml`). Every snippet in this corpus is an excerpt from this skeleton. A pattern that cannot be phrased here is not a pattern yet — it is Awaiting Primitives.

```yaml
name: my-score
description: "One line."

instrument: opus                       # primary; see instruments: map below
instruments:
  cheap:  { profile: opencode, config: { model: "zai-coding-plan/glm-5.3-flash" } }
instrument_fallbacks: [opus, cheap]    # [] on a deterministic stage = the etiquette does not degrade

movements:
  1: { name: produce }
  2: { name: verify, instrument: cli } # movement-level instrument override
  3: { name: consume }

sheet:
  total_items: 3
  fan_out: { 2: 6 }                    # STATIC at parse time — no data-driven width
  dependencies: { 2: [1], 3: [2] }     # movement numbers
  per_sheet_fallbacks:
    8: []                              # keyed by EXPANDED sheet number (see below)
  cadenzas:
    8:
      - file: "{{ workspace }}/evidence/produce.json"
        as: context
        required: true                 # fail closed when absent

spec:
  spec_dir: "{score_dir}/specs"        # corpus attached by reference
  spec_tags: { 2: [flight-rules] }     # movement-keyed: undesignated specs are ABSENT, not hidden

prompt:
  variables:
    ceiling: 40
  template: |
    {% if stage == 1 %}
    Do the work. Write {{ workspace }}/deliverable.md and evidence/produce.json.
    {% elif stage == 2 %}
    python3 "{score_dir}/scripts/evidence-gate.py" "{{ workspace }}/evidence/"
    {% elif stage == 3 %}
    Work only from admitted artifacts. You are at rung {{ rung }}.
    {% endif %}

validations:                           # flat list; format-string paths; stage-scoped
  - type: file_exists
    path: "{workspace}/deliverable.md"
    condition: "stage == 1"
  - type: command_succeeds
    command: 'test -s "{workspace}/evidence/produce.json"'
    condition: "stage == 1"
  - type: content_regex
    pattern: "ADMITTED|CUT"
    path: "{workspace}/verdicts/overview.md"
    condition: "stage == 2"
```

**Sheet numbering** (the detail the draft got wrong everywhere): with `total_items: 3` and `fan_out: {2: 6}`, movement 1 is sheet 1, movement 2 expands to sheets 2–7, movement 3 is sheet 8. `per_sheet_fallbacks` and `cadenzas` key on the *expanded* sheet number; `spec_tags`, `skip_when`, `dependencies`, and `fan_out` key on the *movement* number.

**Two templating systems, deliberately different:** the prompt template is Jinja (`{{ workspace }}`, `{% if stage == N %}`, `{{ instance }}`); validation paths and commands are format strings (`{workspace}`, `{instance}`). Mixing them is the most common first-score bug.

**Verified real (safe to build on today):** `per_sheet_fallbacks` (empty chain = deterministic kernel), `skip_when` in **command form** (the old expression form was never evaluated and is rejected), `spec_dir`/`spec_tags`, `techniques` (kinds: `skill`/`mcp`/`protocol`, `required: true`), cadenzas as `{file|directory, as, required}`, `schedule` (exactly one of `cron`/`interval`, IANA `timezone`, `overlap`, `misfire`, `jitter_seconds` — the durable lease is what makes exactly-one-attempt-per-window true across conductor restarts), `max_wall_seconds`, the durable `on_failure` hook (atomic claim, restart reconciliation, same-ID protection, original-failure integrity), `capture_files`/`auto_capture_stdout`/`lookback_sheets`/`max_output_chars` under `cross_sheet`, `instrument_map` (instrument → movement numbers), `cost_limits` (pauses the job — distinct from the breaker), `circuit_breaker` (**trips on sheet-failure counts only** — never on spend, flag rates, or ratios), `parallel: {enabled, max_concurrent}`, `retry: {max_retries}`, `instrument: cli` (a real builtin that owns execution deterministically), the `skipped_upstream` template variable, and `mzt validate` (three-layer validation plus DAG visualization — the render surface Behavioral Pre-Mortem builds on).

**Verified absent (do not write these; they are the draft's fabrications, now archived as such):** per-sheet `isolation: git-worktree` (isolation is **job-level**: one worktree per job; `parallel.enabled` + `isolation.enabled` together is warned against), data-driven fan-out width (`instances: "{{ claims }}"` — fan-out expands at parse time), retry hooks that feed user-visible ledgers per attempt, offset-from-heartbeat scheduling, and a score-facing export of the conductor's claim table.

**Instrument recommendations (freshness 2026-09-03):** opus / codex-cli / glm via the paid Z.AI coding-plan profile for vendor-diverse tiers; free OpenRouter and local Ollama for cost-zero tiers; `instrument: cli` for the etiquette. gemini-cli is retired product-wide and must not appear in new scores. *Standing rule: every instrument recommendation in this corpus carries a freshness date; an undated recommendation is an error.*

---

## The Grammar: Ten Convergences (C1–C10)

Each convergence is the same structural move in four or more genuinely independent materials, mined without cross-communication. Review 2's structural-identity test is now part of the definition: a convergence must state its state variables, authority holder, medium, deterministic check, and failure transition, and must name a non-example.

| # | Move | One-line statement | Core carriers |
|---|------|--------------------|---------------|
| C1 | Admissibility over correctness | Not "is this output right" but "may this output enter the record" — pedigree decides usability | Proof-Carrying Artifact, Skeptical Oracle, Flight Rules |
| C2 | Custody is a state machine | `offered → accepted → released`, never a gap; sender holds through overlap; deadline is a place, not a number | Positive Transfer, Black-Box Ledger |
| C3 | Permission is a physical object | Authority travels, expires, or is consumed — never a sentiment the prompt asserts | Replication Licensing, Designation Is Authorization, Fencing Token |
| C4 | History is append-only | Corrections supersede, never rewrite; a shrinking journal is a rewritten journal | Fork-Evident History, Errata Ledger |
| C5 | The etiquette is deterministic | The protocol layer is non-LLM with an empty fallback chain; the performance layer is not | The Etiquette Law (formerly The Tool Chain), every gate in every pattern |
| C6 | Time is five primitives | Dependency order ≠ stagger ≠ leased recurrence ≠ acknowledged handoff ≠ deadline-first | Fencing Token, Canon of Phases (Zeitgeber's phase lock: awaiting) |
| C7 | Lagged feedback oscillates | Damp the trend, shed fast, restore slow; asymmetric degradation ladders | Hutchinson's Warning (core) + Metered Merge (archive) — *thinnest convergence; see Open Questions* |
| C8 | Independence is constructed | Sample count is not independence; isolation, vendor diversity, or disjoint question ownership is | Skeptical Oracle, First Article Characterization, Join-Semilattice Merge |
| C9 | Truth decays | Admission is not permanence; validity is leased and renewed against current sources | Negative-Treatment Watch, Flight Rules (effectivity pinning) |
| C10 | Failure degrades in character | Specify in advance what the system stops into — a rehearsed posture, never scatter | Standby–GO (hold), Hutchinson's Warning (ladder) |

### Structural identity per convergence (Review 2's demand)

| C | State variables | Authority holder | Medium | Deterministic check | Failure transition | Non-example |
|---|-----------------|------------------|--------|--------------------|--------------------|-------------|
| C1 | claim + evidence bundle | the checker (small, auditable) | sidecar artifact | re-hash / re-run / cite-by-digest | inadmissible → excluded, not downweighted | a confidence score attached to a claim |
| C2 | item custody state | current owner (ledger-recorded) | ledger file | state-machine gate (timestamps ordered, no regressions) | unaccepted → held + escalated, never dropped | an FYI handoff note |
| C3 | token/license counter | serialization point (file or counter) | physical file (mv-able) | token compare / both-ways file assert | stale/expired → rejected at the boundary | "you are authorized" in a prompt |
| C4 | journal digest chain | nobody (algebra) | append-only journal | chain recompute + prefix check | edit → chain break at edit point, visible | timestamps with an append promise |
| C5 | gate exit codes | the deterministic instrument | exit code + typed report | the gate *is* the check | instrument down → score stops (no fallback) | an LLM asked "did the tests pass?" |
| C6 | schedule/lease/token clock | the conductor's scheduler | lease record | lease renewal per cycle | lease lapse → skip (overlap: skip), never double-fire | hoping two crons don't overlap |
| C7 | budget/occupancy trend (EMA) | the router (reads written state) | capacity-state file | EMA threshold + asymmetry assert | cross → shed now; restore only after M windows | instantaneous spend checks |
| C8 | sample provenance | the composer (before the run) | instrument_map / prompt scoping | disjointness is verifiable in the config | independence unproven → claims labeled weaker | asking the same model three times |
| C9 | claim validity lease | the recurring audit | source digests | re-fetch/re-hash vs anchored digest | stale → quarantined + dependents enumerated | a nightly "sources changed" email |
| C10 | degradation rung | the router (written state only) | capacity-state file + declared rung | rung-transition asymmetry assert | pressure → rehearsed posture (hold/ladder/skip) | try/catch that empties the output |

---

## The Six Generators

Six physical pressures that generate every universal move, subsuming v4's Ten Forces (mapping in parentheses).

| Generator | The pressure | Generates | v4 forces subsumed |
|-----------|--------------|-----------|--------------------|
| **G1. Irreversibility** | Some moments cannot be taken back; asymmetric error cost forces admission control before the boundary | C1, waiver discipline, arm-before-fire | Exponential Defect Cost, Progressive Commitment |
| **G2. The unreliable narrator** | Producers hallucinate, flatter, err, or lie; truth cannot be adjudicated claim-by-claim | C1, C5 (tiny kernel), C8, grounding validations | Information Asymmetry, Structured Disagreement |
| **G3. Mortal executors** | Every worker ends — shift, process, context window, lease — and the work must not | C2, C6, fencing, black-box ledgers, succession, roll calls | Partial Failure |
| **G4. Shared finite budgets** | Money, wall-clock, context, attention: finite, shared, contested, telemetry late | C7, degradation ladders, cost limits as first-class objects | Finite Resources, Producer-Consumer Mismatch |
| **G5. Mutable truth** | The world moves under the corpus: sources rot, configs advance, errata land | C9, C4, re-tiering | Accumulated Signal |
| **G6. Distributed ignorance** | No participant sees the whole; coordination must work anyway | C6 (observable phase), join-semilattices, self-stabilization, stigmergy | Convergence Imperative, Instrument-Task Fit |

LLM orchestration is the intersection of all six at full intensity — hallucinating narrators (G2), dying contexts (G3), lagged shared budgets (G4), mutable sources (G5), no global view (G6) — and, uniquely among the domains studied, it *acts* on the world, importing G1's irreversibility into a medium that otherwise feels frictionless.

---

## Composition Contracts

Review 2: "'Composes with everything' is not useful." Every `composes_with` entry in this corpus declares one of four relations:

1. **Layering** — A wraps B: B runs inside A's envelope (B's stages are A's payload).
2. **Substitution** — A replaces one of B's components with a stricter one (a judge becomes a join; a self-report becomes a gate).
3. **Prerequisite** — A's output is B's admission condition (B may not start until A's artifact passes).
4. **Payload/substrate** — A carries B's artifacts as content over B's verification structure (sidecars over a digest chain; corrections over fork-evidence).

---

# Laws & Foundational Primitives

## The Etiquette Law (formerly The Tool Chain)

---
name: "The Etiquette Law"
scale: foundational
status: working
forces: ["Instrument-Task Fit", "Accumulated Signal"]
generators: ["G2 The Unreliable Narrator"]
problem: "Deterministic protocol checks are given to LLM instruments that can hallucinate them, making the coordination layer no more reliable than the performers it coordinates."
signals:
  - "any check whose result could be a shell exit code"
  - "a gate described in prose inside a prompt"
  - "a fallback from a deterministic instrument to an LLM"
stages:
  - name: etiquette-gate
    sheets: 1
    instrument_guidance: "instrument: cli — deterministic by construction; this stage must never think"
    fallback_friendly: false
    purpose: "Own the protocol decision (admit/reject) as a command with an empty fallback chain."
  - name: performance
    sheets: 1
    instrument_guidance: "any AI instrument matched to the work's grain"
    fallback_friendly: true
    purpose: "Do the judgment work the gate admitted."
dependencies:
  performance: [etiquette-gate]
composes_with:
  - pattern: "Every core pattern"
    how: "prerequisite — every gate in this corpus is an Etiquette Law stage"
---

**Status:** Working. **Source:** v4 iterations 2–4; confirmed iteration 5 — 74 independent empty-fallback-chain attestations across the six expeditions; prior art CI/CD.

**Core Dynamic.** The deterministic part is always the etiquette, never the music. The protocol layer — cues, gates, ledgers, meters — goes to non-LLM instruments with empty fallback chains, not because AI instruments are unreliable, but because the etiquette must be *more reliable than the performers*, and the cheapest way to make something reliable is to make it not need to think. Three different things are routinely conflated and must not be: *tool use inside an LLM sheet*, *a deterministic validation command*, and *a non-LLM instrument that owns execution* (`instrument: cli`). The etiquette always belongs to the third. The de Bruijn criterion names the audit condition: the checker must be small enough to audit by reading.

**When to use:** always — this is the substrate of every other pattern. The moment a check can be a command, it must be a command.

**When NOT to use:** the work itself is judgment (do not "optimize" tone into a linter). A deterministic stage given a fallback to an LLM is the anti-pattern this law exists to name — a fallback for a clock is a second clock, and two clocks are the desynchronization you built the law to prevent.

**Marianne Score Structure**

```yaml
movements:
  1: { name: gate, instrument: cli }
  2: { name: ai-review }

sheet:
  total_items: 2
  dependencies: { 2: [1] }
  per_sheet_fallbacks:
    1: []                      # the etiquette does not degrade

prompt:
  template: |
    {% if stage == 1 %}
    bash "{score_dir}/scripts/run-gates.sh" "{{ workspace }}" --lint --schema --tests
    {% elif stage == 2 %}
    Review only what the gate admitted. Cite gate outputs by path.
    {% endif %}

validations:
  - type: command_succeeds
    command: 'test -s "{workspace}/gate-report.json"'
    condition: "stage == 1"
  - type: content_regex
    pattern: "gate-report.json"
    path: "{workspace}/review.md"
    condition: "stage == 2"
```

**Near-miss:** an `agentai` sheet asked "run the linter and report whether it passed" — tool *use* inside a thinking instrument; the exit code became a sentence, and sentences hallucinate.

**Example.** A documentation pipeline: markdown lint, link check, and schema validation as `instrument: cli` movements with empty fallback chains; the AI reviewer consumes only the typed gate report — its judgment is spent on meaning, not on re-deriving what a script already decided.

---

## Fan-out + Synthesis (Foundational Primitive)

---
name: "Fan-out + Synthesis"
scale: foundational
status: working
forces: ["Information Asymmetry", "Finite Resources"]
generators: ["G6 Distributed Ignorance"]
problem: "Work that could be parallelized is done sequentially, or parallel outputs remain fragmented without meaningful integration."
signals:
  - "problem decomposes into independent sub-problems"
  - "sub-problems can be worked simultaneously"
  - "diverse perspectives must be integrated, not concatenated"
stages:
  - name: prepare
    sheets: 1
    instrument_guidance: "matched to decomposition difficulty; a cheap instrument suffices for simple scoping"
    fallback_friendly: true
    purpose: "Define scope and shared context."
  - name: analyze
    sheets: fan_out(6)
    instrument_guidance: "capability must match analysis grain; diverse instruments only if independence is the goal (else interchangeable)"
    fallback_friendly: true
    purpose: "Work independent facets in parallel."
  - name: synthesize
    sheets: 1
    instrument_guidance: "stronger than the producers — integration is higher-order work; a cheap fallback risks concatenation"
    fallback_friendly: false
    purpose: "Integrate parallel outputs, addressing cross-cutting themes."
dependencies:
  analyze: [prepare]
  synthesize: [analyze]
composes_with:
  - pattern: "Join-Semilattice Merge"
    how: "substitution — replaces the judge-synthesis with an algebraic join when facts are additive"
  - pattern: "Attested Merge Gate"
    how: "substitution — replaces trust-the-merge with contracted, attested, swept merging"
  - pattern: "Skeptical Oracle"
    how: "substitution — replaces trust-the-findings with deterministic reconstruction"
  - pattern: "Proof-Carrying Artifact"
    how: "layering — wraps the fan-out so synthesis consumes only admitted evidence"
---

**Status:** Working. **Source:** ubiquitous; iterations 1–4, confirmed iteration 5 (all six expeditions were forbidden from returning it; the ban is the confirmation — every voice had to position its discoveries against this move, and all six reported the territory around it as saturated). Prior art: MapReduce.

**Core Dynamic.** Split work into parallel independent streams, merge in a synthesis stage. The boundary condition the corpus earned in iteration 5 stands: fan-out answers *who does what in what order* — and the perpendicular questions (who is authorized, what evidence traveled, who owns failure, when to stop) are not answerable inside it. Every communication and adaptation pattern in this corpus is a wrapper around this move, not a replacement for it.

**When to use:** the problem decomposes into independent sub-problems with a meaningful merge, and the merge can be trusted or made trustworthy.

**When NOT to use:** sub-problems share mutable state (isolated writers + a merge authority); synthesis is trivial concatenation (a pure join, no judge); fan-out width of 1 suffices; or the outputs must *agree* rather than integrate.

**Marianne Score Structure**

```yaml
movements:
  1: { name: prepare }
  2: { name: analyze }
  3: { name: synthesize }

sheet:
  total_items: 3
  fan_out: { 2: 6 }
  dependencies: { 2: [1], 3: [2] }

prompt:
  template: |
    {% if stage == 1 %}
    Define scope. Write {{ workspace }}/scope.md and stop.
    {% elif stage == 2 %}
    Analyze module {{ instance }}. Write {{ workspace }}/analysis-{{ instance }}.md and stop.
    {% elif stage == 3 %}
    Read all analysis files. Produce a unified review addressing cross-cutting concerns.
    {% endif %}

validations:
  - type: file_exists
    path: "{workspace}/scope.md"
    condition: "stage == 1"
  - type: file_exists
    path: "{workspace}/analysis-{instance}.md"
    condition: "stage == 2"
  - type: command_succeeds
    # Quorum floor 4-of-6 is a DECLARED degradation decision: two dead analysts
    # must not kill the synthesis, but the synthesis must know what it is missing.
    command: 'test $(ls {workspace}/analysis-*.md | wc -l) -ge 4'
    condition: "stage == 3"
```

**Near-miss:** six analysts all reading each other's outputs "for coherence" — independence destroyed before the merge; you paid for a fan-out and got one committee with six names.

**Example.** Six-region market analysis: one sheet per region, one synthesis, wrapped in Proof-Carrying Artifact sidecars so the synthesis consumes only admitted evidence.

---
# Communication Patterns

*v4 had one pattern at this scale — the declared critical deficit. Six enter v5.1. The group's discovery: shared files as a medium for **permission and phase** (who may act, on what, valid until when, superseded by whom), where v4's Stigmergic Workspace used them as a medium for content. Acknowledgement that lives in a prompt is vibes; acknowledgement that lives in a workspace file with a timestamp is a receipt.*

## Proof-Carrying Artifact

---
name: "Proof-Carrying Artifact"
scale: communication
status: working
forces: ["Information Asymmetry", "Structured Disagreement", "Exponential Defect Cost"]
generators: ["G2 The Unreliable Narrator", "G1 Irreversibility"]
problem: "Consumers must either trust producer claims across a trust boundary or re-derive the work at full cost."
signals:
  - "any handoff where the cost of being wrong exceeds the cost of checking"
  - "claims like 'tests pass' or 'this number came from the source'"
  - "a downstream sheet about to build on an upstream assertion"
stages:
  - name: produce
    sheets: 1
    instrument_guidance: "the expensive producer — any AI instrument matched to the work"
    fallback_friendly: true
    purpose: "Do the work AND write the admissibility evidence beside it."
  - name: extract
    sheets: 1
    instrument_guidance: "instrument: cli — deterministic anchor extraction and directory preparation"
    fallback_friendly: false
    purpose: "Build the typed claim ledger and the verdicts directory."
  - name: verify
    sheets: fan_out(10)
    instrument_guidance: "vendor-diverse AI checkers, one claim each; static worst-case width (data-driven width does not exist in the substrate)"
    fallback_friendly: true
    purpose: "Verify one claim against its source anchor; verdict ADMITTED or CUT."
  - name: admit
    sheets: 1
    instrument_guidance: "instrument: cli — re-hash every digest; exit nonzero on mismatch"
    fallback_friendly: false
    purpose: "Mechanically refuse any artifact whose evidence does not re-hash."
  - name: consume
    sheets: 1
    instrument_guidance: "any AI instrument; receives only admitted evidence as a required cadenza"
    fallback_friendly: true
    purpose: "Work only from admitted artifacts; DEBT-listed claims ship visibly unanchored."
dependencies:
  extract: [produce]
  verify: [extract]
  admit: [verify]
  consume: [admit]
composes_with:
  - pattern: "Fork-Evident History"
    how: "payload/substrate — sidecars become journal links over the digest chain"
  - pattern: "Flight Rules"
    how: "substitution — rule citations grounding-validated; a fabricated citation fails the run"
  - pattern: "Skeptical Oracle"
    how: "substitution — the oracle's reconstruction stage is this pattern applied to peer review"
  - pattern: "Fan-out + Synthesis"
    how: "layering — wraps the fan-out so synthesis consumes only admitted evidence"
---

**Status:** Working. **Source:** proof-carrying code, LCF kernels (iteration 5, Reasoner expedition). Absorbs the Annotated Galley (claim form) and Traceability Chain (pedigree form), seams stated below per the merge law.

**Core Dynamic.** The producer does the expensive work and ships the artifact *with its admissibility evidence*; the consumer checks rather than trusts, and checking is orders of magnitude cheaper than producing. Trust shifts from the producer's identity or confidence to the checker's smallness (the de Bruijn criterion: the checker must be small enough to audit by reading). A claim without its evidence bundle is not *wrong* — it is *inadmissible*: it cannot even be considered. One mechanism, three forms, each with a **different admission check** (Review 2's split — they are not the same bundle):

- **Proof form** (canonical): the bundle is `{command, exit_code, stdout_digest, input_digests[], outputs[]}` — the means of re-checking the property itself. *Admission check: re-run / re-hash.*
- **Pedigree form** (absorbed Traceability Chain): the bundle is a provenance block — source hashes, upstream sheet IDs, spec versions, uncertainty statement. *Admission check: digest presence + spec-version match.* **Seam: pedigree answers where it came from; proof answers why it should be admitted. Pedigree alone never admits.**
- **Claim form** (absorbed Annotated Galley): the bundle is an inline anchor — `[[C7: claim text | source: evidence/report.pdf#p12]]` — extracted into a typed claim ledger before verification. *Admission check: anchor extractable + source addressable.* A claim that cannot name its source does not get weakly verified; it is structurally inadmissible.

**When to use:** every handoff across a trust boundary — sheet to sheet, score to score via `on_success`, agent to human reviewer.

**When NOT to use:** properties not cheaply decidable — taste, tone, "is this a good design" has no checker, and pretending to verify it produces theater. When the checker grows as complex as the producer, the asymmetry that made the pattern worth having is gone. Ephemeral artifacts never re-consumed downstream. In the claim form: evaluative claims cannot anchor; private or perishable sources rot the anchor (needs Negative-Treatment Watch downstream).

**Marianne Score Structure**

```yaml
movements:
  1: { name: produce }
  2: { name: extract, instrument: cli }
  3: { name: verify }
  4: { name: admit, instrument: cli }
  5: { name: consume }

sheet:
  total_items: 5
  fan_out: { 3: 10 }                  # STATIC worst-case width: one checker per claim,
  dependencies: { 2: [1], 3: [2], 4: [3], 5: [4] }   # capped at 10; a bigger claim set
  per_sheet_fallbacks:                # splits into batches of scores, not wider fan-out
    2: []
    4: []                             # extraction and admission never degrade
  cadenzas:
    10:
      - file: "{{ workspace }}/claim-ledger.json"
        as: context
        required: true                # no verdict without the ledger in context

prompt:
  variables:
    claims: 10
  template: |
    {% if stage == 1 %}
    Do the work. Write {{ workspace }}/deliverable.md. EVERY load-bearing claim carries
    an inline anchor [[Cn: text | source: path#locator]]. Also write
    {{ workspace }}/evidence/produce.json recording {command, exit_code, digests, outputs}.
    {% elif stage == 2 %}
    mkdir -p "{{ workspace }}/verdicts" && python3 "{score_dir}/scripts/anchor-extractor.py" \
      "{{ workspace }}/deliverable.md" > "{{ workspace }}/claim-ledger.json"
    {% elif stage == 3 %}
    Verify ONLY claim {{ instance }} against its source anchor in claim-ledger.json.
    Verdict ADMITTED or CUT. Quote the claim verbatim and cite the anchor ID.
    Write {{ workspace }}/verdicts/C{{ instance }}.md and stop.
    {% elif stage == 4 %}
    bash "{score_dir}/scripts/evidence-gate.sh" "{{ workspace }}/evidence/" \
      "{{ workspace }}/claim-ledger.json" "{{ workspace }}/verdicts/"
    {% elif stage == 5 %}
    Work only from admitted artifacts. DEBT-listed claims ship visibly unanchored.
    {% endif %}

validations:
  - type: command_succeeds
    command: 'test -s "{workspace}/evidence/produce.json"'      # the produce stage is INSTRUCTED to write it
    condition: "stage == 1"
  - type: command_succeeds
    command: 'test -s "{workspace}/claim-ledger.json" && test -d "{workspace}/verdicts"'  # extract stage creates the dir
    condition: "stage == 2"
  - type: content_regex
    pattern: "ADMITTED|CUT"
    path: "{workspace}/verdicts/C{instance}.md"
    condition: "stage == 3"
  - type: command_succeeds
    command: 'bash {score_dir}/scripts/evidence-gate.sh --check "{workspace}/evidence/"'  # re-hash; nonzero on mismatch
    condition: "stage == 4"
```

**Near-miss:** attaching a confidence score to each claim — pedigree theater; confidence is not a checker, and 0.9 twice is not evidence once.

**Example.** A contract-review pipeline: every extracted clause claim ("the liability cap is $1M") ships with file path + byte-range digest; the synthesis stage mechanically refuses claims whose digests do not re-hash against the corpus it was given. The paralegal-level claim never enters the memo unverified — not because the extractor is trusted, but because unverified claims are inadmissible.

---

## Positive Transfer

---
name: "Positive Transfer"
scale: communication
status: working
forces: ["Partial Failure", "Information Asymmetry"]
generators: ["G3 Mortal Executors"]
problem: "Work moving between executors passes through moments with no owner, and a failed handoff silently drops custody."
signals:
  - "work crossing a trust boundary — different instruments, scores, or teams"
  - "the cost of a moment without an owner exceeds the cost of a moment with two"
  - "shift boundaries, score-to-score chains, escalation from worker to human"
stages:
  - name: offer
    sheets: 1
    instrument_guidance: "the sender — any AI instrument; must prepare the offer while CONTINUING to own the item"
    fallback_friendly: true
    purpose: "Write handoff-{id}.json in state offered; retain ownership."
  - name: accept
    sheets: 1
    instrument_guidance: "the receiver — different instrument or score; writes acceptance, may inspect but NOT mutate until release"
    fallback_friendly: true
    purpose: "Positively accept; keyed to the handoff's identity so a duplicate cue is a no-op."
  - name: gate
    sheets: 1
    instrument_guidance: "instrument: cli — the ledger state machine IS the pattern's enforcement"
    fallback_friendly: false
    purpose: "Assert release > acceptance > offer, no regressions, no released-without-accepted."
dependencies:
  accept: [offer]
  gate: [accept]
composes_with:
  - pattern: "Canon of Phases"
    how: "layering — the rotation's boundary contains this dialogue compressed"
  - pattern: "Black-Box Ledger"
    how: "prerequisite — unaccepted offers feed the failure packet"
---

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

---

## The MIST Card

---
name: "The MIST Card"
scale: communication
status: approximation
forces: ["Partial Failure", "Accumulated Signal"]
generators: ["G3 Mortal Executors", "G2 The Unreliable Narrator"]
problem: "A retry loop treats an arriving item as fresh and repeats an intervention that already failed, wasting the window or compounding damage."
signals:
  - "any score-authored retry, recovery chain, or multi-stage escalation"
  - "the next handler must know what previous handlers already tried"
  - "two attempts where one should do is itself a hunt signal"
stages:
  - name: ledger-writer
    sheets: 1
    instrument_guidance: "instrument: cli — a wrapper that appends the attempt row; conductor-internal retries CANNOT feed this (no per-attempt hooks exist)"
    fallback_friendly: false
    purpose: "Append every attempt row mechanically; agents never self-report from memory."
  - name: recovery
    sheets: 1
    instrument_guidance: "any AI instrument; receives the ledger as a required cadenza"
    fallback_friendly: true
    purpose: "Propose a remedy WITH the treatment history in context."
  - name: constraint-check
    sheets: 1
    instrument_guidance: "instrument: cli — fingerprint collision gate"
    fallback_friendly: false
    purpose: "Reject any remedy whose fingerprint matches a recorded failure."
dependencies:
  recovery: [ledger-writer]
  constraint-check: [recovery]
composes_with:
  - pattern: "Black-Box Ledger"
    how: "layering — the card rides the failure packet"
  - pattern: "Flight Rules"
    how: "prerequisite — a rule action colliding with a recorded failed remedy is a rule-delta signal"
  - pattern: "Replication Licensing"
    how: "prerequisite — recovery distinguishes never-started from started-died"
---

**Status:** Approximation — the scope Review 1's engine audit forced. The draft claimed conductor retry hooks feed the ledger mechanically; **no such hooks exist** (the conductor retries internally via checkpoint/resume; nothing appends to a user-visible ledger per attempt). The pattern governs *score-authored* retry and recovery chains, where the retry path is a wrapper the score owns. Full mechanical feeding of conductor-level retries awaits per-attempt hooks (see Awaiting Primitives).

**Core Dynamic.** When work moves through a chain of handlers, the item's **treatment history** must travel with it — and the history is not narrative, it is **constraint**. The next handler is not free to act as if the item were fresh: the failed remedy from two attempts ago must not be re-applied. The card is append-only precisely because a rewrite destroys the constraints. The cardinal failure is "re-triage from scratch."

**The fingerprint function (Reviews 2 and 3 both demanded it defined):**

```
fingerprint = sha256(
  error_class                    # normalized: lowercase, strip vendor prefixes
  | normalize(tool + args)       # sort flag-arguments alphabetically, collapse whitespace,
                                 #   drop volatile tokens (timestamps, temp paths, retry counts)
  | target_path                  # resolved absolute path, workspace-relative prefix stripped
)
```

Normalization is the load-bearing half: it is chosen so "retry with a tweak" — same tool, reordered flags, cosmetic difference — **collides** with the recorded failure, while a genuinely different remedy (different tool, different target) does not.

**When to use:** any score-authored retry loop, recovery chain, or multi-stage escalation where re-trying a failed remedy wastes the window or compounds the damage.

**When NOT to use:** the record travels on a different channel than the item (the card left on the ambulance). Handlers disagree on schema — the fixed form is the point. Nobody is required to read it before acting (enforce with a `required: true` cadenza or do not bother).

**Marianne Score Structure**

```yaml
movements:
  1: { name: attempt, instrument: cli }
  2: { name: recovery }
  3: { name: constraint-check, instrument: cli }

sheet:
  total_items: 3
  dependencies: { 2: [1], 3: [2] }
  per_sheet_fallbacks: { 1: [], 3: [] }
  cadenzas:
    2:
      - file: "{{ workspace }}/mist-ledger.yaml"
        as: context
        required: true              # no remedy may be proposed without the history

prompt:
  template: |
    {% if stage == 1 %}
    bash "{score_dir}/scripts/attempt-wrapper.sh" "{{ workspace }}/item.json" \
      -- your-command-here          # wrapper appends {item, error_class, remedy_fingerprint,
    {% endif %}                     # timestamp, outcome} to mist-ledger.yaml, THEN execs
    {% if stage == 2 %}             # the command and appends the result row
    Item {{ id }} has failed handlers before you; the ledger above is CONSTRAINT, not
    history. Propose the next remedy. A remedy whose fingerprint appears in the ledger
    as failed WILL be rejected downstream — do not propose it.
    {% elif stage == 3 %}
    python3 "{score_dir}/scripts/fingerprint-collision.py" "{{ workspace }}/mist-ledger.yaml" \
      "{{ workspace }}/proposed-remedy.json" --reject-on-collision
    {% endif %}

validations:
  - type: content_regex
    pattern: "fingerprint: [0-9a-f]{64}"
    path: "{workspace}/mist-ledger.yaml"
    condition: "stage == 1"          # a run that retried without a row is a masked retry
  - type: command_succeeds
    command: 'python3 {score_dir}/scripts/fingerprint-collision.py {workspace}/mist-ledger.yaml {workspace}/proposed-remedy.json --check'
    condition: "stage == 3"
```

**Near-miss:** a free-text "lessons learned" section — narrative history does not constrain the next handler; only a keyed, fingerprinted, collision-checked ledger does.

**Example.** A content-migration concert processing 4,000 documents: item #3171 failed twice on an OCR timeout, once on a schema mismatch. When the recovery score reaches it, its MIST row forbids the third OCR retry and routes to the manual-review instrument — without the card, the run burns the batch window on a third identical timeout.

---

## Fork-Evident History

---
name: "Fork-Evident History"
scale: communication
status: working
forces: ["Structured Disagreement", "Accumulated Signal"]
generators: ["G2 The Unreliable Narrator", "G5 Mutable Truth"]
problem: "A retroactively edited history is undetectable, so downstream consumers cannot know they saw the same claims as everyone else."
signals:
  - "self-chaining scores where iteration N+1 must not silently weaken iteration N"
  - "long concerts whose claims are consumed by multiple downstream parties"
  - "corrections-heavy domains where the honest correction cites what it supersedes"
stages:
  - name: link
    sheets: 1
    instrument_guidance: "any AI instrument — its evidence compiler appends one journal record per sheet"
    fallback_friendly: true
    purpose: "Append {sheet, inputs, outputs, prev_digest} to the workspace journal."
  - name: chain-and-verify
    sheets: 1
    instrument_guidance: "instrument: cli — journal-keeper/recompute; or use git outright"
    fallback_friendly: false
    purpose: "Compute the running digest; verify prefix property and append-only length."
dependencies:
  chain-and-verify: [link]
composes_with:
  - pattern: "The Errata Ledger"
    how: "payload/substrate — corrections are payloads over this chain (the chain verifies; the ledger corrects)"
  - pattern: "Proof-Carrying Artifact"
    how: "payload/substrate — sidecars are the per-entry links"
  - pattern: "Self-Stabilizing Custody"
    how: "prerequisite — legitimacy predicates read the journal"
---

**Status:** Working. **Source:** Lamport/Pease signed messages; Raft log-matching; Certificate Transparency; in-toto. **Reframed per Reviews 2 and 3:** this is the *substrate* layer — fork-evidence is what corrections and proof sidecars ride on, not a sibling of them.

**Core Dynamic.** Signatures and digest chains convert equivocation from undetectable to detectable: a liar must now tell the *same* lie to everyone, and any two observers can mechanically compare notes. A hash chain fixes history — each entry commits to its predecessor's digest — so a retroactive edit breaks the chain at exactly the edit point, and prefix checks expose forks. Corrections enter as *supersession* entries citing the digest of what they replace; a shrinking journal is a rewritten journal. **The simplest robust form is `git` itself:** the commit DAG is already fork-evident and verifiable by any clone — when your workspace is a git repo, `git log --oneline` + `git diff` is the journal-keeper, and this pattern costs one disciplined habit (commit at every sheet boundary, never rewrite history) rather than a script.

**When to use:** self-chaining scores; multi-consumer concerts; corrections-heavy domains.

**When NOT to use:** short single-shot runs with no re-consumption. Histories that must be legitimately rewritten — deletion rights require envelope-key shredding, not history edits. Anywhere nobody will ever verify: unwatched chains are ceremony.

**Marianne Score Structure**

```yaml
movements:
  1: { name: work }
  2: { name: journal-verify, instrument: cli }

sheet:
  total_items: 2
  dependencies: { 2: [1] }
  per_sheet_fallbacks: { 2: [] }

prompt:
  template: |
    {% if stage == 1 %}
    Do the work. Then append one record to {{ workspace }}/journal.jsonl:
    {sheet, inputs, outputs, prev_digest} where prev_digest is the sha256 of the last line.
    {% elif stage == 2 %}
    python3 "{score_dir}/scripts/journal-verify.py" "{{ workspace }}/journal.jsonl" \
      --recompute --assert-append-only --require-supersedes-on-corrections
    {% endif %}

validations:
  - type: command_succeeds
    command: 'python3 {score_dir}/scripts/journal-verify.py {workspace}/journal.jsonl --check'
    condition: "stage == 2"
  - type: content_regex
    pattern: "supersedes: [0-9a-f]{64}"      # every correction entry cites its victim
    path: "{workspace}/journal.jsonl"
    condition: "stage == 2"
```

**Near-miss:** timestamps and an append promise — chronological ordering without digest commitment detects nothing; the edit is still invisible.

**Example.** A multi-day competitive-analysis concert: day-3 correction of a day-1 market-size figure enters as a supersession citing the original entry's digest; the client's auditor later proves no day-1 claim was quietly altered to flatter the narrative.

---

## The Errata Ledger

---
name: "The Errata Ledger"
scale: communication
status: working
forces: ["Accumulated Signal", "Producer-Consumer Mismatch"]
generators: ["G5 Mutable Truth"]
problem: "A correction that silently rewrites the text lies about its own history, and a correction notice nobody consumes leaves derived copies wrong."
signals:
  - "a canonical document with derived translations, summaries, or extracts"
  - "syndicated anything"
  - "a downstream copy that would otherwise drift from corrected truth"
stages:
  - name: intake
    sheets: 1
    instrument_guidance: "any AI instrument — assembles {claim_id, error, new_text, authority}"
    fallback_friendly: true
    purpose: "Stage the correction for atomic commit."
  - name: atomic-commit
    sheets: 1
    instrument_guidance: "instrument: cli — THE single serialized writer; writes corrected canon AND ledger row in one movement"
    fallback_friendly: false
    purpose: "Commit the pair together; the hash-join makes divergence impossible."
  - name: propagate
    sheets: 1
    instrument_guidance: "any AI instrument or CLI regenerator — consumes entries newer than its watermark"
    fallback_friendly: true
    purpose: "Update derived copies; advance the watermark."
dependencies:
  atomic-commit: [intake]
  propagate: [atomic-commit]
composes_with:
  - pattern: "Fork-Evident History"
    how: "payload/substrate — chaining beneath the published corrections"
  - pattern: "Negative-Treatment Watch"
    how: "prerequisite — decay detection feeds corrections"
  - pattern: "Proof-Carrying Artifact"
    how: "substitution — the hash-join is a grounding check applied to the pair"
---

**Status:** Working. **Source:** NYT/NPR/AP corrections practice; NLM citable errata. **Kept per Review 2's condition:** the atomic pair commit and the propagation watermark are now stated as *the* load-bearing mechanism (without them this is Fork-Evident History plus a correction payload). **Serialization wired per Review 3:** one deterministic writer movement owns the commit — not an assertion.

**Core Dynamic.** A correction must be two things at once — a change to the living text and a durable record of the change. Only the first is the silent rewrite; only the second is the errata nobody reads while the text stays wrong. The pattern is the *atomic pair*: fix and notice commit together, and the notice — not the fix — is what propagates downstream, because derived copies hold state the fix cannot reach directly.

**When to use:** multi-consumer corpora: canonical documents with derived translations, summaries, extracts; syndicated anything.

**When NOT to use:** consumers ignore the ledger — an advisory watermark is a seam, not a mechanism (this needs acknowledged-handoff grammar or a deterministic join). Corrections so frequent they flood the ledger (batch per release, not per typo). Adversarial environments where notices get scrubbed — there the ledger needs digest chaining beneath it.

**Marianne Score Structure**

```yaml
movements:
  1: { name: intake }
  2: { name: atomic-commit, instrument: cli }
  3: { name: propagate }

sheet:
  total_items: 3
  dependencies: { 2: [1], 3: [2] }
  per_sheet_fallbacks: { 2: [] }      # the serialized writer never degrades

prompt:
  template: |
    {% if stage == 1 %}
    Stage the correction to {{ workspace }}/pending-correction.json:
    {claim_id, error, new_text, authority}. Do NOT touch the canon.
    {% elif stage == 2 %}
    python3 "{score_dir}/scripts/errata-commit.py" "{{ workspace }}" \
      --canon spec.md --ledger ledger/corrections.jsonl
      # writes BOTH in one movement: corrected canon file AND appends
      # {id, claim_id, prior_hash, new_hash, date, note}; exits nonzero if either half fails
    {% elif stage == 3 %}
    Consume {{ workspace }}/ledger/corrections.jsonl entries newer than your watermark
    in watermark.json. Regenerate affected derived copies. Advance the watermark.
    {% endif %}

validations:
  - type: command_succeeds
    # the deterministic hash-join: the entry's new_hash MUST equal sha256 of the corrected file
    command: 'python3 {score_dir}/scripts/errata-commit.py --verify-join "{workspace}"'
    condition: "stage == 2"
  - type: file_exists
    path: "{workspace}/watermark.json"
    condition: "stage == 3"           # a consumer that ran without a watermark is a fabrication
```

**Failure wiring:** a cycle ending ledger-written-but-canon-unwritten is a failed state — `on_failure` custody holds the half-committed pair for repair rather than retry-blind (the commit script's nonzero exit is what makes the half-state visible).

**Near-miss:** a CHANGELOG.md nobody's build consumes — the notice without the propagation watermark is a diary, not a mechanism.

**Example.** A product's canonical spec sheet with generated PDF, web page, and partner-portal extracts: a dimensional error corrected once in canon, and the ledger entry drives regeneration of every extract whose watermark predates it — no extract silently retains the wrong number.

---

## Standby–GO

---
name: "Standby–GO"
scale: communication
status: working
forces: ["Progressive Commitment", "Exponential Defect Cost"]
generators: ["G1 Irreversibility"]
problem: "A one-phase cue discovers receiver readiness at the moment of irreversible execution."
signals:
  - "preparation must overlap live performance and the switch must be atomic"
  - "content freeze to publish cutover; staging to production rotation; cache rebuild under traffic"
  - "build buffer B while buffer A serves"
stages:
  - name: serve-A
    sheets: 1
    instrument_guidance: "the live consumer — pinned to the buffer named by current"
    fallback_friendly: true
    purpose: "Keep serving from frozen buffer A."
  - name: prep-B
    sheets: fan_out(4)
    instrument_guidance: "N departments, any instruments; each builds into buffer-B/ and writes ready-{dept}.json"
    fallback_friendly: true
    purpose: "Build the replacement in parallel; each completion is an ack."
  - name: arm-gate
    sheets: 1
    instrument_guidance: "instrument: cli — verifies the COMPLETE ack set and every B-artifact validating"
    fallback_friendly: false
    purpose: "Write armed-{cue}.json only when every department has armed."
  - name: go
    sheets: 1
    instrument_guidance: "instrument: cli — the atomic switchover; refuses unless armed, refuses on duplicate cue"
    fallback_friendly: false
    purpose: "Flip the current pointer in one mv-class operation; log GO {cue}."
dependencies:
  prep-B: [serve-A]
  arm-gate: [prep-B]
  go: [arm-gate]
composes_with:
  - pattern: "First Article Characterization"
    how: "prerequisite — characterize buffer B before arming"
  - pattern: "Hutchinson's Warning"
    how: "substitution — the hold is degradation rung zero"
---

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

---

# Score-Level Patterns

## The Attested Merge Gate

---
name: "The Attested Merge Gate"
scale: score-level
status: working
forces: ["Producer-Consumer Mismatch", "Exponential Defect Cost"]
generators: ["G1 Irreversibility", "G6 Distributed Ignorance"]
problem: "Parallel writers produce artifacts that must compose, and trusting their self-reports lets incompatible work merge."
signals:
  - "N different hands producing artifacts against a shared contract"
  - "an interface writable before the work starts"
  - "multi-module builds, multi-author documents, multi-vendor assembly"
stages:
  - name: contract-freeze
    sheets: 1
    instrument_guidance: "any AI instrument; output is the interface corpus pinned by manifest"
    fallback_friendly: true
    purpose: "Author and pin the interface contract in spec_dir."
  - name: writers
    sheets: fan_out(6)
    instrument_guidance: "writers in instance-tagged namespaces (job-level worktree isolation is per-JOB, not per-sheet — see substrate matrix)"
    fallback_friendly: true
    purpose: "Build the slice; attest consumed spec hashes and output hashes."
  - name: sweep
    sheets: 1
    instrument_guidance: "instrument: cli — executes the contract over actual bytes"
    fallback_friendly: false
    purpose: "Deterministic compatibility check; the merge is granted, never assumed."
  - name: merge-authority
    sheets: 1
    instrument_guidance: "one AI sheet with serial ancestry; applies merges only where attestation AND sweep both pass"
    fallback_friendly: true
    purpose: "Merge or adjudicate; conflicts produce disposition records, never silent overwrites."
  - name: post-merge-verify
    sheets: 1
    instrument_guidance: "instrument: cli — full-suite run plus release manifest"
    fallback_friendly: false
    purpose: "Bind merged content to branch attestations."
dependencies:
  writers: [contract-freeze]
  sweep: [writers]
  merge-authority: [sweep]
  post-merge-verify: [merge-authority]
composes_with:
  - pattern: "Join-Semilattice Merge"
    how: "substitution — the algebraic alternative when facts are additive; skip the authority"
  - pattern: "First Article Characterization"
    how: "prerequisite — the manifest checks are the sweep's content"
  - pattern: "Prefabrication (v4 archive)"
    how: "substitution — obsolete unless it adds attestation, grounded sweep, and single merge authority"
---

**Status:** Working. **Source:** aerospace ICDs; semiconductor IP-block assembly; signed-CI merge workflows. **Restated per Review 1** on real isolation: per-sheet `isolation: git-worktree` does not exist (isolation is job-level; `parallel.enabled` + `isolation.enabled` together is warned against as hazard #29). Two buildable forms replace the fabrication: **(a) job-level chaining** — N isolated *jobs* (one worktree each), one merge job; or **(b) shared-workspace namespace conventions** — writers in instance-tagged directories, the deterministic sweep as the real gate. Form (b) is shown here; form (a) is the concert-scale upgrade.

**Core Dynamic.** Parallel writers are safe exactly to the degree that they never touch the same truth at the same time. An interface contract is frozen and pinned; each writer builds against its slice and *attests* — a manifest with identities and hashes of what it consumed and produced. Then the part fan-out architectures skip: **the merge is a separate act with a single owner**, and the integration authority does *not* trust the attestations — it runs a grounded compatibility check on the actual bytes. Ownership is answerable at every joint: the writer owned the branch, the checker owned the verdict, the authority owned the merge.

**When to use:** any job where N different hands produce artifacts that must compose — different tasks, not copies of one task — against a contract writable before the work starts.

**When NOT to use:** the interface cannot be frozen first (collapses into an expensive meeting). Writers share one mutable surface without namespace discipline (a race with paperwork). The compatibility check is an LLM's opinion — a gate described is not a gate executed.

**Marianne Score Structure**

```yaml
spec:
  spec_dir: "{score_dir}/specs"
  spec_tags: { 2: [icd] }                  # writers receive only their interface slice

movements:
  1: { name: contract-freeze }
  2: { name: writers }
  3: { name: sweep, instrument: cli }
  4: { name: merge-authority }
  5: { name: post-merge-verify, instrument: cli }

sheet:
  total_items: 5
  fan_out: { 2: 6 }
  dependencies: { 2: [1], 3: [2], 4: [3], 5: [4] }
  per_sheet_fallbacks: { 3: [], 5: [] }

prompt:
  template: |
    {% if stage == 1 %}
    Author the interface contract into {{ workspace }}/contract/. Pin identity by manifest
    (sha256 per file). Write {{ workspace }}/contract/MANIFEST.json.
    {% elif stage == 2 %}
    Build module {{ instance }} against the tagged contract slice. Work ONLY in
    {{ workspace }}/work/module-{{ instance }}/. Produce the artifact AND
    {{ workspace }}/work/module-{{ instance }}/attestation.json:
    {consumed_spec_hashes, output_files, output_hashes, conformance_claim}.
    {% elif stage == 3 %}
    bash "{score_dir}/scripts/compat-sweep.sh" "{{ workspace }}/work" \
      --contract "{{ workspace }}/contract" --schema --typecheck --tests
    {% elif stage == 4 %}
    Admit ONLY branches where attestation AND sweep both passed (see {{ workspace }}/sweep-report.json).
    Merge passing branches; conflicts route to a disposition record — never a silent overwrite.
    Write {{ workspace }}/release-manifest.json binding merged content to branch attestations.
    {% elif stage == 5 %}
    bash "{score_dir}/scripts/full-suite.sh" "{{ workspace }}" --release-manifest release-manifest.json
    {% endif %}

validations:
  - type: file_exists
    path: "{workspace}/contract/MANIFEST.json"
    condition: "stage == 1"
  - type: file_exists
    path: "{workspace}/work/module-{instance}/attestation.json"
    condition: "stage == 2"
  - type: command_succeeds
    command: 'bash {score_dir}/scripts/compat-sweep.sh {workspace}/work --check-only'
    condition: "stage == 3"
```

**Graceful degradation:** `skipped_upstream` at fan-in — one dead writer degrades the merge visibly instead of killing the audit trail.

**Near-miss:** attestation manifests with no compatibility sweep — paperwork over bytes; the authority trusting exactly what it should run.

**Example.** Localizing a technical manual into six languages: the terminology lock is the ICD; six translator sheets work in tagged namespaces, each attesting which term-base version it consumed; a deterministic terminology checker flags every drift; an editor sheet admits only passing chapters and adjudicates conflicts against the term base, producing a record of every override.

---

## Join-Semilattice Merge

---
name: "Join-Semilattice Merge"
scale: score-level
status: working
forces: ["Structured Disagreement", "Finite Resources"]
generators: ["G6 Distributed Ignorance"]
problem: "The fan-in point is both a bottleneck and a trust point: merging concurrent writers requires arbitration that can destroy concurrent work."
signals:
  - "genuinely additive facts: findings keyed by ID, coverage observations, disjoint-segment translations"
  - "isolated writers appending disjoint records"
  - "concurrent updates delivered in any order, possibly duplicated"
stages:
  - name: writers
    sheets: fan_out(5)
    instrument_guidance: "any instruments; each emits records into an append-only, instance-tagged ID namespace"
    fallback_friendly: true
    purpose: "Append disjoint records — the instance tag makes concurrent numbering collision-free by construction."
  - name: join
    sheets: 1
    instrument_guidance: "instrument: cli — jq -s union by ID, dedupe by content digest; no LLM participates in merging"
    fallback_friendly: false
    purpose: "Converge the lattice deterministically."
  - name: synthesize
    sheets: 1
    instrument_guidance: "any AI instrument — tension/emergence work over the joined lattice, never a summary"
    fallback_friendly: true
    purpose: "Interpret the lattice; do not re-merge it."
dependencies:
  join: [writers]
  synthesize: [join]
composes_with:
  - pattern: "Fan-out + Synthesis"
    how: "substitution — the trust-free fan-in"
  - pattern: "Attested Merge Gate"
    how: "substitution — when a contract, not algebra, is what you have"
---

**Status:** Working. **Source:** CRDTs; the CALM theorem. **Isolation claim corrected per Review 1:** per-sheet worktrees do not exist; the instance-tagged namespace (`findings/{instance}-{n}.json`) is what makes concurrent numbering collision-free by construction — and it renders per-sheet isolation mostly unnecessary.

**Core Dynamic.** Convergence by *data-type construction*, not arbitration. When every writer's output is an append into an ID-keyed, monotone namespace and the merge function is a semilattice join (commutative, associative, idempotent), "conflict" is not suppressed or adjudicated — it is *undefined*. Any interleaving of concurrent updates, delivered in any order, possibly duplicated, converges to the same state without coordination. The fan-in stops being a bottleneck and a trust point simultaneously.

**When to use:** genuinely additive facts — findings keyed by ID, coverage observations, translations of disjoint segments, tagged excerpts, sensor readings.

**When NOT to use:** non-monotone semantics — veto, rejection, move operations, "take the latest prose" (last-writer-wins silently destroys concurrent work; it is amnesia, not convergence). Interacting facts (this finding contradicts that one) — a join can only collect both; adjudication needs the Skeptical Oracle. Deletion (needs tombstones; forward-only supersession avoids them).

**Marianne Score Structure**

```yaml
movements:
  1: { name: writers }
  2: { name: join, instrument: cli }
  3: { name: synthesize }

sheet:
  total_items: 3
  fan_out: { 1: 5 }
  dependencies: { 2: [1], 3: [2] }
  per_sheet_fallbacks: { 2: [] }

prompt:
  template: |
    {% if stage == 1 %}
    Transcribe your disjoint source set. Append each observation as
    {{ workspace }}/findings/{{ instance }}-<n>.json — instance-tagged, ID-keyed,
    append-only. Never touch another instance's namespace.
    {% elif stage == 2 %}
    jq -s 'sort_by(.id) | group_by(.id) | map(.[0])' {{ workspace }}/findings/*.json \
      > {{ workspace }}/joined.jsonl
    {% elif stage == 3 %}
    Read {{ workspace }}/joined.jsonl. Find tensions and emergent themes. Do NOT summarize —
    the join already merged; you interpret.
    {% endif %}

validations:
  - type: command_succeeds
    # THE idempotence probe: run the join twice into scratch; diff must be empty.
    # merge ∘ merge = merge, mechanically checked — a property check, not a process check.
    command: 'bash {score_dir}/scripts/idempotence-probe.sh {workspace}/findings'
    condition: "stage == 2"
  - type: command_succeeds
    command: 'test "$(cat {workspace}/findings/*.json | wc -l)" -ge 5'
    condition: "stage == 1"
```

**Near-miss:** "merge with last-writer-wins" — amnesia marketed as convergence.

**Example.** Five analysts each transcribe a disjoint source set into a shared observation lattice over a weekend, working offline in isolated checkouts; Monday's join converges all five branches with no coordination meeting, no merge conflicts, and no analyst blocked on another's schedule.

---

## Behavioral Pre-Mortem

---
name: "Behavioral Pre-Mortem"
scale: score-level
status: working
forces: ["Exponential Defect Cost", "Partial Failure"]
generators: ["G1 Irreversibility", "G4 Shared Finite Budgets"]
problem: "Mechanism interactions — concurrency windows, skip/fallback interplay, self-chain livelock — are invisible in YAML source and kill in production."
signals:
  - "a DAG where mechanisms interact: concurrency caps meeting shared regions"
  - "skip_when conditions interacting with fallback chains"
  - "self-chain loop conditions that could livelock; recurring schedules whose leases could double-fire"
stages:
  - name: render
    sheets: 1
    instrument_guidance: "instrument: cli — mzt validate renders the DAG; a programmatic JobConfig render dumps the full graph"
    fallback_friendly: false
    purpose: "Render the execution graph itself — never a hand-written mirror."
  - name: check
    sheets: 1
    instrument_guidance: "instrument: cli — typed invariant checker over the rendered graph"
    fallback_friendly: false
    purpose: "Check safety/liveness invariants; emit counterexample artifacts on violation."
  - name: explain
    sheets: 1
    instrument_guidance: "any AI instrument — runs ONLY on violation"
    fallback_friendly: true
    purpose: "Turn the counterexample trace into a human-readable fix proposal."
dependencies:
  check: [render]
  explain: [check]
composes_with:
  - pattern: "Self-Stabilizing Custody"
    how: "substitution — the kill-injection probe is this pattern's runtime twin"
  - pattern: "The Etiquette Law"
    how: "prerequisite — 'deterministic stages have empty fallback chains' is itself a checked invariant"
---

**Status:** Working. **Source:** TLA+/TLC at AWS. **The render is real and named (Review 3):** `mzt validate` performs three validation layers (YAML syntax, Pydantic schema, extended semantics) and renders the DAG visualization; a programmatic JobConfig dry-render is established substrate discipline for auditing concurrency and ancestry before releasing locks.

**Core Dynamic.** The pattern's object is not the work product — it is the orchestration's own *behavior space*. Before anything runs, render the plan and check every reachable behavior against invariants. Safety violations (two writers to one path in overlapping windows; a fallback routing to an occupied executor) surface as counterexample traces — concrete interleavings that break the invariant; liveness violations (a self-chain livelock; a recurring schedule whose lease has no owner; an orphan stage nothing consumes) as fairness-cycle witnesses. The AWS lesson generalized: the bugs that kill are usually *design* bugs, and the cheapest place to find one is where fixing it costs a YAML edit, not a production incident.

**Typed graph schema (Review 2's demand) and mandatory counterexample output:** the checker consumes `{nodes: {id, instrument, fallback_chain[], cadenza_dirs[], skip_when}, edges: {from, to, kind: dependency|fan_out|chain}, windows: {concurrency_cap, shared_regions[]}}`. On violation it MUST emit a counterexample artifact — the offending interleaving as an ordered event list — not a prose complaint. An invariant checker without counterexample output is a lint with ambitions.

**When to use:** any DAG where mechanisms *interact*; any score expensive enough that a wasted run matters.

**When NOT to use:** state explosion — the model must be bounded (finite workers, finite queue depths, bounded loop unrollings). Trivial pipelines with no interaction. Nondeterminism that lives outside the model (external APIs) — those need runtime patterns (fencing, self-stabilization), not pre-mortems.

**Marianne Score Structure**

```yaml
movements:
  1: { name: render, instrument: cli }
  2: { name: check, instrument: cli }
  3: { name: explain }

sheet:
  total_items: 3
  dependencies: { 2: [1], 3: [2] }
  per_sheet_fallbacks: { 1: [], 2: [] }

prompt:
  template: |
    {% if stage == 1 %}
    mzt validate "{score_dir}/this-score.yaml" --json > {{ workspace }}/graph-render.json
    {% elif stage == 2 %}
    python3 "{score_dir}/scripts/invariant-check.py" "{{ workspace }}/graph-render.json" \
      --no-cycles --no-shared-region-two-writers \
      --deterministic-stages-have-empty-fallbacks \
      --ai-stages-have-nonempty-fallbacks \
      --leases-name-an-owner --chains-reach-terminal --emit-counterexamples
    {% elif stage == 3 %}
    The checker found violations ({{ workspace }}/counterexamples.jsonl). For each, turn the
    trace into a concrete YAML fix proposal. Cite the trace line by line.
    {% endif %}

validations:
  - type: command_succeeds
    command: 'test -s "{workspace}/graph-render.json"'
    condition: "stage == 1"
  - type: content_regex
    # a render that silently dropped a sheet would otherwise check a phantom
    pattern: "\"stage\""
    path: "{workspace}/graph-render.json"
    condition: "stage == 1"
  - type: command_succeeds
    command: 'python3 {score_dir}/scripts/invariant-check.py {workspace}/graph-render.json --check-only'
    condition: "stage == 2"
```

**Near-miss:** a design-review meeting over the YAML source — checking a hand-written mirror of the graph, not the rendered graph; the mirror is where the bug isn't.

**Example.** A data-migration concert with parallel loaders and per-loader fallbacks: the pre-mortem finds that under one `skip_when` combination, two fallback paths both route to the same writer in overlapping windows — a two-writer safety violation fixed by one dependency edge, discovered for the cost of a dry run instead of a corrupted staging table.

---

## First Article Characterization

---
name: "First Article Characterization"
scale: score-level
status: working
forces: ["Exponential Defect Cost", "Instrument-Task Fit"]
generators: ["G1 Irreversibility", "G4 Shared Finite Budgets"]
problem: "Validating each item of a large homogeneous fan-out from first principles is unaffordable, and validating none is unacceptable."
signals:
  - "fan-out volume work under a new or changed configuration"
  - "N report instances, N translations, N generated artifacts of one kind"
  - "a genuine shared configuration across the population"
stages:
  - name: first-article
    sheets: 1
    instrument_guidance: "the production instrument — produces ONE instance under current configuration"
    fallback_friendly: true
    purpose: "Produce the unit that will become the reference."
  - name: characterize
    sheets: 1
    instrument_guidance: "a DIFFERENT instrument family if available — an instrument calibrating itself is not calibration"
    fallback_friendly: false
    purpose: "Produce the characterization manifest: every expected property, keyed, each with its check."
  - name: reference-freeze
    sheets: 1
    instrument_guidance: "instrument: cli — stamp the manifest with the configuration hash"
    fallback_friendly: false
    purpose: "Store the golden reference bound to the config it certified."
  - name: volume
    sheets: fan_out(200)
    instrument_guidance: "any instruments; each instance validated by executing the manifest's checks"
    fallback_friendly: true
    purpose: "Grounded volume: validate against the reference, not from principles."
dependencies:
  characterize: [first-article]
  reference-freeze: [characterize]
  volume: [reference-freeze]
composes_with:
  - pattern: "Standby–GO"
    how: "prerequisite — characterize buffer B, then arm"
  - pattern: "Skeptical Oracle"
    how: "layering — the characterization fan-out behind a trust fence"
  - pattern: "Attested Merge Gate"
    how: "prerequisite — the manifest checks are the sweep's content"
---

**Status:** Working. **Source:** AS9102 First Article Inspection; golden units; pharmacopoeia reference standards. **The manifest-runner idiom is now named (Review 1):** 200 instances × N keyed checks is not a static validation list — the buildable form is ONE deterministic manifest-runner script that loops over the keyed checks internally per instance. The grounding property lives in that script; it is a named Script Library entry, not an opacity.

**Core Dynamic.** Before volume production runs, the first unit under the new configuration is characterized *completely and independently* — every property keyed and numbered, each with the check that verifies it. **The characterized article becomes the law:** volume is not re-validated from first principles; it is validated against the reference, and disputes are settled against the retained golden unit, not re-derivation. When configuration changes, a *delta* characterizes only what changed.

**Hard exclusions (Review 2 made them exclusions, not warnings):** instances that are not actually of one kind — grounding the many against a reference requires a *genuine shared configuration*, or the first article certifies a population of one. Reference rot — a golden unit whose underlying config silently changed poisons every validation that trusted it; the reference must be bound to its configuration manifest.

**When to use:** fan-out volume work under a new or changed configuration where validating each from scratch is unaffordable but validating none is unacceptable.

**Marianne Score Structure**

```yaml
movements:
  1: { name: first-article }
  2: { name: characterize }
  3: { name: reference-freeze, instrument: cli }
  4: { name: volume }

sheet:
  total_items: 4
  fan_out: { 4: 200 }
  dependencies: { 2: [1], 3: [2], 4: [3] }
  per_sheet_fallbacks: { 3: [] }
  skip_when:
    2: { command: 'test "$(sha256sum {workspace}/config-fingerprint.json | cut -d" " -f1)" = "$(jq -r .config_hash {workspace}/reference/manifest.json 2>/dev/null || echo none)"' }
                                         # unchanged config reuses the reference;
                                         # changed config forces re-characterization

prompt:
  template: |
    {% if stage == 1 %}
    Produce ONE instance of the artifact under the current configuration.
    {% elif stage == 2 %}
    Characterize the first article COMPLETELY: every expected property in
    {{ workspace }}/characterization.json as {key, property, check} — keyed like balloon numbers.
    You are the independent measurer; a different instrument family from the producer.
    {% elif stage == 3 %}
    python3 "{score_dir}/scripts/reference-freeze.py" "{{ workspace }}" \
      --config-fingerprint config-fingerprint.json --manifest characterization.json
    {% elif stage == 4 %}
    Produce instance {{ instance }}. Then run the manifest checks against your own output:
    python3 "{score_dir}/scripts/manifest-runner.py" "{{ workspace }}/reference/manifest.json" \
      "{{ workspace }}/out-{{ instance }}/" --emit-report
    {% endif %}

validations:
  - type: file_exists
    path: "{workspace}/reference/manifest.json"
    condition: "stage == 3"
  - type: command_succeeds
    # the manifest-runner: the ONE deterministic loop over keyed checks per instance
    command: 'python3 {score_dir}/scripts/manifest-runner.py {workspace}/reference/manifest.json {workspace}/out-{instance}/ --check-only'
    condition: "stage == 4"
```

**Near-miss:** spot-checking 5% of volume randomly — sampling where a reference manifest would be total; you learn the population's mood, not its conformance.

**Example.** Generating 200 localized versions of a product page: one version is deeply characterized (terminology, tone, layout, legal lines — each keyed); the manifest becomes the acceptance suite; the remaining 199 are validated by executing those keyed checks. Source copy changes → hash check forces delta characterization of exactly the changed lines.

---

## The Skeptical Oracle

---
name: "The Skeptical Oracle"
scale: score-level
status: working
forces: ["Structured Disagreement", "Information Asymmetry"]
generators: ["G2 The Unreliable Narrator", "G6 Distributed Ignorance"]
problem: "Vendor-diverse advisors' findings cannot enter the record without importing their hallucinations."
signals:
  - "vendor-diverse review fan-outs"
  - "LLM-judge ensembles judging anything mechanically reproducible"
  - "you want the union of different models' coverage without inheriting any model's failures"
stages:
  - name: propose
    sheets: fan_out(3)
    instrument_guidance: "N heterogeneous instruments (opus / codex-cli / glm), each REQUIRED to attach a reproduction pointer to every finding"
    fallback_friendly: true
    purpose: "Propose findings with reproduction pointers — never conclusions."
  - name: reconstruct
    sheets: 1
    instrument_guidance: "instrument: cli — runs every pointer; the test fails or the finding is dropped"
    fallback_friendly: false
    purpose: "Deterministic reconstruction into a typed verified-findings manifest."
  - name: interpret
    sheets: 1
    instrument_guidance: "any AI family — interprets the VERIFIED manifest only; OPTIONAL consumer, not part of the oracle proper"
    fallback_friendly: true
    purpose: "Severity, narrative, ordering of verified facts — never generation of them."
dependencies:
  reconstruct: [propose]
  interpret: [reconstruct]
composes_with:
  - pattern: "Proof-Carrying Artifact"
    how: "substitution — the oracle is PCA applied to peer review"
  - pattern: "Immune Checkpoint"
    how: "layering — recall-side harvest here; precision-side gate there; the pair covers both directions of reviewer error"
---

**Status:** Working. **Source:** Isabelle/Sledgehammer's untrusted provers. **Scope corrected per Review 2** (the interpretation stage is an optional consumer) **and Review 3** (the oracle must not price out a free-local run).

**Core Dynamic.** N vendor-diverse advisors propose; a deterministic reconstructor disposes. Nothing any advisor says enters the record until it can be *reproduced* — re-derived by a cheap, mechanical process the advisors cannot influence. Heterogeneity is harvested, not trusted: the point of different model families is that they fail differently; the point of reconstruction is that their different failures never become the record's failures. Crucially this is *not* a vote or quorum: voting asks advisors to check each other (peer trust); reconstruction asks a deterministic instrument to check them all (no peer trust at all). Sledgehammer's own numbers set expectations: reconstruction fails about 5% of the time, and those proofs are simply not added.

**The reproduction pointer is a schema, not prose (Review 3):** `{finding_id, kind: failing_test|lint_rule|grep_invariant|reproducer_script, ref: "tests/test_x.py::test_y" | "rule-id" | "pattern + path" | "scripts/repro-N.sh", expected: fail|violation}`. A finding without a pointer is not weakly verified — it is a lead.

**The single-family degraded mode (Review 3):** when only one vendor is available (free-local runs), run N instances of that one family with **disjoint question ownership** — each instance reviews a disjoint slice, so independence of *coverage* is preserved even though independence of *failure* is not. The output is labeled `independence: question-disjoint-single-family` — honest about being the weaker claim. Do not silently relabel it vendor-diverse.

**When to use:** vendor-diverse review fan-outs; ensembles judging anything mechanically reproducible.

**When NOT to use:** claims that are not reconstructible — style judgments, strategy recommendations — where the deterministic reproducer cannot exist, and pretending to have one yields a filter that passes only trivia. Reconstruction as expensive as solving (keep the reconstruction path cheaper than the search). A single advisor (nothing to integrate; verify directly).

**Marianne Score Structure**

```yaml
movements:
  1: { name: propose }
  2: { name: reconstruct, instrument: cli }
  3: { name: interpret }

sheet:
  total_items: 3
  fan_out: { 1: 3 }
  dependencies: { 2: [1], 3: [2] }
  per_sheet_fallbacks: { 2: [] }        # if the deterministic checker is down, the score stops

instruments:
  glm: { profile: opencode, config: { model: "zai-coding-plan/glm-5.3-flash" } }
instrument_map:
  opus: [1]                              # movement 1 instance routing via instruments +
  codex-cli: [1]                         # fan-out; vendor diversity constructed in config,
  glm: [1]                               # where it is inspectable

prompt:
  template: |
    {% if stage == 1 %}
    Review the subject. EVERY finding must carry a reproduction pointer:
    {finding_id, kind: failing_test|lint_rule|grep_invariant|reproducer_script, ref, expected}.
    Findings without pointers are leads, not findings.
    {% elif stage == 2 %}
    bash "{score_dir}/scripts/reproducer-harness.sh" "{{ workspace }}/findings" \
      --run-all-pointers --emit "{{ workspace }}/verified-manifest.json" \
      --quarantine "{{ workspace }}/leads-quarantine.jsonl"
    {% elif stage == 3 %}
    Interpret {{ workspace }}/verified-manifest.json: severity, narrative, ordering.
    You are reading VERIFIED facts. Unverified leads in the quarantine file are
    visible but never confusable with findings.
    {% endif %}

validations:
  - type: command_succeeds
    command: 'bash {score_dir}/scripts/reproducer-harness.sh {workspace}/findings --check-only'
    condition: "stage == 2"
  - type: content_regex
    pattern: "repro_id: [A-Za-z0-9_-]+"     # a finding without a reproducer binding is inadmissible
    path: "{workspace}/verified-manifest.json"
    condition: "stage == 2"
```

**Near-miss:** a majority vote across three vendors — peer trust dressed as verification; two coordinated hallucinations outrank one truth.

**Example.** Cross-model code review for a release gate: three families review the diff; only findings that trigger a failing test, a linter rule, or a grep-able invariant violation survive into the report; two other families rank the verified findings for release notes. Unverified hunches sit in a clearly labeled leads file — useful, honest, never confusable with findings.

---
# Concert-Level Patterns

## Negative-Treatment Watch

---
name: "Negative-Treatment Watch"
scale: concert-level
status: working
forces: ["Accumulated Signal", "Progressive Commitment"]
generators: ["G5 Mutable Truth"]
problem: "Admitted claims silently rot as their external sources move, and derived work keeps building on stale truth."
signals:
  - "long-lived corpora whose truth depends on mutable externals"
  - "legal research, scientific claim bases, compliance baselines, dependency manifests, docs with code anchors"
  - "a missed audit cycle must be visible, not silent"
stages:
  - name: sweep
    sheets: 1
    instrument_guidance: "instrument: cli — deterministic fetch/hash of every anchored source, hard-bounded per cycle"
    fallback_friendly: false
    purpose: "Detect source drift; count flag rate."
  - name: adjudicate
    sheets: 1
    instrument_guidance: "any AI instrument — reviews ONLY flagged claims (few, cheap)"
    fallback_friendly: true
    purpose: "Does the negative treatment touch the issue our claim relies on?"
  - name: quarantine
    sheets: 1
    instrument_guidance: "instrument: cli — moves flagged claims; enumerates dependents from the claim graph"
    fallback_friendly: false
    purpose: "Quarantine + blast-radius enumeration; hold auto-quarantine when flag rate exceeds threshold."
dependencies:
  adjudicate: [sweep]
  quarantine: [adjudicate]
composes_with:
  - pattern: "The Errata Ledger"
    how: "prerequisite — decay detection feeds corrections"
  - pattern: "Flight Rules"
    how: "substitution — effectivity pinning is the same lease applied to configuration"
  - pattern: "Proof-Carrying Artifact"
    how: "prerequisite — the anchors it audits are PCA claim-form bundles"
---

**Status:** Working. **Source:** Shepard's/KeyCite citators; PubMed linked errata; CVE feeds. Runs on a leased `schedule`.

**Core Dynamic.** Admission is not permanence. The brief is filed, the magazine printed, the claim enters canon — and the world keeps moving: courts overrule, journals retract, dependencies patch. The citator's move turns the citation graph into a *decay detector*: every admitted claim holds a **validity lease**, renewed by a recurring audit against the current state of its sources. Staleness is made loud instead of impossible — the flag, not the silence, is the product. Because citators demonstrably disagree (two independent authorities agreed on negative treatment in only 53 of the relationships each identified), the watch cross-checks rather than trusts one probe.

**The claim graph (Review 2's requirement):** the ledger is not a flat list. Every claim carries `{id, source_anchor: {path, digest}, dependents: [claim-ids...]}` — source anchors so drift is mechanically detectable, dependent edges so blast radius is enumerable. Without dependent edges, quarantine is detection without consequence.

**Mass invalidation is a different event from fifty independent ones:** when the flag rate exceeds threshold, the sweep script **holds auto-quarantine** and escalates to a re-tiering decision — mass invalidation means the premise changed, not fifty claims. (This hold is enforced by the deterministic sweep script comparing counts — Review 1's correction: `circuit_breaker` accepts sheet-failure counts only, and is wired for exactly that.)

**When to use:** long-lived corpora whose truth depends on mutable externals.

**When NOT to use:** sources are immutable or self-contained (nothing to watch). The schedule runs without a durable lease — a missed cycle must be *visible*, or staleness returns silently through the gap. Alert fatigue: if every cycle flags half the corpus, readers stop reading. One probe trusted alone.

**Marianne Score Structure**

```yaml
schedule:
  interval: 7d
  timezone: "Europe/Amsterdam"
  overlap: skip
  misfire: skip

movements:
  1: { name: sweep, instrument: cli }
  2: { name: adjudicate }
  3: { name: quarantine, instrument: cli }

sheet:
  total_items: 3
  dependencies: { 2: [1], 3: [2] }
  per_sheet_fallbacks: { 1: [], 3: [] }

prompt:
  template: |
    {% if stage == 1 %}
    bash "{score_dir}/scripts/source-sweep.sh" "{{ workspace }}/claim-ledger.json" \
      --refetch --rehash --flag-drift --flag-rate-hold-threshold 0.10 \
      --max-wall 600
    {% elif stage == 2 %}
    Adjudicate ONLY the claims flagged in {{ workspace }}/flagged.json (they are few).
    For each: does the negative treatment touch the issue our claim relies on?
    Verdict QUARANTINE or RETAIN, with the touched issue named.
    {% elif stage == 3 %}
    bash "{score_dir}/scripts/quarantine.sh" "{{ workspace }}/claim-ledger.json" \
      "{{ workspace }}/adjudications.json" --enumerate-dependents
    {% endif %}

validations:
  - type: command_succeeds
    command: 'test -s "{workspace}/sweep-report.json"'
    condition: "stage == 1"
  - type: file_exists
    path: "{workspace}/lease-record.json"
    condition: "stage == 1"            # a cycle that ran without touching leases is a fabrication
  - type: content_regex
    pattern: "dependent(s)?: \\[.+\\]|no dependents"
    path: "{workspace}/quarantine-report.md"
    condition: "stage == 3"            # every quarantined claim appears WITH its blast radius or its absence
```

**Near-miss:** a nightly "sources changed" digest email — detection without dependent enumeration or quarantine is weather reporting.

**Example.** An internal API-docs corpus where every code sample anchors to a repository path and commit SHA: the weekly watch detects upstream API changes, quarantines samples whose anchors broke, and enumerates every tutorial page that embeds them.

---

## Canon of Phases

---
name: "Canon of Phases"
scale: concert-level
status: working
forces: ["Partial Failure", "Finite Resources"]
generators: ["G3 Mortal Executors", "G6 Distributed Ignorance"]
problem: "A continuous stream of work outlives any single worker's endurance — context, budget, or lease — and restarts from zero at every boundary."
signals:
  - "an always-on triage queue, rolling literature watch, moderation across a day, long migrations in shifts"
  - "the stream must never restart from zero"
  - "no single score should run for a day straight"
stages:
  - name: accept
    sheets: 1
    instrument_guidance: "interchangeable with the other phases — the SAME part; instrument diversity is a DEFECT here"
    fallback_friendly: true
    purpose: "Read the latest handoff packet; verify beat continuity; write accepted-through. No packet and not rotation zero = STOP."
  - name: work
    sheets: 1
    instrument_guidance: "same instrument as every other phase — interchangeability is the design"
    fallback_friendly: true
    purpose: "Process queue items from the packet's cursor to this phase's soft stop."
  - name: hand-off
    sheets: 1
    instrument_guidance: "same instrument; writes the packet"
    fallback_friendly: true
    purpose: "Write open items, in-flight state, last beat, cursor, incident notes."
dependencies:
  work: [accept]
  hand-off: [work]
composes_with:
  - pattern: "Positive Transfer"
    how: "layering — the boundary contains the transfer dialogue compressed into one packet"
  - pattern: "Replication Licensing"
    how: "layering — the packet boundary carries license state"
---

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

---

# Adaptation Patterns

## The Fencing Token

---
name: "The Fencing Token"
scale: adaptation
status: working
forces: ["Partial Failure", "Progressive Commitment"]
generators: ["G3 Mortal Executors", "G1 Irreversibility"]
problem: "A paused or retried executor cannot observe its own expiry and silently overwrites newer work with older, slower work."
signals:
  - "a shared mutable surface two sequenced executors may touch"
  - "workspace regions republished by a retry after timeout"
  - "scheduled jobs whose lease lapsed while the job kept running"
stages:
  - name: grant
    sheets: 1
    instrument_guidance: "instrument: cli — atomically increments the counter and stamps run identity"
    fallback_friendly: false
    purpose: "Issue the monotonic token as a workspace file."
  - name: guarded-work
    sheets: 1
    instrument_guidance: "any AI instrument; reads the token FILE and embeds it in every artifact manifest"
    fallback_friendly: true
    purpose: "Do the work with the token embedded in outputs."
  - name: admit-gate
    sheets: 1
    instrument_guidance: "instrument: cli — compares embedded token against the current counter"
    fallback_friendly: false
    purpose: "Reject stale writes at the boundary."
dependencies:
  guarded-work: [grant]
  admit-gate: [guarded-work]
composes_with:
  - pattern: "Self-Stabilizing Custody"
    how: "layering — bounds the convergence window's misbehavior"
  - pattern: "Replication Licensing"
    how: "substitution — same family (physical authority), different primitive: ordering defense vs exactly-once consumption (seam stated in both)"
---

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

---

## The Black-Box Ledger

---
name: "The Black-Box Ledger"
scale: adaptation
status: working
forces: ["Partial Failure", "Accumulated Signal"]
generators: ["G3 Mortal Executors", "G2 The Unreliable Narrator"]
problem: "After the executor dies, what happened is knowable only from survivor testimony — reconstructed memory — unless a channel that does not share the executor's fate recorded it continuously."
signals:
  - "any long orchestration whose post-failure value depends on knowing what actually happened"
  - "production incidents, adversarial review concerts, audit trails"
  - "failure analysis must be grounded rather than narrated"
stages:
  - name: continuous-record
    sheets: 1
    instrument_guidance: "the work movements themselves — wired with auto_capture_stdout and named capture_files"
    fallback_friendly: true
    purpose: "Write all along, to media that survive the crash."
  - name: correlated-readout
    sheets: 1
    instrument_guidance: "any AI instrument — reads the BUNDLED packet, never one channel"
    fallback_friendly: true
    purpose: "Interpret evidence read as a bundle, because evidence read alone lies."
dependencies:
  correlated-readout: [continuous-record]
composes_with:
  - pattern: "Flight Rules"
    how: "prerequisite — the packet's failure signature feeds the rule matcher"
  - pattern: "The MIST Card"
    how: "layering — the card rides the packet"
  - pattern: "Positive Transfer"
    how: "prerequisite — unaccepted offers feed the failure packet"
---

**Status:** Working. **Source:** ICAO Annex 13 recorder custody; incident scribe channels; WAL/journaling filesystems.

**Core Dynamic.** After the executor dies, there are exactly two ways to know what happened: reconstruction from survivor testimony, or playback of a record written continuously by a channel that does not share the executor's fate. Every serious safety domain chose the second, in a specific shape: the recorder is not triggered by the crash — it writes all along, to crash-protected media, on power independent of what crashes; **survival is structural, not reactive** (Review 2's fate-separation demand, stated as a requirement: a log buffer inside the dying process shares fate and is a diary, not a recorder).

**Fate separation, concretely:** the conductor outlives the sheets and is the independent power bus; workspace state is the crash-protected medium; workspace archival is the secondary recorder. The authorable half is the capture wiring and the correlated-readout discipline; the packet assembly is engine-supplied by the durable `on_failure` hook (Review 3's honesty: a score author benefits from it, they do not build it).

**The correlation rule is the deep one:** evidence travels in bundles, and the bundle composition is mandated, because evidence read alone lies (flight-data readout without the cockpit-voice channel misleads, and voice without data misleads differently). And settlement must not launder the failure: **the original error travels verbatim.**

This is the fifth failure class — terminal custody — completing the table:

| Class | v4 pattern | What it owns | What it cannot answer |
|---|---|---|---|
| Task repair | Andon Cord | The moment of detection | Who holds the work while the human is en route |
| Batch quarantine | Dead Letter Quarantine | The poisoned item | What happens downstream of the hole |
| Infrastructure failover | Circuit Breaker | The route | What happens when there is no alternate path |
| Side-effect compensation | Saga Compensation Chain | The undo | The evidence of what happened before the undo |
| **Terminal custody** | **Black-Box Ledger (this)** | **The job itself, after the executor is gone** | — |

**When to use:** any long orchestration whose post-failure value depends on knowing what actually happened.

**When NOT to use:** the logger shares fate with the thing logging. The record is reconstructed afterward from memory — that is testimony, and testimony is what the recorder exists to replace. Volume drowns signal (bounded overwrite is a design feature — tune `max_output_chars`/`lookback_sheets`). Evidence is editable after the fact — a mutable black box is a diary.

**Marianne Score Structure**

```yaml
cross_sheet:
  auto_capture_stdout: true            # continuous write — every sheet, all along
  max_output_chars: 4000               # bounded overwrite is a FEATURE
  lookback_sheets: 5
  capture_files: ["*-report.json", "*.jsonl"]

movements:
  1: { name: the-work }
  2: { name: correlated-readout }

sheet:
  total_items: 2
  dependencies: { 2: [1] }

# on terminal failure, the durable on_failure hook assembles ONE evidence packet:
# job identity, chain depth, per-sheet artifacts so far, cost spent, and the ORIGINAL
# error verbatim — engine-supplied custody; the score's job is to have recorded.

prompt:
  template: |
    {% if stage == 1 %}
    Do the work. Write {{ workspace }}/*-report.json as you go — the recorder is
    your ordinary output discipline, not an extra channel you remember at the end.
    {% elif stage == 2 %}
    Read the failure packet as a BUNDLE: logs + artifacts + config hash + instrument
    identities. No channel alone. Ground every claim in the packet's bytes and cite
    the packet path per claim.
    {% endif %}

validations:
  - type: file_exists
    path: "{workspace}/failure-packet/manifest.json"
    condition: "stage == 2"
  - type: command_succeeds
    # the original error string is present UNMODIFIED — settlement does not launder failure
    command: 'bash {score_dir}/scripts/packet-integrity.sh "{workspace}/failure-packet" --verbatim-error'
    condition: "stage == 2"
```

**Near-miss:** stderr tee'd to a log file in the same process — the recorder shares fate with the crash, surviving nothing.

**Example.** A nightly data-pipeline concert dies at 03:00 when an API credential expires mid-sheet. The on-duty engineer does not interview the half-finished agents — they open the packet: which sheets completed, what each wrote, the exact 401s in order, the config hash that was live. The evidence was assembled before anyone woke up.

---

## Flight Rules

---
name: "Flight Rules"
scale: adaptation
status: working
forces: ["Exponential Defect Cost", "Accumulated Signal"]
generators: ["G1 Irreversibility", "G5 Mutable Truth"]
problem: "Under failure, deliberation is the enemy: the response is re-derived under duress instead of looked up from pre-negotiated, versioned condition-action bindings."
signals:
  - "the same failures recur and the correct response is knowable in advance"
  - "incident response, failure recovery, go/no-go criteria"
  - "a responder who reasons for ten minutes where reading for ten seconds would do"
stages:
  - name: rule-corpus
    sheets: 1
    instrument_guidance: "any AI instrument — authors one YAML per rule under change control"
    fallback_friendly: true
    purpose: "Maintain the rule corpus: id, machine-checkable condition, action, rationale, effectivity, revision history."
  - name: handler
    sheets: 1
    instrument_guidance: "AI matching confined to signature PROPOSAL; deterministic selection for high-risk classes"
    fallback_friendly: true
    purpose: "Match the failure signature; execute; CITE rule IDs in output."
  - name: change-board
    sheets: 1
    instrument_guidance: "instrument: cli — serialized board applies deltas as new versions"
    fallback_friendly: false
    purpose: "Rule deltas from every incident; never edit history."
dependencies:
  handler: [rule-corpus]
  change-board: [handler]
composes_with:
  - pattern: "The Black-Box Ledger"
    how: "prerequisite — the packet's failure signature feeds the matcher"
  - pattern: "The MIST Card"
    how: "prerequisite — a rule action colliding with a recorded failed remedy is a rule-delta signal"
  - pattern: "After-Action Review (v4 archive)"
    how: "prerequisite — the AAR's output artifact becomes the delta"
---

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
  # THE grounding validation, shown concretely (Review 3): every cited rule ID must
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

---

## Self-Stabilizing Custody

---
name: "Self-Stabilizing Custody"
scale: adaptation
status: working
forces: ["Partial Failure", "Convergence Imperative"]
generators: ["G3 Mortal Executors", "G6 Distributed Ignorance"]
problem: "Crash, corruption, and restart are treated as exceptional events requiring an exceptional recovery protocol, when they are just arbitrary states the ordinary rules should leave."
signals:
  - "conductor restarts mid-concert; workspaces resumed after host failure"
  - "global rollback costs more than local re-derivation"
  - "recovery from PARTIALLY corrupt state — where checkpoint-restore fails"
stages:
  - name: predicates
    sheets: 1
    instrument_guidance: "instrument: cli — each sheet's completion claim is script-checkable from disk"
    fallback_friendly: false
    purpose: "Define legitimacy: output artifact exists, digest matches journal, no later entry supersedes it."
  - name: local-correction
    sheets: 1
    instrument_guidance: "the recovered sheets themselves — each re-derives ONLY its own legitimacy"
    fallback_friendly: true
    purpose: "Re-run if illegitimate; never reset a sibling."
  - name: closure
    sheets: 1
    instrument_guidance: "instrument: cli — fan-in proceeds only over legitimately-done predecessors"
    fallback_friendly: false
    purpose: "Verify closure: every predecessor legitimate or visibly skipped."
dependencies:
  local-correction: [predicates]
  closure: [local-correction]
composes_with:
  - pattern: "The Fencing Token"
    how: "layering — MANDATORY wherever side effects exist; bounds the convergence window's misbehavior"
  - pattern: "The Black-Box Ledger"
    how: "prerequisite — the journal legitimacy predicates read"
  - pattern: "Behavioral Pre-Mortem"
    how: "substitution — the kill-injection probe is the pre-mortem's runtime twin"
---

**Status:** Working. **Source:** Dijkstra 1974; Schneider 1993; routing reconvergence.

**Core Dynamic.** Crash, corruption, and restart are not exceptional events requiring an exceptional recovery protocol — they are just "an arbitrary state," which is exactly what the system was designed to leave. The discipline is twofold: write the **legitimacy predicate** first (what counts as healthy, decidable from observable state — for orchestration, decidable *from disk*), then give each component a **local correction rule that moves only its own state toward the predicate**. Nobody performs a global rollback; nobody needs a coherent global snapshot to begin. Recovery is a *property of the ordinary rules*, so the system resumes correctly even when failure detection itself failed. This formalizes the substrate's standing law: scheduler state is a projection; occupancy is re-derived from physical evidence, never trusted from memory.

**Monotone rules and the convergence test (Review 2):** corrections must be monotone — two local corrections must not make each other illegitimate (the metastable-failure guard). And convergence is *tested*, not asserted: a kill-injection probe at each physical interruption point asserts closure and convergence before the pattern is trusted.

**The bounded-misbehavior caveat is constitutive:** self-stabilization *tolerates a bounded period of misbehavior during convergence* — an illegitimate component that can act on the world before correcting must be paired with the Fencing Token. This pairing is mandatory, not advisory, wherever side effects exist.

**When to use:** conductor restarts mid-concert; workspaces resumed after host failure; any long score where global rollback costs more than local re-derivation; recovery from *partially* corrupt state.

**When NOT to use:** predicates not locally decidable — if proving your own legitimacy requires a global snapshot, you have rebuilt the coordination you were avoiding. Correction rules that can oscillate under unfair scheduling (metastable failure; the fix is monotone rules).

**Marianne Score Structure**

```yaml
movements:
  1: { name: predicates, instrument: cli }
  2: { name: local-correction }
  3: { name: closure, instrument: cli }

sheet:
  total_items: 3
  dependencies: { 2: [1], 3: [2] }
  per_sheet_fallbacks: { 1: [], 3: [] }
  skip_when:
    2: { command: 'bash {score_dir}/scripts/legitimacy.sh {workspace} --sheet {{ instance }} --quiet' }
                                          # already-legitimate sheets skip re-derivation

prompt:
  template: |
    {% if stage == 1 %}
    bash "{score_dir}/scripts/legitimacy.sh" "{{ workspace }}" --emit-predicates
    {% elif stage == 2 %}
    Re-derive ONLY your own legitimacy: your output artifact exists, its digest matches
    the journal, no later entry supersedes it. If illegitimate, re-run your work.
    NEVER reset or modify a sibling sheet's state.
    {% elif stage == 3 %}
    bash "{score_dir}/scripts/closure.sh" "{{ workspace }}" --require-legitimate-or-skipped
    {% endif %}

validations:
  - type: command_succeeds
    command: 'bash {score_dir}/scripts/closure.sh {workspace} --check-only'
    condition: "stage == 3"
  - type: file_exists
    path: "{workspace}/recovery-ledger.json"
    condition: "stage == 2"            # which sheets re-derived — auditable, not asserted
```

**Near-miss:** global `rm -rf workspace; rerun` — rollback as recovery, discarding legitimate work at the cost the pattern exists to avoid.

**Example.** An overnight research concert is interrupted by an infrastructure restart at 3 AM: on resume, each in-flight sheet independently determines done/in-progress/not-started from its artifacts and the journal; no coordination phase, no operator triage, no global rollback — coherence is every sheet's local job.

---

## Hutchinson's Warning (Damped Load-Shedding)

---
name: "Hutchinson's Warning"
scale: adaptation
status: working
forces: ["Finite Resources", "Producer-Consumer Mismatch"]
generators: ["G4 Shared Finite Budgets"]
problem: "Negative feedback with lag oscillates: a controller fed by lagged telemetry throttles hard, bursts through, and throttles hard forever."
signals:
  - "a large multi-movement score with a genuinely shared budget — money, wall-clock, or context"
  - "spend telemetry arrives with lag (batched billing, periodic usage polls) — which is everywhere"
  - "feeding work into anything with a real capacity curve: paid APIs, human review, CI pools"
stages:
  - name: trend-probe
    sheets: 1
    instrument_guidance: "instrument: cli — computes the spend-rate EMA from the ledger"
    fallback_friendly: false
    purpose: "Emit capacity-state.yaml {ema, ceiling, rung} — the WRITTEN state the router and prompts cite."
  - name: router
    sheets: 1
    instrument_guidance: "instrument: cli — chooses the rung; down-cross immediate, up-cross after M windows"
    fallback_friendly: false
    purpose: "Translate the damped trend into a declared degradation rung."
  - name: work
    sheets: 1
    instrument_guidance: "rung-dependent: rung 0 full instruments; rung 1 instrument_map routes half the movements cheap; rung 2 scope reduction; rung 3 deferral"
    fallback_friendly: true
    purpose: "Execute under the chosen rung, DECLARED in the state file the prompt cites."
  - name: settle
    sheets: 1
    instrument_guidance: "instrument: cli — appends actuals; the EMA is the only thing the next iteration reads"
    fallback_friendly: false
    purpose: "Close the loop on measured trend, never instantaneous reading."
dependencies:
  router: [trend-probe]
  work: [router]
  settle: [work]
composes_with:
  - pattern: "The Etiquette Law"
    how: "layering — the rungs are instrument tiers on the chain"
  - pattern: "Standby–GO"
    how: "substitution — the hold is degradation rung zero"
---

**Status:** Working. **Source:** Nicholson's 1954 blowfly cultures; the Hutchinson delay-logistic. **Narrowed per Review 2** to its structural identity: *damped delayed-feedback control with asymmetric shed/restore*. The Metered Merge absorption is **reversed** — its ALINEA equation lives in the archive as its own entry (same damping law, applied to admission flow instead of budget), and the seam is stated here and there.

**Core Dynamic.** The deep result of density dependence is not "who gets cut when the food runs out" — that is triage, and v4 owns triage. The deep result is that **negative feedback with delay oscillates**, and the design problem is *damping*: feedback lag longer than the system's natural period generates oscillation (Nicholson's violent ~35-day cycles). Translated: under a hard budget ceiling, sheets are not killed in priority order by a judge stage — they degrade along a ladder each experiences locally, and the controller must measure spend as a **damped trend (EMA)**, never an instantaneous reading. The asymmetry is load-bearing: **shed fast (one measurement window), restore slow (several)** — a controller that restores as eagerly as it sheds is Nicholson's culture in YAML. And the most LLM-specific instance: **context is a habitat** — `lookback_sheets` and `max_output_chars` bound the population of artifacts competing for each consumer's attention, and when density exceeds capacity the failure is quiet: no sheet starves, every sheet gets measurably worse.

**Control wiring, corrected per Review 1:** `circuit_breaker` accepts **sheet-failure counts only** — it is wired for exactly that. Spend ceilings live in `cost_limits`, which *pauses the job* — a different, correct, observable. The rung ladder is neither: it is score-level routing that reads the written `capacity-state.yaml`; the rung is declared in that file — which the prompt cites — so degradation is *declared*, not experienced as mysterious constraint.

**When to use:** large multi-movement scores with a genuine shared budget; lagged telemetry; feeding anything with a real capacity curve.

**When NOT to use:** the resource is not actually shared (per-sheet budgets have no density dependence; a controller there is ceremony). The shed ladder is symmetric (the failure mode restated). The consumer's capacity is constant and known (a static rate or plain stagger is the same thing with less machinery). No honest sensor — feedback on a lied-about occupancy is worse than open loop.

**Marianne Score Structure**

```yaml
cost_limits: { max_cost_usd: 40 }      # the ceiling — pauses the job when hit (its own observable)

movements:
  1: { name: trend-probe, instrument: cli }
  2: { name: router, instrument: cli }
  3: { name: work }
  4: { name: settle, instrument: cli }

sheet:
  total_items: 4
  dependencies: { 2: [1], 3: [2], 4: [3] }
  per_sheet_fallbacks: { 1: [], 2: [], 4: [] }

instruments:
  cheap: { profile: opencode, config: { model: "zai-coding-plan/glm-5.3-flash" } }
instrument_map:
  opus: [3]                             # rung 1 would rewrite this map to route half
  cheap: [3]                            # the movements cheap — routing by WRITTEN state

prompt:
  variables: { ceiling: 40, restore_windows: 3 }
  template: |
    {% if stage == 1 %}
    python3 "{score_dir}/scripts/ema-probe.py" "{{ workspace }}/spend-ledger.jsonl" \
      --alpha 0.3 --ceiling {{ ceiling }} --emit "{{ workspace }}/capacity-state.yaml"
    {% elif stage == 2 %}
    bash "{score_dir}/scripts/rung-router.sh" "{{ workspace }}/capacity-state.yaml" \
      --shed-immediate --restore-after {{ restore_windows }} --emit-rung
    {% elif stage == 3 %}
    You are running at rung {{ rung }} (see {{ workspace }}/capacity-state.yaml — read it):
    0 full instruments, 1 cheap instrument for half the movements, 2 narrower scope,
    3 deferral. The rung is DECLARED state, not a suggestion.
    {% elif stage == 4 %}
    bash "{score_dir}/scripts/settle.sh" "{{ workspace }}/spend-ledger.jsonl" \
      --append-actuals --assert-under-ceiling
    {% endif %}

validations:
  - type: file_exists
    path: "{workspace}/capacity-state.yaml"
    condition: "stage == 2"            # the router cannot run on unwritten state
  - type: command_succeeds
    # THE validation that makes the damping real: down-cross immediate, up-cross after M windows
    command: 'bash {score_dir}/scripts/rung-router.sh {workspace}/capacity-state.yaml --assert-asymmetry'
    condition: "stage == 4"
  - type: command_succeeds
    command: 'bash {score_dir}/scripts/settle.sh {workspace}/spend-ledger.jsonl --check-only'
    condition: "stage == 4"
```

**Worked example with real numbers (Review 3's demand):** a 40-sheet documentation migration under `$40`. The ledger records actual spend per sheet; the EMA (α = 0.3) over the last 5 entries reads $0.82/sheet at sheet 20 — 0.82 × 40 = $32.8 projected, under the $34 shed threshold (0.85 × ceiling): rung 0. At sheet 25, lagged billing catches up: EMA jumps to $0.94/sheet → $37.6 projected → cross → rung 1 **immediately**: sheets 26+ route to the cheap instrument and a reduced `capture_files` list, declared in `capacity-state.yaml`. Occupancy falls; the EMA declines $0.94 → $0.88 → $0.81 over three windows; only when EMA < $28 (0.7 × ceiling) for **three consecutive windows** does the router restore rung 0. No sheet is executed against a wall; the habitat gets honestly poorer, then honestly richer — and the post-hoc assertion `total spend ≤ $40` is checked mechanically at settle.

**Near-miss:** per-sheet budget checks against instantaneous spend — the lagged-telemetry oscillator with extra steps.

---

# Iteration Patterns

## Replication Licensing

---
name: "Replication Licensing"
scale: iteration
status: working
forces: ["Progressive Commitment", "Exponential Defect Cost"]
generators: ["G1 Irreversibility", "G3 Mortal Executors"]
problem: "A cycle counter cannot prevent a side-effectful cycle from happening twice, and naive retries duplicate deployments."
signals:
  - "any self-chaining or recurring score whose work stage has side effects that must be exactly-once per cycle"
  - "deploys, sends, publishes, billing events, state migrations"
  - "a conductor crash mid-stage would otherwise leave 'did the deploy happen?' answerable only by archaeology"
stages:
  - name: restriction-point
    sheets: 1
    instrument_guidance: "instrument: cli — verify inputs, prior completion, and NO unconsumed license; then issue"
    fallback_friendly: false
    purpose: "Issue licenses/cycle-{n}.json naming exactly what it authorizes, by hash."
  - name: work
    sheets: 1
    instrument_guidance: "any AI instrument; its FIRST action is the mv that consumes the license"
    fallback_friendly: true
    purpose: "Consume the license by moving it; possession of the moved file is the proof of authorization."
  - name: mitosis
    sheets: 1
    instrument_guidance: "instrument: cli — verification-only gate on the products"
    fallback_friendly: false
    purpose: "Check products complete and grounded; arm the next restriction point."
dependencies:
  work: [restriction-point]
  mitosis: [work]
composes_with:
  - pattern: "The Fencing Token"
    how: "substitution — same family (physical authority), different primitive: exactly-once consumption vs ordering defense (seam stated in both)"
  - pattern: "Canon of Phases"
    how: "layering — the packet boundary carries license state"
---

**Status:** Working. **Source:** MCM2-7 licensing; geminin's steric blockade; the G1 restriction point. Ranked strongest pattern in the corpus by Review 1: fully expressible today, its atomic `mv`-as-consumption is a real mechanism with a real validation, and it covers a failure class (exactly-once under crash) nothing else owns.

**Core Dynamic.** `max_chain_depth` counts cycles; it cannot prevent a cycle from *happening twice*. The cell solved duplication safety the way orchestration should: the right to do expensive, side-effectful work is a **single-use artifact** that (a) carries provenance — the license names exactly what it authorizes, by hash; (b) is atomically consumed by the act of beginning — the `mv` across a filesystem boundary is the firing; and (c) cannot be re-issued until a checkpoint has verified the products of the last cycle. The anti-relicensing guard is constitutive: refusal is the default state, and permission is the temporary, supervised exception. Crash between start and finish leaves a consumed license and no products — recovery can therefore *tell the difference* between "never started" and "started, died," which is precisely the ambiguity that makes naive retries duplicate deployments.

**When to use:** any self-chaining or recurring score whose work stage has side effects that must be exactly-once per cycle.

**When NOT to use:** purely idempotent work (regenerating a derived file that overwrites in place; a `file_modified` check suffices). License issuance and consumption not *atomically* ordered: issue-then-consume with any gap invites a second consumer to read a still-valid license — the consumption must be the `mv` the work stage itself performs as its first act.

**Marianne Score Structure**

```yaml
schedule:
  interval: 1d
  timezone: "Europe/Amsterdam"
  overlap: skip
  misfire: skip

movements:
  1: { name: restriction-point, instrument: cli }
  2: { name: work }
  3: { name: mitosis, instrument: cli }

sheet:
  total_items: 3
  dependencies: { 2: [1], 3: [2] }
  per_sheet_fallbacks: { 1: [], 3: [] }

prompt:
  template: |
    {% if stage == 1 %}
    bash "{score_dir}/scripts/license-issue.sh" "{{ workspace }}" \
      --verify-inputs --verify-prior-complete --refuse-if-unconsumed \
      --emit licenses/cycle-{n}.json     # {cycle, input_sha256 map, issued_utc, consumer, expires_at}
    {% elif stage == 2 %}
    Your FIRST action: mv {{ workspace }}/licenses/cycle-*.json {{ workspace }}/consumed/
    Then do the expensive work, writing outputs that reference the license's input hashes.
    {% elif stage == 3 %}
    bash "{score_dir}/scripts/mitosis.sh" "{{ workspace }}" \
      --verify-products-grounded --emit-completion-marker
    {% endif %}

validations:
  - type: command_succeeds
    # the atomic move, asserted BOTH ways: consumed present AND licenses/ empty of it
    command: 'test -n "$(ls {workspace}/consumed/cycle-*.json 2>/dev/null)" && test -z "$(ls {workspace}/licenses/cycle-*.json 2>/dev/null)"'
    condition: "stage == 2"
  - type: command_succeeds
    command: 'bash {score_dir}/scripts/mitosis.sh {workspace} --check-only'
    condition: "stage == 3"
```

**Failure wiring:** `mzt recover` finding a consumed license with no products enters resume-or-compensate, never re-license — the "no unconsumed license" check is constitutive and cannot be skipped by configuration.

**Near-miss:** a `deployed.flag` file checked at start — presence-of-marker without atomic consumption re-licenses on every retry; the flag can be read by two consumers at once.

**Example.** A nightly publishing pipeline: build → deploy → notify. The conductor crashes after deploy, before notify. Naive retry redeploys. Under licensing: the license was consumed by deploy; recovery finds consumed-license-without-completion-marker and resumes at notify — the restriction point physically cannot re-issue for cycle n until mitosis verified cycle n's products, and the next license carries n+1's input hashes, which the deploy target will not match if the content did not change.

---

# Within-Stage & Instrument Strategy Patterns

## Designation Is Authorization

---
name: "Designation Is Authorization"
scale: instrument-strategy
status: working
forces: ["Instrument-Task Fit", "Information Asymmetry"]
generators: ["G2 The Unreliable Narrator"]
problem: "Authority expressed as a list of rights the subject names lets authority leak through any confused intermediary."
signals:
  - "mixed-instrument fan-outs where sheets differ in trust"
  - "a cheap summarizer touching sensitive context; tool attachment that must be scoped"
  - "technique/skill injection that must not be ambient"
stages:
  - name: capability-manifest
    sheets: 1
    instrument_guidance: "any AI instrument — authors the per-sheet designation map (this is DESIGN, pre-run)"
    fallback_friendly: true
    purpose: "Declare per sheet: techniques attachments, cadenza directories (exactly one subtree each), spec_tags."
  - name: scoped-execution
    sheets: 1
    instrument_guidance: "the designated sheets — running with only what was handed"
    fallback_friendly: true
    purpose: "Execute with designated context only: undesignated specs are ABSENT, not hidden."
  - name: capability-audit
    sheets: 1
    instrument_guidance: "instrument: cli — dumps every sheet's effective capability set"
    fallback_friendly: false
    purpose: "Make designation inspectable for review."
dependencies:
  scoped-execution: [capability-manifest]
  capability-audit: [scoped-execution]
composes_with:
  - pattern: "Proof-Carrying Artifact"
    how: "layering — evidence bundles as designated context"
  - pattern: "The Etiquette Law"
    how: "layering — instruments as capability endpoints on the chain"
---

**Status:** Working. **Source:** the object-capability model; the confused deputy. **The distinction Review 2 demanded is load-bearing:** conductor-mediated designation scopes **context and attachment** — which spec corpora enter the prompt (`spec_dir` + `spec_tags`: undesignated specs are absent, not hidden), which techniques attach (`skill`/`mcp`/`protocol`, optionally `required`), which cadenza directories are handed. It is **not OS-level capability confinement** of filesystem or tool access: a sheet can still `cat` anything its process can reach. Prompt-injection defense by absence-of-naming is context scoping — real and useful, and the *use* the control plane was built for — but true confinement (sandboxing the process itself) needs engine/runtime work and is recorded in Awaiting Primitives. The pattern's claims stop at the boundary it can enforce today.

**Core Dynamic.** An ACL system says: the subject holds a list of rights and *names* objects to act on — the naming channel is ambient, so authority leaks through any confused intermediary. A capability system says: the only objects that exist for you are the ones you were handed; **designation and authority are the same event**. A sheet given exactly the `docs/` subtree and one read-only protocol technique cannot prompt-inject its way into deploy credentials — not because a rule forbade it, but because those names were never in its world.

**When to use:** mixed-trust fan-outs; scoped tool attachment; non-ambient technique injection.

**When NOT to use:** authority is genuinely global and stable (per-sheet capability sets cost more than the ambient risk). Revocation must propagate instantly through deep delegation chains. (And: you need confinement the conductor cannot mediate — see the boundary above.)

**Marianne Score Structure**

```yaml
spec:
  spec_dir: "{score_dir}/specs"
  spec_tags: { 2: [public-api] }          # the untrusted sheet sees ONLY public-api specs

movements:
  1: { name: capability-manifest }
  2: { name: scoped-execution }
  3: { name: capability-audit, instrument: cli }

sheet:
  total_items: 3
  dependencies: { 2: [1], 3: [2] }
  per_sheet_fallbacks: { 3: [] }
  cadenzas:
    2:
      - directory: "{score_dir}/context/docs-subtree"
        as: context
        required: true                   # exactly one subtree — fail closed when absent

prompt:
  template: |
    {% if stage == 1 %}
    Author {{ workspace }}/capability-map.yaml: per movement, the techniques attachments,
    cadenza directory (exactly one subtree), and spec_tags. Least designation that suffices.
    {% elif stage == 2 %}
    You have been designated: the docs subtree (cadenza) and the public-api spec slice.
    Work within it. Other specs are not hidden from you — they are absent from your world.
    {% elif stage == 3 %}
    python3 "{score_dir}/scripts/capability-render.py" "{score_dir}/this-score.yaml" \
      --dump-effective-sets
    {% endif %}

validations:
  - type: command_succeeds
    # topology check: no two sheets' cadenza directories overlap unless a shared-artifact
    # stage declares the intersection
    command: 'python3 {score_dir}/scripts/capability-render.py {score_dir}/this-score.yaml --assert-no-undeclared-overlap'
    condition: "stage == 3"
```

**Near-miss:** a prompt line "you may only read docs/" — an ACL spoken politely; every other name remains in the sheet's world, waiting for a confused deputy.

**Example.** A security-audit score for a client codebase: an untrusted third-party-model sheet gets only the spec excerpts tagged `public-api` plus a read-only grep protocol; the fixer sheet gets repo-write. When the auditor sheet's prompt is later found to contain injected instructions from a scanned file, the blast radius is what it was designated — nothing.

---

## Immune Checkpoint

---
name: "Immune Checkpoint"
scale: within-stage
status: working
forces: ["Exponential Defect Cost", "Instrument-Task Fit"]
generators: ["G2 The Unreliable Narrator", "G1 Irreversibility"]
problem: "In a system with a powerful reviewer and an automated remediation path, the reviewer is the most dangerous instrument: a false-positive finding triggers rollback or deletion of healthy work."
signals:
  - "adversarial review feeding automated remediation — fix-PRs, scanner-gated deploys, takedowns"
  - "reviewer recall tuned high AND a downstream stage treating findings as verdicts rather than leads"
  - "an AI code reviewer opening fix-PRs directly"
stages:
  - name: adversarial-review
    sheets: 1
    instrument_guidance: "a strong instrument generating findings in a strict schema"
    fallback_friendly: true
    purpose: "Produce {id, claim, location, evidence, proposed_remediation, severity} — high recall, no self-restraint required."
  - name: tolerance-checkpoint
    sheets: 1
    instrument_guidance: "instrument: cli — deterministic, INSIDE the review boundary, before findings are ever emitted as actionable"
    fallback_friendly: false
    purpose: "Ground location against actual bytes; compute blast radius; classify load-bearing. Failed/ambiguous → tolerated, never routed."
  - name: remediation
    sheets: 1
    instrument_guidance: "any AI instrument — receives ONLY the actionable subset"
    fallback_friendly: true
    purpose: "Remediate the bijective actionable set — no more."
dependencies:
  tolerance-checkpoint: [adversarial-review]
  remediation: [tolerance-checkpoint]
composes_with:
  - pattern: "The Skeptical Oracle"
    how: "layering — recall-side harvest there; precision-side gate here; the pair covers both directions of reviewer error"
  - pattern: "Andon Cord (v4 archive)"
    how: "prerequisite — the human summons for ambiguous findings"
---

**Status:** Working. **Source:** regulatory T cells; CTLA-4's higher affinity winning ties. **Plain structural language first (Review 2): this is a precision gate on the critic.** The immunology is illustration, not argument.

**Core Dynamic.** The corpus had adversarial review and gates on the work. It had nothing that gates the **critic** — yet with a powerful reviewer and an automated remediation path, a false-positive finding doesn't waste a cycle, it triggers rollback, churn, or deletion of healthy work. That is autoimmunity, and its prevalence scales with reviewer capability. The checkpoint is an inhibitory gate *inside the review path*: findings cannot trigger destructive remediation until each passes a self-tolerance check — grounding (the cited file:line exists and contains what is claimed), blast-radius computation (the proposed remediation's diff is bounded and touches what the finding names), and load-bearing classification. The constitutive-presence rule is the part worth copying exactly: the checkpoint cannot be configured away, and **on ambiguity it defaults to tolerance** — no action, escalate to a human. The off-signal is designed to win ties. Everything still surfaces — flagged `autoimmune-suspect` rather than `actionable`.

**The recalibration rule, correctly wired (Review 1's fix):** a checkpoint rejecting >80% of findings is itself a finding — the reviewer and the code have diverged and need recalibration, not more rounds. This is enforced by a **deterministic count gate** comparing actionable vs tolerated totals (a script, an exit code), not by `circuit_breaker`, which accepts sheet-failure counts only.

**When to use:** any score where adversarial review feeds automated remediation.

**When NOT to use:** findings are advisory-only and a human reads every one (the checkpoint duplicates the reader). The tolerance check is weaker than the reviewer (a grep that can't see what the finding means will pass plausible nonsense). "Tolerance by default" misread as "review is optional" — the checkpoint suppresses automated *action*, never the finding itself.

**Marianne Score Structure**

```yaml
movements:
  1: { name: adversarial-review }
  2: { name: tolerance-checkpoint, instrument: cli }
  3: { name: remediation }

sheet:
  total_items: 3
  dependencies: { 2: [1], 3: [2] }
  per_sheet_fallbacks: { 2: [] }        # the checkpoint cannot be degraded away

prompt:
  template: |
    {% if stage == 1 %}
    Generate findings in STRICT schema: {id, claim, location, evidence,
    proposed_remediation, severity}. Tune recall high — the checkpoint downstream
    is your precision; do not self-censor.
    {% elif stage == 2 %}
    bash "{score_dir}/scripts/tolerance-checkpoint.sh" "{{ workspace }}/findings.json" \
      --ground-locations --compute-blast-radius --classify-load-bearing \
      --default-to-tolerance --emit "{{ workspace }}/actionable.json" \
      --tolerated "{{ workspace }}/tolerated.jsonl"
    {% elif stage == 3 %}
    Remediate EXACTLY the findings in {{ workspace }}/actionable.json. If you find yourself
    working on something not in that file, stop — the bijection is the contract.
    {% endif %}

validations:
  - type: command_succeeds
    # the bijection is the anti-bypass proof: remediation's input set EQUALS the actionable set
    command: 'bash {score_dir}/scripts/assert-bijection.sh {workspace}/actionable.json {workspace}/remediation-log.json'
    condition: "stage == 3"
  - type: command_succeeds
    # the recalibration gate: a checkpoint rejecting >80% is itself a finding (a count gate,
    # NOT circuit_breaker — the breaker accepts sheet-failure counts only)
    command: 'bash {score_dir}/scripts/recalibration-gate.sh {workspace}/actionable.json {workspace}/tolerated.jsonl --max-rejection-ratio 0.8'
    condition: "stage == 2"
```

**Near-miss:** a second reviewer stage — more judgment layered on judgment; the gate must be a checker, not another critic.

**Example.** An automated PR-review agent for a monorepo, recall tuned high, opening fix-PRs directly. Without a checkpoint, one bad afternoon of plausible hallucinated "bugs" reverts healthy code across a dozen services — and the team's rational response is to turn the agent off entirely. With the checkpoint: every finding resolves to real bytes or is tolerated; ambiguous ones sit in a human queue; the fix-PR stream runs at a precision that keeps the automation alive.

---

# Substrate Documentation (engine-supplied, not score-authored)

*Reclassified per Review 3: these mechanisms are the engine's, not the score author's. A score author benefits from them and wires into them; presenting them as authorable patterns misleads a newcomer into hunting for YAML that isn't theirs to write.*

**Claim custody (the Accountability Board's engine half).** The conductor's governing law, earned in blood: a durable row that says work began is not custody of the actual process; **custody belongs to the semantic result, not the process status** — errors observed at exit 0 are still failing. Cancellation must kill and reap the actual child process group while atomically writing a terminal settlement that does not launder the original error; a restarted conductor must reject stable-ID replacement of an incomplete claim; recovered hooks must retain their configured depth/cooldown/workspace semantics across restart.

**The terminal-failure packet (the Black-Box Ledger's engine half).** The durable `on_failure` hook assembles the evidence packet atomically: job identity, chain depth, per-sheet artifacts, cost spent, the original error verbatim — with restart reconciliation and same-ID protection so duplicate external effects are impossible.

**The rendered graph.** `mzt validate` (YAML syntax, Pydantic schema, extended semantics) plus DAG visualization is the render surface Behavioral Pre-Mortem builds on; programmatic JobConfig dry-rendering for concurrency/ancestry audits is established discipline.

**What is still missing (the score-facing half of the Accountability Board, now in Awaiting Primitives):** a score-facing export of the conductor's claim table with physical process handles, so a PAR sweep can reconcile registry against handles without owning the processes. Until it exists, the authorable approximation is documented under Awaiting Primitives.

---
# Substrate Availability Matrix

*The unanimous demand of all three reviews. Every pattern declares what the substrate provides today. "Real keys" = engine fields verified this iteration. "Scripts" = user-supplied deterministic scripts from the Script Library. "Engine work" = blocked on substrate features that do not exist.*

| Pattern | Status | Real keys consumed | Scripts required | Engine work needed |
|---|---|---|---|---|
| The Etiquette Law | working | `instrument: cli`, `per_sheet_fallbacks: []`, `command_succeeds` | run-gates.sh | none |
| Fan-out + Synthesis | working | `fan_out`, `dependencies`, `capture_files` | none | none |
| Proof-Carrying Artifact | working | `per_sheet_fallbacks`, `required: true` cadenzas, static `fan_out` | anchor-extractor.py, evidence-gate.sh | data-driven fan-out width (would remove batching) |
| Positive Transfer | working | `max_wall_seconds`, `on_failure`, `capture_files` | handoff-gate.sh | none |
| The MIST Card | **approximation** | `required: true` cadenzas | attempt-wrapper.sh, fingerprint-collision.py | per-attempt retry hooks (conductor-internal retries out of scope) |
| Fork-Evident History | working | (git, or) `command_succeeds` | journal-verify.py | none |
| The Errata Ledger | working | `per_sheet_fallbacks: []` | errata-commit.py | none |
| Standby–GO | working | `skip_when` (command form), `max_wall_seconds`, `per_sheet_fallbacks: []` | arm-gate.sh, go.sh | none |
| The Attested Merge Gate | working | `spec_dir`/`spec_tags`, `skipped_upstream` | compat-sweep.sh, full-suite.sh | per-sheet worktree isolation (job-level chaining is the available form) |
| Join-Semilattice Merge | working | static `fan_out`, instance-tagged namespaces | idempotence-probe.sh | none |
| Behavioral Pre-Mortem | working | `mzt validate` DAG render, JobConfig | invariant-check.py | none |
| First Article Characterization | working | `skip_when` (command form), static `fan_out` | reference-freeze.py, manifest-runner.py | none |
| The Skeptical Oracle | working | `instrument_map`, static `fan_out`, `per_sheet_fallbacks: []` | reproducer-harness.sh | none |
| Negative-Treatment Watch | working | leased `schedule` (interval/cron, IANA tz, overlap/misfire), `max_wall_seconds` | source-sweep.sh, quarantine.sh | none |
| Canon of Phases | working | leased `schedule`, `overlap: skip`, IANA `timezone` | packet-gate.sh | none (multi-deployment topology) |
| The Fencing Token | working | `max_wall_seconds`, workspace files | token-grant.sh, token-admit.sh | none |
| The Black-Box Ledger | working | `auto_capture_stdout`, `capture_files`, `max_output_chars`, `lookback_sheets`, durable `on_failure` | packet-integrity.sh | none (packet assembly is engine-supplied) |
| Flight Rules | working | `spec_dir`/`spec_tags`, `command_succeeds` | rule-board.sh | none |
| Self-Stabilizing Custody | working | `skip_when` (command form), `mzt recover` | legitimacy.sh, closure.sh | none |
| Hutchinson's Warning | working | `cost_limits`, `instrument_map`, `max_output_chars`, `lookback_sheets` | ema-probe.py, rung-router.sh, settle.sh | per-window spend telemetry (ledger discipline substitutes) |
| Replication Licensing | working | leased `schedule`, `mzt recover`, `max_chain_depth` | license-issue.sh, mitosis.sh | none |
| Designation Is Authorization | working | `spec_dir`/`spec_tags`, `techniques` (skill/mcp/protocol, `required`), cadenza `directory` | capability-render.py | OS-level capability confinement (context designation is what exists) |
| Immune Checkpoint | working | `per_sheet_fallbacks: []` | tolerance-checkpoint.sh, assert-bijection.sh, recalibration-gate.sh | none |

**Patterns NOT in core because the substrate lacks their primitive** (see Awaiting Primitives): Zeitgeber Entrainment (offset-from-heartbeat scheduling), the Accountability Board's score-facing sweep (claim-table export), MIST Card's conductor-retry feeding, true capability confinement.

---

# The Script Library

*Promoted from open question to core deliverable (Reviews 1 and 3). The corpus's entire determinism story rests on these twelve scripts; before this section they were "an unnamed file on the reader's machine." Interface contracts follow; the library is v6's blocking deliverable and lives at `{score_dir}/scripts/` in every proof score.*

| Script | Consumed by | Interface contract |
|---|---|---|
| `run-gates.sh` | Etiquette Law | `run-gates.sh <workspace> --lint --schema --tests` → exit 0 iff all gates pass; writes `gate-report.json` |
| `anchor-extractor.py` | PCA (claim form) | `anchor-extractor.py <deliverable.md>` → claim-ledger JSON on stdout; `--check` re-validates extraction |
| `evidence-gate.sh` | PCA (proof form) | `evidence-gate.sh <evidence-dir> [ledger] [verdicts]` → re-hashes every digest; exit nonzero on mismatch; `--check` re-verify only |
| `handoff-gate.sh` | Positive Transfer | `handoff-gate.sh --state-machine <handoff.json>` → asserts release>accept>offer, no regressions, single acceptance per id |
| `attempt-wrapper.sh` | MIST Card | `attempt-wrapper.sh <item> -- <command>` → appends ledger row (error_class, remedy fingerprint, outcome), then execs; appends result row |
| `fingerprint-collision.py` | MIST Card | `fingerprint-collision.py <ledger> <proposed> [--reject-on-collision]` → sha256 over normalized(error_class, tool+args, target_path) |
| `journal-verify.py` | Fork-Evident History | `journal-verify.py <journal.jsonl> --recompute --assert-append-only --require-supersedes-on-corrections` |
| `errata-commit.py` | Errata Ledger | `errata-commit.py <workspace> --canon <f> --ledger <l>` → atomic pair write; `--verify-join` asserts new_hash = sha256(canon) |
| `arm-gate.sh` / `go.sh` | Standby–GO | arm: `--cue N --require-ready K --validate-artifacts` → writes armed-N.json; go: refuses unless armed, refuses duplicate cue, mv's the pointer |
| `compat-sweep.sh` | Attested Merge Gate | `compat-sweep.sh <work> --contract <dir> --schema --typecheck --tests` → sweep-report.json |
| `idempotence-probe.sh` | Join-Semilattice Merge | runs the join twice into scratch; `diff` must be empty |
| `invariant-check.py` | Behavioral Pre-Mortem | typed graph schema in, `--emit-counterexamples` out (ordered event lists, not prose) |
| `reference-freeze.py` / `manifest-runner.py` | First Article | freeze: stamp config hash into reference; runner: `manifest-runner.py <manifest> <out-dir> --check-only` loops keyed checks per instance |
| `reproducer-harness.sh` | Skeptical Oracle | runs every reproduction pointer; emits verified-manifest + leads-quarantine |
| `source-sweep.sh` / `quarantine.sh` | Negative-Treatment Watch | sweep: refetch/rehash/flag-drift with `--flag-rate-hold-threshold`; quarantine: moves claims, enumerates dependents |
| `packet-gate.sh` | Canon of Phases | asserts accepted-through predates results; monotonic beat; rotation-zero exactly once |
| `token-grant.sh` / `token-admit.sh` | Fencing Token | grant: atomic increment + run-id stamp; admit: `--reject-stale` on embedded token < counter |
| `packet-integrity.sh` | Black-Box Ledger | `--verbatim-error` asserts the original error string present unmodified |
| `rule-board.sh` | Flight Rules | `--apply-as-new-versions --contradiction-review`; refuses history edits |
| `legitimacy.sh` / `closure.sh` | Self-Stabilizing Custody | per-sheet predicate check from disk; closure requires legitimate-or-visibly-skipped |
| `ema-probe.py` / `rung-router.sh` / `settle.sh` | Hutchinson's Warning | EMA from ledger; rung with `--assert-asymmetry` (down immediate, up after M); settle appends actuals, asserts under ceiling |
| `license-issue.sh` / `mitosis.sh` | Replication Licensing | issue: refuse-if-unconsumed; mitosis: verify products grounded, emit completion marker |
| `capability-render.py` | Designation Is Authorization | dumps effective capability sets; `--assert-no-undeclared-overlap` |
| `tolerance-checkpoint.sh` / `assert-bijection.sh` / `recalibration-gate.sh` | Immune Checkpoint | ground/blast-radius/classify with `--default-to-tolerance`; bijection assert; `--max-rejection-ratio 0.8` |

**Standing rule:** a pattern referencing a script not in this table is incomplete, and a proof score shipping a pattern without its script is unproven.

---

# The Proof Program

*All three reviews found the proof corpus broken in the same ways. Dispositions are now explicit; the queue is prioritized; proof coverage is a **blocking requirement for v6** (Review 1: "a pattern without a buildable score is a hypothesis").*

**State found:** six proof scores exist; all six prove **v4** patterns; zero prove any v5/v5.1 core pattern. Clusters: security-audit ×2 (echelon-repair, immune-cascade — the same problem shape, and immune-cascade still recommends the retired gemini-cli), codegen-with-gates ×3 (shipyard-sequence — a documented-flawed proof left standing — prefabrication, dead-letter-quarantine), claim-verification ×1 (source-triangulation — orchestration-identical to Fan-out + Synthesis; never exercises reconstruction). Every proof resolves to a single instrument (`claude-code`): C8's vendor diversity has never been exercised by any proof in corpus history. All carry dead `../../workspaces/` relative paths and folded-scalar warnings.

| Legacy proof | Disposition |
|---|---|
| shipyard-sequence | **Retire.** Documented-flawed ("a gate described is not a gate executed") and left standing; its honest successor is an Attested Merge Gate proof |
| echelon-repair | **Archive** to the v4 evidence base (proves graduated response) |
| immune-cascade | **Repair** (purge gemini-cli) then archive; name-trap for Immune Checkpoint documented |
| prefabrication | **Archive** — superseded as evidence by the Attested Merge Gate proof (v6) |
| dead-letter-quarantine | **Keep** as v4 evidence (the failure-class table's citation); re-instrument off claude-code-only |
| source-triangulation | **Keep**; re-scoped as Fan-out + Synthesis evidence (its actual structure) |

**v6 proof queue (priority order):** Replication Licensing · Join-Semilattice Merge · Skeptical Oracle (vendor-diverse, finally exercising C8) · Standby–GO · Immune Checkpoint · Proof-Carrying Artifact · Fencing Token · Errata Ledger. Every new proof: auto-derived or `{score_dir}`-anchored workspaces, single-line command scalars (the V303 killer is folded YAML), `command_succeeds` gates wherever a command exists, and its Script Library entries shipped in-score.

---

# Problem → Pattern Selection Table

*Review 3's missing on-ramp. Joined to the v4 selection guide (Appendix A) which remains authoritative for the archive.*

| If your problem is… | Start with | Compose with |
|---|---|---|
| Claims crossing a trust boundary | Proof-Carrying Artifact | Fork-Evident History, Flight Rules |
| Work changing owners | Positive Transfer | Black-Box Ledger |
| A retry that must not re-try a failed remedy | The MIST Card | Flight Rules, Replication Licensing |
| Correcting canon without silent rewrites | The Errata Ledger | Fork-Evident History, Negative-Treatment Watch |
| An atomic cutover under live traffic | Standby–GO | First Article Characterization |
| Parallel writers composing against a contract | The Attested Merge Gate | Join-Semilattice Merge |
| Parallel writers appending additive facts | Join-Semilattice Merge | Fan-out + Synthesis |
| Killing design bugs before the first run | Behavioral Pre-Mortem | The Etiquette Law |
| Validating volume output affordably | First Article Characterization | Skeptical Oracle |
| Harvesting vendor diversity without hallucinations | The Skeptical Oracle | Immune Checkpoint |
| Truth rotting as sources move | Negative-Treatment Watch | The Errata Ledger |
| A stream outliving every worker | Canon of Phases | Positive Transfer |
| A zombie overwriting newer work | The Fencing Token | Self-Stabilizing Custody |
| Knowing what happened after the crash | The Black-Box Ledger | Flight Rules |
| Failures re-argued at 3 AM | Flight Rules | The MIST Card |
| Restart recovery without global rollback | Self-Stabilizing Custody | The Fencing Token |
| Budget oscillation (throttle-burst-throttle) | Hutchinson's Warning | The Etiquette Law |
| A side effect that must happen exactly once | Replication Licensing | Canon of Phases |
| Untrusted sheets near sensitive context | Designation Is Authorization | Proof-Carrying Artifact |
| A reviewer triggering destructive remediation | Immune Checkpoint | The Skeptical Oracle |

**If you're new, start here:** The Etiquette Law → Fan-out + Synthesis → Proof-Carrying Artifact → The Fencing Token → Standby–GO.

---

# Merge Ledger — Disposition of All Candidates

*Nothing is deleted silently; the archive (Appendix A) remains the extended corpus. Corrected count per Review 1: 6 absorbed + 18 archived = **24** iteration-5 candidates dispositioned beyond the core (the draft's closing line said 18 — that error is recorded, not patched).*

### Iteration-5 candidates absorbed as named variants (seam stated inside the absorber)

| Pattern | Absorbed into | The seam that survives |
|---------|---------------|------------------------|
| Annotated Galley | Proof-Carrying Artifact (claim form) | Per-claim fan-out, checkers receive ONLY claim + source; ADMIT/CUT/DEBT |
| Traceability Chain | Proof-Carrying Artifact (pedigree form) | Pedigree answers *where from*; proof answers *why admissible* — different admission checks |
| ~~Metered Merge~~ | ~~Hutchinson's Warning~~ | **ABSORPTION REVERSED per Review 2** — see archived table below |
| Sighted Versions | Standby–GO | Continuous production + serialized promotion; pending/canon buffers — **seam now stated in the pattern body, not only here (Review 1: an absorption that hides the distinction is a deletion)**: Standby–GO's double-buffer IS the two-version state; Sighted Versions adds the *promotion authority* — the serialized sheet that decides which pending version becomes canon, and the visibility ledger of who saw which version |
| Timekeeper's Ledger | Fencing Token family | Pulse and fence are one family with two instruments (epoch-fenced counter) |
| Package Is the Permission | Proof-Carrying Artifact + Designation | Fail-closed `required: true` cadenzas; consumer audits the package |

### Iteration-5 candidates archived (valid, composable, not core)

| Pattern | Disposition |
|---------|-------------|
| Configuration Control Board | Serialized change office; composes Flight Rules' change board |
| Effectivity Blocks | Config-manifest validity lease; composes Flight Rules, First Article, Replication Licensing — **strong candidate for core next iteration; three compositions already depend on it** |
| Sign-Off Chain Against the Hard Date | Waiver discipline + disjoint failure-class ownership; composes Attested Merge Gate |
| Custody Transfer with Seals | Pairwise integrity check; seam vs Fork-Evident: point seals vs chain verification |
| Is-Line-Clear | Shared-medium admission (counterparty-answered permission); fail-to-DANGER lifecycle |
| Concurrent Count | Two-tally reconciliation with split-search discipline; composes Skeptical Oracle |
| Firing the Pass | Deadline-first (backward) scheduling; resurrects The Aboyeur; convergence-in-waiting |
| Allostatic Setpoint | Wear accounting — single witness; needs a second domain (LLM drift/compaction debt is the candidate) |
| Mycorrhizal Reciprocity | Reciprocal quality markets with graduated sanction; needs allocatable scarcity |
| Prescribed-Fire Pulse | Measured-fuel maintenance bursts on leased schedule; composes workspace hygiene |
| Globally-Typed Choreography | Offer/need typecheck over the rendered DAG; deadlock as validate-time error — **strong candidate; composes PCA + Behavioral Pre-Mortem** |
| Transfer of Command | Planned succession via mandated state document + declared minute; composes Black-Box Ledger |
| Devolution Packet | Awaiting Primitives — vendor-dispersed succession needs multi-host orchestration |
| Black Start | Awaiting Primitives — global capability rebuild order needs multi-host |
| Continuity Ledger | Serialized world-fact writer with typed assertions; composes Join-Semilattice (different fact types) |
| Rejoinder Ledger | Bijection response discipline; composes Skeptical Oracle |
| Re-Tiering Decision | Mass reclassification, authority separated from existence; triggered by Negative-Treatment Watch's flag-rate hold |
| Variant Apparatus | Dissent preserved inside the deliverable with witness sigla — the strongest form of C4; **strong candidate** |
| **Metered Merge** (restored per Review 2) | Admission-rate steering: `admit = k + gain × (target − measured)`, clamped; queue-spill override; degradation to a logged pretimed rate. Same damping law as Hutchinson's Warning applied to **flow**, not budget — the equation and sensor loop are why it is not safely absorbable |

### v4 archive dispositions

- **In v5.1 core/primitives (2):** Fan-out + Synthesis (foundational primitive), The Tool Chain (the Etiquette Law).
- **Confirmed unchanged, remain the v4 bestiary (Appendix A):** the remaining 54 patterns — the saturated who-does-what-in-what-order axis. The v5.1 core wraps them: v4's gates become Etiquette Law stages, v4's fan-outs gain evidence sidecars, v4's reviews gain checkpoints and reconstruction.
- **Unblocked by substrate advance:** Saga Compensation Chain (durable `on_failure` now exists).
- **Resurrected from Awaiting Primitives:** Stretto Entry → Canon of Phases; The Aboyeur → Firing the Pass.
- **Partially addressed:** Backpressure Valve → Metered Merge's leased admission gate approximates without concurrent execution; Comping Substrate → Canon of Phases covers rotation, not the full adaptive layer.
- **Newly awaiting:** Devolution Packet, Black Start (multi-host), Zeitgeber (offset scheduling), Accountability Board's score-facing sweep (claim-table export), MIST Card's conductor-retry feeding (per-attempt hooks), true capability confinement (process sandboxing).

---

# Patterns Awaiting Primitives

| Pattern | Blocked on | The buildable approximation (state it, don't hide it) |
|---|---|---|
| **Zeitgeber Entrainment** | offset-from-heartbeat scheduling (ScheduleConfig has cron/interval/timezone/overlap/misfire/jitter — no phase anchor) | Leased `schedule` + a heartbeat artifact the consumer reads as a `required: true` cadenza + a staleness gate (`skip_when` command comparing heartbeat age to period + tolerance) + skip-to-next-cue on staleness — never a catch-up burst. Different failure modes, different cost: the collapsed form polls and skips; the aspired form phase-locks. |
| **Accountability Board (score-facing PAR sweep)** | a score-facing export of the conductor's claim table with physical process handles | A CLI PAR movement probing the process table directly (`pgrep`/`ps` against a claims ledger the score maintains), reaping ghosts, asserting zero open rows before wrap-up. Weaker: it sees only processes it spawned. |
| **MIST Card (conductor retries)** | per-attempt retry hooks appending to a user-visible ledger | Scope to score-authored retry chains via the attempt-wrapper (in core, status: approximation). |
| **True capability confinement** | OS-level sandboxing of sheet processes (filesystem/tool scope) | Context designation (spec_tags/techniques/cadenza directories) — absent, not hidden; confinement of *prompt content*, not of *process reach* (in core, boundary stated). |
| **Devolution Packet** | multi-host orchestration | — |
| **Black Start** | multi-host orchestration | — |
| Backpressure Valve | concurrent score execution | Metered Merge's leased admission gate |
| Comping Substrate | concurrent execution with shared filesystem | Canon of Phases rotation |
| Supervision Hierarchy | supervisor config surface | workspace snapshots + conductor-mediated restart (v4 note) |

---

# Glossary

*v4 entries stand unless corrected; additions and coinage definitions first (Review 3's demand).*

| Term | Meaning |
|------|---------|
| **Etiquette (vs music)** | The deterministic protocol layer (cues, gates, ledgers, meters) — always non-LLM with an empty fallback chain. The performance layer is the music. |
| **Admissible** | A claim that may *enter the record* — it carries evidence a small checker verified. Inadmissible ≠ wrong: it is not even considered. |
| **Rung** | A named degradation tier (0 full instruments → 1 cheap routing → 2 narrower scope → 3 deferral), declared in `capacity-state.yaml`, never in prompt text. |
| **Beat** | The canon's unit of rotation continuity; the handoff packet's monotonic counter. |
| **Golden unit** | The retained first article — the reference artifact disputes are settled against, bound to the configuration hash that produced it. |
| **Arm / fire** | Standby–GO's two phases: collective acknowledged preparation; then one irreversible addressed execution. |
| **PAR** | Personnel accountability roll call — here, the reconciliation of claimed work against physical process handles. |
| **Watermark** | A consumer's high-water mark over the corrections ledger; entries newer than the watermark are unprocessed. |
| **Fencing token** | A monotonic number attached to authority; the shared substrate rejects writes bearing a lower number than the highest seen. |
| **License** | A single-use authorization artifact, atomically consumed (`mv`) by the act of beginning. |
| **Validity lease** | An admitted claim's right to remain admitted, renewed by recurring audit against current sources. |
| **Reproduction pointer** | A typed reference (failing test / lint rule / grep invariant / reproducer script) by which an oracle finding is mechanically re-derived. |
| `on_failure` | Durable terminal-failure hook: atomically claimed, reconciled across restart, same-ID protected, original-failure integrity preserved (v4's "Aspirational" note is **stale** — the primitive exists). |
| `schedule` | Durable leased recurrence: exactly one of `cron`/`interval`, IANA `timezone`, `overlap`, `misfire`, `jitter_seconds`. The lease is what makes exactly-one-attempt-per-window true across conductor restarts. |
| `spec_dir`/`spec_tags` | A specification corpus attached to movements, filtered by tags — context injection by reference; undesignated specs are absent, not hidden. |
| `techniques` | Per-sheet ECS attachments typed `skill`/`mcp`/`protocol`, optionally `required: true`. |
| `isolation: git-worktree` | Per-JOB isolated worktree (one per job) — **not per-sheet**; `parallel.enabled` + `isolation.enabled` together is warned against. |
| `per_sheet_fallbacks` | Fallback chain keyed by expanded sheet number. An **empty chain** on a deterministic stage declares: if this instrument is down, the score stops. |
| `circuit_breaker` | Threshold-triggered stop on **sheet-failure counts** — full stop. Spend lives in `cost_limits` (which pauses); ratios and flag rates live in deterministic gates. |
| Grounding validation | A validation that re-verifies a claim against workspace bytes (re-hash, re-run, cite-by-digest) at the moment of consumption. |
| Sheet / Score / Concert / Conductor / Workspace / Instrument / Prelude / Cadenza / Fan-out / Self-chaining / `capture_files` / validation types | *(unchanged from v4 — see Appendix A glossary)* |

---

# Open Questions (v5.1)

1. **The human seam.** Escalation-to-human is the terminal state inside at least four core patterns (Positive Transfer's hold, Immune Checkpoint's tolerance default, Standby–GO's hold escalation, Canon of Phases' rotation zero) and no pattern governs it. v4's Andon Cord is the archive ancestor. The next iteration must either give the human seam a vocabulary or admit the corpus stops at the boundary where custody matters most. **Named v6 requirement (Review 1).**
2. **C7 is the thinnest convergence.** One core carrier (Hutchinson's Warning) plus one archived family member (Metered Merge). v6 must find a third carrier or demote C7 to a law of controller design. *(The draft hid this; Review 1 found it.)*
3. **Proof debt — now blocking.** The v6 queue is prioritized above; a v5.1 pattern without a proof by end of v6 drops to hypothesis status. Vendor diversity must be exercised at least once (it never has been).
4. **The Script Library must be built.** Interfaces are specified above; the scripts must ship, in-score, with the proofs.
5. **Effectivity Blocks and Globally-Typed Choreography** are the two archived candidates with three and two compositions respectively depending on them — prime core candidates for v6.
6. **Cost model.** Per-pattern cost estimates relative to baseline remain unwritten; Hutchinson's Warning begins budget-as-first-class but does not finish it.
7. **Instrument freshness as validation.** Freshness dates are prose today; v6 should make an undated instrument recommendation a mechanical corpus error.
8. **Self-application.** This document recorded its own errata (Review Integration, item 10); the next iteration should run Fork-Evident History over corpus versions as standing practice — the sibling-citation misnumbering found by luck in the collision must become structurally impossible.
9. **Inherited from v4:** within-score context compression, dynamic instrument selection, the prompt-technique/orchestration boundary.

---

*The Rosetta Pattern Corpus v5.1 — 21 core patterns, 2 foundational primitives, 10 convergences with structural identity tables, 6 generators, 24 iteration-5 candidates dispositioned, 54 v4 patterns retained in Appendix A with frontmatter. The ten moves are its parts of speech, the six generators its phonemes, the domains its dialects, and agent orchestration the demanding speaker that needs every word it has. A grammar that includes words the speaker cannot pronounce is worse than a smaller pronounceable grammar — every word in this corpus is now pronounced in the real dialect.*

---
---

# Appendix A — The v4 Bestiary (complete, with frontmatter)

*All 56 v4 patterns, every one retained with its curated frontmatter. The v5.1 core wraps these; they answer who-does-what-in-what-order — the saturated axis — and remain composable exactly as v4 left them. Their score structures predate the dialect verification of this iteration; where a v4 snippet and The Real Dialect disagree, The Real Dialect wins and the v4 snippet is historical.*


## Foundational (v4 form — revised in main body as the foundational primitive)

---
name: "Fan-out + Synthesis"
scale: score-level
type: orchestration-pattern
status: working
forces:
  - "Information Asymmetry"
  - "Finite Resources"
generators: []
problem: "Work that could be parallelized is done sequentially, wasting time, or parallel outputs remain fragmented without meaningful integration."
signals:
  - "problem decomposes into independent sub-problems"
  - "sub-problems can be worked on simultaneously"
  - "need to integrate diverse perspectives or findings"
  - "synthesis must address cross-cutting themes, not just concatenate"
fan_out:
  analyze: 6
stages:
  - name: prepare
    sheets: 1
    instrument_guidance: "score-author's choice — sonnet or opus for complex problem decomposition requiring clear scope definition; haiku may suffice for simple scoping tasks"
    fallback_friendly: true
    purpose: "Define scope and shared context for parallel analysis."
    artifacts: ["scope.md"]
  - name: analyze
    sheets: "fan_out(6)"
    instrument_guidance: "score-author's choice — instrument capability must match the analysis complexity; sonnet recommended for code review or detailed analysis; haiku suffices for simple classification or data extraction"
    fallback_friendly: true
    purpose: "Analyze independent facets in parallel, each producing separate findings."
    artifacts: ["analysis-{{ instance_id }}.md"]
  - name: synthesize
    sheets: 1
    instrument_guidance: "sonnet or opus — synthesis requires finding cross-cutting themes and integrating diverse perspectives, higher-order reasoning beyond what produced individual analyses; fallback to cheaper instruments risks mere concatenation"
    fallback_friendly: false
    purpose: "Read all parallel outputs and produce unified result addressing cross-cutting concerns."
    artifacts: []
composes_with:
  - pattern: "Barn Raising"
    how: "Barn Raising establishes shared conventions before fan-out, preventing output format drift across parallel instances."
  - pattern: "Shipyard Sequence"
    how: "Shipyard Sequence validates the prepare stage's scope before expensive fan-out begins, preventing cascading rework."
  - pattern: "After-Action Review"
    how: "After-Action Review provides a coda on the synthesis stage, extracting lessons from the integration process."
  - pattern: "Triage Gate"
    how: "Triage Gate classifies parallel outputs by quality before synthesis, allowing the synthesis stage to handle different quality tiers differently."
  - pattern: "Relay Zone"
    how: "Relay Zone compresses verbose parallel outputs before synthesis, reducing synthesis complexity when fan-out produces high-volume results."
dependencies: {}
---

## Fan-out + Synthesis

`Status: Working` · **Source:** Ubiquitous — confirmed across all expeditions. Prior art: MapReduce (Dean & Ghemawat, 2004).

### Core Dynamic

Split work into parallel independent streams, merge in a synthesis stage. N agents work simultaneously on different facets. A final agent reads all outputs and produces a unified result. Most score-level patterns in this corpus build on, modify, or explicitly reject this structure. It is the default move when information asymmetry meets finite resources.

### When to Use / When NOT to Use

Use when the problem decomposes into independent sub-problems with a meaningful merge. Not when sub-problems share mutable state, synthesis is trivial concatenation, or fan-out width of 1 suffices.

### Marianne Score Structure

```yaml
sheets:
  - name: prepare
    prompt: "Define scope and shared context for the analysis."
    validations:
      - type: file_exists
        path: "{{ workspace }}/scope.md"
  - name: analyze
    instances: 6
    prompt: "Analyze module {{ instance_id }}. Write findings to analysis-{{ instance_id }}.md."
    capture_files: ["scope.md"]
    validations:
      - type: file_exists
        path: "{{ workspace }}/analysis-{{ instance_id }}.md"
  - name: synthesize
    prompt: "Read all analysis files. Produce a unified review addressing cross-cutting concerns."
    capture_files: ["analysis-*.md"]
    validations:
      - type: command_succeeds
        command: "test $(ls {{ workspace }}/analysis-*.md | wc -l) -ge 4"
```

### Failure Mode

Synthesis produces concatenation rather than integration. Validate with `command_succeeds` checking the synthesis references cross-cutting themes, not just individual reports. If fan-out agents share state, outputs will converge — use Prefabrication with interface contracts instead.

### Composes With

Barn Raising (conventions govern fan-out), Shipyard Sequence (validate before fanning out), After-Action Review (coda on synthesis), Triage Gate (classify outputs before synthesis), Relay Zone (compress before synthesis)

---

## Within-Stage Patterns (v4)

---
name: "Decision Propagation"
scale: within-stage
type: orchestration-pattern
status: working
forces:
  - "Information Asymmetry"
generators: []
problem: "Downstream agents contradict upstream decisions because constraints are buried in prose rather than structured, parseable briefs."
signals:
  - "early decisions have compounding effects on later stages"
  - "downstream agents unknowingly violate upstream constraints"
  - "decisions are buried in prose output rather than structured artifacts"
  - "agents cannot tell which upstream decisions are load-bearing"
fan_out:
  implement: 4
config_features:
  - "fan_out"
  - "capture_files"
stages:
  - name: decide
    sheets: 1
    instrument_guidance: "score-author's choice — needs strong reasoning to identify load-bearing decisions and write concrete constraint briefs; sonnet or opus recommended"
    fallback_friendly: false
    purpose: "Make the architecture decision and write a structured constraint-brief with decision, rationale, implications, and downstream constraints."
    artifacts: ["constraint-brief.yaml"]
  - name: implement
    sheets: "fan_out(4)"
    instrument_guidance: "score-author's choice — must be capable enough for the implementation task; constraints are externalized in the brief so instrument follows them"
    fallback_friendly: true
    purpose: "Read the constraint brief, build one component per instance, and acknowledge which constraints were incorporated."
    artifacts: []
composes_with:
  - pattern: "CDCL Search"
    how: "When propagated decisions lead to failure, CDCL Search extracts the failure reason as a learned clause that prevents the same bad decision propagation in future iterations."
  - pattern: "CEGAR Loop"
    how: "CEGAR Loop's refinement iterations generate decisions at progressively finer abstraction levels; Decision Propagation structures each level's decisions for downstream consumption."
  - pattern: "Commander's Intent Envelope"
    how: "Commander's Intent Envelope defines the decision space boundaries (constraints and freedoms) within which Decision Propagation's structured briefs specify concrete downstream constraints."
dependencies: {}
---

## Decision Propagation

`Status: Working` · **Source:** Constraint satisfaction (renamed from Arc Consistency Propagation). **Forces:** Information Asymmetry.

### Core Dynamic

When a sheet makes a decision that constrains downstream sheets, it writes a structured constraint brief rather than embedding the decision in prose. The brief has: decision, rationale, implications, and constraints-for-downstream. Each downstream sheet reads the brief and acknowledges which constraints it incorporated. Writing the brief requires judgment — the agent must identify which decisions are load-bearing.

### When to Use / When NOT to Use

Use when decisions in early stages have compounding effects. Not when stages are independent or constraints are simple enough for the prompt alone.

### Marianne Score Structure

```yaml
sheets:
  - name: decide
    prompt: >
      Make the architecture decision. Write constraint-brief.yaml:
      {decision, rationale, implications: [], constraints_for_downstream: []}.
    validations:
      - type: command_succeeds
        command: "python3 -c \"import yaml; b=yaml.safe_load(open('{{ workspace }}/constraint-brief.yaml')); assert 'constraints_for_downstream' in b\""
  - name: implement
    instances: 4
    prompt: "Read constraint-brief.yaml. Build component {{ instance_id }}. Acknowledge constraints."
    capture_files: ["constraint-brief.yaml"]
```

### Failure Mode

Constraint briefs too abstract to constrain. The brief should name specific artifacts and interfaces, not just abstract goals. Validate with `command_succeeds` checking brief has concrete entries.

### Composes With

CDCL Search, CEGAR Loop, Commander's Intent Envelope

---
name: "Commander's Intent Envelope"
scale: within-stage
type: prompt-technique
status: working
forces:
  - "Information Asymmetry"
generators: []
problem: "Instruction-based prompts break when the agent encounters conditions the prompt author didn't anticipate."
signals:
  - "task has more than one valid approach"
  - "inputs are variable-format or unpredictable"
  - "different instruments would solve this differently"
  - "want to validate outcomes, not methods"
stages:
  - name: execute
    sheets: 1
    instrument_guidance: "score-author's choice — instrument must be capable enough to exercise autonomous judgment within the envelope; stronger instruments benefit more from the freedoms"
    fallback_friendly: true
    purpose: "Execute within an intent envelope structured as PURPOSE (why), END STATE (measurable success), CONSTRAINTS (hard boundaries), FREEDOMS (autonomous decisions). The agent finds its own path."
    artifacts: ["decision-log.md"]
composes_with:
  - pattern: "Mission Command"
    how: "Commander's Intent Envelope IS Mission Command at the individual sheet scale — the same intent structure applied within one agent rather than across a team."
  - pattern: "Fan-out + Synthesis"
    how: "The intent envelope is shared as prelude across fan-out instances, giving each instance the same boundaries but allowing different methods."
  - pattern: "After-Action Review"
    how: "The decision-log artifact feeds directly into After-Action Review, providing the record of autonomous decisions for doctrine extraction."
dependencies: {}
---

## Commander's Intent Envelope

`Status: Working` · **Source:** Military mission command doctrine, Expedition 5. **Scale:** within-stage. **Iteration:** 4. **Type:** Prompt technique.

### Core Dynamic

Structures a single sheet's prompt as PURPOSE (why this task matters in the larger score), END STATE (measurable success conditions), CONSTRAINTS (hard boundaries — MUST NOT violate), and FREEDOMS (decisions the agent may make autonomously). The structural distinction from ordinary prompting: this changes the coordination contract from instructions (do X then Y) to boundaries (achieve Z however you see fit, except A). The agent finds its own path within the envelope. Validates end-state achievement and autonomous decision-making, not method compliance.

### When to Use / When NOT to Use

Use when the task has more than one valid approach, when inputs are variable-format, or when different instruments would achieve the end state differently. Not for purely mechanical tasks (format conversion, command execution), security-critical operations where deviations create vulnerabilities, or when validation criteria can't capture the end state precisely.

### Marianne Score Structure

```yaml
sheets:
  - name: execute
    prompt: |
      ## Commander's Intent
      PURPOSE: Ensure the web application has no exploitable input validation vulnerabilities.
      END STATE: Report listing all confirmed vulnerabilities with severity, location, fix. Zero false positives.
      CONSTRAINTS: Do not modify source code. Do not run code. Do not access external services.
      FREEDOMS: Choose which files to review. Choose review order. Choose depth based on risk.

      ## Context
      Read {{ workspace }}/codebase/ for the application source.

      ## Resources
      Write findings to {{ workspace }}/security-report.md and decision-log.md.
    validations:
      - type: file_exists
        path: "{{ workspace }}/security-report.md"
      - type: file_exists
        path: "{{ workspace }}/decision-log.md"
      - type: content_contains
        path: "{{ workspace }}/decision-log.md"
        content: "DECISION:"
```

### Failure Mode

Intent briefs too vague produce incoherent decisions; too specific collapses the decision space back to instructions. The decision-log validation is critical: if the agent made no autonomous decisions, the envelope wasn't adding value over direct instructions. If the log shows decisions outside the CONSTRAINTS, the boundaries were unclear.

### Composes With

Mission Command (intent IS mission command at sheet scale), Fan-out + Synthesis (intent envelope shared across instances), After-Action Review (decision-log feeds doctrine)

---
name: "Quorum Trigger"
scale: within-stage
type: prompt-technique
status: working
forces:
  - "Accumulated Signal"
generators:
  - "Threshold-Triggered Switch"
problem: "Agents continue executing their original plan after accumulating evidence that makes continuing wasteful or dangerous."
signals:
  - "conditions discovered mid-task should change the approach"
  - "findings accumulate that individually seem minor but collectively demand action"
  - "agent needs to self-interrupt based on evidence density"
  - "severity of issues should trigger a mode switch, not just a note"
stages:
  - name: audit
    sheets: 1
    instrument_guidance: "score-author's choice — must be capable enough for the domain task (code review, research, data processing) and disciplined enough to maintain the signal register faithfully"
    fallback_friendly: true
    purpose: "Execute the primary task while maintaining a signal register; switch to alternate behavior (remediation, escalation) when accumulated signals cross the predefined threshold."
    artifacts: ["signal-register.yaml", "quorum-trigger-report.md"]
  - name: verify-threshold
    sheets: 1
    instrument_guidance: "cli — deterministic validation that the threshold state matches the agent's claimed behavior"
    fallback_friendly: false
    purpose: "Independently verify that the signal register's threshold state matches whether the trigger report exists, catching agent miscounting or threshold evasion."
    artifacts: []
composes_with:
  - pattern: "Andon Cord"
    how: "Quorum Trigger fires within a stage to detect accumulated problems; Andon Cord provides the between-stage diagnostic response when the trigger fires."
  - pattern: "Circuit Breaker"
    how: "Quorum Trigger monitors task-level quality signals; Circuit Breaker monitors infrastructure-level failure signals — both are threshold-triggered switches at different abstraction levels."
  - pattern: "Immune Cascade"
    how: "Quorum Trigger's threshold firing can initiate Immune Cascade's escalating triage response, routing accumulated findings through graduated investigation tiers."
dependencies: {}
---

## Quorum Trigger

`Status: Working` · **Source:** Bacterial quorum sensing (threshold-triggered behavioral switch), Expedition 2. **Scale:** within-stage. **Iteration:** 4. **Force:** Accumulated Signal. **Type:** Prompt technique.

### Core Dynamic

Within-stage behavioral switch triggered by accumulated signal density. The agent works on its primary task while maintaining an explicit signal register (a YAML file tracking findings with severity levels). When accumulated signals cross a predefined threshold (e.g., "3+ CRITICAL findings"), the agent stops its current plan and switches to an alternate behavior (remediation, diagnosis, escalation). The switch is binary — a phase transition, not a gradual adjustment.

**Enforcement note:** The signal register is agent-maintained and therefore untrustworthy in isolation. A downstream CLI validation sheet should verify the register's threshold state independently. Do not rely solely on the agent self-reporting whether the trigger fired.

### When to Use / When NOT to Use

Use when conditions discovered mid-task make continuing the original plan wasteful or dangerous: code review finding critical security flaws, research discovering the premise is wrong, data processing hitting malformed records. Not when the threshold is ambiguous, the task is too short for the switch to fire, or the behavioral switch loses valuable pre-switch context.

### Marianne Score Structure

```yaml
sheets:
  - name: audit
    prompt: |
      Audit each module for vulnerabilities. Maintain a signal register in signal-register.yaml:
      each entry has {module, severity: LOW|MEDIUM|HIGH|CRITICAL, finding}.

      THRESHOLD: If you accumulate 3+ CRITICAL findings before completing the full audit,
      STOP scanning and switch to writing a remediation plan for findings so far.
      Write quorum-trigger-report.md if threshold fires.
    validations:
      - type: file_exists
        path: "{{ workspace }}/signal-register.yaml"
      - type: content_regex
        pattern: "severity:\\s+(LOW|MEDIUM|HIGH|CRITICAL)"
  - name: verify-threshold
    instrument: cli
    validations:
      - type: command_succeeds
        command: "python3 -c \"import yaml; r=yaml.safe_load(open('{{ workspace }}/signal-register.yaml')); crits=[e for e in r if e.get('severity')=='CRITICAL']; import os; triggered=os.path.exists('{{ workspace }}/quorum-trigger-report.md'); assert (len(crits)>=3)==triggered, f'Threshold mismatch: {len(crits)} crits, triggered={triggered}'\""
```

### Failure Mode

Agent miscounts findings or ignores the threshold entirely. The CLI verification sheet catches this: if 3+ CRITICALs exist but no trigger report (or vice versa), the validation fails. The deeper failure: the agent classifies everything as MEDIUM to avoid triggering. Only domain-specific validation of severity assignments catches this.

### Composes With

Andon Cord (quorum trigger within a stage, andon cord between stages), Circuit Breaker (quorum for quality, circuit breaker for infrastructure), Immune Cascade (quorum-triggered triage)

---
name: "Constraint Propagation Sweep"
scale: within-stage
type: prompt-technique
status: working
forces:
  - "Information Asymmetry"
  - "Exponential Defect Cost"
generators: []
problem: "Agents generate from contradictory specifications because constraint conflicts remain hidden until expensive work is already complete."
signals:
  - "specifications from different stakeholders contain implicit contradictions"
  - "generated outputs fail because requirements conflicted silently"
  - "reconciling heterogeneous inputs costs less than reworking outputs"
  - "constraint set is large enough that pairwise conflicts are non-obvious"
stages:
  - name: synthesize
    sheets: 1
    instrument_guidance: "score-author's choice — needs strong reasoning to enumerate constraints, resolve pairwise contradictions, and generate from the reduced space; sonnet or opus recommended for complex constraint sets"
    fallback_friendly: true
    purpose: "Single sheet with three mandatory prompt phases: ENUMERATE all constraints from inputs, RESOLVE them pairwise to prune contradictions, GENERATE output from the reduced solution space."
    artifacts: ["constraint-audit.yaml", "synthesis.md"]
composes_with:
  - pattern: "Decision Propagation"
    how: "Decision Propagation feeds structured constraint briefs into the sweep's enumeration phase, providing pre-identified constraints from upstream decisions."
  - pattern: "CDCL Search"
    how: "CDCL Search's learned failure clauses become additional constraints in the sweep's enumeration phase, preventing previously discovered contradictions from recurring."
  - pattern: "Rashomon Gate"
    how: "Rashomon Gate applies multiple analytical frames to the same constraint set, revealing frame-dependent contradictions the sweep might miss from a single perspective."
dependencies: {}
---

## Constraint Propagation Sweep

`Status: Working` · **Source:** Constraint satisfaction, structured reasoning. **Scale:** within-stage. **Iteration:** 4. **Force:** Domain Reduction. **Type:** Prompt technique.

### Core Dynamic

Before generating ANY output, the prompt instructs the agent to separate three kinds of reasoning into mandatory phases: (1) ENUMERATE all constraints from the specification and workspace artifacts, (2) RESOLVE them pairwise to identify contradictions and prune impossible options, (3) GENERATE from the reduced solution space. The phases MUST be separate — generating during resolution skips contradictions; resolving during generation loses information. This is domain reduction before search: pruning is cheap, search through contradictory requirements is expensive.

This is a prompt structuring technique, not a multi-sheet orchestration pattern. The phases are instructions within one prompt, not separate sheets. This means no intermediate validation between phases — the agent can skip resolution and you'd only detect it from the output quality, not structurally. For structural enforcement, use three separate sheets with validation between them.

### When to Use / When NOT to Use

Use when specifications contain implicit contradictions from different stakeholders, when generating from conflicting requirements costs more than constraint analysis, or when reconciling heterogeneous inputs (multiple analyst reports, multi-team requirements). Not when constraints are few and independent, the specification is already consistent, or the task is creative rather than constrained.

### Marianne Score Structure

```yaml
sheets:
  - name: synthesize
    prompt: |
      ENUMERATE: List every constraint from the input documents.
      RESOLVE: Check each pair for conflicts. Mark the weaker constraint as pruned.
      Write constraint-audit.yaml: {id, constraint, status: active|pruned, reason}.
      GENERATE: Produce the architecture using only active constraints.
      Write the synthesis to synthesis.md.
    capture_files: ["requirements/*.md"]
    validations:
      - type: file_exists
        path: "{{ workspace }}/constraint-audit.yaml"
      - type: command_succeeds
        command: "python3 -c \"import yaml; a=yaml.safe_load(open('{{ workspace }}/constraint-audit.yaml')); pruned=[e for e in a if e.get('status')=='pruned']; print(f'{len(pruned)} constraints pruned of {len(a)} total')\""
```

### Failure Mode

Agent performs all three phases but doesn't actually prune — the audit shows zero pruned constraints despite contradictory inputs. The `command_succeeds` validation catches this by printing stats, but can't enforce quality. For high-stakes synthesis, follow with a dedicated clash detection sheet comparing the synthesis against all input constraints.

### Composes With

Decision Propagation (propagation feeds constraint briefs), CDCL Search (failures become new constraints), Rashomon Gate (multiple frames on the same constraint set)

## Score-Level Patterns (v4)

---
name: "Triage Gate"
scale: score-level
type: orchestration-pattern
status: working
forces:
  - "Finite Resources"
  - "Partial Failure"
generators:
  - "Exploit Failure as Signal"
problem: "Fan-out produces mixed-quality outputs but synthesis processes all outputs regardless of quality, wasting resources."
signals:
  - "fan-out produces wildly varying output quality"
  - "synthesis stage is expensive and shouldn't process garbage"
  - "some outputs need rework, others are ready"
  - "structural quality checks are definable"
config_features:
  - "capture_files"
stages:
  - name: triage
    sheets: 1
    instrument_guidance: "haiku recommended — classification task dominated by structural checks (schema, sections, word count); semantic assessment is secondary and doesn't require strong reasoning"
    fallback_friendly: true
    purpose: "Classify each fan-out output as RED (forward to synthesis), YELLOW (rework with targeted prompt), GREEN (supplementary), or BLACK (discard with logged reason)."
    artifacts: ["triage-manifest.yaml"]
composes_with:
  - pattern: "Immune Cascade"
    how: "Triage Gate provides coarse filtering that precedes Immune Cascade's graduated verification stages."
  - pattern: "Fan-out + Synthesis"
    how: "Triage Gate filters fan-out outputs before synthesis, preventing synthesis from processing low-quality or unusable outputs."
  - pattern: "Relay Zone"
    how: "Triage Gate classifies fan-out outputs by quality; Relay Zone compresses the classified results to prevent context overflow in downstream processing stages."
dependencies: {}
---

## Triage Gate

`Status: Working` · **Source:** Emergency medicine START protocol, military command. **Forces:** Finite Resources + Partial Failure.

### Core Dynamic

Coarse classification before expensive processing. A fast classifier reads fan-out outputs and routes: **RED** (forward to synthesis), **YELLOW** (rework with targeted prompt), **GREEN** (supplementary), **BLACK** (discard with logged reason). Structural checks first (schema compliance, required sections, word count), then semantic if needed. This is the convergence ranked #1 across all domains.

### When to Use / When NOT to Use

Use when fan-out produces mixed quality, downstream processing is expensive, and structural quality checks are definable. Not when all outputs must be incorporated or fan-out is narrow (2-3 agents).

### Marianne Score Structure

```yaml
sheets:
  - name: triage
    prompt: >
      Read each output in fan-out-results/. For each, write a line in triage-manifest.yaml:
      {id, category: RED|YELLOW|GREEN|BLACK, reason, rework_prompt}.
      Use structural checks first: required sections present, word count > 200.
    capture_files: ["fan-out-results/*.md"]
    validations:
      - type: command_succeeds
        command: "python3 -c \"import yaml; m=yaml.safe_load(open('{{ workspace }}/triage-manifest.yaml')); assert all(e['category'] in ['RED','YELLOW','GREEN','BLACK'] for e in m)\""
```

### Failure Mode

If YELLOW count is 0, the rework stage still executes but produces nothing — guard with a Read-and-React conditional. If everything is BLACK, synthesis gets no inputs; the score should fail explicitly.

### Composes With

Immune Cascade, Fan-out + Synthesis, Relay Zone

---
name: "Immune Cascade"
scale: instrument-strategy
type: orchestration-pattern
status: working
proof_score: "rosetta-proof-immune-cascade.yaml"
forces:
  - "Finite Resources"
  - "Exponential Defect Cost"
generators:
  - "Graduate & Filter"
problem: "Expensive instruments waste resources on broad scanning when cheap preliminary work could narrow scope first."
signals:
  - "broad scanning is expensive but most issues are benign"
  - "don't know which findings warrant expensive investigation"
  - "need to narrow findings before expensive deep analysis"
stages:
  - name: broad-sweep
    sheets: "fan_out(8)"
    instrument_guidance: "haiku — fast, cheap scanning across partitions; capability sufficient for breadth-first issue discovery"
    fallback_friendly: true
    purpose: "Parallelize broad scanning to identify findings efficiently at low cost."
    artifacts: ["sweep-{{ instance_id }}.md"]
  - name: triage-handoff
    sheets: 1
    instrument_guidance: "score-author's choice — requires judgment to triage findings and prioritize targets; stronger instruments produce better targeting"
    fallback_friendly: false
    purpose: "Deduplicate broad findings and create prioritized targeting brief for expensive investigation."
    artifacts: ["targeting-brief.md"]
  - name: deep-investigation
    sheets: 1
    instrument_guidance: "opus — deep code analysis and remediation requiring full reasoning capability; critical for thorough investigation"
    fallback_friendly: false
    purpose: "Deep-dive on prioritized targets with thorough analysis and remediation design."
    artifacts: []
  - name: learning
    sheets: 1
    instrument_guidance: "score-author's choice — documents methodology and learnings; can use cheaper instrument"
    fallback_friendly: true
    purpose: "Document methodology and learnings for future audit iterations."
    artifacts: ["doctrine.md"]
composes_with:
  - pattern: "Triage Gate"
    how: "The triage-handoff stage implements Triage Gate logic, filtering broad findings to identify investigation targets."
  - pattern: "After-Action Review"
    how: "After-Action Review processes Immune Cascade's findings and learning stage outputs to extract methodology improvements."
  - pattern: "Relay Zone"
    how: "Relay Zone compresses the high-volume broad-sweep outputs before triage-handoff, preventing context overflow when parallel scans produce results."
fan_out:
  broad-sweep: 8
config_features:
  - "fan_out"
  - "capture_files"
dependencies: {}
---

## Immune Cascade

`Status: Working` · **Source:** Immunology (innate/adaptive response). Absorbs Kill Chain F2T2EA. **Forces:** Finite Resources + Exponential Defect Cost.

### Core Dynamic

Escalating tiers: fast/cheap/broad first for intelligence, slow/expensive/precise targeting what tier 1 found, then learning persistence. Three structural moves: graduated response, intelligence forwarding, learning persistence. **Strict Sequential Variant (from Kill Chain):** When the problem is pure narrowing, collapse to a linear pipeline where `command_succeeds verifying count decreased` validates each gate.

### When to Use / When NOT to Use

Use when the problem requires broad search before targeted work and cheap scanning methods exist. Not when the problem is narrow enough for direct attack.

### Marianne Score Structure

```yaml
sheets:
  - name: broad-sweep
    instances: 8
    instrument: haiku
    prompt: "Scan {{ partition }} for issues. Write raw findings."
    validations:
      - type: file_exists
        path: "{{ workspace }}/sweep-{{ instance_id }}.md"
  - name: triage-handoff
    prompt: "Read all sweep files. Deduplicate. Prioritize. Write targeting-brief.md."
    capture_files: ["sweep-*.md"]
  - name: deep-investigation
    instrument: opus
    prompt: "Deep-dive on prioritized targets. Write remediation."
    capture_files: ["targeting-brief.md"]
  - name: learning
    prompt: "Write doctrine.md: what scanning missed, what triage misjudged, rules for next run."
    validations:
      - type: content_regex
        pattern: "RULE:\\s+.+"
```

### Failure Mode

The learning stage is useless if it doesn't write persistent, structured output. Specify the artifact: `doctrine.md` with `RULE:` entries that the next iteration's broad sweep reads via prelude.

### Composes With

Triage Gate (handoff IS triage), After-Action Review (coda), Relay Zone (relay between tiers)

---
name: "Mission Command"
scale: score-level
type: orchestration-pattern
status: working
forces:
  - "Information Asymmetry"
generators:
  - "Contract at Interfaces"
problem: "Centralized instruction-following breaks when agents face conditions the planner didn't anticipate."
signals:
  - "tasks require agent judgment and conditions may vary"
  - "validation should check outcomes, not methods"
  - "multiple agents must coordinate around shared intent"
  - "top-down instructions are too brittle for variable conditions"
fan_out:
  execute: 4
stages:
  - name: mission-brief
    sheets: 1
    instrument_guidance: "score-author's choice — needs strong reasoning to write a clear intent envelope with testable end-state; sonnet or opus recommended"
    fallback_friendly: false
    purpose: "Write the mission brief defining PURPOSE, KEY TASKS, and END STATE."
    artifacts: ["mission-brief.md"]
  - name: execute
    sheets: "fan_out(4)"
    instrument_guidance: "score-author's choice — must be capable enough for the actual task (code refactoring, analysis, etc.); instrument depends on task complexity"
    fallback_friendly: false
    purpose: "Execute the mission by reading the brief and working autonomously within the intent envelope."
    artifacts: []
composes_with:
  - pattern: "After-Action Review"
    how: "After-Action Review evaluates whether decentralized execution achieved the mission brief's end state and extracts lessons."
  - pattern: "Barn Raising"
    how: "Barn Raising establishes shared conventions before Mission Command's parallel execution, preventing convention drift across agents."
  - pattern: "Prefabrication"
    how: "Prefabrication defines strict interface contracts that constrain Mission Command agents' output format while preserving freedom of method."
dependencies: {}
---

## Mission Command

`Status: Working` · **Source:** Auftragstaktik (Prussian military doctrine). **Forces:** Information Asymmetry.

### Core Dynamic

Separate "what and why" (centralized) from "how" (decentralized). The intent envelope has three layers: **purpose** (why), **key tasks** (what), **end state** (what done looks like). Agents adapt freely within the decision space. Validate end-state achievement, never method compliance. The structural distinction: Mission Command scores have a *specific, named intent document* that replaces per-agent context acquisition, plus end-state-only validation.

### When to Use / When NOT to Use

Use when tasks require agent judgment and conditions may differ from expectations. Not for mechanical tasks or constraints so tight only one approach is valid.

### Marianne Score Structure

```yaml
sheets:
  - name: mission-brief
    prompt: >
      Write mission-brief.md with three sections:
      PURPOSE: why this refactoring matters.
      KEY TASKS: the 4 modules that must be decoupled.
      END STATE: all 340 tests pass, public API unchanged, coupling metric < 0.3.
    validations:
      - type: content_contains
        content: "PURPOSE:"
      - type: content_contains
        content: "END STATE:"
  - name: execute
    instances: 4
    prompt: "Read mission-brief.md. Decouple module {{ instance_id }}."
    capture_files: ["mission-brief.md"]
    validations:
      - type: command_succeeds
        command: "cd {{ workspace }} && python -m pytest --tb=no -q"
```

### Failure Mode

Intent briefs too vague produce incoherent decisions. Too specific collapses the decision space. The end state must be testable with `command_succeeds`.

### Composes With

After-Action Review, Barn Raising, Prefabrication

---
name: "Shipyard Sequence"
scale: score-level
type: orchestration-pattern
status: working
proof_score: "shipyard-sequence.yaml"
forces:
  - "Exponential Defect Cost"
  - "Finite Resources"
generators:
  - "Graduate & Filter"
  - "Gate on Environmental Readiness"
problem: "Expensive fan-out proceeds on a broken foundation, wasting resources on downstream work that will fail."
signals:
  - "downstream fan-out is expensive"
  - "foundation must be solid before scaling work"
  - "need real validation tools, not LLM judgment"
  - "costs multiply when defects reach later stages"
fan_out:
  outfitting: 4
stages:
  - name: construct-schema
    sheets: 1
    instrument_guidance: "score-author's choice — needs code generation for schema/migrations; sonnet or opus for complex domains, haiku for simple schemas"
    fallback_friendly: true
    purpose: "Generate the database schema and migration files."
    artifacts: ["schema.sql"]
  - name: launch-gate
    sheets: 1
    instrument_guidance: "any instrument with command execution — validation is deterministic tool-based (command_succeeds), not LLM judgment; even haiku suffices"
    fallback_friendly: true
    purpose: "Validate the schema using real tools (migrate --check, test suite) before expensive fan-out."
    artifacts: []
  - name: outfitting
    sheets: "fan_out(4)"
    instrument_guidance: "score-author's choice — builds services/modules on validated foundation; capability depends on service complexity"
    fallback_friendly: true
    purpose: "Build services or modules in parallel against the validated schema."
    artifacts: []
composes_with:
  - pattern: "Succession Pipeline"
    how: "Succession Pipeline graduates candidates through quality tiers; Shipyard Sequence validates foundation quality before expensive fan-out investment."
  - pattern: "Dormancy Gate"
    how: "Dormancy Gate waits for external environmental conditions; Shipyard Sequence gates on foundation validation readiness before proceeding."
  - pattern: "Triage Gate"
    how: "Triage Gate filters work items before processing; Shipyard Sequence validates foundation before expensive downstream fan-out."
dependencies:
  launch-gate: [construct-schema]
  outfitting: [launch-gate]
config_features:
  - "fan_out"
  - "command_succeeds"
---

## Shipyard Sequence

`Status: Working` · **Source:** Shipbuilding hull block method. **Forces:** Exponential Defect Cost + Finite Resources.

### Core Dynamic

Validate foundational work under realistic conditions before investing in expensive fan-out. The launch gate uses `command_succeeds` exclusively — real execution, not LLM judgment. Construction has 1-3 stages; outfitting fans out only after launch passes.

### When to Use / When NOT to Use

Use when downstream fan-out is expensive, foundation must be solid, and real validation tools exist. Not when work is naturally parallel from the start.

### Marianne Score Structure

```yaml
sheets:
  - name: construct-schema
    prompt: "Generate the database schema and migration files."
  - name: launch-gate
    validations:
      - type: command_succeeds
        command: "cd {{ workspace }} && python manage.py migrate --check"
      - type: command_succeeds
        command: "cd {{ workspace }} && python manage.py test db_schema --verbosity=0"
  - name: outfitting
    instances: 4
    prompt: "Build {{ service_name }} against the validated schema."
    capture_files: ["schema.sql"]
```

### Failure Mode

If launch validation is too lenient, expensive fan-out proceeds on a broken foundation. The gate must use `command_succeeds`, never `content_contains`.

### Composes With

Succession Pipeline, Dormancy Gate, Triage Gate

---
name: "Succession Pipeline"
scale: score-level
type: orchestration-pattern
status: working
forces:
  - "Exponential Defect Cost"
generators:
  - "Graduate & Filter"
problem: "Work requires sequential substrate transformations, but unstructured execution produces outputs incompatible with downstream stages."
signals:
  - "each stage needs fundamentally different methods"
  - "one stage's output becomes the next stage's input substrate"
  - "stages have categorical differences, not just detail levels"
  - "work resembles ecological succession with distinct phases"
stages:
  - name: parse
    sheets: 1
    instrument_guidance: "score-author's choice — parsing is often mechanical; cheaper instruments or CLI parsers work if parsing is deterministic; use stronger instruments only if parsing requires inference"
    fallback_friendly: true
    purpose: "Parse source files into abstract syntax trees."
    artifacts: ["ast.json"]
  - name: transform
    sheets: 1
    instrument_guidance: "score-author's choice — must understand both AST and target IR semantics; sonnet or opus recommended for complex transformations involving semantic analysis or optimization"
    fallback_friendly: false
    purpose: "Transform AST into intermediate representation."
    artifacts: ["ir.dot"]
  - name: generate
    sheets: 1
    instrument_guidance: "score-author's choice — must understand IR and generate valid target code; sonnet or opus for complex languages, haiku may suffice for simple templated output"
    fallback_friendly: false
    purpose: "Generate target code from intermediate representation."
    artifacts: []
composes_with:
  - pattern: "Shipyard Sequence"
    how: "Shipyard Sequence gates each succession stage on environmental readiness, ensuring the substrate is prepared before the next transformation begins."
  - pattern: "Barn Raising"
    how: "Barn Raising establishes conventions for how each stage structures its substrate output so the next stage can consume it reliably."
dependencies: {}
---

## Succession Pipeline

`Status: Working` · **Source:** Forest succession ecology. **Forces:** Exponential Defect Cost.

### Core Dynamic

Each stage transforms the workspace into a state where the next becomes possible. The substrate transformation test: does Stage N's output become Stage N+1's input *substrate* — a different *kind* of thing? Three mandatory phases using categorically different methods.

### When to Use / When NOT to Use

Use when stages require fundamentally different methods and each output is the next's prerequisite environment. Not when each stage uses the same approach (that's iteration).

### Marianne Score Structure

```yaml
sheets:
  - name: parse
    prompt: "Parse source files into abstract syntax trees. Write AST JSON."
    validations:
      - type: command_succeeds
        command: "python3 -c \"import json; json.load(open('{{ workspace }}/ast.json'))\""
  - name: transform
    prompt: "Transform AST into intermediate representation."
    capture_files: ["ast.json"]
  - name: generate
    prompt: "Generate target code from IR."
    capture_files: ["ir.dot"]
```

### Failure Mode

If your stages use the same method with growing detail, that's Fixed-Point Iteration, not Succession.

### Composes With

Shipyard Sequence, Barn Raising

---
name: "Red Team / Blue Team"
scale: score-level
type: orchestration-pattern
status: working
forces:
  - "Information Asymmetry"
  - "Partial Failure"
generators:
  - "Exploit Failure as Signal"
problem: "Artifacts tested by known adversaries pass trivially; unknown adversaries reveal real flaws."
signals:
  - "testing is too predictable when defenders know the attacks"
  - "need to find vulnerabilities that prepared defense would miss"
  - "want realistic stress-testing where defenders work blind"
stages:
  - name: red-attack
    sheets: 1
    instrument_guidance: "score-author's choice — needs reasoning capability to devise effective attacks; stronger instrument produces more sophisticated attacks"
    fallback_friendly: true
    purpose: "Devise and execute attacks against the artifact, recording both methods and effects."
    artifacts: ["red-workspace/effects.md", "red-workspace/methods.md"]
  - name: relay
    sheets: 1
    instrument_guidance: "cli — shell command to copy effect descriptions without revealing method details"
    fallback_friendly: true
    purpose: "Copy attack effects from red's workspace to blue's briefing, redacting methods."
    artifacts: ["blue-briefing/effects.md"]
  - name: blue-defend
    sheets: 1
    instrument_guidance: "score-author's choice — must have reasoning capability to devise defenses against unknown attacks; stronger instrument produces more robust defenses"
    fallback_friendly: true
    purpose: "Read attack effects and devise defenses without knowing attack methods."
    artifacts: ["blue-response.md"]
  - name: purple-debrief
    sheets: 1
    instrument_guidance: "score-author's choice — needs strong reasoning to analyze attack-defense interactions and extract lessons; opus or sonnet recommended"
    fallback_friendly: false
    purpose: "Analyze all attack and defense data to generate attack-defense matrix and lessons."
    artifacts: ["debrief.md"]
composes_with:
  - pattern: "After-Action Review"
    how: "Purple debrief IS an after-action review, documenting attack-defense interactions and extracting patterns."
  - pattern: "Immune Cascade"
    how: "Red Team / Blue Team stress-tests each tier of Immune Cascade's repairs to validate robustness across difficulty levels."
dependencies: {}
---

## Red Team / Blue Team

`Status: Working` · **Source:** Military adversarial exercises. **Forces:** Information Asymmetry + Partial Failure.

### Core Dynamic

Information asymmetry via redaction: Red writes *effects* but not *methods*. Blue sees effects, must defend blind. Purple debrief gets full access. **Enforcement:** Separate workspace subdirectories (`red-workspace/` vs `blue-briefing/`). A relay stage copies only effect descriptions. Blue's `capture_files` is restricted to `blue-briefing/` only.

### When to Use / When NOT to Use

Use when the artifact needs adversarial stress-testing and the defender should not know attack methods. Not when the team is collaborative or the artifact is too simple for adversarial testing.

### Marianne Score Structure

```yaml
sheets:
  - name: red-attack
    prompt: "Attack the artifact. Write effects to red-workspace/effects.md and methods to red-workspace/methods.md."
    validations:
      - type: file_exists
        path: "{{ workspace }}/red-workspace/effects.md"
  - name: relay
    instrument: cli
    validations:
      - type: command_succeeds
        command: "cp {{ workspace }}/red-workspace/effects.md {{ workspace }}/blue-briefing/effects.md"
  - name: blue-defend
    prompt: "Read blue-briefing/effects.md. Defend. Write blue-response.md."
    capture_files: ["blue-briefing/effects.md"]
  - name: purple-debrief
    prompt: "Read ALL files. Write debrief with attack-defense matrix."
    capture_files: ["red-workspace/**", "blue-briefing/**", "blue-response.md"]
```

### Failure Mode

Red produces weak attacks, Blue passes trivially. Validate Red output contains specific attack categories. If relay leaks methods, Blue's defense is tainted.

### Composes With

After-Action Review (purple debrief IS AAR), Immune Cascade

---
name: "Prefabrication"
scale: score-level
type: orchestration-pattern
status: working
proof_score: "prefabrication.yaml"
forces:
  - "Producer-Consumer Mismatch"
  - "Finite Resources"
generators:
  - "Contract at Interfaces"
problem: "Parallel tracks produce incompatible outputs because no shared interface contract exists before work begins."
signals:
  - "parallel work must produce compatible outputs"
  - "integration fails due to interface mismatches"
  - "tracks can't communicate during development"
  - "neither track depends on the other's code"
fan_out:
  build: 4
stages:
  - name: interface-spec
    sheets: 1
    instrument_guidance: "score-author's choice — needs strong reasoning to write a precise, unambiguous interface contract; contract quality determines integration success. Proof score uses contract-designer (claude-code with extended timeout)."
    fallback_friendly: false
    purpose: "Define the shared interface contract before parallel work begins. Contract must be precise enough to prevent incompatible implementations but not so restrictive it eliminates parallelization benefits."
    artifacts: ["interface-spec.yaml"]
  - name: build
    sheets: "fan_out(4)"
    instrument_guidance: "score-author's choice — capability depends on what's being built (code generation, document creation, etc.); proof score uses code-builder (claude-code). Each instance builds independently against the contract."
    fallback_friendly: true
    purpose: "Build components in parallel according to the interface contract. Each track works independently without seeing other tracks' code."
    artifacts: ["component-*/**"]
  - name: integrate
    sheets: 1
    instrument_guidance: "score-author's choice — verification and assembly work; does not need highest capability if contract is solid. Proof score uses verifier (claude-code)."
    fallback_friendly: true
    purpose: "Assemble all pre-validated components and verify all interfaces match the contract. Integration is mechanical if the contract is precise."
    artifacts: []
composes_with:
  - pattern: "Barn Raising"
    how: "Barn Raising establishes shared conventions before Prefabrication's parallel tracks begin, providing the foundation that the interface contract builds upon."
  - pattern: "Clash Detection"
    how: "Clash Detection verifies no conflicts exist between assembled components after Prefabrication's integration stage completes."
  - pattern: "Mission Command"
    how: "Both patterns coordinate independent parallel work through shared intent artifacts — Prefabrication uses an interface contract, Mission Command uses a mission brief with intent envelope."
dependencies: {}
---

## Prefabrication

`Status: Working` · **Source:** Construction industry (offsite fabrication). **Forces:** Producer-Consumer Mismatch + Finite Resources.

### Core Dynamic

Define interface contracts before parallel work begins. Each parallel track gets a shared interface definition and builds to it. Integration only assembles pre-validated pieces. Different from Fan-out + Synthesis: prefabrication has an explicit interface specification stage before fan-out.

### When to Use / When NOT to Use

Use when parallel tracks must produce compatible outputs. Not when outputs are independent (use plain Fan-out) or when the interface can't be defined upfront.

### Marianne Score Structure

```yaml
sheets:
  - name: interface-spec
    prompt: "Define the shared API contract. Write interface-spec.yaml."
    validations:
      - type: file_exists
        path: "{{ workspace }}/interface-spec.yaml"
  - name: build
    instances: 4
    prompt: "Build component {{ instance_id }} according to interface-spec.yaml."
    capture_files: ["interface-spec.yaml"]
  - name: integrate
    prompt: "Assemble all components. Verify all interfaces match."
    capture_files: ["component-*/**"]
```

### Failure Mode

Interface spec too loose allows incompatible implementations. Too tight eliminates the benefits of parallel work.

### Composes With

Barn Raising, Clash Detection, Mission Command

---
name: "Relay Zone"
scale: score-level
type: orchestration-pattern
status: working
forces:
  - "Producer-Consumer Mismatch"
  - "Information Asymmetry"
generators: []
problem: "Cumulative outputs across pipeline stages exceed context window limits, degrading downstream agent performance."
signals:
  - "pipeline outputs growing too large for downstream context windows"
  - "later stages receiving more context than they can effectively use"
  - "information from early stages drowning out recent findings"
  - "need to preserve key findings while discarding volume"
stages:
  - name: relay
    sheets: 1
    instrument_guidance: "score-author's choice — needs strong enough comprehension to identify key findings and compress without losing critical information; sonnet recommended for cost-effective compression"
    fallback_friendly: true
    purpose: "Read all prior stage outputs and compress to a relay brief preserving key findings, open questions, and critical data at ~20% of original size."
    artifacts: ["relay-brief.md"]
composes_with:
  - pattern: "Fan-out + Synthesis"
    how: "Relay Zone compresses fan-out outputs before synthesis, preventing context window overflow when many parallel streams merge."
  - pattern: "Forward Observer"
    how: "Forward Observer summarizes large input for a single expensive stage; Relay Zone compresses accumulated outputs between any pipeline stages."
  - pattern: "Screening Cascade"
    how: "Relay Zone compresses accumulated results between screening stages, preventing context bloat as items escalate through the cascade."
dependencies: {}
---

## Relay Zone

`Status: Working` · **Source:** Track relay (athletics). **Forces:** Producer-Consumer Mismatch.

### Core Dynamic

Context compression between pipeline stages. A dedicated relay sheet reads the full output of the previous stage and produces a compressed summary for the next stage. Prevents context window bloat across long pipelines.

### When to Use / When NOT to Use

Use when cumulative outputs exceed context limits. Not when all information must survive compression.

### Marianne Score Structure

```yaml
sheets:
  - name: relay
    prompt: >
      Read all prior outputs. Compress to relay-brief.md:
      key findings, open questions, critical data only. Target 20% of original size.
    capture_files: ["full-output/**"]
    validations:
      - type: file_exists
        path: "{{ workspace }}/relay-brief.md"
      - type: command_succeeds
        command: "test $(wc -w < '{{ workspace }}/relay-brief.md') -lt 2000"
```

### Failure Mode

Relay loses critical information. Downstream stages produce incorrect results because the relay omitted a key finding. Validate relay completeness by checking key terms survive compression.

### Composes With

Fan-out + Synthesis, Forward Observer, Screening Cascade

---
name: "Quorum Consensus"
scale: "score-level"
type: "orchestration-pattern"
status: "working"
forces:
  - "Partial Failure"
  - "Finite Resources"
generators:
  - "Threshold-Triggered Switch"
problem: "Partial agent failure should not block the pipeline when majority agreement is sufficient."
signals:
  - "fan-out agents may fail unpredictably"
  - "partial failure shouldn't block downstream stages"
  - "need to proceed with majority agreement"
  - "some agents' failures are acceptable if quorum reached"
fan_out:
  analyze: 5
stages:
  - name: analyze
    sheets: "fan_out(5)"
    instrument_guidance: "score-author's choice — any instrument capable of analyzing the artifact; quorum is based on count, not quality"
    fallback_friendly: true
    purpose: "Execute analysis in parallel across 5 agents, each producing a workspace file."
    artifacts: ["analysis-*.md"]
  - name: quorum-check
    sheets: 1
    instrument_guidance: "cli instrument — executes validation command to verify that at least 3 analyses were produced"
    fallback_friendly: false
    purpose: "Verify that at least 3 of 5 agents produced valid outputs."
    artifacts: []
  - name: synthesize
    sheets: 1
    instrument_guidance: "score-author's choice — instrument should be capable of reading multiple analyses and synthesizing consensus; stronger instruments produce higher-quality synthesis"
    fallback_friendly: true
    purpose: "Synthesize consensus from successful analyses, noting which agents' outputs were missing."
    artifacts: []
composes_with:
  - pattern: "Triage Gate"
    how: "Triage Gate pre-filters candidates before Quorum Consensus's fan-out, reducing unnecessary agent invocations."
  - pattern: "Source Triangulation"
    how: "Source Triangulation enforces diversity across fan-out agents, preventing systematic bias that would corrupt the quorum validity."
  - pattern: "Fan-out + Synthesis"
    how: "Quorum Consensus is a specific implementation of Fan-out + Synthesis that adds a quorum check to handle partial failure, synthesizing results only from the successful majority."
dependencies: {}
---

## Quorum Consensus

`Status: Working` · **Source:** Distributed systems quorum. **Forces:** Partial Failure + Finite Resources.

### Core Dynamic

Accept results when a quorum (majority) of fan-out agents agree, even if some fail. N agents run; the synthesis stage proceeds when M of N produce valid output. The remaining agents' failures are logged but don't block the pipeline.

### When to Use / When NOT to Use

Use when fan-out may have partial failure and majority agreement is sufficient. Not when every agent's output is critical.

### Marianne Score Structure

```yaml
sheets:
  - name: analyze
    instances: 5
    prompt: "Analyze the artifact. Write analysis-{{ instance_id }}.md."
  - name: quorum-check
    instrument: cli
    validations:
      - type: command_succeeds
        command: "test $(ls {{ workspace }}/analysis-*.md 2>/dev/null | wc -l) -ge 3"
  - name: synthesize
    prompt: "Read available analyses. Note which are missing. Synthesize from quorum."
    capture_files: ["analysis-*.md"]
```

### Failure Mode

Quorum reached but the surviving agents all made the same error. Use Source Triangulation to ensure diversity.

### Composes With

Triage Gate, Source Triangulation, Fan-out + Synthesis

---
name: "Commissioning Cascade"
scale: instrument-strategy
type: orchestration-pattern
status: working
forces:
  - "Instrument-Task Fit"
  - "Exponential Defect Cost"
generators:
  - "Match Instrument to Grain"
  - "Graduate & Filter"
problem: "Different validation scopes require different tools; single-pass validation misses issues or wastes resources."
signals:
  - "unit tests pass but integration fails"
  - "validation is slow because all scopes use expensive instruments"
  - "can't diagnose failures because all tests run together"
  - "need different rigor levels for different scopes"
stages:
  - name: unit-check
    sheets: 1
    instrument_guidance: "cli — required for reliable shell command execution; capability is running shell commands"
    fallback_friendly: true
    purpose: "Run unit tests against the codebase."
    artifacts: []
  - name: integration-check
    sheets: 1
    instrument_guidance: "cli — required for reliable shell command execution; capability is running shell commands"
    fallback_friendly: true
    purpose: "Run integration tests against deployed services."
    artifacts: []
  - name: acceptance-review
    sheets: 1
    instrument_guidance: "score-author's choice — needs strong reasoning to evaluate test results against requirements; sonnet or opus recommended"
    fallback_friendly: false
    purpose: "Read test results and write acceptance report."
    artifacts: []
composes_with:
  - pattern: "Echelon Repair"
    how: "Echelon Repair classifies work items by difficulty; Commissioning Cascade validates each echelon's output using tier-appropriate validation instruments."
  - pattern: "Shipyard Sequence"
    how: "Shipyard Sequence progresses through launch stages; Commissioning Cascade validates each stage with scope-appropriate instruments."
  - pattern: "The Tool Chain"
    how: "The Tool Chain chains tools together; Commissioning Cascade validates the output of each tool using scope-appropriate instruments."
dependencies: {}
---

## Commissioning Cascade

`Status: Working` · **Source:** Marine vessel commissioning. **Forces:** Instrument-Task Fit + Exponential Defect Cost.

### Core Dynamic

Validate at multiple scopes using different tools at each level. Unit → integration → acceptance, each with scope-appropriate validation instruments. Split chained validations into separate checks so failures are diagnosable.

### When to Use / When NOT to Use

Use when different validation scopes require different tools. Not when a single validation pass suffices.

### Marianne Score Structure

```yaml
sheets:
  - name: unit-check
    instrument: cli
    validations:
      - type: command_succeeds
        command: "cd {{ workspace }} && python -m pytest tests/unit/ -q"
  - name: integration-check
    instrument: cli
    validations:
      - type: command_succeeds
        command: "cd {{ workspace }} && python -m pytest tests/integration/ -q"
  - name: acceptance-review
    prompt: "Read test results. Write acceptance report against the original requirements."
    capture_files: ["test-results/**"]
```

### Failure Mode

Unit tests pass but integration fails — the cascade catches this. If all validation is at one level, cascading adds no value.

### Composes With

Echelon Repair, Shipyard Sequence, The Tool Chain

---
name: "The Tool Chain"
scale: "instrument-strategy"
type: "orchestration-pattern"
status: "working"
forces:
  - "Instrument-Task Fit"
  - "Finite Resources"
  - "Producer-Consumer Mismatch"
generators:
  - "Match Instrument to Grain"
  - "Contract at Interfaces"
problem: "Expensive AI instruments waste budget on deterministic tasks that CLI tools could handle more cheaply."
signals:
  - "most pipeline stages are deterministic transformations"
  - "costs are high using AI instruments for every step"
  - "work is expressible as shell commands with exit codes"
  - "need to optimize cost without losing necessary judgment"
stages:
  - name: "plan"
    sheets: 1
    instrument_guidance: "claude — synthesizes processing plan from input characteristics; judgment needed"
    fallback_friendly: false
    purpose: "Read input and design a processing plan."
    artifacts: ["processing-plan.yaml"]
  - name: "fetch"
    sheets: 1
    instrument_guidance: "cli — curl is deterministic API call; no AI needed"
    fallback_friendly: true
    purpose: "Fetch raw data from the source API."
    artifacts: ["raw.csv"]
  - name: "clean"
    sheets: 1
    instrument_guidance: "cli — user-supplied Python script; data transformation is deterministic"
    fallback_friendly: true
    purpose: "Clean and normalize the raw data."
    artifacts: ["clean.csv"]
  - name: "analyze"
    sheets: 1
    instrument_guidance: "cli — user-supplied Python script; analysis logic is deterministic"
    fallback_friendly: true
    purpose: "Analyze cleaned data and produce structured report."
    artifacts: ["report.md"]
  - name: "interpret"
    sheets: 1
    instrument_guidance: "claude — interprets numerical results and synthesizes recommendations; judgment needed"
    fallback_friendly: false
    purpose: "Interpret analysis results and write executive summary with recommendations."
    artifacts: []
composes_with:
  - pattern: "Echelon Repair"
    how: "The Tool Chain implements Echelon Repair's E1 tier — deterministic work routed to CLI instruments for cost optimization."
  - pattern: "Commissioning Cascade"
    how: "Commissioning Cascade validates the output quality of each stage, especially the CLI-based transformations."
  - pattern: "Composting Cascade"
    how: "Composting Cascade accumulates CLI instrument exit codes and output as signal for overall process health."
script_dependencies:
  - "clean_data.py"
  - "analyze.py"
config_features:
  - "capture_files"
dependencies: {}
---

## The Tool Chain

`Status: Working` · **Source:** CI/CD pipelines (Jenkins, GitHub Actions), Expedition 1. **Scale:** score-level + instrument strategy. **Iteration:** 4.

### Core Dynamic

Inverts the corpus default: non-AI tools do primary work, AI agents appear only at planning, triage, and interpretation points. Instrument selection follows the work's nature: deterministic work gets deterministic tools, judgment work gets judgment instruments. Most real-world pipelines are 80% deterministic tools, 20% AI judgment.

**Implementation note:** Sheets with `instrument: cli` use validation commands as the execution mechanism. The sheet has no `prompt` — the `command_succeeds` validation IS the work. This is a valid Marianne pattern for deterministic stages.

### When to Use / When NOT to Use

Use when most stages are deterministic transformations (data processing, code compilation, format conversion), when work is expressible as CLI commands with exit codes, when cost matters — CLI instruments are free. Not when every stage requires judgment or output can't be validated by exit code alone.

### Marianne Score Structure

```yaml
sheets:
  - name: plan
    instrument: claude
    prompt: "Read input. Produce processing-plan.yaml."
  - name: fetch
    instrument: cli
    validations:
      - type: command_succeeds
        command: "curl -sf -o {{ workspace }}/raw.csv 'https://api.example.com/data'"
  - name: clean
    instrument: cli
    validations:
      - type: command_succeeds
        command: "python3 {{ workspace }}/clean_data.py {{ workspace }}/raw.csv {{ workspace }}/clean.csv"
  - name: analyze
    instrument: cli
    validations:
      - type: command_succeeds
        command: "python3 {{ workspace }}/analyze.py {{ workspace }}/clean.csv {{ workspace }}/report.md"
  - name: interpret
    instrument: claude
    prompt: "Read report.md. Write executive summary with recommendations."
    capture_files: ["report.md"]
```

**Script dependencies:** `clean_data.py` and `analyze.py` must exist in the workspace — seeded via prelude, generated by the plan sheet, or supplied by the user.

### Failure Mode

CLI stages fail silently when piped: `cmd | tail -5` always exits 0. Use `bash -c '...; exit ${PIPESTATUS[0]}'` in `command_succeeds` validations. AI stages used where CLI suffices waste budget.

### Example

Survey processing: AI plans, `curl` fetches, `python3` cleans and analyzes, AI writes executive summary. Cost: ~$0.50 instead of ~$5.00 all-LLM.

### Composes With

Echelon Repair (tool chain IS echelon E1), Commissioning Cascade (CLI tiers for validation), Composting Cascade (CLI instruments as thermometers)

---
name: "Canary Probe"
scale: score-level
type: orchestration-pattern
status: working
forces:
  - "Progressive Commitment"
generators:
  - "Incremental Exposure"
problem: "Full-scale execution risks loss of resources and time when pipeline changes or output formats are unproven."
signals:
  - "batch processing many items with unproven pipeline"
  - "pipeline changes with uncertain format impact"
  - "high cost of full-scale failure"
  - "need validated evidence before full commitment"
fan_out:
  canary-run: 3
  full-run: 20
stages:
  - name: select-canary
    sheets: 1
    instrument_guidance: "score-author's choice — needs capability to identify structurally representative items (different sizes, formats, edge cases); haiku acceptable"
    fallback_friendly: true
    purpose: "Select a small representative subset from the full item list for testing."
    artifacts: ["canary-manifest.yaml"]
  - name: canary-run
    sheets: "fan_out(3)"
    instrument_guidance: "score-author's choice — MUST match the exact instruments used in full-run; canary tests the identical pipeline"
    fallback_friendly: false
    purpose: "Execute the full pipeline on each canary item using identical instruments and validations."
    artifacts: ["canary-result-{{ instance_id }}.md"]
  - name: canary-evaluate
    sheets: 1
    instrument_guidance: "score-author's choice — needs analysis and reasoning capability; haiku acceptable"
    fallback_friendly: true
    purpose: "Analyze all canary results and produce a go/no-go verdict with detailed reasoning."
    artifacts: ["canary-verdict.yaml"]
  - name: canary-gate
    sheets: 1
    instrument_guidance: "cli — purely gatekeeping logic checking the verdict file; no LLM needed"
    fallback_friendly: false
    purpose: "Enforce the canary verdict; halt execution if canary failed."
    artifacts: []
  - name: full-run
    sheets: "fan_out(20)"
    instrument_guidance: "score-author's choice — must match canary-run instruments; processes remaining items"
    fallback_friendly: false
    purpose: "Execute the full pipeline at scale on remaining items, conditional on canary verdict passing."
    artifacts: []
composes_with:
  - pattern: "Progressive Rollout"
    how: "Canary Probe IS the validation gate and phase 1 of Progressive Rollout before scaling to full deployment."
  - pattern: "Dead Letter Quarantine"
    how: "Canary Probe's failures reveal items that should be sent to Dead Letter Quarantine instead of full-run processing."
  - pattern: "Speculative Hedge"
    how: "Run Canary Probe on each hedge path before committing full-run resources to one strategy."
dependencies: {}
---

## Canary Probe

`Status: Working` · **Source:** DevOps canary deployment, military recon-in-force, Expedition 5. **Scale:** score-level. **Iteration:** 4. **Force:** Progressive Commitment.

### Core Dynamic

Run a miniature version of the full pipeline on a tiny subset of real data before committing to full scale. The canary uses the EXACT SAME pipeline — identical instruments, validations, prompts — just on fewer items. If the canary dies, you've lost almost nothing. If it lives, you have evidence (not hope) that full-scale execution works.

**Representativeness caveat:** Canary testing's fundamental limitation is that the subset must be representative. If it isn't, you learn nothing. The selection stage should use structural diversity criteria (different file sizes, different formats, edge cases), not random sampling.

### When to Use / When NOT to Use

Use for any score operating on a list of items, migration scores, batch processing, or concert coordination where Score B depends on Score A's output format. Not when the canary subset can't be representative (tail-risk failures) or setup cost makes a probe nearly as expensive as the full run.

### Marianne Score Structure

```yaml
sheets:
  - name: select-canary
    prompt: >
      Select 3 representative items from the full set, choosing for structural diversity
      (different sizes, formats, edge cases). Write canary-manifest.yaml listing selected items.
    validations:
      - type: file_exists
        path: "{{ workspace }}/canary-manifest.yaml"
  - name: canary-run
    instances: 3
    prompt: >
      Read canary-manifest.yaml. Process item at index {{ instance_id }}.
      Write result to canary-result-{{ instance_id }}.md.
    capture_files: ["canary-manifest.yaml"]
    validations:
      - type: file_exists
        path: "{{ workspace }}/canary-result-{{ instance_id }}.md"
  - name: canary-evaluate
    prompt: >
      Read all canary results. Evaluate: did each produce valid output?
      Write canary-verdict.yaml: {go: true/false, results: [{item, pass, reason}]}.
    capture_files: ["canary-result-*.md", "canary-manifest.yaml"]
    validations:
      - type: command_succeeds
        command: "python3 -c \"import yaml; v=yaml.safe_load(open('{{ workspace }}/canary-verdict.yaml')); assert 'go' in v\""
  - name: canary-gate
    instrument: cli
    validations:
      - type: command_succeeds
        command: "python3 -c \"import yaml; v=yaml.safe_load(open('{{ workspace }}/canary-verdict.yaml')); assert v['go'], 'Canary failed'\""
  - name: full-run
    instances: 20
    prompt: "Process remaining items from the full set."
    capture_files: ["canary-manifest.yaml"]
```

### Failure Mode

Canary passes but full run fails — the canary subset was unrepresentative. Mitigate by selecting for structural diversity, not convenience. If the canary itself is expensive (complex setup), the pattern provides no cost advantage — use a simpler validation gate instead.

### Composes With

Progressive Rollout (canary IS phase 1), Dead Letter Quarantine (canary failures reveal quarantine candidates), Speculative Hedge (canary each hedge path before committing)

---
name: "Speculative Hedge"
scale: score-level
type: orchestration-pattern
status: working
forces:
  - "Progressive Commitment"
generators:
  - "Incremental Exposure"
problem: "Choosing one approach that fails requires expensive restart from scratch, wasting the initial attempt's cost."
signals:
  - "uncertain which approach will work for this problem"
  - "starting over after failed approach costs more than running both"
  - "need guaranteed progress despite approach uncertainty"
  - "multiple valid strategies exist but success is unpredictable"
stages:
  - name: analyze
    sheets: 1
    instrument_guidance: "sonnet or opus — requires strategic analysis to define competing approaches and robust evaluation criteria"
    fallback_friendly: false
    purpose: "Analyze the problem and define two competing approaches with evaluation criteria."
    artifacts: ["hedge-plan.yaml"]
  - name: approach-a
    sheets: 1
    instrument_guidance: "score-author's choice — instrument must match the task complexity; mechanical transformations may use cheaper instruments than clean-room rewrites"
    fallback_friendly: true
    purpose: "Execute approach A using mechanical transformation strategy."
    artifacts: ["approach-a-result/**"]
  - name: approach-b
    sheets: 1
    instrument_guidance: "score-author's choice — clean-room rewrites typically need stronger reasoning than mechanical transforms; choose based on actual task complexity"
    fallback_friendly: false
    purpose: "Execute approach B using clean-room rewrite strategy."
    artifacts: ["approach-b-result/**"]
  - name: evaluate
    sheets: 1
    instrument_guidance: "sonnet or opus — must run tests, evaluate results, and make justified winner selection with rationale"
    fallback_friendly: false
    purpose: "Run tests against both approaches and select winner with rationale."
    artifacts: ["hedge-decision.yaml"]
composes_with:
  - pattern: "Canary Probe"
    how: "Canary Probe validates each approach on a small subset before Speculative Hedge commits full resources to parallel execution."
config_features:
  - "capture_files"
  - "command_succeeds"
dependencies: {}
---

## Speculative Hedge

`Status: Working` · **Source:** CPU branch prediction, military COA analysis, financial hedging, Expedition 5. **Scale:** score-level. **Iteration:** 4. **Force:** Progressive Commitment.

### Core Dynamic

Run DIFFERENT strategies on the SAME problem and commit to whichever succeeds. Not fan-out (same task, different data) — this runs different APPROACHES on the same data. The cost analysis: if retry-from-scratch costs more than running both, hedge.

**Execution note:** In current Marianne, approaches run sequentially (sheets execute in order). This means the delivery time is the SUM of both approaches, not the MAX. The value proposition is not time savings but elimination of the "wrong approach, start over" scenario — you always get at least one valid result. For true parallel hedging, use two separate scores in a concert.

### When to Use / When NOT to Use

Use for migration tasks with unknown edge cases, research with multiple search strategies, any task where "wrong approach, retry" costs more than "both approaches, discard one." Not when both approaches are equally expensive and success rate is high, when budget is hard-capped, or when approaches interfere.

### Marianne Score Structure

```yaml
sheets:
  - name: analyze
    prompt: "Analyze the problem. Define two approaches and evaluation criteria. Write hedge-plan.yaml."
  - name: approach-a
    prompt: "Execute approach A: mechanical transformation. Write all output to approach-a-result/."
  - name: approach-b
    prompt: "Execute approach B: clean-room rewrite guided by tests. Write all output to approach-b-result/."
    capture_files: ["hedge-plan.yaml"]
  - name: evaluate
    prompt: "Run tests against both. Write hedge-decision.yaml: {winner, rationale, test_results}."
    capture_files: ["approach-a-result/**", "approach-b-result/**"]
    validations:
      - type: command_succeeds
        command: "python3 -c \"import yaml; d=yaml.safe_load(open('{{ workspace }}/hedge-decision.yaml')); assert 'winner' in d\""
```

### Failure Mode

Both approaches fail — the hedge didn't reduce risk, it doubled cost. Mitigate with a Canary Probe on each approach before full execution. If approaches write to the same files (no subdirectory isolation), they clobber each other's output — always use separate output directories.

### Composes With

Canary Probe (canary each approach before full hedge)

---
name: "Dead Letter Quarantine"
scale: score-level
type: orchestration-pattern
status: working
proof_score: "dead-letter-quarantine.yaml"
forces:
  - "Partial Failure"
  - "Information Asymmetry"
  - "Finite Resources"
generators:
  - "Exploit Failure as Signal"
  - "Accumulate Knowledge"
problem: "Batch processing repeatedly fails on the same items because no systematic analysis identifies root causes or adapts strategy."
signals:
  - "some items consistently fail across retries"
  - "batch processing has persistent partial failures"
  - "retry loops waste resources on unfixable items"
  - "no visibility into why certain items fail while others succeed"
  - "failures seem random but may have underlying patterns"
fan_out:
  process: 10
config_features:
  - fan_out
stages:
  - name: process
    sheets: "fan_out(10)"
    instrument_guidance: "score-author's choice — initial batch processing; proof score demonstrates haiku for cost efficiency, but any capable instrument works"
    fallback_friendly: true
    purpose: "Process batch items in parallel, writing success results to workspace files."
    artifacts: ["result-*.md"]
  - name: collect
    sheets: 1
    instrument_guidance: "score-author's choice — failure detection and categorization; needs judgment to classify error types and extract symptoms from missing/malformed outputs"
    fallback_friendly: true
    purpose: "Identify failed items from missing or invalid outputs and create structured quarantine manifest."
    artifacts: ["quarantine.yaml"]
  - name: analyze-quarantine
    sheets: 1
    instrument_guidance: "capable instrument required — cross-failure pattern analysis is the core Dead Letter Quarantine dynamic; identifies systematic causes not visible in individual failures; proof score recommends opus"
    fallback_friendly: false
    purpose: "Analyze quarantined items to identify common failure patterns and design adapted reprocessing strategies."
    artifacts: ["quarantine-analysis.md"]
  - name: reprocess
    sheets: 1
    instrument_guidance: "score-author's choice — applies adapted strategies from analysis; needs sufficient capability for the underlying task (code generation, data transformation, etc.)"
    fallback_friendly: true
    purpose: "Reprocess quarantined items using adapted strategies that address identified root causes."
    artifacts: ["reprocess-results.yaml"]
composes_with:
  - pattern: "Triage Gate"
    how: "Triage Gate's BLACK-category items (reject/quarantine) feed directly into Dead Letter Quarantine's collection stage for batch pattern analysis."
  - pattern: "Screening Cascade"
    how: "Screening Cascade's rejected items route to Dead Letter Quarantine, where accumulated rejections reveal systematic criteria gaps in the screening filters."
  - pattern: "Circuit Breaker"
    how: "Circuit Breaker halts processing and routes tripped failures to Dead Letter Quarantine for root cause analysis before resuming."
  - pattern: "Immune Cascade"
    how: "Dead Letter Quarantine handles items that fail Immune Cascade's successive verification stages, analyzing what defects survived earlier tiers."
  - pattern: "After-Action Review"
    how: "After-Action Review can analyze Dead Letter Quarantine's pattern-finding process itself, extracting doctrine about what kinds of failures cluster."
dependencies: {}
---

## Dead Letter Quarantine

`Status: Working` · **Source:** RabbitMQ/Kafka dead letter queues, Expedition 5. **Scale:** score-level. **Iteration:** 4. **Force:** Graceful Failure.

### Core Dynamic

After N retries, STOP RETRYING AND QUARANTINE. Move failed items to a separate processing path with different handling: different instruments, different prompts, different strategy. The quarantine is an ARTIFACT that persists, accumulates, and can be ANALYZED. "Why did these 7 items fail?" often reveals a systematic issue that fixing once clears the entire quarantine.

### When to Use / When NOT to Use

Use for any batch processing where some items are expected to fail, self-chaining scores where iteration N should not re-attempt items from N-1, or concert-level routing of failures to a different score. Not when every item MUST succeed, failures are truly random, or the quarantine grows to dwarf successful items (the pipeline itself is broken).

### Marianne Score Structure

```yaml
sheets:
  - name: process
    instances: 10
    prompt: "Process item {{ instance_id }}. Write result-{{ instance_id }}.md on success."
  - name: collect
    prompt: >
      Identify failures (missing or empty result files). Write quarantine.yaml listing
      failed items with {item_id, error_symptom, attempted_strategy}.
    capture_files: ["result-*.md"]
  - name: analyze-quarantine
    prompt: >
      Read quarantine.yaml. Identify common failure patterns.
      Write quarantine-analysis.md with: {pattern, affected_items, suggested_strategy}.
    capture_files: ["quarantine.yaml"]
    validations:
      - type: file_exists
        path: "{{ workspace }}/quarantine-analysis.md"
  - name: reprocess
    prompt: >
      Read quarantine-analysis.md. For each failure pattern, apply the suggested strategy.
      Write reprocess-results.yaml: [{item_id, outcome: success|permanent_quarantine, detail}].
    capture_files: ["quarantine.yaml", "quarantine-analysis.md"]
    validations:
      - type: command_succeeds
        command: "python3 -c \"import yaml; r=yaml.safe_load(open('{{ workspace }}/reprocess-results.yaml')); success=[e for e in r if e['outcome']=='success']; print(f'{len(success)}/{len(r)} reprocessed successfully')\""
```

### Failure Mode

Quarantine analysis finds no patterns — items failed for unrelated reasons. The reprocess stage still runs but the "adapted strategy" has nothing to adapt from. In this case, escalate to a more capable instrument (Opus) rather than repeating the same strategy. If the quarantine grows across self-chain iterations, the pipeline itself needs debugging, not the items.

### Composes With

Triage Gate (BLACK category feeds quarantine), Screening Cascade (rejected items go to quarantine for pattern analysis), Circuit Breaker (circuit-tripped failures enter quarantine)

---
name: "Clash Detection"
scale: score-level
type: orchestration-pattern
status: working
forces:
  - "Exponential Defect Cost"
  - "Producer-Consumer Mismatch"
  - "Information Asymmetry"
generators:
  - "Exploit Failure as Signal"
  - "Gate on Environmental Readiness"
problem: "Parallel tracks produce conflicting artifacts that break integration, and discovering conflicts during integration is expensive."
signals:
  - "parallel work needs to integrate but conflicts are unpredictable"
  - "integration testing is expensive"
  - "contracts can't anticipate all conflict modes"
  - "need to detect conflicts before attempting merge"
fan_out:
  track-work: 4
stages:
  - name: track-work
    sheets: "fan_out(4)"
    instrument_guidance: "score-author's choice — instrument must match the component-building task complexity; pattern is instrument-agnostic for this stage"
    fallback_friendly: true
    purpose: "Build one component in parallel with other tracks"
    artifacts: []
  - name: clash-scan
    sheets: 1
    instrument_guidance: "sonnet or better — needs analytical capability to compare outputs across all tracks, detect naming collisions, interface mismatches, and resource conflicts; missing conflicts defeats the pattern's purpose"
    fallback_friendly: false
    purpose: "Compare all parallel track outputs to detect conflicts without attempting merge"
    artifacts: ["clash-report.yaml"]
  - name: integrate
    sheets: 1
    instrument_guidance: "score-author's choice — depends on integration complexity; pattern focuses on pre-integration detection, not integration method"
    fallback_friendly: true
    purpose: "Assemble all track outputs after clash detection passes"
    artifacts: []
composes_with:
  - pattern: "Prefabrication"
    how: "Prefabrication defines interface contracts for parallel tracks; Clash Detection verifies those contracts weren't violated and catches unanticipated conflicts."
  - pattern: "Andon Cord"
    how: "When Clash Detection finds conflicts (non-zero clash_count), Andon Cord halts integration and triggers diagnostic workflow to analyze root cause."
  - pattern: "The Tool Chain"
    how: "The Tool Chain provides CLI tools (linters, static analyzers) that Clash Detection invokes to find structural conflicts beyond what LLM inspection catches."
config_features:
  - "fan_out"
  - "capture_files"
  - "command_succeeds"
dependencies: {}
---

## Clash Detection

`Status: Working` · **Source:** MEP coordination / BIM in construction, Expedition 1. **Scale:** score-level. **Iteration:** 4.

### Core Dynamic

After parallel tracks produce outputs but BEFORE integration, a dedicated stage compares all outputs for CONFLICTS — without trying to merge them. Cheaper than integration testing. Different from the contract (which prevents KNOWN conflict classes) and integration testing (which discovers conflicts empirically). Clash detection uses the OUTPUTS as inputs, overlays them, and searches for interference patterns. The scope is detection, not resolution — downstream stages handle fixes.

### When to Use / When NOT to Use

Use when parallel tracks produce artifacts that must coexist (code modules, config files, API schemas), when the contract can't anticipate all conflict modes, or when integration testing is expensive enough that catching conflicts earlier saves meaningful cost. Not when parallel tracks produce truly independent artifacts, when the contract is exhaustive, or when parallel work is done by the same agent.

### Marianne Score Structure

```yaml
sheets:
  - name: track-work
    instances: 4
    prompt: "Build component {{ instance_id }}."
  - name: clash-scan
    prompt: >
      Read ALL track outputs. Search for naming collisions, interface mismatches,
      resource conflicts. Write clash-report.yaml with {clashes: [{type, items, detail}], clash_count: N}.
    capture_files: ["track-*/**"]
    validations:
      - type: command_succeeds
        command: "python3 -c \"import yaml; r=yaml.safe_load(open('{{ workspace }}/clash-report.yaml')); c=r.get('clash_count',0) if r else 0; assert c==0, f'{c} clashes found'\""
  - name: integrate
    prompt: "Assemble all track outputs."
    capture_files: ["track-*/**"]
```

### Failure Mode

Clash detection finds conflicts — the assertion fails, blocking integration. This is the INTENDED behavior. The score author must add a resolution stage after clash-scan that fixes conflicts and re-runs the scan. If clash-report.yaml is malformed or missing the `clash_count` key, the validation fails with a clear assertion error rather than a cryptic KeyError.

### Composes With

Prefabrication (clash detection after prefab tracks), Andon Cord (clash triggers diagnostic), The Tool Chain (CLI clash detection for structural conflicts)

---
name: "Rashomon Gate"
scale: score-level
type: orchestration-pattern
status: working
forces:
  - "Structured Disagreement"
generators:
  - "Frame Multiplication"
  - "Verify through Diverse Observers"
problem: "Single-frame analysis produces unreliable conclusions when the optimal analytical perspective is unknown."
signals:
  - "the right analytical frame is unknown"
  - "multiple valid perspectives exist (security, performance, maintainability)"
  - "risk is getting the right answer from the wrong frame"
  - "need to distinguish genuine ambiguity from frame artifacts"
fan_out:
  analyze: 4
config_features:
  - "fan_out"
  - "cadenza"
stages:
  - name: evidence
    sheets: 1
    instrument_guidance: "score-author's choice — capability depends on what artifact needs assembly (document analysis, code audit, synthesis work)"
    fallback_friendly: true
    purpose: "Assemble the artifact that all analyst instances will examine from their different frames."
    artifacts: ["evidence/**"]
  - name: analyze
    sheets: "fan_out(4)"
    instrument_guidance: "score-author's choice — needs analytical capability appropriate to the domain; all instances should use similar-strength instruments to avoid confounding frame differences with capability differences"
    fallback_friendly: true
    purpose: "Analyze the evidence through an assigned analytical frame (security, performance, maintainability, correctness) provided via cadenza."
    artifacts: ["analysis-{{ instance_id }}.md"]
  - name: triangulate
    sheets: 1
    instrument_guidance: "score-author's choice — must distinguish genuine disagreement from different vocabulary and identify agreement patterns across frames; sonnet or opus recommended"
    fallback_friendly: false
    purpose: "Categorize all findings by agreement level (UNANIMOUS, MAJORITY, SPLIT, UNIQUE) and produce structured triangulation report."
    artifacts: ["triangulation.yaml"]
composes_with:
  - pattern: "Source Triangulation"
    how: "Rashomon Gate varies analytical frames over the same evidence; Source Triangulation varies evidence sources — they can be nested for full cross-product validation."
  - pattern: "Sugya Weave (Editorial Synthesis)"
    how: "Sugya Weave synthesizes the categorized findings from Rashomon Gate into a coherent position that acknowledges where frames agree and disagree."
  - pattern: "Commander's Intent Envelope"
    how: "Each analytical frame definition acts as a Commander's Intent Envelope for that instance, defining perspective constraints while leaving method autonomous."
dependencies: {}
---

## Rashomon Gate

`Status: Working` · **Source:** Kurosawa's *Rashomon* (1950), epistemological frame analysis, Expedition 6. **Scale:** score-level. **Iteration:** 4. **Force:** Structured Disagreement.

### Core Dynamic

Every fan-out instance gets the SAME evidence but analyzes from a DIFFERENT analytical frame. Contradictions are not failures — they are data. The synthesis categorizes findings by agreement level: UNANIMOUS (high confidence), MAJORITY, SPLIT (genuine ambiguity), UNIQUE (deep insight or frame artifact). The PATTERN of agreement across frames reveals more than any single analysis.

Different from Source Triangulation (which divides sources) and plain fan-out (which divides work). The cadenza mechanism (see Glossary) maps 1:1 to instances — each instance receives a different frame file defining its analytical perspective.

### When to Use / When NOT to Use

Use for problems where the right analytical frame is unknown, security audits (attacker/defender/compliance), code review (correctness/maintainability/performance), any task where the risk is "right answer from the wrong frame." Not when frames are so similar they produce trivially similar outputs, evidence is unambiguous, or the synthesis agent can't distinguish genuine disagreement from different vocabulary.

### Marianne Score Structure

```yaml
sheets:
  - name: evidence
    prompt: "Assemble the artifact all analysts will examine."
  - name: analyze
    instances: 4
    cadenza:
      - "frame-security.md"
      - "frame-performance.md"
      - "frame-maintainability.md"
      - "frame-correctness.md"
    prompt: "Analyze the evidence through your assigned frame. Write analysis-{{ instance_id }}.md."
    capture_files: ["evidence/**"]
    validations:
      - type: file_exists
        path: "{{ workspace }}/analysis-{{ instance_id }}.md"
  - name: triangulate
    prompt: >
      Read all analyses. For EACH finding across all frames, categorize:
      UNANIMOUS (all frames agree), MAJORITY (most agree), SPLIT (even division), UNIQUE (one frame only).
      Write triangulation.yaml: {findings: [{finding, category, frames_agreeing, detail}], summary_counts: {unanimous: N, majority: N, split: N, unique: N}}.
    capture_files: ["analysis-*.md"]
    validations:
      - type: command_succeeds
        command: "python3 -c \"import yaml; t=yaml.safe_load(open('{{ workspace }}/triangulation.yaml')); assert len(t.get('findings',[])) > 0, 'No findings categorized'\""
```

### Failure Mode

Frames too similar produce trivially UNANIMOUS results — the gate adds cost without insight. Frames too dissimilar produce all UNIQUE results — no agreement signal to act on. The optimal frame set produces a mix of categories. If the validation only checks for keyword presence (UNANIMOUS/SPLIT), an agent can write the keywords without doing the categorization. The `command_succeeds` validation checking finding count prevents this.

### Composes With

Source Triangulation (Rashomon for frames, triangulation for sources), Sugya Weave (weave the triangulated findings into a position), Commander's Intent Envelope (frame IS the intent for each instance)

---
name: "Graceful Retreat"
scale: score-level
type: orchestration-pattern
status: working
forces:
  - "Partial Failure"
  - "Finite Resources"
generators:
  - "Exploit Failure as Signal"
problem: "Long-running work risks total failure on hard deadlines unless tiers of acceptable output are planned in advance."
signals:
  - "work has hard time deadlines where partial output has value"
  - "downstream pipeline stages can adapt to variable completeness"
  - "attempting full completion might waste resources or miss deadlines"
stages:
  - name: execute
    sheets: 1
    instrument_guidance: "score-author's choice — any instrument capable of the actual work (code analysis, content generation, research, etc.); instrument selection determines speed and depth of Tier 1 attempt; weaker instruments may force faster fallback to Tier 2/3"
    fallback_friendly: true
    purpose: "Attempt Tier 1 (full output), fall back to Tier 2 (core sections) or Tier 3 (summary) if needed. Produce completion-status.yaml recording which tier was achieved."
    artifacts: ["completion-status.yaml", "analysis.md"]
  - name: verify-tier
    sheets: 1
    instrument_guidance: "cli — lightweight validation of tier claims; verifies completion-status.yaml and asserts that claimed tier's artifacts exist with expected content"
    fallback_friendly: true
    purpose: "Independently verify that claimed tier achievement matches the artifact contents; check that core sections exist if Tier 2+ claimed."
    artifacts: []
composes_with:
  - pattern: "Andon Cord"
    how: "When Graceful Retreat selects a lower tier, Andon Cord provides detailed diagnostics of what failed in the higher tier for process improvement."
  - pattern: "Dead Letter Quarantine"
    how: "Tier 3 summary-only outputs are routed to Dead Letter Quarantine for enhanced reprocessing with additional resources or different instruments."
  - pattern: "Cathedral Construction"
    how: "Graceful Retreat completes one iteration within time constraints; Cathedral Construction continues work across iterations without losing prior partial progress."
dependencies: {}
---

`Status: Working` · **Source:** Military phased withdrawal, Netflix degradation, Expedition 5. **Scale:** score-level. **Iteration:** 4. **Force:** Graceful Failure.

### Core Dynamic

Defines TIERS OF COMPLETENESS upfront. Tier 1: full output, all sections. Tier 2: core sections only. Tier 3: summary-only with pointers to what couldn't be completed. Each tier has its own validation criteria. If Tier 1 fails, the agent falls back to Tier 2 rather than failing entirely. The retreat is PLANNED — tiers defined in the prompt, not discovered during failure.

**Enforcement note:** Tier achievement is self-reported by the agent. For structural enforcement, a downstream CLI validation sheet should independently verify which tier's criteria are met, rather than trusting the agent's `tier_achieved` claim.

### When to Use / When NOT to Use

Use for long-running sheets where partial output has value, hard deadlines where "something by Tuesday" beats "perfection by Thursday," or pipeline stages where downstream can operate on partial input. Not when partial output is dangerous (security audits, financial calculations) or downstream can't distinguish "complete but simple" from "incomplete due to retreat."

### Marianne Score Structure

```yaml
sheets:
  - name: execute
    prompt: |
      TIER 1 (attempt first): Full analysis with all 5 sections (overview, architecture, security, performance, recommendations).
      TIER 2 (if Tier 1 fails): 3 core sections (overview, architecture, recommendations).
      TIER 3 (if Tier 2 fails): Executive summary with top-3 issues only.

      Write completion-status.yaml: {tier_achieved: 1|2|3, sections_completed: [], sections_skipped: [], reason}.
      Write the analysis to analysis.md.
    validations:
      - type: file_exists
        path: "{{ workspace }}/completion-status.yaml"
      - type: file_exists
        path: "{{ workspace }}/analysis.md"
  - name: verify-tier
    instrument: cli
    validations:
      - type: command_succeeds
        command: "python3 -c \"import yaml; s=yaml.safe_load(open('{{ workspace }}/completion-status.yaml')); tier=s['tier_achieved']; content=open('{{ workspace }}/analysis.md').read(); checks={'overview' in content.lower(), 'architecture' in content.lower()}; assert all(checks), f'Tier {tier} claimed but missing core sections'\""
```

### Failure Mode

Agent always retreats to Tier 3 because it's easiest — the retreat becomes the default. Validate that Tier 1 was genuinely attempted (check for partial Tier 1 artifacts). If downstream stages can't adapt to different tiers, the retreat produces useless partial output — ensure downstream reads `completion-status.yaml` and adjusts expectations.

### Composes With

Andon Cord (retreat triggers diagnostic), Dead Letter Quarantine (Tier 3 outputs enter quarantine for enhanced reprocessing), Cathedral Construction (retreat within a single iteration, continue next)

---
name: "Source Triangulation"
scale: score-level
type: orchestration-pattern
status: working
proof_score: "source-triangulation.yaml"
forces:
  - "Information Asymmetry"
  - "Structured Disagreement"
generators:
  - "Verify through Diverse Observers"
  - "Frame Multiplication"
problem: "Single-source analysis cannot detect contradictions between what code does, documentation says, and tests prove."
signals:
  - "technical claims need independent verification"
  - "multiple source types exist (code, docs, tests, benchmarks)"
  - "single perspective might miss contradictions"
  - "need to categorize claims as corroborated vs uncorroborated"
stages:
  - name: extract
    sheets: 1
    instrument_guidance: "haiku or similar cheap instrument — claim extraction is straightforward identification work, doesn't require deep reasoning"
    fallback_friendly: true
    purpose: "Extract and structure claims that need verification, defining verification criteria for each."
    artifacts: ["01-claims.md"]
  - name: investigate
    sheets: "fan_out(3)"
    instrument_guidance: "sonnet or similar mid-tier instrument — each voice needs code/doc/test reading and analysis capability to find supporting or contradicting evidence"
    fallback_friendly: false
    purpose: "Analyze from assigned source (code/docs/tests) to find evidence supporting or contradicting each claim."
    artifacts: ["02-code-findings.md", "02-docs-findings.md", "02-test-findings.md"]
  - name: triangulate
    sheets: 1
    instrument_guidance: "opus or sonnet — deep cross-referencing synthesis requires strong reasoning to categorize claims across all source evidence"
    fallback_friendly: false
    purpose: "Cross-reference all investigation results to categorize each claim as CORROBORATED, UNCORROBORATED, or CONTRADICTED."
    artifacts: ["03-triangulation.md"]
dependencies:
  investigate: [extract]
  triangulate: [investigate]
fan_out:
  investigate: 3
composes_with:
  - pattern: "Rashomon Gate"
    how: "Rashomon Gate applies different analytical frames to the same evidence; Source Triangulation divides the evidence itself across structurally different source types."
  - pattern: "Triage Gate"
    how: "Triage Gate filters incoming claims before Source Triangulation's multi-source investigation, preventing waste on obviously true or false claims."
  - pattern: "Sugya Weave (Editorial Synthesis)"
    how: "Source Triangulation's three investigation voices (code, docs, tests) feed into Sugya Weave (Editorial Synthesis)'s dialectical synthesis when claims require interpretive layering beyond fact-checking."
---

## Source Triangulation

`Status: Working` · **Source:** Journalism, intelligence analysis. **Forces:** Information Asymmetry.

### Core Dynamic

Multiple agents analyze the SAME problem from DIFFERENT sources. The synthesis identifies: corroborated (multiple sources agree), uncorroborated (single source), and contradicted (sources disagree). Different from Rashomon Gate (which uses different frames on same evidence). Source Triangulation divides the evidence itself.

### When to Use / When NOT to Use

Use when claims need independent verification and multiple source types exist. Not when a single authoritative source suffices.

### Marianne Score Structure

```yaml
sheets:
  - name: investigate
    instances: 3
    cadenza:
      - "source-code.md"
      - "source-docs.md"
      - "source-tests.md"
    prompt: "Analyze from your assigned source. Write findings-{{ instance_id }}.md."
    validations:
      - type: file_exists
        path: "{{ workspace }}/findings-{{ instance_id }}.md"
  - name: triangulate
    prompt: >
      Read all findings. Categorize each claim: CORROBORATED (2+ sources),
      UNCORROBORATED (1 source), CONTRADICTED (sources disagree).
    capture_files: ["findings-*.md"]
```

### Failure Mode

Sources too similar produce trivially corroborated results. Ensure sources are structurally independent.

### Composes With

Rashomon Gate, Triage Gate, Sugya Weave (Editorial Synthesis)

---
name: "Talmudic Page"
scale: score-level
type: orchestration-pattern
status: working
forces:
  - "Information Asymmetry"
generators:
  - "Accumulate Knowledge"
problem: "Multiple perspectives on an artifact produce disconnected analyses when commentaries reference only the source, not each other."
signals:
  - "primary artifact needs multi-layer annotation"
  - "analysis requires multiple perspectives anchored to one text"
  - "commentaries should reference both source and each other"
  - "single-perspective analysis is insufficient"
fan_out:
  commentary: 3
stages:
  - name: central-text
    sheets: 1
    instrument_guidance: "score-author's choice — needs reasoning capability to produce substantive core analysis that anchors all commentary"
    fallback_friendly: false
    purpose: "Write the core analysis that serves as the central reference text."
    artifacts: ["core-analysis.md"]
  - name: commentary
    sheets: "fan_out(3)"
    instrument_guidance: "score-author's choice — each instance provides a perspective on the central text; cheaper instruments acceptable if commentary task is straightforward"
    fallback_friendly: true
    purpose: "Read the core analysis and write commentary from a specific perspective."
    artifacts: ["commentary-1.md", "commentary-2.md", "commentary-3.md"]
  - name: interlink
    sheets: 1
    instrument_guidance: "score-author's choice — must track and cross-reference multiple sources (core + all commentaries); sonnet or opus recommended for synthesis work"
    fallback_friendly: false
    purpose: "Synthesize the core analysis and all commentaries, highlighting cross-references and inter-commentary connections."
    artifacts: ["synthesis.md"]
composes_with:
  - pattern: "Sugya Weave (Editorial Synthesis)"
    how: "Sugya Weave extends Talmudic Page's multi-layer commentary structure with editorial synthesis that extracts themes across all layers."
  - pattern: "Fan-out + Synthesis"
    how: "Talmudic Page is Fan-out + Synthesis with the constraint that all fan-out instances must reference a shared central text, creating hub-and-spoke commentary structure."
dependencies: {}
---

## Talmudic Page

`Status: Working` · **Source:** Talmudic commentary layout (Mishnah + Gemara + commentaries). **Forces:** Information Asymmetry.

### Core Dynamic

A central text surrounded by commentary layers at different levels of abstraction. The central text anchors all commentary; each layer responds to the text AND to other layers. Produces interlinked multi-perspective analysis without losing the central thread.

### When to Use / When NOT to Use

Use when a primary artifact needs multi-layer annotation. Not when commentaries are independent (use plain Fan-out).

### Marianne Score Structure

```yaml
sheets:
  - name: central-text
    prompt: "Write the core analysis."
  - name: commentary
    instances: 3
    prompt: "Read the core analysis. Write commentary from your perspective."
    capture_files: ["core-analysis.md"]
  - name: interlink
    prompt: "Read core + all commentaries. Write cross-referenced synthesis."
    capture_files: ["core-analysis.md", "commentary-*.md"]
```

### Failure Mode

Commentaries ignore each other and respond only to the central text. The interlink stage must reference cross-commentary connections.

### Composes With

Sugya Weave, Fan-out + Synthesis

---
name: "Forward Observer"
scale: instrument-strategy
type: orchestration-pattern
status: working
forces:
  - "Finite Resources"
  - "Information Asymmetry"
generators:
  - "Match Instrument to Grain"
problem: "Expensive instruments waste resources reading raw input; cheap summarization can preserve actionable information."
signals:
  - "input exceeds available context window"
  - "expensive instrument required for main task"
  - "token costs dominate total cost"
  - "most input is redundant or low-value"
stages:
  - name: observe
    sheets: 1
    instrument_guidance: "haiku — fast, cheap observation; sufficient for compression and extraction of key items"
    fallback_friendly: true
    purpose: "Read large input and extract key findings and actionable items into observer-brief.md."
    artifacts: ["observer-brief.md"]
  - name: operate
    sheets: 1
    instrument_guidance: "opus — full reasoning capability required for detailed analysis on compressed input"
    fallback_friendly: false
    purpose: "Execute main analysis and detailed work based on the observer-brief.md summary."
    artifacts: []
composes_with:
  - pattern: "Relay Zone"
    how: "Forward Observer produces a formatted brief that Relay Zone can reliably relay between stages."
  - pattern: "Screening Cascade"
    how: "Screening Cascade filters volume before Forward Observer compresses the remainder for expensive instruments."
  - pattern: "Immune Cascade"
    how: "Immune Cascade escalates difficult items to expensive instruments; Forward Observer compresses large items for those same instruments."
dependencies: {}
---

## Forward Observer

`Status: Working` · **Source:** Military forward observation. **Forces:** Finite Resources + Information Asymmetry.

### Core Dynamic

A cheap, fast observer (instrument: haiku or sonnet) reads large input and produces a compressed brief for the expensive operator (instrument: opus). Reduces context window pressure and cost. The observer cost must save more tokens downstream than it consumes.

### When to Use / When NOT to Use

Use when input is too large for the main instrument or when cheap summarization preserves actionable information. Not when all information is critical.

### Marianne Score Structure

```yaml
sheets:
  - name: observe
    instrument: haiku
    prompt: "Read the full input. Write observer-brief.md: key findings, actionable items only."
    validations:
      - type: file_exists
        path: "{{ workspace }}/observer-brief.md"
  - name: operate
    instrument: opus
    prompt: "Read observer-brief.md. Execute the detailed analysis."
    capture_files: ["observer-brief.md"]
```

### Failure Mode

Observer discards critical information. Validate by checking brief covers all major topics from the input.

### Composes With

Relay Zone, Screening Cascade, Immune Cascade

---
name: "Closed-Loop Call"
scale: score-level
type: orchestration-pattern
status: working
forces:
  - "Producer-Consumer Mismatch"
  - "Partial Failure"
generators:
  - "Contract at Interfaces"
  - "Exploit Failure as Signal"
problem: "Semantic drift across pipeline stages when consumers misunderstand producer outputs."
signals:
  - "handoff fidelity is critical"
  - "semantic drift is a real risk"
  - "stages have non-obvious dependencies"
  - "previous stage outputs are ambiguous"
stages:
  - name: produce
    sheets: 1
    instrument_guidance: "score-author's choice — any instrument capable of writing structured output with key decisions listed"
    fallback_friendly: true
    purpose: "Write output with a manifest listing key decisions."
    artifacts: ["manifest.yaml"]
  - name: consume
    sheets: 1
    instrument_guidance: "score-author's choice — instrument must be capable of reading and comprehending the produce output"
    fallback_friendly: true
    purpose: "Read output and write a readback confirming comprehension of each decision."
    artifacts: ["readback.yaml"]
  - name: verify
    sheets: 1
    instrument_guidance: "cli — Python validation script comparing manifest.yaml and readback.yaml for structural alignment"
    fallback_friendly: false
    purpose: "Validate that the readback matches the manifest structure, catching semantic drift."
    artifacts: []
composes_with:
  - pattern: "Prefabrication"
    how: "Prefabrication defines strict output contracts that Closed-Loop Call verifies are correctly understood."
  - pattern: "Relay Zone"
    how: "Relay Zone compresses accumulated outputs between stages; Closed-Loop Call verifies the compressed handoff preserved semantic meaning."
  - pattern: "Succession Pipeline"
    how: "Succession Pipeline chains execution stages; Closed-Loop Call ensures each handoff maintains semantic fidelity."
dependencies: {}
---

## Closed-Loop Call

`Status: Working` · **Source:** Aviation CRM callout-response protocol. **Forces:** Producer-Consumer Mismatch + Partial Failure.

### Core Dynamic

Explicit handoff verification between stages. Stage A produces output. Stage B reads it and writes back a confirmation of what it understood. A CLI validation compares the two. Prevents semantic drift across pipeline stages.

### When to Use / When NOT to Use

Use when handoff fidelity is critical and semantic drift is a real risk. Not when stages are trivially compatible.

### Marianne Score Structure

```yaml
sheets:
  - name: produce
    prompt: "Write output with manifest.yaml listing key decisions."
  - name: consume
    prompt: "Read output. Write readback.yaml confirming your understanding of each decision."
    capture_files: ["manifest.yaml", "output/**"]
  - name: verify
    instrument: cli
    validations:
      - type: command_succeeds
        command: "python3 -c \"import yaml; m=yaml.safe_load(open('{{ workspace }}/manifest.yaml')); r=yaml.safe_load(open('{{ workspace }}/readback.yaml')); assert set(m.keys())==set(r.keys()), f'Key mismatch: {set(m.keys())-set(r.keys())}'\""
```

### Failure Mode

Readback is verbatim copy, not comprehension check. The validation should check structural understanding, not string matching.

### Composes With

Relay Zone, Prefabrication, Succession Pipeline

---
name: "Sugya Weave (Editorial Synthesis)"
scale: within-stage
type: orchestration-pattern
status: working
forces:
  - "Information Asymmetry"
  - "Convergence Imperative"
generators: []
problem: "Diverse inputs need synthesis into an authoritative position with argued support, not neutral aggregation."
signals:
  - "multiple perspectives exist but need editorial judgment"
  - "summary isn't sufficient — need a supported position"
  - "inputs are diverse and require interpretation"
  - "neutrality would hide necessary judgment calls"
stages:
  - name: weave
    sheets: 1
    instrument_guidance: "score-author's choice — needs strong reasoning for position-taking and argument construction; sonnet or opus recommended for editorial depth"
    fallback_friendly: false
    purpose: "Read diverse inputs, take an argued position, and produce editorial synthesis with supporting evidence and acknowledged counterarguments."
    artifacts: ["editorial-synthesis.md"]
composes_with:
  - pattern: "Fan-out + Synthesis"
    how: "Fan-out produces diverse inputs; Sugya Weave synthesizes them with an editorial position rather than neutral aggregation."
  - pattern: "Source Triangulation"
    how: "Source Triangulation provides multiple perspectives; Sugya Weave adjudicates between them with an argued position on which is most credible."
  - pattern: "Rashomon Gate"
    how: "Rashomon Gate produces multiple interpretations; Sugya Weave takes a supported position on which interpretation best fits the evidence."
dependencies: {}
---

## Sugya Weave (Editorial Synthesis)

`Status: Working` · **Source:** Talmudic sugya structure. **Forces:** Information Asymmetry + Convergence Imperative.

### Core Dynamic

Not just synthesis — editorial synthesis. The weaver takes a POSITION on the inputs, arguing for one interpretation while acknowledging alternatives. Produces an opinionated conclusion, not a summary. Requires structured validation that the position is supported.

### When to Use / When NOT to Use

Use when diverse inputs need an authoritative position, not just aggregation. Not when neutrality is required.

### Marianne Score Structure

```yaml
sheets:
  - name: weave
    prompt: >
      Read all inputs. Take a position. Write editorial-synthesis.md with:
      POSITION, SUPPORTING EVIDENCE, COUNTERARGUMENTS, CONCLUSION.
    capture_files: ["input-*.md"]
    validations:
      - type: content_contains
        content: "POSITION:"
      - type: content_contains
        content: "COUNTERARGUMENTS:"
```

### Failure Mode

Position is unsupported assertion. Validate that supporting evidence references specific inputs.

### Composes With

Fan-out + Synthesis, Source Triangulation, Rashomon Gate

---
name: "Barn Raising"
scale: score-level
type: orchestration-pattern
status: working
forces:
  - "Producer-Consumer Mismatch"
  - "Finite Resources"
generators:
  - "Contract at Interfaces"
problem: "Parallel work streams produce inconsistent structure and style when each agent makes independent convention choices."
signals:
  - "parallel agents will work on similar types of artifacts"
  - "consistency in naming, structure, or style matters for integration"
  - "each agent might make reasonable but incompatible choices"
  - "prefabrication contracts aren't enough — need broader standards"
fan_out:
  build: 6
config_features:
  - "fan_out"
  - "capture_files"
stages:
  - name: conventions
    sheets: 1
    instrument_guidance: "score-author's choice — needs strong reasoning to anticipate integration needs and write comprehensive but not overly rigid conventions; sonnet or opus recommended"
    fallback_friendly: true
    purpose: "Write a conventions document defining naming, structure, and stylistic standards for parallel work streams."
    artifacts: ["conventions.md"]
  - name: build
    sheets: "fan_out(6)"
    instrument_guidance: "score-author's choice — depends on task complexity; instrument must be capable of the actual work being coordinated"
    fallback_friendly: true
    purpose: "Build assigned component following the shared conventions."
    artifacts: []
dependencies:
  build: ["conventions"]
composes_with:
  - pattern: "Prefabrication"
    how: "Prefabrication defines strict interface contracts (input/output schemas), while Barn Raising establishes broader conventions (naming, style, structure) that complement those contracts."
  - pattern: "Mission Command"
    how: "Mission Command provides the intent envelope defining what to achieve, while Barn Raising provides the implementation conventions defining how to structure the work."
  - pattern: "Lines of Effort"
    how: "Lines of Effort separates parallel streams of work; Barn Raising ensures those streams remain consistent through shared conventions."
---

## Barn Raising

`Status: Working` · **Source:** Community barn raising (Amish). **Forces:** Producer-Consumer Mismatch + Finite Resources.

### Core Dynamic

Shared conventions established before parallel work. A conventions document defines naming, structure, interfaces. All parallel tracks read it. Different from Prefabrication (which defines interfaces). Barn Raising defines conventions — broader scope, softer constraints.

### When to Use / When NOT to Use

Use when parallel agents need consistency beyond interface contracts. Not when a single agent does all work.

### Marianne Score Structure

```yaml
sheets:
  - name: conventions
    prompt: "Write conventions.md: naming rules, file structure, code style."
    validations:
      - type: file_exists
        path: "{{ workspace }}/conventions.md"
  - name: build
    instances: 6
    prompt: "Read conventions.md. Build component {{ instance_id }}."
    capture_files: ["conventions.md"]
```

### Failure Mode

Conventions too vague to enforce consistency. Too rigid to allow agent judgment. Strike the balance based on integration requirements.

### Composes With

Prefabrication, Mission Command, Lines of Effort

---
name: "Nurse Log"
scale: score-level
type: orchestration-pattern
status: working
forces:
  - "Finite Resources"
generators: []
problem: "Downstream stages waste resources redoing common preparation work because no shared substrate exists."
signals:
  - "multiple stages need the same research or data collection"
  - "agents are duplicating preparation work"
  - "downstream work is blocked waiting for common prerequisites"
config_features:
  - "fan_out"
fan_out:
  work: 4
stages:
  - name: prepare-substrate
    sheets: 1
    instrument_guidance: "score-author's choice — needs capability for thorough research, data collection, and organization; sonnet or opus recommended because substrate quality is load-bearing for all downstream instances"
    fallback_friendly: false
    purpose: "Research the domain, collect reference material, and organize it into shared substrate."
    artifacts: ["substrate/"]
  - name: work
    sheets: "fan_out(4)"
    instrument_guidance: "score-author's choice — depends on component-building task complexity; substrate reading requires minimal capability, but actual component construction may require more reasoning"
    fallback_friendly: true
    purpose: "Build component using the prepared substrate."
    artifacts: []
composes_with:
  - pattern: "Fermentation Relay"
    how: "Fermentation Relay can escalate the substrate preparation stage if initial research proves insufficient for downstream work."
  - pattern: "Fan-out + Synthesis"
    how: "Nurse Log's work stage uses fan-out to build components in parallel; Fan-out + Synthesis adds a synthesis stage to combine those parallel outputs."
dependencies: {}
---

## Nurse Log

`Status: Working` · **Source:** Forest ecology (nurse logs). **Forces:** Finite Resources.

### Core Dynamic

A preparation stage creates general-purpose substrate (research, data collection, organization) that makes downstream stages more productive. Different from Reconnaissance Pull (which discovers the approach). Nurse Log prepares the ground regardless of approach.

### When to Use / When NOT to Use

Use when downstream stages share common preparation needs. Not when preparation is stage-specific.

### Marianne Score Structure

```yaml
sheets:
  - name: prepare-substrate
    prompt: "Research the domain. Collect reference material. Organize into substrate/."
    validations:
      - type: file_exists
        path: "{{ workspace }}/substrate/"
  - name: work
    instances: 4
    prompt: "Read substrate/. Build component {{ instance_id }}."
    capture_files: ["substrate/**"]
```

### Failure Mode

Substrate too generic to help. Make preparation specific to the downstream work, not a generic research dump.

### Composes With

Fermentation Relay, Fan-out + Synthesis

---

## Concert-Level Patterns (v4)

---
name: "Lines of Effort"
scale: concert-level
type: orchestration-pattern
status: approximation
forces:
  - "Information Asymmetry"
  - "Finite Resources"
generators: []
problem: "Parallel campaign workstreams drift apart without convergence mechanisms connecting distinct efforts toward a unified end state."
signals:
  - "campaign has distinct workstreams with different objectives"
  - "parallel efforts must converge toward a shared end state"
  - "workstreams need autonomy but unified direction"
  - "coordination should happen through shared state, not message passing"
approximation_note: "The YAML demonstrates a single-score approximation using fan-out sheets for parallel lines. True Lines of Effort requires concert-level orchestration where each line is its own score with independent instruments, success criteria, and lifecycle, coordinated through shared workspace state."
config_features:
  - fan_out
fan_out:
  line-work: 3
stages:
  - name: define-lines
    sheets: 1
    instrument_guidance: "score-author's choice — needs strong reasoning to define distinct objectives and measurable convergence criteria for each line"
    fallback_friendly: false
    purpose: "Define lines of effort with objectives and convergence criteria."
    artifacts: ["lines-definition.md"]
  - name: line-work
    sheets: "fan_out(3)"
    instrument_guidance: "score-author's choice — each line may need different capability depending on its objective; instrument should match the line's task complexity"
    fallback_friendly: true
    purpose: "Execute each line of effort per its defined objectives, working independently within shared workspace."
    artifacts: []
  - name: convergence-check
    sheets: 1
    instrument_guidance: "score-author's choice — needs strong synthesis capability to assess convergence across all lines toward unified end state"
    fallback_friendly: false
    purpose: "Read all line outputs and assess convergence toward the unified end state."
    artifacts: []
composes_with:
  - pattern: "Season Bible"
    how: "Season Bible maintains the mutable reference document that tracks evolving state across lines, ensuring continuity as each line progresses."
  - pattern: "After-Action Review"
    how: "After-Action Review evaluates each line's execution against its objectives, feeding lessons into subsequent convergence checks."
  - pattern: "Barn Raising"
    how: "Barn Raising establishes shared conventions across all lines before parallel execution begins, preventing convention drift between independent workstreams."
dependencies: {}
---

## Lines of Effort

`Status: Working (single-score approximation)` · **Source:** Military operational design (JP 5-0). **Forces:** Information Asymmetry + Finite Resources.

### Core Dynamic

Sustained parallel campaigns with different objectives converging toward a unified end state. Each line has its own scores, instruments, and success criteria. Coordination through shared workspace state, not message passing. Requires concert-level orchestration with multiple scores.

### When to Use / When NOT to Use

Use for large campaigns with distinct workstreams that must converge. Not when workstreams are independent or campaign is short.

### Marianne Score Structure

```yaml
# Single-score approximation — true Lines of Effort requires a concert
sheets:
  - name: define-lines
    prompt: "Define 3 lines of effort with objectives and convergence criteria."
  - name: line-work
    instances: 3
    prompt: "Execute line {{ instance_id }} per the defined objectives."
    capture_files: ["lines-definition.md"]
  - name: convergence-check
    prompt: "Read all line outputs. Assess convergence toward unified end state."
    capture_files: ["line-*/**"]
```

### Failure Mode

Lines diverge without convergence checks. Regular synchronization points are essential.

### Composes With

Season Bible, After-Action Review, Barn Raising

---
name: "Season Bible"
scale: concert-level
type: orchestration-pattern
status: working
forces:
  - "Producer-Consumer Mismatch"
generators:
  - "Contract at Interfaces"
problem: "Multi-score campaigns lose continuity because agents lack shared memory of prior decisions and evolving constraints."
signals:
  - "scores make decisions inconsistent with earlier work"
  - "agents repeat mistakes or ignore prior learnings"
  - "no central record of evolving state across campaign"
  - "continuity errors accumulate as work progresses"
stages:
  - name: read-bible
    sheets: 1
    instrument_guidance: "score-author's choice — needs reading comprehension to extract relevant constraints from the bible; any capable instrument"
    fallback_friendly: true
    purpose: "Read season-bible.md to understand current state and constraints before beginning work."
    artifacts: []
  - name: work
    sheets: 1
    instrument_guidance: "score-author's choice — instrument depends entirely on the nature of the work being performed; bible reading is context, not the task"
    fallback_friendly: false
    purpose: "Execute the actual work while respecting constraints documented in the bible."
    artifacts: []
  - name: update-bible
    sheets: 1
    instrument_guidance: "score-author's choice — needs to write coherent documentation updates; sonnet or haiku sufficient for most continuity recording"
    fallback_friendly: true
    purpose: "Update season-bible.md with new decisions, state changes, and continuity constraints discovered during work."
    artifacts: ["season-bible.md"]
composes_with:
  - pattern: "Lines of Effort"
    how: "Multiple parallel effort lines all read and update the shared bible, maintaining cross-stream continuity."
  - pattern: "Relay Zone"
    how: "Relay Zone compresses accumulated outputs to prevent context overflow; Season Bible preserves canonical state that survives compression, ensuring continuity decisions persist across relayed handoffs."
  - pattern: "Cathedral Construction"
    how: "Long-running iterative construction where the bible accumulates architectural decisions and constraints across iterations."
dependencies: {}
---

## Season Bible

`Status: Working` · **Source:** Television production (show bible). **Forces:** Producer-Consumer Mismatch.

### Core Dynamic

A mutable reference document that evolves as the campaign progresses. Different from Barn Raising conventions (which are static). The bible records decisions, character evolutions, and continuity constraints. Scores read it before starting and update it after completing.

### When to Use / When NOT to Use

Use for multi-score campaigns needing continuity. Not for single-score work.

### Marianne Score Structure

```yaml
sheets:
  - name: read-bible
    prompt: "Read season-bible.md. Note current state and constraints."
    capture_files: ["season-bible.md"]
  - name: work
    prompt: "Execute work respecting bible constraints."
  - name: update-bible
    prompt: "Update season-bible.md with new decisions and state changes."
    validations:
      - type: content_contains
        path: "{{ workspace }}/season-bible.md"
        content: "Updated:"
```

### Failure Mode

Bible grows stale — scores read it but don't update. Validate update stage actually modifies the bible.

### Composes With

Lines of Effort, Relay Zone, Cathedral Construction

---
name: "Saga Compensation Chain"
scale: concert-level
type: orchestration-pattern
status: aspirational
blocked_by: "on_failure handlers — Marianne does not yet support on_failure actions in score/concert configuration"
forces:
  - "Partial Failure"
generators: []
problem: "Partial completion of a multi-score concert leaves inconsistent shared state with no automated path to undo forward steps."
signals:
  - "concert scores produce side effects on shared state"
  - "partial completion is worse than full rollback"
  - "manual cleanup after failure is expensive and error-prone"
  - "each score's effects need a documented undo path"
stages:
  - name: forward-step
    sheets: 1
    instrument_guidance: "score-author's choice — instrument must handle the domain task (migration, transformation, etc.); capability depends on task complexity"
    fallback_friendly: false
    purpose: "Execute one forward step of the saga, appending side effects and compensation path to saga-log.yaml."
    artifacts: ["saga-log.yaml"]
  - name: compensate
    sheets: 1
    instrument_guidance: "score-author's choice — must be capable enough to read the saga log and execute compensations in reverse order; same capability tier as forward steps"
    fallback_friendly: false
    purpose: "Read saga-log.yaml and execute compensation actions in reverse order to neutralize forward steps' side effects."
    artifacts: []
composes_with:
  - pattern: "After-Action Review"
    how: "The saga compensation log feeds After-Action Review with structured records of what succeeded, what failed, and what was compensated."
dependencies: {}
---

## Saga Compensation Chain

`Status: Aspirational [on_failure compensation actions]` · **Source:** Garcia-Molina & Salem (1987), distributed transactions, Expedition 4. **Scale:** concert-level. **Iteration:** 4. **Force:** Graceful Failure.

### Core Dynamic

Every forward score in a concert is paired with a compensating score. If score Tk fails, compensations run Ck-1, Ck-2, ..., C1 in reverse order — not rollback (commits already happened) but forward-acting undo. The compensation isn't "delete what you made" — it's a score that produces artifacts neutralizing the forward score's effects.

**Implementation status:** Marianne does not yet have `on_failure` actions. The pattern can be approximated today with: (1) each forward score writes to `saga-log.yaml` documenting its side effects and compensation path, (2) on manual detection of failure, the user runs a separate compensation score that reads the saga log and undoes in reverse order.

### When to Use / When NOT to Use

Use for multi-score concerts where each score produces side effects on shared state, when partial completion is worse than full rollback, or when manual cleanup cost exceeds compensation engineering cost. Not when scores are idempotent, when scores don't produce side effects beyond workspace files, or when the concert is short enough for manual recovery.

### Marianne Score Structure

```yaml
# Forward score — writes to saga log for compensation context
sheets:
  - name: forward-step
    prompt: >
      Execute the migration step. Append to saga-log.yaml:
      {step: "schema-migration", artifacts: [...], side_effects: [...], compensation: "revert-schema.yaml"}.
    validations:
      - type: command_succeeds
        command: "python3 -c \"import yaml; log=yaml.safe_load(open('{{ workspace }}/saga-log.yaml')); assert len(log) > 0\""

# Compensation score (run manually or via future on_failure)
# sheets:
#   - name: compensate
#     prompt: "Read saga-log.yaml. For each entry in REVERSE order, execute the compensation."
#     capture_files: ["saga-log.yaml"]
```

### Failure Mode

Compensation scores can also fail — producing "compensation failure" on top of the original failure. Keep compensations simple and idempotent. The saga log must be written BEFORE side effects, not after — otherwise a crash between effect and log entry leaves uncompensatable state.

### Composes With

After-Action Review (compensation log feeds AAR), Look-Ahead Window (pre-check compensation score availability)

---
name: "Progressive Rollout"
scale: concert-level
type: orchestration-pattern
status: working
forces:
  - "Progressive Commitment"
generators:
  - "Incremental Exposure"
problem: "Full deployment before validation risks large-scale failure; incremental rollout with monitoring gates progression but requires coordinating batch selection, execution, and go/no-go decisions across phases."
signals:
  - "works on 5 doesn't guarantee works on 500"
  - "need to detect scaling issues before full deployment"
  - "rollback from 100% deployment is expensive"
  - "early validation could prevent large-scale failures"
config_features:
  - "self_chaining"
  - "fan_out"
  - "max_chain_depth"
  - "inherit_workspace"
fan_out:
  execute-batch: 5
stages:
  - name: select-batch
    sheets: 1
    instrument_guidance: "score-author's choice — any instrument capable of reading YAML state, computing batch sizes, and updating rollout state; algorithmic task suitable for any tier"
    fallback_friendly: true
    purpose: "Select the next batch based on current rollout phase and update state."
    artifacts: ["current-batch.yaml", "rollout-state.yaml"]
  - name: execute-batch
    sheets: "fan_out(5)"
    instrument_guidance: "score-author's choice — instrument depends on the actual work being rolled out (refactoring needs strong code reasoning, data migrations may need specific domain knowledge)"
    fallback_friendly: false
    purpose: "Process items in the current batch with 5 parallel workers."
    artifacts: []
  - name: monitor
    sheets: 1
    instrument_guidance: "score-author's choice — any instrument capable of analyzing results, computing error rates, and making threshold-based go/no-go decisions"
    fallback_friendly: true
    purpose: "Compute health metrics and determine whether to proceed to the next phase."
    artifacts: ["phase-verdict.yaml"]
composes_with:
  - pattern: "Canary Probe"
    how: "Canary Probe provides the initial safety probe that becomes phase 1 of Progressive Rollout's graduated deployment sequence."
  - pattern: "Dead Letter Quarantine"
    how: "Dead Letter Quarantine analyzes failed items from each rollout phase to determine whether failures are systemic or isolated."
dependencies: {}
---

## Progressive Rollout

`Status: Working` · **Source:** DevOps graduated deployment, feature flags, Expedition 5. **Scale:** concert-level. **Iteration:** 4. **Force:** Progressive Commitment.

### Core Dynamic

Apply a change in PHASES with increasing scope. Each phase's success GATES the next. Each phase's monitoring INFORMS the next's parameters. Different from Canary Probe (probe-then-full). Progressive Rollout is probe → 10% → 25% → 50% → 100%.

**Implementation note:** Marianne's `instances` field is static per score execution. The rollout achieves graduated scaling through the select-batch sheet: each self-chain iteration reads `rollout-state.yaml` to determine which items are in the current batch. The instance count stays fixed (e.g., 5 parallel workers), but the batch selection grows across iterations.

### When to Use / When NOT to Use

Use for large-scale migrations, multi-repository changes, any operation where "works on 5" doesn't guarantee "works on 500." Not when items are not independent or monitoring can't distinguish success from luck.

### Marianne Score Structure

```yaml
sheets:
  - name: select-batch
    prompt: >
      Read rollout-state.yaml (or initialize if first run).
      Select the next batch: phase 1 = 3 items, phase 2 = 20, phase 3 = 80, phase 4 = remainder.
      Write current-batch.yaml and update rollout-state.yaml with phase number and processed items.
    capture_files: ["rollout-state.yaml"]
    validations:
      - type: file_exists
        path: "{{ workspace }}/current-batch.yaml"
  - name: execute-batch
    instances: 5
    prompt: "Read current-batch.yaml. Process items assigned to worker {{ instance_id }}."
    capture_files: ["current-batch.yaml"]
  - name: monitor
    prompt: >
      Compute health metrics for this phase. Write phase-verdict.yaml:
      {go: bool, phase: N, confidence, items_processed, items_remaining, error_rate}.
    validations:
      - type: command_succeeds
        command: "python3 -c \"import yaml; v=yaml.safe_load(open('{{ workspace }}/phase-verdict.yaml')); assert v.get('go', False), f'Phase {v.get(\"phase\")} failed: error_rate={v.get(\"error_rate\")}'\""
on_success:
  action: self
  inherit_workspace: true
  max_chain_depth: 10
```

### Failure Mode

Early phases pass with small samples but later phases fail at scale — sampling bias. If error rate exceeds threshold at any phase, the rollout pauses (self-chain breaks on failed validation) and Dead Letter Quarantine analyzes failures. `max_chain_depth` prevents infinite rollout if the termination condition (`items_remaining == 0`) isn't reached.

### Composes With

Canary Probe (canary IS phase 1), Dead Letter Quarantine (failed items in each phase), Stratification Gate (N consecutive healthy phases before advancing)

---
name: "Systemic Acquired Resistance"
scale: concert-level
type: orchestration-pattern
status: working
forces:
  - "Accumulated Signal"
generators:
  - "Threshold-Triggered Switch"
problem: "Failures encountered in one score don't inform subsequent scores in a concert, causing repeated failures across the campaign."
signals:
  - "scores in a concert face similar threats"
  - "first-encounter failure cost is high"
  - "failures repeat across scores in a concert"
  - "no mechanism to share failure recovery"
config_features:
  - capture_files
  - on_success
  - inherit_workspace
stages:
  - name: work
    sheets: 1
    instrument_guidance: "score-author's choice — must handle failure recovery and write structured primers; stronger instruments produce more effective countermeasures"
    fallback_friendly: false
    purpose: "Execute the primary task while reading relevant defense primers and writing new primers when recovering from failures."
    artifacts: ["output.md", "priming/*.yaml"]
composes_with:
  - pattern: "After-Action Review"
    how: "Primers are structured AAR output — AAR extracts lessons, SAR broadcasts them as actionable defenses."
  - pattern: "Back-Slopping (Learning Inheritance)"
    how: "Back-Slopping (Learning Inheritance) provides the mechanism for culture inheritance; SAR structures that culture as threat-specific primers."
  - pattern: "Circuit Breaker"
    how: "Circuit Breaker generates a failure signal; SAR captures that signal as a primer to adjust future behavior."
dependencies: {}
---

## Systemic Acquired Resistance

`Status: Working` · **Source:** Plant immune priming (SAR/ISR), Expedition 2. **Scale:** concert-level. **Iteration:** 4. **Force:** Accumulated Signal.

### Core Dynamic

When a score recovers from a failure, it broadcasts failure-derived defenses to all subsequent scores via structured `priming/` directory. Primed scores CHANGE BEHAVIOR — adjusting prompts, validation thresholds, or monitoring. The priming is specific: a rate-limit encounter primes for rate-limit handling, not general defensiveness.

**Primer schema:** Each primer file in `priming/` follows: `{threat_type: string, trigger_signature: string, countermeasure: string, confidence: float, timestamp: string}`. Downstream scores read primers matching their threat surface and incorporate countermeasures into their prompts.

### When to Use / When NOT to Use

Use for concert campaigns where scores face related threat landscapes, when failure in one score should make the entire campaign more resilient, or when first-encounter failure cost is high. Not when scores face unrelated threats, the priming signal is too vague, or defense overhead degrades unaffected scores (autoimmune response — primers that are too broad cause unnecessary caution).

### Marianne Score Structure

```yaml
sheets:
  - name: work
    prompt: |
      Before starting, read priming/ for defense primers matching your work type.
      For each relevant primer, incorporate the countermeasure into your approach.

      Execute the primary task. Write output to output.md.

      If you encounter and recover from a failure, write a primer to priming/:
      File: priming/{threat_type}.yaml
      Schema: {threat_type, trigger_signature, countermeasure, confidence, timestamp}.
    capture_files: ["priming/*.yaml"]
    validations:
      - type: file_exists
        path: "{{ workspace }}/output.md"
```

### Failure Mode

Primers too broad cause autoimmune response — every score wastes tokens on irrelevant defenses. Primers too narrow never match. The `trigger_signature` field is the key: specific enough to match real threats, broad enough to generalize. If primers accumulate without pruning, the priming directory becomes noise. Include a `confidence` field and prune low-confidence primers after N uses without trigger.

### Composes With

After-Action Review (primers are structured AAR output), Back-Slopping (Learning Inheritance) (priming IS culture inheritance across scores), Circuit Breaker (primer from circuit-tripped instrument)

---

## Communication Patterns (v4)

---
name: "Stigmergic Workspace"
scale: communication
type: orchestration-pattern
status: working
forces:
  - "Information Asymmetry"
  - "Finite Resources"
generators: []
problem: "Parallel agents duplicate effort or produce conflicts because they lack visibility into each other's progress and decisions."
signals:
  - "parallel agents need loose coordination without direct messaging"
  - "workspace files already capture meaningful state other agents need"
  - "real-time coordination would create bottlenecks"
  - "agents react to each other's outputs, not each other's messages"
config_features:
  - "fan_out"
  - "capture_files"
fan_out:
  work: 8
stages:
  - name: work
    sheets: "fan_out(8)"
    instrument_guidance: "score-author's choice — this is a communication mechanism, not an execution prescription; instrument depends entirely on the actual task the workers perform"
    fallback_friendly: true
    purpose: "Read workspace for current state, perform assigned work, write results and signals to shared directories for other workers to discover."
    artifacts: ["shared/signals/"]
composes_with:
  - pattern: "Barn Raising"
    how: "Barn Raising establishes shared workspace conventions (naming, directory structure, file formats) that prevent Stigmergic Workspace's failure mode of conflicting writes."
  - pattern: "Lines of Effort"
    how: "Lines of Effort organizes sustained parallel campaigns that use Stigmergic Workspace as their coordination mechanism — each line reads and writes to shared workspace state."
dependencies: {}
---

## Stigmergic Workspace

`Status: Working` · **Source:** Ant colony optimization. **Forces:** Information Asymmetry + Finite Resources.

### Core Dynamic

Agents coordinate through workspace artifacts, not direct communication. Agent A writes a file; Agent B reads it. No messages, no coordination protocol — the workspace IS the communication channel.

### When to Use / When NOT to Use

Use when agents need loose coordination and the workspace captures state. Not when real-time coordination is needed.

### Marianne Score Structure

```yaml
sheets:
  - name: work
    instances: 8
    prompt: >
      Read workspace for current state. Do your work. Write results.
      If you find something relevant to other workers, write it to shared/signals/.
    capture_files: ["shared/signals/**"]
```

### Failure Mode

Conflicting writes to the same file. Use namespaced output directories per instance.

### Composes With

Barn Raising, Lines of Effort

## Adaptation Patterns (v4)

---
name: "Read-and-React"
scale: adaptation
type: prompt-technique
status: working
forces:
  - "Partial Failure"
  - "Information Asymmetry"
generators:
  - "Gate on Environmental Readiness"
problem: "Downstream agents follow fixed behavior regardless of upstream results because their prompts don't instruct them to inspect and adapt to workspace state."
signals:
  - "downstream behavior should change based on upstream results"
  - "adaptation path is not known before execution begins"
  - "workspace state determines which work is needed next"
  - "agents proceed with default behavior ignoring what previous stages produced"
config_features:
  - "capture_files"
stages:
  - name: work
    sheets: 1
    instrument_guidance: "score-author's choice — any instrument capable of reading workspace files and adapting its approach; instrument depends on the actual task being adapted"
    fallback_friendly: true
    purpose: "Read workspace state from previous stages and adapt behavior based on what exists — conditionally varying approach within the prompt based on workspace artifacts."
    artifacts: []
composes_with:
  - pattern: "Triage Gate"
    how: "Triage Gate classifies fan-out outputs into quality categories that Read-and-React sheets then detect and adapt their processing strategy around."
  - pattern: "Fragmentary Order (FRAGO)"
    how: "FRAGO writes correction documents into the workspace that Read-and-React sheets detect and incorporate, adjusting behavior based on the presence and content of the FRAGO."
  - pattern: "Dormancy Gate"
    how: "Dormancy Gate waits for external conditions; Read-and-React adapts behavior based on the workspace state that exists once conditions are met and the gate opens."
dependencies: {}
---

## Read-and-React

`Status: Working` · **Source:** Basketball read-and-react offense. **Forces:** Partial Failure + Information Asymmetry.

### Core Dynamic

Downstream stages read workspace state and adapt their behavior. Not conditional branching (which requires conductor support) but workspace-driven behavioral adaptation within a sheet's prompt.

### When to Use / When NOT to Use

Use when downstream behavior should adapt to upstream results. Not when the adaptation path is known upfront.

### Marianne Score Structure

```yaml
sheets:
  - name: work
    prompt: >
      Read previous outputs. Based on what you find:
      - If analysis-complete.yaml exists: proceed to synthesis.
      - If analysis-complete.yaml is missing: extend analysis first.
    capture_files: ["analysis-*.md", "analysis-complete.yaml"]
```

### Failure Mode

Agent ignores the workspace state and proceeds with default behavior. Validate that the expected adaptation actually occurred.

### Composes With

Triage Gate, FRAGO, Dormancy Gate

---
name: "Dormancy Gate"
scale: score-level
type: orchestration-pattern
status: working
forces:
  - "Finite Resources"
generators:
  - "Gate on Environmental Readiness"
problem: "External prerequisites are not immediately available, but work cannot safely proceed without them."
signals:
  - "downstream work depends on external system state"
  - "prerequisites will eventually be satisfied but are not immediate"
  - "need to wait and retry, not fail outright"
stages:
  - name: check-conditions
    sheets: 1
    instrument_guidance: "cli — lightweight condition testing via command execution; no LLM reasoning required"
    fallback_friendly: true
    purpose: "Verify that external conditions are satisfied by testing workspace state or running verification commands."
    artifacts: []
  - name: proceed
    sheets: 1
    instrument_guidance: "score-author's choice — instrument selection depends on the task being performed"
    fallback_friendly: true
    purpose: "Proceed with the actual work once external conditions are confirmed ready."
    artifacts: []
composes_with:
  - pattern: "Read-and-React"
    how: "Dormancy Gate pauses until conditions warrant re-evaluation, enabling Read-and-React to dynamically re-run the score."
  - pattern: "Shipyard Sequence"
    how: "Dormancy Gate ensures each shipyard phase waits for its external prerequisites before proceeding."
dependencies: {}
---

## Dormancy Gate

`Status: Working` · **Source:** Seed dormancy in botany. **Forces:** Finite Resources.

### Core Dynamic

A gate that waits for external conditions before proceeding. The gate checks workspace state — if conditions aren't met, the score self-chains and checks again. Unlike a validation (which fails the score), dormancy gates pause and retry.

### When to Use / When NOT to Use

Use when work depends on external conditions that will eventually be met. Not when conditions are already known.

### Marianne Score Structure

```yaml
sheets:
  - name: check-conditions
    instrument: cli
    validations:
      - type: command_succeeds
        command: "test -f {{ workspace }}/external-data-ready.flag"
  - name: proceed
    prompt: "Conditions met. Begin processing."
    capture_files: ["external-data/**"]
```

### Failure Mode

External condition never materializes. `max_chain_depth` provides a safety bound.

### Composes With

Read-and-React, Shipyard Sequence

---
name: "Reconnaissance Pull"
scale: score-level
type: orchestration-pattern
status: working
forces:
  - "Information Asymmetry"
generators:
  - "Accumulate Knowledge"
problem: "Planning without prior exploration risks misaligned approaches and wasted effort."
signals:
  - "task structure and complexity are unclear"
  - "initial exploration costs are low relative to execution"
  - "approach is not obvious from requirements alone"
config_features:
  - capture_files
stages:
  - name: recon
    sheets: 1
    instrument_guidance: "sonnet — balanced cost and capability; sufficient for landscape discovery without deep reasoning"
    fallback_friendly: true
    purpose: "Discover and document the landscape of the input: structure, complexity, and risks."
    artifacts: ["recon-report.md"]
  - name: plan
    sheets: 1
    instrument_guidance: "score-author's choice — planning complexity depends on task and landscape complexity; stronger instruments benefit from comprehensive recon"
    fallback_friendly: true
    purpose: "Analyze reconnaissance findings and synthesize a detailed execution plan."
    artifacts: ["execution-plan.md"]
  - name: execute
    sheets: 1
    instrument_guidance: "score-author's choice — execution capability must match task requirements; recon and plan inform instrument selection"
    fallback_friendly: false
    purpose: "Execute the work as specified in the execution plan."
    artifacts: []
composes_with:
  - pattern: "Mission Command"
    how: "Reconnaissance Pull provides landscape discovery before Mission Command agents begin execution within their intent envelope."
  - pattern: "Canary Probe"
    how: "Reconnaissance Pull informs Canary Probe's incremental exposure strategy by discovering the landscape before probing begins."
dependencies: {}
---

## Reconnaissance Pull

`Status: Working` · **Source:** Military reconnaissance doctrine. **Forces:** Information Asymmetry.

### Core Dynamic

A cheap, fast reconnaissance stage discovers the landscape before committing to a plan. The recon output is advisory — downstream stages read it and adapt. Different from Forward Observer (which compresses). Reconnaissance discovers.

### When to Use / When NOT to Use

Use when the approach isn't obvious and exploration is cheap. Not when the task is well-understood.

### Marianne Score Structure

```yaml
sheets:
  - name: recon
    instrument: sonnet
    prompt: "Survey the input. Write recon-report.md: structure, complexity, risks, recommended approach."
    validations:
      - type: file_exists
        path: "{{ workspace }}/recon-report.md"
  - name: plan
    prompt: "Read recon-report.md. Write execution plan."
    capture_files: ["recon-report.md"]
  - name: execute
    prompt: "Execute per plan."
    capture_files: ["execution-plan.md"]
```

### Failure Mode

Recon is too shallow to inform planning. Use a more capable instrument for recon if the domain is complex.

### Composes With

Mission Command, Canary Probe

---
name: "Fragmentary Order (FRAGO)"
scale: adaptation
type: orchestration-pattern
status: working
forces:
  - "Partial Failure"
generators: []
problem: "Plans become stale mid-execution when discovered conditions diverge from expectations but no mechanism exists for targeted correction without full replanning."
signals:
  - "earlier stages produced results that invalidate downstream assumptions"
  - "the plan is partially wrong but not wrong enough to discard"
  - "downstream agents need adjusted guidance, not a completely new plan"
  - "conditions discovered mid-execution were not anticipated by the original plan"
stages:
  - name: assess
    sheets: 1
    instrument_guidance: "score-author's choice — needs enough reasoning to compare actual outputs against the plan and identify meaningful deviations; instrument depends on domain complexity"
    fallback_friendly: true
    purpose: "Read outputs so far, identify deviations from the execution plan, and write frago.md with targeted corrections if needed."
    artifacts: ["frago.md"]
  - name: continue
    sheets: 1
    instrument_guidance: "score-author's choice — must be capable enough for the underlying task; the FRAGO adjustment doesn't change instrument requirements"
    fallback_friendly: true
    purpose: "Read frago.md if it exists and adjust execution approach per the corrections while continuing the original plan."
    artifacts: []
composes_with:
  - pattern: "Read-and-React"
    how: "Read-and-React provides the workspace-driven adaptation mechanism that the continue stage uses to detect and respond to the FRAGO correction document."
  - pattern: "Lines of Effort"
    how: "FRAGO provides mid-execution course corrections to individual lines of effort when they diverge from the convergence plan."
  - pattern: "Mission Command"
    how: "Mission Command defines the original intent envelope; FRAGO adjusts tactical guidance when execution conditions diverge from the original brief without overriding the mission's purpose or end state."
dependencies: {}
---

## Fragmentary Order (FRAGO)

`Status: Working` · **Source:** Military fragmentary orders. **Forces:** Partial Failure.

### Core Dynamic

Mid-execution course correction via cadenza injection. When earlier stages produce unexpected results, a FRAGO sheet writes a correction document that downstream stages read. Not replanning — targeted adjustments to the existing plan.

### When to Use / When NOT to Use

Use when plans need mid-execution adjustment based on discovered conditions. Not when the plan is too broken for incremental fixes.

### Marianne Score Structure

```yaml
sheets:
  - name: assess
    prompt: "Read outputs so far. Identify deviations from plan. Write frago.md if corrections needed."
    capture_files: ["execution-plan.md", "progress/**"]
  - name: continue
    prompt: "Read frago.md if it exists. Adjust approach per corrections."
    capture_files: ["frago.md", "execution-plan.md"]
```

### Failure Mode

FRAGO contradicts the original plan too severely. Downstream agents can't reconcile. Keep corrections incremental.

### Composes With

Read-and-React, Lines of Effort, Mission Command

---
name: "After-Action Review"
scale: iteration
type: orchestration-pattern
status: working
forces:
  - "Information Asymmetry"
  - "Partial Failure"
generators:
  - "Accumulate Knowledge"
  - "Exploit Failure as Signal"
problem: "Execution insights are lost between iterations because no systematic reflection captures what worked, what failed, and why."
signals:
  - "same mistakes happen repeatedly across iterations"
  - "execution insights disappear after completion"
  - "teams don't know what actually worked or why it worked"
  - "improvement recommendations don't reach subsequent iterations"
config_features:
  - "capture_files"
stages:
  - name: aar
    sheets: 1
    instrument_guidance: "sonnet or opus recommended — must synthesize multiple execution outputs, identify concrete deltas between intent and reality, extract actionable lessons with specific references; cheaper instruments risk the documented failure mode (generic platitudes without specific output references)"
    fallback_friendly: false
    purpose: "Analyze execution outcomes against original intent, identify concrete deltas, extract what to sustain and what to improve for next iteration."
    artifacts: ["aar.md"]
composes_with:
  - pattern: "Immune Cascade"
    how: "AAR analyzes which items graduated through Immune Cascade's tier gates and extracts lessons about gate criteria effectiveness for refinement."
  - pattern: "Cathedral Construction"
    how: "AAR captures lessons from each Cathedral Construction iteration and feeds improvements into the next cycle's prelude as accumulated knowledge."
  - pattern: "Back-Slopping (Learning Inheritance)"
    how: "AAR generates the aar.md artifact that Back-Slopping (Learning Inheritance) propagates forward as starter culture to seed the next iteration with learning inheritance."
dependencies: {}
---

## After-Action Review

`Status: Working` · **Source:** US Army AAR protocol. **Forces:** Information Asymmetry + Partial Failure.

### Core Dynamic

Dedicated review stage after execution. Not quality checking (that's validation). AAR asks: what was supposed to happen, what actually happened, why the difference, what to change. The AAR output feeds the next iteration's prelude.

### When to Use / When NOT to Use

Use after any significant execution to capture learning. Not for trivial tasks.

### Marianne Score Structure

```yaml
sheets:
  - name: aar
    prompt: >
      Read all execution outputs. Write aar.md:
      INTENDED: what the score was supposed to produce.
      ACTUAL: what was actually produced.
      DELTA: why the difference.
      SUSTAIN: what worked.
      IMPROVE: what to change next time.
    capture_files: ["**"]
    validations:
      - type: content_contains
        content: "SUSTAIN:"
      - type: content_contains
        content: "IMPROVE:"
```

### Failure Mode

AAR is generic platitudes. Validate specific references to actual outputs and concrete improvement recommendations.

### Composes With

Immune Cascade, Cathedral Construction, Back-Slopping (Learning Inheritance)

---
name: "Andon Cord"
scale: adaptation
type: orchestration-pattern
status: working
forces:
  - "Partial Failure"
  - "Information Asymmetry"
generators:
  - "Exploit Failure as Signal"
problem: "Validation failures are retried blindly without diagnosing root cause, wasting resources on repeated errors."
signals:
  - "validation failures repeat the same error across retries"
  - "failure output is informative but gets ignored"
  - "retry costs are high (~$1+ per attempt)"
  - "agent needs corrective guidance, not just another attempt"
stages:
  - name: generate
    sheets: 1
    instrument_guidance: "score-author's choice — must be capable enough for the implementation task; pattern focuses on failure handling workflow rather than generation instrument selection"
    fallback_friendly: true
    purpose: "Generate the initial implementation."
    artifacts: ["test-output.log"]
  - name: diagnose
    sheets: 1
    instrument_guidance: "capable instrument (sonnet or opus recommended) — diagnostic reasoning is load-bearing; failure mode explicitly mentions opus for triage to ensure accurate root cause analysis"
    fallback_friendly: false
    purpose: "Analyze failure output and identify root cause with concrete fix plan."
    artifacts: ["andon-diagnosis.md"]
  - name: regenerate
    sheets: 1
    instrument_guidance: "score-author's choice — same capability tier as generate stage; applies the identified fix rather than performing full regeneration"
    fallback_friendly: true
    purpose: "Apply the diagnosis to fix the identified issue without rewriting from scratch."
    artifacts: []
composes_with:
  - pattern: "Circuit Breaker"
    how: "Circuit Breaker monitors instrument-level failures across tasks; Andon Cord diagnoses task-level validation failures within a single workflow, operating at different failure scopes."
  - pattern: "Quorum Trigger"
    how: "Quorum Trigger activates Andon Cord when multiple validation failures reach threshold, preventing single-failure noise from triggering expensive diagnosis stages."
  - pattern: "Commissioning Cascade"
    how: "Commissioning Cascade verifies outputs at multiple quality gates; Andon Cord provides the diagnostic-and-fix mechanism when any commissioning tier fails validation."
dependencies: {}
---

## Andon Cord

`Status: Working` · **Source:** Toyota Production System stop-the-line, Expedition 1. **Scale:** adaptation. **Iteration:** 4. **Force:** Graceful Failure.

### Core Dynamic

Replaces blind retry with diagnostic intervention. On validation failure: detect → stop (don't retry blindly) → diagnose (dedicated diagnostic sheet reads failure output) → fix (inject diagnosis as cadenza) → resume (re-run with new context). Transforms failure response from stochastic retry to deterministic diagnosis.

**Relationship to self-healing:** Marianne's conductor-level self-healing feature implements a similar detect-diagnose-fix loop. Andon Cord is the score-level pattern — you compose it explicitly in your YAML. Self-healing is the conductor-level implementation that applies automatically. Both exist at different abstraction levels.

### When to Use / When NOT to Use

Use when failures are diagnostic (agent misunderstood the task, missed a constraint), when failure output contains enough information to diagnose root cause, or when retry cost justifies a diagnostic stage (~$1+ per attempt). Not when failures are stochastic (network timeouts — just retry), failure output is empty, or diagnosis cost exceeds a few blind retries.

### Marianne Score Structure

```yaml
sheets:
  - name: generate
    prompt: "Generate the REST API implementation."
    validations:
      - type: command_succeeds
        command: "cd {{ workspace }} && pytest -x 2>&1 | tee {{ workspace }}/test-output.log; exit ${PIPESTATUS[0]}"
  - name: diagnose
    prompt: |
      The previous stage failed validation. Read the failed output and test results.
      Write andon-diagnosis.md with:
      ROOT CAUSE: (what specifically went wrong)
      FIX PLAN: (concrete steps to fix)
    capture_files: ["**/*.py", "test-output.log"]
    validations:
      - type: content_contains
        content: "ROOT CAUSE:"
      - type: content_contains
        content: "FIX PLAN:"
  - name: regenerate
    prompt: "Read andon-diagnosis.md. Fix the identified issue. Do not rewrite from scratch."
    capture_files: ["andon-diagnosis.md", "**/*.py"]
    validations:
      - type: command_succeeds
        command: "cd {{ workspace }} && pytest -x"
```

### Failure Mode

Diagnosis is wrong — the root cause analysis misidentifies the problem, and the fix introduces new failures. Validate that the regenerated output passes the SAME validation that the original failed. If diagnosis consistently fails, fall back to a more capable instrument for the diagnostic sheet (Opus for triage, per CEGAR Loop strategy).

### Composes With

Circuit Breaker (andon for task failure, circuit breaker for instrument failure), Quorum Trigger (quorum triggers andon), Commissioning Cascade (andon at each commissioning tier)

---
name: "Circuit Breaker"
scale: adaptation
type: orchestration-pattern
status: working
forces:
  - "Accumulated Signal"
  - "Finite Resources"
generators:
  - "Threshold-Triggered Switch"
problem: "Long-running jobs fail catastrophically or waste resources when instruments become unavailable mid-execution."
signals:
  - "backend outages cause sudden job failures"
  - "primary instrument becomes unavailable mid-concert"
  - "self-chaining jobs lose progress when instruments fail"
  - "cost overruns from repeated retries on broken instruments"
stages:
  - name: check-circuit
    sheets: 1
    instrument_guidance: "cli — system introspection only; reads circuit-state.yaml to determine current breaker status (closed/open/half-open)"
    fallback_friendly: true
    purpose: "Read the persistent circuit state and report the current status."
    artifacts: []
  - name: health-probe
    sheets: 1
    instrument_guidance: "ollama — probes the primary instrument's health; if unavailable, the probe fails and triggers circuit opening"
    fallback_friendly: false
    purpose: "Probe the primary instrument's health; record latency and success/failure to guide circuit state transitions."
    artifacts: ["probe-result.yaml"]
  - name: route-work
    sheets: 1
    instrument_guidance: "score-author's choice — makes routing decisions between primary and fallback based on circuit state; needs logical capability"
    fallback_friendly: false
    purpose: "Read circuit state and probe results; route work to primary instrument (if closed and healthy) or fallback (if open or failed). Update circuit state with new failure counts and timestamps."
    artifacts: ["circuit-state.yaml"]
  - name: consolidate
    sheets: 1
    instrument_guidance: "score-author's choice — final assembly of outputs from whichever execution path succeeded; straightforward merging task"
    fallback_friendly: true
    purpose: "Merge results from primary or fallback execution paths into a unified output."
    artifacts: []
composes_with:
  - pattern: "Dead Letter Quarantine"
    how: "Dead Letter Quarantine receives items that fail both primary and fallback execution routes for manual inspection."
  - pattern: "Echelon Repair"
    how: "Circuit Breaker can gate escalation within echelon tiers; if a cheaper tier's primary instrument fails, escalate to the next tier instead of falling back."
  - pattern: "Speculative Hedge"
    how: "Speculative Hedge pre-executes with candidate instruments in parallel; Circuit Breaker routes work to the fastest/most reliable hedge when primary is unavailable."
config_features:
  - "self_chaining"
  - "inherit_workspace"
dependencies: {}
---

## Circuit Breaker

`Status: Working` · **Source:** Nygard's "Release It!" (2007), Netflix Hystrix, Expedition 5. **Scale:** adaptation. **Iteration:** 4. **Force:** Graceful Failure.

### Core Dynamic

After N instrument failures, STOP TRYING. Three states: Closed (normal — route to primary instrument), Open (all requests use fallback immediately — zero cost on broken instrument), Half-Open (one probe request — if it succeeds, close; if it fails, reopen). The critical distinction: instrument failure vs. task failure. A circuit breaker on "agent produced bad output" would shut down the pipeline. This is for infrastructure failures — backends crashing, APIs timing out, models OOM-ing.

**Stateful implementation:** The circuit state persists in `circuit-state.yaml` across self-chain iterations. Each execution reads the state, makes routing decisions, and updates the state. The self-chain carries the state forward via `inherit_workspace`.

### When to Use / When NOT to Use

Use for scores using unreliable instruments (external APIs, local models), long-running concerts where backends may degrade mid-execution, or self-chaining scores where instruments become unavailable. Not when failure is in the TASK (not the instrument), when only one instrument is available, or for short scores where manual intervention is faster.

### Marianne Score Structure

```yaml
sheets:
  - name: check-circuit
    instrument: cli
    validations:
      - type: command_succeeds
        command: "python3 -c \"import yaml,os; s=yaml.safe_load(open('{{ workspace }}/circuit-state.yaml')) if os.path.exists('{{ workspace }}/circuit-state.yaml') else {'state':'closed','failures':0}; print(f'Circuit: {s[\"state\"]}, failures: {s[\"failures\"]}')\""
  - name: health-probe
    instrument: ollama
    prompt: "Health check. Write probe-result.yaml: {status: ok|fail, latency_ms, error}."
    validations:
      - type: file_exists
        path: "{{ workspace }}/probe-result.yaml"
  - name: route-work
    prompt: >
      Read circuit-state.yaml and probe-result.yaml.
      If circuit CLOSED and probe OK: execute with primary instrument (ollama). Write to primary-output/.
      If circuit OPEN or probe FAIL: execute with fallback instrument (claude). Write to fallback-output/.
      Update circuit-state.yaml: {state, failures, last_check, last_transition}.
    capture_files: ["circuit-state.yaml", "probe-result.yaml"]
  - name: consolidate
    prompt: "Merge results from whichever path completed."
    capture_files: ["primary-output/**", "fallback-output/**"]
on_success:
  action: self
  inherit_workspace: true
  max_chain_depth: 20
```

### Failure Mode

Circuit opens permanently because the health probe itself is too sensitive (marks transient failures as outages). Use a failure count threshold (e.g., 3 consecutive failures) before opening. If the fallback instrument also fails, the circuit breaker can't help — escalate to Dead Letter Quarantine.

### Composes With

Dead Letter Quarantine (circuit-tripped items go to quarantine), Echelon Repair (circuit breaker per echelon), Speculative Hedge (backup instrument IS the hedge)

## Instrument Strategy Patterns (v4)

---
name: "Echelon Repair"
scale: instrument-strategy
type: orchestration-pattern
status: working
proof_score: "echelon-repair.yaml"
forces:
  - "Instrument-Task Fit"
  - "Finite Resources"
generators:
  - "Match Instrument to Grain"
problem: "Expensive instruments waste resources on work that cheaper instruments could handle."
signals:
  - "work items vary wildly in difficulty"
  - "expensive instrument is wasted on trivial tasks"
  - "costs are high but most work is simple"
  - "need to triage before processing"
stages:
  - name: classify
    sheets: 1
    instrument_guidance: "haiku — fast, cheap classification; capability is sufficient for difficulty labeling"
    fallback_friendly: true
    purpose: "Read each work item and classify difficulty as E1/E2/E3."
    artifacts: ["echelon-manifest.yaml"]
  - name: e1-repair
    sheets: 1
    instrument_guidance: "haiku — simple items; speed and cost matter more than depth"
    fallback_friendly: true
    purpose: "Process items classified as E1 (simple)."
    artifacts: []
  - name: e2-repair
    sheets: 1
    instrument_guidance: "sonnet — moderate items; needs more reasoning than haiku provides"
    fallback_friendly: false
    purpose: "Process items classified as E2 (moderate complexity)."
    artifacts: []
  - name: e3-repair
    sheets: 1
    instrument_guidance: "opus — complex items; full reasoning capability required"
    fallback_friendly: false
    purpose: "Process items classified as E3 (high complexity)."
    artifacts: []
composes_with:
  - pattern: "Commissioning Cascade"
    how: "Commissioning Cascade verifies the output quality of each echelon tier."
  - pattern: "Fermentation Relay"
    how: "Fermentation Relay provides the instrument tier escalation that Echelon Repair's classification routes into."
  - pattern: "Screening Cascade"
    how: "Screening Cascade pre-filters items before echelon classification to remove obvious non-candidates."
  - pattern: "Circuit Breaker"
    how: "Circuit Breaker halts escalation to expensive echelons when failure rates spike."
dependencies: {}
---

## Echelon Repair

`Status: Working` · **Source:** Military echelon maintenance. **Forces:** Instrument-Task Fit + Finite Resources.

### Core Dynamic

Graduated instrument assignment. Easy work goes to cheap/fast instruments. Hard work escalates to expensive/capable instruments. The classification stage determines difficulty BEFORE assignment.

### When to Use / When NOT to Use

Use when work items vary in difficulty and instruments vary in cost/capability. Not when all work is equally complex.

### Marianne Score Structure

```yaml
sheets:
  - name: classify
    instrument: haiku
    prompt: "Read each item. Classify difficulty: E1 (simple), E2 (moderate), E3 (complex). Write echelon-manifest.yaml."
    validations:
      - type: command_succeeds
        command: "python3 -c \"import yaml; m=yaml.safe_load(open('{{ workspace }}/echelon-manifest.yaml')); assert all(e['echelon'] in ['E1','E2','E3'] for e in m)\""
  - name: e1-repair
    instrument: haiku
    prompt: "Process E1 items from echelon-manifest.yaml."
    capture_files: ["echelon-manifest.yaml"]
  - name: e2-repair
    instrument: sonnet
    prompt: "Process E2 items."
    capture_files: ["echelon-manifest.yaml"]
  - name: e3-repair
    instrument: opus
    prompt: "Process E3 items."
    capture_files: ["echelon-manifest.yaml"]
```

### Failure Mode

Misclassification: E3 items assigned to E1. Validate E1 output quality; escalate failures to E2.

### Composes With

Commissioning Cascade, Fermentation Relay, Screening Cascade, Circuit Breaker

---
name: "Fermentation Relay"
scale: instrument-strategy
type: orchestration-pattern
status: working
forces:
  - "Instrument-Task Fit"
generators:
  - "Match Instrument to Grain"
problem: "Expensive instruments waste resources fixing quality issues that cheap instruments created during initial processing."
signals:
  - "cheap instruments produce output too noisy for expensive stages to use directly"
  - "expensive instruments waste budget on noise filtering instead of core work"
  - "early outputs require multiple refinement steps before quality is acceptable"
  - "no single instrument choice works well across all pipeline stages"
stages:
  - name: extract
    sheets: 1
    instrument_guidance: "haiku — fast, cheap initial processing; sufficient for raw information extraction from input"
    fallback_friendly: true
    purpose: "Extract raw information from input."
    artifacts: ["extraction.md"]
  - name: refine
    sheets: 1
    instrument_guidance: "sonnet — moderate reasoning to resolve ambiguities from raw extraction; capability tier between haiku and opus"
    fallback_friendly: false
    purpose: "Refine extraction by resolving ambiguities and inconsistencies."
    artifacts: ["refined.md"]
  - name: polish
    sheets: 1
    instrument_guidance: "opus — highest reasoning capability for final quality pass; capable of catching subtle issues the refinement stage may miss"
    fallback_friendly: false
    purpose: "Perform final quality pass and produce polished output."
    artifacts: []
composes_with:
  - pattern: "Echelon Repair"
    how: "Fermentation Relay defines the multi-tier instrument cost progression that Echelon Repair routes classified difficult items through for remediation."
  - pattern: "Succession Pipeline"
    how: "Both use sequential refinement stages; Fermentation Relay optimizes for cost-graduated instruments while Succession Pipeline emphasizes early defect detection."
  - pattern: "Screening Cascade"
    how: "Screening Cascade pre-filters items before input to Fermentation Relay's pipeline, improving extraction quality and reducing noise for refinement stages."
dependencies: {}
---

## Fermentation Relay

`Status: Working` · **Source:** Fermentation microbiology. **Forces:** Instrument-Task Fit.

### Core Dynamic

Cheap instruments do initial processing; expensive instruments refine. The pipeline is fixed in YAML. "Substrate-driven" refers to how you design the gate between stages, not runtime switching.

### When to Use / When NOT to Use

Use when early stages benefit from fast/cheap processing and later stages need precision. Not when all stages need the same capability.

### Marianne Score Structure

```yaml
sheets:
  - name: extract
    instrument: haiku
    prompt: "Extract raw information. Write extraction.md."
    validations:
      - type: file_exists
        path: "{{ workspace }}/extraction.md"
  - name: refine
    instrument: sonnet
    prompt: "Refine extraction. Resolve ambiguities."
    capture_files: ["extraction.md"]
  - name: polish
    instrument: opus
    prompt: "Final quality pass. Produce polished output."
    capture_files: ["refined.md"]
```

### Failure Mode

Early cheap stages produce such poor output that expensive stages spend all their budget fixing garbage. Validate intermediate quality.

### Composes With

Echelon Repair, Succession Pipeline, Screening Cascade

---
name: "Screening Cascade"
scale: instrument-strategy
type: orchestration-pattern
status: working
forces:
  - "Instrument-Task Fit"
  - "Finite Resources"
generators:
  - "Graduate & Filter"
  - "Match Instrument to Grain"
problem: "Difficulty emerges during processing; fixed upfront instruments waste expensive resources on simple work or fail on complex work."
signals:
  - "work items vary in difficulty but this only becomes clear during processing"
  - "cheap instruments can screen routine items but some need escalation to stronger capabilities"
  - "costs are high because you're using expensive instruments for work that doesn't warrant them"
  - "difficult work emerges during execution, not from upfront inspection"
stages:
  - name: screen-1
    sheets: 1
    instrument_guidance: "haiku — fast, cost-effective initial screening; sufficient to identify items requiring stronger instruments"
    fallback_friendly: true
    purpose: "Process all items with cheap instrument; mark uncertain items for escalation."
    artifacts: ["screen-1-results.yaml"]
  - name: screen-2
    sheets: 1
    instrument_guidance: "sonnet — stronger reasoning than haiku; handles items that exceed haiku's capability but don't require opus"
    fallback_friendly: false
    purpose: "Screen items escalated from stage 1 with improved capability; further escalate remaining uncertain items."
    artifacts: ["screen-2-results.yaml"]
  - name: screen-3
    sheets: 1
    instrument_guidance: "opus — full reasoning capability for items that exceeded both cheaper instruments; required for the most difficult work"
    fallback_friendly: false
    purpose: "Process items escalated from stage 2 with maximum reasoning capability."
    artifacts: []
composes_with:
  - pattern: "Echelon Repair"
    how: "Screening Cascade discovers difficulty progressively through escalating screens; Echelon Repair pre-classifies items upfront, providing alternative approaches to matching work with instruments."
  - pattern: "Immune Cascade"
    how: "Screening Cascade escalates through capability tiers; Immune Cascade provides fallback processing when escalation fails, with items flowing to Immune Cascade's recovery paths."
  - pattern: "Dead Letter Quarantine"
    how: "Dead Letter Quarantine captures items that exceed all screening stages' capabilities, isolating unprocessable work from the main pipeline."
dependencies: {}
---

## Screening Cascade

`Status: Working` · **Source:** Medical screening. **Forces:** Instrument-Task Fit + Finite Resources.

### Core Dynamic

Batch processing with escalating instruments at each stage. Stage 1 screens with cheap instrument, passes ambiguous cases to Stage 2 with more capable instrument, and so on. Different from Echelon Repair (which classifies upfront): Screening Cascade discovers difficulty through progressive screening.

### When to Use / When NOT to Use

Use when difficulty isn't classifiable upfront but emerges during processing. Not when all items need the same treatment.

### Marianne Score Structure

```yaml
sheets:
  - name: screen-1
    instrument: haiku
    prompt: "Process all items. Mark items you're uncertain about as ESCALATE. Write screen-1-results.yaml."
    validations:
      - type: file_exists
        path: "{{ workspace }}/screen-1-results.yaml"
  - name: screen-2
    instrument: sonnet
    prompt: "Process ESCALATE items from screen-1. Mark remaining uncertain as ESCALATE-2."
    capture_files: ["screen-1-results.yaml"]
  - name: screen-3
    instrument: opus
    prompt: "Process ESCALATE-2 items."
    capture_files: ["screen-2-results.yaml"]
```

### Failure Mode

Stage 1 escalates everything (no screening value). Validate escalation rates: if >50% escalate, the screening threshold is too conservative.

### Composes With

Echelon Repair, Immune Cascade, Dead Letter Quarantine

---
name: "Vickrey Auction"
scale: instrument-strategy
type: orchestration-pattern
status: approximation
forces:
  - "Instrument-Task Fit"
generators:
  - "Match Instrument to Grain"
problem: "Selecting an instrument without evidence wastes resources or produces inferior results when multiple candidates are viable."
signals:
  - "multiple instruments are available and it's unclear which performs best"
  - "instrument choice is based on guesswork, not evidence"
  - "cost or quality varies significantly across instruments for the same task"
approximation_note: "The YAML covers competitive probing and evaluation but not dynamic instrument selection for the full run. Using the winning instrument requires a two-score concert or human-in-the-loop step, which cannot be expressed in a single score."
stages:
  - name: probe-haiku
    sheets: 1
    instrument_guidance: "haiku — one of the candidate instruments being competitively evaluated"
    fallback_friendly: false
    purpose: "Process a sample item using haiku to produce a probe output for comparison."
    artifacts: ["probe-haiku.md"]
  - name: probe-sonnet
    sheets: 1
    instrument_guidance: "sonnet — one of the candidate instruments being competitively evaluated"
    fallback_friendly: false
    purpose: "Process the same sample item using sonnet to produce a probe output for comparison."
    artifacts: ["probe-sonnet.md"]
  - name: evaluate
    sheets: 1
    instrument_guidance: "score-author's choice — needs judgment capability to compare outputs and recommend an instrument; sonnet or opus recommended"
    fallback_friendly: true
    purpose: "Compare probe outputs and write an instrument recommendation with rationale."
    artifacts: ["instrument-recommendation.yaml"]
composes_with:
  - pattern: "Echelon Repair"
    how: "Vickrey Auction's probe results inform which instrument tiers to assign in Echelon Repair's classification-based routing."
  - pattern: "Canary Probe"
    how: "Canary Probe tests pipeline viability on a data subset; Vickrey Auction tests instrument fitness on the same task, combining to validate both pipeline and instrument choice before full commitment."
dependencies: {}
---

## Vickrey Auction

`Status: Working (two-run approximation)` · **Source:** Vickrey auction theory. **Forces:** Instrument-Task Fit.

### Core Dynamic

Competitive probing: run the same task on multiple instruments, evaluate which performed best, use that instrument for the full run. The probing informs the NEXT run, not this one — dynamic instrument selection requires either a two-score concert or human-in-the-loop step.

### When to Use / When NOT to Use

Use when multiple instruments are available and it's unclear which performs best. Not when one instrument is clearly superior.

### Marianne Score Structure

```yaml
sheets:
  - name: probe-haiku
    instrument: haiku
    prompt: "Process the sample item. Write probe-haiku.md."
  - name: probe-sonnet
    instrument: sonnet
    prompt: "Process the same sample item. Write probe-sonnet.md."
  - name: evaluate
    prompt: "Compare probe outputs. Write instrument-recommendation.yaml: {winner, rationale}."
    capture_files: ["probe-haiku.md", "probe-sonnet.md"]
```

### Failure Mode

Probe item isn't representative of the full workload. Use multiple probe items.

### Composes With

Echelon Repair, Canary Probe

---
name: "Composting Cascade"
scale: score-level
type: orchestration-pattern
status: working
forces:
  - "Accumulated Signal"
  - "Instrument-Task Fit"
generators:
  - "Threshold-Triggered Switch"
  - "Match Instrument to Grain"
problem: "Phase transitions in iterative work need measurable readiness signals rather than time-based or manual progression decisions."
signals:
  - "phase transitions are time-based or manual, not metrics-driven"
  - "unclear when simple work is complete and should escalate to complex restructuring"
  - "churn rates don't drive phase changes, even when they indicate ongoing work"
  - "workspace readiness isn't observable"
stages:
  - name: simple-work
    sheets: 1
    instrument_guidance: "score-author's choice — simple cleanup (renaming, type hints, extraction) is cost-sensitive but needs reasoning; haiku recommended"
    fallback_friendly: true
    purpose: "Execute simple cleanup tasks (renaming, type hints, function extraction)."
    artifacts: []
  - name: temperature-check
    sheets: 1
    instrument_guidance: "cli — shell script measuring workspace metrics (type coverage, test pass rate, etc.); must support --threshold argument"
    fallback_friendly: false
    purpose: "Check if workspace metrics meet threshold for phase transition."
    artifacts: []
  - name: complex-work
    sheets: 1
    instrument_guidance: "opus — complex restructuring (abstractions, algorithm rewrites) requires full reasoning capability; haiku or sonnet insufficient"
    fallback_friendly: false
    purpose: "Execute complex restructuring (abstractions, algorithm rewrites)."
    artifacts: []
  - name: cooling-check
    sheets: 1
    instrument_guidance: "cli — shell script measuring change rate (code churn, diff magnitude); must support --max-churn argument"
    fallback_friendly: false
    purpose: "Check if work is cooling (change rate below exhaustion threshold)."
    artifacts: []
  - name: maturation
    sheets: 1
    instrument_guidance: "haiku — documentation writing is cost-sensitive; cheaper instrument sufficient for guides and changelogs"
    fallback_friendly: true
    purpose: "Write documentation (migration guide, changelog)."
    artifacts: ["migration-guide.md", "changelog.md"]
composes_with:
  - pattern: "The Tool Chain"
    how: "Composting Cascade uses CLI instruments (Tool Chain) as workspace thermometers to measure readiness for phase transitions."
  - pattern: "Succession Pipeline"
    how: "Composting Cascade IS succession with metric-driven phase gates rather than time-based progression."
  - pattern: "Echelon Repair"
    how: "Composting Cascade escalates instruments per phase; complex-work uses opus while simple-work and maturation use cheaper instruments."
script_dependencies:
  - "temperature.py"
  - "exhaustion.py"
dependencies: {}
---

## Composting Cascade

`Status: Working` · **Source:** Four-phase composting microbiology, Expedition 2. **Scale:** score-level + instrument strategy. **Iteration:** 4. **Force:** Threshold Accumulation.

### Core Dynamic

The work's own output drives phase transitions. CLI instruments measure workspace state ("temperature") and threshold crossings trigger phase changes. The agents don't know they're transitioning — the thermometer knows. CLI instruments are in the control loop; AI instruments are the workers.

**"Temperature" defined:** Workspace metrics that indicate readiness for the next phase. Examples: type coverage percentage (for refactoring), test pass rate (for code generation), function count per file (for extraction work). The metric must be measurable by a CLI script and meaningfully indicate phase readiness.

**Script dependencies:** `temperature.py` and `exhaustion.py` are user-supplied. Interface contract: `temperature.py --threshold N` exits 0 if temperature meets threshold, exits 1 otherwise. `exhaustion.py --max-churn N` exits 0 if change rate is below threshold (work is cooling), exits 1 otherwise.

### When to Use / When NOT to Use

Use for multi-phase projects where work nature should change based on measurable workspace state, codebase refactoring where simple cleanup enables complex restructuring, or documentation campaigns where raw generation enables consolidation. Not when workspace metrics don't reflect work state, phase transitions need human judgment, or the work is single-phase.

### Marianne Score Structure

```yaml
sheets:
  - name: simple-work
    prompt: "Execute simple cleanup tasks. Rename variables, add type hints, extract functions."
  - name: temperature-check
    instrument: cli
    validations:
      - type: command_succeeds
        command: "python3 {{ workspace }}/temperature.py --threshold 60"
  - name: complex-work
    instrument: opus
    prompt: "Execute complex restructuring. Introduce abstractions, rewrite algorithms."
    capture_files: ["temperature-report.yaml"]
  - name: cooling-check
    instrument: cli
    validations:
      - type: command_succeeds
        command: "python3 {{ workspace }}/exhaustion.py --max-churn 5"
  - name: maturation
    instrument: haiku
    prompt: "Write documentation, migration guide, changelog."
```

### Failure Mode

Temperature metric doesn't correlate with actual readiness — complex-work fires too early and fails because the codebase isn't ready. Calibrate thresholds empirically: run the pipeline once, observe when complex-work succeeds, set the threshold there. If temperature never rises (simple-work doesn't change the measured metric), the cascade stalls at the temperature check.

### Composes With

The Tool Chain (CLI instruments as thermometers), Succession Pipeline (composting IS succession with metric-driven gates), Echelon Repair (instrument escalation per phase)

## Iteration Patterns (v4)

---
name: "CDCL Search"
scale: iteration
type: orchestration-pattern
status: working
forces:
  - "Partial Failure"
  - "Information Asymmetry"
generators:
  - "Accumulate Knowledge"
  - "Exploit Failure as Signal"
problem: "Iterative processes repeat the same failures because no mechanism captures and propagates failure patterns as constraints."
signals:
  - "same failures occur across retry attempts"
  - "retries don't help because nothing is learned"
  - "failures contain diagnostic information that could prevent recurrence"
  - "need to avoid known bad paths in subsequent iterations"
config_features:
  - "self_chaining"
  - "inherit_workspace"
stages:
  - name: attempt
    sheets: 1
    instrument_guidance: "score-author's choice — instrument capability must match the task being attempted; learned clauses guide behavior but don't reduce the task's inherent capability requirements"
    fallback_friendly: false
    purpose: "Attempt the task while avoiding failure patterns documented in learned-clauses.yaml from previous iterations."
    artifacts: []
  - name: analyze-failure
    sheets: 1
    instrument_guidance: "sonnet or opus recommended — requires strong reasoning to extract generalizable failure patterns; weak instruments produce clauses that are too specific (don't generalize) or too broad (over-constrain)"
    fallback_friendly: false
    purpose: "Extract the root cause of failure and append it as a constraint to learned-clauses.yaml to guide future attempts."
    artifacts: ["learned-clauses.yaml"]
composes_with:
  - pattern: "Back-Slopping (Learning Inheritance)"
    how: "Back-Slopping (Learning Inheritance) provides the learning inheritance mechanism; CDCL Search uses it to accumulate and forward learned failure clauses across self-chaining iterations."
  - pattern: "After-Action Review"
    how: "After-Action Review extracts lessons post-execution for human learning; CDCL Search's analyze-failure stage performs similar extraction inline for machine learning between iterations."
  - pattern: "CEGAR Loop"
    how: "Both are iterative constraint refinement patterns — CEGAR Loop refines abstractions when verification fails, CDCL Search refines the search space by adding failure-derived clauses; compose by using CDCL for failure learning within CEGAR's refinement loop."
dependencies: {}
---

## CDCL Search

`Status: Working` · **Source:** Conflict-driven clause learning (SAT solving). **Forces:** Partial Failure + Information Asymmetry.

### Core Dynamic

When a branch fails, extract WHY it failed and add the failure reason as a new constraint. The constraint prevents the same failure pattern in subsequent iterations. Learning from failure, not just retrying.

### When to Use / When NOT to Use

Use when failures are informative and recurring patterns are likely. Not when failures are random.

### Marianne Score Structure

```yaml
sheets:
  - name: attempt
    prompt: "Read learned-clauses.yaml. Attempt the task avoiding known failure patterns."
    capture_files: ["learned-clauses.yaml"]
  - name: analyze-failure
    prompt: "If attempt failed, extract failure reason. Append to learned-clauses.yaml."
    validations:
      - type: command_succeeds
        command: "python3 -c \"import yaml; c=yaml.safe_load(open('{{ workspace }}/learned-clauses.yaml')); print(f'{len(c)} clauses learned')\""
on_success:
  action: self
  inherit_workspace: true
  max_chain_depth: 10
```

### Failure Mode

Learned clauses are too specific (don't generalize) or too broad (over-constrain). Validate clause quality.

### Composes With

Back-Slopping (Learning Inheritance), After-Action Review, CEGAR Loop

---
name: "Fixed-Point Iteration"
scale: iteration
type: orchestration-pattern
status: working
forces:
  - "Convergence Imperative"
generators:
  - "Measure Convergence Character"
problem: "Iterative refinement requires explicit convergence detection to avoid wasting iterations."
signals:
  - "repeated application produces improvements but stopping criterion is unclear"
  - "iterations are expensive and need measurable termination beyond fixed counts"
  - "output stabilizes after refinement but manual convergence checking is tedious"
config_features:
  - "self_chaining"
stages:
  - name: iterate
    sheets: 1
    instrument_guidance: "score-author's choice — the improvement task itself determines required instrument capability; Fixed-Point Iteration prescribes no specific tier"
    fallback_friendly: true
    purpose: "Read the previous iteration's output and improve it."
    artifacts:
      - "output.md"
  - name: convergence-check
    sheets: 1
    instrument_guidance: "cli instrument is required — the convergence validation uses actual shell commands (diff) to measure iteration deltas"
    fallback_friendly: false
    purpose: "Check if output has converged by comparing current iteration to previous."
    artifacts: []
composes_with:
  - pattern: "CDCL Search"
    how: "CDCL Search instantiates fixed-point iteration as a SAT solver, iteratively refining clause sets toward satisfiability."
  - pattern: "Cathedral Construction"
    how: "Cathedral Construction applies fixed-point iteration to progressively refine and layer architectural components."
  - pattern: "Memoization Cache"
    how: "Memoization Cache optimizes fixed-point iteration by caching intermediate results across refinement cycles."
dependencies: {}
---

## Fixed-Point Iteration

`Status: Working` · **Source:** Numerical analysis, compiler dataflow. **Forces:** Convergence Imperative.

### Core Dynamic

Repeat the same operation until the output stops changing. Convergence is structural: diff the output of iteration N against iteration N-1. When the diff is empty (or below threshold), stop.

### When to Use / When NOT to Use

Use when the task naturally converges (each pass finds fewer issues). Not when convergence isn't guaranteed.

### Marianne Score Structure

```yaml
sheets:
  - name: iterate
    prompt: "Read previous output. Improve. Write output."
    capture_files: ["output.md"]
  - name: convergence-check
    instrument: cli
    validations:
      - type: command_succeeds
        command: "diff {{ workspace }}/output-prev.md {{ workspace }}/output.md | wc -l | xargs test 5 -gt"
on_success:
  action: self
  inherit_workspace: true
  max_chain_depth: 10
```

### Failure Mode

Never converges. `max_chain_depth` provides the safety bound.

### Composes With

CDCL Search, Cathedral Construction, Memoization Cache

---
name: "Cathedral Construction"
scale: iteration
type: orchestration-pattern
status: working
forces:
  - "Convergence Imperative"
  - "Finite Resources"
generators:
  - "Accumulate Knowledge"
problem: "Large artifacts cannot be produced in a single pass and require iterative construction toward a known target."
signals:
  - "artifact is too large to complete in one pass"
  - "work must be built incrementally toward a target"
  - "each iteration adds structural elements"
  - "need to track progress toward a known endpoint"
config_features:
  - "self_chaining"
stages:
  - name: plan-iteration
    sheets: 1
    instrument_guidance: "score-author's choice — planning benefits from strong reasoning (sonnet/opus recommended), but the iteration cycle provides correction opportunities so mid-tier instruments are viable"
    fallback_friendly: true
    purpose: "Read current state and plan what to add this iteration."
    artifacts: []
  - name: build
    sheets: 1
    instrument_guidance: "score-author's choice — depends entirely on what is being built (code, documentation, analysis); match instrument capability to the construction task complexity"
    fallback_friendly: true
    purpose: "Execute the plan and add to the cathedral."
    artifacts: ["cathedral/**"]
  - name: inspect
    sheets: 1
    instrument_guidance: "score-author's choice — review and critique work; sonnet-level reasoning typically sufficient since this is evaluation rather than primary construction"
    fallback_friendly: true
    purpose: "Review what was built and write inspection report."
    artifacts: ["inspection-report.md"]
composes_with:
  - pattern: "After-Action Review"
    how: "After-Action Review extracts lessons from the iteration history that Cathedral Construction accumulates, turning execution record into doctrine."
  - pattern: "Back-Slopping (Learning Inheritance)"
    how: "Back-Slopping (Learning Inheritance) carries forward patterns and learnings from previous iterations; Cathedral Construction's inherit_workspace provides the substrate for this knowledge transfer."
  - pattern: "Memoization Cache"
    how: "Memoization Cache stores previously-built components to avoid rebuilding; Cathedral Construction's incremental additions benefit from cached artifacts across iterations."
dependencies: {}
---

## Cathedral Construction

`Status: Working` · **Source:** Medieval cathedral building. **Forces:** Convergence Imperative + Finite Resources.

### Core Dynamic

Long-running iterative refinement where each iteration adds structural elements. Different from Fixed-Point (which converges to stability). Cathedral Construction builds toward a known target through incremental addition.

### When to Use / When NOT to Use

Use for large artifacts that can't be produced in one pass. Not when the work is convergent (use Fixed-Point).

### Marianne Score Structure

```yaml
sheets:
  - name: plan-iteration
    prompt: "Read current state. Plan what to add this iteration."
    capture_files: ["cathedral/**"]
  - name: build
    prompt: "Execute the plan. Add to the cathedral."
  - name: inspect
    prompt: "Review what was built. Write inspection-report.md."
on_success:
  action: self
  inherit_workspace: true
  max_chain_depth: 20
```

### Failure Mode

Each iteration adds but never integrates. Include integration checks in the inspection stage.

### Composes With

After-Action Review, Back-Slopping (Learning Inheritance), Memoization Cache

---
name: "Rehearsal Spotlight"
scale: iteration
type: orchestration-pattern
status: working
forces:
  - "Convergence Imperative"
  - "Finite Resources"
generators:
  - "Measure Convergence Character"
problem: "Iteration is expensive; reworking entire outputs wastes resources when only parts need refinement."
signals:
  - "iteration cycles are expensive"
  - "only specific sections need rework"
  - "most output is good but a few parts are weak"
  - "need to focus rework effort on problem areas"
fan_out:
  rehearse: 3
config_features:
  - "self_chaining"
  - "fan_out"
  - "capture_files"
script_dependencies:
  - "check_quality.py"
stages:
  - name: evaluate
    sheets: 1
    instrument_guidance: "score-author's choice — must reason about section quality; sonnet or opus recommended"
    fallback_friendly: true
    purpose: "Read output, score each section for quality, and identify targets for rework."
    artifacts: ["spotlight-targets.yaml"]
  - name: rehearse
    sheets: "fan_out(3)"
    instrument_guidance: "score-author's choice — must match the task being reworked (code, prose, analysis, etc.); capability is load-bearing for quality"
    fallback_friendly: false
    purpose: "Rework the targeted weak sections based on evaluation feedback."
    artifacts: []
  - name: check-done
    sheets: 1
    instrument_guidance: "cli — executes shell-based quality validation checks"
    fallback_friendly: false
    purpose: "Verify that reworked sections meet quality threshold; trigger self-chain if quality is insufficient."
    artifacts: []
composes_with:
  - pattern: "Echelon Repair"
    how: "Echelon Repair allocates effort by difficulty tier; Rehearsal Spotlight focuses rework effort on specific weak sections within one score iteration."
  - pattern: "Soil Maturity Index"
    how: "Soil Maturity Index measures convergence readiness of context; Rehearsal Spotlight applies convergence measurement to identify which sections need another rehearsal."
  - pattern: "CEGAR Loop"
    how: "CEGAR Loop iteratively refines through abstraction phases; Rehearsal Spotlight structures the refinement cycle to rework only sections that failed the previous quality check."
dependencies: {}
---

## Rehearsal Spotlight

`Status: Working` · **Source:** Theater rehearsal. **Forces:** Convergence Imperative + Finite Resources.

### Core Dynamic

After each iteration, identify the weakest sections and re-run ONLY those. Focuses expensive iteration on the parts that need it most.

### When to Use / When NOT to Use

Use when iteration is expensive and only parts of the output need rework. Not when the whole output needs rework each time.

### Marianne Score Structure

```yaml
sheets:
  - name: evaluate
    prompt: "Read output. Score each section. Write spotlight-targets.yaml: sections needing rework."
    capture_files: ["output/**"]
  - name: rehearse
    instances: 3
    prompt: "Rework the targeted section. Write improved version."
    capture_files: ["spotlight-targets.yaml", "output/**"]
  - name: check-done
    instrument: cli
    validations:
      - type: command_succeeds
        command: "python3 {{ workspace }}/check_quality.py --min-score 8"
on_success:
  action: self
  inherit_workspace: true
  max_chain_depth: 5
```

### Failure Mode

Spotlight always targets the same sections. Track which sections have been rehearsed and escalate persistent weaknesses.

### Composes With

Echelon Repair, Soil Maturity Index, CEGAR Loop

---
name: "Soil Maturity Index"
scale: iteration
type: orchestration-pattern
status: working
forces:
  - "Convergence Imperative"
generators:
  - "Measure Convergence Character"
problem: "Iterative processes lack domain-specific termination conditions beyond structural equality."
signals:
  - "iterative improvement plateaus on structural metrics but output lacks qualitative maturity"
  - "need to distinguish real convergence from mere structural stability"
  - "process converges structurally but hasn't achieved expected coherence or readiness"
  - "domain-specific maturity assessment required before proceeding to next phase"
stages:
  - name: iterate
    sheets: 1
    instrument_guidance: "score-author's choice — any instrument capable of reading and improving content based on domain-specific maturity criteria"
    fallback_friendly: true
    purpose: "Read the output and refine it based on domain-specific maturity criteria, iteratively improving toward qualitative convergence."
    artifacts: ["output.md"]
  - name: maturity-check
    sheets: 1
    instrument_guidance: "cli — executes the maturity assessment script to determine if output has reached target maturity state"
    fallback_friendly: false
    purpose: "Execute the maturity assessor script to determine if output has achieved desired maturity; exit code controls self-chaining termination."
    artifacts: []
composes_with:
  - pattern: "Fixed-Point Iteration"
    how: "Soil Maturity Index provides domain-specific convergence detection where Fixed-Point Iteration uses only structural no-change metrics."
  - pattern: "Back-Slopping (Learning Inheritance)"
    how: "Back-Slopping (Learning Inheritance) extracts learnings from iterations; Soil Maturity Index determines when iterations have produced sufficient signal for learning."
  - pattern: "Delphi Convergence"
    how: "Delphi Convergence measures consensus across independent attempts; Soil Maturity Index assesses convergence within a single iterative stream."
script_dependencies:
  - "maturity_assessor.py"
config_features:
  - "self_chaining"
dependencies: {}
---

## Soil Maturity Index

`Status: Working` · **Source:** Soil science maturity metrics. **Forces:** Convergence Imperative.

### Core Dynamic

Domain-specific termination condition for iterative processes. Instead of "nothing changed" (Fixed-Point) or "all sections pass" (Rehearsal Spotlight), the maturity index measures a qualitative shift — the output has changed CHARACTER, not just improved. A script-driven exit code determines termination.

### When to Use / When NOT to Use

Use when convergence is qualitative (the writing style matured, the architecture became cohesive). Not when convergence is structural.

### Marianne Score Structure

```yaml
sheets:
  - name: iterate
    prompt: "Read output. Improve based on maturity criteria."
    capture_files: ["output/**"]
  - name: maturity-check
    instrument: cli
    validations:
      - type: command_succeeds
        command: "python3 {{ workspace }}/maturity_assessor.py --output {{ workspace }}/output.md"
on_success:
  action: self
  inherit_workspace: true
  max_chain_depth: 10
```

### Failure Mode

Maturity metric doesn't capture the intended qualitative shift. Iterate on the assessor, not just the output.

### Composes With

Fixed-Point Iteration, Back-Slopping (Learning Inheritance), Delphi Convergence

---
name: "Delphi Convergence"
scale: iteration
type: orchestration-pattern
status: working
forces:
  - "Convergence Imperative"
  - "Information Asymmetry"
generators:
  - "Measure Convergence Character"
problem: "Multiple independent agents must converge without anchoring on early opinions."
signals:
  - "expert opinions vary widely and need to converge"
  - "agents anchor on initial assessments and won't update"
  - "single-round synthesis isn't achieving consensus"
fan_out:
  assess: 3
script_dependencies:
  - "check_convergence.py"
config_features:
  - "fan_out"
  - "self_chaining"
  - "command_succeeds"
stages:
  - name: assess
    sheets: "fan_out(3)"
    instrument_guidance: "score-author's choice — needs strong reasoning capability for expert assessment; sonnet or opus recommended"
    fallback_friendly: false
    purpose: "Each assessor independently evaluates the problem and documents their position, reading prior-round assessments if available."
    artifacts: []
  - name: check-convergence
    sheets: 1
    instrument_guidance: "cli — convergence validation via user-supplied script that analyzes assessment variance"
    fallback_friendly: true
    purpose: "Run the convergence check script to determine if assessments have sufficiently converged."
    artifacts: []
composes_with:
  - pattern: "Source Triangulation"
    how: "Source Triangulation verifies consistency across one-pass multi-perspective views; Delphi Convergence extends to iterative rounds where perspectives update toward consensus."
  - pattern: "Rashomon Gate"
    how: "Rashomon Gate captures multiple conflicting perspectives; Delphi Convergence iterates those perspectives toward measurable convergence."
dependencies: {}
---

## Delphi Convergence

`Status: Working` · **Source:** Delphi method (RAND Corporation). **Forces:** Convergence Imperative + Information Asymmetry.

### Core Dynamic

Multiple agents independently assess, then converge through structured rounds. Different from Fan-out + Synthesis (one round). Delphi iterates until convergence — each round shares anonymized prior assessments, allowing agents to update positions.

### When to Use / When NOT to Use

Use when independent expert judgment needs convergence. Not when a single assessment suffices.

### Marianne Score Structure

```yaml
sheets:
  - name: assess
    instances: 3
    prompt: "Read prior round results if they exist. Write your independent assessment."
    capture_files: ["round-*/**"]
  - name: check-convergence
    instrument: cli
    validations:
      - type: command_succeeds
        command: "python3 {{ workspace }}/check_convergence.py --threshold 0.8"
on_success:
  action: self
  inherit_workspace: true
  max_chain_depth: 5
```

### Failure Mode

Agents anchor on first-round assessments and never genuinely update. Validate that positions actually change between rounds.

### Composes With

Source Triangulation, Rashomon Gate

---
name: "Back-Slopping (Learning Inheritance)"
scale: iteration
type: orchestration-pattern
status: working
forces:
  - "Convergence Imperative"
generators:
  - "Accumulate Knowledge"
problem: "Iterative processes lose hard-won insights because each iteration starts from scratch without accumulated learning."
signals:
  - "later iterations repeat mistakes from earlier ones"
  - "valuable insights discovered during work are lost between iterations"
  - "iterative process plateaus because it cannot build on prior discovery"
config_features:
  - self_chaining
stages:
  - name: work
    sheets: 1
    instrument_guidance: "score-author's choice — instrument must be capable enough for the primary task and able to read and update structured culture artifacts"
    fallback_friendly: true
    purpose: "Execute the primary task informed by accumulated culture, then update the culture artifact with new learning."
    artifacts: ["culture.yaml"]
composes_with:
  - pattern: "Cathedral Construction"
    how: "Cathedral Construction's incremental building uses Back-Slopping's culture artifact to carry integration lessons and architectural decisions across iterations."
  - pattern: "CDCL Search"
    how: "CDCL Search's learned clauses are a specialized form of culture; Back-Slopping generalizes the inheritance mechanism beyond failure-specific constraints to all accumulated learning."
  - pattern: "Systemic Acquired Resistance"
    how: "Systemic Acquired Resistance broadcasts defense primers across scores in a concert; Back-Slopping carries learning forward across iterations within a single self-chaining score."
dependencies: {}
---

## Back-Slopping (Learning Inheritance)

`Status: Working` · **Source:** Sourdough bread making. **Forces:** Convergence Imperative.

### Core Dynamic

Each iteration inherits a "culture" artifact from the previous iteration containing accumulated learning. The culture grows and refines over iterations, carrying forward what worked and what to avoid.

### When to Use / When NOT to Use

Use when later iterations should benefit from earlier learning. Not when each iteration is independent.

### Marianne Score Structure

```yaml
sheets:
  - name: work
    prompt: "Read culture.yaml for accumulated learning. Do the work. Update culture.yaml with new insights."
    capture_files: ["culture.yaml"]
    validations:
      - type: file_exists
        path: "{{ workspace }}/culture.yaml"
on_success:
  action: self
  inherit_workspace: true
  max_chain_depth: 10
```

### Failure Mode

Culture grows without pruning. Old lessons that no longer apply accumulate. Include a pruning step that removes stale entries.

### Composes With

Cathedral Construction, CDCL Search, Systemic Acquired Resistance

---
name: "CEGAR Loop"
scale: iteration
type: orchestration-pattern
status: working
forces:
  - "Progressive Commitment"
  - "Instrument-Task Fit"
generators:
  - "Incremental Exposure"
  - "Match Instrument to Grain"
problem: "Coarse-grained analysis produces spurious findings requiring expensive verification to distinguish real from false alarms."
signals:
  - "coarse analysis produces too many false alarms"
  - "expensive to verify every finding at fine grain"
  - "most findings disappear when abstraction is refined"
  - "need selective refinement, not full re-analysis"
stages:
  - name: coarse-check
    sheets: 1
    instrument_guidance: "sonnet — module-level analysis is primarily pattern-matching; sonnet provides good context for reducing false positives without the cost of opus"
    fallback_friendly: true
    purpose: "Analyze code at module level, identifying potential issues without deep reasoning."
    artifacts: ["findings.yaml"]
  - name: triage-findings
    sheets: 1
    instrument_guidance: "opus — distinguishing real from spurious findings requires deep code reasoning and domain knowledge; cannot be delegated to cheaper instruments"
    fallback_friendly: false
    purpose: "Verify each finding: determine if it is a real issue or an artifact of coarse abstraction."
    artifacts: ["triage-report.yaml"]
  - name: refine-or-report
    sheets: 1
    instrument_guidance: "score-author's choice — filtering findings and selecting refinement targets is data-processing logic; any capable instrument suffices"
    fallback_friendly: true
    purpose: "Filter triage results and identify areas requiring finer-grained analysis; report findings confirmed as real."
    artifacts: ["refinement-targets.yaml", "current-report.md"]
  - name: check-termination
    sheets: 1
    instrument_guidance: "cli — this stage uses shell-based validation to assert convergence (no LLM needed)"
    fallback_friendly: false
    purpose: "Verify that all refinement targets have been resolved, terminating the loop if convergence is achieved."
    artifacts: []
composes_with:
  - pattern: "Memoization Cache"
    how: "Memoization Cache skips re-analysis of modules whose code has not changed, reducing the cost of CEGAR iterations."
  - pattern: "CDCL Search"
    how: "CDCL Search uses real findings confirmed by CEGAR triage as logical constraints to guide subsequent search."
  - pattern: "Immune Cascade"
    how: "CEGAR instantiates Immune Cascade with abstraction level as the escalation tier: coarse analysis first, then selective refinement on false positives."
config_features:
  - "self_chaining"
dependencies: {}
---

## CEGAR Loop (Progressive Refinement)

`Status: Working` · **Source:** Counterexample-Guided Abstraction Refinement (Clarke et al., 2000), Expedition 4. **Scale:** iteration. **Iteration:** 4. **Force:** Progressive Commitment.

### Core Dynamic

Iteratively refines ABSTRACTION LEVEL, not output. Start coarse. If a problem is found, check if it's REAL or SPURIOUS (artifact of over-abstraction). If spurious, refine only the specific part that caused the false alarm. You never refine more than necessary. The structural move is minimum-cost verification through progressive abstraction refinement.

The multi-instrument strategy is central: cheap instrument (Sonnet) for the broad coarse pass, expensive instrument (Opus) for the targeted triage. This matches the work's nature — coarse scanning is pattern-matching (cheap), distinguishing real from spurious requires deep reasoning (expensive).

**Termination:** The loop terminates when the CLI validation sheet finds `refinement-targets.yaml` is empty (all findings resolved as REAL or SPURIOUS with no new areas to refine). If `max_chain_depth` is reached before convergence, the loop produces its best current report rather than failing.

### When to Use / When NOT to Use

Use for code review at scale (module-level first, function-level only where coarseness misleads), security audits (dependency scan then exploitability analysis), any verification where thorough analysis is expensive and most of the system is fine. Not when the abstraction hierarchy is shallow, spurious counterexamples are rare, or checking spurious vs. real costs more than full fine-grained analysis.

### Marianne Score Structure

```yaml
sheets:
  - name: coarse-check
    instrument: sonnet
    prompt: "Analyze at module level. Write findings.yaml with [{module, finding, confidence}]."
    validations:
      - type: file_exists
        path: "{{ workspace }}/findings.yaml"
  - name: triage-findings
    instrument: opus
    prompt: >
      For each finding in findings.yaml, determine: REAL or SPURIOUS?
      Write triage-report.yaml: [{module, finding, verdict: REAL|SPURIOUS, evidence}].
    capture_files: ["findings.yaml"]
    validations:
      - type: file_exists
        path: "{{ workspace }}/triage-report.yaml"
  - name: refine-or-report
    prompt: >
      Read triage-report.yaml.
      Write refinement-targets.yaml listing modules with SPURIOUS findings needing finer analysis.
      Write current-report.md summarizing all REAL findings confirmed so far.
    capture_files: ["triage-report.yaml"]
  - name: check-termination
    instrument: cli
    validations:
      - type: command_succeeds
        command: "python3 -c \"import yaml; t=yaml.safe_load(open('{{ workspace }}/refinement-targets.yaml')); assert len(t)==0, f'{len(t)} targets remain'\""
on_success:
  action: self
  inherit_workspace: true
  max_chain_depth: 5
```

### Failure Mode

Triage consistently marks real findings as spurious — refinement chases ghosts while real issues pass through. Validate by checking that refined areas produce fewer findings (convergence signal). If the loop exhausts `max_chain_depth` without converging, the abstraction hierarchy may be too shallow for this problem — fall back to full fine-grained analysis. The check-termination assertion fails when targets remain, breaking the self-chain — this is intentional, forcing refinement to continue.

### Composes With

Memoization Cache (unchanged modules skip re-analysis), CDCL Search (real findings become constraints), Immune Cascade (CEGAR IS graduated response with abstraction control)

---
name: "Memoization Cache"
scale: iteration
type: orchestration-pattern
status: working
forces:
  - "Progressive Commitment"
generators:
  - "Incremental Exposure"
problem: "Self-chaining scores and iterative processes re-execute stages whose inputs haven't changed, wasting computation."
signals:
  - "self-chaining scores re-analyze unchanged modules wastefully"
  - "concert campaigns process overlapping inputs redundantly"
  - "CEGAR Loops re-examine stable abstraction regions unnecessarily"
  - "iterative refinement compounds costs when inputs don't change"
stages:
  - name: check-cache
    sheets: 1
    instrument_guidance: "cli — simple Python script execution; no language model required"
    fallback_friendly: true
    purpose: "Validate the memoization cache is intact and contains entries for the current stage."
    artifacts: []
  - name: analyze
    sheets: 1
    instrument_guidance: "score-author's choice — capability depends on the analysis task, but memoization is load-bearing for avoiding re-execution"
    fallback_friendly: false
    purpose: "Analyze only files not in the cache or with changed fingerprints; update memo-cache.yaml with new entries."
    artifacts: ["memo-cache.yaml"]
composes_with:
  - pattern: "CEGAR Loop"
    how: "CEGAR Loop refines abstractions; Memoization Cache prevents re-analyzing unchanged regions of the refined model."
  - pattern: "Cathedral Construction"
    how: "Cathedral Construction builds iteratively; Memoization Cache caches layer results to avoid re-analyzing unchanged layers."
  - pattern: "Fixed-Point Iteration"
    how: "Fixed-Point Iteration converges through repeated refinement; Memoization Cache detects converged regions and skips re-analysis."
script_dependencies:
  - "cache_check.py"
dependencies: {}
---

## Memoization Cache

`Status: Working` · **Source:** Dynamic programming, functional memoization (Bellman, 1957), Expedition 4. **Scale:** iteration + score-level. **Iteration:** 4.

### Core Dynamic

Workspace artifact `memo-cache.yaml` records input fingerprints and corresponding output fingerprints per stage. Before executing, the agent checks the cache: if the input fingerprint matches, reuse the cached output without re-execution. Not about caching LLM responses (infrastructure concern) — about recognizing at the ORCHESTRATION level that a stage's inputs haven't changed. Self-chaining scores that re-analyze unchanged modules are computing Fibonacci naively.

**Context invalidation:** Cache entries include a `context_hash` derived from prelude content and relevant workspace state beyond direct inputs. When the prelude changes (different instructions, updated conventions), the context hash invalidates affected entries even if input files are identical. The user-supplied `cache_check.py` script computes both input fingerprints and context hash.

### When to Use / When NOT to Use

Use for self-chaining scores where each iteration modifies only part of the workspace, concert campaigns where scores analyze overlapping inputs, or CEGAR Loops where refined modules need re-analysis but unchanged ones don't. Not when inputs change every iteration, cache management costs more than re-execution, or the context hash is too coarse (invalidating too much) or too fine (missing real invalidations).

### Marianne Score Structure

```yaml
sheets:
  - name: check-cache
    instrument: cli
    validations:
      - type: command_succeeds
        command: "python3 {{ workspace }}/cache_check.py --stage analysis --workspace {{ workspace }}"
  - name: analyze
    prompt: >
      Read memo-cache.yaml. Analyze ONLY files not in the cache (or with changed fingerprints).
      Update memo-cache.yaml with new entries: {file, input_hash, output_hash, context_hash, timestamp}.
    capture_files: ["memo-cache.yaml"]
    validations:
      - type: file_exists
        path: "{{ workspace }}/memo-cache.yaml"
```

**Script dependency:** `cache_check.py` is user-supplied. Interface contract: `--stage NAME --workspace PATH`. Exits 0 if cache is valid and contains entries for the current stage. Exits 1 if cache needs rebuilding. The script computes SHA-256 fingerprints of input files and a context hash from prelude content.

### Failure Mode

Cache serves stale results because the context hash missed a relevant change (e.g., a prelude update changed the analysis criteria but not the input files). If cached results look wrong, clear the cache and re-run — the first run is no more expensive than running without memoization. Over-aggressive caching (caching everything) wastes disk and adds lookup overhead; only cache stages where re-execution is expensive.

### Composes With

CEGAR Loop (cache unchanged abstractions), Cathedral Construction (cache across cathedral iterations), Fixed-Point Iteration (cache stable regions during convergence)
