# Core Thesis and Scope

## What Enclave is

Enclave is a theoretical architecture for **reactive actor branching narrative in interactive media**.

Its central problem is the conflict between:

- deeply authored narrative;
- meaningful Participant and Actor agency;
- persistent consequence;
- information asymmetry;
- computational tractability.

Traditional interactive narrative makes broad agency expensive because meaningful divergence creates growing combinations of state, consequence, dialogue, Actor behaviour, Event eligibility, information availability, and future content. Conventional systems cope by restricting action, reconverging branches, isolating side content, or limiting how deeply consequences propagate.

Modern probabilistic systems materially improve open-ended interpretation and Actor behaviour, but they are poor sole custodians of authoritative persistent state. Enclave treats that mismatch as an architectural opportunity rather than asking one system to do everything.

## Core thesis

Human authors should define a rich narrative world and its possibility space rather than enumerate every branch Participants or Actors may create.

Participants and Actors then act inside that world. Their actions are interpreted, resolved against authoritative state, persisted as consequences, and allowed to alter later narrative circumstances.

The realized narrative is therefore an **emergent trajectory through a persistently authored narrative world**.

It is neither:

- a fixed branching tree;
- unrestricted procedural storytelling;
- an LLM improvising the next chapter;
- an LLM-owned simulation;
- merely an NPC memory framework.

## Primary runtime purpose

Enclave can be used as an informational and causal architecture for a fully deterministic simulation.

Its **primary design purpose**, however, is to provide the persistent structure necessary for **faithful, bounded, unsupervised narrative agents attached to persistent Actors**.

Those agents should operate as inhabitants of the authored world rather than omniscient narrative generators.

A Cognitive Actor therefore persists independently of any individual model invocation. Its identity, Knowledge, Memories, relationships, goals, Enclave relationships, circumstances, prior actions, and consequences live outside the temporary inference context.

The model invocation is a temporary cognitive process serving that persistent Actor.

## Human authorship is a design requirement

The paper deliberately treats human authorship as positive creative infrastructure, not a legacy constraint to be removed.

Human authors provide:

- worldbuilding;
- characters and institutions;
- conflicts and relationships;
- themes and philosophical intent;
- secrets and information;
- motivations and goals;
- possible Events;
- intended developments;
- constraints;
- narrative pressures;
- acceptable or meaningful outcomes.

The architectural problem is how to **extend the reach of human authorship** into circumstances an author did not individually anticipate.

A recurring framing is that authors act like **pre-emptive Gamemasters**: they prepare the world, situations, Actors, pressures, intentions, plans, possible developments, and consequences in advance rather than scripting every Participant path.

Live in-play author or Gamemaster intervention remains a possible application, but is not required by the theory.

## Participant authorship

Participant action contributes to the realized narrative without displacing human authorship.

The author creates the meaningful world and possibility space. The Participant partially authors the realized sequence by deciding what to engage with, disrupt, combine, reveal, conceal, or redirect.

This is **Participant authorship inside a purposefully authored world**, not the disappearance of authorship.

## Key distinction: narrative sandboxing

Existing games show that **world sandboxing** is highly developed. A finite authored substrate of rules, objects, systems, and affordances can produce world states nobody explicitly enumerated.

The asymmetry is that deeply authored narrative is usually less sandboxed than the world.

Enclave's narrower contribution is therefore a **reactive authored narrative sandbox**: authored narrative structures should be able to absorb emergent world Events as persistent meaningful inputs without requiring every reaction to be explicitly authored beforehand.

## The two central runtime ideas

The architecture culminates in two coupled mechanisms.

### 1. Independent bounded Cognitive Actors

Each Cognitive Actor reasons from its own persistent subjective state rather than from omniscient world state.

The architecture distinguishes:

- the complete informational state of the world;
- the persistent informational state available to a particular Actor;
- the temporary subset assembled for a particular cognitive operation.

This is how probabilistic Actors can remain faithful to their authored identities, histories, secrets, mistakes, relationships, and circumstances.

### 2. Persistent cause and effect

A narrative agent determines what its Actor attempts to do.

It does **not** independently decide what actually happens.

Attempted actions return to authoritative systems for resolution. Accepted outcomes become Events and persistent consequences that alter physical state, informational state, Actor Memory, future access, later decisions, and authored developments.

The central runtime loop is therefore:

```text
bounded Actor perspective
    ->
temporary cognition
    ->
attempted action
    ->
authoritative resolution
    ->
persistent Event/consequence
    ->
changed world and informational state
    ->
new bounded perspectives
```

This coupling is the practical architectural response to the Agency-Persistence Gap.

## Theoretical scope

The paper is architectural, not prescriptive implementation work.

It should define:

- conceptual responsibilities;
- authority boundaries;
- semantic primitives;
- key derivatives;
- causal flow;
- epistemic separation;
- information distribution;
- Cognitive Actor operation;
- scaling principles.

It should not prematurely prescribe:

- one storage engine;
- one graph schema;
- one retrieval algorithm;
- one prompt format;
- one transmission algorithm;
- one belief-revision algorithm;
- one authoring tool;
- one model stack.

Enclave currently has an **ontology, information-flow architecture, Cognitive Actor runtime model, and interaction/authority model**, not a complete data model.

## Broader generalization

Although the paper is framed around interactive narrative, the architecture may generalize beyond games to **reactive Actors in controlled information environments**.

A possible generalized framing remains:

> *An Event-Driven System for Reactive Actors in a Controlled Information Environment*

The generalized composition is:

- authoritative external state;
- persistent Events;
- Actor-local experiential Memory;
- persistent Facts / Knowledge;
- controlled exposure;
- source and authority semantics;
- bounded Actor cognition;
- deterministic consequences;
- probabilistic decision makers.

This broader framing should not replace the current paper title unless explicitly decided later.
