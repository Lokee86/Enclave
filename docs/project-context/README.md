# Enclave Project Context

This directory is the canonical **working-context bundle** for the Enclave paper. It exists so that future work does not depend on reconstructing decisions from chat history or inferring them from stale drafts.

It does **not** replace the paper or outline. It records the current conceptual state of the project, including settled decisions, working hypotheses, superseded framings, implementation boundaries, research roles, and unresolved questions.

## Paper

**Current title:** *Event-Driven Systems for Reactive Actor Branching Narrative in Interactive Media*

**Project name:** Enclave

**Status:** theoretical architectural framework / paper. Enclave is not yet a complete implementation specification or a defined data model.

The canonical paper outline is currently developed through **Section 13**, with Sections 9–13 substantially settled. Section 12, **Actor Cognition**, and Section 13, **Persistent Cause and Effect**, form the paper's central runtime pair.

## Precedence

When sources disagree, use this order:

1. explicit latest decisions recorded in this directory;
2. current `docs/paper-outline.md`;
3. `docs/research/bibliography-notes.md` and retained research;
4. `docs/design-paper.md`, which is an older draft and must not override the current outline/context bundle.

Do not silently revive superseded terminology or section structures from older drafts.

## Current central proposition

> Authors create the narrative. Actors disrupt it. Events make those disruptions consequential. The system makes the authored world capable of responding.

The architectural objective is not to replace human authorship with generated narrative. It is to make deeply authored narrative worlds capable of absorbing participant and Actor actions that were not individually anticipated while preserving authoritative state, persistent consequence, asymmetric information, and authorial structure.

## Current conceptual core

Enclave combines three complementary capabilities:

- **human authorship** provides meaning, worldbuilding, characters, conflicts, themes, intentions, pressures, and possible developments;
- **conventional computation** provides persistence, identity, authoritative state, validation, causality, indexing, and exact constraints;
- **probabilistic systems** provide interpretation, semantic flexibility, contextual reasoning, open-ended Actor behaviour, and natural expression.

The architecture is deliberately hybrid. No one layer is expected to perform the class of work it handles poorly.

The system is also compatible with fully deterministic simulation. Its **primary design purpose**, however, is to provide the persistent structure necessary for faithful, bounded, and unsupervised narrative agents attached to Actors.

## Foundational primitive model

The latest ontology contains **seven foundational primitives in three families**:

| Family | Primitives |
| --- | --- |
| **Knowledge** | Facts, Memories, Events |
| **Nexuses** | Loci, Actors, Participants |
| **Classification** | Domains |

These are the irreducible semantic building blocks currently required by the theory.

## Key derivatives

Section 10 defines six important derivatives rather than expanding the foundational ontology:

1. **Interaction** — an Event characterized by causal process.
2. **Enclave** — a specialized Domain associated with an Actor population, commonly cross-Domain.
3. **Rank** — a specialized subordinate Enclave intrinsic to every Enclave.
4. **Facet** — an identifiable entity whose relevant context is expressed through multiple independent Enclave hierarchies.
5. **Combinatorial Enclave** — the conjunction/intersection of two or more Enclaves.
6. **Inheritance** — parent-child implication between Enclaves, also used to reduce redundant combinatorial population computation.

A useful implementation distinction is:

> **Combinatorial identity is cheap; population intersection is expensive.**

## Information runtime

Section 11 now establishes the principal information-flow machinery:

- authored initial Knowledge distribution;
- deterministic and/or probabilistic Knowledge transmission;
- emergent diffusion;
- Enclave Saturation;
- Institutional Knowledge;
- Institutional Emission;
- information distribution as persistent world state.

Saturation is a relationship between a **Fact, an Enclave, and its relevant Actor population**. Once an implementation-defined Saturation Threshold is reached, the Fact may become Institutional Knowledge of that Enclave. Institutional Emission then provides a causal abstraction for large-scale information dissemination without requiring every Actor-to-Actor transmission to be simulated individually.

Canonicality remains independent from distribution, saturation, institutionalization, and belief.

## Central runtime pair

The paper has now reached the two runtime ideas around which the architecture ultimately turns:

1. **bounded independent Cognitive Actors** — persistent Actors whose narrative agents reason from their own Knowledge, Memory, circumstances, goals, and informational access rather than omniscient world state;
2. **persistent narrative cause and effect** — attempted actions leave the Actor, are resolved by authoritative systems, become Events/consequences, and alter the world from which later Actors reason.

The core loop is therefore:

```text
persistent bounded Actor state
    ->
temporary cognitive context
    ->
interpretation / reasoning
    ->
attempted action
    ->
authoritative resolution
    ->
Event and persistent consequence
    ->
changed world and informational state
    ->
later bounded cognition
```

Section 12 develops the first half. Section 13 develops the second.

## Files in this directory

- `01-core-thesis-and-scope.md` — what Enclave is, what problem it solves, and what it is not.
- `02-paper-structure-and-section-intent.md` — current section order, intended argumentative flow, and current section status.
- `03-ontology-and-primitives.md` — seven foundational primitives, key derivatives, and ontology/data-model boundaries.
- `04-authority-interaction-and-information-flow.md` — authority, Events, Interaction, transmission, diffusion, Saturation, Institutional Knowledge/Emission, and informational world state.
- `05-authoring-agency-sandbox-and-persistence.md` — human authorship, branching, Gamemaster analogy, Agency-Persistence Gap, and narrative sandbox.
- `06-computation-implementation-and-scaling.md` — persistent Cognitive Actors, bounded subjective state, context construction, cognitive cycle, model division, combinatorial scaling, and variable fidelity.
- `07-research-prior-art-and-evidence-map.md` — what the existing research corpus is being used to support and new evidence needs.
- `08-worked-example-applications-and-generalization.md` — Northern Fortress / House Vale example, applications, live authoring, and generalization beyond games.
- `09-decisions-non-goals-and-open-questions.md` — settled editorial/architectural decisions, superseded framings, non-goals, and remaining questions.
- `10-runtime-architecture-checkpoint-2026-10-06.md` — latest compact context dump covering the Sections 9–13 architectural consolidation.

Related outlines outside this directory:

- `docs/addendum-generalization-outline.md` — Addendum A, generalization beyond interactive narrative.
- `docs/addendum-combinatorial-enclaves-outline.md` — Addendum B, combinatorial Enclave / Inheritance computation.

## Maintenance rule

When a conceptual decision is settled in discussion, update this context bundle before or alongside editing the paper. Mark uncertain items as **working** rather than allowing multiple incompatible versions to coexist without explanation.
