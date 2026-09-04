---
name: "Demobilization Checkout"
scale: concert-level
type: orchestration-pattern
status: working
forces:
  - "Partial Failure"
  - "Finite Resources"
generators:
  - "Exploit Failure as Signal"
problem: "Concerts end by stopping being visible, leaving orphaned processes, live leases firing into dead workspaces, and credentials outliving their purpose."
signals:
  - "a campaign with physical footprint: daemons, leases, clones, containers, credentials"
  - "retirement has no owner; archival is the only ending ritual"
  - "'the run ended' treated as if it meant 'the run failed'"
config_features:
  - "on_success"
  - "instrument: cli"
stages:
  - name: census
    sheets: 1
    instrument_guidance: "instrument: cli — fresh enumeration at demob; the WRITE-TIME ledger is its pre-history"
    fallback_friendly: false
    purpose: "Emit census.jsonl of everything with a footprint."
    artifacts: ["census.jsonl"]
  - name: dispositions
    sheets: 1
    instrument_guidance: "any — one disposition row per resource id, in a SEPARATE table"
    fallback_friendly: true
    purpose: "archive | release | retain-and-why, per census id."
    artifacts: ["dispositions.jsonl"]
  - name: act
    sheets: 1
    instrument_guidance: "instrument: cli — executes dispositions; Gas-Free discipline where destructive"
    fallback_friendly: false
    purpose: "Emit receipts.jsonl; destructive rows run under permits."
    artifacts: ["receipts.jsonl"]
  - name: liveness-settle
    sheets: 1
    instrument_guidance: "instrument: cli — the settlement probes must return EMPTY"
    fallback_friendly: false
    purpose: "Prove the host is clean with the physical checks that prove a conductor stopped."
    artifacts: []
  - name: seal
    sheets: 1
    instrument_guidance: "instrument: cli — harvest before archive; manifest after"
    fallback_friendly: false
    purpose: "After-action material out of the live tree, then archive + terminal manifest."
    artifacts: ["after-action/", "terminal-manifest.json"]
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

## Demobilization Checkout

`Status: Working` · **Source:** iteration 6 (Expedition 5 — ICS demobilization, ICS-347, ICS Form 221). **Scale:** concert-level. **Forces:** Partial Failure, Finite Resources.

### Core Dynamic

The corpus knows how to start things and how to fail things. Demobilization is the third ending: **release with accounting**. Every resource the concert consumed — process, workspace, lease, credential, branch, container — gets a checkout record with a disposition before the workspace archives. Doctrine's two sharpest edges: demobilization planning **begins at incident initiation** (the Write-Time Record's commissioning ledger is the census's pre-history — every provisioning row already carries its `decommission_cmd`), and resources are released **as soon as they are no longer needed**. The failure mode demob prevents is not dramatic; it is sediment: orphaned processes holding ports, unstopped leases firing into dead workspaces, finished campaigns occupying a hundred gigabytes because retirement had no owner. The incident that never demobilizes never actually ends; it just stops being visible. "The run ended" is not "the run failed."

Four separated tables: `census.jsonl` (what exists — CLI enumeration), `dispositions.jsonl` (what the AI decided, per resource id), `receipts.jsonl` (what the CLI did), settlement results (liveness probes that must return empty). The bijections are exact: every census id has exactly one disposition; every destructive disposition has a permit; every disposition has a receipt or a written reason. The demob score is chained by `on_success: run_job` from the concert's terminal score, with its mirror on `on_failure` — failure also demobilizes, with evidence preservation taking disposition priority.

### When to Use / When NOT to Use

Use: any concert with physical footprint — long-running monitoring scores, migration campaigns, release pipelines with clones and containers, anything with leases or daemons.

Not: hermetic one-shot scores with no footprint beyond their workspace (archival alone suffices); when the accounting costs more than the resources — demob is triage too: inventory what could leak, not everything.

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
  per_sheet_fallbacks: { 1: [], 3: [], 4: [], 5: [] }
prompt:
  template: |
    {% if stage == 1 %}
    bash "{score_dir}/scripts/demob.sh" census --processes --leases --workspaces \
      --credentials --branches --containers --emit "{{ workspace }}/census.jsonl"
    {% elif stage == 2 %}
    Write ONE disposition row per census id in {{ workspace }}/dispositions.jsonl:
    {id, disposition: archive|release|retain, reason}. Counts must match EXACTLY.
    {% elif stage == 3 %}
    bash "{score_dir}/scripts/demob.sh" act --dispositions "{{ workspace }}/dispositions.jsonl" \
      --receipts "{{ workspace }}/receipts.jsonl" --permits-required-for destructive
    {% elif stage == 4 %}
    bash "{score_dir}/scripts/demob.sh" settle --receipts "{{ workspace }}/receipts.jsonl" --liveness-must-return-empty
    {% else %}
    bash "{score_dir}/scripts/demob.sh" seal --harvest "{{ workspace }}/after-action/" --archive --emit-manifest
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

### Review Integration

Iteration 6: Review 1 found the draft conflated census and disposition rows in one file (making the "exact" join ambiguous), performed a single terminal census despite claiming as-needed release, and showed no `on_success`/`on_failure` attachment. Four separated tables, the commissioning pre-history via the Write-Time Record, the real hook attachment, and the Gas-Free discipline on destructive cleanup are the fixes.
