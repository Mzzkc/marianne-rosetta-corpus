---
name: Designation Is Authorization
scale: instrument-strategy
status: working
forces:
- Instrument-Task Fit
- Information Asymmetry
generators:
- Verify through Diverse Observers
problem: Authority expressed as a list of rights the subject names lets authority leak through any confused intermediary.
signals:
- mixed-instrument fan-outs where sheets differ in trust
- a cheap summarizer touching sensitive context; tool attachment that must be scoped
- technique/skill injection that must not be ambient
stages:
- name: capability-manifest
  sheets: 1
  instrument_guidance: claude-code or codex-cli — any AI instrument — authors the per-sheet designation map (this is DESIGN, pre-run)
  fallback_friendly: true
  purpose: 'Declare per sheet: techniques attachments, cadenza directories (exactly one subtree each), spec_tags.'
  artifacts: []
- name: scoped-execution
  sheets: 1
  instrument_guidance: claude-code or codex-cli — the designated sheets — running with only what was handed
  fallback_friendly: true
  purpose: 'Execute with designated context only: undesignated specs are ABSENT, not hidden.'
  artifacts: []
- name: capability-audit
  sheets: 1
  instrument_guidance: any-wrapped CLI profile — dumps every sheet's effective capability set
  fallback_friendly: false
  purpose: Make designation inspectable for review.
  artifacts: []
dependencies:
  scoped-execution:
  - capability-manifest
  capability-audit:
  - scoped-execution
composes_with:
- pattern: Proof-Carrying Artifact
  how: layering — evidence bundles as designated context
- pattern: The Etiquette Law
  how: layering — instruments as capability endpoints on the chain
type: orchestration-pattern
---

## Designation Is Authorization


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

### Review Integration

Review 2 forced the boundary between context designation and process confinement. This working form limits attached specs, techniques, and cadenzas; true operating-system confinement remains outside the available primitives. The Package Is the Permission is absorbed here and in Proof-Carrying Artifact: a `required: true` cadenza makes absence fail closed, while the consumer's package audit proves that the bytes actually attached match the designated manifest. During split curation, the monolith's G1–G6 draft label was mapped to the nearest generator in forces.md, and every stage now names a current profile: deterministic stages use an any-wrapped CLI profile; judgment stages name claude-code, codex-cli, or opencode as appropriate.
