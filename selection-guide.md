# Pattern Selection Guide

This guide helps you choose patterns based on **what you're trying to accomplish**, not what the patterns are called. Each problem type includes 2-3 pattern combinations that work well together.

---

## Getting Started: Five Essential Patterns

If you're new to orchestration, start with these five patterns in order. They cover the most common coordination problems and compose naturally:

| Pattern | Problem It Solves | When To Use It |
|---------|-------------------|----------------|
| **Fan-out + Synthesis** | Work could be parallelized but isn't, or parallel outputs remain fragmented | Problem decomposes into independent sub-problems; need to integrate diverse perspectives |
| **Shipyard Sequence** | Expensive work proceeds on a broken foundation, wasting resources | Downstream work is expensive; foundation must be solid before scaling |
| **The Etiquette Law** | Thinking instruments make deterministic protocol checks less reliable | A check can be expressed as a command with an exit status; protocol stages need empty AI fallback chains |
| **Canary Probe** | Full-scale execution risks loss when pipeline changes are unproven | Batch processing with unproven pipeline; high cost of full-scale failure |
| **Andon Cord** | Validation failures retry blindly without diagnosing root cause | Validation failures repeat the same error; failure output is informative but gets ignored |

**Why this order?** Fan-out + Synthesis teaches parallelization. Shipyard Sequence shows validation before scaling. The Etiquette Law establishes deterministic protocol ownership. Canary Probe introduces incremental commitment. Andon Cord closes the loop with intelligent failure handling.

---

## Iteration 7.1 Problem → Pattern Additions (Discover Pass 2, Cycle 7)

Twenty-one new patterns after three adversarial reviews (Practitioner, Skeptic, Newcomer); from 24 drafted — Firing the Pass evicted as a duplication (proven Sep 4), Staggered Quorum Spend cut (launches cannot be cancelled; benched as The Phased Quorum Wave), The Recovery Arc benched (checkpoint persistence unwired), The Shared Pulse ⊕ Datum Grid folded into The Shared Reference, Hotwash split in two. Problem-first, per this guide's rule.

| If your problem is… | Start with | Compose with |
|---|---|---|
| A late decision (human sign-off, slow validation) must stall commits but not work. | **The Cue Light** | Standby–GO (its parent), The Graded Ladder |
| Contamination is found after consumers already started, and rerouting is possible. | **The Contamination Wire** | Dead Letter Quarantine, The Validity Window |
| N parallel workers must agree on terms, schema, or phase without agreeing on content. | **The Shared Reference** (datum: immutable; pulse: versioned) | The Misclosure Ledger, Prefabrication |
| The plan changes mid-run and sheets are running under a version that no longer exists. | **The Change-Order Ledger** | The Negative Ledger, Configuration Control Board |
| About to spend on a large fan-out with an untested prompt+toolchain. | **Unison Drift** | Rashomon Gate, First Article Characterization |
| One contested judgment where a single reviewer's blind spot is the danger. | **The Dialectical Pair** | Rejoinder Ledger, The Editor's Disposition |
| Schema-valid garbage looks exactly like truth at volume. | **The Torque-Verify Pass** | Immune Cascade, Concurrent Count |
| "Skip it this run" is being decided ad hoc, under pressure, every run. | **The Dispatch Catalogue (MEL)** | Capability Census, The Validity Window |
| Small deviations individually fine but jointly breaching a declared margin. | **Dispatch with Declared Penalty (CDL)** | The Dispatch Catalogue (MEL), Capability Census |
| Verification spend compounds; budget pressure silently downgrades review. | **The Priced Verification Ladder** | Immune Cascade, Echelon Repair |
| Failure evidence accumulates with no consumer committed to act on it. | **The Hotwash Dispatch (Lesson Routing)** | After-Action Review, The Spent Lesson Checkout |
| Prompts carry remediated failures from many iterations back — context debt. | **The Spent Lesson Checkout** | The Hotwash Dispatch, The Validity Window |
| A small upstream artifact (schema, rubric, lexicon) parameterizes everything downstream. | **Keystone-First Sequencing** | Cathedral Construction, Prefabrication |
| An AI seam touches something irreversible and the check must never fail open. | **The Watchman's Gate** | Readback Before Commit, The Hold-Point Witness |
| A seam only an external human authority may open; the score must not self-sign. | **The Hold-Point Witness** | Transfer of Command at the Seam, The Graded Ladder |
| Many advisories, but the output must be ONE action, not one document. | **The Editor's Disposition** | Rejoinder Ledger, Condorcet's Premise |
| Volume production should be gated on one inspected representative first article. | **The Mock-Up Bay** | The Serial Troponin, The Unprimed Falsifier |
| A long campaign's plan is a hypothesis; pivots must not orphan completed evidence. | **The Midseason Pivot Ledger** | Season Bible, Continuity Ledger, Fork-Evident History |
| Wave-1 output is soil (fixtures, stubs, schemas), not deliverables. | **Facilitator-First Decomposition** | Keystone-First Sequencing, The Attested Merge Gate |
| Downstream can honestly begin on partial upstream evidence; engine fleet semantics are all-or-nothing. | **The Inspection and Redline Stakes** | Fleet Receipt Ledger, Admission by First Cycle (successor) |
| A vendor rate limit mid-wave would leave a cold joint of inconsistent vintage. | **The Continuous Pour Schedule** | The Rostered Watch, Circuit Breaker |

