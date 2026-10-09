# Runtime Architecture Checkpoint — 2026-10-06

This file is a compact context dump of the major architectural consolidation completed while drafting Sections 9–13. It is intended as a fast recovery point for future sessions.

## Current paper state

Canonical outline: `docs/paper-outline.md`

Current structure:

1. Abstract
2. Human Authorship as a Design Requirement
3. Authoring as Worldbuilding, Adversarial Design, and Narrative Planning
4. Player Agency and the Branching Narrative Problem
5. The Agency-Persistence Gap
6. Sandbox Games and the Existing Sandbox Capability
7. The Enclave System: Overview
8. Layers of Authority
9. Primitives
10. Key Derivatives
11. Knowledge Distribution and Access
12. Actor Cognition
13. Persistent Cause and Effect
14. Computational Architecture and Scale
15. Worked System Example
16. Practical Applications
17. Conclusion

Sections 9–13 have undergone major architectural consolidation. Sections 12 and 13 now form the settled central runtime pair. Section 14 is the next major target.

## Foundational ontology

Seven foundational primitives:

### Knowledge
- Facts
- Memories
- Events

### Nexuses
- Loci
- Actors
- Participants

### Classification
- Domains

The former nine-primitive model is superseded.

## Key derivatives

Section 10:

1. Interaction
2. Enclave
3. Rank
4. Facet
5. Combinatorial Enclave
6. Inheritance

### Interaction

Canonical definition:

> **An Interaction is an Event characterized by causal process.**

### Enclave

A specialized Domain associated with an Actor population.

Typically cross-Domain and participating in one hierarchy.

### Rank

A specialized subordinate Enclave intrinsic to every Enclave.

### Facet

An identifiable entity represented through multiple independent Enclave hierarchies.

Canonical example: a city such as Nanaimo.

### Combinatorial Enclave

The conjunction/intersection of multiple Enclaves.

Semantic identity is preserved even where different combinations resolve to the same Actor population.

### Inheritance

Parent-child implication between Enclaves.

Used semantically and computationally.

Key phrase:

> **Combinatorial identity is cheap; population intersection is expensive.**

Detailed math belongs in Addendum B.

## Information architecture — Section 11

### Initial distribution

The Knowledge Base is the source of all represented Knowledge, but Actor access is bounded.

Current demonstrative authored graph:

`Domains > Facets > Enclaves & Combinatorial Enclaves > Ranks > Memory`

This is conceptual, not a mandatory literal database hierarchy.

### Transmission

Knowledge can move through Actors, Participants, and Loci.

Transmission can be deterministic, probabilistic, or hybrid.

### Diffusion

Facts can be retransmitted, summarized, distorted, contradicted, or transformed.

Long-lived worlds can naturally produce rumours, renown, myths, and legends.

### Saturation

Saturation is a relationship among:

- a Fact;
- an Enclave;
- its relevant Actor population.

It is evaluated against narrow meaningful populations and can move upward through broader populations.

### Institutional Knowledge

When a Fact crosses the implementation-defined Saturation Threshold within an Enclave, it may become Institutional Knowledge.

### Institutional Emission

Institutional Knowledge can be emitted through ordinary institutional mechanisms rather than simulating every individual pairwise transmission.

Participants do not receive this automatically.

### Information as world state

The system stores not only truth and physical state but also distribution:

- who knows what;
- where Knowledge exists;
- institutional adoption;
- emission;
- reach;
- contradictory versions.

Informational state itself is causal.

## Cognitive Actor architecture — Section 12

Section 12 is now settled under the title **Actor Cognition**.

### 12.1 Bounded Narrative Agents

- Enclave can support fully deterministic simulation;
- its primary design purpose is faithful, bounded, unsupervised narrative agents;
- agents operate as inhabitants rather than omniscient narrators;
- authors create world/Actors/constraints rather than enumerate every response;
- bounded agents can create effectively unbounded emergent trajectories inside a deeply authored space.

The paper explicitly keeps the line that bounded narrative context eliminates secret/narrative leaks from Enclave's own context. It separately notes the external risk of model training-data contamination.

### 12.2 The Persistent Cognitive Actor

Core invariant:

> **The Actor is persistent; the model invocation is not.**

Persistent Actor state includes identity, Knowledge, Memory, relationships, goals, circumstances, prior actions, and consequences outside inference.

### 12.3 The Actor's Subjective World

Three scopes:

1. complete world informational state;
2. persistent Actor-accessible subjective state;
3. temporary active context.

Key formulation:

> **Epistemic boundaries determine what an Actor can know; retrieval determines what the Actor is presently attending to.**

