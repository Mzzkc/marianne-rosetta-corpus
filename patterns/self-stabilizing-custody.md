---
name: Self-Stabilizing Custody
scale: adaptation
status: working
forces:
- Partial Failure
- Convergence Imperative
generators:
- Exploit Failure as Signal
- Contract at Interfaces
problem: Crash, corruption, and restart are treated as exceptional events requiring an exceptional recovery protocol, when they are just arbitrary states the ordinary rules should leave.
signals:
- conductor restarts mid-concert; workspaces resumed after host failure
- global rollback costs more than local re-derivation
- recovery from PARTIALLY corrupt state — where checkpoint-restore fails
stages:
- name: predicates
  sheets: 1
  instrument_guidance: any-wrapped CLI profile — each sheet's completion claim is script-checkable from disk
  fallback_friendly: false
  purpose: 'Define legitimacy: output artifact exists, digest matches journal, no later entry supersedes it.'
  artifacts: []
- name: local-correction
  sheets: 1
  instrument_guidance: claude-code or codex-cli — the recovered sheets themselves — each re-derives ONLY its own legitimacy
  fallback_friendly: true
  purpose: Re-run if illegitimate; never reset a sibling.
  artifacts: []
- name: closure
  sheets: 1
  instrument_guidance: any-wrapped CLI profile — fan-in proceeds only over legitimately-done predecessors
  fallback_friendly: false
  purpose: 'Verify closure: every predecessor legitimate or visibly skipped.'
  artifacts: []
dependencies:
  local-correction:
  - predicates
  closure:
  - local-correction
composes_with:
- pattern: The Fencing Token
  how: layering — MANDATORY wherever side effects exist; bounds the convergence window's misbehavior
- pattern: The Black-Box Ledger
  how: prerequisite — the journal legitimacy predicates read
- pattern: Behavioral Pre-Mortem
  how: substitution — the kill-injection probe is the pre-mortem's runtime twin
type: orchestration-pattern
---

## Self-Stabilizing Custody


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

### Review Integration

Review 2 required monotone local correction, kill-injection convergence tests, and mandatory Fencing Token composition wherever side effects exist. During split curation, the monolith's G1–G6 draft label was mapped to the nearest generator in forces.md, and every stage now names a current profile: deterministic stages use an any-wrapped CLI profile; judgment stages name claude-code, codex-cli, or opencode as appropriate.