**Pass-2 corrections to existing guidance:** `skip_when` skips on command *success* — write permission predicates as refusals (absent/invalid artifact ⇒ command succeeds ⇒ skip), and never let a load-bearing check live only in `skip_when` (V1: evaluation errors proceed). Parallel workers never append to one shared file: per-worker files, one aggregating writer, write-temp-then-rename. `failure_history` is sheet-local retry state, not a cross-sheet broadcast — use typed verdict artifacts. Proof-status vocabulary: primitives-proven / approximation / aspirational ("native-proven" is retired).

## Iteration 7 Problem → Pattern Additions (Discover Pass 1, Cycle 7)

Sixteen new patterns after three adversarial reviews; nine draft entries folded or cut (folds noted where they landed). Problem-first, per this guide's rule.

| If your problem is… | Start with | Compose with |
|---|---|---|
| A receiver may have misunderstood an instruction, and the misread would surface at commit time. | **Readback Before Commit** | Fan-out + Synthesis, The Poisoned-Artifact Advisory |
| An upstream failure contaminated artifacts that downstream work already consumed. | **The Poisoned-Artifact Advisory** | Dead Letter Quarantine, The Validity Window |
| Rejected candidates vanish, and future choosers re-pay the rediscovery price. | **The Sealed Dissent** (within-run) / **The Negative Ledger** (cross-run) | Variant Apparatus, Fork-Evident History |
| N parallel estimates of an additive total disagree within tolerance, and the fan-in is about to average or argue. | **The Misclosure Ledger** | Concurrent Count, Condorcet's Premise |
| A survey task's fan-out width is being sized by feel. | **One Field, Many Cores** | Immune Cascade (priced variant), First Article Characterization |
| Interruptions are all priced the same — always human, or always auto. | **The Graded Ladder** | Transfer of Command at the Seam, The Acknowledged False Alarm |
| Work escalates to a human who must act without archaeology. | **Transfer of Command at the Seam** | The Write-Time Record, The Black-Box Ledger |
| A suppression/ignore list is rotting with no expiry. | **The Acknowledged False Alarm** | Configuration Control Board, The Validity Window |
| Near-passes (lucky validations, near-limit durations) are silently ignored. | **The Near-Miss Ledger** *(aspirational)* | After-Action Review, The Unprimed Falsifier |
| Verification runs every check to completion when most cases clear cheaply. | **The Serial Troponin** | Immune Cascade (priced variant), Circuit Breaker |
| Iteration state must survive a boundary or restart as an external artifact. | **The Watch Rollover** | Transfer of Command, Cathedral Construction |
| A fleet roster says members are ready, but readiness has decayed since authorship. | **The Capability Census** | Concurrent Count, Dormancy Gate |
| Fleet members end unaccounted — partial failure hides at fleet scale. | **The Fleet Receipt Ledger** | The Non-Waiting Hand, Demobilization Checkout |
| A parent must spawn derivative work without waiting, without fire-and-forget. | **The Non-Waiting Hand** | The Fleet Receipt Ledger, Is-Line-Clear |
| A fleet should admit a member only on fresh, full-strength proof. | **Admission by First Cycle** | Capability Census, Sign-Off Chain Against the Hard Date |