### 12.4 Memory and Cognition

Memory supplies Actor-specific continuity beyond individual inference sessions.

The Memory subsystem must preserve experience, support later retrieval/salience, and support the Memory Classification process already established in §9.3 whereby narratively relevant Memory content may correspond to, contextualize, or create Knowledge/Facts.

Persistence, salience, validity, and forgetting remain separate concepts.

### 12.5 Context Construction

Context is a temporary field of attention over the larger persistent subjective state.

The current section explicitly allows the complete legitimate subjective state to be supplied when economical, with pruning/retrieval becoming necessary as scale requires. Structural, semantic, temporal, causal, and exploratory relevance may all contribute to selection.

Context may expand progressively during cognition when reasoning establishes a need for additional legitimate Knowledge or Memory.

### 12.6 The Cognitive Cycle

Representative cycle:

```text
trigger
-> identify Actor
-> establish epistemic boundary / Knowledge context
-> retrieve Memory context
-> compose working context
-> interpret / reason
-> retrieve more if needed
-> choose attempted action
-> express behaviour/dialogue
-> submit attempt to authoritative systems
-> resolve Event/consequence
-> return state/information exposure
-> persist relevant Memory / classify if appropriate
```

Critical boundary:

> the Cognitive Actor determines what it attempts; the authoritative system determines what actually happens.

### 12.7 Divided Cognitive Responsibility

Three broad responsibilities are separated:

- **Enclave** — authoritative world state, Actor-accessible Knowledge, epistemic boundaries, Knowledge context, Event resolution;
- **Memory system** — persistent experiential state and relevant Memory context;
- **narrative agent** — interpretation, reasoning, planning, communication, and action selection.

Each responsibility may combine deterministic and probabilistic mechanisms.

### 12.8 Reliquary and the Development of the Enclave Architecture

Reliquary remains theoretically optional, but the applied Enclave architecture was substantially informed by practical work on Reliquary.

Important inherited distinctions include:

- persistent state vs temporary cognitive context;
- availability vs present attention;
- semantic vs structural relevance;
- provenance;
- source chronology vs content-valid time;
- salience vs truth/persistence;
- progressive context construction;
- deterministic routing/constraint around probabilistic judgment.

The current paper intentionally presents Reliquary as architectural lineage and a strongly recommended analogous substrate without making it a theoretical dependency.

Section 12 closes by handing directly into §13: the Actor can now perceive, reason, remember, and choose from a bounded persistent perspective; §13 explains how those attempted actions become persistent causes in the shared world.

## The architectural climax

Sections 12 and 13 are the two central runtime sections of the paper.

### Section 12

How a deeply authored world can support independent, bounded, persistent Cognitive Actors.

### Section 13

How attempted actions enter causal Interactions and produce persistent narrative consequences in the shared world.

Settled points:

- sandbox and simulation-heavy games already provide sophisticated systemic/physical causality; Enclave focuses on **persistent narrative cause and effect**;
- once an attempted action enters the world, **Interaction** is the causal unit, and an Interaction is already an Event characterized by causal process;
- failed attempts generally still constitute Interactions/Events in the theory, while implementation fidelity determines what is worth persisting;
- probabilistic interpretation could also support an effectively open-ended physical action vocabulary over a finite simulated substrate, but this is complementary rather than Enclave's principal purpose;
- **temporal cadence** allows Actor plans, deadlines, institutions, and scheduled developments to continue without Participant intervention, making inaction causally meaningful;
- Enclave relocates much of the authorial burden from enumerating paths and reactions into constructing the persistent narrative substrate from which causal histories emerge;
- Interactions and other Events provide natural triggers for causally relevant reevaluation rather than requiring universal continuous simulation.

Together:

```text
persistent bounded Actor
    ->
temporary cognition
    ->
attempted action
    ->
Interaction / authoritative causal resolution
    ->
persistent Event/consequence
    ->
changed physical + informational world state
    ->
later bounded cognition
```

This is the Enclave runtime in its simplest form.

## Next major work

1. Revise Section 14 around computational architecture and scale now that the §12–§13 runtime core is settled.
2. Carry forward the §13 event-driven model into scaling:
   - event-driven activation;
   - variable fidelity;
   - persistent Memory/Knowledge cost;
   - deterministic/probabilistic division;
   - Combinatorial Enclave reduction;
   - Saturation/Institutional Emission compression.
3. Ensure Section 15's worked example traces the entire central loop, including temporal cadence and causal divergence.
4. Formalize Addendum B math/algorithms.
5. Complete remaining citation/editorial verification without reopening settled architecture unnecessarily.
