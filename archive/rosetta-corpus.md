# The Rosetta Pattern Corpus — v6 (Final, post-adversarial-review)

**Iteration:** 6, final — the v6 draft after three adversarial reviews (Practitioner, Skeptic, Newcomer), verdicts **Flawed; needs major revision** / **Needs revision** / **Needs revision**; this document is the integration.
**Core entries:** 17 counted — 5 laws (The Etiquette Law, The Validity Window, The Freeze, Typed Force, The Write-Time Record) and 12 patterns — down from the draft's 25. Seven draft entries left the core (4 → Awaiting Primitives, 2 → archive, 1 → demoted to an idiom); 1 was split and survives renamed. Fan-out + Synthesis returns to **foundational primitive**, uncounted, where v5.1 had already put it.
**Candidate pool this iteration:** 42 patterns from six disjoint expeditions, 27 expedition-level kills, collided in `03-the-collision.md`; merged against the permanent v5.1 corpus (21 core + 2 foundational; every v5.1 entry retained in the decomposed view — see Merge Ledger).
**Curation denominator, stated honestly (Review 2's demand):** the permanent corpus is **111 pattern files, 5 of them laws** across core, archive, and awaiting tiers. The 17-entry core is the *counted, proof-owing* set, not the whole corpus. Nothing is hidden behind the word "draft."
**Status of this document:** FINAL for iteration 6. Every score structure below is written in the dialect the engine actually accepts, re-verified against source on 2026-09-04 (`src/marianne/core/config/{job,execution,workspace,orchestration,spec}.py`, `src/marianne/execution/validation/engine.py`). Where a needed primitive does not exist, the pattern says so and routes to Awaiting Primitives — no exceptions this time, including the two fabrications the reviews missed (see Review Integration, systemic change 2).

---

## Review Integration

Three adversarial reviews attacked `04-draft-corpus.md`. Review 1 (The Practitioner) reviewed all 25 patterns individually, re-ran `mzt validate` across the proof estate, and returned **Flawed; needs major revision**. Review 2 (The Skeptic) applied the structural-identity test — a pattern survives only if its invariant and transition function survive complete removal of the metaphor — and returned **Needs revision**. Review 3 (The Newcomer) read the engine source and asked whether someone who just ran their first score could use the document; it returned **Needs revision** with the headline: "The pattern *ideas* are the strongest I've seen in this concert. The *score structures* are systematically un-loadable as written." Here is what changed, pattern by pattern, with the reviews that forced each decision.

### Cut from core → Patterns Awaiting Primitives (4)

**Calling the Show** — all three reviews found the defining machinery inexpressible in the shown DAG. Review 1: "Move to Awaiting Primitives until an actual recurring cue state machine is shown... the DAG is four serial movements and models none of that." Review 2: "the displayed four-stage chain is not continuous, does not overlap standby N+1 with execution N, and cannot 'proceed around' a held dependency — `skipped_upstream` skips dependents; it is not a bypass lane." Review 3: "the pipelined cue structure cannot be expressed in the linear movement DAG shown." The overlap (standby for cue N+1 pipelined against execution of cue N) and the hold-and-proceed-around semantics require either a recurring per-cue state machine or cross-score cue pointers; neither exists. Moved to Awaiting with the buildable approximation stated: Standby–GO invoked once per cue inside a bounded self-chain, the cue ledger as a workspace artifact advanced by a CLI movement, and holds recorded as visible skips — the continuous form is the blocked part, not the cue discipline.

**Relieving the Watch** — Reviews 1 and 2 killed the structure; Review 3 dissented and the dissent is recorded here, not buried. Review 1: "the deck log is supposedly maintained continuously, but it is appended once after the work movement; a crash during work loses exactly the state the pattern claims to preserve... Cut or move to Awaiting Primitives." Review 2: "Marianne cannot recover an LLM's unexternalized mid-attempt state from that. Without a write-ahead protocol, transactional checkpoints, or a runtime hook, this is Self-Stabilizing Custody plus a diary." Review 3 called it "the crash-recovery pattern every long-running user needs, and the deck-log is concrete." Adjudication: the majority carries it, because the pattern's central claim — any-instant relief — is exactly the part mid-movement crashes falsify. Moved to Awaiting, blocked on mid-sheet checkpointing (a write-ahead hook or transactional sheet checkpoints). The expressible half ships in the Awaiting entry: the deck log as an append-only JSONL the working sheet writes *as it proceeds* (not at movement end), movement-boundary reconciliation gates joining log claims to disk facts, and `mzt recover` rehearsed as the spine. When the checkpoint primitive lands, this re-enters core with Review 3's endorsement already on record.

**The Strike Clock** — Review 1: "Marianne timeouts fail sheets; they do not branch into pre-armed alternate work... Strengthen substantially or archive." Review 2: "the example declares no wall-clock budget mechanism... no mechanism by which timeout selects a tier; normal timeout fails work rather than branching to a pre-armed product." Review 3, precisely: "no primitive selects a degradation tier on timeout. The Strike Clock's central claim — 'time-out selects a tier instead of triggering invention' — has no carrier. By the draft's own rule... Strike Clock and ATO violate that rule silently." The draft's own standing rule was its own indictment. Moved to Awaiting, blocked on a timeout→tier transition. What survives, per Review 3: the inverted-DAG teardown order, per-movement budgets via `instrument_config.timeout_seconds` (and the *scheduled-run* wall clock `max_wall_seconds`, job.py:907 — which exists but bounds a whole scheduled run and selects nothing), pack-for-next-run, and the curfew report as the successor's first input. The tier-arithmetic is the blocked half.

**Put-In** — Reviews 1 and 2 killed the mechanism; Review 3 dissented, again recorded. Review 1: "no old/new instrument assignment, no actual shadow execution, no separate workspace, and no demonstrated runtime fallback remap... Move to Awaiting Primitives until a real two-job handoff and rollback trial exist." Review 2: "Retaining files is not retaining an executable fallback route... the actual transfer primitive is missing." Review 3: "the model-deprecation answer, with a real diff gate" — one of the strongest. Adjudication: the kill turns on a real absence — seat remap at runtime. `fan_out` and instrument assignment expand at parse time (already recorded in awaiting.md under Physarum); isolation is job-level, so the shadow run is expressible as a *second job*, but flipping the live seat mid-concert is not expressible at all. Moved to Awaiting with the buildable approximation: track-sheet compile from incumbent artifacts, shadow run as an isolated job producing artifacts alongside (never over) the incumbent's, structured diff gate with `--require-bijection`, and the cutover as a *versioned score edit* — the incumbent written into the next score version's fallback chain, which is the honest, available form of "the old chair stays warm."

### Cut → archive / demoted (3)

**Command by Negation** — unanimous. Review 1: "an operating posture, not yet a score pattern... Cut it from core until delivery receipts and a negative-broadcast acknowledgement join exist." Review 2: "There is no positive transition system here... Fold the cost discipline into Mission Command or the Declared Window." Review 3: "the pattern lives in settings, not structure... demote to an idiom under Mission Command / context economics." Demoted to an **idiom** recorded under Mission Command and the Declared Window: `cross_sheet: {auto_capture_stdout: false, lookback_sheets: <small>, max_output_chars: <small>}` plus intent-forward prelude and terminal validations. One correction to the draft baked into the idiom: the draft wrote `lookback_sheets: 0` intending *zero context* — in the engine, **0 means ALL completed sheets** (workspace.py:346). Context austerity uses a small positive bound, never 0.

**The ATO Cycle** — Review 1: "The defining property is three overlapping generations, but the score shows one serial cycle and configures scheduled overlap to `skip`... Cut the current form." Review 2: "The score's `overlap: skip` prohibits overlapping scheduled jobs and shows only one serial cycle... Cut or redesign around physically concurrent cycle identities and atomic rollover." The frozen-manifest half is the Freeze law under cadence pressure; the rolled-backlog half is Positive Transfer; the identity — overlapping generations — needs concurrent cycle instances, which `overlap: skip` (correctly, for single-workspace safety) forbids. Archived with the redesign condition stated: separate workspaces per cycle generation, `overlap` policy decided per-pair, atomic cut→backlog bijection. Not Awaiting: nothing here is blocked on an engine primitive; it is blocked on a design that has not been written.

**Cluster Lead** — Review 1: "Member discovery, report freshness, identity, and needs-register completeness are unspecified... This is a weekly report generator, not yet coordination without command." Review 2: "Keep only if 'coverage unknown' is represented per missing member/region, not as a blanket phrase that greens the report" — the draft's `content_regex: "coverage unknown|owned by:"` passes on one lucky phrase. Review 3: "real-world true, structurally thin: a schema, an ingest, a gap report. Archive with the 'coverage unknown' honesty clause quoted into the law on truth decay." Archived exactly so. The honesty clause is promoted into the corpus (below, in The Declared Window and the C9 grammar row): **a coordination artifact whose inputs are incomplete publishes the incompleteness — "coverage unknown" per unreported member/region — never a manufactured success.** The 3W reporting schema and `csv_unique_key` duplication check are real and noted in the archive entry for reuse.

### Split (1)

**Test Screening to Picture Lock** — Review 2: "two patterns stapled together: unprimed external evaluation followed by the Freeze... Split the falsifier from the lock and prove each." Executed. The lock half (hash-frozen cut, finishing fan-out keyed to the digest, drift gate) **is** The Freeze law's iterative form and lives there — one lock primitive, not two. The surviving pattern is renamed **The Unprimed Falsifier**: evaluation by recipients who receive *only the artifact* — never the makers' intent — returning typed, located evidence. Review 1's strengthening conditions (physical context isolation, structured reaction cards, evidence-density math, executable recut loop) and Review 3's demand for a priming-absence check that actually runs are implemented in the structure below.

### Narrowed (2)

**Typed Force** — Review 1 wanted the umbrella cut: "too broad to be a law... Retain the fan-in typing rule and precedent semantics separately." Review 2 kept it but demanded the split that saves it: "Separate syntactic typing from the authority that assigns a type." The law survives **narrowed to one discipline with the authority inside it**: (1) type at creation, (2) the type is assigned by a *named authority* carried as a provenance field — a gate can check syntax and provenance, never truth, and the law no longer pretends otherwise, (3) the type selects the enforcement rule, (4) retyping is visible. Its former umbrella is delegated to the pattern forms that earned it: binding/persuasive force → The Precedent Bench; fan-in aggregation headers → The Dropped Axiom; evidence admissibility → Proof-Carrying Artifact (v5.1); allocation provenance → archive. Review 3's enum mismatch (the typecheck whitelist didn't contain Condorcet's demotion ladder) is fixed by making the demotion ladder the shared enum across both patterns.

**Fan-out + Synthesis** — Reviews 1 and 2, unanimously: "This is a primitive, not a differentiated corpus pattern" / "a primitive DAG shape... Keep it as syntax and remove it from the pattern count." The draft had re-promoted it to counted core; it returns to foundational primitive, as v5.1 had already ruled. Its two iteration-6 clauses (the typing clause, the window clause) survive as named contracts attached at the merge — The Dropped Axiom's header and The Declared Window's manifest — not as reasons to re-count the primitive.

### Strengthened (every survivor, with the reviews that forced it)

- **The Etiquette Law** — "the moment a check can be a command, it must be a command" was too absolute (Reviews 1 and 2). The criterion is now stated: a check moves to a deterministic stage when it can be made *replayable, externally checkable, and bounded* — and Review 1's second clause is added to the law: **a deterministic gate must be small, independently testable, and exercised against a reachable negative control** — a gate that cannot fail is a receipt.
- **The Validity Window** — the transition table Reviews 1 and 2 demanded: states `{stamped, valid, expired, regenerated, degraded}`, the precedence between elapsed TTL, minimum age, and accumulated maturity stated, regeneration executed inside the gate movement's single CLI transaction (expiry fails forward to a *new* window id, never re-presents the same bytes), and the adjacency rule: the gate runs in the movement immediately before the consumer, and the consumer must cite the window id it was admitted under.
- **The Freeze** — the pin is now expressible: `file_sha256` cannot pin a runtime-written digest (it requires a literal 64-hex at authorship, execution.py:668-680), so the lock movement writes `frozen.sha256` and every consumer-side check is `sha256sum -c` via `command_succeeds` (Review 3's fix). Delivery is by **required cadenza** on each specialist sheet — the frozen artifact physically cannot be absent (Reviews 1 and 2). The distinctions from Prefabrication, Fork-Evident History, and Attested Merge Gate are stated in the body (Review 1).
- **The Write-Time Record** — the atomic transaction Reviews 1 and 2 required: intent row, effect, and receipt commit inside **one CLI process** keyed by a stable `effect_id`; a crash leaves an open row that the audit *fails* on (fail-closed), and a re-run refuses double-execution by id. Line-count decorations are gone; the audit is a three-way join (row ↔ receipt ↔ settlement) with empty residue.
- **Monitor Mix** — per-instance delivery is real: cadenzas key on the expanded sheet number and the file path carries `{{ instance }}`, so each fan-out voice receives exactly its mix, `required: true` (Reviews 1 and 2). The line check validates every mix against the prescription's channel list and char budgets *before* the performers run, and outputs must cite the mix id they performed from.
- **Condorcet's Premise** — routing fixed to expanded sheet numbers via `per_sheet_instruments` (Review 3); the calibration ground truth is a pre-authored fixture in the score directory, not runtime invention (Reviews 1 and 3); the estimator is defined and bounded — mean pairwise error co-occurrence ρ̄ over calibration items, design effect n/(1+(n−1)ρ̄) as an equicorrelation *upper bound*, with the full co-occurrence matrix riding the manifest as data (Review 2); and the family census is **provenance evidence, not independence** — instrument-name inequality proves nothing on this host, and measured error behavior is the only admissible basis for the aggregation rule (Review 1).
- **The Declared Window** — the word ban is dead (Reviews 1 and 2: "easy to evade," "a lexical heuristic"). The contract is now a structured claim ledger: the synthesizer emits `claims.jsonl` rows `{claim_id, text, class ∈ {in-window, total-seen, refused}, window_id}`; a CLI movement writes the window manifest from the run's actual `cross_sheet` configuration and prior artifacts; the join gate asserts every global-quantifier claim in the prose has a ledger row and the counts reconcile (`exact_in_window + refused = claims_emitted`). The corpus-level honesty rule from Cluster Lead is quoted into this pattern.
- **The Gas-Free Certificate** — Review 1's finding was the most dangerous in the set: "the destructive AI sheet is told to run the permit check as its first action, but the validation occurs after the sheet, so destruction can precede or ignore the check... otherwise this pattern teaches false safety." Fixed at the root: **destruction is a command, so the whole pattern is CLI-native.** The destroy movement is `instrument: cli` running one wrapper that checks the permit (digest match + freshness) and executes the destruction in the same transaction; a failed check refuses, exit non-zero, nothing destroyed. The AI plans; the wrapper presses the button. Independence is authored provenance — a separately-committed `certifier/` directory with its own digest recorded in the permit — not a pathname (Review 2).
- **Top-Down Demolition Order** — the strongest pattern by all three reviews ("genuinely distinct," "survives complete removal of the ship-breaking story," "a genuine correction to naive saga thinking"). Strengthened per Review 1: the serialized driver is real — a bounded self-chain (`concert` + `on_success: run_job`) re-invoking the score per removal step, each step's CLI wrapper sweeping consumers-of-current-step (`--expect-empty`) before and re-deriving the leaf set after; the plan is JSON checked by jq, never prose greps; the order re-derivation lives in a separately-authored `verify/` directory.
- **Rent-Then-Commit** — the routing state machine now exists in the real dialect: the ladder decision is written by a CLI movement, and the two lanes are **sheets gated by `skip_when` commands** — the cheap lane's sheets skip when `decision.lane != "rent"`, the strong lane's when `!= "buy"`; no dynamic instrument assignment is claimed. The self-chain is the real `concert`/`on_success` form (see systemic change 2), `capture_files` carries the decision into executors, and executors cite the ladder position (Reviews 1 and 3). The deterministic 2-competitive bound is proven; the randomized 1.582 variant is recorded as archive-color requiring its distribution assumptions stated (Review 2).
- **Vintage Overlay** — survived Review 3's cut motion 2–1, and the merge critique is answered structurally: the overlay *files* are authored artifacts, so they are pinned with literal `file_sha256` digests; the condition-map lookup is **total with refusal** — an unknown condition vector exits non-zero rather than defaulting (Reviews 1 and 2); the manifest reaches consumers as a required cadenza (data, not dynamic `spec_tags` — Review 2's correction that runtime-measured conditions cannot re-route already-resolved spec tags); and the vintage record (conditions + digests + overlay ids) is the Write-Time Record's run-level instance.
- **The Economic Injury Line** — "February" is now structural: the threshold inputs and table are **authored into the spec corpus before the season**, digest-pinned; the run's first movement only *verifies* the re-derivation against the pinned table (Reviews 1 and 2). `run_seed` is a declared prompt variable; the wasp clause is an executable tier ordering (broad-spectrum tier barred while the incremental tier's efficacy check passes); the no-action season is a real negative control — visibly skipped treatment sheets and a green exit (Review 1).
- **The Precedent Bench** — narrowed to a typed append-only decision registry (Review 1: "narrow it to a typed append-only decision registry") with **one final adjudication authority** (Review 2): a single named bench seat decides; advisory seats may fan out but their aggregate is a Dropped Axiom-typed input, never an undisclosed vote. The precedent index reaches the brief and bench sheets by required cadenza keyed to their expanded sheet numbers (Review 1's placement fix); enrollment is one serialized CLI writer appending holding rows and supersession edges atomically; and the registration-time/runtime delivery distinction is stated as what it is — spec-corpus fragments inject as of registration, the cadenza injects the live index at runtime, and a score citing precedent that moved between the two is exactly what the cite-join gate catches.
- **Demobilization Checkout** — four separate tables replace the conflated one (Review 1): `census.jsonl` (what exists), `dispositions.jsonl` (what the AI decided per resource id), `receipts.jsonl` (what the CLI did), and the settlement probe results — census maintenance begins at commissioning via the Write-Time Record (Review 2), and the seal movement runs the Gas-Free discipline before any destructive cleanup. The `on_success`/`on_failure` attachment is written in the real form: hooks live on the concert's terminal score, `run_job` to the demob score, mirror on failure with evidence-preservation disposition priority.
- **The Dropped Axiom** — input typing is declared by the **producer**, not classified by the synthesizer (Review 1: "Make the input type explicit... do not force one omnibus table"): each panel-emitting stage writes `input_type ∈ {binary-verdict, ranking, interconnected-propositions, non-reconstructible-judgment}` on its output, the synthesizer applies exactly the lookup row for the declared type, and the typechecker enforces rule ↔ `axioms_dropped` bijection per row. Kept as a standalone within-stage pattern against Review 2's fold motion (Reviews 1 and 3 wanted the fan-in rule separate and immediate; the fold is recorded as the losing argument with its reason).

### Systemic changes

1. **Every score structure rewritten in the real dialect — and this time verified against source, not against memory of v5.1.** The v5.1 final shipped a Real Dialect section and the v6 draft violated it anyway; the reviews caught the violations (movement-level `fan_out`, expanded `total_items`, top-level `cadenzas`/`instrument_map`, `spec_tags` under `spec:`, digest-free `file_sha256`, `max_wall_seconds` as a movement curfew). All are fixed. Two of v5.1's own Real Dialect claims were also wrong and are corrected here: `spec_tags` is a **`sheet:` field**, not a `spec:` field (job.py:246); `instrument_map` keys on **expanded sheet numbers** and rejects duplicate assignment (job.py:436-459) — movement-keyed maps with one sheet claimed twice fail at load.
2. **Two fabrications the reviews did not name, found by this integration's own source pass.** (a) `lookback_sheets: 0` means **all completed sheets** (workspace.py:346) — the draft used it twice to mean *zero context*; every such use would have silently maximized context. (b) `on_success: {action: self, ...}` is not a shape the engine accepts — `on_success` is a list of typed hooks (`run_job` requiring `job_path`, `run_command`, `run_script`) under `concert: {enabled, max_chain_depth, inherit_workspace}` (orchestration.py:280-341). Self-chaining is real but only in that form; all self-chain structures below use it.
3. **The curation denominator is stated in the header** (Review 2: "That makes the effective living core roughly 44 entries, not 25... it hides the denominator"). Core 17 / archive / awaiting are named tiers of one 111-file corpus, every file indexed in INDEX.md.
4. **Bookkeeping corrected to disk** (Review 1: "Disk contains 13, not 14, proof-score YAMLs"; Review 3 confirmed): 13 YAMLs; both reviews independently ran `mzt validate` and agree — 7 pass (`cathedral-construction`, `firing-the-pass`, `join-semilattice-merge`, `live-relay`, `negative-treatment-watch`, `rashomon-gate`, `the-attested-merge-gate`), 6 fail (`dead-letter-quarantine`, `echelon-repair`, `prefabrication` — folded-command checks; `immune-cascade`, `shipyard-sequence`, `source-triangulation` — dead `../../workspaces/` parents). The corpus no longer counts a non-validating file as a live proof; dispositions are in the Proof Estate section.
5. **Proof debt is reported as zero-for-six, not "targeted"** (Review 3: "'Proof debt is a blocking requirement, inherited' — then the draft is blocked, by its own rule"). The six queued proofs exist on disk as **zero executed scores**. The queue stands, each entry now carrying the minimal-discriminating-score constraint (Reviews 1 and 2: stop rewarding monument size; a proof must fail when the pattern is removed), and the blocked status is the honest current state.
6. **The Script Library debt is named at its true size** (Review 3: "Open Question 7 says '~20'; I count roughly 50"). Every script referenced below is a named entry with an interface contract in the Script Library section; the corpus states plainly that these are contracts to implement, not shipped files. Patterns whose load-bearing structure reduces to an unshipped script say so in their `status:` field (`approximation` where the wrapper is the pattern).
7. **The human-escalation seam is carried as an unowned terminal, third iteration running** (all three reviews). It is recorded in Open Questions with its instances (hold escalation, the impairment emergency, negation's surface order, waiver authority) and the v4 Andon Cord named as ancestor. No pattern below pretends to own it.
8. **Divergences and dissents are preserved, not flattened.** Review 3's dissents on Relieving the Watch and Put-In are quoted in the Awaiting entries; the Vintage Overlay 2–1 and Dropped Axiom fold-motion votes are recorded with reasons. A corpus that erases its reviewers' minority reports is exactly the silent-supersession failure the Precedent Bench exists to prevent.

---
## The Real Dialect (v6, re-verified 2026-09-04)

The substrate as verified against engine source this iteration: `src/marianne/core/config/job.py` (MovementDef at :156, SheetConfig at :203, instrument_map validator at :436), `src/marianne/core/config/execution.py` (ValidationRule at :498), `src/marianne/core/config/workspace.py` (CrossSheetConfig at :323), `src/marianne/core/config/orchestration.py` (PostSuccessHookConfig/ConcertConfig at :280-341), `src/marianne/execution/validation/engine.py` (condition parser at :254), plus the seven passing proof scores as living usage. Every snippet in this corpus is an excerpt from this skeleton. A pattern that cannot be phrased here is not a pattern yet — it is Awaiting Primitives.

```yaml
name: my-score
description: "One line."

instrument: opus                       # primary; named alternates below
instruments:
  cheap:  { profile: opencode, config: { model: "zai-coding-plan/glm-5.3-flash" } }
instrument_fallbacks: [opus, cheap]    # [] on a deterministic stage = the etiquette does not degrade

movements:                             # MovementDef is extra="forbid":
  1: { name: produce }                 #   allowed keys are name, instrument,
  2: { name: verify, instrument: cli,   #   instrument_config, voices, instrument_fallbacks.
       instrument_fallbacks: [] }       #   fan_out here FAILS AT LOAD.
  3: { name: panel, voices: 3 }         # voices = per-movement fan-out shorthand
  4: { name: consume }

sheet:
  size: 1
  total_items: 4                       # LOGICAL movements, pre-expansion
  fan_out: { 3: 3 }                    # movement-number -> instance count; parse-time, static
  dependencies: { 2: [1], 3: [2], 4: [3] }   # movement numbers
  spec_tags: { 3: [flight-rules] }     # a SHEET field (movement-keyed), NOT under spec:
  per_sheet_fallbacks:
    8: []                              # keyed by EXPANDED sheet number
  cadenzas:
    8:                                 # keyed by EXPANDED sheet number
      - file: "{{ workspace }}/evidence/produce.json"   # Jinja in the prompt pipeline
        as: context
        required: true                 # fail closed when absent
  per_sheet_instruments:               # expanded sheet numbers; one sheet, one instrument
    5: claude-code
    6: codex-cli
    7: opencode

spec:
  spec_dir: "{score_dir}/specs"        # corpus attached by reference

cross_sheet:
  lookback_sheets: 5                   # NOTE: 0 means ALL completed sheets, not none
  max_output_chars: 4000
  capture_files: ["{{ workspace }}/decision.yaml"]   # Jinja here too

concert:                               # self-chaining / job chaining lives HERE
  enabled: true
  max_chain_depth: 12
  inherit_workspace: true
on_success:                            # a LIST of typed hooks — {action: self} is not a shape
  - type: run_job
    job_path: "{score_dir}/my-score.yaml"

prompt:
  variables: { run_seed: 7 }
  template: |
    {% if stage == 1 %}
    Do the work. Write {{ workspace }}/deliverable.md.
    {% elif stage == 2 %}
    bash "{score_dir}/scripts/gate.sh" "{{ workspace }}"
    {% elif stage == 3 %}
    You are voice {{ instance }} of {{ voice_count }}.
    {% else %}
    Work only from admitted artifacts. Cite their paths.
    {% endif %}

validations:                           # flat list; FORMAT-STRING paths ({workspace}); never Jinja
  - type: file_exists
    path: "{workspace}/deliverable.md"
    condition: "stage == 1"
  - type: command_succeeds
    command: 'bash {score_dir}/scripts/gate.sh {workspace} --check-only'
    condition: "stage == 2"
  - type: content_contains
    path: "{workspace}/verdict.md"
    pattern: "ADMITTED"
    sheet: 8                           # shorthand for condition: "sheet_num == 8"
  - type: file_sha256
    path: "{workspace}/pinned-input.yaml"
    sha256: "<64-hex literal, known at authorship>"
    condition: "stage == 1"
```

**Sheet numbering** (the detail the draft got wrong everywhere): with `total_items: 4` and `fan_out: {3: 3}`, movement 1 is sheet 1, movement 2 is sheet 2, movement 3 expands to sheets 3–5, movement 4 is sheet 6. `per_sheet_fallbacks`, `cadenzas`, `per_sheet_instruments`, `instrument_map`, **and `skip_when`** key on the *expanded* sheet number (skip_when is resolved against `sheet.num` at dispatch — adapter.py:2947; v5.1's claim that it keys on the movement number is corrected here); `spec_tags`, `dependencies`, and `fan_out` key on the *movement* number. `condition: "stage == N"` gates by movement number (all voices of that movement) and is the house style in the passing proof scores; `sheet: N` targets one expanded sheet.

**Two templating systems, deliberately different:** the prompt pipeline (templates, cadenza/prelude paths, capture_files) is Jinja `{{ }}`; the validation engine (paths, commands, working_directory, skip_when) is Python format `{}`. `{{ score_dir }}` in a template, `{workspace}` in a command. Mixing them is the most common first-score bug.

**Validation types available:** `file_exists`, `file_modified`, `content_contains`, `content_regex`, `command_succeeds`, `path_in_scope`, `field_match`, `file_sha256` (literal digest only — runtime pinning is `sha256sum -c` inside a `command_succeeds`), `csv_unique_key`. Conditions support `sheet_num ==/>=/<= N` and `and` conjunctions; a condition naming an unknown variable evaluates **false** (the validation silently never runs — write `sheet_num`, not a hoped-for variable).

**Primitive coverage refresh (source-verified 2026-09-04):**

| Primitive | Real dialect account |
|---|---|
| `prompt_extensions` | Score-level extensions append first, then expanded-sheet extensions; entries are inline text or `.md`/`.txt` directives. |
| `interactive_mode` | `instrument_config.interactive` is tri-state; absent uses the verified profile default, explicit true/false forces driven/headless execution, with per-sheet nudge controls. |
| `mcp_shared_pool` | The daemon multiplexes one configured process per MCP server over Unix sockets and exposes only MCP techniques active for the sheet. |
| `bridge` | `bridge` accepts Ollama/MCP proxy and hybrid-routing config, but the conductor does not consume it: config-only, not a routing claim. |
| `code_execution` | Opt-in code mode executes classified shell/Python/Node blocks with timeouts; `require_sandbox` fails closed without `bwrap`, otherwise fallback is unsandboxed and loud. |
| `sheet_pacing` | `pause_between_sheets_seconds` delays later serial dispatch after a successful sheet; it is nonnegative score-level pacing. |
| `relative_workspace_anchor` | A file-loaded relative `workspace` anchors to the score directory; string-loaded YAML anchors it to process CWD. |
| `state_backends` | Scores model `json`/`sqlite` plus `state_path`; conductor runs remain SQLite-registry-authoritative and do not consume the per-score path. |
| `entropy_response` | Learning config models low-entropy cooldown, budget boost, and quarantine revisit; live daemon health uses daemon-level settings, not this per-score block. |
| `learning_auto_apply` | Structured trust/status/count controls supersede deprecated flat fields; live dispatch still injects generic pattern results rather than consuming them. |
| `agent_card` | A score can publish an A2A discovery card and route in-process; inbox and registry state are memory-only, not restart-persistent. |
| `runtime_variables` | Repeated `mzt run --var key=value` strings override prompt variables, later duplicates win, and the merged values persist across resume. |
| `cli_pause` | `mzt pause` requests a sheet-boundary pause and may wait for acknowledgement; `--force` delegates to immediate cancel. |
| `cli_resume` | `mzt resume` continues paused/failed/chain-held state; `--from-sheet` deliberately resets that sheet and every later sheet. |
| `cli_modify` | `mzt modify` validates a replacement score, pauses a running job, swaps its config, and may resume it. |
| `cli_cancel` | `mzt cancel` interrupts the active sheet and marks the job `CANCELLED`; it is not graceful boundary pause. |
| `cli_clear` | `mzt clear` removes eligible terminal job state; it does not clear instrument rate limits. |
| `conductor_lifecycle_cli` | `mzt start`, `stop`, `restart`, and `conductor-status` operate the single conductor daemon. |
| `clear_rate_limits_cli` | `mzt clear-rate-limits` clears one/all instrument limit records and returns affected `WAITING` sheets to `PENDING`. |
| `prompt_preflight` | Daemon-level token preflight warns or rejects at configured thresholds; zero disables a threshold and warning must remain below error. |
| `self_healing` | After retry exhaustion a sheet enters the HEALING baton state: the healing coordinator diagnoses (context, diagnosis, remedies registry) and re-dispatches with a repaired prompt; the `--self-healing`/`--escalation` run paths select it. Conductor-amended row 2026-09-04 — the inventory's 21st primitive, added during gap-report review. |

**Verified real, additions since v5.1:** `voices` as movement-level fan-out shorthand; `per_sheet_instruments` (expanded-sheet-keyed); `instrument_map` with the duplicate-assignment rejection; `skip_when` in command form (per movement, exit 0 = skip, fail-open on error); `concert`/`on_success` typed hooks (`run_job` + `job_path`, `run_command`, `run_script`, with `hold` semantics for pause-at-chain); job-level `max_wall_seconds` for *scheduled runs* (ge 60; bounds the run, selects nothing); `instrument_config.timeout_seconds` for per-movement budgets; `mzt validate` three-layer static validation.

**Verified absent (do not write these):** `fan_out` or any key besides the five MovementDef fields under `movements:`; digest-free `file_sha256`; runtime digest discovery; movement-level wall clocks; any timeout that *selects* work instead of failing it; runtime instrument reassignment; mid-sheet checkpoints; `{score_dir}` inside validation commands under `mzt recover` (the recovery path builds a reduced context — prefer `{workspace}`-relative script paths or copy scripts into the workspace at commissioning).

**Instrument recommendations (freshness 2026-09-04):** opus / codex-cli / opencode (GLM-5.3-flash via the paid Z.AI coding-plan profile) for vendor-diverse tiers; ollama for cost-zero tiers; `instrument: cli` for the etiquette. gemini-cli remains retired. Diversity claims pass only through the family census with `family_source` provenance from a live `mzt config` probe — instrument-name inequality proves nothing on this host, where claude-code and opencode both default through GLM/Z.AI-family routes.

---

## The Grammar: v5.1's C1–C10 stand; iteration-6 carriers update four rows

The ten convergences and their structural-identity discipline are unchanged from v5.1 (state variables, authority, medium, deterministic check, failure transition, non-example — see the v5.1 final, preserved in git history and the decomposed view). Iteration-6 additions that survived review:

- **C8 (Independence is constructed)** now carries its arithmetic: Condorcet's Premise supplies the measured design effect and the demotion ladder. Independence claims pass only through the census; `family_source` is provenance, not proof.
- **C9 (Truth decays)** is generalized by the Validity Window law: a validity interval measured from a creation event, whose crossing *is* an event with a defined handler. Cluster Lead's archived honesty rule is quoted into C9's carrier set: **incomplete inputs publish their incompleteness.**
- **C10 (Failure degrades in character)** is armed at composition time where expressible (pre-computed thresholds, skip-gated lanes, pre-authorized tier orderings). The Strike Clock's timeout→tier transition — the strongest form — is Awaiting Primitives, and C10 now says so instead of implying it.
- **C7 (Lagged feedback oscillates)** remains the thinnest convergence; its iteration-6 family members (Batch-Plant Stagger, Green Wave) stay archived. Recorded, not hidden.

The five iteration-6 convergences recorded but not minted in the draft (pre-paid judgment, the unprimed falsifier, artifacts-not-messages, ending-as-phase, two-axes-of-order) keep that status. The Unprimed Falsifier's carrier survived review as a core pattern; pre-paid judgment survives inside the Economic Injury Line and Rent-Then-Commit; two-axes-of-order survives inside Top-Down Demolition's contrast row. None is minted as a law — the minting criterion (a second iteration independently re-deriving it) remains unmet.

**Generators.** Iteration 6 proposed eight generators against v5's six; the reconciliation in the draft stands (G7 unknown horizon, G8 blind maker are the additions), and the corpus's working vocabulary for pattern frontmatter remains the ten forces and eleven generators of `forces.md`. Mapping for the new core: the unknown-horizon generator (G7) expresses as **Finite Resources + Threshold-Triggered Switch** (Rent-Then-Commit, Economic Injury Line); the blind maker (G8) expresses as **Structured Disagreement + Verify through Diverse Observers** (The Unprimed Falsifier). A future iteration may formalize G7/G8 into forces.md; this document does not edit the force table.

---
# Laws & Foundational Primitives

*Five laws. A law is shared arithmetic and transition rules that multiple patterns specialize while guarding different acts. A law differs from a schema discipline (Review 2's test): removing it must change behavior in more than one pattern; otherwise it is a field.*

## The Etiquette Law (formerly The Tool Chain)

```yaml
---
name: "The Etiquette Law"
scale: foundational
status: working
forces: ["Instrument-Task Fit", "Accumulated Signal"]
generators: ["Verify through Diverse Observers"]
problem: "Deterministic protocol checks are given to LLM instruments that can hallucinate them, making the coordination layer no more reliable than the performers it coordinates."
signals:
  - "any check whose result could be a shell exit code"
  - "a gate described in prose inside a prompt"
  - "a fallback from a deterministic instrument to an LLM"
stages:
  - name: "etiquette-gate"
    sheets: 1
    instrument_guidance: "instrument: cli — deterministic by construction; this stage must never think"
    fallback_friendly: false
    purpose: "Own the protocol decision (admit/reject) as a command with an empty fallback chain, self-tested against a reachable negative control."
  - name: "performance"
    sheets: 1
    instrument_guidance: "opus, codex-cli, or opencode — matched to the work's judgment grain"
    fallback_friendly: true
    purpose: "Do the judgment work the gate admitted."
dependencies:
  performance: ["etiquette-gate"]
composes_with:
  - pattern: "Every core pattern"
    how: "prerequisite — every gate in this corpus is an Etiquette Law stage"
---
```

**Source:** v4 iterations 2–4; confirmed iteration 5 (74 attestations) and iteration 6 (every deterministic movement in all 42 candidates carried an empty fallback chain, without coordination).

### Core Dynamic

The deterministic part is always the etiquette, never the music. The protocol layer — cues, gates, ledgers, meters, permits, tallies — goes to non-LLM instruments with empty fallback chains, not because AI instruments are unreliable, but because the etiquette must be *more reliable than the performers*, and the cheapest way to make something reliable is to make it not need to think. Three things must not be conflated: tool use inside an LLM sheet, a deterministic validation command, and a non-LLM instrument that owns execution (`instrument: cli`). The etiquette always belongs to the third. The de Bruijn criterion names the audit condition: the checker must be small enough to audit by reading.

**The criterion, stated (Reviews 1 and 2):** a check moves to a deterministic stage when it can be made *replayable, externally checkable, and bounded* — not "always, the moment it can be a command." Process startup cost, dependency weight, and privilege boundaries are real reasons an inline tool call inside a thinking sheet can be the safer choice; the law governs where *authority over the decision* lives, and that answer is: with a command whose exit code anyone can re-derive.

**The second clause (Review 1):** a deterministic gate must be **small, independently testable, and exercised against a reachable negative control**. A gate that cannot fail is a receipt, not a gate. The structure below carries the self-test as a load-bearing movement, not an aspiration: one fixture that must pass and one corruption that must fail, executed before anything is admitted.

### When to Use / When NOT to Use

Use: wherever a decision can be expressed as a command with an exit status — admission, freshness, counting, ordering, digests, presence.

Not: the work itself is judgment (do not "optimize" tone into a linter). The anti-pattern the law exists to name: a deterministic stage given a fallback to an LLM — a fallback for a clock is a second clock, and two clocks are the desynchronization you built the law to prevent.

### Marianne Score Structure

```yaml
movements:
  1: { name: gates, instrument: cli, instrument_fallbacks: [] }
  2: { name: review }

sheet:
  size: 1
  total_items: 2
  dependencies: { 2: [1] }
  per_sheet_fallbacks:
    1: []                      # the etiquette does not degrade

prompt:
  template: |
    {% if stage == 1 %}
    bash "{score_dir}/scripts/run-gates.sh" "{{ workspace }}" --lint --schema --tests
    The script runs its own teeth first: one known-good fixture must pass,
    one corrupted fixture must fail. Its exit code is the whole decision.
    {% elif stage == 2 %}
    Review only what the gate admitted. Cite gate outputs by path.
    {% endif %}

validations:
  - type: command_succeeds
    command: 'bash {score_dir}/scripts/run-gates.sh {workspace} --self-test'
    condition: "stage == 1"
  - type: command_succeeds
    command: 'bash {score_dir}/scripts/run-gates.sh {workspace} --check-only'
    condition: "stage == 1"
  - type: content_contains
    path: "{workspace}/review.md"
    pattern: "gate-report"
    condition: "stage == 2"
```

### Example

A documentation pipeline: markdown lint, link check, and schema validation as one `instrument: cli` movement with an empty fallback chain and a self-test; the AI reviewer consumes only the typed gate report — its judgment is spent on meaning, not on re-deriving what a script already decided.

### Composes With

Prerequisite — every gate in every pattern in this corpus is an Etiquette Law stage.

---

## Fan-out + Synthesis (Foundational Primitive — uncounted)

```yaml
---
name: "Fan-out + Synthesis"
scale: foundational
status: working
forces: ["Information Asymmetry", "Structured Disagreement"]
generators: ["Frame Multiplication"]
problem: "Work that could be parallelized is done sequentially, or parallel outputs remain fragmented without meaningful integration."
signals:
  - "problem decomposes into independent sub-problems"
  - "sub-problems can be worked simultaneously"
  - "diverse perspectives must be integrated, not concatenated"
stages:
  - name: "prepare"
    sheets: 1
    instrument_guidance: "any — defines scope and partitions"
    fallback_friendly: true
    purpose: "Define the scope and write the partition map."
  - name: "analyze"
    sheets: "fan_out(6)"
    instrument_guidance: "opus/codex-cli/opencode per partition; assign via per_sheet_instruments on expanded numbers"
    fallback_friendly: true
    purpose: "Work one partition; write an instance-tagged artifact."
  - name: "synthesize"
    sheets: 1
    instrument_guidance: "strong reasoner — must carry a typed merge header"
    fallback_friendly: false
    purpose: "Merge with a declared aggregation header and window manifest."
dependencies:
  analyze: ["prepare"]
  synthesize: ["analyze"]
composes_with:
  - pattern: "The Dropped Axiom"
    how: "the merge header grows the typing clause — every fan-in declares its aggregation rule"
  - pattern: "The Declared Window"
    how: "the window clause — synthesis over bounded lookback emits a window manifest"
  - pattern: "Join-Semilattice Merge"
    how: "substitution — when facts are additive, replace judgment-merge with the algebraic join"
---
```

**Status:** foundational primitive, uncounted in the core (Reviews 1 and 2; v5.1 had already ruled this and the draft's re-promotion is reversed). Prior art MapReduce; confirmed iteration 6 by the ban — the brief again forbade returning it, and all 42 candidates positioned against it.

### Core Dynamic

Split work into parallel independent streams, merge in a synthesis stage. The primitive carries two named contracts grown this iteration, both attached **at the merge**, neither a reason to re-count the primitive: the **typing clause** — the synthesis output header carries `{aggregation_rule, axioms_dropped, declared_authority}` (The Dropped Axiom's contract), and the **window clause** — a synthesis reading bounded lookback emits a window manifest joinable to its claims (The Declared Window's contract). "Composes with everything" is retired; the composition contracts in the v5.1 final govern.

### Marianne Score Structure

```yaml
movements:
  1: { name: prepare }
  2: { name: analyze, voices: 6 }
  3: { name: synthesize }

sheet:
  size: 1
  total_items: 3                    # three movements; expansion yields 8 sheets
  fan_out: { 2: 6 }
  dependencies: { 2: [1], 3: [2] }
  per_sheet_fallbacks:
    8: []                           # movement 3 = sheet 8; the merge does not degrade

prompt:
  template: |
    {% if stage == 1 %}
    Define scope. Write {{ workspace }}/scope.md and the partition map.
    {% elif stage == 2 %}
    Analyze partition {{ instance }} of {{ voice_count }}. Write
    {{ workspace }}/analysis-{{ instance }}.md with an input_type header row.
    {% else %}
    Read all analysis files. Your output header MUST carry aggregation_rule,
    axioms_dropped, declared_authority. Write {{ workspace }}/synthesis.md.
    {% endif %}

validations:
  - type: command_succeeds
    command: 'test $(ls {workspace}/analysis-*.md | wc -l) -eq 6'
    condition: "stage == 2"
  - type: content_contains
    path: "{workspace}/synthesis.md"
    pattern: "aggregation_rule:"
    condition: "stage == 3"
```

Note what the review forced: the fan-out completeness check asserts **exactly six** files once, after movement 2's sheets have run — not "at least four" mid-fan-out, which fails the first several sheets (Review 1's finding that validations run per expanded sheet).

---

## The Validity Window

```yaml
---
name: "The Validity Window"
scale: foundational
status: working
forces: ["Information Asymmetry", "Accumulated Signal"]
generators: ["Threshold-Triggered Switch"]
problem: "Pipelines hold expirable state — tokens, permits, freshness-bound context, generated datasets — and silently reuse it after it expires."
signals:
  - "state whose safety or truth depends on when it was created"
  - "a TTL, freshness bound, or maturity threshold mentioned only in prose"
  - "retry or resume paths that re-present old artifacts"
stages:
  - name: "stamp"
    sheets: 1
    instrument_guidance: "instrument: cli — the creation event writes the clock; nothing else may"
    fallback_friendly: false
    purpose: "Write {window_id, subject_digest, issued_at, expires_at, handler} atomically."
  - name: "probe"
    sheets: 1
    instrument_guidance: "instrument: cli — measures monotone accumulation when readiness is not wall-clock"
    fallback_friendly: false
    purpose: "Append measured maturity units to the accumulation ledger."
  - name: "gate"
    sheets: 1
    instrument_guidance: "instrument: cli — the two-sided window arithmetic in one transaction"
    fallback_friendly: false
    purpose: "Decide valid | expired→regenerate | degraded, adjacent to the consumer."
  - name: "consume"
    sheets: 1
    instrument_guidance: "any — works under the window the gate admitted"
    fallback_friendly: true
    purpose: "Consume the artifact, citing the window id in the output header."
dependencies:
  probe: ["stamp"]
  gate: ["stamp", "probe"]
  consume: ["gate"]
composes_with:
  - pattern: "The Gas-Free Certificate"
    how: "the destructive-boundary specialization — independence and digest binding added"
  - pattern: "The Declared Window"
    how: "the epistemic specialization — the window bounds claims, not safety"
  - pattern: "Effectivity Blocks"
    how: "generalizes it — config validity is one carrier of the window arithmetic"
---
```

**Source:** minted iteration 6 from convergence C9's carriers (Builder, Reasoner, Commander, Gardener); survived all three reviews with the transition table demanded by Reviews 1 and 2 added.

### Core Dynamic

A validity interval measured from a creation event, whose crossing forces regeneration or degradation — never silent reuse. The arithmetic is one discipline across carriers: a creation event stamps a clock; crossing the clock is an *event with a defined handler*; the handler regenerates or degrades. **The transition table (Reviews 1 and 2):**

| State | Entry condition | Handler |
|---|---|---|
| `stamped` | creation event wrote `{window_id, subject_digest, issued_at, expires_at, handler}` | artifact usable only via `valid` |
| `valid` | now ∈ [issued_at + min_age, expires_at) **and** maturity ≥ floor | consumer admitted; consumer must cite `window_id` |
| `expired` | now ≥ expires_at, or maturity probe red under min-age backstop | **fail forward to regeneration**: a NEW window id, never re-presentation of the same bytes |
| `regenerated` | gate re-stamped within its own transaction | old id lands on a revocation list; any input containing it fails the join |
| `degraded` | handler declares degradation instead | tier label written to the window report; the run proceeds at declared lower force |

**Precedence (Review 1):** minimum age gates entry, expiry gates exit, accumulated maturity is a *parallel* readiness channel measured by monotone accumulation (not every day is a day) with the minimum-age backstop surviving a green probe. **Adjacency (Review 1):** the gate movement runs immediately before the consumer — never validated a sheet after consumption — and the consumer cites the window id, so a stale id appearing in any consumer input is a join failure, not a prose hope.

### Marianne Score Structure

```yaml
movements:
  1: { name: stamp, instrument: cli, instrument_fallbacks: [] }
  2: { name: probe, instrument: cli, instrument_fallbacks: [] }
  3: { name: gate, instrument: cli, instrument_fallbacks: [] }
  4: { name: consume }

sheet:
  size: 1
  total_items: 4
  dependencies: { 2: [1], 3: [1, 2], 4: [3] }
  per_sheet_fallbacks:
    1: []
    2: []
    3: []

prompt:
  variables: { ttl_minutes: 90, min_age_seconds: 30 }
  template: |
    {% if stage == 1 %}
    bash "{score_dir}/scripts/window.sh" stamp --subject "{{ workspace }}/artifact.bin" \
      --ttl-minutes {{ ttl_minutes }} --min-age {{ min_age_seconds }} --emit "{{ workspace }}/window.json"
    {% elif stage == 2 %}
    bash "{score_dir}/scripts/window.sh" probe --maturity-ledger "{{ workspace }}/maturity.jsonl" --append
    {% elif stage == 3 %}
    bash "{score_dir}/scripts/window.sh" gate "{{ workspace }}/window.json" \
      --maturity "{{ workspace }}/maturity.jsonl" --regenerate-on-expiry
    {% else %}
    Consume the artifact. Your output header MUST cite window_id from
    {{ workspace }}/window.json. Report generation is forbidden without it.
    {% endif %}

validations:
  - type: command_succeeds
    command: 'bash {score_dir}/scripts/window.sh --self-test'   # stale fixture must fail; green-under-min-age must fail
    condition: "stage == 3"
  - type: command_succeeds
    command: 'bash {score_dir}/scripts/window.sh gate {workspace}/window.json --check-only'
    condition: "stage == 4"
  - type: content_contains
    path: "{workspace}/output.md"
    pattern: "window_id:"
    condition: "stage == 4"
```

The negative controls run in `--self-test`: a stale window must fail the gate and produce a new id; a green probe under minimum age must fail. The stale id must never appear in a consumer input — the join is `window.sh audit`'s job in any downstream score.

### Example

A long migration pipeline using 60-minute cloud tokens: each stage batch-refreshes and stamps; the probe actually authenticates a synthetic request; the gate passes only inside the window. When stage four overruns, the gate routes to re-batch inside its own transaction instead of letting stage five discover a 401 mid-flight.

---

## The Freeze (Lock-as-Interface)

```yaml
---
name: "The Freeze"
scale: foundational
status: working
forces: ["Exponential Defect Cost", "Producer-Consumer Mismatch"]
generators: ["Contract at Interfaces"]
problem: "Downstream work starts against upstream structure that is still moving, so finishers build on a version that stops existing."
signals:
  - "parallel specialists blocked on a structure still under negotiation"
  - "re-deciding structure later costs multiples of deciding it now"
  - "post-freeze edits arriving silently instead of as visible amendments"
stages:
  - name: "propose"
    sheets: "fan_out(3)"
    instrument_guidance: "any — pitches complete structures with stable element ids"
    fallback_friendly: true
    purpose: "Propose complete candidate structures with stable BEAT-xx identifiers."
  - name: "lock"
    sheets: 1
    instrument_guidance: "instrument: cli — the appointed convergence authority's decision, executed deterministically"
    fallback_friendly: false
    purpose: "Write frozen structure + digest; one hash becomes the interface."
  - name: "specialize"
    sheets: "fan_out(3)"
    instrument_guidance: "any — each receives the frozen artifact by required cadenza"
    fallback_friendly: true
    purpose: "Draft against the frozen structure, citing its digest."
  - name: "join-gate"
    sheets: 1
    instrument_guidance: "instrument: cli — sha256sum -c plus citation join"
    fallback_friendly: false
    purpose: "Reject any successor built on a different hash."
dependencies:
  lock: ["propose"]
  specialize: ["lock"]
  join-gate: ["specialize"]
composes_with:
  - pattern: "Fork-Evident History"
    how: "payload/substrate — the lock's digest is the chain's head"
  - pattern: "Prefabrication"
    how: "contrast — authored-in-advance contract with no discovery room; the Freeze has discovery then authority-declared termination"
  - pattern: "The Unprimed Falsifier"
    how: "the falsifier's evidence loop terminates in this lock, not in convergence"
---
```

**Source:** minted iteration 6 (convergence: iteration terminates by authority declaration, not convergence); survived review with the pin made expressible and the delivery made physical (Reviews 1, 2, 3).

### Core Dynamic

An artifact under negotiation becomes, by declaration, an **interface** — digest-named, delivered by required cadenza, consumed by parallel successors whose validity is a join against the digest. Transition rules: iteration terminates by *authority declaration* (an appointed convergence authority, not an elected one); the frozen thing is the spec that parallel specialization obeys; post-freeze change travels as visible amendment — a new digest that supersedes, never a silent edit of the frozen bytes. The reordering economics are the point: structure decided at the beat stage costs 10× less than at the prose stage.

**The pin, made expressible (Review 3):** `file_sha256` cannot verify a digest discovered at runtime — it requires a literal 64-hex at authorship. The lock movement writes `frozen.sha256`; every consumer-side check is `sha256sum -c` inside a `command_succeeds`. **The delivery, made physical (Reviews 1 and 2):** the frozen artifact reaches each specialist as a **required cadenza keyed to its expanded sheet number** — absent file, failed sheet, no specialist improvises against a structure it never received.

### Marianne Score Structure

```yaml
movements:
  1: { name: propose, voices: 3 }
  2: { name: lock, instrument: cli, instrument_fallbacks: [] }
  3: { name: specialize, voices: 3 }
  4: { name: join-gate, instrument: cli, instrument_fallbacks: [] }

sheet:
  size: 1
  total_items: 4                     # expansion: 1-3 propose, 4 lock, 5-7 specialize, 8 join
  fan_out: { 1: 3, 3: 3 }
  dependencies: { 2: [1], 3: [2], 4: [3] }
  cadenzas:
    5:
      - file: "{{ workspace }}/frozen/structure.yaml"
        as: context
        required: true
    6:
      - file: "{{ workspace }}/frozen/structure.yaml"
        as: context
        required: true
    7:
      - file: "{{ workspace }}/frozen/structure.yaml"
        as: context
        required: true
  per_sheet_fallbacks:
    4: []
    8: []

prompt:
  template: |
    {% if stage == 1 %}
    Propose a complete structure with stable BEAT-xx identifiers for your pitch.
    Write {{ workspace }}/pitch-{{ instance }}.yaml.
    {% elif stage == 2 %}
    bash "{score_dir}/scripts/lock.sh" --pitches "{{ workspace }}/pitch-*.yaml" \
      --emit "{{ workspace }}/frozen/structure.yaml" --digest "{{ workspace }}/frozen.sha256"
    {% elif stage == 3 %}
    Draft your section against the frozen structure you received. Cite its digest
    (from frozen.sha256) in your output header. Write {{ workspace }}/draft-{{ instance }}.md.
    {% else %}
    bash "{score_dir}/scripts/freeze-join.sh" "{{ workspace }}/draft-*.md" --against "{{ workspace }}/frozen.sha256"
    {% endif %}

validations:
  - type: command_succeeds
    command: 'cd {workspace} && sha256sum -c frozen.sha256'
    condition: "stage == 3"
  - type: command_succeeds
    command: 'bash {score_dir}/scripts/freeze-join.sh {workspace}/draft-1.md {workspace}/draft-2.md {workspace}/draft-3.md --against {workspace}/frozen.sha256'
    condition: "stage == 4"
  - type: content_contains
    path: "{workspace}/draft-1.md"
    pattern: "structure-digest:"
    condition: "stage == 3"
```

The join gate rejects any successor built on a different hash — drift, not opinion, kills the stale finisher. A late scoped-delta pass (the Punch-Up form) re-enters through a new lock: add-only over the frozen spine, with the gate proving the structure delta is zero and the prose delta positive.

### Example

A six-chapter onboarding guide: three pitching sheets propose incompatible orderings; the lock freezes one beat shape; three drafting sheets write against it, each receiving it by cadenza; the gate rejects any chapter whose headings drift from the locked sequence. A readability pass lands as an amendment with a new digest, visibly superseding.

---

## Typed Force (narrowed)

```yaml
---
name: "Typed Force"
scale: foundational
status: working
forces: ["Structured Disagreement", "Information Asymmetry"]
generators: ["Contract at Interfaces"]
problem: "Authority-carrying and claim-carrying objects flow through pipelines without a type a gate can join on, so binding decisions and persuasive suggestions enforce identically."
signals:
  - "downstream consumers behave differently depending on what kind of thing this is, but the kind is not a field"
  - "a decision record indistinguishable from an observation"
  - "an aggregation presented as neutral"
stages:
  - name: "emit-typed"
    sheets: 1
    instrument_guidance: "any — emits objects whose force field is assigned by a NAMED authority"
    fallback_friendly: true
    purpose: "Produce decision/claim objects carrying {force, assigned_by} at creation."
  - name: "typecheck"
    sheets: 1
    instrument_guidance: "instrument: cli — joins on the type, never judges the type"
    fallback_friendly: false
    purpose: "Enforce type-selects-rule and visible retyping; reject untyped and unassigned rows."
dependencies:
  typecheck: ["emit-typed"]
composes_with:
  - pattern: "The Precedent Bench"
    how: "its authority form — binding/persuasive force over decisions"
  - pattern: "The Dropped Axiom"
    how: "its fan-in form — aggregation headers over merges"
  - pattern: "Proof-Carrying Artifact"
    how: "its evidence form — admissibility typing over artifacts (v5.1)"
---
```

**Source:** minted iteration 6; **narrowed by review** — Review 1's umbrella-cut is answered by delegation (below), Review 2's syntax/authority split is executed as the `assigned_by` provenance field.

### Core Dynamic

Untyped authority is vibes; untyped claims are furniture. The law is four transitions, no more: **(1) type at creation** — an object carries its force field when emitted, not when disputed; **(2) the type is assigned by a named authority** — `assigned_by` is a provenance field a gate can check; the gate checks syntax and provenance and *never* the truth of the assignment, which belongs to the assigning authority and is contested through that authority's own motion procedure; **(3) the type selects the enforcement rule** — bind/persuade, admit/quarantine, fund-acquisition-only, demote; **(4) retyping is visible** — supersession or demotion edges, never silent edits.

What the draft's umbrella claimed and this narrowing delegates: legal force semantics → The Precedent Bench; fan-in aggregation typing → The Dropped Axiom; evidence admissibility → Proof-Carrying Artifact; allocation provenance → archive. The law is the shared discipline those patterns specialize.

### Marianne Score Structure

```yaml
movements:
  1: { name: emit-typed }
  2: { name: typecheck, instrument: cli, instrument_fallbacks: [] }

sheet:
  size: 1
  total_items: 2
  dependencies: { 2: [1] }
  per_sheet_fallbacks:
    2: []

prompt:
  template: |
    {% if stage == 1 %}
    Produce the decision artifact {{ workspace }}/decision.jsonl. Every row MUST carry
    force ∈ {binding, persuasive} and assigned_by: <authority-id>, set at creation.
    Aggregations additionally carry {aggregation_rule, axioms_dropped, declared_authority}.
    {% else %}
    python3 "{score_dir}/scripts/force-typecheck.py" "{{ workspace }}/decision.jsonl"
    {% endif %}

validations:
  - type: command_succeeds
    command: 'python3 {score_dir}/scripts/force-typecheck.py {workspace}/decision.jsonl'
    condition: "stage == 2"
  - type: content_regex
    pattern: "force: (binding|persuasive)"
    path: "{workspace}/decision.jsonl"
    condition: "stage == 2"
  - type: content_contains
    path: "{workspace}/decision.jsonl"
    pattern: "assigned_by:"
    condition: "stage == 2"
```

The typechecker enforces the bijection — rule ∈ the shared demotion ladder `{majority, weighted-correlation, editorial-with-dissents, refusal}` ⟺ the matching `axioms_dropped` declaration (Review 3's enum mismatch fixed by sharing one ladder with Condorcet's Premise) — and rejects any row whose `assigned_by` is empty or unknown.

### Example

A refactoring campaign's early scores decided "no new dependencies," "errors at exit 0 are still failing." Typed as holdings, they bind later scores until explicitly overruled; a later score wanting a new dependency files a typed motion — distinguish or overrule — and the citation gate catches an un-overruled contradiction deterministically.

---

## The Write-Time Record

```yaml
---
name: "The Write-Time Record"
scale: foundational
status: working
forces: ["Partial Failure", "Information Asymmetry"]
generators: ["Accumulate Knowledge"]
problem: "Obligations and provenance are reconstructed by archaeology at end-of-life, after the people and context that created them are gone."
signals:
  - "provisioning creates removal obligations nobody writes down"
  - "a teardown plan that begins with 'figure out what we created'"
  - "a manifest written from memory at the end of a campaign"
stages:
  - name: "plan-effects"
    sheets: 1
    instrument_guidance: "any — plans effects as typed rows with stable effect ids"
    fallback_friendly: true
    purpose: "Emit effects-plan.jsonl: {effect_id, kind, command, decommission_cmd}."
  - name: "transact"
    sheets: 1
    instrument_guidance: "instrument: cli — ONE process writes intent row, executes effect, appends receipt"
    fallback_friendly: false
    purpose: "Atomic per-effect transaction; idempotent by effect_id; fail-closed on open rows."
  - name: "audit"
    sheets: 1
    instrument_guidance: "instrument: cli — three-way join with empty residue"
    fallback_friendly: false
    purpose: "row ↔ receipt ↔ settlement join; open rows or unmatched receipts fail."
dependencies:
  transact: ["plan-effects"]
  audit: ["transact"]
composes_with:
  - pattern: "Demobilization Checkout"
    how: "its consumption side — the demob census reads the record as its work list"
  - pattern: "Fork-Evident History"
    how: "payload/substrate — the record rides the append-only chain"
  - pattern: "Vintage Overlay"
    how: "the vintage record is its run-level instance"
---
```

**Source:** minted iteration 6; Reviews 1 and 2 demanded atomicity — the draft's three loosely sequenced stages allowed a row to exist while the effect failed, changed target, or ran twice. This structure closes that window.

### Core Dynamic

Obligations and provenance are recorded at the moment the obligation is created — not discovered by archaeology at the end. The ship carries its Inventory of Hazardous Materials from keel-laying, so the demolition contractor's work list is written by the builder years before the dismantler exists. **The atomicity rule (Reviews 1 and 2):** intent row, effect, and receipt commit inside **one CLI process**, keyed by a stable `effect_id`: the transact wrapper appends the intent row, executes the command, and appends the receipt — `{effect_id, exit_code, settled_at}` — in a single invocation. A crash between intent and receipt leaves an **open row**, and open rows fail the audit (fail-closed, never silently carried). A re-run with the same `effect_id` detects the prior state and refuses double-execution: unstarted rows re-run; started-unsettled rows stop for inspection; settled rows are joined, never repeated. Recovery semantics per transition, as Review 1 required.

This is Legion's own first law — disk over memory — discovered independently by every mature coordination domain: the only honest moment to record a promise is the moment it is made, and a manifest written at end-of-life from memory is exactly the survivor-testimony failure the record exists to prevent.

### Marianne Score Structure

```yaml
movements:
  1: { name: plan-effects }
  2: { name: transact, instrument: cli, instrument_fallbacks: [] }
  3: { name: audit, instrument: cli, instrument_fallbacks: [] }

sheet:
  size: 1
  total_items: 3
  dependencies: { 2: [1], 3: [2] }
  per_sheet_fallbacks:
    2: []
    3: []

prompt:
  template: |
    {% if stage == 1 %}
    Plan the effects. Write {{ workspace }}/effects-plan.jsonl, one row per effect:
    {effect_id, kind, command, decommission_cmd}. effect_id is stable and unique.
    {% elif stage == 2 %}
    bash "{score_dir}/scripts/effects.sh" transact --plan "{{ workspace }}/effects-plan.jsonl" \
      --ledger "{{ workspace }}/disposal-ledger.jsonl"
    {% else %}
    bash "{score_dir}/scripts/effects.sh" audit --ledger "{{ workspace }}/disposal-ledger.jsonl" --require-empty-residue
    {% endif %}

validations:
  - type: command_succeeds
    command: 'bash {score_dir}/scripts/effects.sh --self-test'
    condition: "stage == 2"
  - type: command_succeeds
    command: 'bash {score_dir}/scripts/effects.sh audit --ledger {workspace}/disposal-ledger.jsonl --require-empty-residue'
    condition: "stage == 3"
```

The self-test is the negative control Review 1 required for every destructive pattern: a fixture row that fails mid-transaction must leave an open row that `audit` rejects, and a re-presented settled id must be refused.

### Example

A two-year research campaign provisions buckets, service accounts, webhooks, and model artifacts across four clouds, each through the transact wrapper. Funding ends: the decommission score reads the ledger as its sole work list — newest-first, by `effect_id` — drains, deletes, and revokes every row, and emits a completion certificate the day the grant closes. No console archaeology, no forgotten webhook.

---
# Communication Patterns

*Three enter — the per-consumer projection, the measured jury, and the window-honesty contract. Calling the Show awaits primitives; Command by Negation is an idiom under Mission Command.*

## Monitor Mix

```yaml
---
name: "Monitor Mix"
scale: communication
status: working
forces: ["Information Asymmetry", "Finite Resources"]
generators: ["Contract at Interfaces"]
problem: "Many consumers need different slices of one shared accumulating state, and each currently receives either everything or someone else's slice."
signals:
  - "one shared state, many consumers with genuinely different depth needs"
  - "a summarizer drowning in function bodies; an implementer starved of them"
  - "routing decisions made ad hoc per run instead of written down"
stages:
  - name: "channel-inventory"
    sheets: 1
    instrument_guidance: "instrument: cli — enumerate the channels; no opinions"
    fallback_friendly: false
    purpose: "Emit channels.yaml from the actual shared state."
  - name: "assemble"
    sheets: 1
    instrument_guidance: "instrument: cli — applies the versioned mixdown prescription"
    fallback_friendly: false
    purpose: "Project per-consumer mixes under char budgets; refuse union-over-source."
  - name: "line-check"
    sheets: 1
    instrument_guidance: "instrument: cli — per-consumer liveness and budget sweep"
    fallback_friendly: false
    purpose: "Every mix has every required channel within budget, before doors."
  - name: "perform"
    sheets: "fan_out(3)"
    instrument_guidance: "per consumer role; each receives ONLY its mix by required cadenza"
    fallback_friendly: true
    purpose: "Perform the consumer role from the mix, citing its mix id."
dependencies:
  assemble: ["channel-inventory"]
  line-check: ["assemble"]
  perform: ["line-check"]
composes_with:
  - pattern: "Relay Zone"
    how: "layering — route per consumer first, then compress a mix that would drown its consumer"
  - pattern: "The Declared Window"
    how: "the mix manifest is the delivery receipt the window contract joins against"
---
```

**Source:** Expedition 3; survived review with delivery enforced and isolation made physical (Reviews 1 and 2).

### Core Dynamic

One shared state, many ears, and no ear wants all of it. Same channels, different gains, different destinations — and the mixing decisions are *routing* decisions, made once, written down as a versioned prescription, and checked by a deterministic sweep before the run starts. Distinct from Relay Zone (compresses the stream's *size*) and Screening Cascade (filters items by escalation): Monitor Mix changes each consumer's **view**, and the mix is a first-class artifact. The line check — every channel in every mix, before doors — is a per-consumer liveness sweep: a consumer whose mix is dead does not perform.

**Delivery enforced (Reviews 1 and 2):** `spec_tags` cannot route a distinct file per fan-out instance, but **cadenzas keyed on expanded sheet numbers can** — each performer's cadenza injects exactly its mix, `required: true`, path templated on `{{ instance }}`. Consumers never read raw channels; the prescription's union-over-source refusal is checked in assembly (a prescription whose mixes exceed the source is amplification, not mixing — it exits non-zero).

### Marianne Score Structure

```yaml
movements:
  1: { name: channel-inventory, instrument: cli, instrument_fallbacks: [] }
  2: { name: assemble, instrument: cli, instrument_fallbacks: [] }
  3: { name: line-check, instrument: cli, instrument_fallbacks: [] }
  4: { name: perform, voices: 3 }

sheet:
  size: 1
  total_items: 4                    # expansion: 1,2,3 then perform = sheets 4,5,6
  fan_out: { 4: 3 }
  dependencies: { 2: [1], 3: [2], 4: [3] }
  cadenzas:
    4:
      - file: "{{ workspace }}/mixes/consumer-{{ instance }}.md"
        as: context
        required: true
    5:
      - file: "{{ workspace }}/mixes/consumer-{{ instance }}.md"
        as: context
        required: true
    6:
      - file: "{{ workspace }}/mixes/consumer-{{ instance }}.md"
        as: context
        required: true
  per_sheet_fallbacks:
    1: []
    2: []
    3: []

prompt:
  template: |
    {% if stage == 1 %}
    bash "{score_dir}/scripts/mix.sh" channels --from "{{ workspace }}/shared/" --emit "{{ workspace }}/channels.yaml"
    {% elif stage == 2 %}
    bash "{score_dir}/scripts/mix.sh" assemble --channels "{{ workspace }}/channels.yaml" \
      --prescription "{score_dir}/mixdown.yaml" --out "{{ workspace }}/mixes/"
    {% elif stage == 3 %}
    bash "{score_dir}/scripts/mix.sh" line-check --dir "{{ workspace }}/mixes/" --against "{score_dir}/mixdown.yaml"
    {% else %}
    You receive ONLY your mix file. Perform your consumer role from it.
    Cite mix id and its channels in your output header.
    {% endif %}

validations:
  - type: command_succeeds
    command: 'bash {score_dir}/scripts/mix.sh line-check --dir {workspace}/mixes --against {score_dir}/mixdown.yaml'
    condition: "stage == 3"
  - type: content_contains
    path: "{workspace}/consumer-outputs/out-1.md"
    pattern: "mix:"
    condition: "stage == 4"
```

The negative control is a line-check fixture: a mix missing a required channel must fail the sweep before any performer runs.

### Example

An incident postmortem: one timeline, three readers. The executive mix: impact counts, deltas, recovery timestamps. The engineer's mix: full command logs and stack traces. Compliance: the custody sequence with seal references. Same channels, three mixes under budget — and the line check guarantees nobody performs without their required channels.

---

## Condorcet's Premise (Independence Audit)

```yaml
---
name: "Condorcet's Premise"
scale: communication
status: working
forces: ["Structured Disagreement"]
generators: ["Verify through Diverse Observers"]
problem: "Voting authority is assumed from panel size, but correlated panels ratify errors with majority confidence instead of averaging them out."
signals:
  - "a fan-in that will vote, over claims that cannot be mechanically reconstructed"
  - "a 'vendor-diverse' claim never family-probed"
  - "n reviewers from what turns out to be one model family"
stages:
  - name: "calibrate"
    sheets: "fan_out(3)"
    instrument_guidance: "three instruments on three expanded sheets via per_sheet_instruments; one per vendor family"
    fallback_friendly: true
    purpose: "Answer pre-authored calibration items with known ground truth."
  - name: "census"
    sheets: 1
    instrument_guidance: "instrument: cli — computes the co-occurrence matrix, design effect, family census, and demotion"
    fallback_friendly: false
    purpose: "Emit panel-manifest.yaml: {rho_bar, n_eff, family_census[], aggregation_rule_demoted_to}."
  - name: "panel"
    sheets: "fan_out(3)"
    instrument_guidance: "same three instruments, same assignment rule as calibration"
    fallback_friendly: true
    purpose: "Work the real task under the demoted aggregation rule."
  - name: "audit"
    sheets: 1
    instrument_guidance: "instrument: cli — joins the verdict's cited rule against the manifest"
    fallback_friendly: false
    purpose: "No vote ships before its own audit passes."
dependencies:
  census: ["calibrate"]
  panel: ["census"]
  audit: ["panel"]
composes_with:
  - pattern: "The Skeptical Oracle"
    how: "complement — reconstruct when possible; audit the jury when not"
  - pattern: "Rashomon Gate"
    how: "layering — frames are jurors; the gate's synthesis demotes by measured dependence"
  - pattern: "The Dropped Axiom"
    how: "the demotion ladder is Typed Force's shared enum"
---
```

**Source:** Expedition 4; survived review with the estimator defined and bounded, the calibration sourced, and the routing made loadable (Reviews 1, 2, 3).

### Core Dynamic

The jury theorem is a contract with two clauses and people only ever read one: majority voting converges on truth as the panel grows **if** each juror is better than a coin flip **and** their errors are independent. The second clause is load-bearing — correlated voters do not average out their errors, they *ratify* them with the confidence of a majority. AI ensembles fail exactly here: same vendor family, same training blind spots, same prompt scaffold — prompt correlation is juror correlation.

**The estimator, defined and bounded (Review 2):** over K calibration items with known answers, compute the full pairwise error co-occurrence matrix M (i,j) = P(jurors i and j both wrong); report ρ̄ = mean of off-diagonal entries and the design effect n/(1+(n−1)ρ̄) as an **equicorrelation upper bound** — a heterogeneous matrix is not safely reducible to one number, so M rides the manifest as data and the bound is labeled an approximation. Missing answers count as errors (declared, not silent). **Calibration sourcing (Reviews 1 and 3):** the fixture is pre-authored in the score directory with ground truth recorded at authorship — seeded items whose answers the run cannot influence. **Family diversity is provenance, not independence (Review 1):** `family_source` stamped from a live `mzt config` probe tells you the census; only measured error behavior tells you the dependence. The demotion ladder — majority → weighted-correlation → editorial-with-dissents → refusal — is selected by the measured bound, and the audit joins the verdict's *cited* rule against the manifest's *demoted* rule. A silent majority over a correlated panel is the failure; the demotion is not.

### Marianne Score Structure

```yaml
instruments:
  a: { profile: claude-code }
  b: { profile: codex-cli }
  c: { profile: opencode, config: { model: "zai-coding-plan/glm-5.3-flash" } }

movements:
  1: { name: calibrate, voices: 3 }
  2: { name: census, instrument: cli, instrument_fallbacks: [] }
  3: { name: panel, voices: 3 }
  4: { name: audit, instrument: cli, instrument_fallbacks: [] }

sheet:
  size: 1
  total_items: 4                    # expansion: calibrate 1-3, census 4, panel 5-7, audit 8
  fan_out: { 1: 3, 3: 3 }
  dependencies: { 2: [1], 3: [2], 4: [3] }
  per_sheet_instruments:            # expanded-sheet-keyed; one sheet, one instrument
    1: a
    2: b
    3: c
    5: a
    6: b
    7: c
  per_sheet_fallbacks:
    4: []
    8: []

prompt:
  template: |
    {% if stage == 1 %}
    Answer the calibration items at "{score_dir}/calibration/items.jsonl". Write
    {{ workspace }}/calibration/answers-{{ instance }}.jsonl. Ground truth is NOT
    available to you; answer honestly and briefly.
    {% elif stage == 2 %}
    bash "{score_dir}/scripts/census.sh" --answers "{{ workspace }}/calibration/" \
      --ground-truth "{score_dir}/calibration/ground-truth.jsonl" \
      --emit "{{ workspace }}/panel-manifest.yaml"
    {% elif stage == 3 %}
    Work the panel task. The aggregation rule recorded in
    {{ workspace }}/panel-manifest.yaml governs your merge; cite it.
    {% else %}
    bash "{score_dir}/scripts/demote.sh" --manifest "{{ workspace }}/panel-manifest.yaml" \
      --verdict "{{ workspace }}/verdict.md"
    {% endif %}

validations:
  - type: command_succeeds
    command: 'bash {score_dir}/scripts/census.sh --self-test'
    condition: "stage == 2"
  - type: command_succeeds
    command: 'bash {score_dir}/scripts/demote.sh --manifest {workspace}/panel-manifest.yaml --verdict {workspace}/verdict.md'
    condition: "stage == 4"
```

The self-test fixture is a synthetic three-juror panel with planted co-occurring errors: the census must demote it to editorial-with-dissents or refusal, and a verdict citing `majority` over it must fail the audit.

### Example

A hospital quality committee fans an incident summary to three external review services for severity verdicts. Two quietly run the same underlying model. The census on ten seeded incidents shows errors co-occurring at ρ̄ ≈ 0.5 — three letterheads, one review — and the aggregation is demoted to argued editorial with recorded dissents before anyone votes on anything real.

---

## The Declared Window (Bounded-Context Honesty)

```yaml
---
name: "The Declared Window"
scale: communication
status: working
forces: ["Information Asymmetry"]
generators: ["Accumulate Knowledge"]
problem: "Synthesis sheets read bounded lookback over large runs and then make global claims their window cannot support."
signals:
  - "streak/trend/consensus language in late sheets ('consistently', 'across the run', 'no objections')"
  - "a truncation whose consumers quote 'the' upstream output"
  - "an honest approximation available but a silent exact-looking guess chosen instead"
stages:
  - name: "work"
    sheets: "fan_out(4)"
    instrument_guidance: "any — writes instance-tagged artifacts"
    fallback_friendly: true
    purpose: "Produce the artifacts the window will bound."
  - name: "window-manifest"
    sheets: 1
    instrument_guidance: "instrument: cli — writes the manifest from the run's ACTUAL cross_sheet config and artifacts"
    fallback_friendly: false
    purpose: "Emit {window_span, exact_in_window, total_items_seen, window: full|partial}."
  - name: "bounded-synthesis"
    sheets: 1
    instrument_guidance: "strong reasoner — every claim tagged, structured ledger emitted"
    fallback_friendly: false
    purpose: "Synthesize with a structured claim ledger joinable to the manifest."
  - name: "join-gate"
    sheets: 1
    instrument_guidance: "instrument: cli — ledger arithmetic and span join"
    fallback_friendly: false
    purpose: "exact_in_window + refused = claims_emitted; every global claim has a row."
dependencies:
  window-manifest: ["work"]
  bounded-synthesis: ["work", "window-manifest"]
  join-gate: ["bounded-synthesis"]
composes_with:
  - pattern: "The Black-Box Ledger"
    how: "bounded capture is the window; the manifest is the claim contract over that bound"
  - pattern: "Hutchinson's Warning"
    how: "complement — density control vs claim honesty: the two halves of bounded context"
---
```

**Source:** Expedition 4; survived review with the word ban replaced by a structured claim ledger (Reviews 1 and 2).

### Core Dynamic

`lookback_sheets` and `max_output_chars` are not hygiene; they are a sliding window over an unbounded artifact stream, and every downstream sheet consuming bounded context stands where the streaming engineers stood — except the engineers knew it. The epistemic rule: from a window you may make **windowed claims** (exact within the window, or approximated with a declared ε) and **counted-total claims** (I saw K items, I read W), but not **global claims** — "all prior findings agree," "no earlier stage contradicts this" — because the window's boundary is also the boundary of your knowledge. **The correction the reviews forced:** a prose word-ban ("all", "never") is easy to evade and produces false positives; the contract is now a **structured claim ledger** — the synthesizer emits `claims.jsonl` rows `{claim_id, text, class ∈ {in-window, total-seen, refused}, window_id}` — and a CLI movement writes the window manifest from the run's *actual* configuration and artifacts, so the manifest is a delivery fact, not a belief. The join gate asserts the arithmetic (`exact_in_window + refused = claims_emitted`) and that every global-quantifier sentence in the synthesis has a ledger row with an honest class. An honest (1±ε) answer with ε in the output is a *stronger* artifact than a silent exact-looking guess.

**The corpus honesty rule (from Cluster Lead's archive, promoted per Review 3):** a coordination artifact whose inputs are incomplete publishes the incompleteness — "coverage unknown," "prior weeks unqueried" — never a manufactured success.

One engine fact baked in: `lookback_sheets: 0` means **all** completed sheets, not none — context austerity uses a small positive bound, and the manifest states which.

### Marianne Score Structure

```yaml
cross_sheet:
  lookback_sheets: 5
  max_output_chars: 4000

movements:
  1: { name: work, voices: 4 }
  2: { name: window-manifest, instrument: cli, instrument_fallbacks: [] }
  3: { name: bounded-synthesis }
  4: { name: join-gate, instrument: cli, instrument_fallbacks: [] }

sheet:
  size: 1
  total_items: 4                    # expansion: work 1-4, manifest 5, synthesis 6, gate 7
  fan_out: { 1: 4 }
  dependencies: { 2: [1], 3: [1, 2], 4: [3] }
  per_sheet_fallbacks:
    5: []
    6: []
    7: []

prompt:
  template: |
    {% if stage == 1 %}
    Work your slice. Write {{ workspace }}/work-{{ instance }}.md.
    {% elif stage == 2 %}
    bash "{score_dir}/scripts/window.sh" manifest --lookback 5 --workspace "{{ workspace }}" \
      --emit "{{ workspace }}/window-manifest.yaml"
    {% elif stage == 3 %}
    Synthesize from the visible window. Write {{ workspace }}/synthesis.md AND
    {{ workspace }}/claims.jsonl — one row per claim: {claim_id, text,
    class: in-window|total-seen|refused, window_id}. Tag every global claim honestly.
    {% else %}
    bash "{score_dir}/scripts/claims.sh" join --manifest "{{ workspace }}/window-manifest.yaml" \
      --claims "{{ workspace }}/claims.jsonl" --prose "{{ workspace }}/synthesis.md"
    {% endif %}

validations:
  - type: command_succeeds
    command: 'bash {score_dir}/scripts/claims.sh join --manifest {workspace}/window-manifest.yaml --claims {workspace}/claims.jsonl --prose {workspace}/synthesis.md'
    condition: "stage == 4"
  - type: content_contains
    path: "{workspace}/synthesis.md"
    pattern: "window:"
    condition: "stage == 3"
```

### Example

A season-long advisory concert synthesizes weekly scouting reports; by week 20 the synthesis sheet sees only the last 5 sheets. When it writes "pest pressure has been consistently low," the ledger forces the sentence to carry its own boundary — "consistently low across the visible five weeks; prior weeks unqueried" — and the extension service publishes a claim it can actually defend.

---

# Score-Level Patterns

*Two enter — the destructive-boundary permit and the structure-ordered removal. Relieving the Watch and the Strike Clock await primitives.*

## The Gas-Free Certificate

```yaml
---
name: "The Gas-Free Certificate"
scale: score-level
status: working
forces: ["Partial Failure", "Exponential Defect Cost"]
generators: ["Gate on Environmental Readiness"]
problem: "Destructive operations run on the strength of a check that passed earlier, against a world that has since moved."
signals:
  - "rm, force-push, schema-drop, secret-revoke, teardown ahead"
  - "'the check passed earlier' is load-bearing for something irreversible"
  - "a retried or resumed run about to reuse yesterday's verification"
stages:
  - name: "certify"
    sheets: 1
    instrument_guidance: "instrument: cli, separately-committed certifier/ dir — independence is authored provenance"
    fallback_friendly: false
    purpose: "Write permit {target_digest, issued_at, expires_at, certifier_digest}."
  - name: "destroy"
    sheets: 1
    instrument_guidance: "instrument: cli wrapper — permit check AND destruction in ONE transaction; AI plans, wrapper executes"
    fallback_friendly: false
    purpose: "Refuse on stale/mismatched permit; execute only inside the same process that checked."
  - name: "record"
    sheets: 1
    instrument_guidance: "instrument: cli — ledger append, permit↔receipt join"
    fallback_friendly: false
    purpose: "The Write-Time Record's consumption side at the destructive boundary."
dependencies:
  destroy: ["certify"]
  record: ["destroy"]
composes_with:
  - pattern: "The Validity Window"
    how: "the destructive-boundary specialization — window + independence + digest binding"
  - pattern: "The Fencing Token"
    how: "substitution — pre-flight and cheap instead of rejection at the write boundary"
  - pattern: "Standby–GO"
    how: "contrast — the cue confirms receiver readiness; the permit confirms environment safety, and it decays"
---
```

**Source:** Expedition 1; Review 1 called its draft form "dangerously ordered" — destruction could precede or ignore the check. The fix is structural: **destruction is a command, so the whole pattern is CLI-native.**

### Core Dynamic

Before any torch touches steel near a tank, the yard obtains a certificate from a *competent person who is not the crew doing the burning* — and the certificate expires, and any interruption invalidates it, and resumption demands re-certification. Three load-bearing properties: **independence** (a separately-committed `certifier/` directory whose digest is recorded in the permit — independence is provenance, not a pathname); **freshness** (bounded validity from issuance — the Validity Window at its sharpest); **binding** (the permit names the exact target state by digest, so it cannot be replayed against different bytes). And the one the reviews forced: **check-and-act atomicity** — the destroy movement is a single CLI wrapper that verifies the permit (digest match, freshness) and executes the destruction in the same process; a failed check refuses with exit non-zero and nothing is destroyed. The AI sheet's role is upstream: planning what to destroy and why. It never presses the button, and no validation-after-the-fact pretends otherwise.

A retried or resumed run re-certifies, because interruption is itself evidence the world may have moved. A retry that reuses yesterday's gas-free check is the explosion.

### Marianne Score Structure

```yaml
movements:
  1: { name: plan-destruction }     # AI: what to destroy, why, with what command
  2: { name: certify, instrument: cli, instrument_fallbacks: [] }
  3: { name: destroy, instrument: cli, instrument_fallbacks: [] }
  4: { name: record, instrument: cli, instrument_fallbacks: [] }

sheet:
  size: 1
  total_items: 4
  dependencies: { 2: [1], 3: [2], 4: [3] }
  per_sheet_fallbacks:
    2: []
    3: []
    4: []

prompt:
  variables: { ttl_minutes: 30 }
  template: |
    {% if stage == 1 %}
    Plan the destruction. Write {{ workspace }}/plan.json: target path, the exact
    destructive command, rollback posture. Do NOT execute anything.
    {% elif stage == 2 %}
    bash "{score_dir}/certifier/gas-free.sh" --plan "{{ workspace }}/plan.json" \
      --ttl-minutes {{ ttl_minutes }} --emit "{{ workspace }}/permit.json"
    {% elif stage == 3 %}
    bash "{score_dir}/certifier/execute.sh" --permit "{{ workspace }}/permit.json" \
      --plan "{{ workspace }}/plan.json"
    {% else %}
    bash "{score_dir}/scripts/ledger.sh" append-permit "{{ workspace }}/permit.json" \
      --receipts "{{ workspace }}/receipts.jsonl"
    {% endif %}

validations:
  - type: command_succeeds
    command: 'bash {score_dir}/certifier/execute.sh --self-test'
    condition: "stage == 3"
  - type: command_succeeds
    command: 'bash {score_dir}/scripts/ledger.sh append-permit {workspace}/permit.json --receipts {workspace}/receipts.jsonl --require-join'
    condition: "stage == 4"
```

The self-test is the negative control Review 1 demanded reaches the real gate: a stale permit fixture and a mismatched-target fixture must both fail `execute.sh` with nothing destroyed.

### Example

A nightly maintenance score force-pushes a regenerated `gh-pages` site. The certify movement verifies branch head, worktree cleanliness, and build reproducibility, and writes a permit naming the exact tree hash. A human's emergency merge at 2 AM invalidates the permit silently and correctly — morning's run re-certifies instead of force-pushing over the emergency fix.

---

## Top-Down Demolition Order

```yaml
---
name: "Top-Down Demolition Order"
scale: score-level
status: working
forces: ["Exponential Defect Cost", "Partial Failure"]
generators: ["Gate on Environmental Readiness"]
problem: "Removal order is computed from commit history, so removing a shared thing succeeds while dependents that quietly stood on it lose their footing."
signals:
  - "retiring a shared library, column, endpoint, schema, or base image"
  - "the danger is not 'removal fails' but 'removal succeeds and three consumers break silently'"
  - "reverse-chronology undo proposed for something with internal structure"
stages:
  - name: "map-structure"
    sheets: 1
    instrument_guidance: "instrument: cli — computes the live reverse-dependency graph"
    fallback_friendly: false
    purpose: "Emit demolition-plan.json: ordered steps, each with a consumers-must-be-empty predicate."
  - name: "verify-order"
    sheets: 1
    instrument_guidance: "instrument: cli in separately-authored verify/ dir — re-derives the order independently"
    fallback_friendly: false
    purpose: "Second, differently-authored derivation must equal the plan."
  - name: "remove-step"
    sheets: 1
    instrument_guidance: "instrument: cli wrapper — sweep empty, remove, re-derive leaves, ledger append; one step per self-chain cycle"
    fallback_friendly: false
    purpose: "Remove exactly one current leaf; the sweep re-runs after because removals create new leaves."
  - name: "final-void"
    sheets: 1
    instrument_guidance: "instrument: cli — absence proven by the full oracle"
    fallback_friendly: false
    purpose: "Artifact gone AND the full build/test oracle green."
dependencies:
  verify-order: ["map-structure"]
  remove-step: ["verify-order"]
  final-void: ["remove-step"]
composes_with:
  - pattern: "Saga Compensation Chain"
    how: "contrast — time order vs structure order: the two axes, stated"
  - pattern: "Behavioral Pre-Mortem"
    how: "prerequisite — dry-render the demolition DAG before the first cut"
  - pattern: "The Soak Period"
    how: "its pair (archive) — structure-computable vs structure-unknowable removals"
---
```

**Source:** Expedition 1; **the strongest pattern by all three reviews** — "genuinely distinct," "survives complete removal of the ship-breaking story," "a genuine correction to naive saga thinking."

### Core Dynamic

**The assembly DAG read backwards is not a valid disassembly DAG.** When the ship was built, temporary staging carried loads that no longer exist; when the building was poured, formwork carried the slabs until the concrete cured. The completed structure bears weight through paths that did not exist during assembly. Demolition engineers do not replay the build in reverse — they compute a *new* order in which the remaining structure is self-stable at every step. The Marianne translation: **removal order is computed from reverse dependencies, not from commit history.** Saga Compensation undoes by time (correct for restoring business state); demolition removes by structure — you may not remove a thing while anything live still stands on it. Before each removal, a deterministic sweep enumerates the element's consumers; removal proceeds only when that set is empty; and the sweep re-runs after every removal because removals create new leaves. This is Legion's own law — enumerate ALL consumers before touching a shared field — promoted from discipline to mechanism.

**The serialized driver (Review 1):** one removal per self-chain cycle. The score re-invokes itself via `concert`/`on_success`; movement 3's sheet is skipped when the ledger shows no remaining steps — so the chain drains the plan and terminates. Parallel removals would race the stability computation; serialization is the safety property.

### Marianne Score Structure

```yaml
concert:
  enabled: true
  max_chain_depth: 40               # bound: one cycle per step plus commissioning
  inherit_workspace: true
on_success:
  - type: run_job
    job_path: "{score_dir}/top-down-demolition.yaml"

movements:
  1: { name: map-structure, instrument: cli, instrument_fallbacks: [] }
  2: { name: verify-order, instrument: cli, instrument_fallbacks: [] }
  3: { name: remove-step, instrument: cli, instrument_fallbacks: [] }
  4: { name: final-void, instrument: cli, instrument_fallbacks: [] }

sheet:
  size: 1
  total_items: 4
  dependencies: { 2: [1], 3: [2], 4: [3] }
  skip_when:
    1: { command: 'test -s {workspace}/demolition-plan.json' }   # plan exists: skip re-mapping
    2: { command: 'test -s {workspace}/order-verified.stamp' }   # verified once: stay verified
    3: { command: 'test $(jq ".steps | map(select(.state != \"done\")) | length" {workspace}/demolition-plan.json) -eq 0' }
    4: { command: 'test $(jq ".steps | map(select(.state != \"done\")) | length" {workspace}/demolition-plan.json) -gt 0' }
  per_sheet_fallbacks:
    1: []
    2: []
    3: []
    4: []

prompt:
  template: |
    {% if stage == 1 %}
    bash "{score_dir}/scripts/dep-graph.sh" --target "{{ target_path }}" \
      --emit "{{ workspace }}/demolition-plan.json"
    {% elif stage == 2 %}
    bash "{score_dir}/verify/order-rederive.sh" --target "{{ target_path }}" \
      --diff-against "{{ workspace }}/demolition-plan.json" && touch "{{ workspace }}/order-verified.stamp"
    {% elif stage == 3 %}
    bash "{score_dir}/scripts/step.sh" --plan "{{ workspace }}/demolition-plan.json" \
      --sweep-expect-empty --ledger "{{ workspace }}/demolition-ledger.jsonl"
    {% else %}
    Prove absence: bash "{score_dir}/scripts/full-oracle.sh" "{{ workspace }}"
    {% endif %}

validations:
  - type: command_succeeds
    command: 'jq -e ".steps | length > 0" {workspace}/demolition-plan.json'
    condition: "stage == 1"
  - type: command_succeeds
    command: 'bash {score_dir}/verify/order-rederive.sh --target {target_path} --diff-against {workspace}/demolition-plan.json'
    condition: "stage == 2"
  - type: command_succeeds
    command: 'bash {score_dir}/scripts/step.sh --self-test'
    condition: "stage == 3"
  - type: command_succeeds
    command: 'bash {score_dir}/scripts/full-oracle.sh {workspace}'
    condition: "stage == 4"
```

The plan and ledger are JSON checked by jq, never prose greps; movement 2 re-derives the order with a *differently-authored* tool (the `verify/` directory — Concurrent Count's discipline applied to structure); the step self-test includes a fixture where a live consumer exists and removal must refuse; and only the full suite is green at the end.

### Example

Deprecating a shared `user-events` topic schema that fourteen services publish to and nine consume. Commit order says the schema came before its consumers, so newest-first would kill the schema first. The demolition order computes: migrate publishers first (no dependents), then consumers, then the topic. Every step leaves the running system self-stable.

---
# Adaptation Patterns

*Three enter — the break-even ladder, the condition-bound overlay, the pre-paid threshold. The ATO Cycle is archived pending a multi-generation redesign.*

## Rent-Then-Commit (Break-Even Escalation)

```yaml
---
name: "Rent-Then-Commit"
scale: adaptation
status: working
forces: ["Finite Resources"]
generators: ["Threshold-Triggered Switch"]
problem: "A repeated per-use cost and a one-time commitment cost face an unknown horizon, and no rule says when committing becomes provably defensible."
signals:
  - "cheap retries that might go on forever vs one expensive settlement"
  - "recompute-every-run vs freeze-a-contract decisions"
  - "spot vs reserved capacity across a chain of unknown length"
stages:
  - name: "ledger-probe"
    sheets: 1
    instrument_guidance: "instrument: cli — reads the persisted spend ledger; nothing else touches it"
    fallback_friendly: false
    purpose: "Emit ladder-state.yaml: cumulative rent vs declared B."
  - name: "ladder-decide"
    sheets: 1
    instrument_guidance: "instrument: cli — pure arithmetic, exit-coded"
    fallback_friendly: false
    purpose: "Emit decision.yaml: {lane: rent|buy, rent_paid, B, ratio_bound: 2}."
  - name: "rent-lane"
    sheets: "fan_out(2)"
    instrument_guidance: "cheap instrument (opencode GLM-5.3-flash); skip_when lane != rent"
    fallback_friendly: true
    purpose: "Cheap partial work while the ledger is below B."
  - name: "buy-lane"
    sheets: 1
    instrument_guidance: "strong reasoner (opus); skip_when lane != buy"
    fallback_friendly: false
    purpose: "Settle the whole remainder now; the horizon ended."
  - name: "settle"
    sheets: 1
    instrument_guidance: "instrument: cli — appends spend; the self-chain carries the ledger"
    fallback_friendly: false
    purpose: "Persist the ledger for the next cycle."
dependencies:
  ladder-decide: ["ledger-probe"]
  rent-lane: ["ladder-decide"]
  buy-lane: ["ladder-decide"]
  settle: ["rent-lane", "buy-lane"]
composes_with:
  - pattern: "Circuit Breaker"
    how: "layering — availability state machine composed with the cost ladder"
  - pattern: "Speculative Hedge"
    how: "substitution — the hedge IS the parallel purchase; the ladder prices when parallelism pays"
  - pattern: "The Economic Injury Line"
    how: "contrast — known damage model (EIL) vs unknown horizon (this); never confuse them"
---
```

**Source:** Expedition 4 (ski-rental); Reviews 1 and 3 demanded the routing actually exist — it now does, in the real dialect.

### Core Dynamic

A repeated per-use cost and a one-time commitment cost face an adversary who knows the horizon and you who do not. The classical result is exactly this strong and exactly this cheap: **keep renting while cumulative rent is below the commitment price B; commit the moment it reaches B; and no adversary can make you pay more than twice what a clairvoyant scheduler would have paid.** The factor of 2 is a proven worst-case bound, and the entire decision policy is arithmetic over a ledger. In an orchestra: cheap retried attempts are rent; the serialized authority, the expensive reasoner, the frozen contract, the precomputed index is the purchase.

**The routing, made real (Reviews 1 and 3):** there is no dynamic instrument reassignment — `fan_out` and instruments resolve at parse time. The lanes are **sheets gated by `skip_when` commands**: the rent lane's sheets skip when `decision.lane != "rent"`, the buy lane's sheet skips when `!= "buy"`. The decision travels by `capture_files` into whichever lane runs, and the executor cites the ladder position in its output header. The self-chain is the real `concert` + `on_success: run_job` form — the draft's `on_success: {action: self}` shape does not exist. The randomized 1.582-competitive variant is archive-color: it requires its draw distribution and seed assumptions stated, and the deterministic 2-bound is the version the corpus carries.

### Marianne Score Structure

```yaml
instruments:
  cheap: { profile: opencode, config: { model: "zai-coding-plan/glm-5.3-flash" } }
concert:
  enabled: true
  max_chain_depth: 12
  inherit_workspace: true
on_success:
  - type: run_job
    job_path: "{score_dir}/rent-then-commit.yaml"

movements:
  1: { name: ledger-probe, instrument: cli, instrument_fallbacks: [] }
  2: { name: ladder-decide, instrument: cli, instrument_fallbacks: [] }
  3: { name: rent-lane, voices: 2 }
  4: { name: buy-lane }
  5: { name: settle, instrument: cli, instrument_fallbacks: [] }

sheet:
  size: 1
  total_items: 5                    # expansion: 1,2, rent 3-4, buy 5, settle 6
  fan_out: { 3: 2 }
  dependencies: { 2: [1], 3: [2], 4: [2], 5: [3, 4] }
  skip_when:                        # keys are EXPANDED sheet numbers (adapter.py:2947)
    3: { command: 'test "$(jq -r .lane {workspace}/decision.yaml)" != "rent"' }
    4: { command: 'test "$(jq -r .lane {workspace}/decision.yaml)" != "rent"' }
    5: { command: 'test "$(jq -r .lane {workspace}/decision.yaml)" != "buy"' }
  per_sheet_instruments:
    3: cheap
    4: cheap
  per_sheet_fallbacks:
    1: []
    2: []
    6: []

cross_sheet:
  capture_files: ["{{ workspace }}/decision.yaml"]

prompt:
  variables: { commitment_price: 6.0 }
  template: |
    {% if stage == 1 %}
    bash "{score_dir}/scripts/ladder.sh" probe --ledger "{{ workspace }}/spend-ledger.jsonl" \
      --commitment {{ commitment_price }} --emit "{{ workspace }}/ladder-state.yaml"
    {% elif stage == 2 %}
    bash "{score_dir}/scripts/ladder.sh" decide --state "{{ workspace }}/ladder-state.yaml" \
      --emit "{{ workspace }}/decision.yaml"
    {% elif stage == 3 %}
    Renting. Complete your slice on the cheap path. Cite lane and ladder
    position from decision.yaml in your output header.
    {% elif stage == 4 %}
    Committed. Settle the whole remainder now. Cite the ladder position.
    {% else %}
    bash "{score_dir}/scripts/ladder.sh" settle --ledger "{{ workspace }}/spend-ledger.jsonl"
    {% endif %}

validations:
  - type: command_succeeds
    command: 'jq -e "(.ratio_bound == 2) and (.commit == (.rent_paid >= .B))" {workspace}/decision.yaml'
    condition: "stage == 2"
  - type: command_succeeds
    command: 'bash {score_dir}/scripts/ladder.sh --self-test'
    condition: "stage == 2"
```

The self-test is the pattern's own negative control: a ledger with rent ≥ B whose decision did not commit must fail; the proof score's substrate exercises the arithmetic it proves.

### Example

A nonprofit's weekly self-chaining score drafts donor summaries on a cheap model and occasionally needs a strong reasoner for contested numbers. Nobody knows which weeks will be contested. The ladder keeps cheap drafting until cumulative cheap spend equals one strong-instrument takeover, then commits — and the board can be told, arithmetically, that no scheduling hindsight could have done better than twice what was paid.

---

## Vintage Overlay

```yaml
---
name: "Vintage Overlay"
scale: adaptation
status: working
forces: ["Instrument-Task Fit", "Finite Resources"]
generators: ["Gate on Environmental Readiness"]
problem: "A canonical pipeline re-runs on a cadence under external conditions that vary, and each run improvises tuning instead of selecting from pre-authored condition-bound parameter sets."
signals:
  - "the pipeline is stable; the conditions are not"
  - "conditions are mechanically measurable (versions, rate climates, volatility)"
  - "per-vintage tuning would beat per-run improvisation"
stages:
  - name: "conditions"
    sheets: 1
    instrument_guidance: "instrument: cli — the weather station has no opinions; records resolved model families, not instrument names"
    fallback_friendly: false
    purpose: "Emit conditions.yaml with per-condition digests."
  - name: "select"
    sheets: 1
    instrument_guidance: "instrument: cli — TOTAL lookup with refusal on unknown vectors"
    fallback_friendly: false
    purpose: "Emit vintage-manifest.yaml binding overlay ids to the condition digests that selected them."
  - name: "execute"
    sheets: 1
    instrument_guidance: "any — receives base spec plus the manifest by required cadenza"
    fallback_friendly: true
    purpose: "Run under base+overlay; mid-run re-tuning is a different vintage pretending to be the same bottle."
  - name: "archive-record"
    sheets: 1
    instrument_guidance: "instrument: cli — the vintage record is the Write-Time Record's run-level instance"
    fallback_friendly: false
    purpose: "Archive conditions + digests + overlay ids as this run's vintage record."
dependencies:
  select: ["conditions"]
  execute: ["select"]
  archive-record: ["execute"]
composes_with:
  - pattern: "Effectivity Blocks"
    how: "the vintage manifest is a run-level effectivity block"
  - pattern: "The Write-Time Record"
    how: "the vintage record is its archival instance"
  - pattern: "Season Bible"
    how: "contrast — mutable continuity within a campaign vs immutable condition-binding per run"
---
```

**Source:** Expedition 2; survived Review 3's cut motion 2–1, with the merge critique answered structurally.

### Core Dynamic

The mature grower's discipline is refusing to write a new score every year. The canonical cycle is stable knowledge; what varies is *which pre-tuned parameter set manifests*, selected by a measurement stage at the top of the run — and that selection is a **lookup**, not judgment. Three review-driven corrections are now constitutive. **Totality with refusal (Reviews 1 and 2):** the condition-map is total over its declared axes; an unknown condition vector exits non-zero — no defaults, no nearest-neighbor guessing. **Manifest as data (Review 2):** runtime-measured conditions cannot re-route already-resolved spec tags, so the manifest reaches consumers as a **required cadenza** — data the sheets read — not as dynamic spec routing. **Pin what is pinnable (Review 1):** the overlay files are authored artifacts, so they are pinned with literal `file_sha256` digests known at authorship; the manifest additionally records the condition digests that did the selecting, so any result's recipe is reproducible months later. The overlay is frozen for the run's duration: mid-run re-tuning is not adaptation, it is a different vintage pretending to be the same bottle.

### Marianne Score Structure

```yaml
movements:
  1: { name: conditions, instrument: cli, instrument_fallbacks: [] }
  2: { name: select, instrument: cli, instrument_fallbacks: [] }
  3: { name: execute }
  4: { name: archive-record, instrument: cli, instrument_fallbacks: [] }

sheet:
  size: 1
  total_items: 4
  dependencies: { 2: [1], 3: [2], 4: [3] }
  cadenzas:
    3:
      - file: "{{ workspace }}/vintage-manifest.yaml"
        as: context
        required: true
  per_sheet_fallbacks:
    1: []
    2: []
    4: []

prompt:
  template: |
    {% if stage == 1 %}
    bash "{score_dir}/scripts/conditions.sh" --probe versions,rates,volatility \
      --emit "{{ workspace }}/conditions.yaml"
    {% elif stage == 2 %}
    bash "{score_dir}/scripts/overlay.sh" select --conditions "{{ workspace }}/conditions.yaml" \
      --map "{score_dir}/condition-map.yaml" --emit "{{ workspace }}/vintage-manifest.yaml"
    {% elif stage == 3 %}
    Execute under base spec plus the overlay named in your manifest. Mid-run
    re-tuning is forbidden — different vintage, same bottle is a lie.
    {% else %}
    bash "{score_dir}/scripts/overlay.sh" archive --manifest "{{ workspace }}/vintage-manifest.yaml" \
      --conditions "{{ workspace }}/conditions.yaml" --out "{{ workspace }}/vintage-record/"
    {% endif %}

validations:
  - type: file_sha256
    path: "{score_dir}/overlays/vendor-v3-drift.yaml"
    sha256: "b1c2d3e4f5a6b7c8d9e0f1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2"
    condition: "stage == 2"
  - type: command_succeeds
    command: 'bash {score_dir}/scripts/overlay.sh select --conditions {workspace}/conditions.yaml --map {score_dir}/condition-map.yaml --self-test'
    condition: "stage == 2"
```

The self-test's fixture is an unknown condition vector that must be refused (exit non-zero), proving the lookup's totality-by-refusal.

### Example

A quarterly SEC-filing extraction pipeline: one canonical score, four runs a year. The 2026-Q3 weather station reads the filing portal's schema version, the data vendor's API generation, and this quarter's document-volume volatility; the manifest binds the `vendor-v3-drift` overlay with the selecting digests; extraction receives base + overlay. The vintage record answers, months later, *which* recipe produced the Q3 numbers.

---

## The Economic Injury Line

```yaml
---
name: "The Economic Injury Line"
scale: adaptation
status: working
forces: ["Finite Resources", "Accumulated Signal"]
generators: ["Threshold-Triggered Switch"]
problem: "Defensive recurring work responds to felt damage instead of a threshold computed from unit economics before the season began."
signals:
  - "real unit costs on both sides — intervening and damage"
  - "most intervals honestly deserve NO action"
  - "a bounded sampling protocol can estimate the pressure cheaply"
stages:
  - name: "verify-threshold"
    sheets: 1
    instrument_guidance: "instrument: cli — re-derives from the PINNED spec inputs; never re-authors"
    fallback_friendly: false
    purpose: "Diff the re-derivation against the digest-pinned table authored before the season."
  - name: "scout"
    sheets: 1
    instrument_guidance: "instrument: cli — bounded statistical sampling, seeded"
    fallback_friendly: false
    purpose: "Append sampled pressure to the scout ledger."
  - name: "verdict"
    sheets: 1
    instrument_guidance: "instrument: cli — one boolean from arithmetic against the frozen table"
    fallback_friendly: false
    purpose: "Emit verdict.json: {not-yet | treat-tier-n, table_digest}."
  - name: "treat"
    sheets: 1
    instrument_guidance: "executor for the authorized tier; skip_when not-yet; broad tier barred while incremental retains efficacy"
    fallback_friendly: true
    purpose: "Execute exactly the authorized tier."
dependencies:
  scout: ["verify-threshold"]
  verdict: ["verify-threshold", "scout"]
  treat: ["verdict"]
composes_with:
  - pattern: "Rent-Then-Commit"
    how: "contrast — known damage model vs unknown horizon; the two adaptation arithmetics"
  - pattern: "Hutchinson's Warning"
    how: "contrast — no trend, no EMA: a standing threshold and a one-bit question per sample"
  - pattern: "Immune Cascade"
    how: "contrast — tiers chosen by triage judgment vs a line computed from unit economics"
---
```

**Source:** Expedition 2 (Stern et al. 1959, EIL = C/(V·I·D·K)); Review 2: "one of the best entries"; the timing critique (Reviews 1 and 2) is fixed by pre-observation custody.

### Core Dynamic

Everything turns on *when* the threshold is made. The farmer does not discover the tripwire by watching the crop feel bad — she computes it in February from the price of the grain, the price of the spray, and last season's damage curves, writes it on the shed wall, and spends the whole season doing almost nothing except counting bugs on a sampling plan. The runtime decision is one boolean produced by arithmetic against a number frozen before the season began. **Judgment is pre-paid.** **The February fix (Reviews 1 and 2):** the inputs and the derived table are **authored into the spec corpus before the season** and digest-pinned with literal `file_sha256`; the run's first movement *verifies* the re-derivation matches the pinned table and refuses to run on a mismatch. The line sits one response-lag *below* the injury level — act at the density where acting now prevents arrival, not at "damage is visible" (too late by construction). And the conservation clause is an **executable tier ordering**: the broad-spectrum tier is barred while an efficacy check on the incremental tier passes — you do not destroy the wasps doing free pest control unless the cheap insurance is already lost.

The season's default outcome is *visibly skipped sheets*: a below-threshold season treats nothing and still exits green — that negative control is the proof, not a degenerate run.

### Marianne Score Structure

```yaml
spec:
  spec_dir: "{score_dir}/specs"

movements:
  1: { name: verify-threshold, instrument: cli, instrument_fallbacks: [] }
  2: { name: scout, instrument: cli, instrument_fallbacks: [] }
  3: { name: verdict, instrument: cli, instrument_fallbacks: [] }
  4: { name: treat }

sheet:
  size: 1
  total_items: 4
  dependencies: { 2: [1], 3: [1, 2], 4: [3] }
  skip_when:
    4: { command: 'jq -e ".action == \"not-yet\"" {workspace}/verdict.json' }
  per_sheet_fallbacks:
    1: []
    2: []
    3: []

prompt:
  variables: { run_seed: 11 }
  template: |
    {% if stage == 1 %}
    bash "{score_dir}/scripts/eil.sh" verify --inputs "{score_dir}/specs/eil-inputs.yaml" \
      --pinned-table "{score_dir}/specs/eil-table.yaml"
    {% elif stage == 2 %}
    bash "{score_dir}/scripts/eil.sh" scout --sample 5pct --seed {{ run_seed }} \
      --ledger "{{ workspace }}/scout-ledger.jsonl"
    {% elif stage == 3 %}
    bash "{score_dir}/scripts/eil.sh" verdict --table "{score_dir}/specs/eil-table.yaml" \
      --ledger "{{ workspace }}/scout-ledger.jsonl" --emit "{{ workspace }}/verdict.json"
    {% else %}
    Execute exactly the tier the verdict authorizes. The broad-spectrum tier is
    barred while the incremental tier retains efficacy.
    {% endif %}

validations:
  - type: file_sha256
    path: "{score_dir}/specs/eil-table.yaml"
    sha256: "a0b1c2d3e4f5a6b7c8d9e0f1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2"
    condition: "stage == 1"
  - type: command_succeeds
    command: 'bash {score_dir}/scripts/eil.sh verify --inputs {score_dir}/specs/eil-inputs.yaml --pinned-table {score_dir}/specs/eil-table.yaml'
    condition: "stage == 1"
  - type: command_succeeds
    command: 'bash {score_dir}/scripts/eil.sh --self-test'
    condition: "stage == 3"
```

The verdict carries the table digest it was computed against — a re-derived threshold mid-run is inadmissible. Fan-out is actively wrong here: the sampling protocol is bounded *statistical* sampling, not an exhaustive partition sweep.

### Example

A stale-listing remediation loop: re-scrape cost C = $0.004/listing; listing value V = expected margin; injury I and damage D fitted from last quarter's A/B data; efficacy K = 0.8. The February stage — run once, before the season — computes and pins the line; a weekly scout samples 5% of categories; remediation sheets stay skipped until sampled staleness crosses the lag-adjusted line — and the broad rebuild tier is barred while the incremental tier handles 80% for free.

---

# Concert-Level Patterns

*Two enter — typed decision force across a campaign, and endings with accounting. Cluster Lead is archived; Put-In awaits a seat-remap primitive.*

## The Precedent Bench (Stare Decisis Binding)

```yaml
---
name: "The Precedent Bench"
scale: concert-level
status: working
forces: ["Information Asymmetry", "Convergence Imperative"]
generators: ["Accumulate Knowledge"]
problem: "A long campaign re-litigates settled decisions every score, or contradicts them silently — because decisions carry no typed force and no supersession record."
signals:
  - "'what have we already decided?' answered by archaeology"
  - "later scores contradicting earlier load-bearing decisions unknowingly"
  - "corrections and overrulings indistinguishable in the record"
stages:
  - name: "cite-check"
    sheets: 1
    instrument_guidance: "instrument: cli — dangling citations rejected before reasoning is paid for"
    fallback_friendly: false
    purpose: "Join the motion's citations against the precedent index."
  - name: "brief"
    sheets: 1
    instrument_guidance: "any — argues follow | distinguish | overrule; receives the live index by required cadenza"
    fallback_friendly: true
    purpose: "Argue the motion; overrule requires named factors."
  - name: "bench"
    sheets: 1
    instrument_guidance: "ONE named adjudication authority (strong reasoner); advisory seats are Dropped-Axiom-typed inputs, never undisclosed votes"
    fallback_friendly: false
    purpose: "Grant or deny; dicta may be declined without ceremony."
  - name: "enroll"
    sheets: 1
    instrument_guidance: "instrument: cli — ONE serialized writer; append holding + supersession edges atomically"
    fallback_friendly: false
    purpose: "The ledger transition: enrolled, or superseded-visibly — never edited."
  - name: "notify"
    sheets: 1
    instrument_guidance: "instrument: cli — supersession flags across the precedent corpus"
    fallback_friendly: false
    purpose: "Every consumer of an overruled holding learns it moved."
dependencies:
  brief: ["cite-check"]
  bench: ["brief"]
  enroll: ["bench"]
  notify: ["enroll"]
composes_with:
  - pattern: "Typed Force"
    how: "its richest form — binding/persuasive force with visible supersession"
  - pattern: "The Errata Ledger"
    how: "contrast — errata correct errors; precedent governs decisions that were right and must yield anyway"
  - pattern: "Fork-Evident History"
    how: "enrollment rides the append-only chain"
---
```

**Source:** Expedition 6; survived review narrowed to a typed append-only decision registry with one adjudication authority (Reviews 1 and 2).

### Core Dynamic

A long campaign accumulates decisions the way a court accumulates cases. Stare decisis resolves the re-litigation tension by giving decisions **typed force**: a decision *necessary to the outcome* of its score (a holding) binds later scores until explicitly overruled; an incidental decision (dictum) persuades and may be declined without ceremony. A score that wants to contradict a holding files a typed motion — **distinguish** (conditions differ in a load-bearing way) or **overrule** (citing reliance, workability, changed circumstances) — and the bench grants or denies. The signature property: **the overruled precedent stays on the books, visibly superseded.** The Errata Ledger corrects errors; only law governs decisions that were correct when made, remain correct as history, and must yield anyway.

**The narrowing (Reviews 1 and 2):** one named adjudication authority decides — advisory benches may fan out, but their aggregate arrives as a Dropped Axiom-typed input with a declared rule, never as an undisclosed vote. The typing decision (`necessary_to_outcome`) is judgment by the *emitting* score under the Typed Force law's provenance rule — assigned by a named authority at creation, contestable by motion, never silently re-typed by a gate. **Delivery (Review 1):** the live precedent index reaches the *brief* and *bench* sheets by required cadenza keyed to their expanded sheet numbers. **Enrollment:** one serialized CLI writer appends the holding row and its supersession edges atomically; an overrule without a named factor does not enroll. **The registration-time/runtime distinction, stated honestly:** spec-corpus fragments inject as they stood at registration; the cadenza injects the live index at runtime — and a score citing precedent that moved between the two is exactly what the cite-join gate catches.

### Marianne Score Structure

```yaml
movements:
  1: { name: cite-check, instrument: cli, instrument_fallbacks: [] }
  2: { name: brief }
  3: { name: bench }
  4: { name: enroll, instrument: cli, instrument_fallbacks: [] }
  5: { name: notify, instrument: cli, instrument_fallbacks: [] }

sheet:
  size: 1
  total_items: 5
  dependencies: { 2: [1], 3: [2], 4: [3], 5: [4] }
  cadenzas:
    2:
      - file: "{{ workspace }}/precedent/INDEX.md"
        as: context
        required: true
    3:
      - file: "{{ workspace }}/precedent/INDEX.md"
        as: context
        required: true
  per_sheet_fallbacks:
    1: []
    4: []
    5: []

prompt:
  template: |
    {% if stage == 1 %}
    bash "{score_dir}/scripts/cite-join.sh" --motions "{{ workspace }}/motions/current.json" \
      --index "{{ workspace }}/precedent/index.jsonl"
    {% elif stage == 2 %}
    Argue the motion: follow | distinguish | overrule. Overrule REQUIRES named
    factors from {reliance, workability, changed-circumstances}. Write
    {{ workspace }}/brief.md.
    {% elif stage == 3 %}
    You are the adjudication authority. Grant or deny. Dicta may be declined
    without ceremony. Write {{ workspace }}/ruling.md with force and assigned_by.
    {% elif stage == 4 %}
    bash "{score_dir}/scripts/enroll.sh" --ruling "{{ workspace }}/ruling.md" \
      --index "{{ workspace }}/precedent/index.jsonl" --atomic
    {% else %}
    bash "{score_dir}/scripts/notify.sh" --supersession-flags "{{ workspace }}/precedent/"
    {% endif %}

validations:
  - type: command_succeeds
    command: 'bash {score_dir}/scripts/cite-join.sh --motions {workspace}/motions/current.json --index {workspace}/precedent/index.jsonl'
    condition: "stage == 1"
  - type: content_contains
    path: "{workspace}/ruling.md"
    pattern: "force:"
    condition: "stage == 3"
  - type: command_succeeds
    command: 'bash {score_dir}/scripts/enroll.sh --self-test'
    condition: "stage == 4"
```

The enroll self-test: an overrule motion lacking a named factor must refuse to enroll; a dangling-citation fixture must die at movement 1, before any reasoning is paid for.

### Example

A refactoring campaign where early scores decided "no new dependencies," "errors at exit 0 are still failing," "unify, never fork." Typed as holdings, they bind later scores until explicitly overruled; a later score wanting a new dependency distinguishes or moves to overrule; the ledger shows the one overrule superseding its predecessor while both remain readable.

---

## Demobilization Checkout

```yaml
---
name: "Demobilization Checkout"
scale: concert-level
status: working
forces: ["Partial Failure", "Finite Resources"]
generators: ["Exploit Failure as Signal"]
problem: "Concerts end by stopping being visible, leaving orphaned processes, live leases firing into dead workspaces, and credentials outliving their purpose."
signals:
  - "a campaign with physical footprint: daemons, leases, clones, containers, credentials"
  - "retirement has no owner; archival is the only ending ritual"
  - "'the run ended' treated as if it meant 'the run failed'"
stages:
  - name: "census"
    sheets: 1
    instrument_guidance: "instrument: cli — fresh enumeration at demob; the WRITE-TIME ledger is its pre-history"
    fallback_friendly: false
    purpose: "Emit census.jsonl of everything with a footprint."
  - name: "dispositions"
    sheets: 1
    instrument_guidance: "any — one disposition row per resource id, in a SEPARATE table"
    fallback_friendly: true
    purpose: "archive | release | retain-and-why, per census id."
  - name: "act"
    sheets: 1
    instrument_guidance: "instrument: cli — executes dispositions; Gas-Free discipline where destructive"
    fallback_friendly: false
    purpose: "Emit receipts.jsonl; destructive rows run under permits."
  - name: "liveness-settle"
    sheets: 1
    instrument_guidance: "instrument: cli — the settlement probes must return EMPTY"
    fallback_friendly: false
    purpose: "Prove the host is clean with the same physical checks that prove a conductor stopped."
  - name: "seal"
    sheets: 1
    instrument_guidance: "instrument: cli — harvest before archive; manifest after"
    fallback_friendly: false
    purpose: "After-action material out of the live tree, then archive + terminal manifest."
dependencies:
  dispositions: ["census"]
  act: ["dispositions"]
  liveness-settle: ["act"]
  seal: ["liveness-settle"]
composes_with:
  - pattern: "The Write-Time Record"
    how: "its consumption side — the commissioning ledger is the census's pre-history"
  - pattern: "The Gas-Free Certificate"
    how: "prerequisite — destructive dispositions run under permits"
  - pattern: "Saga Compensation Chain"
    how: "contrast — saga compensates effects; demob releases resources"
---
```

**Source:** Expedition 5; survived all three reviews ("survives," "every multi-cloud user has lived the six-weeks-of-console-archaeology failure") with the tables separated and the attachment made real.

### Core Dynamic

The corpus knows how to start things and how to fail things. Demobilization is the third ending: **release with accounting**. Every resource the concert consumed — process, workspace, lease, credential, branch, container — gets a checkout record with a disposition before the workspace archives. Doctrine's two sharpest edges: demobilization planning **begins at incident initiation** (the Write-Time Record's commissioning ledger is the census's pre-history — every provisioning row already carries its `decommission_cmd`), and resources are released **as soon as they are no longer needed**. The failure mode demob prevents is not dramatic; it is sediment: orphaned processes holding ports, unstopped leases firing into dead workspaces, finished campaigns occupying a hundred gigabytes because retirement had no owner. The incident that never demobilizes never actually ends; it just stops being visible. "The run ended" is not "the run failed."

**The tables, separated (Review 1):** `census.jsonl` (what exists — CLI enumeration), `dispositions.jsonl` (what the AI decided, per resource id), `receipts.jsonl` (what the CLI did), settlement results (liveness probes that must return empty). The bijections are exact: every census id has exactly one disposition; every destructive disposition has a permit; every disposition has a receipt or a written reason. **The attachment, made real:** the demob score is chained by `on_success: run_job` from the concert's terminal score, with its mirror on `on_failure` — failure also demobilizes, with evidence preservation taking disposition priority.

### Marianne Score Structure

```yaml
movements:
  1: { name: census, instrument: cli, instrument_fallbacks: [] }
  2: { name: dispositions }
  3: { name: act, instrument: cli, instrument_fallbacks: [] }
  4: { name: liveness-settle, instrument: cli, instrument_fallbacks: [] }
  5: { name: seal, instrument: cli, instrument_fallbacks: [] }

sheet:
  size: 1
  total_items: 5
  dependencies: { 2: [1], 3: [2], 4: [3], 5: [4] }
  per_sheet_fallbacks:
    1: []
    3: []
    4: []
    5: []

prompt:
  template: |
    {% if stage == 1 %}
    bash "{score_dir}/scripts/demob.sh" census --processes --leases --workspaces \
      --credentials --branches --containers --emit "{{ workspace }}/census.jsonl"
    {% elif stage == 2 %}
    Write ONE disposition row per census id in {{ workspace }}/dispositions.jsonl:
    {id, disposition: archive|release|retain, reason}. Census and disposition
    counts must match EXACTLY — nothing unaccounted.
    {% elif stage == 3 %}
    bash "{score_dir}/scripts/demob.sh" act --dispositions "{{ workspace }}/dispositions.jsonl" \
      --receipts "{{ workspace }}/receipts.jsonl" --permits-required-for destructive
    {% elif stage == 4 %}
    bash "{score_dir}/scripts/demob.sh" settle --receipts "{{ workspace }}/receipts.jsonl" \
      --liveness-must-return-empty
    {% else %}
    bash "{score_dir}/scripts/demob.sh" seal --harvest "{{ workspace }}/after-action/" \
      --archive --emit-manifest
    {% endif %}

validations:
  - type: command_succeeds
    command: 'bash {score_dir}/scripts/demob.sh settle --receipts {workspace}/receipts.jsonl --liveness-must-return-empty'
    condition: "stage == 4"
  - type: command_succeeds
    command: 'bash {score_dir}/scripts/demob.sh bijection --census {workspace}/census.jsonl --dispositions {workspace}/dispositions.jsonl --receipts {workspace}/receipts.jsonl --exact'
    condition: "stage == 5"
```

Census and settle are pure CLI (`pgrep`, `find`, `git`, container CLIs, `sha256sum`) with empty fallback chains — no AI reinterprets a liveness fact.

### Example

A quarter-long model-evaluation campaign ends: its demob score finds two stale evaluation daemons holding GPU memory, three scheduled lease entries pointing at archived workspaces, and one service credential — stops/revokes each with a checkout row, harvests the eval histories into the after-action review, archives, and leaves a terminal manifest proving the host is clean.

---
# Iteration Patterns

## The Unprimed Falsifier (formerly Test Screening to Picture Lock)

```yaml
---
name: "The Unprimed Falsifier"
scale: iteration
status: working
forces: ["Structured Disagreement", "Convergence Imperative"]
generators: ["Verify through Diverse Observers", "Measure Convergence Character"]
problem: "Makers cannot perceive their finished artifact — fluency hides the claims it makes — and internal evaluation shares the blind spot."
signals:
  - "anything read by humans whose makers are too close to it"
  - "'we think it's clear' has ever been wrong"
  - "self-evaluation and structural-equality checks both passing while users misread the thing"
stages:
  - name: "assemble"
    sheets: 1
    instrument_guidance: "any — builds the current cut from the beat map and drafts"
    fallback_friendly: true
    purpose: "Produce the artifact under evaluation."
  - name: "read-cold"
    sheets: "fan_out(5)"
    instrument_guidance: "cheap local tier (ollama) — the audience is many, shallow, and genuinely naive; each receives ONLY the artifact by cadenza"
    fallback_friendly: true
    purpose: "Report section-anchored reactions: confusion, dead zones, misreads."
  - name: "note-code"
    sheets: 1
    instrument_guidance: "instrument: cli — codes cards into typed, located evidence"
    fallback_friendly: false
    purpose: "Emit evidence.json: per-section density of located reactions."
  - name: "verdict"
    sheets: 1
    instrument_guidance: "strong reasoner — evidence-targeted recut or done; NOT the lock authority"
    fallback_friendly: false
    purpose: "Recut ONLY where density crosses threshold; declare done or chain."
dependencies:
  read-cold: ["assemble"]
  note-code: ["read-cold"]
  verdict: ["note-code"]
composes_with:
  - pattern: "The Freeze"
    how: "termination — the loop ends in authority-declared lock, not convergence (the lock half of the old Test Screening lives there)"
  - pattern: "Rehearsal Spotlight"
    how: "substitution — external falsifier replaces self-evaluation"
  - pattern: "The Declared Window"
    how: "the audience's claims are windowed to what the cut shows them — they are the honest window"
---
```

**Source:** Expedition 6, entered the draft as "Test Screening to Picture Lock"; split per Review 2 — the lock half routes to The Freeze, the falsifier stands alone.

### Core Dynamic

The people who made the film are constitutionally incapable of seeing it. They know what every shot was *meant* to say; the audience, seeing cold, reports what it *says*. The test screening is **falsification by outsiders**: recruited naive readers receive *only the artifact* — never the makers' intent, never the questions the makers are worried about (that would prime them) — and return reaction cards coded into **typed, located evidence**: where readers were confused, where attention died, what they thought happened. Thumbs-up/down is not a location; "bored somewhere in act two" is. The recut is *targeted*: only where evidence density crosses a threshold — a quiet screening is a verdict too, and recutting everything after every screening is churn with a ritual attached.

**Unprimedness is structural, not asserted (Reviews 1 and 3):** this score authors **no prelude**; each reader sheet's cadenza injects exactly one file — the cut — `required: true`; reader prompts contain no design-document references; and a priming check runs as a command gate: the reader outputs must contain no reference to any intent-document filename (grep over the cards returns empty). Readers tier to cheap local instruments — many, shallow, genuinely naive. Termination is authority-declared lock (The Freeze), with the self-chain bounded by `max_chain_depth` as the perfectionism circuit-breaker — infinite test screening is a known pathology.

### Marianne Score Structure

```yaml
concert:
  enabled: true
  max_chain_depth: 4               # the perfectionism breaker
  inherit_workspace: true
on_success:
  - type: run_job
    job_path: "{score_dir}/unprimed-falsifier.yaml"

movements:
  1: { name: assemble }
  2: { name: read-cold, voices: 5 }
  3: { name: note-code, instrument: cli, instrument_fallbacks: [] }
  4: { name: verdict }

sheet:
  size: 1
  total_items: 4                    # expansion: assemble 1, readers 2-6, code 7, verdict 8
  fan_out: { 2: 5 }
  dependencies: { 2: [1], 3: [2], 4: [3] }
  skip_when:                        # EXPANDED sheet keys: all five reader sheets
    2: { command: 'test -f {workspace}/done.stamp' }
    3: { command: 'test -f {workspace}/done.stamp' }
    4: { command: 'test -f {workspace}/done.stamp' }
    5: { command: 'test -f {workspace}/done.stamp' }
    6: { command: 'test -f {workspace}/done.stamp' }
  cadenzas:
    2:
      - file: "{{ workspace }}/cut.md"
        as: context
        required: true
    3:
      - file: "{{ workspace }}/cut.md"
        as: context
        required: true
    4:
      - file: "{{ workspace }}/cut.md"
        as: context
        required: true
    5:
      - file: "{{ workspace }}/cut.md"
        as: context
        required: true
    6:
      - file: "{{ workspace }}/cut.md"
        as: context
        required: true
  per_sheet_instruments:            # cheap local tier on every reader sheet
    2: ollama
    3: ollama
    4: ollama
    5: ollama
    6: ollama
  per_sheet_fallbacks:
    7: []
    8: []

prompt:
  template: |
    {% if stage == 1 %}
    Assemble the current cut from the beat map and drafts into {{ workspace }}/cut.md.
    {% elif stage == 2 %}
    You are a naive reader. You receive ONLY the cut. Report section-anchored
    reactions: confusion, dead zones, misreads. No design docs exist for you.
    Write {{ workspace }}/cards/card-{{ instance }}.md with one `section:` anchor per note.
    {% elif stage == 3 %}
    bash "{score_dir}/scripts/notes.sh" code --cards "{{ workspace }}/cards/" \
      --density --emit "{{ workspace }}/evidence.json"
    {% else %}
    Read {{ workspace }}/evidence.json. If any section's density crosses 2: recut
    ONLY those sections into a new {{ workspace }}/cut.md. Otherwise write
    {{ workspace }}/done.stamp. A quiet screening is a verdict too.
    {% endif %}

validations:
  - type: content_contains
    path: "{workspace}/cards/card-1.md"
    pattern: "section:"
    condition: "stage == 2"
  - type: command_succeeds
    command: 'test $(grep -lE "design-doc|intent|spec/" {workspace}/cards/*.md | wc -l) -eq 0'
    condition: "stage == 3"
  - type: command_succeeds
    command: 'bash {score_dir}/scripts/notes.sh code --cards {workspace}/cards --density --self-test'
    condition: "stage == 3"
```

The grep gate is the priming check: any card naming an intent-document path fails the run — the falsification property is enforced, not hoped for. The lock that terminates the loop is The Freeze's, invoked by the next score in the chain against the final cut's digest.

### Example

An API reference read cold by five naive sheets that have never seen the design docs. Cards report: "the auth section assumes a token the reader doesn't have yet," "examples 3–4 read as one example," "the error table lost me." Note-code locates density in the auth section; the verdict recuts exactly that; when a screening runs quiet, the done-stamp lands and the Freeze takes over for the finishing fan-out.

---

# Within-Stage Patterns

## The Dropped Axiom (Fan-In Typing)

```yaml
---
name: "The Dropped Axiom"
scale: within-stage
status: working
forces: ["Structured Disagreement"]
generators: ["Frame Multiplication"]
problem: "Every fan-in embodies an aggregation function constrained by theorems that do not care about intentions, and the synthesis presents its concealed choice as neutrality."
signals:
  - "sheets expressing rankings, priorities, or multi-premise verdicts"
  - "a synthesis that believes it is 'just combining'"
  - "an unlabelled 'consensus' output"
stages:
  - name: "fan-in"
    sheets: 1
    instrument_guidance: "any — but the PRODUCER declares input_type on its output; the synthesizer never classifies"
    fallback_friendly: true
    purpose: "Apply the lookup row for each declared input type; emit the typed header."
  - name: "typecheck"
    sheets: 1
    instrument_guidance: "instrument: cli — enforces rule↔axioms bijection per declared type"
    fallback_friendly: false
    purpose: "Reject empty axioms_dropped on rankings; reject dual-pole aggregation; reject unknown input_type."
dependencies:
  typecheck: ["fan-in"]
composes_with:
  - pattern: "Typed Force"
    how: "its fan-in form — the typing discipline's merge specialization"
  - pattern: "Fan-out + Synthesis"
    how: "grows this header at every merge — the primitive's typing clause"
  - pattern: "Sugya Weave (Editorial Synthesis)"
    how: "substitution — editorial authority entered by declaration rather than accident"
---
```

**Source:** Expedition 4 (Arrow's impossibility theorem; judgment aggregation); kept standalone against Review 2's fold motion (Reviews 1 and 3), with input typing moved to the producer (Review 1).

### Core Dynamic

Every fan-in embodies an aggregation function, and aggregation functions are constrained by theorems that do not care about your intentions. If the sheets express *rankings* over three or more alternatives, Arrow's theorem is already in the room: no rule satisfies unrestricted domain, Pareto, independence of irrelevant alternatives, and non-dictatorship at once — so your "neutral synthesis" is impossible, and whatever it actually does is a concealed choice about which axiom it silently dropped. **Concealment is the defect, not the dropping.** If the sheets express interconnected propositions, majority on each premise can entail a conclusion the majority on the conclusion rejects — and both procedures are "majority rule."

**The pattern, as a lookup the producer types (Review 1):** the panel-emitting stage writes `input_type ∈ {binary-verdict, ranking, interconnected-propositions, non-reconstructible-judgment}` on its own output — the synthesizer applies exactly the row for the declared type and never classifies inputs itself. The rows: `binary-verdict` + audited independence → majority (Condorcet's territory); `ranking` → declare the dropped axiom (IIA dropped is positional scoring; non-dictatorship dropped is a named editorial authority; unrestricted-domain dropped is declared single-peaked structure with a median); `interconnected-propositions` → premise-pole or conclusion-pole, exactly one, declared; `non-reconstructible-judgment` → editorial synthesis with dissents. The output field `axioms_dropped` is the pattern's whole teeth: an empty value on a ranking aggregation is not innocence, it is perjury. Review 2's fold motion is recorded as the losing argument: the fan-in rule earns its own file because it upgrades *every existing merge in every existing score* with one header field — the cheapest broad improvement in the corpus.

### Marianne Score Structure

```yaml
movements:
  1: { name: fan-in }
  2: { name: typecheck, instrument: cli, instrument_fallbacks: [] }

sheet:
  size: 1
  total_items: 2
  dependencies: { 2: [1] }
  per_sheet_fallbacks:
    2: []

prompt:
  template: |
    {% if stage == 1 %}
    You are aggregating panel outputs, each carrying its declared input_type.
    Apply the typing table per declared type — never re-classify an input.
    Your output header MUST carry {aggregation_rule, axioms_dropped,
    declared_authority}. Write {{ workspace }}/synthesis.md.
    {% else %}
    bash "{score_dir}/scripts/fanin-typecheck.sh" "{{ workspace }}/synthesis.md"
    {% endif %}

validations:
  - type: content_contains
    path: "{workspace}/synthesis.md"
    pattern: "aggregation_rule:"
    condition: "stage == 1"
  - type: command_succeeds
    command: 'bash {score_dir}/scripts/fanin-typecheck.sh {workspace}/synthesis.md'
    condition: "stage == 2"
```

The typechecker enforces the bijection per declared type — rule ∈ the shared demotion ladder `{majority, weighted-correlation, editorial-with-dissents, refusal}` ⟺ the matching `axioms_dropped` declaration — and the Arrow table lives as data in the checker, so the lens and the gate share one source of truth. The self-test: a ranking aggregation with empty `axioms_dropped` must fail.

### Example

A city planning office fans a zoning dispute to five stakeholder panels, each returning ranked preferences over seven land-use options with `input_type: ranking` declared. The synthesis wants to output "the consensus ranking." Arrow says no such neutral object exists; the typed fan-in forces the office to declare — in the published document — that it drops independence of irrelevant alternatives and scores positions, or that the planning director is the named authority. Either is legitimate; an unlabelled "consensus" is neither.

---

## Merge Ledger — Disposition of Every Candidate

Nothing is deleted silently; the decomposed view (`patterns/`, INDEX.md) is the extended body, and every disposition is recorded here.

### Draft's 25, dispositioned (17 counted + 1 primitive + 7 out)

| Entry | Disposition |
|---|---|
| The Etiquette Law | **Core, law** — criterion stated + negative-control clause (R1, R2) |
| Fan-out + Synthesis | **Foundational primitive, uncounted** (R1, R2; v5.1 ruling restored) |
| The Validity Window | **Core, law** — transition table + adjacency (R1, R2) |
| The Freeze | **Core, law** — cadenza delivery + `sha256sum -c` pin (R1, R2, R3) |
| Typed Force | **Core, law, narrowed** — `assigned_by` provenance; umbrella delegated (R1's cut answered, R2's split executed) |
| The Write-Time Record | **Core, law** — atomic transact wrapper, fail-closed audit (R1, R2) |
| Monitor Mix | **Core** — per-instance cadenzas, line-check gate (R1, R2) |
| Condorcet's Premise | **Core** — expanded-sheet routing, defined bounded estimator, pre-authored calibration (R1, R2, R3) |
| The Declared Window | **Core** — structured claim ledger replaces word ban (R1, R2) |
| The Gas-Free Certificate | **Core** — check-and-act atomic in one CLI wrapper (R1, R2) |
| Top-Down Demolition Order | **Core** — serialized self-chain driver, differently-authored re-derivation (R1) |
| Rent-Then-Commit | **Core** — skip_when lane routing, real self-chain form (R1, R3) |
| Vintage Overlay | **Core** — total-with-refusal lookup, pinned overlays, manifest-as-data (R1, R2; R3's cut motion defeated 2–1) |
| The Economic Injury Line | **Core** — pre-observation custody of the pinned table (R1, R2) |
| The Precedent Bench | **Core** — one adjudication authority, separated tables, honest registration semantics (R1, R2) |
| Demobilization Checkout | **Core** — four tables, commissioning pre-history, real hook attachment (R1, R2) |
| The Unprimed Falsifier | **Core** — split from Test Screening to Picture Lock (R2); lock half → The Freeze |
| The Dropped Axiom | **Core** — producer-declared input_type (R1); fold motion (R2) defeated 2–1 |
| Calling the Show | **Awaiting Primitives** — overlapped cue machine absent (R1, R2, R3) |
| Relieving the Watch | **Awaiting Primitives** — mid-sheet checkpoints absent (R1, R2; R3's dissent recorded) |
| The Strike Clock | **Awaiting Primitives** — timeout→tier transition absent (R1, R2, R3); inverted-DAG + curfew report preserved |
| Put-In | **Awaiting Primitives** — seat remap absent (R1, R2; R3's dissent recorded) |
| Command by Negation | **Demoted to idiom** under Mission Command + context economics (R1, R2, R3 unanimous) |
| The ATO Cycle | **Archived** — redesign condition stated: concurrent cycle identities + atomic rollover (R1, R2) |
| Cluster Lead | **Archived** — honesty clause promoted to corpus rule (R1, R3; R2's conditional not met) |

### v5.1 core, all retained in the decomposed view

Proof-Carrying Artifact (Typed Force's evidence form), Positive Transfer, The MIST Card, Fork-Evident History, The Errata Ledger, Standby–GO, The Attested Merge Gate, Join-Semilattice Merge, Behavioral Pre-Mortem, First Article Characterization, The Skeptical Oracle, Negative-Treatment Watch, Canon of Phases, The Fencing Token, The Black-Box Ledger, Flight Rules, Self-Stabilizing Custody, Hutchinson's Warning, Replication Licensing, Designation Is Authorization, Immune Checkpoint — plus the archived pool (Metered Merge, Effectivity Blocks, and the rest of the 111 files indexed in INDEX.md). Iteration-6 seams recorded in the draft (Standby–GO's three-way differentiation, Fencing Token ↔ Gas-Free, Errata Ledger ↔ Precedent Bench) stand.

### Iteration-6 archive pool — promotion queue unchanged

The Appraisal Room, The Fact Desk, Timeline Bell, Principal Chair, Extension Circuit, Green Wave, The Advance Sheet, The Soak Period, Heat-Sum Clock, Recurrent Selection, Cover-Crop Rotation, Containment Class Permit, Batch-Plant Stagger, Program Bus, Voice-Leading Contract, The Indistinguishable Pair, Budget-Feasible Routing, Two-Speed Targeting — archived, composable, in priority order per the draft's ranking. Budget-Feasible Routing remains the designated instrument-strategy proof candidate.

### Kills standing

The 27 expedition-level kills remain killed. The awaiting ledger's prior 13 rows stand; this iteration adds four (below) and strengthens two existing rows without fabricating primitives (mid-flight abort, runtime fan-out width — unchanged).

---

## Patterns Awaiting Primitives — iteration-6 additions

Added to `awaiting.md`, each with its blocking primitive and buildable approximation:

| Pattern | Blocked By | Buildable approximation / current boundary |
|---|---|---|
| Calling the Show | A recurring per-cue state machine with overlapped standby and hold-and-proceed-around | Standby–GO invoked once per cue inside a bounded self-chain; cue ledger as a workspace artifact advanced by a CLI movement; holds recorded as visible skips — the pipelined overlap and the bypass lane are the blocked part. |
| Relieving the Watch | Mid-sheet checkpointing (write-ahead hook or transactional sheet checkpoints) | Deck log as append-only JSONL written *as the sheet works*; movement-boundary reconciliation gates joining log claims to disk facts; `mzt recover` as the rehearsed spine. Review 3's dissent on record: "the crash-recovery pattern every long-running user needs." |
| The Strike Clock | A timeout→tier transition (timeouts fail sheets; they select nothing) | Inverted-DAG teardown order derived from the assembly DAG; per-movement budgets via `instrument_config.timeout_seconds`; job-level `max_wall_seconds` for scheduled runs; pack-for-next-run; curfew report as the successor's first input. The tier-arithmetic is the blocked half. |
| Put-In | Runtime seat remap (instrument assignment expands at parse time) | Track-sheet compile from incumbent artifacts; shadow run as an isolated job writing alongside, never over; structured diff gate with `--require-bijection`; cutover as a versioned score edit with the incumbent written into the next version's fallback chain. Review 3's dissent on record. |

---

## Proof Estate (corrected to disk)

`proof-scores/` holds **13** YAML scores (the draft said 14; both R1 and R3 counted). Both reviewing sheets independently ran `mzt validate` and agree on the split:

- **Passing (7):** cathedral-construction, firing-the-pass, join-semilattice-merge, live-relay, negative-treatment-watch, rashomon-gate, the-attested-merge-gate.
- **Failing (6):** dead-letter-quarantine, echelon-repair, prefabrication (folded multi-line command scalars); immune-cascade, shipyard-sequence, source-triangulation (dead `../../workspaces/` parent paths).

Dispositions: the six failures are **not live proofs** and are not counted as such. Repair order: the three path failures first (mechanical), the three folded-scalar failures second (validation-shape fixes). The reviewers' clustering findings stand and constrain the queue: three near-duplicate trios (tiered security audit; multi-lens synthesis; contract-frozen parallel build), six proofs sharing a live-publication tail, and the deserts untouched — adaptation (0), within-stage (0), instrument-strategy (0), concert-governance, destructive permits, structural demolition, per-consumer routing, bounded-context epistemics, measured panel dependence.

**The v6 proof queue, honestly stated: zero of six executed.** The queue stands, each entry now bound to the minimal-discriminating-score constraint (Reviews 1 and 2: a proof must fail when the pattern is removed while incidental machinery remains — stop rewarding monuments): Rent-Then-Commit (arithmetic-gate negative control: rent ≥ B without commit must fail), The Declared Window (an untagged global claim under `window: partial` must fail the join), The Dropped Axiom (empty `axioms_dropped` on a ranking must fail typecheck), Gas-Free Certificate (stale-permit fixture must refuse with nothing destroyed), Demobilization Checkout (a census row without disposition must fail the bijection), Budget-Feasible Routing (an assignment to an instrument lacking the task's technique tag must fail). Proof debt remains a **blocking requirement for v7** — and it is currently unmet, which is the honest current state of this corpus.

---

## Script Library (the debt, named at its true size)

Review 3 counted roughly 50 named scripts against the draft's "~20." The final core reduces the surface to **24 named scripts**, each an entry with an interface contract below; they are contracts to implement, not shipped files, and every pattern whose load-bearing gate reduces to one says so in its structure. Contracts follow one convention throughout: `--self-test` runs the pattern's negative-control fixtures and exits non-zero on any that unexpectedly pass; `--emit`/`--check-only` separate writing from verifying.

| Script | Pattern | Contract |
|---|---|---|
| `run-gates.sh` | Etiquette Law | `--lint --schema --tests`, `--self-test`, `--check-only`; exit code is the decision |
| `window.sh` | Validity Window | `stamp --subject --ttl --min-age --emit`; `probe --maturity-ledger --append`; `gate <window> --maturity --regenerate-on-expiry`; `manifest`; `--self-test` |
| `lock.sh` / `freeze-join.sh` | The Freeze | lock: `--pitches --emit --digest`; join: drafts `--against <sha256 file>` rejects hash drift |
| `force-typecheck.py` | Typed Force | rows `{force, assigned_by}`; rule↔ladder bijection; rejects unassigned rows |
| `effects.sh` | Write-Time Record | `transact --plan --ledger` (atomic, idempotent by effect_id); `audit --ledger --require-empty-residue`; `--self-test` |
| `mix.sh` | Monitor Mix | `channels --from --emit`; `assemble --channels --prescription --out` (refuses union-over-source); `line-check --dir --against` |
| `census.sh` / `demote.sh` | Condorcet's Premise | census: `--answers --ground-truth --emit` (co-occurrence matrix, ρ̄, n_eff, family census, demotion); demote: `--manifest --verdict` joins cited vs demoted rule |
| `window.sh manifest` / `claims.sh` | Declared Window | manifest from actual config+artifacts; `claims join --manifest --claims --prose` arithmetic + span join |
| `gas-free.sh` / `execute.sh` | Gas-Free | certify: `--plan --ttl --emit` (records certifier digest); execute: `--permit --plan` — check-and-act atomic, refuses stale/mismatched |
| `dep-graph.sh` / `order-rederive.sh` / `step.sh` / `full-oracle.sh` | Top-Down Demolition | plan as JSON; differently-authored re-derivation; step: sweep-empty → remove → re-derive → ledger; oracle: full suite |
| `ladder.sh` | Rent-Then-Commit | `probe --ledger --commitment`; `decide --state --emit` (`commit == (rent_paid >= B)`, ratio_bound 2); `settle --ledger` |
| `conditions.sh` / `overlay.sh` | Vintage Overlay | probe → conditions.yaml with digests; `select` total-with-refusal; `archive` → vintage record |
| `eil.sh` | Economic Injury Line | `verify --inputs --pinned-table` (refuses mismatch); `scout --sample --seed --ledger`; `verdict --table --ledger --emit` |
| `cite-join.sh` / `enroll.sh` / `notify.sh` | Precedent Bench | cite-join rejects dangling citations pre-reasoning; enroll: one serialized writer, `--atomic`, refuses factorless overrules; notify: supersession flags |
| `demob.sh` | Demobilization | `census`; `act --dispositions --receipts --permits-required-for`; `settle --liveness-must-return-empty`; `bijection --exact`; `seal --harvest --archive` |
| `notes.sh` | Unprimed Falsifier | `code --cards --density --emit`; `--self-test` |

Owner and shipping plan: the library needs a commissioning score that authors, self-tests, and versions these scripts — the same debt v5.1 flagged, now with contracts instead of names. It is the corpus's largest single dependency and it is visible here rather than in an appendix of regrets.

---

## Open Questions (v7)

1. **The curation ceiling after cuts.** 17 counted core against a 25 ceiling leaves 8 seats; the promotion queue (Appraisal Room, Fact Desk, Timeline Bell, Principal Chair first) is the ordered fill. Whether the ceiling itself survives v7's review is open.
2. **The law/pattern boundary.** Five laws now; the five un-minted convergences (pre-paid judgment, unprimed falsifier, artifacts-not-messages, ending-as-phase, two-axes-of-order) each gained a surviving carrier this iteration but not a second independent derivation. The minting criterion stands untested.
3. **The human-escalation seam — third iteration unowned.** Hold escalation, the impairment emergency, negation's surface order, waiver authority: at least four terminals resolve to "escalate to a human" with no governing pattern. Andon Cord (archive) is the ancestor; v7 should either mint the seam or close the question.
4. **Proof debt, now quantified.** Zero of six queue entries executed; six legacy proofs non-validating; three near-duplicate trios in the passing seven. v7 is blocked by this corpus's own rule until the queue's minimal discriminating proofs exist.
5. **Cadenza form variance — resolved.** The draft's Open Question 3 is closed by source: `cadenzas` is a SheetConfig field keyed by expanded sheet number, items `{file|directory, as, required}` (job.py:288-296). One form is canonical; the expedition's `required:` list-of-directories sketch was not a variant, it was an error.
6. **Divergences hunting their second domain.** Effectiveness-weighted time, licensed displacement, the proceeds rule, typed legal supersession remain single-witness; LLM orchestration candidates are recorded in the draft and stand.
7. **G7/G8 formalization.** Unknown-horizon and blind-maker generators are expressed through existing forces this iteration; whether they earn forces.md rows is v7's call, with Rent-Then-Commit and the Unprimed Falsifier as the candidate carriers.

---

## Coda: the corpus obeyed its own discovery, and this time its own dialect

The strongest evidence for the thesis remains that the six expeditions, working disjoint territories, *practiced* the grammar they were uncovering — trust converted to artifacts, claims typed, judgment pre-paid, endings accounted. The draft did all of that and still shipped structures that could not load, which is the other half of the lesson and now part of the record: a corpus that preaches engine facts over prose must re-verify its own YAML against source every iteration, because v5.1's Real Dialect section did not save v6's draft from fabricating against it — only the reviewers and a fresh source pass did. The correction discipline is now the corpus's own Precedent Bench holding: *verify the dialect at authorship, cite the source line, and let no structure ship on memory.*

Six domains, six voices, one grammar — cut where the structure was absent, strengthened where the idea outran its carrier, and the laws the harvest actually earned. *Grammar first, lexicon second, laws at curation — and the review is integrated.*

*— Sheet 13 of 13. The corpus is final.*