Iteration-7 folds (reach the parent pattern, not a new name): failure evidence aging and held-work pinning → **The Validity Window** (two new profiles); tiered verification with committed price tables → **Immune Cascade** (priced variant); conductor-mediated failure transport in loops → **Dead Letter Quarantine**; waiting on a ripening prerequisite against a hard date → **Sign-Off Chain Against the Hard Date** (ripening face); anonymous multi-round estimation with mechanical aggregates → **Delphi Convergence**; least-context worker packets and negative examples → **Prefabrication** (prevention by desk design).

## Iteration 6 Problem → Pattern Additions

Rows for the iteration-6 core: four laws, twelve patterns. Problem-first, per this guide's rule.

| If your problem is… | Start with | Compose with |
|---|---|---|
| Pipelines hold expirable state — tokens, permits, freshness-bound context, generated datasets — and silently reuse it after it expires. | **The Validity Window** | The Gas-Free Certificate, The Declared Window |
| Downstream work starts against upstream structure that is still moving, so finishers build on a version that stops existing. | **The Freeze** | Fork-Evident History, The Unprimed Falsifier |
| Authority-carrying objects flow without a type a gate can join on, so binding decisions and persuasive suggestions enforce identically. | **Typed Force** | The Precedent Bench, The Dropped Axiom |
| Obligations and provenance are reconstructed by archaeology at end-of-life, after the people who created them are gone. | **The Write-Time Record** | Demobilization Checkout, Vintage Overlay |
| Many consumers need different slices of one shared accumulating state, and each receives everything or someone else's slice. | **Monitor Mix** | Relay Zone, The Declared Window |
| Voting authority is assumed from panel size, but correlated panels ratify errors with majority confidence. | **Condorcet's Premise** | The Skeptical Oracle, Rashomon Gate |
| Synthesis sheets read bounded lookback over large runs and then make global claims their window cannot support. | **The Declared Window** | The Black-Box Ledger, Hutchinson's Warning |
| A destructive operation will run on the strength of a check that passed earlier, against a world that has since moved. | **The Gas-Free Certificate** | The Validity Window, The Fencing Token |
| Removing a shared thing would succeed while dependents that quietly stood on it lose their footing. | **Top-Down Demolition Order** | Saga Compensation Chain, Behavioral Pre-Mortem |
| A repeated per-use cost and a one-time commitment cost face an unknown horizon, with no rule for when committing is provably defensible. | **Rent-Then-Commit** | Circuit Breaker, The Economic Injury Line |
| A stable canonical pipeline re-runs under varying external conditions, and each run improvises tuning. | **Vintage Overlay** | Effectivity Blocks, The Write-Time Record |
| Defensive recurring work responds to felt damage instead of a threshold computed from unit economics before the season. | **The Economic Injury Line** | Rent-Then-Commit, Hutchinson's Warning |
| A long campaign re-litigates settled decisions every score, or contradicts them silently. | **The Precedent Bench** | Typed Force, The Errata Ledger |
| A concert is ending with processes, leases, workspaces, and credentials still live — retirement has no owner. | **Demobilization Checkout** | The Write-Time Record, The Gas-Free Certificate |
| Makers cannot perceive their finished artifact, and internal evaluation shares the blind spot. | **The Unprimed Falsifier** | The Freeze, Rehearsal Spotlight |
| A fan-in presents its concealed aggregation choice as neutrality. | **The Dropped Axiom** | Typed Force, Fan-out + Synthesis |

Moved out of core this iteration: Calling the Show, Relieving the Watch, The Strike Clock, and Put-In are in Patterns Awaiting Primitives (with buildable approximations); Command by Negation is an idiom under Mission Command and the Declared Window; The ATO Cycle and Cluster Lead are archived with their surviving components recorded.

---

## Iteration 5.1 Problem → Pattern Additions

These rows cover every newly curated split pattern, plus the renamed foundational law. Archived/incubator entries remain selectable: their individual files state their evidence strength and limits.

