# Rosetta Corpus Pattern Index

This index is what agents read FIRST when selecting patterns. It conveys WHEN and WHY to use each pattern, not HOW (that's in the individual pattern files).

**Iteration 6 additions (2026-09-04):** four foundational laws (The Validity Window, The Freeze, Typed Force, The Write-Time Record), three communication patterns (Monitor Mix, Condorcet's Premise, The Declared Window), two score-level (The Gas-Free Certificate, Top-Down Demolition Order), three adaptation (Rent-Then-Commit, Vintage Overlay, The Economic Injury Line), two concert-level (The Precedent Bench, Demobilization Checkout), one iteration (The Unprimed Falsifier), one within-stage (The Dropped Axiom). Calling the Show, Relieving the Watch, The Strike Clock, and Put-In moved to Patterns Awaiting Primitives; Command by Negation is an idiom under Mission Command; The ATO Cycle and Cluster Lead are archived. Core count: 17 counted entries + Fan-out + Synthesis as uncounted primitive.

Each entry shows:
- **Problem**: The coordination problem this pattern addresses
- **Signals**: When you would reach for this pattern (symptoms or situations)
- **Key compositions**: Other patterns this frequently combines with

Patterns are grouped by **scale** — the coordination scope at which they operate.

---

## Foundational

Primitive coordination moves that other patterns wrap or specialize.

**Fan-out + Synthesis**
- Problem: Work that could be parallelized is done sequentially, or parallel outputs remain fragmented without meaningful integration.
- Signals: problem decomposes into independent sub-problems; sub-problems can be worked simultaneously; diverse perspectives must be integrated, not concatenated
- Key compositions: Join-Semilattice Merge, The Attested Merge Gate, The Skeptical Oracle, Proof-Carrying Artifact

**The Etiquette Law**
- Problem: Deterministic protocol checks are given to LLM instruments that can hallucinate them, making the coordination layer no more reliable than the performers it coordinates.
- Signals: any check whose result could be a shell exit code; a gate described in prose inside a prompt; a fallback from a deterministic instrument to an LLM
- Key compositions: Every core pattern

**The Validity Window**
- Problem: Pipelines hold expirable state — tokens, permits, freshness-bound context, generated datasets — and silently reuse it after it expires.
- Signals: state whose safety or truth depends on when it was created; a TTL or freshness bound mentioned only in prose; retry or resume paths that re-present old artifacts
- Key compositions: The Gas-Free Certificate, The Declared Window, Effectivity Blocks

**The Freeze**
- Problem: Downstream work starts against upstream structure that is still moving, so finishers build on a version that stops existing.
- Signals: parallel specialists blocked on a structure still under negotiation; re-deciding structure later costs multiples of deciding it now; post-freeze edits arriving silently instead of as visible amendments
- Key compositions: Fork-Evident History, Prefabrication, The Unprimed Falsifier

**Typed Force**
- Problem: Authority-carrying and claim-carrying objects flow through pipelines without a type a gate can join on, so binding decisions and persuasive suggestions enforce identically.
- Signals: downstream consumers behave differently depending on what kind of thing this is, but the kind is not a field; a decision record indistinguishable from an observation; an aggregation presented as neutral
- Key compositions: The Precedent Bench, The Dropped Axiom, Proof-Carrying Artifact

**The Write-Time Record**
- Problem: Obligations and provenance are reconstructed by archaeology at end-of-life, after the people and context that created them are gone.
- Signals: provisioning creates removal obligations nobody writes down; a teardown plan that begins with "figure out what we created"; a manifest written from memory at the end of a campaign
- Key compositions: Demobilization Checkout, Fork-Evident History, Vintage Overlay

---

## Within-Stage

Patterns that structure a single sheet's prompt content or behavior.

**Commander's Intent Envelope**
- Problem: Instruction-based prompts break when the agent encounters conditions the prompt author didn't anticipate.
- Signals: task has more than one valid approach; inputs are variable-format or unpredictable; different instruments would solve this differently; want to validate outcomes, not methods
- Key compositions: Mission Command, Fan-out + Synthesis, After-Action Review

**Constraint Propagation Sweep**
- Problem: Agents generate from contradictory specifications because constraint conflicts remain hidden until expensive work is already complete.
- Signals: specifications from different stakeholders contain implicit contradictions; generated outputs fail because requirements conflicted silently; reconciling heterogeneous inputs costs less than reworking outputs; constraint set is large enough that pairwise conflicts are non-obvious
- Key compositions: Decision Propagation, CDCL Search, Rashomon Gate

**Decision Propagation**
- Problem: Downstream agents contradict upstream decisions because constraints are buried in prose rather than structured, parseable briefs.
- Signals: early decisions have compounding effects on later stages; downstream agents unknowingly violate upstream constraints; decisions are buried in prose output rather than structured artifacts; agents cannot tell which upstream decisions are load-bearing
- Key compositions: CDCL Search, CEGAR Loop (Progressive Refinement), Commander's Intent Envelope

**Immune Checkpoint**
- Problem: In a system with a powerful reviewer and an automated remediation path, the reviewer is the most dangerous instrument: a false-positive finding triggers rollback or deletion of healthy work.
- Signals: adversarial review feeding automated remediation — fix-PRs, scanner-gated deploys, takedowns; reviewer recall tuned high AND a downstream stage treating findings as verdicts rather than leads; an AI code reviewer opening fix-PRs directly
- Key compositions: The Skeptical Oracle, Andon Cord

**Quorum Trigger**
- Problem: Agents continue executing their original plan after accumulating evidence that makes continuing wasteful or dangerous.
- Signals: conditions discovered mid-task should change the approach; findings accumulate that individually seem minor but collectively demand action; agent needs to self-interrupt based on evidence density; severity of issues should trigger a mode switch, not just a note
- Key compositions: Andon Cord, Circuit Breaker, Immune Cascade

**Sugya Weave (Editorial Synthesis)**
- Problem: Diverse inputs need synthesis into an authoritative position with argued support, not neutral aggregation.
- Signals: multiple perspectives exist but need editorial judgment; summary isn't sufficient — need a supported position; inputs are diverse and require interpretation; neutrality would hide necessary judgment calls
- Key compositions: Fan-out + Synthesis, Source Triangulation, Rashomon Gate

**The Dropped Axiom**
- Problem: Every fan-in embodies an aggregation function constrained by theorems that do not care about intentions, and the synthesis presents its concealed choice as neutrality.
- Signals: sheets expressing rankings, priorities, or multi-premise verdicts; a synthesis that believes it is "just combining"; an unlabelled "consensus" output
- Key compositions: Typed Force, Fan-out + Synthesis, Sugya Weave (Editorial Synthesis)

---

## Score-Level

Patterns that arrange multiple sheets within a single score.

**Barn Raising**
- Problem: Parallel work streams produce inconsistent structure and style when each agent makes independent convention choices.
- Signals: parallel agents will work on similar types of artifacts; consistency in naming, structure, or style matters for integration; each agent might make reasonable but incompatible choices; prefabrication contracts aren't enough — need broader standards
- Key compositions: Prefabrication, Mission Command, Lines of Effort

**Behavioral Pre-Mortem**
- Problem: Mechanism interactions — concurrency windows, skip/fallback interplay, self-chain livelock — are invisible in YAML source and kill in production.
- Signals: a DAG where mechanisms interact: concurrency caps meeting shared regions; skip_when conditions interacting with fallback chains; self-chain loop conditions that could livelock; recurring schedules whose leases could double-fire
- Key compositions: Self-Stabilizing Custody, The Etiquette Law

**Canary Probe**
- Problem: Full-scale execution risks loss of resources and time when pipeline changes or output formats are unproven.
- Signals: batch processing many items with unproven pipeline; pipeline changes with uncertain format impact; high cost of full-scale failure; need validated evidence before full commitment
- Key compositions: Progressive Rollout, Dead Letter Quarantine, Speculative Hedge

**Clash Detection**
- Problem: Parallel tracks produce conflicting artifacts that break integration, and discovering conflicts during integration is expensive.
- Signals: parallel work needs to integrate but conflicts are unpredictable; integration testing is expensive; contracts can't anticipate all conflict modes; need to detect conflicts before attempting merge
- Key compositions: Prefabrication, Andon Cord, The Etiquette Law

**Closed-Loop Call**
- Problem: Semantic drift across pipeline stages when consumers misunderstand producer outputs.
- Signals: handoff fidelity is critical; semantic drift is a real risk; stages have non-obvious dependencies; previous stage outputs are ambiguous
- Key compositions: Prefabrication, Relay Zone, Succession Pipeline

**Composting Cascade**
- Problem: Phase transitions in iterative work need measurable readiness signals rather than time-based or manual progression decisions.
- Signals: phase transitions are time-based or manual, not metrics-driven; unclear when simple work is complete and should escalate to complex restructuring; churn rates don't drive phase changes, even when they indicate ongoing work; workspace readiness isn't observable
- Key compositions: The Etiquette Law, Succession Pipeline, Echelon Repair

**Concurrent Count**
- Problem: A single inventory count cannot distinguish a real total from omissions caused by one traversal or observer.
- Signals: completeness matters; two independent enumerations are affordable; a count mismatch can be narrowed by partitions
- Key compositions: The Skeptical Oracle

**Configuration Control Board**
- Problem: Configuration changes cross a shared boundary without one serialized authority, so individually reasonable edits combine into an incoherent active configuration.
- Signals: several writers propose changes to one configuration corpus; a bad change can affect many downstream sheets; approval and application must be distinguishable
- Key compositions: Flight Rules

**Dead Letter Quarantine**
- Problem: Batch processing repeatedly fails on the same items because no systematic analysis identifies root causes or adapts strategy.
- Signals: some items consistently fail across retries; batch processing has persistent partial failures; retry loops waste resources on unfixable items; no visibility into why certain items fail while others succeed; failures seem random but may have underlying patterns
- Key compositions: Triage Gate, Screening Cascade, Circuit Breaker, Immune Cascade, After-Action Review

**Dormancy Gate**
- Problem: External prerequisites are not immediately available, but work cannot safely proceed without them.
- Signals: downstream work depends on external system state; prerequisites will eventually be satisfied but are not immediate; need to wait and retry, not fail outright
- Key compositions: Read-and-React, Shipyard Sequence

**Firing the Pass**
- Problem: Forward scheduling discovers too late that prerequisite work cannot fit before a fixed release instant.
- Signals: the terminal date is fixed; stage durations have credible upper bounds; late work has explicit cut or degrade options
- Key compositions: Graceful Retreat, Standby–GO

**First Article Characterization**
- Problem: Validating each item of a large homogeneous fan-out from first principles is unaffordable, and validating none is unacceptable.
- Signals: fan-out volume work under a new or changed configuration; N report instances, N translations, N generated artifacts of one kind; a genuine shared configuration across the population
- Key compositions: Standby–GO, The Skeptical Oracle, The Attested Merge Gate

**Globally-Typed Choreography**
- Problem: Every local handoff looks plausible while the rendered score graph contains an unmet need, type mismatch, or dependency deadlock.
- Signals: many stages exchange typed artifacts; local validation passes but integration stalls; the rendered DAG is available before execution
- Key compositions: Proof-Carrying Artifact, Behavioral Pre-Mortem

**Graceful Retreat**
- Problem: Long-running work risks total failure on hard deadlines unless tiers of acceptable output are planned in advance.
- Signals: work has hard time deadlines where partial output has value; downstream pipeline stages can adapt to variable completeness; attempting full completion might waste resources or miss deadlines
- Key compositions: Andon Cord, Dead Letter Quarantine, Cathedral Construction

**Join-Semilattice Merge**
- Problem: The fan-in point is both a bottleneck and a trust point: merging concurrent writers requires arbitration that can destroy concurrent work.
- Signals: genuinely additive facts: findings keyed by ID, coverage observations, disjoint-segment translations; isolated writers appending disjoint records; concurrent updates delivered in any order, possibly duplicated
- Key compositions: Fan-out + Synthesis, The Attested Merge Gate

**Live Relay**
- Problem: Sequential creative agents lose artistic continuity or individual authority because handoffs preserve either substrate or voice, but not the living identity of the performance.
- Signals: work is a sustained creative performance over time; different sections benefit from different creative voices; continuity of identity matters more than continuity of raw substrate; gaps between agents would be detectable by the audience
- Key compositions: Mission Command, Stigmergic Workspace, Succession Pipeline, The Etiquette Law

**Mission Command**
- Problem: Centralized instruction-following breaks when agents face conditions the planner didn't anticipate.
- Signals: tasks require agent judgment and conditions may vary; validation should check outcomes, not methods; multiple agents must coordinate around shared intent; top-down instructions are too brittle for variable conditions
- Key compositions: After-Action Review, Barn Raising, Prefabrication

**Nurse Log**
- Problem: Downstream stages waste resources redoing common preparation work because no shared substrate exists.
- Signals: multiple stages need the same research or data collection; agents are duplicating preparation work; downstream work is blocked waiting for common prerequisites
- Key compositions: Fermentation Relay, Fan-out + Synthesis

**Prefabrication**
- Problem: Parallel tracks produce incompatible outputs because no shared interface contract exists before work begins.
- Signals: parallel work must produce compatible outputs; integration fails due to interface mismatches; tracks can't communicate during development; neither track depends on the other's code
- Key compositions: The Attested Merge Gate, Barn Raising, Clash Detection, Mission Command

**Quorum Consensus**
- Problem: Partial agent failure should not block the pipeline when majority agreement is sufficient.
- Signals: fan-out agents may fail unpredictably; partial failure shouldn't block downstream stages; need to proceed with majority agreement; some agents' failures are acceptable if quorum reached
- Key compositions: Triage Gate, Source Triangulation, Fan-out + Synthesis

**Rashomon Gate**
- Problem: Single-frame analysis produces unreliable conclusions when the optimal analytical perspective is unknown.
- Signals: the right analytical frame is unknown; multiple valid perspectives exist (security, performance, maintainability); risk is getting the right answer from the wrong frame; need to distinguish genuine ambiguity from frame artifacts
- Key compositions: Source Triangulation, Sugya Weave (Editorial Synthesis), Commander's Intent Envelope

**Reconnaissance Pull**
- Problem: Planning without prior exploration risks misaligned approaches and wasted effort.
- Signals: task structure and complexity are unclear; initial exploration costs are low relative to execution; approach is not obvious from requirements alone
- Key compositions: Mission Command, Canary Probe

**Red Team / Blue Team**
- Problem: Artifacts tested by known adversaries pass trivially; unknown adversaries reveal real flaws.
- Signals: testing is too predictable when defenders know the attacks; need to find vulnerabilities that prepared defense would miss; want realistic stress-testing where defenders work blind
- Key compositions: After-Action Review, Immune Cascade

**Relay Zone**
- Problem: Cumulative outputs across pipeline stages exceed context window limits, degrading downstream agent performance.
- Signals: pipeline outputs growing too large for downstream context windows; later stages receiving more context than they can effectively use; information from early stages drowning out recent findings; need to preserve key findings while discarding volume
- Key compositions: Fan-out + Synthesis, Forward Observer, Screening Cascade

**Shipyard Sequence**
- Problem: Expensive fan-out proceeds on a broken foundation, wasting resources on downstream work that will fail.
- Signals: downstream fan-out is expensive; foundation must be solid before scaling work; need real validation tools, not LLM judgment; costs multiply when defects reach later stages
- Key compositions: Succession Pipeline, Dormancy Gate, Triage Gate

**Sign-Off Chain Against the Hard Date**
- Problem: A hard deadline collapses independent review obligations into one vague approval, hiding which failure class was knowingly waived.
- Signals: release date cannot move; several reviewers own disjoint risk classes; some defects may be waived but must remain attributable
- Key compositions: The Attested Merge Gate

**Source Triangulation**
- Problem: Single-source analysis cannot detect contradictions between what code does, documentation says, and tests prove.
- Signals: technical claims need independent verification; multiple source types exist (code, docs, tests, benchmarks); single perspective might miss contradictions; need to categorize claims as corroborated vs uncorroborated
- Key compositions: Rashomon Gate, Triage Gate, Sugya Weave (Editorial Synthesis)

**Speculative Hedge**
- Problem: Choosing one approach that fails requires expensive restart from scratch, wasting the initial attempt's cost.
- Signals: uncertain which approach will work for this problem; starting over after failed approach costs more than running both; need guaranteed progress despite approach uncertainty; multiple valid strategies exist but success is unpredictable
- Key compositions: Canary Probe

**Succession Pipeline**
- Problem: Work requires sequential substrate transformations, but unstructured execution produces outputs incompatible with downstream stages.
- Signals: each stage needs fundamentally different methods; one stage's output becomes the next stage's input substrate; stages have categorical differences, not just detail levels; work resembles ecological succession with distinct phases
- Key compositions: Shipyard Sequence, Barn Raising

**Talmudic Page**
- Problem: Multiple perspectives on an artifact produce disconnected analyses when commentaries reference only the source, not each other.
- Signals: primary artifact needs multi-layer annotation; analysis requires multiple perspectives anchored to one text; commentaries should reference both source and each other; single-perspective analysis is insufficient
- Key compositions: Sugya Weave (Editorial Synthesis), Fan-out + Synthesis

**The Attested Merge Gate**
- Problem: Parallel writers produce artifacts that must compose, and trusting their self-reports lets incompatible work merge.
- Signals: N different hands producing artifacts against a shared contract; an interface writable before the work starts; multi-module builds, multi-author documents, multi-vendor assembly
- Key compositions: Join-Semilattice Merge, First Article Characterization, Prefabrication

**The Skeptical Oracle**
- Problem: Vendor-diverse advisors' findings cannot enter the record without importing their hallucinations.
- Signals: vendor-diverse review fan-outs; LLM-judge ensembles judging anything mechanically reproducible; you want the union of different models' coverage without inheriting any model's failures
- Key compositions: Proof-Carrying Artifact, Immune Checkpoint

**Triage Gate**
- Problem: Fan-out produces mixed-quality outputs but synthesis processes all outputs regardless of quality, wasting resources.
- Signals: fan-out produces wildly varying output quality; synthesis stage is expensive and shouldn't process garbage; some outputs need rework, others are ready; structural quality checks are definable
- Key compositions: Immune Cascade, Fan-out + Synthesis, Relay Zone

**The Gas-Free Certificate**
- Problem: Destructive operations run on the strength of a check that passed earlier, against a world that has since moved.
- Signals: rm, force-push, schema-drop, secret-revoke, teardown ahead; "the check passed earlier" is load-bearing for something irreversible; a retried or resumed run about to reuse yesterday's verification
- Key compositions: The Validity Window, The Fencing Token, Standby–GO

**Top-Down Demolition Order**
- Problem: Removal order is computed from commit history, so removing a shared thing succeeds while dependents that quietly stood on it lose their footing.
- Signals: retiring a shared library, column, endpoint, schema, or base image; the danger is not "removal fails" but "removal succeeds and consumers break silently"; reverse-chronology undo proposed for something with internal structure
- Key compositions: Saga Compensation Chain, Behavioral Pre-Mortem, The Soak Period (archive)

---

## Concert-Level

Patterns that coordinate multiple scores in a campaign.

**Canon of Phases**
- Problem: A continuous stream of work outlives any single worker's endurance — context, budget, or lease — and restarts from zero at every boundary.
- Signals: an always-on triage queue, rolling literature watch, moderation across a day, long migrations in shifts; the stream must never restart from zero; no single score should run for a day straight
- Key compositions: Positive Transfer, Replication Licensing

**Lines of Effort**
- Problem: Parallel campaign workstreams drift apart without convergence mechanisms connecting distinct efforts toward a unified end state.
- Signals: campaign has distinct workstreams with different objectives; parallel efforts must converge toward a shared end state; workstreams need autonomy but unified direction; coordination should happen through shared state, not message passing
- Key compositions: Season Bible, After-Action Review, Barn Raising

**Mycorrhizal Reciprocity**
- Problem: Participants consume shared quality improvements without returning evidence or maintenance, so the shared substrate degrades.
- Signals: several scores reuse one shared corpus; contributions and consumption are measurable; scarce review capacity can be allocated conditionally
- Key compositions: Season Bible

**Negative-Treatment Watch**
- Problem: Admitted claims silently rot as their external sources move, and derived work keeps building on stale truth.
- Signals: long-lived corpora whose truth depends on mutable externals; legal research, scientific claim bases, compliance baselines, dependency manifests, docs with code anchors; a missed audit cycle must be visible, not silent
- Key compositions: The Errata Ledger, Flight Rules, Proof-Carrying Artifact

**Progressive Rollout**
- Problem: Full deployment before validation risks large-scale failure; incremental rollout with monitoring gates progression but requires coordinating batch selection, execution, and go/no-go decisions across phases.
- Signals: works on 5 doesn't guarantee works on 500; need to detect scaling issues before full deployment; rollback from 100% deployment is expensive; early validation could prevent large-scale failures
- Key compositions: Canary Probe, Dead Letter Quarantine

**Saga Compensation Chain**
- Problem: Partial completion of a multi-score concert leaves inconsistent shared state unless each committed effect has durable, reverse-ordered compensation authority.
- Signals: concert scores produce externally visible side effects; partial completion is worse than a compensating forward action; manual cleanup after failure is expensive or error-prone; each effect can name an idempotent compensating operation
- Key compositions: After-Action Review, The Black-Box Ledger, Replication Licensing

**Season Bible**
- Problem: Multi-score campaigns lose continuity because agents lack shared memory of prior decisions and evolving constraints.
- Signals: scores make decisions inconsistent with earlier work; agents repeat mistakes or ignore prior learnings; no central record of evolving state across campaign; continuity errors accumulate as work progresses
- Key compositions: Lines of Effort, Relay Zone, Cathedral Construction

**Systemic Acquired Resistance**
- Problem: Failures encountered in one score don't inform subsequent scores in a concert, causing repeated failures across the campaign.
- Signals: scores in a concert face similar threats; first-encounter failure cost is high; failures repeat across scores in a concert; no mechanism to share failure recovery
- Key compositions: After-Action Review, Back-Slopping (Learning Inheritance), Circuit Breaker

**Transfer of Command**
- Problem: Planned succession changes the named operator but leaves tacit state, pending decisions, and incident context behind.
- Signals: ownership changes at a known time; work spans shifts or deployments; the successor must act immediately without re-discovery
- Key compositions: The Black-Box Ledger, Positive Transfer

**The Precedent Bench**
- Problem: A long campaign re-litigates settled decisions every score, or contradicts them silently — because decisions carry no typed force and no supersession record.
- Signals: "what have we already decided?" answered by archaeology; later scores contradicting earlier load-bearing decisions unknowingly; corrections and overrulings indistinguishable in the record
- Key compositions: Typed Force, The Errata Ledger, Fork-Evident History

**Demobilization Checkout**
- Problem: Concerts end by stopping being visible, leaving orphaned processes, live leases firing into dead workspaces, and credentials outliving their purpose.
- Signals: a campaign with physical footprint (daemons, leases, clones, containers, credentials); retirement has no owner; "the run ended" treated as if it meant "the run failed"
- Key compositions: The Write-Time Record, The Gas-Free Certificate, Saga Compensation Chain

---

## Communication

Patterns that enable coordination through durable workspace state and evidence.

**Continuity Ledger**
- Problem: Parallel authors silently contradict shared world facts because prose canon has no typed, serialized assertion boundary.
- Signals: many writers depend on persistent facts; facts have different types and update rules; contradictions appear only during late synthesis
- Key compositions: Join-Semilattice Merge, The Errata Ledger

**Custody Transfer with Seals**
- Problem: A receiver acknowledges custody without proving that the bytes received are the bytes the sender released.
- Signals: artifact crosses a process, score, or human boundary; transport may truncate or replace files; point-in-time transfer integrity matters more than full history
- Key compositions: Positive Transfer, Fork-Evident History

**Fork-Evident History**
- Problem: A retroactively edited history is undetectable, so downstream consumers cannot know they saw the same claims as everyone else.
- Signals: self-chaining scores where iteration N+1 must not silently weaken iteration N; long concerts whose claims are consumed by multiple downstream parties; corrections-heavy domains where the honest correction cites what it supersedes
- Key compositions: The Errata Ledger, Proof-Carrying Artifact, Self-Stabilizing Custody

**Is-Line-Clear**
- Problem: A sender infers that a shared medium is free and transmits into an unobserved conflicting operation.
- Signals: two parties share a scarce mutable channel; only the counterparty can attest readiness; silence is ambiguous rather than permission
- Key compositions: Standby–GO

**Positive Transfer**
- Problem: Work moving between executors passes through moments with no owner, and a failed handoff silently drops custody.
- Signals: work crossing a trust boundary — different instruments, scores, or teams; the cost of a moment without an owner exceeds the cost of a moment with two; shift boundaries, score-to-score chains, escalation from worker to human
- Key compositions: Canon of Phases, The Black-Box Ledger

**Proof-Carrying Artifact**
- Problem: Consumers must either trust producer claims across a trust boundary or re-derive the work at full cost.
- Signals: any handoff where the cost of being wrong exceeds the cost of checking; claims like 'tests pass' or 'this number came from the source'; a downstream sheet about to build on an upstream assertion
- Key compositions: Fork-Evident History, Flight Rules, The Skeptical Oracle, Fan-out + Synthesis

**Rejoinder Ledger**
- Problem: A response claims to address review findings while omitting, duplicating, or answering a different finding under similar prose.
- Signals: large review sets require formal response; closure depends on every finding receiving one disposition; rewording makes manual matching unreliable
- Key compositions: The Skeptical Oracle

**Standby–GO**
- Problem: A one-phase cue discovers receiver readiness at the moment of irreversible execution.
- Signals: preparation must overlap live performance and the switch must be atomic; content freeze to publish cutover; staging to production rotation; cache rebuild under traffic; build buffer B while buffer A serves
- Key compositions: First Article Characterization, Hutchinson's Warning

**Stigmergic Workspace**
- Problem: Parallel agents duplicate effort or produce conflicts because they lack visibility into each other's progress and decisions.
- Signals: parallel agents need loose coordination without direct messaging; workspace files already capture meaningful state other agents need; real-time coordination would create bottlenecks; agents react to each other's outputs, not each other's messages
- Key compositions: Barn Raising, Lines of Effort

**The Errata Ledger**
- Problem: A correction that silently rewrites the text lies about its own history, and a correction notice nobody consumes leaves derived copies wrong.
- Signals: a canonical document with derived translations, summaries, or extracts; syndicated anything; a downstream copy that would otherwise drift from corrected truth
- Key compositions: Fork-Evident History, Negative-Treatment Watch, Proof-Carrying Artifact

**The MIST Card**
- Problem: A retry loop treats an arriving item as fresh and repeats an intervention that already failed, wasting the window or compounding damage.
- Signals: any score-authored retry, recovery chain, or multi-stage escalation; the next handler must know what previous handlers already tried; two attempts where one should do is itself a hunt signal
- Key compositions: The Black-Box Ledger, Flight Rules, Replication Licensing

**Variant Apparatus**
- Problem: Synthesis erases material dissent to produce one smooth deliverable, depriving consumers of the conditions under which the conclusion changes.
- Signals: credible witnesses disagree; the disagreement affects action; a single conclusion would conceal assumptions rather than resolve them
- Key compositions: Sugya Weave (Editorial Synthesis), Talmudic Page

**Monitor Mix**
- Problem: Many consumers need different slices of one shared accumulating state, and each currently receives either everything or someone else's slice.
- Signals: one shared state, many consumers with genuinely different depth needs; a summarizer drowning in function bodies while an implementer starves of them; routing decisions made ad hoc per run instead of written down
- Key compositions: Relay Zone, The Declared Window

**Condorcet's Premise**
- Problem: Voting authority is assumed from panel size, but correlated panels ratify errors with majority confidence instead of averaging them out.
- Signals: a fan-in that will vote, over claims that cannot be mechanically reconstructed; a "vendor-diverse" claim never family-probed; n reviewers from what turns out to be one model family
- Key compositions: The Skeptical Oracle, Rashomon Gate, The Dropped Axiom

**The Declared Window**
- Problem: Synthesis sheets read bounded lookback over large runs and then make global claims their window cannot support.
- Signals: streak/trend/consensus language in late sheets ("consistently", "across the run", "no objections"); a truncation whose consumers quote "the" upstream output; a silent exact-looking guess chosen over a declared approximation
- Key compositions: The Black-Box Ledger, Hutchinson's Warning

---

## Adaptation

Patterns that adjust behavior mid-execution based on runtime conditions.

**Allostatic Setpoint**
- Problem: A system holds a fixed quality or throughput target while cumulative wear rises invisibly until performance collapses.
- Signals: meeting the target consumes a degrading reserve; maintenance debt accumulates across cycles; the safe target should change with measured wear
- Key compositions: Hutchinson's Warning

**Andon Cord**
- Problem: Validation failures are retried blindly without diagnosing root cause, wasting resources on repeated errors.
- Signals: validation failures repeat the same error across retries; failure output is informative but gets ignored; retry costs are high (~$1+ per attempt); agent needs corrective guidance, not just another attempt
- Key compositions: Circuit Breaker, Quorum Trigger, Commissioning Cascade

**Circuit Breaker**
- Problem: Long-running jobs fail catastrophically or waste resources when instruments become unavailable mid-execution.
- Signals: backend outages cause sudden job failures; primary instrument becomes unavailable mid-concert; self-chaining jobs lose progress when instruments fail; cost overruns from repeated retries on broken instruments
- Key compositions: Dead Letter Quarantine, Echelon Repair, Speculative Hedge

**Effectivity Blocks**
- Problem: A manifest or rule is treated as timeless even though it is valid only for a bounded configuration, population, or interval.
- Signals: a reference artifact certifies only one configuration family; rules change while work remains in flight; retries may observe a different active manifest
- Key compositions: Flight Rules, First Article Characterization, Replication Licensing

**Flight Rules**
- Problem: Under failure, deliberation is the enemy: the response is re-derived under duress instead of looked up from pre-negotiated, versioned condition-action bindings.
- Signals: the same failures recur and the correct response is knowable in advance; incident response, failure recovery, go/no-go criteria; a responder who reasons for ten minutes where reading for ten seconds would do
- Key compositions: The Black-Box Ledger, The MIST Card, After-Action Review

**Fragmentary Order (FRAGO)**
- Problem: Plans become stale mid-execution when discovered conditions diverge from expectations but no mechanism exists for targeted correction without full replanning.
- Signals: earlier stages produced results that invalidate downstream assumptions; the plan is partially wrong but not wrong enough to discard; downstream agents need adjusted guidance, not a completely new plan; conditions discovered mid-execution were not anticipated by the original plan
- Key compositions: Read-and-React, Lines of Effort, Mission Command

**Hutchinson's Warning**
- Problem: Negative feedback with lag oscillates: a controller fed by lagged telemetry throttles hard, bursts through, and throttles hard forever.
- Signals: a large multi-movement score with a genuinely shared budget — money, wall-clock, or context; spend telemetry arrives with lag (batched billing, periodic usage polls) — which is everywhere; feeding work into anything with a real capacity curve: paid APIs, human review, CI pools
- Key compositions: The Etiquette Law, Standby–GO

**Metered Merge**
- Problem: A fixed merge admission rate either starves available capacity or overloads the consumer when measured congestion changes with delay.
- Signals: a queue feeds a bounded merge or review consumer; occupancy can be measured periodically; admission rate can change between leased batches
- Key compositions: Hutchinson's Warning

**Read-and-React**
- Problem: Downstream agents follow fixed behavior regardless of upstream results because their prompts don't instruct them to inspect and adapt to workspace state.
- Signals: downstream behavior should change based on upstream results; adaptation path is not known before execution begins; workspace state determines which work is needed next; agents proceed with default behavior ignoring what previous stages produced
- Key compositions: Triage Gate, Fragmentary Order (FRAGO), Dormancy Gate

**Self-Stabilizing Custody**
- Problem: Crash, corruption, and restart are treated as exceptional events requiring an exceptional recovery protocol, when they are just arbitrary states the ordinary rules should leave.
- Signals: conductor restarts mid-concert; workspaces resumed after host failure; global rollback costs more than local re-derivation; recovery from PARTIALLY corrupt state — where checkpoint-restore fails
- Key compositions: The Fencing Token, The Black-Box Ledger, Behavioral Pre-Mortem

**The Black-Box Ledger**
- Problem: After the executor dies, what happened is knowable only from survivor testimony — reconstructed memory — unless a channel that does not share the executor's fate recorded it continuously.
- Signals: any long orchestration whose post-failure value depends on knowing what actually happened; production incidents, adversarial review concerts, audit trails; failure analysis must be grounded rather than narrated
- Key compositions: Flight Rules, The MIST Card, Positive Transfer

**The Fencing Token**
- Problem: A paused or retried executor cannot observe its own expiry and silently overwrites newer work with older, slower work.
- Signals: a shared mutable surface two sequenced executors may touch; workspace regions republished by a retry after timeout; scheduled jobs whose lease lapsed while the job kept running
- Key compositions: Self-Stabilizing Custody, Replication Licensing

**Rent-Then-Commit**
- Problem: A repeated per-use cost and a one-time commitment cost face an unknown horizon, and no rule says when committing becomes provably defensible.
- Signals: cheap retries that might go on forever vs one expensive settlement; recompute-every-run vs freeze-a-contract decisions; spot vs reserved capacity across a chain of unknown length
- Key compositions: Circuit Breaker, Speculative Hedge, The Economic Injury Line

**Vintage Overlay**
- Problem: A canonical pipeline re-runs on a cadence under external conditions that vary, and each run improvises tuning instead of selecting from pre-authored condition-bound parameter sets.
- Signals: the pipeline is stable but the conditions are not; conditions are mechanically measurable (versions, rate climates, volatility); per-vintage tuning would beat per-run improvisation
- Key compositions: Effectivity Blocks, The Write-Time Record, Season Bible

**The Economic Injury Line**
- Problem: Defensive recurring work responds to felt damage instead of a threshold computed from unit economics before the season began.
- Signals: real unit costs on both sides — intervening and damage; most intervals honestly deserve NO action; a bounded sampling protocol can estimate the pressure cheaply
- Key compositions: Rent-Then-Commit, Hutchinson's Warning, Immune Cascade

---

## Instrument-Strategy

Patterns that match instrument capabilities and authority to task requirements.

**Commissioning Cascade**
- Problem: Different validation scopes require different tools; single-pass validation misses issues or wastes resources.
- Signals: unit tests pass but integration fails; validation is slow because all scopes use expensive instruments; can't diagnose failures because all tests run together; need different rigor levels for different scopes
- Key compositions: Echelon Repair, Shipyard Sequence, The Etiquette Law

**Designation Is Authorization**
- Problem: Authority expressed as a list of rights the subject names lets authority leak through any confused intermediary.
- Signals: mixed-instrument fan-outs where sheets differ in trust; a cheap summarizer touching sensitive context; tool attachment that must be scoped; technique/skill injection that must not be ambient
- Key compositions: Proof-Carrying Artifact, The Etiquette Law

**Echelon Repair**
- Problem: Expensive instruments waste resources on work that cheaper instruments could handle.
- Signals: work items vary wildly in difficulty; expensive instrument is wasted on trivial tasks; costs are high but most work is simple; need to triage before processing
- Key compositions: Commissioning Cascade, Fermentation Relay, Screening Cascade, Circuit Breaker

**Fermentation Relay**
- Problem: Expensive instruments waste resources fixing quality issues that cheap instruments created during initial processing.
- Signals: cheap instruments produce output too noisy for expensive stages to use directly; expensive instruments waste budget on noise filtering instead of core work; early outputs require multiple refinement steps before quality is acceptable; no single instrument choice works well across all pipeline stages
- Key compositions: Echelon Repair, Succession Pipeline, Screening Cascade

**Forward Observer**
- Problem: Expensive instruments waste resources reading raw input; cheap summarization can preserve actionable information.
- Signals: input exceeds available context window; expensive instrument required for main task; token costs dominate total cost; most input is redundant or low-value
- Key compositions: Relay Zone, Screening Cascade, Immune Cascade

**Immune Cascade**
- Problem: Expensive instruments waste resources on broad scanning when cheap preliminary work could narrow scope first.
- Signals: broad scanning is expensive but most issues are benign; don't know which findings warrant expensive investigation; need to narrow findings before expensive deep analysis
- Key compositions: Triage Gate, After-Action Review, Relay Zone

**Re-Tiering Decision**
- Problem: A population's risk tier changes item by item, leaving structurally similar items under inconsistent controls after systemic evidence appears.
- Signals: flag rate crosses a declared hold threshold; one cause affects a broad dependent population; classification authority must be separate from artifact existence
- Key compositions: Negative-Treatment Watch, Screening Cascade

**Screening Cascade**
- Problem: Difficulty emerges during processing; fixed upfront instruments waste expensive resources on simple work or fail on complex work.
- Signals: work items vary in difficulty but this only becomes clear during processing; cheap instruments can screen routine items but some need escalation to stronger capabilities; costs are high because you're using expensive instruments for work that doesn't warrant them; difficult work emerges during execution, not from upfront inspection
- Key compositions: Echelon Repair, Immune Cascade, Dead Letter Quarantine

**Vickrey Auction**
- Problem: Selecting an instrument without evidence wastes resources or produces inferior results when multiple candidates are viable.
- Signals: multiple instruments are available and it's unclear which performs best; instrument choice is based on guesswork, not evidence; cost or quality varies significantly across instruments for the same task
- Key compositions: Echelon Repair, Canary Probe

---

## Iteration

Patterns that structure repeated refinement and learning across execution cycles.

**After-Action Review**
- Problem: Execution insights are lost between iterations because no systematic reflection captures what worked, what failed, and why.
- Signals: same mistakes happen repeatedly across iterations; execution insights disappear after completion; teams don't know what actually worked or why it worked; improvement recommendations don't reach subsequent iterations
- Key compositions: Immune Cascade, Cathedral Construction, Back-Slopping (Learning Inheritance)

**Back-Slopping (Learning Inheritance)**
- Problem: Iterative processes lose hard-won insights because each iteration starts from scratch without accumulated learning.
- Signals: later iterations repeat mistakes from earlier ones; valuable insights discovered during work are lost between iterations; iterative process plateaus because it cannot build on prior discovery
- Key compositions: Cathedral Construction, CDCL Search, Systemic Acquired Resistance

**Cathedral Construction**
- Problem: Large artifacts cannot be produced in a single pass and require iterative construction toward a known target.
- Signals: artifact is too large to complete in one pass; work must be built incrementally toward a target; each iteration adds structural elements; need to track progress toward a known endpoint
- Key compositions: After-Action Review, Back-Slopping (Learning Inheritance), Memoization Cache

**CDCL Search**
- Problem: Iterative processes repeat the same failures because no mechanism captures and propagates failure patterns as constraints.
- Signals: same failures occur across retry attempts; retries don't help because nothing is learned; failures contain diagnostic information that could prevent recurrence; need to avoid known bad paths in subsequent iterations
- Key compositions: Back-Slopping (Learning Inheritance), After-Action Review, CEGAR Loop (Progressive Refinement)

**CEGAR Loop (Progressive Refinement)**
- Problem: Coarse-grained analysis produces spurious findings requiring expensive verification to distinguish real from false alarms.
- Signals: coarse analysis produces too many false alarms; expensive to verify every finding at fine grain; most findings disappear when abstraction is refined; need selective refinement, not full re-analysis
- Key compositions: Memoization Cache, CDCL Search, Immune Cascade

**Delphi Convergence**
- Problem: Multiple independent agents must converge without anchoring on early opinions.
- Signals: expert opinions vary widely and need to converge; agents anchor on initial assessments and won't update; single-round synthesis isn't achieving consensus
- Key compositions: Source Triangulation, Rashomon Gate

**Fixed-Point Iteration**
- Problem: Iterative refinement requires explicit convergence detection to avoid wasting iterations.
- Signals: repeated application produces improvements but stopping criterion is unclear; iterations are expensive and need measurable termination beyond fixed counts; output stabilizes after refinement but manual convergence checking is tedious
- Key compositions: CDCL Search, Cathedral Construction, Memoization Cache

**Memoization Cache**
- Problem: Self-chaining scores and iterative processes re-execute stages whose inputs haven't changed, wasting computation.
- Signals: self-chaining scores re-analyze unchanged modules wastefully; concert campaigns process overlapping inputs redundantly; CEGAR Loops re-examine stable abstraction regions unnecessarily; iterative refinement compounds costs when inputs don't change
- Key compositions: CEGAR Loop (Progressive Refinement), Cathedral Construction, Fixed-Point Iteration

**Prescribed-Fire Pulse**
- Problem: Low-grade workspace fuel accumulates until cleanup becomes a disruptive emergency instead of a bounded maintenance action.
- Signals: temporary artifacts and stale branches grow predictably; small maintenance bursts are cheaper than periodic reclamation; cleanup safety can be checked deterministically
- Key compositions: Stigmergic Workspace

**Rehearsal Spotlight**
- Problem: Iteration is expensive; reworking entire outputs wastes resources when only parts need refinement.
- Signals: iteration cycles are expensive; only specific sections need rework; most output is good but a few parts are weak; need to focus rework effort on problem areas
- Key compositions: Echelon Repair, Soil Maturity Index, CEGAR Loop (Progressive Refinement)

**Replication Licensing**
- Problem: A cycle counter cannot prevent a side-effectful cycle from happening twice, and naive retries duplicate deployments.
- Signals: any self-chaining or recurring score whose work stage has side effects that must be exactly-once per cycle; deploys, sends, publishes, billing events, state migrations; a conductor crash mid-stage would otherwise leave 'did the deploy happen?' answerable only by archaeology
- Key compositions: The Fencing Token, Canon of Phases

**Soil Maturity Index**
- Problem: Iterative processes lack domain-specific termination conditions beyond structural equality.
- Signals: iterative improvement plateaus on structural metrics but output lacks qualitative maturity; need to distinguish real convergence from mere structural stability; process converges structurally but hasn't achieved expected coherence or readiness; domain-specific maturity assessment required before proceeding to next phase
- Key compositions: Fixed-Point Iteration, Back-Slopping (Learning Inheritance), Delphi Convergence

**The Unprimed Falsifier**
- Problem: Makers cannot perceive their finished artifact — fluency hides the claims it makes — and internal evaluation shares the blind spot.
- Signals: anything read by humans whose makers are too close to it; "we think it's clear" has ever been wrong; self-evaluation and structural-equality checks both passing while users misread the thing
- Key compositions: The Freeze, Rehearsal Spotlight, The Declared Window

---

## Composition Clusters

Patterns that frequently compose together for specific purposes:

**Quality Assurance Pipeline:** Shipyard Sequence, Succession Pipeline, Triage Gate
- Sequential quality gates where foundation validation precedes expensive fan-out, classification routes outputs, and stage progression depends on quality thresholds.

**Cost-Optimized Processing:** Echelon Repair, Fermentation Relay, Screening Cascade
- Instrument tier matching where cheap instruments classify/screen, mid-tier refines, and expensive instruments handle only complex cases.

**Intent-Driven Coordination:** Mission Command, Commander's Intent Envelope, After-Action Review
- Decentralized execution around shared intent with outcome-focused validation and systematic learning capture.

**Parallel Work Integration:** Fan-out + Synthesis, Barn Raising, Prefabrication
- Consistent parallel execution where shared conventions prevent drift, interface contracts enable composition, and synthesis integrates diverse outputs.

**Failure Intelligence:** CDCL Search, Back-Slopping (Learning Inheritance), After-Action Review
- Learning from failure where constraints extracted from failures prevent recurrence and lessons propagate across iterations.

**Adaptive Recovery:** Andon Cord, Circuit Breaker, Dead Letter Quarantine
- Intelligent failure response where root-cause diagnosis replaces blind retry, instrument failures trigger fallbacks, and chronic failures are quarantined.

**Multi-Frame Analysis:** Rashomon Gate, Source Triangulation, Sugya Weave (Editorial Synthesis)
- Diverse perspective application where multiple frames reveal different insights, sources cross-validate claims, and editorial synthesis produces argued positions.

**Progressive Validation:** Canary Probe, Progressive Rollout, Speculative Hedge
- Incremental commitment where small-scale validation precedes full deployment, scaling progression is gated on evidence, and parallel approaches hedge uncertainty.

**Iterative Refinement:** Cathedral Construction, Fixed-Point Iteration, Memoization Cache
- Bounded iteration toward targets where convergence detection prevents waste, incremental construction scales to large artifacts, and caching avoids redundant work.

**Context Management:** Relay Zone, Forward Observer, Screening Cascade
- Information compression where cheap instruments pre-filter or summarize before expensive processing, preventing context overflow and reducing token costs.

**Evidence-Bearing Custody:** Proof-Carrying Artifact, Fork-Evident History, The Fencing Token
- Evidence admission, tamper-evident history, and epoch ordering make cross-boundary claims and writes independently checkable.

**Attested Parallel Merge:** The Attested Merge Gate, Join-Semilattice Merge, First Article Characterization
- Contract attestation, algebraic merge, and representative characterization reduce merge trust without serializing all production.

---

## Selection Guidance

When choosing patterns:

1. **Start with the problem, not the pattern name.** Read the signals — do they match your situation?
2. **Check the scale.** Foundational patterns define primitive moves; the remaining scales identify the coordination scope they control.
3. **Follow the compositions.** Each listed relationship is declared by the pattern's own frontmatter.
4. **Read the full pattern file.** This index tells you WHEN; the pattern file tells you HOW.
