# The Rosetta Pattern Corpus — Discover Pass 1, Cycle 7 (Final, post-adversarial-review)

**Iteration:** discover pass 1 of the cycle-7 Rosetta loop, final — the 25-pattern draft (`04-draft-corpus.md`) after three adversarial reviews (Practitioner, Skeptic, Newcomer; verdicts **NEEDS REVISION** ×3), integrated.
**Inputs:** 01-the-question.md, six sealed expedition reports, 03-the-collision.md, 04-draft-corpus.md, 05-review-{1,2,3}.md, the permanent corpus (111 pattern files, 5 laws, v6 core of 17), and the 17 historical proof scores plus `prove-pass-1/04-proof-score.yaml` (Barn Raising).
**This pass's yield:** **16 core patterns** (15 `working`, 1 `aspirational`), **1 first-promote candidate** (The Bounded Grep), **9 demotions** — cut, folded into named permanent patterns, or split — down from the draft's ~30 patterns billed as 25. Every score structure below is written in the dialect the engine actually accepts or explicitly marked `status: aspirational` with the blocking dependency named. Every pattern carries YAML (Review 3's category-failure finding: "not one line of YAML in the entire draft"), a primitive-status flag, and a discriminating negative control with its sentinel specified.
**Where this lives:** workspace copy (this file); permanent monolith `archive/rosetta-corpus.md`; decomposed view `patterns/*.md` + `INDEX.md` + `selection-guide.md` (the prove path selects from the decomposed files — they are authoritative for selection).

---

## Merge Policy (unchanged in spirit, corrected in practice)

1. **No duplication of the permanent corpus — and no unnamed neighbors.** Review 3 caught the draft violating its own rule: the Graded Net never mentioned **Immune Cascade**, whose proof score's header states the Net's claimed invariant word for word. That violation is repaired the honest way: the Graded Net's real differentiators (committed price tables, the ≥10× tier-collapse rule, promotion-by-declared-risk, dual-family tier 3) are **folded into Immune Cascade** as the "priced variant" section, exactly as Pre-Load was to be folded into the Net. The same treatment applies to four more drafts whose claimed ground turned out to be owned: Aged Lead and Held-State Clock → The Validity Window (profiles, per Review 2's structural-identity test); Automatic Curriculum → Dead Letter Quarantine (transport refinement); Anthesis Window → Sign-Off Chain Against the Hard Date (ripening face, per Review 3's consistency demand). One collision the reviews did not flag is also repaired here: **Anonymous Rounds vs. Delphi Convergence** — the corpus already owns Delphi; the draft's additions (mechanically computed aggregates as the only feedback, published non-convergence, the anonymity content_regex gate) fold into it.
2. **Convergence is promotion evidence, not identity evidence.** Review 2's rule, adopted: a pattern is merged only when its structural fingerprint — (DAG, state machine, communication channel, decision authority, failure semantics) — matches. Collision counts are retained as confidence signals, never as identity claims.
3. **Composite headings are banned.** The draft's five "×"/"with"-as-smuggling headings (Review 3) are severed: Sealed Dissent and Negative Ledger are two patterns with two lookup semantics; Watch Rollover and Rolling Continuity are split (Continuity's carry-ratio mechanics live as a section of Watch Rollover's ledger, its independent promotion deferred); Admission by First Cycle keeps the receipt gate, the Readiness Cycle moves to candidates; Pre-Load and Vendor Board were already folds and stay folded (into Immune Cascade and Capability Census respectively).
4. **Zero-mention primitives take priority — flagged per pattern.** The draft put eight of eleven zero-mention primitives "under pattern discipline" without saying which had never executed once. The table below is the correction: every pattern's load-bearing primitives are marked **native-proven** (exercised in a proof score on disk), **native-unproven** (engine-supported, zero proof-score exercise), or **blocked** (no primitive; the pattern says so and routes around it).

### Pattern × Primitive × Proof-Status Table

| Pattern | Load-bearing primitives | Status | Proof score? |
|---|---|---|---|
| Readback Before Commit | `response_format: json_schema`, fan_out, CLI gate | native-**unproven** (0 proof-score hits for `response_format`) | none yet — top of proof order |
| The Poisoned-Artifact Advisory | workspace artifacts, CLI gate, `capture_files` | working (no exotic primitives) | none yet |
| The Sealed Dissent | typed candidate ids, CLI grep gate | working | none yet |
| The Negative Ledger | canonical signature codes, `on_fail` post-step | working | none yet |
| The Misclosure Ledger | fan_out, `per_sheet_instruments`, CLI closer | working | none yet |
| One Field, Many Cores | committed grid manifest, fan_out, CLI composite | working (static grid; dynamic width blocked) | none yet |
| The Graded Ladder | typed fields, predeclared branch sheets, `skip_when` routing, `escalate` trigger | native-unproven (`triggers` 0 hits; routing restated as real syntax) | none yet |
| Transfer of Command at the Seam | `escalate`/`pause` trigger, briefing sheet before pause, CLI disposition | native-unproven | none yet |
| The Acknowledged False Alarm | validation scripts reading a workspace list file; `validate_suppress` as the future native face | working (honest mechanism; engine-native form blocked on dynamic suppress lists) | none yet |
| The Near-Miss Ledger | conductor state export (`.marianne-observer.jsonl`) | **aspirational** — observability dependency unverified | none; blocked until status API cited |
| The Serial Troponin | `sheet.loops` + `until`, typed `state.yaml` carrier | native-unproven (`loops`/`until` 0 hits in proof scores; engine-supported per cycle score) | none yet |
| The Watch Rollover | append-only ledger, `file_exists` dependency, `checkpoint_persistence` | working (rollover); checkpoint carrier native-unproven | none yet |
| The Capability Census | CLI probes, roster/census artifacts, fail-closed entry validation | working | none yet |
| The Fleet Receipt Ledger | non-waiting auditor child, jq bijection | working (requires out-of-band execution path — see structure) | none yet |
| The Non-Waiting Hand | `triggers.on_success.concert` + `inherit_workspace`, spawn ledger | native-unproven (`concert` appears only in self-chains, never as non-waiting handoff) | none yet |
| Admission by First Cycle | `fleet` groups + `depends_on`, receipt ledger, jq admission gate | native-unproven (`fleet` 0 hits) | none yet |

**Engine-behavior claims still owing a source citation** (Review 3's finding, kept visible rather than buried): (a) `skip_when` fails open on timeout — load-bearing for gate-direction discipline in Capability Census and Admission by First Cycle; (b) conductor export of retry counts/durations — load-bearing for Graded Ladder's challenge counter and the Near-Miss Ledger; (c) `fleet.depends_on` waiting on *first cycle* rather than full completion. Each is used as stated by the draft but must be verified against engine source before the prove path builds on it; they are the first three rows of Open Questions.

### What This Pass Confirms in the permanent corpus

- **Concurrent Count** — dual-enumeration discipline arrived five times independently (collision §1.2); now also the spine of Fleet Receipt Ledger and Capability Census.
- **The Validity Window** — evidence-TTL arrived five times from five materials; this pass *adds* two profiles (failure-evidence aging; held-state pinning) rather than competing entries.
- **The Etiquette Law** — all six expeditions re-derived the receipt test and built reachable negative controls unprompted.
- **Immune Cascade** — independently re-derived as the Graded Net from SOC triage and rigging economics; strengthened (see fold).
- **Rent-Then-Commit, Sign-Off Chain Against the Hard Date, Dead Letter Quarantine, Dormancy Gate, Rejoinder Ledger, Delphi Convergence** — cited as owned ground by at least two expeditions and composed with by name; the Anthesis Window fold adds Sign-Off Chain's ripening face, the Curriculum fold adds Dead Letter Quarantine's conductor-mediated transport.

### The seven generators (the pass's own finding, carried forward)

The 40 expedition proposals converged on seven structural moves, each forced by an invariant no domain can opt out of: (1) unobservability of understanding → the typed echo; (2) the argument-proof gap in set claims → dual enumerations; (3) asymmetry of error prices → tiered spend; (4) non-stationarity of the world → evidence TTL; (5) mortality of contexts → continuity artifacts; (6) shadow price of rejection → sealed dissent and negative ledgers; (7) gradient of irreversibility → verification depth scaled to undo cost. The grammar is universal; the domain supplies the constants. (Map to the corpus's eleven generators: 1→Contract at Interfaces, 2→Verify through Diverse Observers, 3→Graduate & Filter/Match Instrument to Grain, 4→Gate on Environmental Readiness, 5→Accumulate Knowledge, 6→Exploit Failure as Signal, 7→Incremental Exposure.)

---

# GROUP I — COMMUNICATION

## Readback Before Commit

```yaml
---
name: "Readback Before Commit"
scale: communication
status: working
forces: ["Information Asymmetry", "Exponential Defect Cost"]
generators: ["Contract at Interfaces"]
problem: "A sender cannot observe whether a receiver understood an instruction, so misreads surface at commit time when they cost the whole downstream subtree."
signals:
  - "every fan-in that consumes AI output"
  - "cross-stage contracts where the producer reasons and the consumer executes"
  - "fan-outs with differentiated instructions where each instance must understand ITS lens"
  - "handoffs between instrument types (reasoner → CLI → reasoner)"
stages:
  - name: instructor
    sheets: 1
    instrument_guidance: "score-author's choice — emits the task spec as a structured file with declared fields"
    fallback_friendly: true
    purpose: "Write spec.json: operation, target, constraints as typed fields."
  - name: echo
    sheets: 1
    instrument_guidance: "the receiver instrument — emits ONLY the echo artifact, no work yet"
    fallback_friendly: true
    purpose: "Restate spec fields in normalized form under response_format: json_schema."
  - name: echo-gate
    sheets: 1
    instrument_guidance: "instrument: cli — pure field comparison; instrument_fallbacks: []"
    fallback_friendly: false
    purpose: "Diff echo against spec field-by-field; exit code IS the hearback."
  - name: execute
    sheets: 1
    instrument_guidance: "the receiver instrument — main work, unlocked only by the gate"
    fallback_friendly: true
    purpose: "Do the actual task, having demonstrably understood it."
dependencies:
  echo: ["instructor"]
  echo-gate: ["echo"]
  execute: ["echo-gate"]
composes_with:
  - pattern: "Fan-out + Synthesis"
    how: "the echo schema is the fan-in contract; N receivers each close their own loop before subtrees unlock"
  - pattern: "The Poisoned-Artifact Advisory"
    how: "the echo is prevention; the advisory is containment after the fact"
  - pattern: "Closed-Loop Call"
    how: "Closed-Loop Call checks semantic drift across stages by re-reading outputs; this checks understanding of inputs before work begins"
---
```

**Source:** Expeditions 1+3+6 (ATC readback/hearback per ICAO/Cardardi 1998; Talmud/peer-review via the brief) — triple collision, the hardest of the pass.

### Core Dynamic
A one-way transmission is not an instruction; it is a hope. Only a **typed echo from the receiver, checked by the sender, converts "I said it" into "we agree."** All three derivations agree on the load-bearing details: the echo is typed, not prose ("roger closes nothing"); the verification is deterministic, never an AI nod; the echo is selective — load-bearing fields only, as ATC reads back altitude, not weather; the economics are Exponential Defect Cost — a mismatch at echo-time costs one round trip, at commit-time the whole subtree.

**The draft's contradictions, repaired per the reviews.** Review 1: "recommending non-verbatim restatement while demanding deterministic jq field-matching guarantees broken gates." Correct — the echo schema is therefore restricted to **normalized, machine-checkable fields**: action enums, explicit target resource identifiers, integer/string bounds echoed exactly. Paraphrase lives only in an optional `understanding` prose field that no gate diffs. Review 2: "a receiver cannot emit an echo, pause while a gate checks it, and then continue its main stage inside the same atomic sheet." Correct — the structure is **four nodes** (instructor → echo-only receiver → CLI comparison → executor), not the draft's three. Schema validity proves representation, not understanding; the negative control tests field mismatch (the discriminating, mechanically detectable failure), and the pattern composes with content-bearing gates, never replaces them.

### Marianne Score Structure
```yaml
sheets:
  - name: instructor
    prompt: "Read the task. Write spec.json with fields: operation (enum), target (exact path/id), constraints (string)."
    validations:
      - type: file_exists
        path: "spec.json"
  - name: echo
    capture_files: ["spec.json"]
    prompt: "FIRST ACT ONLY: restate spec.json as echo.json with the SAME operation enum, the SAME target string, and constraints copied field-wise. Emit nothing else."
    response_format: { type: json_schema, schema: { type: object, required: [operation, target, constraints] } }
    validations:
      - type: file_exists
        path: "echo.json"
  - name: echo-gate
    instrument: cli
    instrument_fallbacks: []
    command: "jq -e --argfile a spec.json --argfile b echo.json '$a.operation==$b.operation and $a.target==$b.target' "
    validations:
      - type: command_succeeds
    on_fail: { action: retry, max_retries: 2 }   # bounded correction loop — the receiver re-echoes
  - name: execute
    capture_files: ["spec.json", "echo.json"]
    prompt: "Execute the task exactly as specified in spec.json."
```
**Negative control:** seed the echo sheet's context with a subtle misreading (spec says `staging_users_v2`, a planted note says `staging_users`). The gate must exit non-zero. **Sentinel (specified, per Review 3):** a variant score with the echo-gate removed; a final CLI validator greps the executor's output for the wrong-table string and fails — proving the misread reaches the main stage when the gate is absent. Both directions must fail for the proof to count.

### When NOT to Use
Human-readable deliverables nobody machine-reads; instructions trivial enough that the readback outprices the misread (don't readback `mkdir`); sheets whose output no gate consumes.

---

## The Poisoned-Artifact Advisory

```yaml
---
name: "The Poisoned-Artifact Advisory"
scale: communication
status: working
forces: ["Partial Failure", "Information Asymmetry"]
generators: ["Exploit Failure as Signal"]
problem: "Upstream failure contaminates artifacts that already propagated, and downstream agents treat the workspace as ground truth because no channel tells them what is poisoned."
signals:
  - "a DAG with shared artifacts and a validation gate that runs after consumers may have started"
  - "a subtle early-sheet failure surfaces three stages later"
  - "quality gates that cannot economically run before every consumer"
stages:
  - name: produce
    sheets: 1
    instrument_guidance: "score-author's choice — writes artifact A"
    fallback_friendly: true
    purpose: "Produce the shared artifact."
  - name: consumers
    sheets: "fan_out(2)"
    instrument_guidance: "score-author's choice — each reads A and derives a downstream artifact"
    fallback_friendly: true
    purpose: "Consume A (these may complete before the gate runs — that is the point)."
  - name: late-gate
    sheets: 1
    instrument_guidance: "instrument: cli — validation of A; its FAIL path is the load-bearing half"
    fallback_friendly: false
    purpose: "On fail, write advisories/poisoned.yaml naming artifact, typed failure class, timestamp."
  - name: containment
    sheets: 1
    instrument_guidance: "strong reasoner — identifies which consumer outputs derived from the poisoned field"
    fallback_friendly: false
    purpose: "Write rework manifest: which outputs are tainted, which clean."
  - name: rework
    sheets: 1
    instrument_guidance: "score-author's choice — re-derives ONLY tainted outputs"
    fallback_friendly: true
    purpose: "Repair the blast radius the advisory made visible."
dependencies:
  consumers: ["produce"]
  late-gate: ["produce"]
  containment: ["consumers", "late-gate"]
  rework: ["containment"]
composes_with:
  - pattern: "Dead Letter Quarantine"
    how: "quarantine is the artifact-side move; the advisory is the prompt-side move — compose both at a late gate"
  - pattern: "The Validity Window"
    how: "advisories age — a fresh advisory is quarantine-now, a stale one is history (failure-evidence profile)"
  - pattern: "The Sealed Dissent"
    how: "a poisoned-artifact event is a first-class entry in the negative ledger"
---
```

**Source:** Expedition 6 (Swiss cheese model / latent-failure investigation, Reason; Wiegmann 2022). Named by the v6 review as the fix for "gates running after downstream work has begun."

### Core Dynamic
The Swiss cheese insight: the holes are in the *layers*, so the advisory must reach agents **after** they may have consumed the poison. The draft's wiring, corrected per both reviews: Review 1 — "`failure_history` does not retroactively un-read an artifact from completed consumers." Review 2 — "'consumers' retries' are assumed rather than wired; the pattern needs explicit invalidation lineage, a list of affected consumers, and a compensating rerun DAG." The structure above is that compensating rerun DAG, as an explicit containment + rework stage pair that runs *after* the late gate and the consumers converge. The advisory itself is a **cadenza inverted** — anti-context: "the thing that looks like context and will poison your reasoning" — and must be *typed* (hard-failed / superseded / stale) because the downstream response differs: re-derive, discard, or re-verify.

### Marianne Score Structure
```yaml
sheets:
  - name: produce
    prompt: "Write data/extract.json per the spec."
  - name: consumers
    instances: 2
    capture_files: ["data/extract.json"]
    prompt: "Read data/extract.json. Write report-{{ instance_id }}.md deriving your figures from it."
  - name: late-gate
    instrument: cli
    command: "python3 scripts/units_check.py data/extract.json || (mkdir -p advisories && printf 'artifact: data/extract.json\\nclass: hard-failed\\nts: %s\\n' \"$(date -Is)\" > advisories/poisoned.yaml && exit 1)"
    validations:
      - type: command_succeeds
  - name: containment
    capture_files: ["advisories/poisoned.yaml", "report-1.md", "report-2.md"]
    prompt: "Artifact data/extract.json is POISONED (units). Identify which report fields derived from it. Write rework-manifest.json listing tainted report fields only."
    validations:
      - type: file_exists
        path: "rework-manifest.json"
  - name: rework
    capture_files: ["rework-manifest.json"]
    prompt: "Re-derive ONLY the fields in rework-manifest.json from the corrected source (corrected-extract.json). Do not touch clean fields."
    validations:
      - type: content_regex
        pattern: "REWORKED-FROM: corrected-extract"
```
**Negative control:** with advisory generation removed, containment cannot name the tainted fields; **sentinel:** a final CLI validator asserts the rework output does NOT contain the poisoned field's signature value (e.g., the 1000× unit error) — with the pattern removed, it does, and the sentinel fails. Transient failures where the retry succeeded must NOT generate advisories — crying wolf burns the channel (pair with the Validity Window's failure-evidence aging).

---

## The Sealed Dissent

```yaml
---
name: "The Sealed Dissent"
scale: communication
status: working
forces: ["Partial Failure", "Accumulated Signal"]
generators: ["Exploit Failure as Signal"]
problem: "Systems erase rejected candidates, forcing every future chooser to pay full rediscovery price for the reasons the alternatives lost."
signals:
  - "selection stages: fan-out N candidates, fan-in picks one, the N−1 vanish"
  - "self-chains where iteration N must not re-derive what iteration N−1 already rejected"
  - "instrument probing: which backends can do X"
problem_note: "within-run lifetime only — the cross-run face is The Negative Ledger, a separate pattern with different lookup semantics"
stages:
  - name: candidates
    sheets: "fan_out(3)"
    instrument_guidance: "score-author's choice — each produces one candidate artifact"
    fallback_friendly: true
    purpose: "Generate N candidates with typed ids."
  - name: selection
    sheets: 1
    instrument_guidance: "strong reasoner — picks the winner AND writes the ledger"
    fallback_friendly: false
    purpose: "Write rejection-ledger.md: candidate id, validator verdict, one-line reason, evidence path."
  - name: consult-gate
    sheets: 1
    instrument_guidance: "instrument: cli — exact-id grep against the ledger, zero AI"
    fallback_friendly: false
    purpose: "Before any later attempt on a rejected candidate id, surface the sealed dissent; non-empty match escalates."
dependencies:
  selection: ["candidates"]
  consult-gate: ["selection"]
composes_with:
  - pattern: "The Negative Ledger"
    how: "same discipline, cross-run lifetime and canonical signatures — see that pattern"
  - pattern: "Variant Apparatus"
    how: "the sealed dissent is the record under a synthesis that had to choose"
  - pattern: "Rejoinder Ledger"
    how: "each sealed dissent is a rejoinder recorded, not resolved"
---
```

**Source:** Expedition 6 (Talmudic jurisprudence — the minority opinion sealed in the page, *teyku*; negative-results publishing, Bik 2024). Unique divergence: no cousin in the other five reports or the 111-pattern pool.

### Core Dynamic
The Talmud does not delete the minority opinion — it seals it in the record, and marks unresolvable disputes *teyku*: "this tension is real and unresolved." The live system needs a decision to proceed, but **the reasons the alternatives lost are load-bearing for every future chooser.** Suppressed null findings become the next lab's sunk cost — the negative-results literature's exact complaint.

**Review 2's split, executed.** "Archiving rejected siblings within a run is exact-id accounting. Preventing reattempts across runs requires canonical approach identity, versioning, expiry, and override semantics. These are two lifetimes and two lookup semantics forced into one entry." The Sealed Dissent keeps the within-run lifetime: **exact candidate-id accounting** — no prose matching, no signatures, ids the selection sheet itself minted. Matching is therefore trivially reliable: the consult gate greps for a candidate id string that cannot collide with prose.

### Marianne Score Structure
```yaml
sheets:
  - name: candidates
    instances: 3
    prompt: "Write candidate-{{ instance_id }}.json: {approach_id: 'cand-{{ instance_id }}', design, cost_estimate}."
  - name: selection
    capture_files: ["candidate-*.json"]
    prompt: "Pick the winner. Then append one line per LOSING candidate to rejection-ledger.md: 'REJECTED cand-N | verdict | one-line reason | evidence: candidate-N.json'."
    validations:
      - type: content_contains
        pattern: "REJECTED cand-"
  - name: consult-gate
    instrument: cli
    command: "! grep -E '^REJECTED cand-[0-9]+' rejection-ledger.md | grep -q \"cand-$1\" || (echo 'escalate: sealed dissent on ' \"$1\" && exit 1)"
```
**Negative control:** pre-seed the ledger with `REJECTED cand-2`; a downstream stage parametrized on `cand-2` must be escalated by the consult gate, not run. **Sentinel:** variant with the ledger write removed — the downstream stage runs `cand-2` unimpeded and a final validator fails on the known-rejected id appearing in output. When NOT to use: archives growing faster than the decision rate; write-only ledgers consulted by ritual.

---

## The Negative Ledger

```yaml
---
name: "The Negative Ledger"
scale: iteration
status: working
forces: ["Partial Failure", "Accumulated Signal"]
generators: ["Exploit Failure as Signal"]
problem: "Falsified approaches are forgotten between runs, so later scores re-burn full runs to rediscover known incompatibilities."
signals:
  - "long-lived workspaces where runs accumulate"
  - "the same vendor/tool/endpoint incompatibility rediscovered by a new score"
  - "integration scouting that should take minutes and takes a run"
stages:
  - name: attempt
    sheets: 1
    instrument_guidance: "score-author's choice — the work sheet whose failure is informative"
    fallback_friendly: true
    purpose: "Attempt the approach; failure evidence is captured, not discarded."
  - name: falsify-record
    sheets: 1
    instrument_guidance: "instrument: cli — on_fail post-step; writes the canonical signature, never prose"
    fallback_friendly: false
    purpose: "Append to ledger/negative.md: {signature_code, tool, endpoint, error_class, digest, ts}."
  - name: consult
    sheets: 1
    instrument_guidance: "instrument: cli — matches canonical signature codes only; zero AI"
    fallback_friendly: false
    purpose: "At the moment of decision, grep the planned approach's signature codes; non-empty match escalates to override-with-reason."
dependencies:
  falsify-record: ["attempt"]
  consult: ["falsify-record"]
composes_with:
  - pattern: "The Sealed Dissent"
    how: "the within-run, exact-id face of the same discipline"
  - pattern: "Dead Letter Quarantine"
    how: "DLQ learns within a batch; the ledger fences across runs"
  - pattern: "Fork-Evident History"
    how: "the ledger is append-only; overrides append to the same entry, growing a dissent of its own"
---
```

### Core Dynamic
Cross-run fence: **canonical approach identity or it does not exist.** Review 2: "grep over a prose signature is not identity and will both miss synonyms and block materially changed approaches." Review 3: "'rate-limited' vs '429' is named as a failure with no mitigation — canonical signature codes or a normalization step are one line away." The fix is the schema above: every entry carries a **closed-vocabulary signature code** (e.g., `AUTH-INCOMPAT`, `RATE-LIMITED`, `SCHEMA-BREAK`) plus the tool/endpoint pair — the things the deciding sheet can state before attempting. Consult matches signature codes, never prose. Override semantics: an override appends its reason **to the same entry** — the ledger grows a dissent of its own, and repeated overrides against an unchanged world are themselves a signal. Entries carry an expiry/generation stamp (a tool upgrade legitimately re-opens fenced ground — pair with the Validity Window's failure-evidence profile).

### Marianne Score Structure
```yaml
sheets:
  - name: attempt
    prompt: "Integrate vendor X per integration-plan.md."
    on_fail:
      - run: "printf 'SIG: AUTH-INCOMPAT | tool: vendor-x | endpoint: oauth2 | ts: %s\\n' \"$(date -Is)\" >> ledger/negative.md"
  - name: consult
    instrument: cli
    command: "! grep -q 'SIG: AUTH-INCOMPAT.*tool: vendor-x' ledger/negative.md || (echo 'FENCED: vendor-x AUTH-INCOMPAT — override requires a reason appended to this entry' && exit 1)"
    validations:
      - type: command_succeeds
```
**Negative control:** pre-seed the ledger with the planned approach's signature; consult must exit non-zero. **Sentinel:** variant with the ledger write removed — three weeks later, score B re-attempts vendor X; the consult gate cannot match, runs, and the sentinel validator fails on the known-bad string reappearing. When NOT to use: vocabulary drift across runs without the closed code set; write-only ledgers gating nothing.

---

# GROUP II — WITHIN-STAGE

## The Misclosure Ledger

```yaml
---
name: "The Misclosure Ledger"
scale: within-stage
status: working
forces: ["Structured Disagreement"]
generators: ["Verify through Diverse Observers"]
problem: "N parallel measurements of the same territory disagree within tolerance, and the system either fights over which is right or averages the disagreement away, when the residual is a quantity belonging to the whole system that should be measured, published, and allocated."
signals:
  - "N independent estimates of the same quantity with declared per-measurer weights"
  - "a fan-in tempted to average, vote, or argue"
  - "the disagreement budget can be declared in advance"
scope_fence: "additive quantities with a real closure constraint only — see When NOT to Use"
stages:
  - name: measure
    sheets: "fan_out(3)"
    instrument_guidance: "per_sheet_instruments across vendor families; stagger launches so correlated measurers don't stampede one vendor"
    fallback_friendly: true
    purpose: "Same brief, independent scalar estimates."
  - name: close
    sheets: 1
    instrument_guidance: "instrument: cli — no LLM allocates its own errors; computes residual, compares to tolerance, allocates by declared weights"
    fallback_friendly: false
    purpose: "Write corrections-{n}.json and the published misclosure ledger, or raise the blunder flag."
  - name: settle
    sheets: 1
    instrument_guidance: "instrument: cli — emits the adjusted record"
    fallback_friendly: false
    purpose: "Write adj-consensus.json; every sheet id present (no silent drops)."
dependencies:
  close: ["measure"]
  settle: ["close"]
composes_with:
  - pattern: "Concurrent Count"
    how: "a second CLI recomputes the residual — the published ledger cannot lie"
  - pattern: "Condorcet's Premise"
    how: "family-probe the panel when weights cannot be justified by track record"
  - pattern: "The Dropped Axiom"
    how: "the allocation table IS the declared aggregation function — typed, not concealed"
---
```

**Source:** Expedition 2 (geodetic traverse adjustment — 300 years of surveying practice; Bowditch/least-squares). The brief named it "the deepest unclaimed structure in the whole audit." Both reviews demanded narrowing; the narrowing is now the fence.

### Core Dynamic
Close a loop around a field and the endpoint does not land on the startpoint. The misclosure is not a scandal — it is the **sum of all the small honest errors**, and classical practice measures it, publishes it, and **allocates it back to the legs by declared weight**. The blunder/tolerance split is the second spine: within tolerance, distribute; beyond tolerance, quarantine the outlier leg and re-measure — never spread a blunder across honest legs. Fan-in as bookkeeping, not voting: no judge, no quorum, an allocation table with weights declared before the loop was walked.

**The narrowing that saves it (Review 2, Review 1).** Review 2: "traverse misclosure exists because measurements participate in a known algebraic closure constraint. Independent estimates do not owe a conserved sum, and 'allocating residual back' can manufacture agreement. As a generic disagreement pattern it is mathematically wrong." Accepted. The pattern's scope fence is now explicit: **additive quantities with a real closure constraint** — component estimates that must sum to a declared total (effort hours across phases, cost across line items, coverage across partitions). For free-standing estimates without closure, use One Field, Many Cores or Delphi Convergence. Review 1's multi-dimensional normalization demand is met by the fence plus per-dimension closure: each dimension closes against its own declared total, weighted independently; no cross-dimensional allocation is attempted.

**Weights have provenance (Review 3).** The weight ledger is a named, committed artifact (`tolerance.yaml`: per-measurer weights, declared tolerance, the closure total), authored before measurement; the retrospective that retunes weights writes a dated amendment to it — an auditable trail, not an aside.

### Marianne Score Structure
```yaml
sheets:
  - name: measure
    instances: 3
    prompt: "Estimate the migration effort in hours for phase P-{{ instance_id }} ONLY. Write estimate-{{ instance_id }}.json {hours: N}."
    response_format: { type: json_object }
  - name: close
    instrument: cli
    instrument_fallbacks: []
    command: "python3 scripts/close_loop.py estimates/ tolerance.yaml --out corrections.json --ledger misclosure.md"
    validations:
      - type: command_succeeds
      - type: content_contains
        path: "misclosure.md"
        pattern: "published-misclosure:"
  - name: settle
    instrument: cli
    command: "python3 scripts/settle.py corrections.json --out adj-consensus.json && jq -e '(.total | length) >= 3' adj-consensus.json"
    validations:
      - type: command_succeeds
```
`close_loop.py` publishes the recomputed residual and fails if the ledger's stated misclosure disagrees with the recomputed one — the ledger cannot lie. **Negative control:** inject one estimate off by 10× tolerance — the closer must exit non-zero and write `blunder-flag.txt` naming the outlier leg; allocation must NOT occur.

---

## One Field, Many Cores

```yaml
---
name: "One Field, Many Cores"
scale: within-stage
status: working
forces: ["Finite Resources", "Progressive Commitment"]
generators: ["Incremental Exposure"]
problem: "Survey-the-territory tasks are sized by feel — either 400 full reviews or one spot-check dressed as a survey — when the load-bearing decision is the sampling plan authored before any sampling."
signals:
  - "scan a codebase / review a document set / triage an inbox / probe a UI"
  - "fan-out width currently chosen by intuition"
  - "between-cell differences matter more than any single core's findings"
stages:
  - name: grid
    sheets: 1
    instrument_guidance: "instrument: cli — reads the committed manifest, partitions into cells, assigns K disjoint core slices"
    fallback_friendly: false
    purpose: "The sampling plan is an authored artifact with its own digest."
  - name: core
    sheets: "fan_out(cells × K)"
    instrument_guidance: "cheapest instrument that can notice the phenomenon; static width from the committed plan"
    fallback_friendly: true
    purpose: "Probe only your slice; emit {cell, findings, confidence}."
  - name: composite
    sheets: 1
    instrument_guidance: "instrument: cli — mechanical per-cell merge (dedup + confidence aggregation)"
    fallback_friendly: false
    purpose: "Emit field-map.yaml with per-cell composites and between-cell deltas."
  - name: heterogeneity-check
    sheets: 1
    instrument_guidance: "instrument: cli — flags cells whose cores disagree beyond the declared band"
    fallback_friendly: false
    purpose: "A cell containing both swamp and knoll composites into a lie — flag it for re-partition."
dependencies:
  core: ["grid"]
  composite: ["core"]
  heterogeneity-check: ["composite"]
composes_with:
  - pattern: "The Graded Net (priced variant, in Immune Cascade)"
    how: "the cell map decides which cells earn tier-2 money"
  - pattern: "First Article Characterization"
    how: "the composite is the field's first article — characterize it, not each core"
---
```

**Source:** Expedition 2 (precision-agriculture soil sampling: Clemson/UNL/ISU extension protocols). Both reviews rated it among the strongest; both demanded repairs, both repaired here.

### Core Dynamic
You cannot assay a whole field and you cannot trust one core. The agronomists' protocol: divide into cells; at each grid point take 10–15 cores in a small radius; **composite into one labeled sample per cell**. Compositing deliberately averages out arm's-length jitter and keeps cell-level difference — two composites differing means something. Translate: **the fan-out's design — cell count, cores per cell, core radius — is the load-bearing decision, made BEFORE sampling**, sized by a declared variance budget, with the merge a mechanical composite and the *cell map*, not any single core, as the artifact.

**Repairs.** Review 2: "the promise that the grid is correct before sampling… heterogeneous cells make the composite lie… add a heterogeneity test and distinguish missing-core refusal from an explicitly declared quorum." The heterogeneity-check stage is that test: within-cell core disagreement beyond the declared band flags the cell for re-partition instead of silently averaging the swamp with the knoll. Missing cores are a hard refusal by default; a quorum (proceed with K−1) must be **explicitly declared** in the grid manifest. Review 1: "if dynamic, the author is left wondering how to bind runtime partition counts" — the grid is **static and committed** (authored or generated at authorship time, digest-recorded); runtime-discovered partitioning is the Dynamic Muster's ground (candidates list), not this pattern's.

### Marianne Score Structure
```yaml
sheets:
  - name: grid
    instrument: cli
    command: "python3 scripts/make_grid.py manifest.yaml --cells 20 --cores 3 --out grid-plan.json && sha256sum grid-plan.json > grid-plan.sha"
    validations:
      - type: command_succeeds
  - name: core
    instances: 60            # cells × cores, STATIC, from the committed plan
    capture_files: ["grid-plan.json"]
    prompt: "Your slice is listed in grid-plan.json under core-{{ instance_id }}. Probe ONLY your slice. Write core-{{ instance_id }}.json {cell, findings[], confidence}."
    response_format: { type: json_object }
    validations:
      - type: file_exists
        path: "core-{{ instance_id }}.json"
  - name: composite
    instrument: cli
    command: "python3 scripts/composite.py grid-plan.json core-*.json --out field-map.yaml --missing refuse"
    validations:
      - type: command_succeeds
      - type: csv_unique_key
        path: "field-map.yaml"
        key: "cell, slice"
  - name: heterogeneity-check
    instrument: cli
    command: "python3 scripts/heterogeneity.py field-map.yaml --band 0.25 --out repartition-needed.txt"
```
**Negative control:** delete one core file — composite must fail for missing coverage under `--missing refuse`. Second control: a seeded heterogeneous cell must land in `repartition-needed.txt`, not in the map.

---

# GROUP III — ADAPTATION

## The Graded Ladder

```yaml
---
name: "The Graded Ladder"
scale: adaptation
status: working
forces: ["Accumulated Signal", "Partial Failure"]
generators: ["Threshold-Triggered Switch"]
problem: "Untyped escalation forces every interruption to be maximally expensive (always human) or maximally cheap (always auto) — both wrong at scale."
signals:
  - "every mixed AI/human score"
  - "retries that could silently absorb a real problem"
  - "WARN/INFO codes exist and someone must decide if they're benign"
stages:
  - name: work-with-typed-raise
    sheets: 1
    instrument_guidance: "score-author's choice — emits escalations as a typed enum field, never prose"
    fallback_friendly: true
    purpose: "Do the work; raises carry escalation_type: CONCERN | UNCOMFORTABLE | SAFETY."
  - name: concern-review
    sheets: 1
    instrument_guidance: "cheap instrument (select: cheapest) — auto-resolve WITH a receipt"
    fallback_friendly: true
    purpose: "Disposition CONCERN raises; append to the receipt ledger."
    skip_when: "test \"$(jq -r .escalation_type raises.json)\" == 'SAFETY' -o \"$(jq -r .escalation_type raises.json)\" == 'UNCOMFORTABLE'"
  - name: adjudicate
    sheets: 1
    instrument_guidance: "strong reasoner — must rule before work continues"
    fallback_friendly: false
    purpose: "Disposition UNCOMFORTABLE raises with a written ruling."
    skip_when: "test \"$(jq -r .escalation_type raises.json)\" == 'CONCERN' -o \"$(jq -r .escalation_type raises.json)\" == 'SAFETY'"
  - name: safety-pause
    sheets: 1
    instrument_guidance: "instrument: cli — fires the escalate/pause trigger; humans enter here"
    fallback_friendly: false
    purpose: "SAFETY reaches the human seam."
    skip_when: "test \"$(jq -r .escalation_type raises.json)\" != 'SAFETY'"
  - name: ledger-gate
    sheets: 1
    instrument_guidance: "instrument: cli — final gate; continuation requires the receipt ledger's unresolved-set to be empty"
    fallback_friendly: false
    purpose: "A gate, not a hope: no disposition, no continuation."
dependencies:
  concern-review: ["work-with-typed-raise"]
  adjudicate: ["work-with-typed-raise"]
  safety-pause: ["work-with-typed-raise"]
  ledger-gate: ["concern-review", "adjudicate", "safety-pause"]
composes_with:
  - pattern: "Transfer of Command at the Seam"
    how: "this pattern is the state machine; that one is the handoff protocol at the SAFETY seam"
  - pattern: "The Acknowledged False Alarm"
    how: "the suppress list is the pre-declared CONCERN class"
  - pattern: "Rejoinder Ledger"
    how: "every disposition is a rejoinder — one per raise, none omitted"
---
```

**Source:** Expedition 3 (TeamSTEPPS CUS — Concerned/Uncomfortable/Safety — and the two-challenge rule; aviation CRM). Owns the corpus's named unowned terminal: typed escalation.

### Core Dynamic
"Escalation" is one word for three different acts. Type the ladder the way CUS types it and the protocol writes itself: **CONCERN** — a WARN or soft signal; auto-resolve *with a receipt*. **UNCOMFORTABLE** — a failed validation or ambiguous judgment; an explicit adjudicator sheet must rule before work continues. **SAFETY** — declared by the raiser in structured output, or reached by the **two-challenge rule**: the same validation failing twice auto-raises one level — the counterweight that keeps auto-resolve from becoming a rubber stamp. The type lives in a typed field, never prose — prose is where expectation bias hides.

**The draft's fabrications, replaced with real syntax (Reviews 1 and 2).** Review 1: "a composer trying to write `{% if escalation_type == 'CONCERN' %}` in Marianne YAML will crash the parser. The routing must be specified as standard `skip_when`." Done — the structure above is predeclared branch sheets gated by `skip_when` on the typed artifact, exactly as prescribed. Review 1: "counting repeated validation failures 'from conductor state' — how? If by grepping `.marianne-observer.jsonl`, state that explicitly." Review 3 filed the conductor-state export as an uncited dependency; it stays flagged in the table above until cited. The buildable form today: the challenge counter is a CLI pre-step that counts the *sheet's own* retry attempts from its validation receipts in the workspace (written by `on_fail` post-steps, the same mechanism as the Negative Ledger) — engine-native, no observer scraping. Review 2's identity-key demand is met: a challenge is the **same validation id against the same artifact digest** — generic retry counts never escalate unrelated transients.

### Marianne Score Structure
See the YAML frontmatter stages; the load-bearing validations:
```yaml
  - name: ledger-gate
    instrument: cli
    command: "test -f ledger/escalations.md && ! grep -q 'DISPOSITION: none' ledger/escalations.md"
    validations:
      - type: command_succeeds
```
**Negative controls:** (a) an item raised twice (same validation id + digest) must land one level up — remove the counter and it auto-resolves forever; (b) a SAFETY raise with the pause trigger removed must still fail the final ledger-gate via the unresolved-set check. **Sentinel:** `field_match` that a CONCERN never reaches the safety-pause path (routing asserted mechanically).

### When NOT to Use
Vocabulary drift ("this seems maybe bad" is not a type); the human tier reached for anything routine — the ladder exists so SAFETY stays rare and *meaningful*; auto-resolve dispositions unrecorded.

---

## Transfer of Command at the Seam

```yaml
---
name: "Transfer of Command at the Seam"
scale: adaptation
status: working
forces: ["Information Asymmetry"]
generators: ["Contract at Interfaces"]
problem: "When work escalates from machine to human, the pause is the trivial half — what's missing is the briefing artifact that lets the receiving commander act without archaeology."
signals:
  - "every pause/escalate trigger and human-in-the-loop approval gate"
  - "every resume-after-overnight"
  - "AI-reviewer handoffs: an adjudicator receiving escalated work needs the same briefing shape"
stages:
  - name: work
    sheets: 1
    instrument_guidance: "score-author's choice — the sheet whose failure trips the seam"
    fallback_friendly: true
    purpose: "Normal work; on terminal failure the seam fires."
  - name: briefing
    sheets: 1
    instrument_guidance: "strong reasoner — inputs pinned to job state, validation output, and file facts so its output is verifiable"
    fallback_friendly: false
    purpose: "Compose the five-element briefing BEFORE the hold: situation, resources, objectives, organization, safety."
  - name: hold
    sheets: 0
    instrument_guidance: "trigger: escalate/pause — nothing runs"
    fallback_friendly: false
    purpose: "The seam itself."
  - name: disposition
    sheets: 1
    instrument_guidance: "instrument: cli — atomic temp-and-rename append to the command log"
    fallback_friendly: false
    purpose: "Record who resolved, what, effective time — from the human's resume action, not from an AI's clock."
  - name: resumed
    sheets: 1
    instrument_guidance: "the work instrument, continuation"
    fallback_friendly: true
    purpose: "Continuation whose prompt includes the disposition verbatim."
dependencies:
  briefing: ["work"]
  disposition: ["briefing"]
  resumed: ["disposition"]
composes_with:
  - pattern: "Transfer of Command"
    how: "that pattern owns planned succession between operators; this owns the machine→human seam specifically"
  - pattern: "The Write-Time Record"
    how: "the briefing is a write-time record for the escalation moment — no end-of-run archaeology"
  - pattern: "The Black-Box Ledger"
    how: "the briefing is assembled from the ledger's continuous record, never from the failing sheet's self-report"
---
```

**Source:** Expedition 3 (ICS Transfer of Command, FEMA: five-element briefing + announced effective time).

### Core Dynamic
The canonical ICS failure is an incident with two people both believing they hold command, or neither; command is never transferred by silence. The briefing artifact: **situation** (what the job was doing when it stopped), **resources** (which artifacts exist, which instruments ran, what they cost), **objectives** (what "resumed" means, stated as validations), **organization** (which sheets remain, which were skipped, what the skip means), **safety** (what must NOT be resumed and why). Two prohibitions carry the pattern: the briefing is assembled **from conductor state and workspace facts, never from the failing sheet's self-report** (self-authored review paths are counterfeit — the corpus knows this), and the effective-time record is not ceremony.

**Wiring corrected per the reviews.** Review 2: "if `pause`/`escalate` halts the job first, the downstream briefing sheet may never run. The briefing must be assembled and validated before the pause trigger, or emitted atomically by the failing path." The structure above assembles the briefing **before** the hold — the work sheet's `on_fail` runs the briefing sheet, and only its completion trips the pause; the briefing is validated while the job still has an executor. Review 2: "a machine timestamp cannot establish when a human actually accepted command; acceptance needs a separate disposition event." The disposition stage is exactly that event: it runs on resume, appended by the human's own resume action (the resume command's first hook), recording the acceptance time — distinct from the pause time the briefing carries. Review 1's demand ("who runs the shell one-liner?") is answered: the disposition append is the resume path's first act, mechanically fired, not a human memory ritual.

### Marianne Score Structure
```yaml
  - name: work
    on_fail:
      - run_job: briefing-score.yaml        # emits briefing.md BEFORE the hold
  - name: briefing
    prompt: "Assemble briefing.md with sections SITUATION, RESOURCES, OBJECTIVES, ORGANIZATION, SAFETY from job-state.json, validation-output.txt, and workspace file facts. Do NOT ask the failing sheet."
    validations:
      - type: content_contains
        pattern: "SITUATION:"
      - type: content_contains
        pattern: "RESOURCES:"
      - type: content_contains
        pattern: "OBJECTIVES:"
      - type: content_contains
        pattern: "ORGANIZATION:"
      - type: content_contains
        pattern: "SAFETY:"
  - name: disposition
    instrument: cli
    command: "printf '%s | resolved-by: resume-action | decision: %s\\n' \"$(date -Is)\" \"$MARIANNE_RESUME_DECISION\" > /tmp/cl && mv /tmp/cl command-log.jsonl.append"
  - name: resumed
    capture_files: ["briefing.md", "command-log.jsonl.append"]
    prompt: "Continue. Your first input is the disposition record; the briefing is your situation report."
    dependencies: { file_exists: "command-log.jsonl.append" }
```
Five separate `content_contains` checks — one per section — because a single-phrase luck-pass is exactly what killed rev-1 proofs. **Negative controls:** escalation fires with briefing assembly removed → the resumed stage cannot start (dependency unmet); a clean run must produce *no* briefing — the gate fails both ways or it's a receipt.

---

## The Acknowledged False Alarm

```yaml
---
name: "The Acknowledged False Alarm"
scale: adaptation
status: working
forces: ["Finite Resources", "Partial Failure"]
generators: ["Threshold-Triggered Switch"]
problem: "Suppression lists rot: entries accumulate silently until the suppressed set includes the code that meant the roof was on fire."
signals:
  - "a score run repeatedly over shifting inputs where some codes are known-benign for named reasons"
  - "brownfield pipelines where zero-warning is a multi-month project and you must ship now with honest debt"
  - "an ignore list that has never been reviewed since it was written"
stages:
  - name: acknowledge
    sheets: 1
    instrument_guidance: "strong reasoner — the one place one belongs: writing a mechanism-level benignity argument"
    fallback_friendly: false
    purpose: "PROPOSE a suppression: {code, mechanism_of_benignity, owner, evidence pointer, expiry}. Cannot edit the enacted list."
  - name: enact
    sheets: 1
    instrument_guidance: "instrument: cli — rebuilds the list file from accepted proposals, stamps digest, decrements countdowns"
    fallback_friendly: false
    purpose: "Expired entries drop and their codes revert to failing. The enacted list is digest-pinned."
  - name: run
    sheets: 1
    instrument_guidance: "the working sheets — their VALIDATION SCRIPTS read the list file"
    fallback_friendly: true
    purpose: "Work under the suppressions; unknown codes still fail."
dependencies:
  enact: ["acknowledge"]
  run: ["enact"]
composes_with:
  - pattern: "Configuration Control Board"
    how: "enactment is a one-seat CCB — propose and apply are distinguishable acts"
  - pattern: "The Validity Window"
    how: "the countdown is a per-entry TTL; expiry changes behavior, it does not merely log"
  - pattern: "The Graded Ladder"
    how: "the suppress list is the pre-declared CONCERN class"
---
```

**Source:** Expedition 5 (alert-fatigue economics — 50–80% false-positive rates in SOC triage; medicine's documented acknowledgement of known-benign findings).

### Core Dynamic
The naive reading of suppression is "an ignore list," and that reading is how alert fatigue kills regimes. The invariant: **every suppression is a named, reasoned, expiring, reviewable decision — never a permanent silence.** The hidden cost of noise is not the wasted triage; it's the real threat dismissed amid fatigue. Suppressions rot; expiry is the pattern.

**The engine disconnect, repaired honestly (Reviews 1, 2, 3).** Review 1: "`validate_suppress` is a static YAML list — a runtime sheet cannot modify the running score's parameters. As written, completely unbuildable." Review 2: "must be proved against actual engine loading semantics." Accepted, and the pattern no longer claims the engine primitive: the *mechanism* is **validation scripts that read a workspace list file** (`scripts/lint.py --ack-file suppress-list.yaml`). The engine-native `validate_suppress` key remains the pattern's *destination*, not its wiring: when a suppress-list file reference or dynamic suppression loading exists in the engine, the pattern adopts it and the proof obligation carries over. What `validate_suppress`'s existence still contributes today is the boundary discipline: ERROR-class codes are never suppressible — the primitive itself forbids it, and the pattern inherits that spine. Review 2's demand for a real reason-linter replaces the draft's cosmetic noun-phrase check: a proposal must carry **code existence, severity eligibility (WARN-only), owner, expiry, and an evidence pointer** — the enact stage rejects entries lacking any field, mechanically.

### Marianne Score Structure
```yaml
  - name: acknowledge
    prompt: "Propose suppressions for WARN codes proven benign. Each entry: {code, mechanism, owner, evidence, expiry_runs}. Mechanism must name WHY it is benign (e.g., 'partner pads exports with BOM; parser handles'), never 'known issue'."
    response_format: { type: json_object }
  - name: enact
    instrument: cli
    command: "python3 scripts/enact_suppressions.py proposed/ --out suppress-list.yaml --min-fields 5 && sha256sum suppress-list.yaml > suppress-list.sha"
    validations:
      - type: command_succeeds
      - type: file_sha256
  - name: run
    instrument: cli
    command: "python3 scripts/lint.py exports/ --ack-file suppress-list.yaml"
    validations:
      - type: command_succeeds
```
**Negative controls:** (a) a proposal missing the evidence field must be *rejected* by enact (field-count check — mechanical, not judgment); (b) an entry whose countdown reaches zero must drop from the list and its code must **fail again** — the control that proves expiry re-arms the alarm; (c) an unknown code must fail the run even with a non-empty list. When NOT to use: suppressions without expiry (the pattern is dead even if the YAML is valid); ERROR-class codes; copy-pasted reasons.

---

## The Near-Miss Ledger

```yaml
---
name: "The Near-Miss Ledger"
scale: adaptation
status: aspirational
blocked_on: "documented conductor status export (retry counts, durations, validation margins) as a score-readable artifact or stable API"
forces: ["Accumulated Signal"]
generators: ["Exploit Failure as Signal"]
problem: "Validation near-passes — the retry that succeeded on attempt 2, the check that passed by luck, the sheet that finished at 95% of its timeout — are silent holes in the defenses, and no pattern consumes them."
signals:
  - "repeated runs of the same score (trends across runs are the signal)"
  - "luck-dependent validations"
  - "capacity planning: duration-near-limit is tomorrow's outage"
stages:
  - name: execution
    sheets: 1
    instrument_guidance: "the normal score, with per-sheet attempt/duration events written to the workspace by on_fail/on_success post-steps (the buildable today-half)"
    fallback_friendly: true
    purpose: "Emit the events the harvester will read."
  - name: harvest
    sheets: 1
    instrument_guidance: "instrument: cli — external next-run collector over attempt/duration events; deterministic extraction, never an LLM summarizer"
    fallback_friendly: false
    purpose: "Write ledger/near-miss.md: class labels (recovered-failure, duration-near-limit, margin-narrow)."
  - name: adapt
    sheets: 1
    instrument_guidance: "strong reasoner — routes each class to a decision"
    fallback_friendly: false
    purpose: "Strengthen-the-gate, pin-the-flake, or accept-with-receipt; decisions append to the same ledger."
dependencies:
  harvest: ["execution"]
  adapt: ["harvest"]
composes_with:
  - pattern: "After-Action Review"
    how: "AAR learns from failures; this learns from non-failures — the optimistic twin"
  - pattern: "The Unprimed Falsifier"
    how: "the luck-pass detector is its standing ally"
---
```

**Source:** Expedition 6 (HRO theory — ASRS's 48-year near-miss corpus; Cooke 2006).

### Core Dynamic
HRO theory's core claim: near-misses are *more informative than failures per unit of damage* — they expose latent weaknesses while the system is still alive to fix them. The elegant part is the source: these signals are already in conductor state; the gap is that no pattern *consumes* them. Harvest, aggregate, route into adaptation.

**Why aspirational (Review 2's finding, accepted in full).** "The desired signals are not shown to be available. Retry counts and durations may exist in conductor state, but 'narrow-margin validations' generally do not unless validators emit margins. An `on_success` harvester inside the run cannot necessarily observe terminal status for the whole run. This needs a documented status API or an external next-cycle collector. Until then it is observability requirements disguised as a score." The pattern is therefore **aspirational, blocked on a cited conductor status export** (Open Question #2). The buildable today-half ships inside it: working sheets emit their own attempt/duration events via `on_fail`/`on_success` post-steps (same mechanism as the Negative Ledger), and validators that *can* emit margins (thresholds in `command_succeeds` scripts) do so; the harvester is a next-run collector over those events. When the documented export exists, the pattern upgrades to `working` unchanged in shape.

### Marianne Score Structure (today-half)
```yaml
  - name: harvest
    instrument: cli
    command: "python3 scripts/harvest_near_miss.py events/*.json --epsilon 0.1 --out ledger/near-miss.md"
    validations:
      - type: file_exists
        path: "ledger/near-miss.md"
```
**Negative control:** a seeded run with one forced-then-recovered failure — the harvester output must contain that sheet with class `recovered-failure`. **Sentinel:** harvester removed → no ledger, and the strengthened validation the adapt stage would have produced is confirmed never applied. When NOT to use: definitions so broad everything qualifies (the epsilon must be defended); ledgers routing to no decision — surveillance without response is voyeurism, not reliability.

---

# GROUP IV — SCORE-LEVEL

## The Serial Troponin

```yaml
---
name: "The Serial Troponin"
scale: score-level
status: working
forces: ["Finite Resources", "Progressive Commitment"]
generators: ["Graduate & Filter"]
problem: "Verification regimes test-to-complete — run every check, await every result, then decide — when most artifacts can be conclusively cleared cheaply but not conclusively convicted cheaply."
signals:
  - "logs, generated configs, dependency trees, translation drafts: one grep can clear, no grep can convict"
  - "the negative case is common and the expensive cascade should be rare, priced, pre-declared"
  - "re-test at interval is natural (the delta between measurements is signal)"
stages:
  - name: declare
    sheets: 1
    instrument_guidance: "instrument: cli — checks listed cheapest-first with PRE-DECLARED exit thresholds, committed and digest-pinned"
    fallback_friendly: false
    purpose: "Write pathway.yaml: per-tier check, exit threshold, retest interval."
  - name: test
    sheets: 1
    instrument_guidance: "instrument: cli — looped sheet; reads state.yaml, runs CURRENT tier's check, advances tier only on indeterminate, writes the typed next state"
    fallback_friendly: false
    purpose: "One typed carrier: state.yaml {status: ruled_out | indeterminate | escalate, current_tier}."
  - name: cascade
    sheets: 1
    instrument_guidance: "strong reasoner — the expensive conviction stage, OUTSIDE the loop"
    fallback_friendly: false
    purpose: "Runs only for escalations — rare by design, priced like it's rare."
dependencies:
  test: ["declare"]
  cascade: ["test"]
composes_with:
  - pattern: "Immune Cascade"
    how: "the priced variant's price table feeds this pathway's tier list; the Net prices the menu, the Troponin times the meal"
  - pattern: "Circuit Breaker"
    how: "the loop bound is a breaker against unbounded serial testing"
  - pattern: "Sign-Off Chain Against the Hard Date"
    how: "the cascade's verdict joins the sign-off record"
---
```

**Source:** Expedition 5 (emergency medicine's 0/1-hour high-sensitivity troponin rule-out pathways).

### Core Dynamic
The pathway's entire economic contribution is **early negative exit** — most cases are ruled out cheaply at step one or two. Two structural commitments make it work where "check things in order" doesn't: the negative-exit threshold is **declared before the first test** (post-hoc thresholds are how motivated reasoning enters), and **ambiguity does not exit** — intermediate results route to *repeat at interval*, not to the decision; the delta between measurements is the signal.

**Repairs per the reviews.** Review 1: "how does the looping sheet execute tier 1 on loop 0 and tier 2 on loop 1? The script must read a state file tracking the current tier." Exactly so — `state.yaml` carries `current_tier`, incremented only on `indeterminate`; the loop body reads it at the top of each pass. Review 2: "an `on_fail: escalate` is not naturally triggered merely because state.yaml says escalate — the transition needs an explicit gate; repeated tests must measure new evidence or greater depth, otherwise they are rerolls." The `until` expression keys on the typed status field, and the tier ordering is **monotone by construction** (each tier's check strictly deepens: schema → cross-check → semantic), with the retest interval forcing *new* evidence (a re-run against changed input, never an identical re-roll — the interval is input-version-keyed).

### Marianne Score Structure
```yaml
  - name: test
    instrument: cli
    loops:
      count: 3
      until: "workspace:state.yaml:status == 'ruled_out' || workspace:state.yaml:status == 'escalate'"
    command: "python3 scripts/pathway_step.py pathway.yaml state.yaml --input feed.xml"
    validations:
      - type: command_succeeds
  - name: legal-transition-gate
    instrument: cli
    command: "python3 scripts/check_transitions.py pathway.yaml state.yaml"
    validations:
      - type: command_succeeds
  - name: cascade
    skip_when: "test \"$(jq -r .status state.yaml)\" != 'escalate'"
    prompt: "The pathway escalated at tier N. Perform the full adversarial conviction review. Write verdict.json."
```
`check_transitions.py` recomputes — never trusts — that no `ruled_out` was emitted unless the tier's declared threshold condition actually held. **Negative controls, both required:** a seeded dirty input must drive the loop to `escalate` within `count`, never to `ruled_out`; a seeded clean input must exit at tier 1. Early exit on dirty and full-course runs on clean are the two ways this pattern fails. When NOT to Use: low negative predictive value in the first check; no natural re-test interval; surveillance rather than rule-out (you need positive conviction every run).

---

# GROUP V — ITERATION

## The Watch Rollover

```yaml
---
name: "The Watch Rollover"
scale: iteration
status: working
forces: ["Partial Failure", "Information Asymmetry"]
generators: ["Accumulate Knowledge"]
problem: "State that must cross an iteration boundary survives only as an external, typed, bounded artifact — context windows die and ledgers persist."
signals:
  - "long self-chaining improvement loops"
  - "bounded loops whose iterations are expensive enough that losing in-flight state at a restart matters"
  - "any score where 'how did the last period end' should have a durable answer"
stages:
  - name: period-work
    sheets: 1
    instrument_guidance: "score-author's choice — the period's work, in a sheet.loops bound or a self-chain cycle"
    fallback_friendly: true
    purpose: "Do the period's work."
  - name: rollover
    sheets: 1
    instrument_guidance: "instrument: cli — writes the four-section ledger under advisory lock with atomic rename; assembled from workspace facts, never the working sheet's self-summary"
    fallback_friendly: false
    purpose: "Write watch-ledger.md: COMPLETED / IN-FLIGHT / POISONED / NEXT-PLAN."
  - name: relief
    sheets: 1
    instrument_guidance: "next period's first sheet — echoes open exceptions before any new work (Readback's discipline at the seam)"
    fallback_friendly: true
    purpose: "Receive the watch: echo in-flight and poisoned items first."
  - name: audit
    sheets: 1
    instrument_guidance: "instrument: cli — diff check; the ledger grows monotonically, no period rewrites another's entries"
    fallback_friendly: false
    purpose: "Append-only enforcement, mechanically."
dependencies:
  rollover: ["period-work"]
  relief: ["rollover"]
  audit: ["relief"]
composes_with:
  - pattern: "Transfer of Command"
    how: "the rollover is scheduled transfer of command with the same ledger discipline"
  - pattern: "Cathedral Construction"
    how: "Cathedral persists the artifact across self-chains; this persists the operational exception set — compose both on long campaigns"
  - pattern: "checkpoint_persistence"
    how: "the carrier that survives restarts (engine primitive, unproven in any proof score — flagged)"
---
```

**Source:** Expedition 3 (ICS operational periods, watch relief at sea). Split from the draft's compound entry per Reviews 1 and 2.

### Core Dynamic
Each period ends with a durable ledger — completed / in-flight / poisoned / next-plan — and the next period begins by *reading* it, its first act an echo of the open exceptions. **A handoff nobody receives is a diary.** The ledger refuses the self-authored summary: it is assembled by a CLI from workspace facts, and the audit stage enforces append-only by diff.

**The split, and what happened to Rolling Continuity.** Review 1: "one is an iteration-boundary accounting contract; the other is a generational decay and pruning algorithm — jamming them together creates confusion." Review 2: "Rollover preserves the complete operational exception set; Continuity deliberately samples and expires a bounded subset — their data-loss policies are opposites." Executed. **Watch Rollover stands alone** (complete exception set, no sampling). **Rolling Continuity is demoted to a section of this pattern's ledger discipline** — the carry file: each cycle's carry is capped at a declared ratio (K entries, size-capped, generation-stamped; entries not re-confirmed for G generations dropped by script, not sentiment; excess drift against a frozen anchor digest routes to review with the carry quarantined). Its promotion as an independent pattern is deferred to the candidates list, owed Review 2's demanded metric: why the chosen carry ratio preserves useful state better than a capped priority queue. The answer is not yet demonstrated, so the pattern is not yet claimed.

### Marianne Score Structure
```yaml
  - name: rollover
    instrument: cli
    command: "python3 scripts/rollover.py workspace-facts/ --out watch-ledger.md --atomic && flock advisory.lock sha256sum watch-ledger.md >> ledger-hist.sha"
    validations:
      - type: content_contains
        path: "watch-ledger.md"
        pattern: "IN-FLIGHT:"
      - type: content_contains
        path: "watch-ledger.md"
        pattern: "POISONED:"
  - name: relief
    capture_files: ["watch-ledger.md"]
    prompt: "FIRST ACT: echo every IN-FLIGHT and POISONED item from watch-ledger.md as {item, blocking_reason}. Then begin this period's plan."
    validations:
      - type: content_contains
        pattern: "ECHO:"
  - name: audit
    instrument: cli
    command: "python3 scripts/append_only_check.py watch-ledger.md ledger-hist.sha"
```
**Negative controls:** two periods with the rollover removed — the second must fail its prelude dependency (`file_exists` on the ledger) rather than silently starting fresh; the proof asserts on the *state*, catching exactly the loss. An audit seeded with a rewritten prior entry must fail the diff. When NOT to use: short scores (no watch to relieve); ledgers written but never read (theater).

---

# GROUP VI — CONCERT-LEVEL

## The Capability Census

```yaml
---
name: "The Capability Census"
scale: concert-level
status: working
forces: ["Instrument-Task Fit", "Partial Failure"]
generators: ["Match Instrument to Grain"]
problem: "A fleet roster is a claim; a census is a proof — and the two artifacts must never merge because they are produced by different authorities and fail differently."
signals:
  - "a fleet launch whose members have decaying prerequisites (credentials, data drops, sibling services, disk state)"
  - "surge: know in seconds who can start"
  - "recurring multi-run workloads where instruments drift between authorship and run N+50"
stages:
  - name: roster-declare
    sheets: 1
    instrument_guidance: "instrument: cli — mechanical; one row per member with typed capability claims and probe contracts"
    fallback_friendly: false
    purpose: "Write roster.jsonl — the CLAIM, authored by the composer."
  - name: muster-probe
    sheets: 1
    instrument_guidance: "instrument: cli — deliberately serial; probes are cheap and serial probing is deterministic and rerunnable"
    fallback_friendly: false
    purpose: "Run each declared probe; write census.jsonl {member, probe_exit, evidence}. Probe failure is a STATUS, not a crash."
  - name: classify
    sheets: 1
    instrument_guidance: "instrument: cli — deterministic mapping from probe evidence to the closed vocabulary; NO judgment seat"
    fallback_friendly: false
    purpose: "Write readiness.json / capabilities.yaml with stale_after. Broken-by-default; disagreement with the roster is signal."
  - name: exceptions
    sheets: 1
    instrument_guidance: "strong reasoner — ONLY the exception rows; cites probe evidence"
    fallback_friendly: false
    purpose: "Adjudicate disagreement rows where the deterministic mapping cannot decide."
dependencies:
  muster-probe: ["roster-declare"]
  classify: ["muster-probe"]
  exceptions: ["classify"]
composes_with:
  - pattern: "Concurrent Count"
    how: "roster vs census are independent enumerations that must agree — the bijection is the count"
  - pattern: "Dormancy Gate"
    how: "the census is the gate's evidence source"
  - pattern: "Admission by First Cycle"
    how: "census establishes CAN RUN; first cycle establishes DOES RUN, validated"
---
```

**Source:** Expedition 4 (NIMS/ICS resource typing; DoDI 7730.66 possessed-vs-operational; OFRP); Expedition 1 (subcontractor prequalification, surety bonding) as the instrument-scale face (the Vendor Board fold: per-instrument fitness attested by a live prequal probe producing a machine-checkable `capabilities.yaml` with `stale_after` — the bonding letter that launders unfitness as qualification is the named failure both scales share).

### Core Dynamic
The roster answers "who belongs" — registration, mechanical, authored. The census answers "who can *run*, now" — obtained the only way orchestration gets answers: by executing a probe and reading its exit code. Reconciliation is a bijection with a typed third column — ready / dormant / broken, a closed vocabulary, broken-by-default. An admission granted is not an admission forever: capacity decays, tokens expire, vendors have incidents.

**The judgment fence, resolved (Review 3's contradiction, Review 2's sharpening).** Review 3: "'a census with judgment in it is an opinion poll' … then stage 3 is 'the one judgment seat.' Either bounded classification is exempt, or the fence is false." Review 2: "a reasoner should not translate probe exit codes into a closed vocabulary when a deterministic mapping can do it; that reintroduces opinion." Resolution: **the fence holds because the classification is now deterministic** — the `classify` stage is a CLI mapping probe evidence to vocabulary states by declared rules. What a reasoner may never do is invent a state or overrule a failed probe; what it *may* do (the `exceptions` stage) is adjudicate the residual disagreement rows the mapping cannot decide, citing probe evidence per row — and its output is itself a typed disposition, never a fourth state. A hallucinated fourth state fails the closed-vocabulary validation mechanically.

**Fail-closed admission (Review 2).** Downstream `skip_when` is fail-open on timeout — dangerous for admission. Admission therefore uses a **fail-closed entry validation** (a `command_succeeds` jq gate), not `skip_when`; visible skips keyed on readiness remain for non-admission decisions only. (The fail-open claim itself is flagged in the citation-owing list.)

### Marianne Score Structure
```yaml
  - name: muster-probe
    instrument: cli
    command: "python3 scripts/muster.py roster.jsonl --serial --out census.jsonl"
    validations:
      - type: csv_unique_key
        path: "census.jsonl"
        key: "member"
  - name: classify
    instrument: cli
    command: "python3 scripts/classify.py roster.jsonl census.jsonl --vocabulary ready,dormant,broken --default broken --out readiness.json --stale-after 24h"
  - name: entry-gate                    # fail-closed, in the CONSUMING score
    instrument: cli
    command: "jq -e 'all(.[]; .state == \"ready\")' readiness.json"
    validations:
      - type: command_succeeds
```
**Negative controls:** a member whose probe exits non-zero must classify not-ready — a census that green-lights a failed probe is a receipt (sentinel: `field_match` asserting the injected member's row reads `broken`); remove the census and the first downstream admission gate fails closed.

---

## The Fleet Receipt Ledger

```yaml
---
name: "The Fleet Receipt Ledger"
scale: concert-level
status: working
forces: ["Partial Failure"]
generators: ["Exploit Failure as Signal"]
problem: "Every fleet member ends in one of four states — completed, failed, never-started, unaccounted — and only the fourth is invisible without a ledger."
signals:
  - "every fleet run that matters enough to audit — which is every fleet run, because unaccounted members are how partial failure hides at fleet scale"
  - "non-waiting children without receipts (the unaccounted-member generator)"
stages:
  - name: collect
    sheets: 1
    instrument_guidance: "instrument: cli — in an OUT-OF-BAND auditor child score, spawned non-waiting at fleet launch; not a depends_on-all terminal group"
    fallback_friendly: false
    purpose: "Gather every receipt into receipts/ — no judgment."
  - name: reconcile
    sheets: 1
    instrument_guidance: "instrument: cli — the bijection as a jq program; accounting that is a set operation cannot be argued with"
    fallback_friendly: false
    purpose: "Roster set == receipt set; mismatches become typed exceptions: unaccounted / duplicate / orphan."
  - name: disposition
    sheets: 1
    instrument_guidance: "strong reasoner — one disposition per exception row, each citing evidence"
    fallback_friendly: false
    purpose: "Write dispositions.jsonl; row count == exception count, no omissions."
dependencies:
  reconcile: ["collect"]
  disposition: ["reconcile"]
composes_with:
  - pattern: "The Non-Waiting Hand"
    how: "mandatory companion — unclosed spawn rows are unaccounted members"
  - pattern: "Demobilization Checkout"
    how: "this is that pattern lifted from a concert's terminal score to fleet authority"
  - pattern: "Rejoinder Ledger"
    how: "dispositions map one-to-one onto exceptions — no omitted, no duplicated"
---
```

**Source:** Expedition 4 (military change-of-command inventory — joint reconciliation of property books; DoDI 7730.66's prohibition on unverified reports). Collision §1.2 — one of five dual-enumeration arrivals. Both reviews called it the strongest concept; both found the wiring broken; the wiring is rebuilt.

### Core Dynamic
Exceptions fall into exactly three typed classes: *unaccounted* (roster member, no receipt), *duplicate* (one member, several receipts), and *orphan* (receipt, no roster member — the most interesting class: **something ran that the composer never declared**). Then, and only then, judgment enters: dispositions, one per row, each citing evidence. The ledger is the fleet layer's proof of work — the artifact that lets someone who was not present reconstruct what actually happened, member by member.

**The fatal wiring problem, fixed (Review 2).** "An accounting group depending on all working groups may never run when a group fails — the exact case it must account for." Correct, and damning as drafted. The rebuilt execution path: the auditor is an **out-of-band child score**, spawned non-waiting (the Non-Waiting Hand's own mechanism) at fleet launch, polling the shared workspace for receipts and reading terminal conductor state **regardless of child outcome**; it runs to completion even when the fleet partially fails — that is its entire reason to exist. Review 1's demand (receipts must be machine-checkable, not prose) is the schema: `{member, status, digest, timestamp, validation_set}`.

### Marianne Score Structure
```yaml
# In the auditor child score (spawned at fleet launch, non-waiting):
  - name: reconcile
    instrument: cli
    command: "python3 scripts/reconcile.py roster.jsonl receipts/ --out reconciliation.json"
    validations:
      - type: command_succeeds
      - type: csv_unique_key
        path: "receipts/"
        key: "member"
  - name: disposition
    capture_files: ["reconciliation.json"]
    prompt: "For each exception row, write ONE disposition citing evidence: {exception, disposition, evidence}."
    response_format: { type: json_object }
    validations:
      - type: command_succeeds
        command: "test $(jq 'length' reconciliation.json) -eq $(jq 'length' dispositions.jsonl)"
```
**Negative control:** delete one member's receipt before reconciliation — the bijection gate must fail and the disposition sheet must record an unaccounted-member disposition. **A ledger that cannot catch a missing receipt is a receipt.** When NOT to use: single-score work (the conductor already accounts for sheets); prose receipts; a reconciliation that has never once reported an exception in rehearsal — a fleet that has not rehearsed its failures.

---

## The Non-Waiting Hand

```yaml
---
name: "The Non-Waiting Hand"
scale: concert-level
status: working
forces: ["Partial Failure", "Information Asymmetry"]
generators: ["Contract at Interfaces"]
problem: "A parent that waits on N sequential children lives N lifetimes, and its cadence — the thing downstream consumers depend on — breaks; but spawning without a contract is fire-and-forget."
signals:
  - "continuous producers with derivative work: monitoring spawning investigations, digests spawning deep-dives, builds spawning releases"
  - "the parent's rhythm is the product and children are consequences"
stages:
  - name: spawn
    sheets: 1
    instrument_guidance: "instrument: cli — appends the ledger row THEN carries the concert trigger; single writer (the parent is the only appender)"
    fallback_friendly: false
    purpose: "Append spawn-ledger.jsonl {child_id, score, ts, trigger_digest}; submit child via concert trigger, CONTINUE."
  - name: child-work
    sheets: 1
    instrument_guidance: "the child score's work sheets — a full score, not a fan-out sheet"
    fallback_friendly: true
    purpose: "Do the derivative work."
  - name: receipt
    sheets: 1
    instrument_guidance: "instrument: cli — the child's terminal act; writes into the shared workspace under its own child_id path (collision-proof)"
    fallback_friendly: false
    purpose: "Write receipts/{child_id}.json {status, digest, ts}. Closes the ledger row."
  - name: reconcile
    sheets: 1
    instrument_guidance: "instrument: cli — next cycle; unclosed rows are the visible failure state"
    fallback_friendly: false
    purpose: "List every spawn: closed, running (lease live), or unclosed (investigate)."
dependencies:
  child-work: ["spawn"]
  receipt: ["child-work"]
  reconcile: ["receipt"]
composes_with:
  - pattern: "The Fleet Receipt Ledger"
    how: "unclosed rows are unaccounted members — the auditor consumes this ledger"
  - pattern: "Is-Line-Clear"
    how: "before each spawn, check the receipt lane is clear"
  - pattern: "Canon of Phases"
    how: "compose when a rotating parent spawns non-waiting children"
---
```

**Source:** Expedition 4 (mission command's intent-based tasking; OFRP surge semantics). Claims `trigger_concert`-shaped machinery (zero proof-score exercise of non-waiting `concert` — flagged in the table). Review 2's verdict — "genuinely distinct; the strengthenings are not reasons to cut it" — is the pattern's mandate.

### Core Dynamic
Waiting is a coupling; this pattern is a **decoupling with a contract instead**. The parent submits a child via `concert` (submit without waiting; `inherit_workspace: true` shares lineage) and continues. What keeps this from fire-and-forget negligence is the interface: the parent writes a **spawn ledger** (append-only JSONL), and the child, as its terminal act, writes a **receipt**. The pair — spawn row and receipt — is the complete communication between generations, deliberately inspectable. **Unclosed rows are the pattern's visible failure state** — not an error, a reconciliation gap. The hand is *typed*: the child knows from its prelude which ledger row spawned it, and its receipt closes that row.

**Review 2's strengthenings, all built in:** single-writer ledger (the parent is the only appender; children write receipts, never ledger rows — no locks needed); stable child job ids (the ledger's `child_id`, minted by the parent, is the receipt's filename — collision-proof by construction under `inherit_workspace`); deadlines/leases (each row carries a `lease_until`; a row past lease without receipt is *lost*, not *running* — the reconcile stage distinguishes the three states mechanically).

### Marianne Score Structure
```yaml
# Parent score:
  - name: spawn
    instrument: cli
    command: "CID=\"child-$(date +%s)-$$\"; printf '{child_id: %s, score: investigate.yaml, ts: %s, lease_until: %s}\\n' \"$CID\" \"$(date -Is)\" \"$(date -d '+2 hours' -Is)\" >> spawn-ledger.jsonl"
    validations:
      - type: command_succeeds
    triggers:
      on_success:
        - concert: { score: investigate.yaml, inherit_workspace: true }
# Child score (terminal sheet):
  - name: receipt
    instrument: cli
    command: "printf '{child_id: %s, status: done, digest: %s, ts: %s}\\n' \"$MARIANNE_CHILD_ID\" \"$(sha256sum findings.md | cut -c1-12)\" \"$(date -Is)\" > \"receipts/$MARIANNE_CHILD_ID.json\""
    validations:
      - type: file_exists
        path: "receipts/{{ child_id }}.json"
```
**Negative control:** remove the child's receipt sheet — the parent's next-cycle reconciliation must report the row unclosed and escalate (or the Fleet Receipt Ledger flags it). **If nothing anywhere can notice the unclosed row, the contract is decorative** — that control is the proof. When NOT to use: the parent's next step genuinely needs the child's output — that is a dependency, and non-waiting is malpractice.

---

## Admission by First Cycle

```yaml
---
name: "Admission by First Cycle"
scale: concert-level
status: working
forces: ["Progressive Commitment", "Exponential Defect Cost"]
generators: ["Incremental Exposure"]
problem: "A fleet bets repetition on a member after one instance — and one validated instance proves only that one instance passed, unless the instance ran at full strength and the proof is fresh."
signals:
  - "fleet groups consume one another's outputs — corpus pipelines, data platforms, release trains"
  - "fleet-growth moments: this is how a new score earns its seat"
  - "members with decaying prerequisites where 'worked last week' is a claim, not evidence"
stages:
  - name: proving-cycle
    sheets: "fleet group"
    instrument_guidance: "each member score runs its REAL validations — a first cycle with gates removed is the fleet-level luck-passing content_regex"
    fallback_friendly: false
    purpose: "One full validated cycle per member, per member's own validation set."
  - name: admission-gate
    sheets: 1
    instrument_guidance: "instrument: cli — fail-closed jq over the receipt ledger; every member present, every receipt recording the FULL validation set, every timestamp inside the staleness bound"
    fallback_friendly: false
    purpose: "Consume evidence of completion (receipts), not merely the conductor's group transition."
  - name: production
    sheets: "fleet group"
    instrument_guidance: "the working groups; depends_on proving"
    fallback_friendly: true
    purpose: "The admitted cohort runs the recurring work."
dependencies:
  admission-gate: ["proving-cycle"]
  production: ["admission-gate"]
composes_with:
  - pattern: "Capability Census"
    how: "census = CAN RUN; first cycle = DOES RUN, validated — compose both before admitting"
  - pattern: "Sign-Off Chain Against the Hard Date"
    how: "the receipt is a sign-off against a specific obligation, with a TTL"
  - pattern: "The Validity Window"
    how: "receipt TTL — a first-cycle receipt from last week is evidence about last week"
---
```

**Source:** Expedition 4 (OFRP phase ordering — basic before integrated before sustainment). Uses `fleet` groups with `depends_on` (zero proof-score exercise — flagged). Split from the Readiness Cycle per Review 2; the cycle form (refit → solo-prove → joint-exercise → standing-watch) moves to the candidates list with its additional claim (cross-member interface failures visible only in joint exercise) owed its own proof.

### Core Dynamic
The engine already encodes the theorem — fleet groups with `depends_on` wait for named groups' first cycle — the pattern is the discipline that makes the wait meaningful. Three clauses: the proving group's first cycle runs under the member's *real* validations, never degraded ones; admission consumes *evidence* (receipts recording the full validation set), not merely the conductor's transition; **the proof ages** — admission carries a staleness bound. The deep structure is induction's: one validated instance establishes the member *can* complete; the fleet bets repetition on it — sound only if the instance was validated at full strength, because integration multiplies any single member's defect across every other member.

**Review 2's narrowings, adopted:** engine-authored receipts (the receipt is written by the member score's terminal CLI act with its validation set recorded — not self-reported prose); freshness rule (the admission jq checks timestamps against the staleness bound); the cycle form separated out. Gate-direction discipline (the draft's most error-prone detail, per Review 3's citation demand): admission gates are **fail-closed validations**; `skip_when` is reserved for repair-path routing where fail-open toward repair is intended — and the fail-open-on-timeout behavior itself is flagged in the citation-owing list.

### Marianne Score Structure
```yaml
fleet:
  groups:
    - name: proving
      members: [ingest-a, ingest-b, ingest-c]     # each runs its own full validations
    - name: production
      members: [model, publish]
      depends_on: [proving]
# The admission gate (first sheet of the production group's entry):
  - name: admission-gate
    instrument: cli
    command: "python3 scripts/admit.py receipts/ roster.jsonl --require-validation-set full --staleness 7d"
    validations:
      - type: command_succeeds
```
**Negative controls:** (a) a variant with one proving member's validations removed — the admission gate must reject its receipt (validation-set field mismatch); (b) a receipt older than the staleness bound must be rejected — freshness is load-bearing, not decorative. When NOT to use: genuinely independent groups (nothing flows between them — the dependency serializes for nothing); first cycles expensive relative to the work; weakened first-cycle validations ("first-cycle-lite" is the failure mode).

---

# Candidates Not Promoted

Recorded with their owed obligation; none is dead.

- **The Bounded Grep** (Dodge-Romig sampling with rectifying escalation) — **first in the proof order**; the strongest candidate to promote on proof.
- **The Readiness Cycle** (refit → solo-prove → joint-exercise → standing-watch) — the fleet lifecycle form split out of Admission by First Cycle; owes a proof that joint exercise surfaces cross-member failures solo cycles cannot.
- **The Commander's Budget** — cut from core (Reviews 1 and 2: engine cannot enforce per-sheet envelopes; `cost_limits` is job-level). Honest remainder: an out-of-band spend ledger + predeclared degrade branches (envelope-state `skip_when` dropping tiers) CAN be built today — that narrower pattern is a candidate, and its first proof owes the degrade-event negative control. If the engine grows per-sheet limits (Open Question #5), the full form returns.
- **The Watch Bill** — cut (Review 3: thinnest unique ground, heaviest unproven stack). Its content folds: assignment-under-budget → Capability Census + the Budget candidate; per-period spawning → the Non-Waiting Hand; rotation → Canon of Phases. Re-enter only with a parent/child score-generation protocol, a constrained renderer, and bill-row↔child-job reconciliation (Review 2's conditions).
- **Rolling Continuity** — demoted to Watch Rollover's carry-file section; independent promotion owed the capped-priority-queue comparison metric.
- **Stamp Before Steel** (two gates: intention vs. state, digest-diffed pre-commit); **The Keystone Probe** (BACI site-minus-control deltas); **The Intensifying Channel** (bandwidth graded by run health); **The Sole-Source Confession** (per-sheet fallback policy as a visible risk register); **The Arbitrated Window** (fan-in admission pacing); **The Voted Blend**, **The Rostered Watch**.
- **Missing elements the reviews named, seconded as candidates**: The Dynamic Muster (runtime-manifest fan-out bridging — Review 1); The Checkpoint Re-Anchor (crash rehydration over existing workspace artifacts — Review 1; adjacent to Self-Stabilizing Custody); The Quota Shunt (pre-flight rate-limit probing and alias shunting — Review 1); The Uncorrupted Baseline (golden-master calibration of evaluation scores themselves — Review 1, adjacent to The Unprimed Falsifier).

# Open Questions

1. **Citation-owing engine behaviors** (Review 3): (a) `skip_when` fail-open on timeout; (b) conductor export of retry counts/durations as score-readable data (blocks Near-Miss Ledger's `working` status); (c) `fleet.depends_on` first-cycle vs. full-completion semantics. Verify against engine source before the prove path builds on them.
2. **Mid-fan-out cancellation** (quorum-first cores) — blocked, no primitive; wanted by Expeditions 1 and 2. Still named.
3. **Runtime price discovery** — instruments quoting cost at runtime; blocked at parse-time resolution. The day it exists, Immune Cascade's priced variant goes fully live.
4. **Per-sheet cost budgets** — `cost_limits` is job-level; the Budget candidate's envelopes are the honest permanent workaround unless the engine grows per-sheet limits.
5. **Unclaimed after this pass:** `schedule_pinning`, `sheet_descriptions`, `stagger_delay_ms` as quorum (claimed only as launch hygiene), select-modifier portfolio doctrine.
6. **Proof-score repair debt** (Reviews 1 and 3): six of seventeen historical proof files fail `mzt validate` (echelon-repair, immune-cascade, dead-letter-quarantine, prefabrication, shipyard-sequence, source-triangulation — folded-command checks, dead workspace parents). The prove path should repair before it extends.

---

# Review Integration

Three adversarial reviews attacked `04-draft-corpus.md`; all three returned **NEEDS REVISION**. Review 1 (The Practitioner) tested every pattern against the engine's parser and causal topology and re-audited the 17 proof scores. Review 2 (The Skeptic) applied the structural-identity test — same DAG, state machine, channel, authority, failure semantics — and read every proof score's primitive usage. Review 3 (The Newcomer) read as someone who installed Marianne that morning, and grepped the entire proof estate for the primitives the draft leans on. Here is what changed, and why.

## Systemic changes (all three reviews)

1. **YAML or it didn't happen (Review 3's category failure).** "There is not one line of YAML in the entire draft… I cannot author a score from any of them." Every pattern in this document now carries a loadable structure in the engine's dialect (modeled on the proof scores' and existing pattern files' syntax: sheets, instances, instrument, capture_files, validations with real types, on_fail post-steps, triggers). Fictional syntax — Jinja2 stage routing, in-loop fan-outs, dynamic `validate_suppress` file arguments, mid-sheet suspension — is gone or replaced with the real mechanism, per pattern below.
2. **The Pattern × Primitive × Proof-Status Table (Review 3's most-useful-artifact demand).** Every load-bearing primitive is marked native-proven / native-unproven / blocked, with proof-score exercise counts from Review 2's grep: zero hits across all 17 scores for `response_format`, `failure_history`, `validate_suppress`, `triggers` (beyond self-chain), `sheet.loops`, `checkpoint_persistence`, `fleet`, `flow_expressions`, `stagger_delay_ms`, `select:`. The draft's claim that eight zero-mention primitives were "under pattern discipline" was true as intent and false as evidence; the table is the permanent correction, and the prove order below targets exactly the unproven columns.
3. **Structural fingerprints over collision counts (Review 2's governing rule).** "Collision count is not evidence of identity; it is at most evidence that several domains noticed a similar pressure." Adopted as merge policy #2. The five-fingerprint test (DAG, state machine, communication channel, decision authority, failure semantics) is why Aged Lead and Held-State Clock folded, why Sealed Dissent and Negative Ledger split, and why the Graded Net is now a variant rather than a pattern.
4. **Composite headings banned (Reviews 1 and 3).** "The 'X' merge must be severed" (Review 1); "smuggling five demoted patterns back in as 'faces' blurs exactly the boundaries the collision stage paid to draw" (Review 3). All five compound entries are severed: two splits (Sealed Dissent/Negative Ledger; Watch Rollover/Rolling Continuity), one demotion-to-section (Rolling Continuity), one fold already accepted (Pre-Load → Immune Cascade's priced variant), one split-to-candidates (Readiness Cycle). Vendor Board stays folded into Capability Census — as an instrument-scale face with the *same* fingerprint (claim vs. proof), which passes the test the others failed.
5. **Sentinels specified (Review 3).** "Six 'sentinel' mentions, zero sentinel specifications." Every negative control in this document names its sentinel as a concrete final CLI validator and what string or state it asserts on.
6. **Two vocabularies, reconciled enough (Review 3).** The draft used sheets/stages/movements interchangeably and never defined cadenza, spec_tags, wrapped prompt. This document uses `sheet`/`stage` consistently, defines engine terms inline at first use, and points to the corpus `glossary.md` for the rest.

## Cuts and folds, pattern by pattern

**The Aged Lead → folded into The Validity Window as the failure-evidence profile** (Review 2: "this is The Validity Window applied to failure records, not a distinct graph… per-class half-lives are policy constants with no calibration method"; Review 1: "in a single 3-minute run every failure occurred 45 seconds ago — without an explicit workspace persistence contract, the aging script evaluates a static list"). Both repairs are recorded in the Validity Window's updated file: the failure-evidence profile (fresh/recent/stale response table, per-class half-lives) and the demand that the half-life table is a committed artifact with declared first-run seed values and a retuning loop — Review 3's "fence without a gate" finding. The Poisoned-Artifact Advisory's composes-with edge now points there.

**The Held-State Clock → folded into The Validity Window as the held-work profile** (Review 2: "hash equality proves unchanged bytes, not continuing external validity; a mutable API can remain represented by an unchanged stale extract — fold with pause/resume times, horizon class, and a source re-observation rule"). The fold carries Review 2's sharpening in: digest equality is byte-truth, and live-horizon inputs get re-observation at resume, not just re-hashing. Review 1's praise ("composed and validated in under 5 minutes — excellent pattern") is why the profile keeps a full executable structure in the Validity Window file rather than a paragraph.

**The Graded Net → folded into Immune Cascade as the priced variant** (Reviews 2 and 3). Review 3: "an unaddressed collision, the draft's own kill-condition… [Immune Cascade's header] is word for word the Graded Net's claimed invariant… its honest differentiators are real — but they are strengthenings of Immune Cascade, and the draft neither names it nor composes with it. By its own policy #1, that is a violation." Review 2: "cut as a duplicate of Immune Cascade/Echelon Repair." Adjudication: fold, not cut — the differentiators survive as Immune Cascade's priced-variant section: committed `tiers.yaml` price tables (digest-pinned, with authored first-run values — Review 3), the ≥10× tier-cost ratio collapse rule, promotion-by-declared-risk not habit, dual-instrument-family tier 3 (correlated error is the enemy at the top), tier isolation of prose (each tier receives only paths, so reviewers cannot be anchored), and the Pre-Load shrinking-fan-out face. The overlap note in the composition edges now names both Echelon Repair and Immune Cascade.

**The Automatic Curriculum → folded into Dead Letter Quarantine** (Reviews 1 and 2). Review 1: "literally a one-line YAML key — there is no pattern to compose here." Review 2: "this substantially re-proves Dead Letter Quarantine: failure → analyze/carry evidence → adapted regeneration → revalidate; transport is not a new control structure." The fold records what the draft got right (the `failure_history` + `sheet.loops` composition is the conductor-mediated transport DLQ lacked; the raw-mode negative control idea) and the corrected control (Review 2: "test omission of the cited correction, not byte-identical recurrence" — stochastic generation owes direction, not repetition). The `lookback_sheets: 0 means ALL` trap (workspace.py:346, per the v6 archive) is restated in the fold because the draft's When-NOT-to-Use carried it as a warning worth keeping.

**The Anthesis Window → folded into Sign-Off Chain Against the Hard Date as the ripening face** (Review 3: "mechanically it is an until loop over a file-fact probe + a hard date + a recorded fallback waiver… if the corpus is willing to fold Pre-Load, consistency demands the same treatment here"; Review 1 confirms composability in 8 minutes; Review 2's two real repairs carried into the fold). The repairs: observation execution succeeding while its *result* remains `not_ready` are separate fields (a passing probe run with an unmet marker is the normal loop condition, not a validation failure); the negative controls are premature marker, absent marker at deadline, forged waiver on the marker path (perjury — `file_exists` on `waiver.json` asserted ONLY on the fallback path), and marker regression — not the draft's strawman calendar-sleep. The two-sided failure geometry (regrow vs. window-close) is preserved as the face's teaching frame; the hard date and waiver join the sign-off record.

**Anonymous Rounds → folded into Delphi Convergence** (this pass's own catch, missed by all three reviews — recorded here because Review 3's Graded-Net finding established the standard). The corpus already owns Delphi; the draft's real additions fold in as sections: mechanically computed aggregates as the ONLY between-round feedback (median + IQR + anonymized outlier-reason digest, computed by a CLI stats sub-step — never a sibling's prose), the honest stopping rule (IQR stability; non-convergence published as the finding), the anonymity content_regex gate (no aggregate may contain a sibling sheet id), and the round cap of 3–4 as load-bearing. Review 2's structural repairs carried in: the anonymity wall is convention, not access control — path-scoped visibility or per-sheet workspaces are required for the claim, and the fold says so; the identical-inputs control tests the statistic only, and the anonymity negative control must instead plant an identifiable sibling answer and assert the aggregate cannot quote it. Review 3's boundary paragraph (frames differ → Rashomon Gate; same question over rounds → Delphi; parallel measurements with declarable tolerance → Misclosure) is quoted into the Delphi file's When-to-Use.

**The Wordless Manual → dissolved** (Review 2: "a bundle of three techniques — least-context manifests, output schemas, negative examples — not one state machine… cut as a standalone; distribute the useful constraints"; Review 1: "strip references to compile-time spec_tags — a runtime sheet cannot alter Stage 2's compile-time context filters"). Dissolved exactly as ordered: least-context manifests → Prefabrication (interface contracts; the manifest-with-hashes is the contract's worker face); output scaffolds → Readback Before Commit (the scaffold is a shape the echo must fit) and The Attested Merge Gate; negative examples refreshed from failure receipts → Dead Letter Quarantine's fold (the curriculum teaches the sheet; the crossed-out examples teach the desk — same `failure_history` substrate). Review 3's dissent — "the only pattern in the draft that reduces error ex ante rather than policing it ex post" — is recorded here, not buried: the ex-ante discipline survives as a named section in Prefabrication ("prevention by desk design"), and if a proof shows the bundled form has a distinct fingerprint, it re-enters as a candidate.

**The Watch Bill → cut to candidates** (Review 3: "thinnest unique ground, heaviest unproven dependency stack, weakest When-to-Use"; Review 1: "a multi-hour engineering task, not a 10-minute pattern"; Review 2: "a meta-orchestration/code-generation act — needs a parent/child score protocol, a constrained renderer, validation before submission, and exact bill-row reconciliation"). See Candidates. The assignment-vs-rotation insight is real and is recorded in the Canon of Phases composition edge.

**The Commander's Budget → cut to candidates** (Reviews 1, 2, 3 unanimous on the engine mismatch). Review 3 caught the internal contradiction: "Line 14: per-sheet cost budgets are blocked. Line 631: each metered sheet runs under a cost_limit derived from its envelope." The honest remainder (out-of-band ledger + predeclared degrade branches) is a candidate with its control named. The combined-YAML promise the draft made is NOT claimed as answered here; it transfers to the prove path's first composition proof (Serial Troponin over Immune Cascade's priced tiers is the designated pair).

**Admission by First Cycle × Readiness Cycle → split** (Review 2: "one successful instance proves only that one instance passed, not that repetition is safe — keep the admission gate; move the cycle form to a separate candidate"). Executed; the cycle's joint-exercise claim is precisely the part owed its own proof.

## Strengthenings, pattern by pattern (survivors)

- **Readback Before Commit** — echo restricted to normalized machine-checkable fields (Review 1); four-node graph with echo-only receiver (Review 2); minimal complete YAML + instrument-support note + bounded correction loop (Review 3). The instrument note: `response_format: json_schema` support varies by instrument — probe it on your panel before relying on the echo gate (see proof order #1).
- **The Poisoned-Artifact Advisory** — phantom consumer retries replaced with an explicit containment + rework DAG (Reviews 1, 2); advisory typed and aged via the Validity Window fold.
- **The Sealed Dissent / Negative Ledger** — split (Review 2); exact-id matching within runs, canonical signature codes across runs with closed vocabulary, expiry, and override-appends-to-entry (Reviews 2, 3).
- **The Misclosure Ledger** — narrowed to additive closed systems with a declared closure total (Review 2); per-dimension closure for vectors (Review 1); weight ledger as a committed, auditable artifact with dated amendments (Review 3).
- **One Field, Many Cores** — static committed grid (Review 1); heterogeneity check + missing-core refusal vs. declared quorum (Review 2).
- **The Graded Ladder** — Jinja2 routing replaced with predeclared branch sheets gated by real `skip_when` commands (Review 1's exact prescription); challenge identity keyed on validation-id + artifact digest; conductor-state dependency flagged, buildable receipts-based counter shipped (Reviews 1, 2, 3).
- **Transfer of Command at the Seam** — briefing assembled and validated BEFORE the pause (Review 2); disposition as a separate acceptance event fired by the resume action (Reviews 1, 2); five per-section validations.
- **The Acknowledged False Alarm** — engine claim withdrawn; validation-scripts-read-list-file mechanism stated honestly with `validate_suppress` as destination; reason-linter replaced with mechanical five-field enactment including evidence pointer and expiry; expiry-re-arms-the-alarm control (Reviews 1, 2).
- **The Near-Miss Ledger** — demoted to aspirational with the observability dependency named (Review 2, seconded by Review 3's citation demand); buildable today-half (self-emitted events + next-run collector) shipped inside it.
- **The Serial Troponin** — state-carrier tier progression specified (Review 1); explicit escalate gate, monotone test ordering, no-reroll interval keying (Review 2); legal-transition recomputation gate added.
- **The Watch Rollover** — split from Rolling Continuity (Reviews 1, 2); atomic-rename single-writer ledger; append-only audit by diff; carry-ratio mechanics as a section with the deferred-promotion metric named (Review 2).
- **The Capability Census** — judgment fence resolved by deterministic classification with a bounded exceptions seat (Reviews 2, 3); fail-closed entry validation replacing skip_when admission (Review 2); probe-contract schema in the roster (Review 3).
- **The Fleet Receipt Ledger** — out-of-band non-waiting auditor replacing the depends_on-all terminal group that could never run on failure (Review 2 — the fatal wiring finding); machine-checkable receipt schema (Review 1).
- **The Non-Waiting Hand** — single-writer ledger, stable child ids as receipt filenames, lease/lost distinction in reconcile (Review 2's four strengthenings, all built).
- **Admission by First Cycle** — engine-authored receipts with recorded validation sets, freshness rule, fail-closed admission (Review 2); split from the cycle form.

## Proof-order overlap findings, adopted

All three reviews found the same imbalance from three angles: the proof estate over-proves fan-out/merge/jury/contract shapes (Review 1: four near-identical jury scores, five contract-first scores; Review 2: the cluster map; Review 3: the Apr/Jun/Sep/Oct batch history) and proves **none** of the orchestration primitives this pass's patterns depend on. The proof order below is the direct answer to Review 1's prescription ("direct the Prove track toward the untouched categories rather than authoring yet another multi-agent jury or contract-merge showcase") and Review 3's missing-element demand.

## Proof order (Review 3's missing sequence)

1. **Readback Before Commit** — smallest unproven primitive (`response_format`), highest newcomer value, four sheets. Proves the echo gate AND the instrument-support probe.
2. **The Fleet Receipt Ledger** — proves the out-of-band auditor path and the jq bijection; no exotic primitives; unarguable negative control.
3. **The Non-Waiting Hand** — proves non-waiting `concert` + `inherit_workspace` + spawn/receipt reconciliation (zero prior exercise).
4. **Immune Cascade priced variant** — extends an existing (currently broken-validation) proof rather than adding a new domain showcase; repairs debt #6 while proving the price table.
5. **The Serial Troponin** — first proof of native `sheet.loops` + `until` with a typed state carrier; designated composition proof (over #4) to answer the combined-YAML question.
6. **Capability Census → Admission by First Cycle** — first `fleet` proof; proves the fail-closed admission gate and (pending citation check) first-cycle semantics.
7. **Transfer of Command at the Seam** — first pause/escalate proof with the pre-pause briefing.
8. **The Graded Ladder** — typed routing across predeclared branches; proves the receipts-based challenge counter.
9. **Misclosure Ledger, One Field Many Cores, Poisoned-Artifact Advisory, Sealed Dissent, Negative Ledger, Acknowledged False Alarm, Watch Rollover** — no exotic primitives; each owed its two-fixture proof (generic + domain transfer, Review 2's class-level demand).
10. **Near-Miss Ledger** — blocked until Open Question #1(b) resolves.

**Newcomer path (Review 3's start-here demand):** Readback Before Commit → Fleet Receipt Ledger → Capability Census. All three load today with CLI gates and no unproven primitives beyond `response_format` (probed in step 1's own proof). Groups IV–VI's fleet/concert machinery is explicitly later-months territory; the INDEX's scale grouping already says so.

---

*Twenty-five draft patterns walked in; sixteen walk out with YAML and negative controls, nine are cut, folded, or split with their reasons cited, and every engine claim is either proven, flagged, or withdrawn. The corpus grows slower than the draft wanted — and its vocabulary grows faster, which is the point. Onward to the prove path.*

---

# The Complete Corpus Inventory (all passes, all runs)

This document is discover pass 1 / cycle 7's contribution. The full corpus is the union of every pass's survivors; nothing from earlier passes was dropped. Counts below are the post-pass state of the decomposed view.

## Holdings after this pass

- **Pattern files:** 127 (111 prior + 16 from this pass) across core, awaiting, and archive tiers
- **Laws (foundational):** 5 — The Etiquette Law, The Validity Window, The Freeze, Typed Force, The Write-Time Record (v6 core, unchanged; Validity Window gains two profiles this pass: failure-evidence aging, held-work pinning)
- **v6 core (17 counted entries):** unchanged in membership; five entries strengthened this pass — Immune Cascade (priced variant folded in), Delphi Convergence (Anonymous Rounds fold), Dead Letter Quarantine (Automatic Curriculum fold), Sign-Off Chain Against the Hard Date (Anthesis Window ripening face), Prefabrication (prevention-by-desk-design section)
- **This pass's core additions (16):** Readback Before Commit, The Poisoned-Artifact Advisory, The Sealed Dissent, The Negative Ledger, The Misclosure Ledger, One Field Many Cores, The Graded Ladder, Transfer of Command at the Seam, The Acknowledged False Alarm, The Near-Miss Ledger (aspirational), The Serial Troponin, The Watch Rollover, The Capability Census, The Fleet Receipt Ledger, The Non-Waiting Hand, Admission by First Cycle
- **Patterns Awaiting Primitives (prior):** Calling the Show, Relieving the Watch, The Strike Clock, Put-In, and others — unchanged
- **Candidates (this pass's demotions + prior backlog):** The Bounded Grep (first in proof order), The Readiness Cycle, The Commander's Budget (narrowed), The Watch Bill, Rolling Continuity, Stamp Before Steel, The Keystone Probe, The Intensifying Channel, The Sole-Source Confession, The Arbitrated Window, The Voted Blend, The Rostered Watch, The Dynamic Muster, The Checkpoint Re-Anchor, The Quota Shunt, The Uncorrupted Baseline
- **Archived with reasons recorded:** The ATO Cycle, Cluster Lead, and this pass's folds (Aged Lead, Held-State Clock, Graded Net, Automatic Curriculum, Anthesis Window, Anonymous Rounds, Wordless Manual — each folded into a named owner, reasons in Review Integration above)
- **Proof scores:** 18 on disk (17 historical + Barn Raising); six historical files carry known `mzt validate` failures (Open Question #6)
- **Prior monolith versions:** `rosetta-corpus-v6.md` (this directory) preserves the iteration-6 final verbatim; iterations 1–5 integration history is preserved in `review-integration.md`

## Where the authority lives

Selection is from the decomposed view: `patterns/*.md` (frontmatter: name, scale, status, forces, generators, problem, signals, stages, dependencies, composes_with), indexed by `INDEX.md`, mapped by `selection-guide.md`. This monolith is the narrative record and the review-integration evidence; where the two ever disagree, the decomposed files win and this document gets corrected.

*End of discover pass 1, cycle 7.*
# The Rosetta Pattern Corpus — Discover Pass 2, Cycle 7 (Final, post-review)

**Sheet 13 of 21 · 2026-10-26 · Disposition:** the draft's 24 patterns attacked by three reviews — The Practitioner (NEEDS REVISION), The Skeptic (FLAWED), The Newcomer (NEEDS REVISION) — and cut, folded, split, and strengthened accordingly. **21 patterns survive.** This document supersedes `04-draft-corpus.md` and is the permanent pass-2 corpus; the archive monolith (`archive/rosetta-corpus.md`) now carries it appended to the pass-1 corpus, and the decomposed view (`patterns/`, `INDEX.md`, `selection-guide.md`) is updated to match (pattern files 127 → 148).

**Proof-status vocabulary, corrected per the Skeptic:** "native-proven" in the draft collapsed five different states. This corpus splits it. Every pattern's proof status uses exactly one of:

- **primitives-proven** — every load-bearing primitive has an executed proof score somewhere in the estate; the pattern's own composition is still unexecuted.
- **approximation** — the pattern composes today on proven primitives, but one load-bearing behavior is unverified and is named on the pattern's face.
- **aspirational** — a load-bearing primitive is blocked or unwired; the pattern waits (see `awaiting.md`).

The draft's Pattern×Primitive table is re-issued below with proof-score cross-references (the Newcomer's fourth demand): which file, if any, exercises each primitive.

---

## Review Integration

What each review changed, pattern by pattern. Nothing here is cosmetic; every item is a structural edit to an entry, a cut, or a fold.

**Hard kills and conversions (consensus of at least two reviews):**

1. **Firing the Pass — EVICTED as a new discovery; recorded as a confirmation.** The Practitioner and the Newcomer both caught it on disk: `patterns/firing-the-pass.md` has existed since Sep 3, is indexed at `INDEX.md:159`, and carries a full proof score (`proof-scores/firing-the-pass.yaml`, "THE NIGHT DISPATCH," 191 KB, revised 2026-09-04 against three adversarial reviews). The draft violated its own Merge Policy rule 1. It is now recorded under Confirmations, below, with the Newcomer's additional finding: the existing proof never touched `stagger_delay_ms`, so the pattern's *clock half* (offset firing of heterogeneous durations) remains unproven even though the pattern itself is proven — the proof-order handoff inherits this as a named gap, not a new pattern.
2. **Staggered Quorum Spend — CUT to bench.** The Skeptic's arithmetic is unanswerable: a staggered fan-out still launches all N members, the engine cannot cancel not-yet-dispatched instances, and the tally depends on the fan-out and therefore waits for completion rather than releasing at k. Staggering delays completion; it saves zero spend. The Practitioner's redesign — sequential waves, launch k, quorum-check, launch N−k only on failure — is benched as **The Phased Quorum Wave** and re-enters when a prove sheet exercises a two-wave quorum gate.
3. **The Recovery Arc — CUT to bench.** The Practitioner: re-launching downstream stages from an intermediate mark requires unwired `checkpoint_persistence` and dynamic DAG re-entry; composing it today means hundreds of lines of `skip_when` across every downstream sheet. The Skeptic concurs ("an aspiration awaiting a supported restart primitive") and adds that `file_modified` proves a timestamp changed, not that correct re-entry occurred. Benched with the Newcomer's repair: it now names **The Checkpoint Re-Anchor** (pass-1 review candidate, `archive/rosetta-corpus.md:1316`) as its nearest prior candidate — the two should be re-derived together when the primitive lands. The marks doctrine (validated intermediate states, cheap sha256 marks) survives as composition guidance inside Serial Troponin and the Mock-Up Bay.
4. **The Shared Pulse — FOLDED into The Shared Reference with The Datum Grid.** The Newcomer's cut: ~70% isomorphic to the Datum Grid (small shared reference artifact + typed citations + straggler detection at fan-in), with the fold-refusal resting on a one-paragraph failure-semantics distinction. The fold forces each profile to pick one semantics, which dissolves the draft's internal contradiction (the draft's Core Dynamic quarantined cross-bar inputs while its Example merged them under their old bar — "a newcomer will implement whichever sentence they read second"). The Skeptic's complexity objection (O(N) claimed, then O(1)) is also settled: the reference is O(1) *per worker* in coordination edges, O(N) total — one edge per worker to the reference, zero worker-to-worker.
5. **Hotwash Dispatch & Spent Lesson Checkout — SPLIT into two patterns.** The Practitioner: "decouple this pairing" — dispatch belongs to within-score retry loops, checkout to persistent-agent memory maintenance; combined they are an uncomposable seven-stage monolith riding two unproven surfaces at once. The Skeptic: "dispatch, retirement, and recurrence escalation should be tested separately before being recombined." Each half is now independently provable, and each names its debt (`failure_history`, `sheet.loops`) on its own face. The Newcomer's neighbor debt is paid: both now name **After-Action Review** (permanent, `patterns/after-action-review.md`) as the capture-side neighbor — AAR owns reflection; Hotwash owns routing the evidence to a pre-committed consumer; Checkout owns supervised retirement.

**Hard rewrites (identity-preserving, mechanism-replacing):**

6. **The Cue Light — rewritten as a confirmation + extension of Standby–GO.** The Newcomer's finding: `patterns/standby-go.md` (permanent, Sep 3) is the same state machine — collective acknowledged arm, gate on complete ack set, missing ack holds, then fire. The draft laundered a confirmation into a first appearance. The entry now states inheritance and extension in two sentences each: inherited — arm/ack/hold/go with a deterministic complete-ack gate; new — (a) the monotone `cycle` freshness counter, (b) broadcast-polled semantics (a mode switch for already-running siblings) versus Standby–GO's addressed irreversible fire, (c) non-blocking consumers. The Practitioner's concurrency fix is structural: no shared mutable `acks[]` array (lost-update race); each consumer writes its own `acks/{consumer}.ack` file, and the protocol is three DAG stages — draft → go-gate → commit. The draft's regex/enum mismatch (`arm` in the schema, absent from the state regex) is fixed.
7. **The Contamination Wire — rewritten off the `failure_history` fallacy onto the native filesystem channel.** The Practitioner, with source knowledge: `failure_history` is sheet-local retry state; it does not broadcast from a gate sheet into downstream prompts. The Skeptic additionally exposed the draft's DAG self-contradiction: if the gate *fails*, consumers block on the failed dependency and never read anything; if the gate *succeeds*, there is no validation failure to carry. The rewrite resolves it: the gate's **typed verdict artifact** is the carrier. The gate succeeds and writes `verdicts/{artifact}.json` (PASS / CONTAMINATED with defect class and evidence digest); CONTAMINATED is a gate *output*, not a validation failure, so consumers dispatch. AI consumers receive the verdict path via `prelude` with a pre-registered routing table; deterministic consumers are *gated*, not warned — their commit wrapper's `skip_when` (polarity-correct: skip when the verdict says CONTAMINATED) refuses without interpreting anything. `failure_history` transport survives only as a flagged, unproven extension for the retry-local case.
8. **The Watchman's Gate — the polarity inversion FIXED.** The Skeptic's catch is the single most important correction of the pass: under Marianne semantics, `skip_when` *skips on command success*. The draft's predicate `test -f pick.json && grep -q GO pick.json` succeeds exactly when GO exists — so it would **skip authorized execution and proceed when the GO is missing** (and V1 says evaluation errors also proceed). The pattern survives because its own Placement Law was right and its example was wrong. The corrected refusal predicate: `skip_when: test ! -f pick.json || ! jq -e '.verdict == "GO"' pick.json` — absent or invalid GO makes the command succeed, the sheet refuses; a present GO makes it fail, the sheet proceeds; and the load-bearing check still lives in the watchman sheet's own fail-closed validation, with `skip_when` carrying only the consent echo, because V1 evaluation errors proceed. The Newcomer's typo fix (`instrument_fallbacks` → `per_sheet_fallbacks`) is applied. This polarity law is now stated once, corpus-wide, in Composition Doctrine.
9. **The Dispatch Catalogue (MEL) — the catalogue is an authoring-time static asset.** The Practitioner and the Skeptic converged from opposite sides: an LLM sheet generating `mel.yaml` as Stage 1 of the run it governs contradicts the pattern's own ex-ante authority story ("written when nobody is tired and nobody is scored on completing this run"). The catalogue is now a reviewed, versioned input authored with the score; the strong reasoner's judgment seat is discharged at *composition* time. The compensation stage is a pre-declared fixed roster with per-defect `skip_when` guards — no dynamic fan-out from `defects.jsonl`.
10. **The Midseason Pivot Ledger — reframed as concert-level.** The Practitioner: a running score cannot splice a new arc into its own DAG; pivot means generating the next movement's score file and launching it via the concert chain. The pattern now says so on its face and composes via concert chaining / self-chaining, with the Skeptic's demand that canon facts be enforceable predicates (digest-anchored, checker-computable), not prose. The emergency `on_fail → goto` form stays flagged native-unproven.

**Strengthened (kept, with the flagged repairs named in-entry):**

11. **Unison Drift** — deterministic vs probabilistic comparison modes (byte-digest marks for deterministic toolchains; normalized semantic marks — parsed-structure digests — for stochastic agents, with the mode declared per mark); the N=2/N=3 tie-break rule (N=2 proves drift exists but cannot say which replica is the odd one out; N=3 disambiguates by majority); quarantine downstream of first divergence via a polarity-correct consumer gate, not prose.
12. **The Dialectical Pair** — composed as an explicit unrolled static DAG (7 sheets: thesis/antithesis ×3 rounds + closer), not a span loop; the transcript is single-writer (each move is its own file `moves/{round}-{side}.json`; the join is computed by the closer, nothing appends concurrently); the sentinel runs on a hand-crafted fixture transcript, not a live debate (the Newcomer's flakiness catch — model behavior cannot be seeded deterministically).
13. **The Torque-Verify Pass** — invariant stated generically per the Skeptic: **total-domain cheap verification + producer-to-mark bijection**, complete coverage before any sampling. The "calibration negative" (same-family reviewer must miss an entailment flaw) is demoted from validation control to documented limitation — a control that depends on a correlated reviewer happening to miss is not a control. The Practitioner's endorsement of the structure stands.
14. **The Priced Verification Ladder** — the Practitioner's missing mechanism supplied: an explicit CLI ledger-update step between tiers computes estimated spend from output token counts / character lengths and appends to `budget-ledger.jsonl` *before* the tier-3 `skip_when` evaluates. Risk class comes from a composer-authored class map, not producer self-classification (the Skeptic's capture objection). Status: **approximation** — the sentinel pair (fat budget ⇒ zero degradation receipts; thin budget ⇒ receipts present) is specified but unexecuted; until then the descent behavior is doctrine, not fact.
15. **Dispatch with Declared Penalty** — the penalty algebra the Skeptic demanded: penalties are declared in named units (`coverage_pct`, `confidence_delta`, `cost_usd`); each margin declares its combination law (sum for additive units, max for latencies, product for probabilities); correlated deviations must be declared co-priced (two deviations from one vendor share a correlation entry, else the sum double-discounts); margins are owned by the composer's `margins.yaml`, never writable by the run.
16. **The Hold-Point Witness** — a notify step in `prepare-hold` (the Practitioner: "a hold point nobody notices is a deadlock wearing a safety vest"); the trust model stated (the Newcomer: say once, centrally, that roster + digest binding is authority-by-file-permission — see Composition Doctrine); stale-disposition handling (the Skeptic): the disposition carries a timestamp and binds the pause event id; a disposition older than the current pause or naming a different pause is rejected by resume-check.
17. **The Editor's Disposition** — one closed route proven first: `accept` and `reject` route deterministically today; the `minor` loop and `major` return-to-advise routes are marked **awaiting `sheet.loops` proof** rather than invented control flow (the Skeptic). Remains the endorsed minimal exercise of `response_format`.
18. **The Mock-Up Bay** — reduced to the minimal loop proof first (the Skeptic: drop the post-loop production fan-out from the first proof; the Practitioner wanted concrete syntax — supplied in Composition Doctrine): rubric-press → build → inspect → refine, three rounds max, `until` over verdict-file facts. The production fan-out is composition, not proof burden.
19. **Keystone-First Sequencing** — kept over the Skeptic's fold objection (the Practitioner listed it among the six strongest; two reviews to one). The differentiation the Skeptic demanded is now in-entry: Cathedral Construction owns iterative construction toward a known target; Prefabrication owns interface contracts between producers; Keystone-First owns *ordering by leverage* — which artifact's output parameterizes the most downstream prompts — and that selection rule applies to scores with no iteration and no contracts. Where they overlap, keystone-first is the decision rule for what Cathedral/Prefabrication build first.
20. **Facilitator-First Decomposition** — the release-receipt gate polarity fixed (the Skeptic caught the same fail-open error as Watchman's Gate: absence of the receipt must *skip*, so the predicate succeeds on absence); edge classification is enforced at validation (an unclassified edge fails), with the honest limitation that labels constrain gating and injection, not runtime semantics.
21. **The Inspection and Redline Stakes** — the Skeptic's race fixed: `tolerance.yaml` declares a **readiness deadline**; the admit sheet is bounded by it (`max_wall_seconds`), and absence is not legible as PARTIAL until the deadline passes — missing-vs-not-yet becomes a typed transition with a timestamp. Differentiation from MEL/CDL stated: MEL answers *may we run degraded* (ex-ante authorization to dispatch), CDL answers *can the margins absorb the sum* (economics); the Stakes answer *what may downstream consume* (partial admission across a fleet boundary). Three different questions, three different table owners.
22. **The Continuous Pour Schedule** — joint receipts have a single named writer (the Skeptic: "last-completing sheet" is not an owner): each wave ends in a `wave-N-joint` CLI sheet that writes the receipt after the wave's members complete — the DAG supplies the serialization. The alias-derived rate-limit claim is cut (the Skeptic: a score cannot derive vendor limits from an alias declaration); documented limits are an authoring-time input to `pour-plan`. The V4-corrected stagger doctrine (per-instrument spacing) stands.

**Newcomer onboarding debt, paid corpus-wide:** a selection table ("what breaks if this is absent"), a glossary bridge (C1–C10 and D1 expanded at first use; `glossary.md` linked), a reconciliation appendix mapping all 24 draft entries to their dispositions and permanent-corpus neighbors, proof-score cross-references in the primitive table, and a designated newcomer's first score (the Mock-Up Bay minimal loop — five sheets, one unproven primitive, the corpus's designated `sheet.loops` proof).

---

## Engine Evidence (V1–V6, corpus property)

| # | Claim | Verdict | Citation |
|---|---|---|---|
| V1 | `skip_when` fails open on timeout/spawn/substitution error | **CONFIRMED** | `skip.py:13-19` → PROCEED |
| V2 | Conductor exports retry counts as score-readable data | **CONFIRMED with sharp edge** — attempt context is prompt-visible, not queryable; carrier is a receipt file via `on_fail: run`. Citation debt: the pass-1 carrier claim cited "conductor export surface" with no file:line; the prove path must pin it | file:line owed to the prove path |
| V3 | `fleet.depends_on` gates on first cycle, not full completion | **REFUTED** — it waits on full successful completion | `fleet.py:337-360` |
| V4 | `stagger_delay_ms` staggers fan-out dispatches | **DELTA** — it is a *same-instrument* spacing rule | `dispatch.py:65-66` |
| V5 | `response_format` structured output captured and validated per-sheet | **CONFIRMED** (schema-validated per attempt; zero end-to-end proof executions corpus-wide) | validation engine |
| V6 | `sheet.loops` `until` evaluates over sheet states, variables, file facts | **CONFIRMED, with grammar limits** — a broken predicate kills the span E999 (fail-closed) | `baton/flow.py:368-376` |

The dual, now with its third leg: **consent channels fail open (`skip_when`), expression channels fail closed (`until`), and `skip_when` skips on success** — every gate predicate must be written as a *refusal* predicate on a channel whose failure direction the check can survive. The Watchman's Gate entry is the worked example.

---

## Convergence Findings (C1–C10, D1) — glossary bridge

The collision's cross-expedition findings, expanded at first use per the Newcomer's demand. Full discussion: `03-the-collision.md`; corpus glossary: `glossary.md`.

- **C1 — Ex-ante authorization:** the rule is written before the data arrives (MEL rows, tolerance stakes, pre-registered rubrics).
- **C2 — Closed vocabularies, deterministically checked:** smallness as safety mechanism; an item with no row is undispatchable.
- **C3 — Independence as instrument-family separation:** same-family assignment is a correlated-failure bug (the Independence Law).
- **C5 — Receipted degradation:** a logged degradation is a risk consciously accepted; a silent skip is a lie the ledger will eventually bill.
- **C8 — The typed stalemate:** honest non-resolution is a first-class terminal with preserved evidence (TEYKU, `verdict: inconclusive`, PARTIAL/HALT).
- **C10 — The placement law:** fail-closed checks get a sheet; fail-open channels carry consent only.
- **D1 — Fan-in under a physical clock:** only domains with irreversible material time produce fan-in under a clock (kitchen pass, mass concrete); its score-form half is unproven (the Firing the Pass proof never touched `stagger_delay_ms`).

## Composition Doctrine (corpus-level, from all three reviews)

1. **The skip_when polarity law.** `skip_when` skips when its command *succeeds*. Permission predicates invert the gate (Watchman's Gate, the draft's version, would have skipped authorized executions). Always write the refusal: the command succeeds when the artifact is *absent*, *stale*, or *poisoned* — so refusal is the skip. And because V1 evaluation errors proceed, no load-bearing check may live only in `skip_when`; it lives in a gate sheet's own fail-closed validation, and `skip_when` carries the consent echo.
2. **Concurrency ownership.** No shared mutable artifact without exactly one writer. Parallel workers write per-worker files (`acks/{consumer}.ack`, `outputs/{sheet_id}/…`, `moves/{round}-{side}.json`); any aggregation happens in a single later CLI sheet whose DAG position serializes it. Multi-line file mutation is write-temp-then-rename (`mv`), never in-place append by concurrent processes.
3. **Scope-check determinism.** A sheet's "files touched" is only knowable if each sheet writes an isolated output directory (`outputs/{sheet_id}/`); scope validations assert over that directory, never over the whole workspace (which concurrent sheets are also writing).
4. **CLI instrument environment.** Deterministic gates assume `jq`, `sha256sum`, `grep`, `test` on PATH; custom scripts live in `{score_dir}/scripts/` and are named per pattern; `per_sheet_fallbacks: []` on every gate (the No-Inheritance Gate).
5. **Intermediate gate failure wiring.** A verification gate that must not terminate the score on a contaminated input *succeeds* and writes a typed verdict artifact (PASS / CONTAMINATED); contamination is data on the happy path, not a validation exit. Hard failures (gate cannot evaluate) use `on_fail: escalate`, never silent continue.
6. **Loops syntax (the Practitioner's missing snippet), for the Mock-Up Bay proof and every consumer:**

```yaml
sheet:
  loops:
    "2-4":
      count: 3
      until: 'file("{workspace}/verdict.json").json.status == "pass"'
      index: "mockup_round"
      cost_limit_usd: 5.0
```

The `until` expression is evaluated over sheet states, variables, and file facts (V6); a predicate that fails to parse or evaluate kills the span E999 — fail-closed — so the verdict-file schema is load-bearing validation, not decoration.

---

# GROUP I — COMMUNICATION

---

## The Cue Light

```yaml
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
---
```

**Status:** working · primitives-proven (pattern-unproven). **Inheritance (the Newcomer's finding, now on the face):** this pattern is a **confirmation + extension of Standby–GO** (`patterns/standby-go.md`, permanent since Sep 3). Inherited: collective acknowledged arm; deterministic complete-ack gate; missing ack holds the cue; then fire. Extended: (1) the monotone `cycle` counter — the freshness fact, so a consumer can never act on a stale light; (2) broadcast-polled semantics — the light changes what *already-running siblings* do, versus Standby–GO's addressed irreversible fire; (3) non-blocking consumers — work proceeds under standby; only commits wait.

**Core Dynamic.** One bit, broadcast, polled — a schema so small it cannot be misread, and an ack set so structured it cannot be forged by prose. The publisher writes `{workspace}/cue/{name}.yaml` with `state ∈ {arm, standby, go, clear}`, `cue_id`, and `cycle`. Consumers ack by writing their **own file** (`acks/{consumer}.ack`, containing sheet id + cycle observed) — never by appending to a shared array, which is a lost-update race under concurrent writers (the Practitioner's structural fix). The go-gate is a CLI sheet whose *validation* is the ack-completeness count: a cue with a missing ack stays `standby` and the gate exits nonzero — the GO must not fire on an incomplete ack set.

**Marianne Score Structure.** Four stages as in frontmatter. The go flip is atomic: write `cue.next.yaml`, then `mv` over the current file (write-temp-then-rename — the concurrency doctrine). Consumers do **not** poll inside a running sheet (a sheet is a discrete execution unit; an in-sheet poll burns timeout budget — the Practitioner's catch): the protocol is draft-stage consumers that finish, ack, and exit; commit-stage wrappers whose `skip_when` is a refusal predicate (`skip_when: 'jq -e ''.state == "standby" or .state == "clear"'' {workspace}/cue/{name}.yaml'` — skip while not GO; V1-fail-open is survivable because the gate already refused loudly). Validations: `content_regex` on the state field `^(arm|standby|go|clear)$` (the draft's regex omitted `arm` — fixed, the Newcomer's catch); `command_succeeds` on the go-gate's ack count. **Sentinel:** a cue whose consumer never acks must leave `state: standby`, the consumer absent from `acks/`, and the go-gate exiting nonzero — no GO ever written.

**Example.** Product-launch pipeline: 8 sheets produce materials concurrently; legal sign-off is the cue. Materials finish, write their ack files, hold publication; legal's approval lands; the go-gate verifies all 8 acks and flips GO; all 8 commit within their own cadence — the launch waits for legal, legal waits for no one.

---

## The Contamination Wire

```yaml
---
name: "The Contamination Wire"
scale: communication
status: working
forces: [Information Asymmetry, Partial Failure, Exponential Defect Cost]
generators: [Exploit Failure as Signal]
problem: "A warning cannot travel backward to consumers who already ran, so contamination evidence must travel forward on the channel every future consumer already reads."
signals:
  - "a multi-consumer artifact fails validation after some consumers have built on it"
  - "one consumer's validation failure is evidence about the artifact, not just about the consumer"
  - "rerouting or halting must remain possible — alternate sources or degraded modes exist"
stages:
  - name: produce
    sheets: fan_out(N)
    instrument_guidance: "work instruments; each writes artifacts/{producer}.json"
    fallback_friendly: true
    purpose: "Produce the fan-out artifacts that will be gated."
  - name: gate
    sheets: 1
    instrument_guidance: "any-wrapped CLI, per_sheet_fallbacks: [] — verification-only; SUCCEEDS and writes typed verdicts, one per artifact"
    fallback_friendly: false
    purpose: "Emit verdicts/{artifact}.json (PASS or CONTAMINATED + defect class + evidence digest). Contamination is gate output, not validation failure."
  - name: consume
    sheets: fan_out(M)
    instrument_guidance: "AI consumers receive the verdict path via prelude and apply a pre-registered routing table; deterministic consumers' commit wrappers carry a refusal skip_when on their input's verdict"
    fallback_friendly: true
    purpose: "Consume clean inputs; reroute or halt-with-receipt on contaminated ones."
dependencies:
  gate: [produce]
  consume: [gate]
composes_with:
  - pattern: "Dead Letter Quarantine"
    how: "division of labor — DLQ owns the item, the wire owns the warning; compose, never merge"
  - pattern: "The Validity Window"
    how: "a verdict older than the window is stale contamination"
  - pattern: "Readback Before Commit"
    how: "the typed verdict is the readback whose absence started this pattern"
  - pattern: "The Cue Light"
    how: "a poison verdict is a one-bit cue for deterministic consumers"
---
```

**Status:** working · primitives-proven (rewritten post-review). **The rewrite (the Practitioner's hard kill and the Skeptic's DAG catch):** the draft carried the warning on `failure_history`, which is sheet-local retry state — it does not broadcast from a gate into downstream prompts. And the draft's DAG was self-defeating: a *failing* gate blocks its dependents; a *succeeding* gate has no validation failure to carry. The resolution: **the gate never fails on contamination.** It succeeds and writes a typed verdict per artifact; CONTAMINATED is data on the happy path, so consumers dispatch and read it.

**Core Dynamic.** The warning travels forward on the channel every future consumer already reads — the workspace file tree — and the *consumer*, not the sender, holds routing authority. AI consumers get the verdict path via `prelude` and apply a pre-registered routing table (`IF verdict for input X is CONTAMINATED with code C → emit refusal.json and consume alternate source Y`). Deterministic (CLI) consumers cannot interpret prompts by construction — they are **gated, not warned**: their commit wrapper's `skip_when` succeeds (skips) when the input's verdict says CONTAMINATED, refusing without interpreting anything. Refusals land in `refusals/{consumer}.json` naming artifact, code, chosen alternate. Dual fingerprints: mycorrhizal defense signaling (Barto et al., PMC4497361) and hazmat placarding on the ICS routing channel — the collision's strongest cross-kingdom co-derivation (C6).

**Marianne Score Structure.** Three stages as in frontmatter; produce → gate → consume is load-bearing (the verification-only-stage discipline). Validations: `content_regex` on each AI consumer's output requiring it to cite its input's verdict path or emit the refusal artifact — the third state (built on ungated input, silently) is what the regex kills. **Sentinel:** a seeded artifact planted with a known defect must produce `refusals/consumer-3.json`; `test -f` exits 1 if absent — the run FAILS if the consumer built on poison. **Inverse control:** a clean run shows no refusals (the warning doesn't fire on silence). **Flagged extension, not core:** `failure_history` transport for the *retry-local* case (same sheet re-attempting) is unproven and named on the pattern's face; the Severity Gate, Computed Signature, and Fighting the Last War (benched) queue behind its proof.

**Example.** Due-diligence concert: a fetch sheet pulls filings; three analysts build on it; the gate validates completeness mid-run and writes CONTAMINATED (code V012) on the partial artifact. The analysts see the verdict at consume time; two reroute to the cached prior-quarter filing and say so in their refusals; one halts with a receipt. No rewinding, no silent stale analysis.

---

## The Shared Reference (Datum Grid ⊕ Shared Pulse, folded)

```yaml
---
name: "The Shared Reference"
scale: communication
status: working
forces: [Information Asymmetry, Producer-Consumer Mismatch]
generators: [Contract at Interfaces]
problem: "N independent workers must agree on terms without converging on content, and pairwise coordination is O(N²) chatter."
signals:
  - "wide fan-outs whose outputs must agree on terminology, schema, or phase without agreeing on content"
  - "stragglers from an earlier regime would otherwise merge silently with current-regime work"
  - "mixed instruments need cheap interoperability across a fan-out"
stages:
  - name: establish
    sheets: 1
    instrument_guidance: "strong reasoner — builds the minimal shared reference (glossary, schema set, phase descriptor)"
    fallback_friendly: true
    purpose: "Write reference.yaml (profile: datum) or pulse.v{k}.yaml (profile: pulse) plus its sha256."
  - name: verify-reference
    sheets: 1
    instrument_guidance: "any-wrapped CLI, per_sheet_fallbacks: [] — schema check, closed-traverse consistency, digest pin"
    fallback_friendly: false
    purpose: "Verify the reference before anyone works from it; a separate sheet because the check must not live in skip_when (V1)."
  - name: work
    sheets: fan_out(N)
    instrument_guidance: "any instruments per the work; outputs cite reference entry IDs and the version/bar they performed against"
    fallback_friendly: true
    purpose: "Ornament the reference; never re-derive it."
  - name: merge
    sheets: 1
    instrument_guidance: "any-wrapped CLI — checks every input's cited version/bar before reconciling"
    fallback_friendly: false
    purpose: "Admit current-regime work; quarantine stragglers as data, never merge them."
dependencies:
  verify-reference: [establish]
  work: [verify-reference]
  merge: [work]
composes_with:
  - pattern: "The Misclosure Ledger"
    how: "closure arithmetic vs the shared reference that makes closure cheap"
  - pattern: "Serial Troponin"
    how: "the bar counter is the serial test transposed from time to space-of-work"
  - pattern: "Prefabrication"
    how: "the reference is the contract-first fan-out's shared contract page"
  - pattern: "Delphi Convergence"
    how: "the pulse is Delphi's missing metronome — which round are we in"
---
```

**Status:** working · primitives-proven. **The fold (the Newcomer's cut):** the draft carried Datum Grid and Shared Pulse as fold-refused siblings at ~70% isomorphism — small shared reference artifact, typed citations, straggler detection at fan-in — with the entire refusal resting on one paragraph of failure semantics. Folded, each profile must pick exactly one semantics, which dissolves the draft's merge/quarantine contradiction (the draft's Core Dynamic quarantined cross-bar inputs while its Example merged them "under their old bar"; a newcomer implements whichever sentence they read second).

**Core Dynamic.** Everyone syncs to a shared reference instead of pairwise to each other: one edge per worker to the reference, zero worker-to-worker — O(1) per worker, O(N) total, never O(N²) chatter. The reference is cheaper and slower than the parts, which is exactly what makes high-rate local work safe. Two profiles with **different failure semantics — choose one per score, never both in one artifact**:

- **Datum (immutable):** pre-verified, digest-pinned, never mutated. Workers cite entries by ID; a worker that re-derives instead of citing is drift, caught cheaply. Swap the datum without re-pinning and all N workers fail loudly at launch — which is the point: tampering must be loud.
- **Pulse (monotone-versioned):** a stable, low-update-rate position artifact (`section`, monotone `bar`, decisions-of-record IDs, `version`), updated only at section boundaries, by its single owner (a CLI pulse-keeper with `per_sheet_fallbacks: []`). The clave change — a rare, typed, versioned rewrite — re-keys all downstream interpretation at once. New version = new file (`pulse.v2.yaml`); the old file persists, so in-flight stragglers are *admitted under their cited version and flagged for re-derivation* (merge-as-flagged), while inputs citing a version that never existed or a corrupted current file are *quarantined* (never merged). This is the profile split the fold forced, stated as typed transitions with timestamps — no ambiguity survives.

**Marianne Score Structure.** Four stages as in frontmatter. Datum profile: workers' first validation is a digest check against the pinned reference, outputs cite ≥1 datum entry ID (`content_regex`), merge runs a normalization-diff (jq) against cited entries. Pulse profile: `field_match` of each ornament's cited `bar`/`version` against the pulse; monotonicity check on `bar`. **Sentinels:** datum — swap `reference.yaml` without re-pinning → all N workers' digest checks fail, N failure receipts; pulse — inject an ornament citing a nonexistent version → quarantined as straggler data with a row in `stragglers.csv`, other inputs still merge, exit code reflects quarantine, not crash.

**Example.** 12-language localization fan-out (datum): the locked terminology glossary is the reference; 12 workers on 12 instrument profiles never exchange a message and still agree on every term; a swapped glossary fails all 12 at once, visibly. Quarter-long compliance-audit concert (pulse): the pulse holds the current regulation-snapshot id and phase; mid-quarter the snapshot is re-versioned; in-flight ornaments merge under their cited old version and are flagged for re-derivation instead of silently mixing regimes.

---

## The Change-Order Ledger

```yaml
---
name: "The Change-Order Ledger"
scale: communication
status: working
forces: [Information Asymmetry, Progressive Commitment, Typed Force]
generators: [Contract at Interfaces]
problem: "Mid-run plan mutations are reconstructible only by diffing prompts, so no sheet can know what it was authorized to do."
signals:
  - "cadenza injections, escalation dispositions, or redlines change scope mid-run"
  - "sheets run under a version of the plan that no longer exists"
  - "'the plan changed mid-run' has ever been answered by archaeology"
stages:
  - name: baseline
    sheets: 1
    instrument_guidance: "mid-tier or CLI — transcribes declared config into ledger.jsonl's opening entry (authorized scope, tolerances, datum digest)"
    fallback_friendly: true
    purpose: "Exhibit A: the authorized state at launch."
  - name: work
    sheets: fan_out(N)
    instrument_guidance: "work instruments; each writes ONLY into outputs/{sheet_id}/ — isolation is what makes the scope check deterministic"
    fallback_friendly: true
    purpose: "Do authorized work; per-sheet outputs are attributable by construction."
  - name: scope-check
    sheets: 1
    instrument_guidance: "any-wrapped CLI, per_sheet_fallbacks: [] — per completed sheet: every file under outputs/{sheet_id}/ ⊆ authorized-set under the latest entry whose effective_from precedes that sheet's recorded start"
    fallback_friendly: false
    purpose: "Deterministic scope enforcement; exits 1 naming the unauthorized path."
  - name: append
    sheets: 1
    instrument_guidance: "CLI, per_sheet_fallbacks: [] — appends change orders {id, authority, effective_from, before/after digests, reason}; digest-chained (prev_entry_sha256)"
    fallback_friendly: false
    purpose: "The only writer to the ledger; authority is authorship-time configuration, never interpreted at runtime."
dependencies:
  work: [baseline]
  scope-check: [work]
composes_with:
  - pattern: "The Negative Ledger"
    how: "duals — the Negative Ledger owns refusals, this owns authorizations"
  - pattern: "Configuration Control Board"
    how: "the ledger is the CCB's runtime enforcement face"
  - pattern: "Commander's-Intent Envelope"
    how: "intent envelopes the run; change orders are its authorized deltas"
  - pattern: "The Midseason Pivot Ledger"
    how: "nearest kin, fold-refused — the change order executes an authorized delta, the pivot executes an interpretation under canon constraints; distinct data model and checker"
---
```

**Status:** working · primitives-proven. **Repairs applied:** the Practitioner's two catches are structural. First, "files touched by a specific sheet" is unknowable in a shared workspace — so each work sheet writes an isolated `outputs/{sheet_id}/` directory and the scope check asserts over that directory alone (never `git status` over a workspace concurrent sheets are also writing). Second, "run-trigger side effects" that "deterministically append" authority were hand-waving: the ledger has exactly one writer stage, and *authority is authorship-time configuration* — an append records a disposition already made by a configured authority (a cadenza directive, a hold-point signature); the append itself never grants authority. Chain-walk integrity (jq + sha256, exit 1 on any break) is checkable by any consumer via ordinary file facts.

**Core Dynamic.** The architect's napkin sketch is not a change order. A change order is a typed, priced, signed instrument naming the scope delta, the authority that ordered it, and an `effective_from` boundary — written *before* downstream sheets consume the change. A sheet executing behavior not covered by the current ledger state is out of scope, full stop. The ledger is for changes that alter *what work is authorized* (scope, tolerance, datum version, target set) — not observations; scope it or drown in it.

**Sentinels.** A: a sheet writing a file authorized only under a *future* `effective_from` fails, naming the file and the not-yet-effective entry id. B: delete a mid-sequence entry → the chain walk breaks at the gap, exits 1 naming the orphan.

**Example.** Data-pipeline remediation score: mid-run, a cadenza narrows the authorized table set after a privacy finding; the change order (authority: the composer, effective_from: sheet 14) means sheet 17's touch of a now-unauthorized table fails its scope check loudly — instead of quietly doing what it was told three days ago by a version of the plan that no longer exists.

---

# GROUP II — WITHIN-STAGE

---

## Unison Drift

```yaml
---
name: "Unison Drift"
scale: within-stage
status: working
forces: [Structured Disagreement, Exponential Defect Cost]
generators: [Verify through Diverse Observers]
problem: "Replicas that should be identical diverge silently, and the divergence point — the actual defect location — is never localized."
signals:
  - "an expensive fan-out is about to be spent on an untested prompt+toolchain"
  - "instrument or vendor swaps may have changed behavior invisibly"
  - "reproducibility of the pipeline is assumed but never measured"
stages:
  - name: mark-plan
    sheets: 1
    instrument_guidance: "any-wrapped CLI — declares rehearsal marks (per-stage output digests expected identical across replicas) and the comparison mode per mark"
    fallback_friendly: false
    purpose: "Define where divergence will be measured and how (byte-digest or normalized-semantic)."
  - name: replicas
    sheets: fan_out(N)
    instrument_guidance: "IDENTICAL instrument, profile, prompt, and seed across replicas — that is the experiment; 2 proves drift exists, 3 names the odd one out"
    fallback_friendly: true
    purpose: "Run the same sequence N times; write per-mark digest artifacts."
  - name: differ
    sheets: 1
    instrument_guidance: "any-wrapped CLI, per_sheet_fallbacks: [] — sha256sum + comm over mark digests; writes drift-ledger.csv (mark, replicas-in-agreement, first-divergent-pair)"
    fallback_friendly: false
    purpose: "Localize the first divergent mark; quarantine everything downstream of it."
dependencies:
  differ: [replicas]
composes_with:
  - pattern: "Rashomon Gate"
    how: "the routing rule this entry adds — unison → drift-diff; Rashomon → compare"
  - pattern: "Readback Before Commit"
    how: "typed echoes make marks comparable; prose marks cannot be diffed"
  - pattern: "The Independence Law"
    how: "the one place instruments must NOT differ — the negative image of family separation"
---
```

**Status:** working · primitives-proven — **the first proof of the pass** (fan-out, `capture_files`, `file_sha256`, CLI differ; zero blocked machinery; ranked #1 by the collision and #1 or top-tier in all three reviews).

**Core Dynamic.** Run replicas that *should* be identical and let them diverge naturally; the divergence is not noise, it is a **measurement**. Where Rashomon Gate fans out expecting disagreement (different lenses, compare conclusions), Unison Drift fans out expecting *identity* — so the first divergence point localizes the fault with cycle-resolution: a nondeterministic tool at step k, an underspecified prompt clause two readers take differently, a dependency that resolved to different versions. Brown's additive law is the localization mechanism: the loop grows one element per cycle, so any divergence is arithmetically locatable to the cycle it entered.

**Repairs applied (the Skeptic's three):** (1) *Deterministic vs probabilistic modes, declared per mark.* "Identical instrument and profile" does not imply byte identity for stochastic agents. Deterministic toolchains compare raw `file_sha256` at each mark; probabilistic agents compare **normalized semantic marks** — digests over parsed structure (the AST, the extracted-term set, the normalized JSON) with temperature and sampling declared — and a mark that cannot be normalized is marked `localization: coarse` on the plan. (2) *The N=2/N=3 tie-break rule (the Newcomer's demand):* N=2 proves drift exists but cannot say which replica is the odd one out — there is no majority; N=3 disambiguates by majority vote. State which question you are asking before choosing N. (3) *Quarantine is a gate, not prose:* the consumer gate's `skip_when` succeeds (skips) on any input downstream of the ledger's first-divergent mark — polarity-correct refusal, checkable.

**Sentinel.** Perturb replica 2 (a seeded stochastic tool where replicas 1 and 3 pin a fixed seed) → the ledger's `first-divergent-mark` equals the seeded tool's stage, and downstream-of-mark outputs are refused by the consumer gate. If the ledger blames an earlier mark, the differ is wrong and the proof fails.

**Example.** Before a 12-instance documentation-translation fan-out, run 3 replicas through the prompt+toolchain once each; the ledger shows first divergence at the terminology-extraction mark — "extract key terms" is underspecified. Fix the clause, rerun, divergence gone, *then* spend on 12.

---

## The Dialectical Pair

```yaml
---
name: "The Dialectical Pair"
scale: within-stage
status: approximation
forces: [Structured Disagreement, Convergence Imperative]
generators: [Frame Multiplication]
problem: "Two-agent debate collapses into position-holding by silence unless engagement is mechanically checkable and the stalemate is a typed terminal."
signals:
  - "risk concentrates in one contested judgment where a single reviewer's blind spot is the danger"
  - "a full jury is overkill but one voice is not enough"
  - "unstructured debate has ended in 'we agree to disagree' with no record of what was contested"
stages:
  - name: thesis-r1
    sheets: 1
    instrument_guidance: "strong reasoner, family A — opens with typed CLAIMs, one per file moves/r1-a.json"
    fallback_friendly: true
    purpose: "State the thesis in checkable parts."
  - name: antithesis-r1
    sheets: 1
    instrument_guidance: "strong reasoner, family B (Independence Law) — OBJECTION or CONCESSION per claim, one per file moves/r1-b.json"
    fallback_friendly: true
    purpose: "Engage every claim; silence is illegal."
  - name: thesis-r2 / antithesis-r2 / thesis-r3 / antithesis-r3
    sheets: 1 each
    instrument_guidance: "alternating, strict dependency order — ANSWER/COUNTER must cite the objection's move id"
    fallback_friendly: true
    purpose: "Bounded exchange; max 3 rounds is structural, not tunable."
  - name: close
    sheets: 1
    instrument_guidance: "any-wrapped CLI, per_sheet_fallbacks: [] — computes the engagement join over moves/*, emits the typed terminal"
    fallback_friendly: false
    purpose: "RESOLVED-for-A / RESOLVED-for-B / TEYKU with open objections preserved."
dependencies:
  antithesis-r1: [thesis-r1]
  thesis-r2: [antithesis-r1]
  close: [antithesis-r3]
composes_with:
  - pattern: "Rejoinder Ledger"
    how: "its bijection applied mid-debate rather than post-review"
  - pattern: "Rashomon Gate"
    how: "the pair is the binary case with engagement rules Rashomon lacks"
  - pattern: "The Editor's Disposition"
    how: "a TEYKU is the strongest possible advisory input — a typed stalemate with a transcript"
  - pattern: "The Sealed Dissent"
    how: "the non-engaging sibling"
---
```

**Status:** approximation — typed moves via `response_format` are native-unproven (V5 schema-validated per attempt, zero end-to-end executions; this and the Editor's Disposition are the tied minimal exercises). **Repair applied (the Practitioner's):** the pattern is now explicitly an **unrolled static DAG of 7 sheets** — not a span loop; alternating two instrument families inside one looped block is Jinja gymnastics nobody should attempt, and the pattern says so.

**Core Dynamic.** Two agents, opposite theses, one artifact, a **closed move vocabulary**: CLAIM, OBJECTION (must cite the claim span), ANSWER (must cite the objection), CONCESSION (withdraw, recorded), COUNTER. Every OBJECTION must receive ANSWER, CONCESSION, or COUNTER before the round ends — *silence is illegal*, and because moves are typed artifacts, engagement is mechanically checkable: the closer computes a join (the Rejoinder Ledger's bijection mid-debate). The typed terminal **TEYKU** — the admitted draw, recorded with open objections — is a first-class outcome 1,500 years old that the corpus's success/fail vocabulary lacked (C8, the Typed-Draw Law). More than ~2.5 viable positions means a pair compresses a 4-way question into false binarity — promote to Rashomon. Empirical questions are not debated; the Etiquette Law runs the test.

**Concurrency repair (the Skeptic's):** no shared append-only transcript — each move is its **own file** (`moves/{round}-{side}.json`), written by exactly one sheet in strict dependency order; the DAG supplies the serialization; the join is computed by the closer over the directory. **Sentinel repair (the Newcomer's):** the sentinel runs on a **hand-crafted fixture transcript** — a `moves/` directory with a deliberate orphan claim — never on a live debate; model behavior cannot be seeded deterministically, and a live-behavior sentinel would be flaky on arrival. `moves-lint.py` exits 1 with `{"orphan_claims": ["c-3"], "rule": "every claim must be engaged"}` — catching position-holding-by-silence, which unstructured debate lets pass.

**Example.** Security-severity debate: A argues "critical, exploitable pre-auth," B argues "low, requires local access." Three rounds of typed moves; two claims survive all objections, one stands contested → TEYKU recorded with the contested claim exposed. The CVE triage proceeds on resolved claims; the contested one goes to a human with the transcript.

---

## The Torque-Verify Pass

```yaml
---
name: "The Torque-Verify Pass"
scale: within-stage
status: working
forces: [Exponential Defect Cost, Instrument-Task Fit]
generators: [Match Instrument to Grain]
problem: "Schema-valid garbage propagates silently because schemas cannot express the semantic invariants (arithmetic, entailment, domain constraints) that make output true."
signals:
  - "structured-output producers at volume where a wrong number looks exactly like a right one"
  - "a sampled deep check over a systematically mis-generated population is confident nonsense"
  - "cheap complete coverage is possible but unclaimed"
stages:
  - name: produce
    sheets: fan_out(N)
    instrument_guidance: "work instruments; response_format: json_schema per unit (V5 engine gate)"
    fallback_friendly: true
    purpose: "Produce typed units whose schema the engine itself validates."
  - name: torque-verify
    sheets: fan_out(N)
    instrument_guidance: "cheap, fast, DIFFERENT instrument family (local ollama or pure CLI — for deterministic invariants CLI IS the second wrench); width 1:1 with produce units, one declared invariant set per unit"
    fallback_friendly: true
    purpose: "Re-check the semantic invariants schemas cannot express; write marks/{unit}.json (unit id, checks run, pass/fail)."
  - name: walk-the-steel
    sheets: 1
    instrument_guidance: "any-wrapped CLI, per_sheet_fallbacks: [] — audit: every produced unit has a mark, every mark passes, marks count = units count"
    fallback_friendly: false
    purpose: "Enforce the bijection; unmarked units are audit failures by definition."
dependencies:
  torque-verify: [produce]
  walk-the-steel: [torque-verify]
composes_with:
  - pattern: "Immune Cascade"
    how: "owns the depth-tiering AFTER this pass"
  - pattern: "Concurrent Count"
    how: "the audit is its dual enumeration institutionalized"
  - pattern: "Readback Before Commit"
    how: "V5's schema gate is the readback; this is the semantic hearback the schema cannot do"
  - pattern: "The Mock-Up Bay"
    how: "units that fail here enter its loop"
---
```

**Status:** working · primitives-proven (`response_format` schema-validated per V5; the semantic-recheck composition itself unexecuted).

**Core Dynamic.** The ironworker torques the bolt and *marks it* — and on critical joints a second qualified person independently verifies with their own wrench. The mark does not make the bolt tight; it makes the verification **visible and auditable without re-doing it**. **The invariant, stated generically (the Skeptic's demand): total-domain cheap verification + producer-to-mark bijection.** Uniform depth, complete coverage, receipted — *before* any sampling, because a sampled deep check of a systematically mis-torqued population is confident nonsense. The verify pass consumes the producer's engine-validated structured output (V5) and re-checks what schemas cannot express: does the number add up? is the claim entailed by the cited source?

**Repair applied (the Skeptic's):** the draft's "calibration negative" — proving a same-family reviewer must *miss* a seeded entailment flaw — is demoted from validation control to documented limitation. A control whose pass condition depends on a correlated reviewer happening to miss a specific flaw is not a control; it is a hope with a fixture. The Independence Law remains the design rule (a second wrench from the same toolbox is the painter's mark); the *proof* of the pass is the bijection audit, not the correlated failure.

**Sentinels.** A seeded arithmetic-flawed unit must fail its mark and the audit names it (exit 1). A seeded plan mismatch (a unit with no verify instance) must fail the bijection.

**Example.** Financial-data extraction: 1,000 filings → structured records; torque-verify re-checks each record's arithmetic (segments sum to total, percents ≤ 100, dates parse and order) with a cheap deterministic instrument; 7 fail, are named, and go to the adversarial tier while 993 proceed — complete cheap coverage first, sampled expensive depth second, each tier doing what it alone can do.

---

# GROUP III — ADAPTATION

---

## The Dispatch Catalogue (MEL)

```yaml
---
name: "The Dispatch Catalogue (MEL)"
scale: adaptation
status: working
forces: [Partial Failure, Finite Resources]
generators: [Threshold-Triggered Switch]
problem: "'Skip it this run' is decided ad hoc under pressure; degraded operation needs ex-ante authorization with compensation and expiry, not runtime judgment."
signals:
  - "instruments, credentials, feeds, or environments have known partial-failure modes worth tolerating for one run but not forever"
  - "the same degradation decision is being remade every run by whoever is tired"
  - "authorization to run degraded should expire, not persist silently"
stages:
  - name: mel-gate
    sheets: 1
    instrument_guidance: "any-wrapped CLI, per_sheet_fallbacks: [] — reads the AUTHORING-TIME mel.yaml (a versioned input, never generated at runtime) and the defect census defects.jsonl; left-join; emits dispatch-permit.json per matched row with expiry stamped; fails closed on any defect with no row"
    fallback_friendly: false
    purpose: "Deterministic admission: an item with no row is undispatchable, full stop."
  - name: compensate
    sheets: fan_out(K)
    instrument_guidance: "cheap instruments — executing a written procedure is mechanical; K is a PRE-DECLARED roster with per-defect skip_when guards, never a dynamic fan-out"
    fallback_friendly: true
    purpose: "Execute the matched row's compensating conditions; write comp-{item}.receipt.json."
  - name: expiry-audit
    sheets: 1
    instrument_guidance: "any-wrapped CLI, per_sheet_fallbacks: [] — at score end and on resume; expired permits revoke dispatch rights"
    fallback_friendly: false
    purpose: "A revoked item with a dependent stage routes to on_fail: escalate, never silently skipped."
dependencies:
  compensate: [mel-gate]
  expiry-audit: [compensate]
composes_with:
  - pattern: "Capability Census"
    how: "census measures, catalogue authorizes — the two artifacts must never merge, different authorities"
  - pattern: "The Validity Window"
    how: "the permit's expiry is a window with a compensation payload — the composition the corpus lacked"
  - pattern: "Dispatch with Declared Penalty"
    how: "MEL compensates procedurally; CDL prices quantitatively — siblings"
  - pattern: "The Graded Ladder"
    how: "a revoked permit's escalation route"
---
```

**Status:** working · primitives-proven (core); the fleet-membership face carries the `fleet` flag (zero proof executions). Ranked #3 by the collision; the Newcomer named it the strongest entry and its legal e-discovery example "the one I'd show a new user first."

**Core Dynamic.** The corpus's failure clause was `RUNNING → (failure) → DEGRADED → RETREAT/ESCALATE`, armed at runtime by judgment. The MEL is a **different state machine entirely**: `AUTHORIZE (pre-run, static, negotiated) → DISPATCH(degraded ∧ compensated) → WINDOW(expiring) → RESTORE`. The `RUNNING → DEGRADED` transition never happens — the system is *born* dispatched-degraded-and-compensated. Three properties: **ex-ante** — the compensating procedure is written when nobody is tired and nobody is scored on completing this run; **the unit of truth is the exemption catalogue, not the incident** — a typed table, one row per dispatchable failure (item, compensating conditions, repair-interval class A/B/C/D, expiry), and *an item with no row is undispatchable, full stop* (C2 — the closed vocabulary is the safety mechanism); **authorization carries an expiry clock** — a Category C deferral self-revokes in 10 days; authorization is a function of state ∧ time. Three authorities, none producible by the others: the composer authors the catalogue; a deterministic gate consults it; no sheet in the run ever gets a judgment seat over its own admission.

**The repair both flagging reviews demanded (the Practitioner's and the Skeptic's, converged from opposite sides):** the draft's Stage 1 was an LLM sheet generating `mel.yaml` *at runtime* — an ad-hoc judgment wearing the catalogue's clothes, contradicting the pattern's own ex-ante story. The catalogue is now an **authoring-time static asset**, versioned with the score, changed by review, never by the run it governs; the strong reasoner's one judgment seat is discharged at composition time. The compensation stage is a **pre-declared fixed roster** whose per-defect `skip_when` guards consult the permit file — the static DAG cannot spawn sheets from a runtime census, and the pattern no longer pretends otherwise.

**Sentinel (unchanged — it was already right):** a defect with no MEL row must abort dispatch — gate exits nonzero, `dispatch-permit.json` **absent**, failure naming the unmatched item. Not "reviewers notice." Novel failures have no row and the answer is "no dispatch" — correct and unsatisfying, and the pattern says so in When NOT to Use.

**Example.** Legal e-discovery: OCR down for 3 of 40,000 documents. The catalogue row: `ocr-unavailable-for-subset` dispatchable iff affected documents are flagged; compensation = mandatory attorney-review queue; interval C. The gate emits the permit; the compensate roster creates the review queue before any run stage sees a document; the permit expires in 10 days, after which the pipeline refuses to run until OCR is fixed or the catalogue is re-authored.

---

## The Priced Verification Ladder with Budget-Forced Degradation

```yaml
---
name: "The Priced Verification Ladder with Budget-Forced Degradation"
scale: instrument-strategy
status: approximation
forces: [Finite Resources, Exponential Defect Cost]
generators: [Graduate & Filter]
problem: "Verification spend compounds unbounded when every artifact gets the deepest affordable check, and degradation under budget pressure is silent."
signals:
  - "verification is a real fraction of total cost across long runs or concert chains"
  - "N× adversarial review for every artifact would kill the run's economics"
  - "budget pressure has quietly downgraded review quality with no record"
stages:
  - name: produce-and-classify
    sheets: fan_out(N)
    instrument_guidance: "work instruments; every artifact's risk_class (low|standard|critical) comes from the COMPOSER-AUTHORED class map keyed on artifact type, never producer self-classification"
    fallback_friendly: true
    purpose: "Produce typed units carrying a declared risk class assigned at creation."
  - name: ledger-update
    sheets: 1
    instrument_guidance: "any-wrapped CLI, per_sheet_fallbacks: [] — computes estimated spend from captured output token counts / character lengths and appends to budget-ledger.jsonl BEFORE the next tier's skip_when evaluates"
    fallback_friendly: false
    purpose: "The explicit spend-capture mechanism the draft lacked; the ledger is not writable by the agents whose work it meters."
  - name: tier-1
    sheets: 1
    instrument_guidance: "CLI validation only (schema, lint, structure) for everything"
    fallback_friendly: false
    purpose: "The cheap tier that is always already running."
  - name: tier-2
    sheets: fan_out(M)
    instrument_guidance: "single-instrument review sheets; skip_when guard: risk_class == low"
    fallback_friendly: true
    purpose: "Bought only for standard-and-above artifacts."
  - name: tier-3
    sheets: fan_out(2)
    instrument_guidance: "adversarial pair, opposing mandates, different vendors — vendor diversity IS the adversarial value; skip_when guard: remaining_budget_below_threshold (reads budget-ledger.jsonl)"
    fallback_friendly: false
    purpose: "The expensive tier; when the envelope thins, it collapses — receipted."
dependencies:
  tier-1: [produce-and-classify, ledger-update]
  tier-2: [tier-1]
  tier-3: [tier-2]
composes_with:
  - pattern: "Echelon Repair"
    how: "its before-failure dual — Repair tiers responses after failure; this prices verification before"
  - pattern: "Immune Cascade"
    how: "tier skeleton (the Skeptic's fold objection answered: the skeleton is shared, the economics are new — descent-on-envelope is the distinct claim, and it is flagged approximation until proven)"
  - pattern: "Rent-Then-Commit"
    how: "the rent/buy decision at each rung transition"
  - pattern: "Dispatch with Declared Penalty"
    how: "the ladder supplies the prices; the CDL supplies the aggregate admission check"
---
```

**Status:** approximation — **the mid-score degradation behavior is unverified** and says so on its face (the Skeptic: `skip_when` is fail-open, the budget ledger's integrity and timing were unspecified, and `cost_limit_usd` is not evidence of a readable remaining-budget value). What is proven: the guards evaluate; the ledger is an ordinary file; the tiers are ordinary sheets.

**Core Dynamic.** Verification depth is a purchase, and the currency is finite. The immune system never escalates everything: innate response is the cheap tier always already running; antibodies and clonal expansion are bought only when cheap-tier receipts come back "not clearing." Three moves: **declared prices on every rung**; **risk-classed entry** (set at creation by the composer's class map, never at review time by the thing being judged — the Skeptic's capture fix); **envelope-forced descent** — when remaining budget thins, rungs collapse downward and the collapse is *receipted*. The pattern's soul: **when it degrades, the organism does not silently skip the top tier — it records the fever it did not mount.** A logged degradation is a risk consciously accepted; a silent skip is a lie the ledger will eventually bill (C5).

**The repair (the Practitioner's missing mechanism):** the draft read "remaining budget" from a ledger nothing wrote. Now an explicit `ledger-update` CLI step runs between tiers: it computes estimated spend from the run's captured output token counts / character lengths and appends to `budget-ledger.jsonl` — a workspace file the metered agents cannot write — *before* the tier-3 guard reads it. `cost_limit_usd` rides at job level as the hard brake.

**Sentinel pair (both polarities, unexecuted until the prove path lands them):** a fat-budget run must produce *zero* degradation receipts (a sentinel script fails if any receipt exists); a thin-budget run must produce receipts naming the rung skipped and the budget at decision time. Until this pair has executed, budget-forced descent is doctrine, not fact — and the pattern's status line says exactly that.

**Example.** Legal-doc processing: bulk standard contracts get tier-1 structural validation only; anything touching indemnity enters at tier 3; when the month's API budget is 80% spent, tier-3 collapses to tier-2 for everything and the receipts say which documents got the weaker look.

---

## Dispatch with Declared Penalty (CDL)

```yaml
---
name: "Dispatch with Declared Penalty (CDL)"
scale: score-level
status: working
forces: [Finite Resources, Partial Failure]
generators: [Threshold-Triggered Switch]
problem: "Deviations are checked per-row, so two individually tolerable deviations jointly breach a margin without anyone seeing the sum."
signals:
  - "a cheap instrument down lowers guarantees without canceling the run"
  - "fleet members accumulate small deviations that must be summed, not listed"
  - "the individually-tolerable-jointly-not check is currently nobody's job"
stages:
  - name: margin-gate
    sheets: 1
    instrument_guidance: "any-wrapped CLI, per_sheet_fallbacks: [] — enumerates open deviations from the census, joins against the authoring-time penalty-table, combines per each margin's declared combination law, compares against margins.yaml (composer-owned file permissions as authority); fails closed on any breached margin even if every individual deviation is inside its own row's bounds"
    fallback_friendly: false
    purpose: "The aggregate admission check — the sum matters, not the rows."
  - name: ledger-update
    sheets: 1
    instrument_guidance: "any-wrapped CLI, per_sheet_fallbacks: [] — appends MEASURED actuals to penalty-actuals.jsonl at run end"
    fallback_friendly: false
    purpose: "Close the loop for the next composition's price revision."
dependencies:
  ledger-update: [margin-gate]
composes_with:
  - pattern: "The Dispatch Catalogue (MEL)"
    how: "side-by-side decision tables — MEL owns procedural compensation, CDL owns the aggregate sum"
  - pattern: "The Priced Verification Ladder"
    how: "the ladder supplies the price tags; this supplies the admissible-sum check"
  - pattern: "Capability Census"
    how: "census says what is down; the table says what it costs; the gate says whether the mission still flies"
  - pattern: "Rent-Then-Commit"
    how: "per-instance rent/buy vs aggregate admission — different objects"
---
```

**Status:** working · primitives-proven. The Practitioner: "Crisp and actionable… the jq aggregation script is trivial to write, the gate is fail-closed, and the aggregate breach sentinel is clearly specified."

**Core Dynamic.** MEL says "fly despite the broken thing, *compensating* procedurally." CDL says "fly despite the missing thing, *paying* quantitatively" — and the payment is checked **in aggregate**: dispatch is authorized iff the mission's declared margins absorb the *total* declared penalty of all open deviations. Two deviations each individually benign can jointly breach a margin; the CDL discipline is what makes that visible, because the gate's arithmetic is over the sum — the individually-tolerable-jointly-not check that naive per-row checking passes, which is the pattern's entire reason to exist.

**The penalty algebra (the Skeptic's demand — without it, jq produces precise nonsense):** every penalty is declared in **named units** (`coverage_pct`, `confidence_delta`, `cost_usd`, `latency_p95_ms`); every margin declares its **combination law** — sum for additive units, max for latencies, product for probabilities — and the combination is computed in the margin's declared unit; **correlated deviations must be declared co-priced** (two deviations from one vendor share a correlation entry, else the sum double-discounts the same underlying failure — the ETOPS caveat: independence assumptions are defeated by same-batch engines); **margins are owned** by the composer's `margins.yaml`, written with the score and never writable by the run — file permissions as an authority mechanism (the same authority-by-file-permission doctrine as the Hold-Point roster and the pulse keeper, stated once in Composition Doctrine). A unit that cannot be declared honestly (quality "points" with no defined combination law) is a MEL compensation row instead, not a CDL penalty.

**Sentinel — the aggregate breach:** two individually-bounded deviations summing past a margin must exit nonzero with `margin-report.json` showing both rows, the combined value, and the breached `margin_key`. Named artifact, named command, named exit code.

**Example.** Market-intelligence pipeline: three of seven sources down (each: coverage −4%, confidence −0.1); sentiment model on fallback tier. Individually fine. The gate combines: coverage 83% — below the client's declared 85% floor for the "comprehensive" tier. The run dispatches *downgraded to standard with a typed downgrade notice* or waits for a source — the client contract, not a runtime judgment, decides. The actuals ledger records what the downgrade really cost; next quarter's margins are repriced from evidence.

---

## The Hotwash Dispatch (Lesson Routing)

```yaml
---
name: "The Hotwash Dispatch (Lesson Routing)"
scale: iteration
status: approximation
forces: [Information Asymmetry, Convergence Imperative]
generators: [Exploit Failure as Signal]
problem: "Failure evidence accumulates in run records but no downstream sheet has committed to change behavior on it, so lessons dispatch into the void as context noise."
signals:
  - "self-improvement loops where iteration N+1 should learn from iteration N's actual validation failures"
  - "failure logs grow while prompts stay identical"
  - "evidence without a named consumer is being carried forward anyway"
stages:
  - name: attempt
    sheets: 1
    instrument_guidance: "work instrument; wrapped prompt receives prior failures via the loop's failure transport"
    fallback_friendly: true
    purpose: "The work; its validation failures are the raw material."
  - name: validate
    sheets: 1
    instrument_guidance: "real validations — the failures land in the engine's record"
    fallback_friendly: false
    purpose: "Honest failure surface; no paraphrase."
  - name: classify
    sheets: 1
    instrument_guidance: "any-wrapped CLI, per_sheet_fallbacks: [] — maps validation codes through the digest-pinned dispatch-table.yaml to consuming sheets and failure classes; writes curriculum/{class}.json"
    fallback_friendly: false
    purpose: "Deterministic routing; unmapped codes land in curriculum/unclaimed/ and are COUNTED — the honesty meter."
dependencies:
  validate: [attempt]
  classify: [validate]
composes_with:
  - pattern: "After-Action Review"
    how: "AAR owns reflection and capture; Hotwash owns routing the evidence to a pre-committed consumer — the neighbor this pattern must never duplicate (the Newcomer's catch)"
  - pattern: "The Paid Question"
    how: "same demand-register logic, transposed from questions to lessons"
  - pattern: "Serial Troponin"
    how: "the loop spine — unproven together, proven together"
  - pattern: "The Spent Lesson Checkout"
    how: "the other half of the lifecycle, now independently provable (the split)"
---
```

**Status:** approximation — the failure-transport surface (`failure_history` for the retry-local case, and any cross-iteration carrier) is native-unproven; the classification and routing machinery itself is ordinary files + CLI and composes today against an explicit failure-report file if the engine transport never lands. **The split (the Practitioner's):** the draft fused dispatch and checkout into one seven-stage monolith riding two unproven surfaces at once; each half now stands alone with its own debt named.

**Core Dynamic.** On the failure-evidence channel: a failure enters the curriculum only if a *named downstream sheet in the next iteration has pre-registered that it will change behavior on that failure class* — otherwise it dies as a logged non-event in `unclaimed/`, counted. Evidence without an owner is noise; the consumer pays for the lesson by pre-committing to consume it. The dispatch table is digest-pinned; a renamed consumer dispatches into the void — which the count catches.

**Validations.** Every `curriculum/{class}.json` names a consuming sheet that exists in the score; the next attempt's output cites the curriculum files it consumed (line-anchored `content_regex`). **Sentinel:** a synthetic failure code planted in the table with no consumer → `test $(ls curriculum/unclaimed/ | wc -l) -ge 1` — the run FAILS if unclaimed failures silently dispatched anyway.

---

## The Spent Lesson Checkout

```yaml
---
name: "The Spent Lesson Checkout"
scale: iteration
status: approximation
forces: [Convergence Imperative, Finite Resources]
generators: [Measure Convergence Character]
problem: "An automatic failure channel with no checkout is a context-debt machine: iteration 30's prompt carries iterations 1–29's failures, most long remediated, each training the current attempt to dodge a ghost."
signals:
  - "long self-chains or shared workspaces where per-iteration context cost is measurable and growing"
  - "prompts carry failures no current sheet has failed for many iterations"
  - "lessons leave the curriculum by silence, not by receipt"
stages:
  - name: track
    sheets: 1
    instrument_guidance: "any-wrapped CLI — appends each iteration's failure classes to curriculum-history.csv (class, iteration, present/absent, signature)"
    fallback_friendly: false
    purpose: "The claim ledger: presence/absence history per class."
  - name: checkout
    sheets: 1
    instrument_guidance: "any-wrapped CLI, per_sheet_fallbacks: [] — finds classes absent N consecutive iterations (N authored, default 2), verifies against the ENGINE'S OWN RECORD, not the CSV; moves them to archive/ with a receipt row"
    fallback_friendly: false
    purpose: "Supervised, receipted retirement: the CSV is the claim, the engine record is the evidence."
  - name: re-enter
    sheets: 1
    instrument_guidance: "CLI — an archived class re-fails → back to active, recurrence_count incremented; at an authored threshold, promoted to escalation instead of curriculum"
    fallback_friendly: false
    purpose: "The loop confesses it cannot fix this."
dependencies:
  checkout: [track]
  re-enter: [checkout]
composes_with:
  - pattern: "The Hotwash Dispatch"
    how: "the other half of the lifecycle — dispatch arms lessons, checkout retires them; composed end-to-end only after each is proven alone (the Skeptic's sequencing)"
  - pattern: "The Validity Window"
    how: "per-class TTLs — the automatic checkout for classes too stale to track"
  - pattern: "Watch Rollover"
    how: "handover hygiene for the curriculum itself — what carries forward is chosen, not defaulted"
  - pattern: "After-Action Review"
    how: "AAR captures; checkout decides what may be forgotten"
---
```

**Status:** approximation — same transport debt as the dispatch half (the engine's own record needs a documented, stable path and schema, which the Skeptic demanded and the engine has not yet exposed; until then the record is an explicit engine-written failure log, if and when it exists). The retirement arithmetic composes today.

**Core Dynamic.** A resource does not leave the incident because the fire is out; it leaves when the demobilization unit confirms its business is complete (ICS-221). Applied to lessons: **ending things is a supervised, receipted act.** A lesson leaves the curriculum only through a verified checkout — a run whose evidence demonstrates the failure class is closed — and the checkout is checked against the *engine's own record*, because a CSV can be forged by absence. Cyclical failures take the re-entry path: a released class that re-fails returns with its recurrence count, and recurrence is itself curriculum — at threshold, the class is promoted to escalation (the loop admits it cannot fix this).

**Sentinel (the draft's best paranoia, preserved):** a never-remediated class planted with a *forged* two-iteration absence in the CSV but a live failure in the engine record → `grep -c "planted-class" archive/*` exits 1 — the run FAILS if checkout trusted the ledger over the evidence.

**Example.** Documentation-generation loop: iteration 1 fails `content_contains` on three required safety warnings; the classifier maps the code to the writer's curriculum; iteration 2's writer sees the actual failure evidence — the three missing strings, not a paraphrase — and the citation check proves it acted on them. Month-long variant: week 1's broken image paths are fixed in week 2 and check out in week 3 with receipts; week 6's prompts carry week 5's *live* problems only — not a museum of solved ones.

---

# GROUP IV — SCORE-LEVEL

---

## Keystone-First Sequencing

```yaml
---
name: "Keystone-First Sequencing"
scale: score-level
status: working
forces: [Exponential Defect Cost, Instrument-Task Fit]
generators: [Gate on Environmental Readiness]
problem: "Construction intuition builds big-to-small (biomass ordering), so the artifacts that parameterize the most downstream prompts are built late and every earlier sheet worked under wrong conditions."
signals:
  - "a small upstream artifact (schema, rubric, lexicon) changes the prompts of many downstream sheets"
  - "merge stages reconcile hundreds of small inconsistencies a different order would have prevented"
  - "the expensive instrument's output would amortize across the whole cheap cascade if it ran first"
stages:
  - name: keystone-identification
    sheets: 1
    instrument_guidance: "short analysis sheet; names the leverage set (schema + rubric + lexicon) with a stated reason per item, schema-typed output — its reasoning is recorded, not trusted"
    fallback_friendly: true
    purpose: "Identify which outputs parameterize the most downstream prompts."
  - name: keystone
    sheets: 1
    instrument_guidance: "the strongest reasoner available — keystones are exactly where expensive judgment compounds"
    fallback_friendly: false
    purpose: "Build the leverage set first, alone, with its own quality gate."
  - name: cascade
    sheets: fan_out(N)
    instrument_guidance: "cheap bulk instruments (ollama / cheapest alias) — downstream work is abundant, lower-stakes"
    fallback_friendly: true
    purpose: "Main fan-out, every prompt CARRYING the keystone content via prelude — following in DAG order is not enough."
dependencies:
  keystone: [keystone-identification]
  cascade: [keystone]
composes_with:
  - pattern: "Cathedral Construction"
    how: "keystone-first is the decision rule for what Cathedral builds first; Cathedral owns iterative construction toward a target"
  - pattern: "Prefabrication"
    how: "keystone-first decides which contract Prefabrication freezes first; Prefabrication owns the producer-producer interface"
  - pattern: "The Attested Merge Gate"
    how: "version echoes feed it"
  - pattern: "The Priced Verification Ladder"
    how: "keystones enter at tier 3; cascade artifacts at their own risk class"
  - pattern: "Firing the Pass"
    how: "the keystone is the mise en place the expeditor gates on (kinship edge, permanent-corpus side)"
---
```

**Status:** working · primitives-proven (dependencies, prelude injection, validations — prime prove-path material). Kept over the Skeptic's fold objection: the Practitioner ranked it among the six strongest, and two reviews beat one. The differentiation the Skeptic demanded is now in-entry (see composes_with): Cathedral Construction owns *iterative construction toward a known target*; Prefabrication owns *interface contracts between producers*; Keystone-First owns *ordering by leverage* — and that selection rule applies to scores with no iteration and no contracts. Where they overlap, keystone-first is the decision rule for what the others build first.

**Core Dynamic.** Ecosystems build *leverage-first*: the component whose presence rewrites the conditions every other component depends on goes in first — even if tiny, even if peripheral. The wolf is a small fraction of the biomass but the prerequisite for the riparian story; willows planted without wolves are elk food. In a DAG, a small set of sheets' outputs *change the prompts of many downstream sheets* — style guides, ground-truth lexicons, schemas, evaluation rubrics. Install them first and gate everything on completion; install them late and rework propagates. This is also *why* mixed-instrument pricing works: the expensive instrument's output amortizes across the whole cheap cascade — the economic argument for instrument mixture in one pattern.

**Sentinel.** A run with the keystone sheet deliberately skipped must fail the version-echo validation across the cascade — cascade work done keyless is the elk-food outcome, caught.

**Example.** Multi-service API documentation score: the OpenAPI spec and terminology lexicon are the wolves; writing endpoint docs before those exist means every doc sheet works under drifting vocabulary and the merge stage reconciles a thousand small inconsistencies a keystone-first order would have prevented.

---

## The Watchman's Gate

```yaml
---
name: "The Watchman's Gate"
scale: score-level
status: working
forces: [Exponential Defect Cost, Partial Failure]
generators: [Threshold-Triggered Switch]
problem: "Destructive execution must never depend on a check that fails open, so the veto must live in a dedicated, deterministic, independently-instrumented sheet."
signals:
  - "any AI → destructive-action seam: deploys, mass rewrites, publication, external sends"
  - "a broken predicate would otherwise admit unvetted work silently (V1)"
  - "the thing being gated and the thing deciding are the same instrument"
stages:
  - name: declare
    sheets: 1
    instrument_guidance: "producer sheet, response_format: json_schema — emits the typed intent (what will be touched, how, declared blast radius)"
    fallback_friendly: true
    purpose: "Make the intent machine-checkable before it is checkable."
  - name: watchman
    sheets: 1
    instrument_guidance: "any-wrapped CLI, per_sheet_fallbacks: [] — MUST be a different instrument class than declare; validates the declaration against standing rules (path scope, declared reversibility, digest match) and writes pick.json (GO/NO-GO + declaration sha256)"
    fallback_friendly: false
    purpose: "The pick instruction IS a validation; refusal is loud, here."
  - name: execute
    sheets: 1
    instrument_guidance: "the destructive sheet; skip_when is the REFUSAL predicate: test ! -f pick.json || ! jq -e '.verdict == \"GO\"' pick.json — succeeds (skips) when GO is absent or invalid"
    fallback_friendly: false
    purpose: "Proceed only under a present, valid GO."
dependencies:
  watchman: [declare]
  execute: [watchman]
composes_with:
  - pattern: "Readback Before Commit"
    how: "this is its placement law given V1"
  - pattern: "The Cue Light"
    how: "pick.json is a one-bit cue with a digest"
  - pattern: "The Hold-Point Witness"
    how: "same placement law, different scale — within-score vs score-to-human"
  - pattern: "Capability Census"
    how: "the census roster is what qualifies the watchman instrument"
---
```

**Status:** working · primitives-proven, verified seam with engine citations attached (V1: `skip.py:13-19`; V5 for the typed declaration). Ranked #5 by the collision; the Newcomer called its delete-the-watchman negative "the draft's best falsifiable claim." The Newcomer also ranked it top-tier *for its citation discipline* — and it survives the Skeptic's kill only because its own law was right and its example was wrong.

**The polarity inversion, fixed (the Skeptic's catch — the most important single correction of the pass).** The draft's `skip_when: 'test -f pick.json && grep -q GO pick.json'` succeeds exactly when the GO exists — under Marianne semantics (skip on command success), it would **skip authorized execution and proceed on unauthorized execution**, with V1 evaluation errors *also* proceeding. The pattern's core doctrine survived untouched — the load-bearing check never lived in `skip_when`; it lives in the watchman sheet's own fail-closed validation — but the consent echo was inverted. Corrected form in the frontmatter and here: `skip_when: 'test ! -f pick.json || ! jq -e ''.verdict == "GO"'' pick.json'`. Absent/invalid GO → command succeeds → the sheet refuses; present GO → command fails → the sheet proceeds; and even a V1 evaluation error only ever risks a refusal, never an unauthorized execution, because the refusal already happened loudly one sheet earlier. This inversion is now **Composition Doctrine #1**, corpus-wide: always write the refusal predicate.

**Core Dynamic.** On a real pick, the operator does not take instructions from the crowd: one qualified signal person exclusively owns the channel to the crane, and is *not the rigger who set the load* — independence at the channel level (C3). Translation to the verified seams: a `response_format: json_schema` producer emits its typed declaration of intent; a separate deterministic gate sheet is the only thing the executing sheet listens to; the gate CANNOT live in the executing sheet's own `skip_when` (fail-open, V1), so the watchman is a real sheet whose validation IS the pick instruction.

**Negative controls.** The dry-run fixture includes a declaration violating path scope — the watchman MUST emit NO-GO (`grep -c NO-GO pick-negative.json` returns 1, else exit 1). **The load-bearing negative:** delete the watchman sheet → execute's refusal predicate finds no `pick.json` → skips → the downstream consumer's validation fails on the missing artifact. The gate is load-bearing *by construction*, and the failure is visible at the consumer, not silent.

**Example.** Database-migration concert: declare emits the migration manifest as json_schema; watchman (pure CLI: jq + a scope checker) verifies the table list against the change-freeze file and writes GO with the manifest digest; the migration sheet's refusal predicate consumes GO. A broken scope checker fails open — and the migration still refuses, because the artifact it needs was never written.

---

## The Hold-Point Witness

```yaml
---
name: "The Hold-Point Witness"
scale: concert-level
status: approximation
forces: [Partial Failure, Progressive Commitment]
generators: [Threshold-Triggered Switch]
problem: "Some seams must STOP — not fail, not retry — until an authority outside the score signs, and the score must not be able to manufacture that signature for itself."
signals:
  - "deployment gates, publication gates, destructive-test authorization, privacy-affecting sends"
  - "the authority to proceed is a human or external system the score cannot impersonate"
  - "a paused job with no notification is a deadlock wearing a safety vest"
stages:
  - name: prepare-hold
    sheets: 1
    instrument_guidance: "strong reasoner + a notification CLI step (Slack/webhook/console) — the package must be honest, complete, and NOTICED"
    fallback_friendly: false
    purpose: "Assemble the typed witness package (what was done, evidence digests, the specific question) and notify the authority that the hold exists."
  - name: hold
    sheets: 1
    instrument_guidance: "engine machinery — on_success trigger pause: true (flow.py:100-102); the job parks durably; nothing retries, nothing times out into proceeding"
    fallback_friendly: false
    purpose: "The designed stop."
  - name: witness-signature
    sheets: 0
    instrument_guidance: "out of band — the human/external witness writes disposition.json (typed: disposition ∈ {proceed, reject, proceed-with-conditions}, conditions, authority_id, timestamp, pause_event_id, package_digest)"
    fallback_friendly: false
    purpose: "The key is manufactured outside the score, by construction."
  - name: resume-check
    sheets: 1
    instrument_guidance: "any-wrapped CLI, per_sheet_fallbacks: [] — first sheet after mzt resume; validates disposition.json's schema, authority_id against the declared roster, package_digest binding, AND freshness: the disposition must name the CURRENT pause event (pause_event_id) and be newer than it"
    fallback_friendly: false
    purpose: "The door checks the key itself; writes unlock.json only on full validation."
  - name: execute-post-hold
    sheets: 1
    instrument_guidance: "the work; skip_when is the refusal predicate (skip when unlock.json absent or invalid)"
    fallback_friendly: true
    purpose: "Proceed under a fully validated unlock."
dependencies:
  hold: [prepare-hold]
  resume-check: [hold]
  execute-post-hold: [resume-check]
composes_with:
  - pattern: "Transfer of Command at the Seam"
    how: "owns the briefing content; this owns the signature protocol and the pause mechanics"
  - pattern: "The Graded Ladder"
    how: "the ladder climbs, the hold point stops — escalate/pause actions feed this seam"
  - pattern: "The Change-Order Ledger"
    how: "a proceed-with-conditions disposition writes an entry before post-hold runs"
  - pattern: "The Watchman's Gate"
    how: "same placement law, different scale"
---
```

**Status:** approximation — pause mechanics are source-cited (`pause: true` flow.py:100-102; `pause_before_chain` orchestration.py:316-323, PAUSED_AT_CHAIN) but the end-to-end seam has zero proof executions (the Skeptic: source citations are not an end-to-end proof); the prove queue's #2 item. The Practitioner confirmed it composable in ten minutes with the notify step added; the Skeptic demanded the trust model, and it is now stated.

**Core Dynamic.** In the inspection test plan, certain joints are *hold points*: the condition exists, the process STOPS until the authorized witness signs, and the signature unlocks exactly the next phase — nothing more. What pass 1 lacked and this adds: the witness signature is a typed artifact with a named authority bound to the package digest, and **resumption without a signature-shaped file is itself a validation failure.** The hold point is not "we paused"; it is "the only key that opens the door is a signed disposition from the named authority — and the door checks the key itself."

**Trust model (the Newcomer's demand, stated once):** `authority_id` is not a cryptographic signature; the trust boundary is **authority-by-file-permission** — the roster and disposition live in workspace paths writable only by the human witness's account, the same doctrine CDL's `margins.yaml` and the pulse keeper rely on. This is honest for workspace-local concerts and must be replaced by real signing for adversarial settings — say so, don't imply it. **Stale-disposition handling (the Skeptic's):** the disposition carries `pause_event_id` and a timestamp; resume-check rejects a disposition naming a different or older pause than the current one — a yesterday's proceed cannot unlock today's hold.

**Negative controls.** A: a disposition from an authority NOT on the roster fails — no unlock, receipt naming the impostor id. B: a digest-mismatched disposition (the package changed after signature — the classic substitution attack) fails. C (the seam itself): resume WITHOUT any disposition.json → the failure receipt names resume-check, NOT execute-post-hold's skip (which merely skips) — proving the refusal lives in the right place even though `skip_when` is fail-open. The exact V1 discipline, demonstrated at the corpus's named unowned seam.

**Example.** Model-release concert: training score completes → hold with the evaluation witness package → data-governance reviewer signs (proceed with condition: EU-market flag off) → resume-check validates id, digest, and pause event → the release score executes with the condition visible in its opening context (a change-order ledger entry, naturally).

---

## The Editor's Disposition

```yaml
---
name: "The Editor's Disposition"
scale: score-level
status: approximation
forces: [Structured Disagreement, Partial Failure]
generators: [Threshold-Triggered Switch]
problem: "Multi-advisory fan-ins fail by advice-drowning or advice-collapse because 'what did the reviewers think?' and 'what do we do?' are conflated into one act."
signals:
  - "multiple independent evaluations must produce ONE action, not one document"
  - "reviewers negotiate into a mushy consensus no one endorses"
  - "authors optimize for appeasement across incompatible reviewer standards"
stages:
  - name: advise
    sheets: fan_out(2-4)
    instrument_guidance: "mixed-family reviewers; each produces a typed report (json_schema: findings[], overall_recommendation from a closed enum, confidence)"
    fallback_friendly: true
    purpose: "Independent answers to 'what is wrong?'"
  - name: respond
    sheets: 1
    instrument_guidance: "optional; Rejoinder Ledger composition — findings frozen with IDs, typed rejoinders written"
    fallback_friendly: true
    purpose: "The author's engagement with findings, typed and joinable."
  - name: dispose
    sheets: 1
    instrument_guidance: "ONE editor sheet (the unitary authority IS the pattern; fan-out there would dissolve it); response_format: json_schema forces {disposition: enum[accept, minor, major, reject], rationale citing finding-IDs, required_changes[]}"
    fallback_friendly: false
    purpose: "One accountable routing decision from a closed vocabulary — not a vote, not synthesis."
  - name: route
    sheets: 1
    instrument_guidance: "any-wrapped CLI, per_sheet_fallbacks: [] — deterministic dispatch on the disposition"
    fallback_friendly: false
    purpose: "accept → publish/merge gate; reject → dead-letter quarantine with advisories attached; minor/major → AWAITING sheet.loops proof (do not invent the loop)"
dependencies:
  respond: [advise]
  dispose: [respond]
  route: [dispose]
composes_with:
  - pattern: "Rejoinder Ledger"
    how: "findings-freeze and bijection supply the respond stage wholesale"
  - pattern: "Condorcet's Premise"
    how: "the decision-table entry this pattern owes the corpus: vote when you want the crowd's aggregated judgment; dispose when you want one accountable routing decision"
  - pattern: "Dead Letter Quarantine"
    how: "reject's destination — advisories preserved verbatim; a rejected-with-receipts artifact is curriculum, not garbage"
  - pattern: "The Dialectical Pair"
    how: "the cheap first line underneath"
---
```

**Status:** approximation — `response_format` native-unproven (V5 schema-validated per attempt, zero end-to-end executions); this is arguably the **minimal exercise** of the corpus's most-cited never-executed primitive (short outputs, closed enum, immediate mechanical check), and the prove queue's #1 item. The `minor`/`major` routes additionally await `sheet.loops` (the Skeptic: one closed route proven first — `accept` and `reject` route deterministically today; the loop routes are named as awaiting, not invented).

**Core Dynamic.** Reviewers ADVISE; the editor DISPOSES. A single agent with different authority reads the reports and issues one of a closed set of dispositions: **accept / minor revision / major revision / reject**. Not a vote (Condorcet), not content synthesis (Sugya Weave), not consensus (Delphi): a **unitary decision authority over typed advisory inputs, with a closed disposition vocabulary and a mandatory rationale citing the advisories.** The closed vocabulary is load-bearing — it prevents the editor from synthesizing a new position or averaging scores; it forces a *routing* decision. The failure semantics are distinctive: a rejected paper with excellent reviews is not a failure — it is a disposition (the Typed-Draw family, C8).

**Sentinel.** One reviewer's finding is objectively fatal and the editor disposes `accept` citing that finding-ID as "addressed" → `disposition-check.py` requires every cited-and-addressed finding to appear in rejoinders as accept+change; missing → exit 1 with `disposition-report.json` carrying `"violations": [{"type": "uncited_acceptance"}]`. This catches the capture failure — an editor laundering a fatal finding through vague rationale. The editor must be a different instrument family than reviewers AND authors (Independence Law at composition time).

**Example.** Content-release gate: three reviewers assess a draft (factual accuracy, brand voice, legal risk) with typed findings; the editor disposes — major revision (legal findings load-bearing) — and the route sends only the legal-flagged sections to re-review, not the whole draft. Without the disposition split, the draft oscillates between three reviewers' incompatible standards for three cycles.

---

## The Mock-Up Bay

```yaml
---
name: "The Mock-Up Bay"
scale: iteration
status: approximation
forces: [Exponential Defect Cost, Progressive Commitment]
generators: [Incremental Exposure, Gate on Environmental Readiness]
problem: "The cost of discovering a detail defect at unit N=400 exceeds one observed unit N=1, but volume production starts without a representative first article under independent inspection."
signals:
  - "mass content generation, template instantiation, codegen rollout, migration waves"
  - "a detail defect would replicate silently across the whole volume"
  - "acceptance criteria are being negotiated after candidates exist"
stages:
  - name: rubric-press
    sheets: 1
    instrument_guidance: "strong reasoner + CLI digest pin — pre-registers the rubric BEFORE any candidate exists; rubric.yaml digest-pinned"
    fallback_friendly: false
    purpose: "Pre-registration is what makes the inspection a test rather than a negotiation (C1)."
  - name: build-candidate
    sheets: 1
    instrument_guidance: "production instrument, production prompt — produces exactly ONE representative artifact"
    fallback_friendly: true
    purpose: "The actual assembly, executed once, under observation."
  - name: inspect
    sheets: 1
    instrument_guidance: "DIFFERENT instrument family; reads the artifact against the pre-registered rubric; writes verdict.json via response_format (typed: pass/fail + defect classes)"
    fallback_friendly: false
    purpose: "Independent sign-off; the builder's own sign-off is a paint sample, not a mock-up."
  - name: refine-brief
    sheets: 1
    instrument_guidance: "reads verdict defects; writes the next iteration's correction memo into the builder's input slot"
    fallback_friendly: true
    purpose: "Feed the loop; rounds are bounded by count."
dependencies:
  inspect: [build-candidate]
  refine-brief: [inspect]
composes_with:
  - pattern: "The Serial Troponin"
    how: "Troponin owns the monotone serial-test spine; this owns the representative-first-article loop with independent sign-off"
  - pattern: "The Unprimed Falsifier"
    how: "its reader panels are this pattern's inspector tier at full adversarial depth"
  - pattern: "First Article Characterization"
    how: "compose its measurement half with this loop's approval half"
  - pattern: "The Wordless Manual (via Prefabrication)"
    how: "production fan-out consumes the approved pattern as template"
  - pattern: "Unison Drift"
    how: "the drift check before the volume spend this pattern gates"
---
```

**Status:** approximation — `sheet.loops` and `response_format` native-unproven (zero proof executions corpus-wide for either); this and Serial Troponin are the two natural first proofs of the loop primitive. **The Newcomer's designation stands: this is the newcomer's first score** — five sheets, one unproven primitive, concrete syntax in Composition Doctrine #6.

**Core Dynamic.** Nobody replicates a facade detail forty stories up before the architect, the waterproofing consultant, and sometimes the AHJ have signed off on a full-scale mock-up — one representative section, production materials, production crews, standing on the ground where everyone can interrogate it. The mock-up is not a drawing review; it is *the actual assembly, executed once, under observation, before commitment to volume.* The deep structure: **the loop's exit condition must be an artifact written by someone other than the builder** — a mock-up the builder signs off themselves is a paint sample, not a mock-up. And the rubric is pre-registered BEFORE any candidate exists (C1). V6 arms the negative discipline: an `until` expression that errors kills the span E999 (fail-closed), so the verdict-file schema is load-bearing validation, not decoration.

**The reduction (the Skeptic's):** the minimal loop proof is rubric-press → build → inspect → refine under the Composition Doctrine #6 loop block; the post-loop production fan-out (width N) is composition, not proof burden — it rides *after* loop exit and is ordinary proven fan-out.

**Sentinels.** A: a seeded defective candidate must produce verdict fail and the loop must iterate (round odometer ≥ 2; exit 1 if production ran after round 1). B: remove the `until` clause → the count-bound loop still terminates but the fixture's defective candidate ships to production → production's own validation fails on the seeded defect marker — proving the exit condition, not the count, is the gate.

**Example.** Brand-voice content farm: one representative article built, inspected against a pre-registered voice rubric by a different instrument, correction memos looped (max 3 rounds), then 400 articles fanned out from the approved pattern.

---

## The Midseason Pivot Ledger

```yaml
---
name: "The Midseason Pivot Ledger"
scale: concert-level
status: approximation
forces: [Information Asymmetry, Progressive Commitment]
generators: [Accumulate Knowledge]
problem: "Campaigns long enough that the plan can be wrong pivot by thrash or by retcon-that-discards; neither reconciles the new frame with completed evidence."
signals:
  - "multi-movement scores, self-chains, concert chains where mid-flight discovery re-shapes later phases"
  - "early discoveries invalidate later decomposition, but completed movements' artifacts are still true"
  - "plans are hypotheses, and the score pretends otherwise"
stages:
  - name: break-arc
    sheets: 1
    instrument_guidance: "strong reasoner — decomposes the goal into ordered beats; writes arc.md + canon-ledger.json (facts as enforceable predicates: typed fact, source artifact digest, weight load-bearing|negotiable)"
    fallback_friendly: false
    purpose: "Planned-arc decomposition with a typed ledger of established facts."
  - name: execute-beat
    sheets: 1
    instrument_guidance: "the workhorse; each beat completes with its facts appended to the canon ledger"
    fallback_friendly: true
    purpose: "Accumulate canon; every fact digest-anchored."
  - name: pivot-review
    sheets: 1
    instrument_guidance: "strong reasoner from a DIFFERENT family than break-arc (the self-dealing rule); scheduled between movements — reads arc + canon + recent beats; either confirms (pivot-continue.marker — the logged absence, a typed draw) or writes pivot.md citing every load-bearing fact it preserves and marking any it reinterprets"
    fallback_friendly: false
    purpose: "The scheduled, non-emergency recontextualization."
  - name: continuity-check
    sheets: 1
    instrument_guidance: "any-wrapped CLI, per_sheet_fallbacks: [] — verifies pivot.md contradicts no load-bearing fact (facts are predicates, so contradiction is computable, not vibes); contradiction or missing citation → exit 1"
    fallback_friendly: false
    purpose: "The hard gate between pivot and splice."
  - name: re-break-remaining
    sheets: 1
    instrument_guidance: "CONCERT-LEVEL by construction: generates the next movement's score file with the new arc spliced in; completed beats' artifacts re-cited with original digests, never re-run"
    fallback_friendly: false
    purpose: "Retcon, not deletion — reinterpretation with continuity accounting."
dependencies:
  execute-beat: [break-arc]
  pivot-review: [execute-beat]
  continuity-check: [pivot-review]
  re-break-remaining: [continuity-check]
composes_with:
  - pattern: "Season Bible"
    how: "bible carries context; ledger carries constraints with weights"
  - pattern: "Continuity Ledger"
    how: "nearest permanent neighbor (the Newcomer's catch) — Continuity Ledger owns the typed serialized assertion boundary among parallel authors; this owns revision-under-canon across campaign phases; compose the ledger INTO the pivot machinery"
  - pattern: "The Graded Ladder"
    how: "pivot-on-failure composes as the top rung's destination"
  - pattern: "Fork-Evident History"
    how: "versioned arc files (arc.v1.md, arc.v2.md)"
  - pattern: "The Change-Order Ledger"
    how: "nearest engineering kin, fold-refused — the change order executes an authorized delta; the pivot executes an interpretation under canon constraints; distinct data model and checker"
---
```

**Status:** approximation — **concert-level, reframed per the Practitioner's kill of the single-score form:** a running score cannot splice a new arc into its own DAG; the splice is a new score file generated at the pivot boundary and launched through the concert chain or self-chaining. The emergency `on_fail → goto` form stays flagged native-unproven (shared with the Graded Ladder and Transfer of Command — one proof services three patterns).

**Core Dynamic.** Every writers' room knows episodes air in order, feedback arrives mid-season, and long series pivot: a character intended for three episodes becomes the center. The instrument is the **board plus the arc ledger**; a pivot does not discard aired episodes, it **retcons** — reconciles the new frame with everything already on screen, the ledger tracking which established facts are load-bearing (cannot be contradicted) versus negotiable. Retcon is not deletion; it is reinterpretation with continuity accounting — and the accounting is what distinguishes a disciplined pivot from thrash. The iteration-scale face (the folded Kishōtenketsu reframe): a scheduled, non-emergency recontextualization cycle where the reframe sheet has authority to re-scope but **not** to invalidate, and the no-reframe outcome is a valid, logged terminal (C8).

**The Skeptic's two repairs, applied:** canon facts are **enforceable predicates**, not prose — each fact is a typed, checker-computable statement (schema-valid, digest-anchored, referentially complete), so the continuity check is a real join, not a vibe; and citation percentage was never continuity — the check is contradiction-freedom over load-bearing predicates plus complete citation, nothing looser. **The Newcomer's neighbor debt, paid:** Continuity Ledger (`patterns/continuity-ledger.md`) is named and composed — it owns the assertion boundary this pattern's canon ledger instantiates.

**Sentinel.** Plant a pivot.md that silently contradicts one load-bearing fact → continuity-check exits 1, `continuity-report.json` carries `"violations": [{"fact_digest": …, "type": "contradicted"}]`. **Anti-orphan validation:** `file_sha256` over the pre-pivot artifact set proves completed beats unchanged post-pivot — a pivot that orphans completed evidence is thrash wearing continuity's clothes, caught by digest.

**Example.** 20-sheet regulatory-compliance campaign: movements 1–3 map data flows; movement 4 discovers an entire unlogged pipeline, invalidating movements 5–20's decomposition. The pivot ledger re-breaks 5–20 around the discovery; movements 1–3's artifacts become canon facts (load-bearing, digest-anchored) cited by the new plan rather than re-executed at 3× cost.

---

## Facilitator-First Decomposition

```yaml
---
name: "Facilitator-First Decomposition"
scale: score-level
status: working
forces: [Producer-Consumer Mismatch, Instrument-Task Fit]
generators: [Contract at Interfaces]
problem: "Dependency edges are unclassified, so wave-1 artifacts that prepare the environment, wave-2 artifacts that coexist with it, and early commitments that BLOCK later designs all look identical in the DAG."
signals:
  - "two-wave scores: scaffolding before implementation, fixtures before adversarial testing, ground truth before evaluation"
  - "refactor/rebuild work where the first act must be REMOVING an existing commitment"
  - "a premature schema freeze is silently inhibiting the better late design"
stages:
  - name: classify-edges
    sheets: 1
    instrument_guidance: "strong reasoner — every planned dependency declared in edges.yaml: facilitate | tolerate | inhibit; an UNDECLARED edge fails validation (this is the enforcement point)"
    fallback_friendly: false
    purpose: "The three-way classification each dependency edge must declare; undeclared defaults to tolerance, and that assumption is where scores rot."
  - name: wave-1
    sheets: fan_out(N)
    instrument_guidance: "mid-tier instruments; artifacts typed and validated for USABILITY BY WAVE 2, not final quality"
    fallback_friendly: true
    purpose: "Facilitators: environmental modification, not deliverables."
  - name: inhibit-release
    sheets: 1
    instrument_guidance: "custom git CLI instrument, conditional (skip_when: no inhibit edges) — formally retires the blocking artifact (moves schema-v1.yaml to retired/, writes a release receipt); a receipt you can forge with prose is not a receipt"
    fallback_friendly: false
    purpose: "The deliberate, receipted disturbance that releases inhibition."
  - name: wave-2
    sheets: fan_out(M)
    instrument_guidance: "mixed by risk class; prelude-injected with wave-1 artifacts per the manifest"
    fallback_friendly: true
    purpose: "The tolerant main body, establishing on prepared soil."
dependencies:
  wave-1: [classify-edges]
  inhibit-release: [wave-1]
  wave-2: [inhibit-release]
composes_with:
  - pattern: "Keystone-First Sequencing"
    how: "shares the wave-1 discipline; keystone output is the point, facilitator output is the soil — fold refused at collision, different decision authority"
  - pattern: "The Attested Merge Gate"
    how: "receipts feed it"
  - pattern: "The Change-Order Ledger"
    how: "a release receipt is an authorization-shaped mutation, recorded"
---
```

**Status:** working · primitives-proven (alongside Keystone-First, the prove path's easiest new pair). **Repair applied (the Skeptic's polarity catch, same as Watchman's Gate):** the inhibit-release gate's `skip_when` is now the *refusal* predicate — it succeeds (skips the blocked sheet) when the release receipt is absent or invalid; the draft's form proceeded on checker failure. **Limitation stated honestly (also the Skeptic's):** edge labels constrain *gating and injection* (which sheets run, what their preludes carry) — they are not runtime semantics the engine enforces; the audit enforces consumption (`grep` check that no `retired/` file was read after retirement, exit code named).

**Core Dynamic.** Connell–Slatyer succession has three models, and pass 1's dual-enumeration generator had one: *tolerance* — independent agents colonize in parallel, coexistence settled downstream. **Facilitation**: wave-1 sheets' artifacts are *environmental modification* — test fixtures, stubs, adversarial examples, data schemas — preparing soil so wave-2 establishes at higher probability; the quality bar is usability, not brilliance. **Inhibition** — the dark third: early occupants hold space and block latecomers until disturbed. The orchestration reading: early commitments (a premature schema freeze, a keystone artifact churned into a contract) *inhibit* later better designs; the disturbance that releases inhibition is a deliberate, receipted decommitment step. Facilitation theater is the failure mode: a wave-1 fixture set nothing tests against is discard, and the score paid for the fiction.

**Example.** Legacy-system modernization: wave 1 builds the strangler-fig scaffolding (routing shims, characterization tests around the legacy module); the inhibition-release step formally retires the legacy interface contract; wave 2 rebuilds each module. Without classification, teams run wave 2 against interfaces wave 1 silently locked in place — inhibition by accident.

---

## The Inspection and Redline Stakes

```yaml
---
name: "The Inspection and Redline Stakes"
scale: concert-level
status: working
forces: [Partial Failure, Exponential Defect Cost]
generators: [Threshold-Triggered Switch]
problem: "'All upstream fully green' (the engine's only fleet dependency semantics, V3) is stricter than downstream work often needs, so partial evidence is either silently starved or silently consumed."
signals:
  - "multi-score workflows where downstream wants to begin on partial upstream evidence"
  - "crawl-then-summarize, migration-then-verification chains"
  - "starved groups are logged as a warning and moved on (fleet.py:314-319) — and nobody surfaces it"
stages:
  - name: upstream-fleet
    sheets: fan_out(N)
    instrument_guidance: "member scores of group A; each writes receipt-{member}.json (digest + status)"
    fallback_friendly: true
    purpose: "Produce receipts; arrival is asynchronous."
  - name: admit
    sheets: 1
    instrument_guidance: "any-wrapped CLI, per_sheet_fallbacks: [] — jq over the receipt set vs the AUTHORING-TIME tolerance.yaml (required receipts, per-receipt digest expectations, degrade policy, AND a readiness deadline); bounded by max_wall_seconds; emits admission.json: FULL, PARTIAL (with skip list), or HALT"
    fallback_friendly: false
    purpose: "The downstream score's first breath: stakes driven before the concrete truck arrives."
  - name: body
    sheets: fan_out(M)
    instrument_guidance: "downstream sheets 2+; per-sheet skip_when is the refusal predicate consulting admission.json's skip list"
    fallback_friendly: true
    purpose: "Work on what was admitted; skip-listed work is visibly absent, not silently missing."
dependencies:
  admit: [upstream-fleet]
  body: [admit]
composes_with:
  - pattern: "Admission by First Cycle"
    how: "pass-1 pattern DEMOTED after V3 — this is its honest successor; the permanent corpus's DAG edge is rewritten"
  - pattern: "Fleet Receipt Ledger"
    how: "the ledger owns bijection accounting; this owns tolerance-declared partial admission"
  - pattern: "The Validity Window"
    how: "receipt TTLs are the stakes' expiry dates"
  - pattern: "The Dispatch Catalogue (MEL)"
    how: "different questions, different table owners: MEL = may WE run degraded (ex-ante authorization); CDL = can the margins absorb the sum (economics); Stakes = what may DOWNSTREAM consume (partial admission across the boundary)"
---
```

**Status:** working · primitives-proven (artifact gates); the fleet face rides the `fleet` proof debt. Ranked #19 by the collision; the Practitioner called it "superb," the Newcomer "demotion done right" and ranked it top-tier.

**Core Dynamic.** The inspector does not write prose reports; they *redline the artifact itself* — deviations marked on the drawing, bound to the exact location they correct — and the tolerance stakes are driven into the ground *before* the concrete truck arrives, so acceptance is observable by anyone, not adjudicated at pour time. Two load-bearing ideas: deviation expressed **against** the artifact, not about it; tolerance **physical and pre-placed**. V3's refutation made this pattern necessary: `fleet.depends_on` waits on full successful completion (fleet.py:337-360), so "admission by first cycle" is dead — but the need it served is real. The honest replacement: the dependent score's admission condition is a **staked tolerance file** — written at authorship, checked by the downstream score's OWN first sheet, degrading explicitly: partial receipt sets produce a visible, receipted **"admitted-with-redlines"** state listing what is missing, never a silent AND-starvation.

**The race, fixed (the Skeptic's):** absent fleet dependencies, admit could run before optional receipts arrive and call temporary absence a legitimate PARTIAL. Now `tolerance.yaml` declares a **readiness deadline**: absence is not legible as PARTIAL until the deadline passes — missing-vs-not-yet is a typed transition with a timestamp, and admit is bounded by `max_wall_seconds` so the deadline is real.

**Sentinels.** Full fixture set → FULL. Seeded missing receipt after deadline → PARTIAL with the right skip list. **The failure-class distinction:** corrupt one receipt's *digest* → admit must emit HALT, not PARTIAL — a digest mismatch is tampering, not absence; different failure class, different verdict. And the stakes written by the upstream producer die on contact — stakes set by the grading crew are not inspection, they're ambition.

**Example.** Market-research concert: 8 regional crawl scores write receipts; the synthesis score's tolerance declares 5 critical regions + 3 nice-to-have; two crawls fail → admission is PARTIAL, synthesis runs with the two regions marked data-absent in its output's caveats, and the concert log carries the redline — anyone reading knows exactly what the synthesis did not see.

---

# GROUP V — INSTRUMENT-STRATEGY

---

## The Continuous Pour Schedule

```yaml
---
name: "The Continuous Pour Schedule"
scale: instrument-strategy
status: approximation
forces: [Finite Resources, Partial Failure]
generators: [Gate on Environmental Readiness]
problem: "A homogeneous fan-out against a rate-limited vendor hits the limit mid-wave, and the interruption (a cold joint) leaves partial generation of inconsistent vintage."
signals:
  - "bulk generation where 'how fast we can dispatch' hits 'how fast the vendor can absorb'"
  - "a mid-wave 429 would leave half a wave at one vintage and half at another"
  - "the run's own rate-limit receipts show interruptions nobody planned for"
stages:
  - name: pour-plan
    sheets: 1
    instrument_guidance: "any-wrapped CLI, per_sheet_fallbacks: [] — computes zones → waves from the work manifest; per-instrument concurrency and DOCUMENTED rate limits are authoring-time inputs (a score cannot derive vendor limits from an alias declaration)"
    fallback_friendly: false
    purpose: "The supply-continuity plan; writes pour-plan.yaml (wave assignments, per-wave stagger, joint plan)."
  - name: wave-N
    sheets: fan_out(K) per wave
    instrument_guidance: "work instruments; stagger_delay_ms matched to the vendor's documented rate limit — same-instrument spacing (V4)"
    fallback_friendly: true
    purpose: "Dependency-ordered waves; each wave bonds to its predecessor's prepared joint."
  - name: wave-N-joint
    sheets: 1 per wave
    instrument_guidance: "any-wrapped CLI — the SINGLE NAMED WRITER of joints.jsonl: wave id, members, output digests"
    fallback_friendly: false
    purpose: "The planned joint: a prepared, keyed, doweled surface — the DAG position serializes the write."
  - name: cure-audit
    sheets: 1
    instrument_guidance: "any-wrapped CLI, per_sheet_fallbacks: [] — every planned joint has a receipt, no wave launched before its joint predecessor's receipt existed"
    fallback_friendly: false
    purpose: "Cold-joint detection is the absence of a receipt at a wave boundary."
dependencies:
  wave-1: [pour-plan]
  wave-1-joint: [wave-1]
  wave-2: [wave-1-joint]
  cure-audit: [wave-N-joint]
composes_with:
  - pattern: "The Rostered Watch"
    how: "stagger claim corrected (V4) — this pattern carries the corrected doctrine; the watch bill's wave/handoff half survives on dependency ordering"
  - pattern: "The Watch Rollover"
    how: "the joint receipt is a watch-boundary pass-down specialized to wave seams"
  - pattern: "Circuit Breaker"
    how: "a wave's cold joint is the trip condition at fan-out granularity"
  - pattern: "Firing the Pass"
    how: "clock-arithmetic cousin at the pass (permanent-corpus side)"
---
```

**Status:** approximation — `stagger_delay_ms` native-unproven (V4 semantics: per-instrument spacing); one minimal verification score serves this pattern and the benched Ramp Meter's shared flag. Differentiation from Rostered Watch/Watch Rollover stated: those own the watch bill and handover; this owns *supply continuity under a rate limit* — paced dispatch plus joint receipts.

**Core Dynamic.** A mat pour fails not because the concrete is bad but because the trucks stopped coming: an interruption mid-pour creates a **cold joint** — fresh against partially hardened — a structural defect, not a cosmetic one. So the plan is a *supply-continuity plan*: zoned pours in deliberate sequence, guaranteed truck spacing, pour rate matched to crew capacity — and where the pour must stop, *planned* construction joints (prepared, keyed, doweled surfaces) instead of accidental ones. The V4-corrected core: `stagger_delay_ms` is a **same-instrument spacing rule** (dispatch.py:65-66) — exactly a truck-spacing rule for one batching plant. Mixed-instrument fan-outs have as many independent pour sequences as instruments; with `select: balance` on a multi-vendor alias, balance spreads across plants while stagger spaces each plant's trucks — they compose.

**Repairs applied (the Skeptic's two):** joint receipts have a **single named writer** — each wave ends in its own `wave-N-joint` CLI sheet that writes the receipt after the wave's members complete; "last-completing sheet appends" was not an owner and invited concurrent writes. And the alias-derived rate-limit claim is **cut**: documented limits are an authoring-time input to `pour-plan`; the score cannot read a vendor's mind. The stagger negative control is honest about its own limits: set stagger 0 against a venue with a *documented* rate limit and the run's own 429 receipts must show the cold joint; *if the venue has no rate limit, the negative control is untestable there and the pattern says so* — a negative control you cannot run is a confession, not a control.

**Example.** 500-document summarization fan-out against one vendor alias: pour-plan splits 25/wave with stagger 1500ms (tier allows 20 rpm); wave 3 loses two members to a vendor incident → the joint receipt records the gap → wave 4's prompts carry the gap notice (the keyed surface) → cure-audit names the two missing documents in the final report instead of the summary silently covering 498.

---

# Candidates Bench (post-review)

Every bench entry carries its reason and its re-entry condition. Attack these first at prove.

- **The Phased Quorum Wave** (redesign of the cut Staggered Quorum Spend; the Practitioner's rewrite) — sequential waves: launch k, quorum-check, launch N−k only on failure. Re-enters when a prove sheet exercises a two-wave quorum gate. The original's economic claim (staggering saves spend) was an illusion: all N members launch and bill regardless (the Skeptic's arithmetic, the Practitioner's verdict).
- **The Recovery Arc** — benched per the Practitioner (unwired `checkpoint_persistence`, dynamic DAG re-entry) and the Skeptic (`file_modified` proves a timestamp changed, not correct re-entry). Now names **The Checkpoint Re-Anchor** (pass-1 review candidate, archive:1316) as its nearest prior — re-derive together when the primitive lands. The marks doctrine (validated intermediate states, cheap sha256 marks) survives as composition guidance inside Serial Troponin and the Mock-Up Bay.
- **The Standing Order** (Expedition 4; nursing pre-delegated authority) — first alternate; composes through Hold-Point Witness + Graded Ladder. Re-enter when the pause seam lands.
- **The Worst-Case Envelope** (Expedition 4; ETOPS) — position-bound worst-case certification; benched on primitive coverage. Its correlation caveat (same-batch engines defeat the independence assumption) feeds the Independence Law and CDL's co-pricing rule.
- **The Ramp Meter** (Expedition 3) — the Continuous Pour's capacity-measuring sibling; one proof serves both; fold-test at prove.
- **The Command-Span Law** (Expedition 4; ICS 3–7 span) — Concurrent Count promoted to a bound-carrying gate; file as law, not pattern — curate path.
- **The Severity Gate, The Computed Signature, Fighting the Last War** (Expedition 5) — all ride `failure_history` verification; queued behind the Contamination Wire's transport proof. The Severity Gate's dosage doctrine and the Computed Signature's `sha256(code || digest || sheet)` bitwise identity are owed promotion the moment the channel is proven; Fighting the Last War's intent-freeze composes into the Hotwash pair now, standalone later.
- **The Authorless Argument** (Expedition 6) — its digest-anchored register lint (VERBATIM vs INFERENCE) is a validation idiom that belongs *inside* synthesis patterns (Sugya Weave, Shared Reference fan-ins); the POISONED fourth register composes into the Contamination Wire today.
- **The Seminar** (Expedition 6) — natural consumer once the Dialectical Pair and Editor's Disposition proofs land.
- **Feeding-Ratio Maintenance** (Expedition 2) — fold-test at curate against Back-Slopping's family.
- **Trading Fours** (Expedition 3) — where coordination serves *expression*, the grammar thins; recorded, not claimed.

**Folds into the permanent corpus executed this pass:** Monotone Test Ordering → Serial Troponin (ecological fingerprint annexed, with the loop-exit discipline `verdict: inconclusive, exit_reason: max_iterations`). Kishōtenketsu Reframe → the Midseason Pivot Ledger's iteration-scale face. Shared Pulse + Datum Grid → **The Shared Reference** (this pass, two profiles).

---

# Confirmations in the permanent corpus (pass 2 evidence, no new entries)

- **Firing the Pass** — the draft's hard duplication failure, now recorded correctly: proven in iteration 5 (`proof-scores/firing-the-pass.yaml`, "THE NIGHT DISPATCH," 191 KB, 2026-09-04, revised against three adversarial reviews). Pass 2's contribution is the *correction*: the existing proof never touched `stagger_delay_ms`, so the pattern's heterogeneous-offset clock half remains unproven — a named gap for the prove path, not a new pattern. The draft's Expedition-3 re-derivation is a fingerprint confirmation (expeditor doctrine), recorded against the existing entry.
- **Serial Troponin** — ecologically re-derived (sourdough serial feeding, adaptive-management triggers) *and* extended: the loop-exit discipline (`verdict: inconclusive, exit_reason: max_iterations` — never fabricate `rising`) is new doctrine on the pass-1 spine; its `sheet.loops` proof debt is now shared by four more consumers.
- **Readback Before Commit** — pass 2 supplies its arming-schedule family (Cue Light, Hold-Point Witness, Mock-Up Bay) and its placement law (Watchman's Gate, V1-cited).
- **The Validity Window** — three new consumers (dispatch-permit expiry in MEL, holding-expiry at the pass, lesson TTLs in Checkout); the MEL row is a validity window *with a compensation payload*.
- **Capability Census** — the MEL gate is its consumer (census measures, catalogue authorizes); the Ramp Meter is its forward-looking sibling.
- **Graded Ladder** — carrier corrected (V2): the challenge counter rides a receipt file via `on_fail: run`, not a status API.
- **Rostered Watch** — stagger claim corrected (V4): stagger is per-instrument spacing; the Continuous Pour Schedule carries the corrected doctrine; the wave/handoff half survives unchanged.
- **Standby–GO** — the Cue Light is its confirmation + extension (cycle freshness, broadcast-polled semantics, non-blocking consumers); the pattern file's composes_with now points back.
- **Dead Letter Quarantine, Sealed Dissent, Negative Ledger, Fleet Receipt Ledger, Non-Waiting Hand, Continuity Ledger, After-Action Review** — each gained named composition edges; none re-derived.

---

# Pattern × Primitive × Proof-Status Table (re-issued, with proof-score cross-references)

Proof-status vocabulary per the Skeptic's split: **primitives-proven** (every load-bearing primitive exercised somewhere) / **approximation** (composes today; one named behavior unverified) / **aspirational** (blocked on an unwired primitive — none remain in the 21; the two blocked candidates are benched). "Pattern-unproven" applies to every row: no pass-2 pattern has an executed end-to-end proof; the table names which primitive each proof must exercise.

| Pattern | Load-bearing primitive | Status | Proving / exercising score on disk |
|---|---|---|---|
| The Cue Light | per-file acks, CLI count gate, refusal `skip_when` | primitives-proven | none for the composition; Standby–GO's arm/fire machinery is native (`standby-go.md`, no dedicated proof file) |
| The Contamination Wire | typed verdict artifacts, prelude injection | primitives-proven | `the-attested-merge-gate.yaml`, `prefabrication.yaml` (typed gates, preludes) |
| The Shared Reference | digests, citations, fan-out, `field_match` | primitives-proven | `prefabrication.yaml` (frozen contract), `source-triangulation.yaml` (typed citations) |
| The Change-Order Ledger | isolated outputs, chain-walk, file facts (V6) | primitives-proven | `the-precedent-bench.yaml` (append-only canon) |
| Unison Drift | fan-out, `capture_files`, `file_sha256`, CLI differ | primitives-proven | first proof of the pass — none yet; every primitive exercised across the estate |
| The Dialectical Pair | `response_format` typed moves | approximation | none — tied minimal exercise with Editor's Disposition (V5: schema-validated, zero executions) |
| The Torque-Verify Pass | `response_format` (V5) + CLI predicates + bijection | primitives-proven | `first-article` machinery in `the-unprimed-falsifier.yaml` (reader arms) |
| The Dispatch Catalogue (MEL) | static table, jq join, expiry arithmetic | primitives-proven | `negative-treatment-watch.yaml` (cost/limits, the only score mentioning cost limits) |
| The Priced Verification Ladder | budget ledger + `skip_when` envelope | approximation | none — sentinel pair unexecuted; descent is doctrine until run |
| Dispatch with Declared Penalty | census + jq aggregate gate | primitives-proven | none for the aggregate; jq gates everywhere |
| The Hotwash Dispatch | failure transport (unproven) + CLI routing | approximation | none — `failure_history` zero executions corpus-wide |
| The Spent Lesson Checkout | engine-record verification (path/schema owed) | approximation | none |
| Keystone-First Sequencing | dependencies + `prelude` + version echo | primitives-proven | `prefabrication.yaml`, `cathedral-construction.yaml` (foundation-first forms) |
| The Watchman's Gate | typed declaration (V5) + CLI gate + refusal `skip_when` (V1) | primitives-proven | none for the gate composition; seam verified V1/V5 |
| The Hold-Point Witness | `pause: true` (flow.py:100-102), `pause_before_chain` (orchestration.py:316-323) | approximation | none — pause seam untouched by all 18 scores |
| The Editor's Disposition | `response_format` closed enum | approximation | none — THE minimal exercise (prove queue #1) |
| The Mock-Up Bay | `sheet.loops` count+until (V6) | approximation | `cathedral-construction.yaml` used fixed counts only; no `until`-terminated loop exists |
| The Midseason Pivot Ledger | canon predicates + digest anti-orphan + concert splice | approximation | none; `sheet.triggers` on_fail→goto unproven |
| Facilitator-First Decomposition | `edges.yaml` + receipt gates | primitives-proven | none for the classification; gates ordinary |
| The Inspection and Redline Stakes | artifact gates across fleet boundary + deadline | primitives-proven | none; `fleet` flag zero executions corpus-wide |
| The Continuous Pour Schedule | `stagger_delay_ms` (V4) + joint receipts | approximation | none — zero `stagger_delay_ms` occurrences in all 18 scores (including `firing-the-pass.yaml`) |

**Zero executions, corpus-wide (all 18 proof scores):** `response_format`, `sheet.loops` (until-terminated), `failure_history`, `stagger_delay_ms`, `sheet.triggers`, `fleet`, the pause seam. The prove queue exists because this column is empty.

---

# Selection Table (the Newcomer's missing entry point — "what breaks if this is absent?")

| If your problem is… | Start with | What breaks if absent |
|---|---|---|
| A late decision must stall commits, not work | **The Cue Light** | Either everything blocks on the decider, or work commits un-vetted |
| Contamination found after consumers started | **The Contamination Wire** | Consumers build on poison or halt en masse with no routing |
| N workers must agree on terms, not content | **The Shared Reference** | Merge drowns in normalization debt; tampering is silent |
| The plan changes mid-run | **The Change-Order Ledger** | Sheets execute a plan that no longer exists |
| About to spend on a big fan-out, untested | **Unison Drift** | Prompt underspecification replicates at N× cost |
| One contested judgment, one blind spot | **The Dialectical Pair** | Position-holding by silence; no record of what was contested |
| Schema-valid garbage looks exactly like truth | **The Torque-Verify Pass** | Systematic defects pass every schema |
| "Skip it this run" is decided ad hoc | **The Dispatch Catalogue (MEL)** | Degradation without authorization, compensation, or expiry |
| Verification cost compounds unbounded | **The Priced Verification Ladder** | The run dies of its own review bill, or degrades silently |
| Small deviations sum past a margin | **Dispatch with Declared Penalty** | Individually-fine jointly-fatal dispatch |
| Failure evidence dispatches into the void | **The Hotwash Dispatch** | Lessons carried with no consumer; context noise |
| Old lessons train new attempts to dodge ghosts | **The Spent Lesson Checkout** | Context debt compounds forever |
| A small artifact parameterizes everything | **Keystone-First Sequencing** | The whole cascade works under wrong conditions |
| An AI seam touches something irreversible | **The Watchman's Gate** | A fail-open predicate admits unvetted destruction |
| A seam only an external authority may open | **The Hold-Point Witness** | Rubber-stamp or deadlock |
| Many advisories, one required action | **The Editor's Disposition** | Advice-drowning or advice-collapse |
| Volume production gated on a first article | **The Mock-Up Bay** (newcomer's first score) | Detail defects replicate across the volume |
| A long campaign's plan is a hypothesis | **The Midseason Pivot Ledger** | Pivots orphan completed evidence or freeze the plan |
| Wave-1 output is soil, not deliverable | **Facilitator-First Decomposition** | Early commitments silently inhibit better designs |
| Downstream needs partial upstream truth | **The Inspection and Redline Stakes** | All-or-nothing starvation or silent partial consumption |
| A vendor rate limit mid-wave is a cold joint | **The Continuous Pour Schedule** | Inconsistent vintage; 429 receipts nobody planned |

---

# Reconciliation Appendix (the Newcomer's demand: every draft entry → its disposition and permanent neighbors)

| Draft entry (04-draft-corpus.md) | Disposition | Permanent-corpus neighbor touched |
|---|---|---|
| The Cue Light | kept, rewritten | Standby–GO (confirmation + extension) |
| The Contamination Wire | kept, rewritten off `failure_history` | Dead Letter Quarantine, Readback Before Commit; repairs The Poisoned-Artifact Advisory's demotion |
| The Shared Pulse | folded → The Shared Reference | The Misclosure Ledger (closure), Serial Troponin (bar) |
| The Datum Grid | folded → The Shared Reference | Prefabrication (contract page) |
| The Change-Order Ledger | kept, repaired | Negative Ledger, Configuration Control Board |
| Unison Drift | kept, strengthened | Rashomon Gate (routing rule) |
| The Dialectical Pair | kept, unrolled | Rejoinder Ledger (bijection) |
| Firing the Pass | **EVICTED → confirmation** | Firing the Pass itself (`firing-the-pass.yaml`, proof since Sep 4) |
| The Torque-Verify Pass | kept, invariant stated | First Article Characterization, Immune Cascade |
| The Dispatch Catalogue (MEL) | kept, ex-ante fixed | Capability Census, The Validity Window |
| The Priced Verification Ladder | kept (approximation) | Immune Cascade (tier skeleton), Echelon Repair |
| Dispatch with Declared Penalty | kept, algebra added | Capability Census, Rent-Then-Commit |
| The Recovery Arc | **CUT to bench** | The Checkpoint Re-Anchor (pass-1 candidate, named) |
| Hotwash Dispatch & Spent Lesson Checkout | **SPLIT** into two patterns | After-Action Review (capture-side neighbor, named) |
| Keystone-First Sequencing | kept over fold objection | Cathedral Construction, Prefabrication (differentiation stated) |
| The Watchman's Gate | kept, polarity FIXED | Readback Before Commit (placement law) |
| The Hold-Point Witness | kept, trust model stated | Transfer of Command at the Seam |
| The Editor's Disposition | kept (approximation) | Rejoinder Ledger, Condorcet's Premise (decision-table row) |
| The Mock-Up Bay | kept, reduced to minimal loop | Serial Troponin (co-first loop proof), The Unprimed Falsifier |
| The Midseason Pivot Ledger | kept, concert-level reframe | Season Bible, **Continuity Ledger** (named), Canon of Phases |
| Facilitator-First Decomposition | kept, polarity fixed | dual-enumeration family (completes it) |
| The Inspection and Redline Stakes | kept, deadline added | Admission by First Cycle (successor), Fleet Receipt Ledger |
| Staggered Quorum Spend | **CUT to bench** (Phased Quorum Wave) | Quorum Consensus / Quorum Trigger (spend-side, benched) |
| The Continuous Pour Schedule | kept, single-writer joints | Rostered Watch (corrected), Watch Rollover |

**Corpus-law candidates promoted to the curate path (unchanged by reviews):** The Independence Law (C3); The Typed-Draw Law (C8); The Placement Law (C10, now with the skip_when polarity clause); The No-Inheritance Gate (C2's negative image — `per_sheet_fallbacks: []` on every deterministic gate).

---

# Proof-Order Handoff (to the prove path — revised by the reviews)

1. **`response_format` end-to-end** — Editor's Disposition or Dialectical Pair (tied minimal exercises). V5 confirms schema validation per attempt; the proof executes it. **Constraint (the Newcomer's):** no new proofs of already-proven primitive sets — the fan-out→digest→join spine is proven ~8 times; do not make it 9.
2. **The pause seam** — Hold-Point Witness; `PAUSED_AT_CHAIN` and `pause: true` cited at file:line; includes the notify step and the stale-disposition rejection.
3. **`sheet.loops` with `until`** — Mock-Up Bay (the newcomer's first score) or Serial Troponin; V6 confirms the grammar and its E999 fail-closed edge. `cathedral-construction.yaml` used fixed counts only.
4. **`failure_history` transport semantics** — lookback window, code-vs-prose content, retried-then-succeeded behavior; the Contamination Wire's flagged extension, the Hotwash Dispatch, and three benched siblings queue behind it.
5. **Unison Drift** — the cheapest fully-proven-primitives new proof; first overall on pure cost.
6. **The `stagger_delay_ms` gap in Firing the Pass** — the existing proof never touched the clock half (the Newcomer's finding); the same minimal score serves the Continuous Pour Schedule and the benched Ramp Meter.
7. **Repair the six failing proof files before extending** — `dead-letter-quarantine.yaml`, `echelon-repair.yaml`, `immune-cascade.yaml`, `prefabrication.yaml`, `shipyard-sequence.yaml`, `source-triangulation.yaml` all fail `mzt validate` (V002, workspace parent missing); the prove path should not build on files that fail validation — keystone-first in miniature.
8. **Pin V2's citation** — the engine-evidence table's one un-cited row; one file:line look during proof #2's source pass.

---

*The map after this pass: 21 surviving patterns (24 drafted − 1 evicted as duplication − 2 cut to bench − 1 fold − 1 split into two), 4 law candidates, 1 demotion repaired, 2 corrections to the permanent corpus (Rostered Watch's stagger claim; Standby–GO's back-pointer), 6 engine citations as corpus property, one corpus-wide polarity law, one concurrency doctrine, and a bench with reasons and re-entry conditions. Every pattern carries a score structure in the engine's real dialect, a negative control with a named sentinel, its proof status on its face — and the status now means one thing instead of five. Down. Forward. Through.*
