---
name: Variant Apparatus
scale: communication
type: orchestration-pattern
status: working
forces:
- Structured Disagreement
- Producer-Consumer Mismatch
generators:
- Frame Multiplication
problem: Synthesis erases material dissent to produce one smooth deliverable, depriving consumers of the conditions under which the conclusion changes.
signals:
- credible witnesses disagree
- the disagreement affects action
- a single conclusion would conceal assumptions rather than resolve them
stages:
- name: witnesses
  sheets: 1
  instrument_guidance: claude-code, codex-cli, and opencode — independent witnesses use stable sigla
  fallback_friendly: false
  purpose: Produce claims and evidence without forced convergence.
  artifacts:
  - witnesses/
- name: apparatus
  sheets: 1
  instrument_guidance: claude-code — edits the main line and inline variants together
  fallback_friendly: false
  purpose: Publish a usable position while preserving consequential dissent.
  artifacts:
  - deliverable-with-variants.md
- name: coverage-gate
  sheets: 1
  instrument_guidance: any-wrapped CLI profile — joins each consequential divergence to an inline siglum
  fallback_friendly: false
  purpose: Reject erased or orphaned variants.
  artifacts:
  - variant-verdict.json
dependencies:
  apparatus:
  - witnesses
  coverage-gate:
  - apparatus
composes_with:
- pattern: Sugya Weave (Editorial Synthesis)
  how: layering — preserves unresolved witness variants inside the argued editorial position
- pattern: Talmudic Page
  how: substitution — compresses multi-layer commentary into a deliverable with inline sigla
---

## Variant Apparatus

`Status: Working` · **Corpus disposition:** Archived/incubator from iteration 5.1.

### Problem Depth

Synthesis erases material dissent to produce one smooth deliverable, depriving consumers of the conditions under which the conclusion changes. The coordination failure is not merely missing documentation: it is an authority or state transition that cannot be reconstructed reliably after the participants diverge.

### Core Dynamic

The editor still chooses a main line, but every consequential alternative remains at the exact claim it contests with stable witness sigla and evidence pointers. Dissent becomes part of the product, not an appendix nobody reads.

### When to Use / When NOT to Use

Use it when the listed signals are present and the state transition can be made visible in durable artifacts. Do not use it when one ordinary serial worker owns the whole boundary, when the claimed state cannot be checked, or when the bookkeeping costs more than the failure it prevents.

### Worked Structure

```yaml
movements:
  1: { name: witnesses }
  2: { name: apparatus }
  3: { name: coverage-gate }

sheet:
  size: 1
  total_items: 3
  dependencies: { 2: [1], 3: [2] }

prompt:
  template: |
    {% if stage == 1 %}
    Produce witnesses/ with stable identity, authority, and input digests.
    {% else %}
    Read predecessor artifacts, perform movement {{ stage }}, and write its declared output.
    {% endif %}

validations:
  - type: file_exists
    path: "{workspace}/witnesses/"
    condition: "stage == 1"
  - type: file_exists
    path: "{workspace}/variant-verdict.json"
    condition: "stage == 3"
```

**Worked example.** A risk memo recommends release under assumption A while inline variants show that the security witness rejects A and what evidence would change the result.

### Failure Modes

The apparatus preserves every stylistic difference and overwhelms the main line, or relegates material dissent to an unlinked appendix. Another common failure is to let an AI verdict stand in for a deterministic identity, count, digest, or transition check; those checks belong to the any-wrapped CLI stage with no AI fallback.

### Review Integration

Archived as a strong candidate because it is the corpus's clearest carrier of preserved dissent. Core promotion needs evidence that consumers can use the apparatus without losing decision clarity. The split file uses only verified Marianne surfaces and current profiles. It does not claim runtime support for operating-system confinement, artifact-offset scheduling, or concurrent shared-workspace backpressure.

### Composes With

- **Sugya Weave (Editorial Synthesis):** layering — preserves unresolved witness variants inside the argued editorial position.
- **Talmudic Page:** substitution — compresses multi-layer commentary into a deliverable with inline sigla.