| If your problem is… | Start with | Compose with |
|---|---|---|
| Deterministic protocol checks are given to LLM instruments that can hallucinate them, making the coordination layer no more reliable than the performers it coordinates. | **The Etiquette Law** | Pattern-specific gate or evidence carrier |
| In a system with a powerful reviewer and an automated remediation path, the reviewer is the most dangerous instrument: a false-positive finding triggers rollback or deletion of healthy work. | **Immune Checkpoint** | The Skeptical Oracle, Andon Cord |
| Mechanism interactions — concurrency windows, skip/fallback interplay, self-chain livelock — are invisible in YAML source and kill in production. | **Behavioral Pre-Mortem** | Self-Stabilizing Custody, The Etiquette Law |
| A single inventory count cannot distinguish a real total from omissions caused by one traversal or observer. | **Concurrent Count** | The Skeptical Oracle |
| Configuration changes cross a shared boundary without one serialized authority, so individually reasonable edits combine into an incoherent active configuration. | **Configuration Control Board** | Flight Rules |
| Forward scheduling discovers too late that prerequisite work cannot fit before a fixed release instant. | **Firing the Pass** | Graceful Retreat, Standby–GO |
| Validating each item of a large homogeneous fan-out from first principles is unaffordable, and validating none is unacceptable. | **First Article Characterization** | Standby–GO, The Skeptical Oracle, The Attested Merge Gate |
| Every local handoff looks plausible while the rendered score graph contains an unmet need, type mismatch, or dependency deadlock. | **Globally-Typed Choreography** | Proof-Carrying Artifact, Behavioral Pre-Mortem |
| The fan-in point is both a bottleneck and a trust point: merging concurrent writers requires arbitration that can destroy concurrent work. | **Join-Semilattice Merge** | Fan-out + Synthesis, The Attested Merge Gate |
| Sequential creative agents lose artistic continuity or individual authority because handoffs preserve either substrate or voice, but not the living identity of the performance. | **Live Relay** | Mission Command, Stigmergic Workspace, Succession Pipeline |
| A hard deadline collapses independent review obligations into one vague approval, hiding which failure class was knowingly waived. | **Sign-Off Chain Against the Hard Date** | The Attested Merge Gate |
| Parallel writers produce artifacts that must compose, and trusting their self-reports lets incompatible work merge. | **The Attested Merge Gate** | Join-Semilattice Merge, First Article Characterization, Prefabrication |
| Vendor-diverse advisors' findings cannot enter the record without importing their hallucinations. | **The Skeptical Oracle** | Proof-Carrying Artifact, Immune Checkpoint |
| A continuous stream of work outlives any single worker's endurance — context, budget, or lease — and restarts from zero at every boundary. | **Canon of Phases** | Positive Transfer, Replication Licensing |
| Participants consume shared quality improvements without returning evidence or maintenance, so the shared substrate degrades. | **Mycorrhizal Reciprocity** | Season Bible |
| Admitted claims silently rot as their external sources move, and derived work keeps building on stale truth. | **Negative-Treatment Watch** | The Errata Ledger, Flight Rules, Proof-Carrying Artifact |
| Planned succession changes the named operator but leaves tacit state, pending decisions, and incident context behind. | **Transfer of Command** | The Black-Box Ledger, Positive Transfer |
| Parallel authors silently contradict shared world facts because prose canon has no typed, serialized assertion boundary. | **Continuity Ledger** | Join-Semilattice Merge, The Errata Ledger |
| A receiver acknowledges custody without proving that the bytes received are the bytes the sender released. | **Custody Transfer with Seals** | Positive Transfer, Fork-Evident History |
| A retroactively edited history is undetectable, so downstream consumers cannot know they saw the same claims as everyone else. | **Fork-Evident History** | The Errata Ledger, Proof-Carrying Artifact, Self-Stabilizing Custody |
| A sender infers that a shared medium is free and transmits into an unobserved conflicting operation. | **Is-Line-Clear** | Standby–GO |
| Work moving between executors passes through moments with no owner, and a failed handoff silently drops custody. | **Positive Transfer** | Canon of Phases, The Black-Box Ledger |
| Consumers must either trust producer claims across a trust boundary or re-derive the work at full cost. | **Proof-Carrying Artifact** | Fork-Evident History, Flight Rules, The Skeptical Oracle |
| A response claims to address review findings while omitting, duplicating, or answering a different finding under similar prose. | **Rejoinder Ledger** | The Skeptical Oracle |
| A one-phase cue discovers receiver readiness at the moment of irreversible execution. | **Standby–GO** | First Article Characterization, Hutchinson's Warning |
| A correction that silently rewrites the text lies about its own history, and a correction notice nobody consumes leaves derived copies wrong. | **The Errata Ledger** | Fork-Evident History, Negative-Treatment Watch, Proof-Carrying Artifact |
| A retry loop treats an arriving item as fresh and repeats an intervention that already failed, wasting the window or compounding damage. | **The MIST Card** | The Black-Box Ledger, Flight Rules, Replication Licensing |
| Synthesis erases material dissent to produce one smooth deliverable, depriving consumers of the conditions under which the conclusion changes. | **Variant Apparatus** | Sugya Weave (Editorial Synthesis), Talmudic Page |
| A system holds a fixed quality or throughput target while cumulative wear rises invisibly until performance collapses. | **Allostatic Setpoint** | Hutchinson's Warning |
| A manifest or rule is treated as timeless even though it is valid only for a bounded configuration, population, or interval. | **Effectivity Blocks** | Flight Rules, First Article Characterization, Replication Licensing |
| Under failure, deliberation is the enemy: the response is re-derived under duress instead of looked up from pre-negotiated, versioned condition-action bindings. | **Flight Rules** | The Black-Box Ledger, The MIST Card, After-Action Review |
| Negative feedback with lag oscillates: a controller fed by lagged telemetry throttles hard, bursts through, and throttles hard forever. | **Hutchinson's Warning** | The Etiquette Law, Standby–GO |
| A fixed merge admission rate either starves available capacity or overloads the consumer when measured congestion changes with delay. | **Metered Merge** | Hutchinson's Warning |
| Crash, corruption, and restart are treated as exceptional events requiring an exceptional recovery protocol, when they are just arbitrary states the ordinary rules should leave. | **Self-Stabilizing Custody** | The Fencing Token, The Black-Box Ledger, Behavioral Pre-Mortem |
| After the executor dies, what happened is knowable only from survivor testimony — reconstructed memory — unless a channel that does not share the executor's fate recorded it continuously. | **The Black-Box Ledger** | Flight Rules, The MIST Card, Positive Transfer |
| A paused or retried executor cannot observe its own expiry and silently overwrites newer work with older, slower work. | **The Fencing Token** | Self-Stabilizing Custody, Replication Licensing |
| Authority expressed as a list of rights the subject names lets authority leak through any confused intermediary. | **Designation Is Authorization** | Proof-Carrying Artifact, The Etiquette Law |
| A population's risk tier changes item by item, leaving structurally similar items under inconsistent controls after systemic evidence appears. | **Re-Tiering Decision** | Negative-Treatment Watch, Screening Cascade |
| Low-grade workspace fuel accumulates until cleanup becomes a disruptive emergency instead of a bounded maintenance action. | **Prescribed-Fire Pulse** | Stigmergic Workspace |
| A cycle counter cannot prevent a side-effectful cycle from happening twice, and naive retries duplicate deployments. | **Replication Licensing** | The Fencing Token, Canon of Phases |

