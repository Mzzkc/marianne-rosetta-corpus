---
name: Effectivity Blocks
scale: adaptation
type: orchestration-pattern
status: working
forces:
- Progressive Commitment
- Accumulated Signal
generators:
- Gate on Environmental Readiness
problem: A manifest or rule is treated as timeless even though it is valid only for a bounded configuration, population, or interval.
signals:
- a reference artifact certifies only one configuration family
- rules change while work remains in flight
- retries may observe a different active manifest
stages:
- name: bind
  sheets: 1
  instrument_guidance: codex-cli — identifies the exact configuration, population, and validity interval
  fallback_friendly: true
  purpose: Write the effectivity block beside the artifact.
  artifacts:
  - effectivity.yaml
- name: admit
  sheets: 1
  instrument_guidance: any-wrapped CLI profile — checks current facts against the declared block
  fallback_friendly: false
  purpose: Reject use outside the declared validity set.
  artifacts:
  - effectivity-verdict.json
dependencies:
  admit:
  - bind
composes_with:
- pattern: Flight Rules
  how: layering — bounds which rule revision applies
- pattern: First Article Characterization
  how: prerequisite — binds the reference to one homogeneous population
- pattern: Replication Licensing
  how: layering — limits what a license may authorize
---

## Effectivity Blocks

`Status: Working` · **Corpus disposition:** Archived/incubator from iteration 5.1.

### Problem Depth

A manifest or rule is treated as timeless even though it is valid only for a bounded configuration, population, or interval. The coordination failure is not merely missing documentation: it is an authority or state transition that cannot be reconstructed reliably after the participants diverge.

### Core Dynamic

Make validity explicit as a machine-checkable tuple such as configuration digest, population predicate, not-before/not-after revisions, and supersession pointer. Consumers check that tuple before use rather than assuming the newest artifact applies everywhere.

### When to Use / When NOT to Use

Use it when the listed signals are present and the state transition can be made visible in durable artifacts. Do not use it when one ordinary serial worker owns the whole boundary, when the claimed state cannot be checked, or when the bookkeeping costs more than the failure it prevents.

### Worked Structure

```yaml
movements:
  1: { name: bind }
  2: { name: admit }

sheet:
  size: 1
  total_items: 2
  dependencies: { 2: [1] }

prompt:
  template: |
    {% if stage == 1 %}
    Produce effectivity.yaml with stable identity, authority, and input digests.
    {% else %}
    Read predecessor artifacts, perform movement {{ stage }}, and write its declared output.
    {% endif %}

validations:
  - type: file_exists
    path: "{workspace}/effectivity.yaml"
    condition: "stage == 1"
  - type: file_exists
    path: "{workspace}/effectivity-verdict.json"
    condition: "stage == 2"
```

**Worked example.** A first article is valid only for schema digest A and generator revision 12–14. Revision 15 changes an output field, so the admission gate refuses to characterize the new batch from the old article.

### Failure Modes

The block carries human prose instead of predicates, or an open-ended wildcard quietly turns bounded validity back into timeless authority. Another common failure is to let an AI verdict stand in for a deterministic identity, count, digest, or transition check; those checks belong to the any-wrapped CLI stage with no AI fallback.

### Review Integration

Archived but marked as a strong next-core candidate because three core compositions already require its validity-lease move. Promotion needs a proof score and script contract. The split file uses only verified Marianne surfaces and current profiles. It does not claim runtime support for operating-system confinement, artifact-offset scheduling, or concurrent shared-workspace backpressure.

### Composes With

- **Flight Rules:** layering — bounds which rule revision applies.
- **First Article Characterization:** prerequisite — binds the reference to one homogeneous population.
- **Replication Licensing:** layering — limits what a license may authorize.
