# Patterns Awaiting Primitives

Each row was rechecked against the source-verified Marianne primitives on 2026-09-03; iteration-6 rows added 2026-09-04 after three adversarial reviews (each blocked on a named absent primitive, per the corpus's no-fabrication rule). A nearby mechanism is not treated as the missing primitive: `cost_limits` is per-job, `fan_out` is parse-time static, and ordinary parallelism does not provide consumer-driven backpressure or multi-host authority.

| Pattern | Blocked By | Buildable approximation / current boundary |
|---|---|---|
| Bulkhead Isolation | Per-sheet resource budgets | `cost_limits` constrains and pauses the whole job; it cannot cap one sheet independently. |
| Kanban Pull | Conductor-level pull/WIP admission limits | `parallel.max_concurrent` is a static job concurrency ceiling, not consumer-signaled pull. |
| Supervision Hierarchy | A supervisor configuration surface with hierarchical restart policies | Workspace snapshots plus conductor-mediated restart remain a manual approximation; durable `on_failure` is terminal handling, not a restart tree. |
| OODA Pulse | A runtime feedback hook that can re-orient and alter the next execution cycle | A score-authored observe/decide self-chain can approximate the loop, but the engine exposes no self-correcting orientation phase. |
| Backpressure Valve | Concurrent producer/consumer score execution with consumer capacity feedback | Metered Merge offers leased admission, but ordinary parallel execution has no capacity signal flowing from consumer to producer. |
| Comping Substrate | A long-lived adaptive coordinator executing concurrently with work scores over shared state | Canon of Phases supplies scheduled rotation, not a continuously adapting shared-filesystem rhythm layer. |
| Physarum Path Reinforcement | Runtime fan-out width and instrument reassignment | `fan_out` expands at parse time; allocation cannot change from workspace evidence during the run. |
| Zeitgeber Entrainment | Offset-from-artifact or offset-from-heartbeat scheduling | Leased `schedule` plus a required heartbeat cadenza and command-form staleness gate can poll and skip, but cannot phase-lock. |
| Accountability Board (score-facing PAR sweep) | Score-facing export of conductor claims with physical process handles | A CLI process probe can reconcile only a score-owned claims ledger and processes it can identify. |
| MIST Card (conductor retries) | Per-attempt retry hooks that append to a user-visible ledger | The curated MIST Card is explicitly an approximation over score-authored retry wrappers. |
| True capability confinement | OS-level sandboxing of sheet filesystem and tool access | Designation Is Authorization confines delivered context, not process reach. |
| Devolution Packet | Multi-host orchestration and delegated host authority | No faithful single-host approximation. Re-proposable when the multi-host primitive exists. |
| Black Start | Multi-host capability discovery and dependency-ordered global restart | No faithful single-host approximation. Re-proposable when the multi-host primitive exists. |
| Calling the Show (iteration 6) | A recurring per-cue state machine with overlapped standby and hold-and-proceed-around | Standby–GO invoked once per cue inside a bounded self-chain; cue ledger as a workspace artifact advanced by a CLI movement; holds recorded as visible skips — the pipelined overlap and the bypass lane are the blocked part. All three adversarial reviews concurred the continuous form is inexpressible in a linear movement DAG. |
| Relieving the Watch (iteration 6) | Mid-sheet checkpointing (write-ahead hook or transactional sheet checkpoints) | Deck log as append-only JSONL written *as the sheet works*; movement-boundary reconciliation gates joining log claims to disk facts; `mzt recover` as the rehearsed spine. The Newcomer review's dissent is on record: "the crash-recovery pattern every long-running user needs" — re-enters core when the checkpoint primitive lands. |
| The Strike Clock (iteration 6) | A timeout→tier transition (timeouts fail sheets; they select nothing — `max_wall_seconds` bounds a scheduled run and selects nothing) | Inverted-DAG teardown order derived from the assembly DAG; per-movement budgets via `instrument_config.timeout_seconds`; pack-for-next-run; curfew report as the successor's first input. The tier-arithmetic is the blocked half. |
| Put-In (iteration 6) | Runtime seat remap (instrument assignment and `fan_out` expand at parse time) | Track-sheet compile from incumbent artifacts; shadow run as an isolated job writing alongside, never over; structured diff gate with `--require-bijection`; cutover as a versioned score edit with the incumbent written into the next version's fallback chain. The Newcomer review's dissent is on record. |

## Moved Out of Awaiting

- **Saga Compensation Chain** is now a working concert-level pattern: durable top-level `on_failure` hooks exist, including restart reconciliation and same-ID protection.
- **Stretto Entry** is superseded by **Canon of Phases**, which uses leased recurrence plus explicit multi-deployment rotation; the old overlapping-sheet name is retired rather than kept as a duplicate.
- **The Aboyeur** is superseded by **Firing the Pass**, which computes deadline-first dated inputs without claiming nonexistent offset-from-artifact scheduling.

## Re-Proposable Research Names

**Contact Point co-evolution** was removed from the iteration-5.1 monolith without a concrete blocking primitive or curated pattern. It is not an awaiting pattern today; a future iteration may re-propose it with a precise substrate contract.