**Iteration 5.1 start-here chain:** The Etiquette Law → Fan-out + Synthesis → Proof-Carrying Artifact → The Fencing Token → Standby–GO.

---

## Problem Types and Pattern Compositions

### Parallelize Work Without Drift

**Problem:** Multiple agents working in parallel produce inconsistent outputs because each makes independent choices.

**Compositions:**
- **Fan-out + Synthesis + Barn Raising** — Parallelize work, establish shared conventions first, then integrate outputs
- **Prefabrication + Mission Command** — Define interface contracts upfront, then execute with outcome validation
- **Fan-out + Synthesis + Triage Gate** — Parallelize, then filter mixed-quality outputs before synthesis

**Signals:** Parallel agents will work on similar artifacts; consistency in naming/structure matters for integration; synthesis must address cross-cutting themes

---

### Optimize Costs

**Problem:** Work items vary in complexity but you're using expensive instruments for everything.

**Compositions:**
- **Echelon Repair + Screening Cascade + Commissioning Cascade** — Classify upfront, route to appropriate tiers, validate each tier's output
- **Fermentation Relay + Succession Pipeline** — Use cheap instruments for initial extraction, escalate through cost-graduated refinement
- **The Etiquette Law + Echelon Repair** — Route deterministic work to CLI tools, use AI only for complex items

