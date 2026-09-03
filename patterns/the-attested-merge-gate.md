---
name: The Attested Merge Gate
scale: score-level
status: working
forces:
- Producer-Consumer Mismatch
- Exponential Defect Cost
generators:
- Incremental Exposure
- Contract at Interfaces
problem: Parallel writers produce artifacts that must compose, and trusting their self-reports lets incompatible work merge.
signals:
- N different hands producing artifacts against a shared contract
- an interface writable before the work starts
- multi-module builds, multi-author documents, multi-vendor assembly
stages:
- name: contract-freeze
  sheets: 1
  instrument_guidance: claude-code or codex-cli — any AI instrument; output is the interface corpus pinned by manifest
  fallback_friendly: true
  purpose: Author and pin the interface contract in spec_dir.
  artifacts: []
- name: writers
  sheets: fan_out(6)
  instrument_guidance: claude-code or codex-cli — writers in instance-tagged namespaces (job-level worktree isolation is per-JOB, not per-sheet — see substrate matrix)
  fallback_friendly: true
  purpose: Build the slice; attest consumed spec hashes and output hashes.
  artifacts: []
- name: sweep
  sheets: 1
  instrument_guidance: any-wrapped CLI profile — executes the contract over actual bytes
  fallback_friendly: false
  purpose: Deterministic compatibility check; the merge is granted, never assumed.
  artifacts: []
- name: merge-authority
  sheets: 1
  instrument_guidance: claude-code or codex-cli — one AI sheet with serial ancestry; applies merges only where attestation AND sweep both pass
  fallback_friendly: true
  purpose: Merge or adjudicate; conflicts produce disposition records, never silent overwrites.
  artifacts: []
- name: post-merge-verify
  sheets: 1
  instrument_guidance: any-wrapped CLI profile — full-suite run plus release manifest
  fallback_friendly: false
  purpose: Bind merged content to branch attestations.
  artifacts: []
dependencies:
  writers:
  - contract-freeze
  sweep:
  - writers
  merge-authority:
  - sweep
  post-merge-verify:
  - merge-authority
composes_with:
- pattern: Join-Semilattice Merge
  how: substitution — the algebraic alternative when facts are additive; skip the authority
- pattern: First Article Characterization
  how: prerequisite — the manifest checks are the sweep's content
- pattern: Prefabrication (v4 archive)
  how: substitution — obsolete unless it adds attestation, grounded sweep, and single merge authority
type: orchestration-pattern
---

## The Attested Merge Gate


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

### Review Integration

Review 1 removed fictional per-sheet worktree isolation in favor of job-level chains or instance-tagged namespaces. Review 2 required attestation, a grounded byte sweep, and one serial merge authority. During split curation, the monolith's G1–G6 draft label was mapped to the nearest generator in forces.md, and every stage now names a current profile: deterministic stages use an any-wrapped CLI profile; judgment stages name claude-code, codex-cli, or opencode as appropriate.
