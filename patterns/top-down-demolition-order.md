---
name: "Top-Down Demolition Order"
scale: score-level
type: orchestration-pattern
status: working
forces:
  - "Exponential Defect Cost"
  - "Partial Failure"
generators:
  - "Gate on Environmental Readiness"
problem: "Removal order is computed from commit history, so removing a shared thing succeeds while dependents that quietly stood on it lose their footing."
signals:
  - "retiring a shared library, column, endpoint, schema, or base image"
  - "the danger is not 'removal fails' but 'removal succeeds and three consumers break silently'"
  - "reverse-chronology undo proposed for something with internal structure"
config_features:
  - "concert"
  - "on_success"
  - "skip_when"
  - "instrument: cli"
stages:
  - name: map-structure
    sheets: 1
    instrument_guidance: "instrument: cli — computes the live reverse-dependency graph"
    fallback_friendly: false
    purpose: "Emit demolition-plan.json: ordered steps, each with a consumers-must-be-empty predicate."
    artifacts: ["demolition-plan.json"]
  - name: verify-order
    sheets: 1
    instrument_guidance: "instrument: cli in separately-authored verify/ dir — re-derives the order independently"
    fallback_friendly: false
    purpose: "Second, differently-authored derivation must equal the plan."
    artifacts: ["order-verified.stamp"]
  - name: remove-step
    sheets: 1
    instrument_guidance: "instrument: cli wrapper — sweep empty, remove, re-derive leaves, ledger append; one step per self-chain cycle"
    fallback_friendly: false
    purpose: "Remove exactly one current leaf; the sweep re-runs after because removals create new leaves."
    artifacts: ["demolition-ledger.jsonl"]
  - name: final-void
    sheets: 1
    instrument_guidance: "instrument: cli — absence proven by the full oracle"
    fallback_friendly: false
    purpose: "Artifact gone AND the full build/test oracle green."
    artifacts: []
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

## Top-Down Demolition Order

`Status: Working` · **Source:** iteration 6 (Expedition 1 — engineered cutting sequences). **Scale:** score-level. **Forces:** Exponential Defect Cost, Partial Failure. **The strongest pattern of iteration 6 by all three reviews.**

### Core Dynamic

**The assembly DAG read backwards is not a valid disassembly DAG.** When the ship was built, temporary staging carried loads that no longer exist; when the building was poured, formwork carried the slabs until the concrete cured. The completed structure bears weight through paths that did not exist during assembly. Demolition engineers do not replay the build in reverse — they compute a *new* order in which the remaining structure is self-stable at every step.

The Marianne translation: **removal order is computed from reverse dependencies, not from commit history.** Saga Compensation undoes by time (correct for restoring business state); demolition removes by structure — you may not remove a thing while anything live still stands on it. Before each removal, a deterministic sweep enumerates the element's consumers; removal proceeds only when that set is empty; the sweep re-runs after every removal because removals create new leaves. This is the enumerate-ALL-consumers law promoted from discipline to mechanism.

The serialized driver: one removal per self-chain cycle — the score re-invokes itself via `concert`/`on_success`; movement 3's sheet is skipped when the ledger shows no remaining steps, so the chain drains the plan and terminates. Parallel removals would race the stability computation; serialization is the safety property. The plan and ledger are JSON checked by jq, never prose greps; the order re-derivation lives in a separately-authored `verify/` directory (Concurrent Count's discipline applied to structure); only the full suite is green at the end.

### When to Use / When NOT to Use

Use: retiring anything where the danger is not "removing it fails" but "removing it *succeeds* and dependents you didn't enumerate quietly lose their footing" — shared libraries, columns, endpoints, message schemas, base images.

Not: the artifact has no internal structure (removal order is ceremony); the reverse-dependency graph cannot be computed deterministically (dynamic dispatch everywhere — the honest answer is a soak period, not a fake sweep).

### Marianne Score Structure

```yaml
concert:
  enabled: true
  max_chain_depth: 40             # bound: one cycle per step plus commissioning
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
    1: { command: 'test -s {workspace}/demolition-plan.json' }
    2: { command: 'test -s {workspace}/order-verified.stamp' }
    3: { command: 'test $(jq ".steps | map(select(.state != \"done\")) | length" {workspace}/demolition-plan.json) -eq 0' }
    4: { command: 'test $(jq ".steps | map(select(.state != \"done\")) | length" {workspace}/demolition-plan.json) -gt 0' }
  per_sheet_fallbacks: { 1: [], 2: [], 3: [], 4: [] }
prompt:
  template: |
    {% if stage == 1 %}
    bash "{score_dir}/scripts/dep-graph.sh" --target "{{ target_path }}" --emit "{{ workspace }}/demolition-plan.json"
    {% elif stage == 2 %}
    bash "{score_dir}/verify/order-rederive.sh" --target "{{ target_path }}" \
      --diff-against "{{ workspace }}/demolition-plan.json" && touch "{{ workspace }}/order-verified.stamp"
    {% elif stage == 3 %}
    bash "{score_dir}/scripts/step.sh" --plan "{{ workspace }}/demolition-plan.json" \
      --sweep-expect-empty --ledger "{{ workspace }}/demolition-ledger.jsonl"
    {% else %}
    bash "{score_dir}/scripts/full-oracle.sh" "{{ workspace }}"
    {% endif %}
validations:
  - type: command_succeeds
    command: 'jq -e ".steps | length > 0" {workspace}/demolition-plan.json'
    condition: "stage == 1"
  - type: command_succeeds
    command: 'bash {score_dir}/scripts/step.sh --self-test'
    condition: "stage == 3"
  - type: command_succeeds
    command: 'bash {score_dir}/scripts/full-oracle.sh {workspace}'
    condition: "stage == 4"
```

Step self-test: a fixture where a live consumer exists and removal must refuse.

### Example

Deprecating a shared `user-events` topic schema that fourteen services publish to and nine consume. Commit order says the schema came before its consumers, so newest-first would kill the schema first. The demolition order computes: migrate publishers first (no dependents), then consumers, then the topic. Every step leaves the running system self-stable.

### Review Integration

Iteration 6: all three reviews ranked it strongest; Review 1's strengthening — a serialized driver (the real `concert`/`on_success` self-chain form, one step per cycle), a graph schema, JSON-not-prose gates, and a sandboxed negative fixture — is implemented. The draft's placeholder `execute-removal` command inside a non-CLI movement is gone: every removal action is a CLI wrapper.