**Signals:** Work items vary wildly in complexity; costs are high but most work is simple; expensive instrument wasted on trivial tasks

---

### Validate Before Scaling

**Problem:** Expensive downstream work proceeds without validating that the foundation or pipeline works correctly.

**Compositions:**
- **Shipyard Sequence + Commissioning Cascade** — Validate foundation with scope-appropriate instruments before fan-out
- **Canary Probe + Progressive Rollout** — Test on small batch first, then scale incrementally with monitoring
- **Triage Gate + Immune Cascade** — Filter broad findings before expensive deep analysis

**Signals:** Downstream fan-out is expensive; foundation must be solid before scaling work; need real validation tools, not LLM judgment

---

### Analyze from Multiple Angles

**Problem:** Single-perspective analysis produces unreliable conclusions when the optimal analytical frame is unknown.

**Compositions:**
- **Rashomon Gate + Sugya Weave (Editorial Synthesis) + Source Triangulation** — Apply multiple frames, synthesize with editorial judgment, verify across independent sources
- **Fan-out + Synthesis + Talmudic Page** — Parallelize analysis, produce multi-layer annotations that reference each other
- **Red Team / Blue Team + After-Action Review** — Adversarial testing with systematic learning capture

**Signals:** Multiple valid perspectives exist; risk is getting the right answer from the wrong frame; need argued position, not neutral aggregation

---

### Handle Partial Failures Gracefully

**Problem:** Some work items consistently fail, but retries waste resources without identifying root causes.

**Compositions:**
- **Dead Letter Quarantine + Triage Gate + Circuit Breaker** — Quarantine chronic failures, classify outputs by quality, halt escalation when failures spike
- **Andon Cord + Commissioning Cascade** — Diagnose root cause from failure output, validate with tier-appropriate instruments
- **Quorum Consensus + Triage Gate** — Proceed with majority agreement, filter mixed-quality outputs

**Signals:** Some items consistently fail across retries; batch processing has persistent partial failures; retry loops waste resources

---

### Learn from Failures

**Problem:** Same mistakes happen repeatedly because execution insights aren't captured or propagated.

**Compositions:**
- **CDCL Search + After-Action Review + Back-Slopping (Learning Inheritance)** — Extract constraints from failures, capture methodology improvements, inherit learning across iterations
- **Systemic Acquired Resistance + Circuit Breaker** — Propagate failure patterns across concert, halt when patterns recur
- **Andon Cord + CDCL Search** — Diagnose root cause, convert to constraint to prevent recurrence

**Signals:** Same failures occur across retry attempts; retries don't help because nothing is learned; later iterations repeat mistakes from earlier ones

---

### Iterate Toward a Goal

**Problem:** Large artifacts require iterative construction, but iterations are expensive and convergence is unclear.

**Compositions:**
- **Cathedral Construction + Memoization Cache + Back-Slopping (Learning Inheritance)** — Build incrementally toward target, cache unchanged regions, inherit learning
- **Fixed-Point Iteration + Soil Maturity Index** — Refine repeatedly, measure domain-specific convergence readiness
- **CEGAR Loop (Progressive Refinement) + Memoization Cache** — Progressively refine abstraction, skip re-analysis of unchanged regions

**Signals:** Artifact too large to complete in one pass; iterations are expensive and need measurable termination; each iteration adds structural elements

---

### Coordinate Without Bottlenecks

**Problem:** Centralized coordination creates bottlenecks, but decentralized work produces inconsistency.

**Compositions:**
- **Mission Command + Commander's Intent Envelope + After-Action Review** — Define intent envelope, execute autonomously, capture decision logs for learning
- **Stigmergic Workspace + Barn Raising** — Coordinate through workspace state, establish shared conventions
- **Lines of Effort + Season Bible** — Parallel workstreams with autonomy, shared memory of decisions and constraints

**Signals:** Tasks require agent judgment; validation should check outcomes not methods; multiple agents must coordinate around shared intent

---

### Manage Large Contexts

**Problem:** Pipeline outputs exceed context window limits, degrading downstream agent performance.

**Compositions:**
- **Relay Zone + Forward Observer + Screening Cascade** — Compress handoffs, use cheap summarization upfront, pre-filter before expensive processing
- **Immune Cascade + Relay Zone** — Narrow scope with cheap scanning, compress findings before triage
- **Forward Observer + The Etiquette Law** — Summarize raw input cheaply, route deterministic work to CLI tools

**Signals:** Input exceeds context window; later stages receive more context than they can effectively use; token costs dominate total cost

---

### Test Unknown Approaches

**Problem:** Uncertain which approach will work, but starting over after failure is expensive.

**Compositions:**
- **Canary Probe + Progressive Rollout + Dead Letter Quarantine** — Test small batch, scale incrementally, quarantine persistent failures
- **Speculative Hedge + Vickrey Auction** — Run candidate approaches in parallel, select winner based on evidence
- **Reconnaissance Pull + Mission Command** — Explore landscape first, then execute with intent envelope

**Signals:** Uncertain which approach works; starting over costs more than running both; need validated evidence before full commitment

---

### Build Incrementally with Quality Gates

**Problem:** Work requires sequential transformations, but unstructured execution produces outputs incompatible with downstream stages.

**Compositions:**
- **Succession Pipeline + Shipyard Sequence + Barn Raising** — Sequential substrate transformations, validate each stage, establish shared conventions
- **Composting Cascade + The Etiquette Law + Succession Pipeline** — Measure readiness signals, chain CLI tools with AI stages, progress through categorical transformations
- **Closed-Loop Call + Relay Zone** — Verify semantic fidelity at handoffs, compress cumulative outputs

**Signals:** Each stage needs fundamentally different methods; one stage's output becomes next stage's input substrate; stages have categorical differences

---

### Detect Quality Issues Early

**Problem:** Finding problems late costs exponentially more than catching them early in the pipeline.

**Compositions:**
- **Shipyard Sequence + Succession Pipeline + Immune Cascade** — Validate foundation before fan-out, progress through quality gates, narrow findings cheaply
- **Commissioning Cascade + Echelon Repair + The Etiquette Law** — Different validation scopes with appropriate instruments, tier-matched validation, validate CLI tool outputs
- **Triage Gate + Fan-out + Synthesis** — Filter mixed-quality outputs before synthesis, prevent garbage from reaching expensive stages

**Signals:** Unit tests pass but integration fails; downstream fan-out is expensive; need to narrow findings before expensive deep analysis

---

### Recover from Failures Intelligently

**Problem:** Failures should inform strategy, not just trigger blind retries.

**Compositions:**
- **Andon Cord + Circuit Breaker + Dead Letter Quarantine** — Diagnose root cause, halt when instrument fails, quarantine unfixable items
- **CDCL Search + Systemic Acquired Resistance** — Extract failure patterns as constraints, propagate across concert
- **Graceful Retreat + Cathedral Construction** — Accept partial completion tiers, preserve progress across iterations

**Signals:** Validation failures repeat same error; instrument becomes unavailable mid-execution; need to proceed with partial results

---

### Converge Diverse Opinions

**Problem:** Multiple independent agents produce varied assessments that need to converge without anchoring on early opinions.

**Compositions:**
- **Delphi Convergence + Source Triangulation + Rashomon Gate** — Iterate toward consensus without early anchoring, verify across independent sources, apply multiple analytical frames
- **Quorum Consensus + Fan-out + Synthesis** — Proceed with majority agreement, integrate diverse perspectives
- **Sugya Weave (Editorial Synthesis) + Talmudic Page** — Editorial synthesis with argued positions, multi-layer annotation with cross-references

**Signals:** Expert opinions vary widely and need to converge; single-round synthesis isn't achieving consensus; agents anchor on initial assessments

---

### Adapt Plans Mid-Execution

**Problem:** Plans become stale when discovered conditions diverge from expectations, but full replanning is wasteful.

**Compositions:**
- **Fragmentary Order (FRAGO) + Read-and-React + Mission Command** — Issue targeted corrections, inspect workspace state and adapt, preserve intent envelope while adjusting methods
- **Quorum Trigger + Andon Cord** — Self-interrupt based on evidence density, diagnose before continuing
- **Dormancy Gate + Read-and-React** — Pause until prerequisites available, re-evaluate dynamically

**Signals:** Earlier stages invalidate downstream assumptions; plan is partially wrong but not wrong enough to discard; conditions discovered mid-execution weren't anticipated

---

## How to Use This Guide

1. **Start with your problem, not a pattern name.** Find the problem type that matches your situation.
2. **Read the signals.** Do they describe what you're experiencing?
3. **Weigh every composition, not the first.** They are listed in the order they were discovered, which is also the order composers reach for them; the first is the most familiar, not the best fit. Read the signals of each before choosing, and prefer the one whose signals match most closely. `tools/unproven.py` lists which patterns no proof score has ever exercised, and its `--usage` mode counts how often each pattern is cited in produced score YAML; a familiar pattern is not evidence that it fits (GH #354, #355).
4. **Read the individual pattern files.** This guide tells you WHEN and WHICH; the pattern files tell you HOW.
5. **Compose incrementally.** You don't need to use all patterns in a composition at once. Start with one, add the next when needed.

---

## Composition Principles

**What makes patterns compose well together?**

- **Shared workspace as integration point** — Patterns coordinate through files, not message passing
- **Complementary forces** — One pattern creates structure another pattern exploits (e.g., Barn Raising establishes conventions that Mission Command agents follow)
- **Sequential or parallel relationship** — One pattern's output feeds another's input (sequential) OR patterns work on independent aspects simultaneously (parallel)
- **Escalation or filtering** — One pattern narrows scope/complexity, another handles what passes through (e.g., Screening Cascade → Echelon Repair)

**What breaks composition?**

- **Conflicting assumptions** — One pattern assumes deterministic tools, another assumes AI judgment on the same stage
- **Circular dependencies** — Pattern A needs Pattern B's output, Pattern B needs Pattern A's output
- **Redundant work** — Both patterns do the same classification/filtering in different ways
- **Wrong scale** — Trying to compose a within-stage prompt technique with a concert-level pattern

---

## Quick Reference: Pattern by Scale

| Scale | What It Controls | Example Patterns |
|-------|------------------|------------------|
| **Within-Stage** | Single sheet's prompt content or behavior | Commander's Intent Envelope, Decision Propagation, Quorum Trigger |
| **Foundational** | Primitive moves used across all scopes | The Etiquette Law, Fan-out + Synthesis |
| **Score-Level** | Multiple sheets within a single score | Shipyard Sequence, Canary Probe, Barn Raising, Mission Command |
| **Concert-Level** | Multiple scores in a campaign | Lines of Effort, Progressive Rollout, Season Bible, Saga Compensation Chain |
| **Communication** | Coordination through workspace state | Stigmergic Workspace |
| **Adaptation** | Adjust behavior mid-execution based on runtime conditions | Andon Cord, Circuit Breaker, Read-and-React, Fragmentary Order (FRAGO) |
| **Instrument-Strategy** | Match instrument capabilities to task requirements | Echelon Repair, Commissioning Cascade, Screening Cascade |
| **Iteration** | Repeated refinement and learning across execution cycles | CDCL Search, Cathedral Construction, After-Action Review, Memoization Cache |

---

## For `marianne compose`

When analyzing a user's goal description, match against these semantic categories:

- **"analyze from multiple perspectives"** → Multi-Frame Analysis patterns
- **"run in parallel"** OR **"parallelize"** → Parallel Work Without Drift patterns
- **"reduce costs"** OR **"optimize budget"** → Optimize Costs patterns
- **"validate before"** OR **"test first"** → Validate Before Scaling patterns
- **"learn from failures"** OR **"stop repeating mistakes"** → Learn from Failures patterns
- **"iterate"** OR **"refine"** → Iterate Toward a Goal patterns
- **"coordinate"** OR **"no bottlenecks"** → Coordinate Without Bottlenecks patterns
- **"too much context"** OR **"context overflow"** → Manage Large Contexts patterns
- **"not sure which approach"** OR **"try different ways"** → Test Unknown Approaches patterns
- **"sequential stages"** OR **"pipeline"** → Build Incrementally with Quality Gates patterns
- **"catch issues early"** → Detect Quality Issues Early patterns
- **"recover from"** OR **"handle failures"** → Recover from Failures Intelligently patterns
- **"converge"** OR **"reach consensus"** → Converge Diverse Opinions patterns
- **"adapt"** OR **"conditions change"** → Adapt Plans Mid-Execution patterns

The compositions under each problem type are not ranked; the first is only the earliest discovered. Match on signals, read the individual pattern files before implementing, and reach for patterns the proof ledger (`tools/unproven.py`) shows unexercised when their signals fit.
