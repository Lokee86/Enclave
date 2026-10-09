# Paper Structure and Section Intent

## Current title

*Event-Driven Systems for Reactive Actor Branching Narrative in Interactive Media*

## Current canonical section order

### 1. Abstract

Establish the core problem and architectural response:

- interactive narrative trades freedom against authorial control;
- probabilistic systems expand reactive capability but create authority/persistence problems;
- Enclave separates authorship, persistent authority, reactive Actors, and probabilistic interpretation;
- objective: preserve human authorship while avoiding exhaustive response enumeration.

### 2. Human Authorship as a Design Requirement

Purpose:

- establish human creativity and long-range narrative intent as valuable;
- make clear that unpredictable participation is a property of interactive media, not a failure of writers;
- show that current authoring mechanisms constrain both writers and Participants;
- frame the objective as increasing authorial leverage rather than replacing authors.

Do not turn this section into an AI architecture section.

### 3. Authoring as Worldbuilding, Adversarial Design, and Narrative Planning

Purpose:

- shift authorship from fixed sequences toward authored worlds and situations;
- use Justin Alexander's situation/node design as practitioner precedent;
- preserve intended future developments without making them fixed plots;
- emphasize information flow as narrative structure;
- distinguish diegetic world organization from abstract scene graphs;
- treat Actors as sources of motion;
- use storylets/conditional content as precedent;
- describe Participant sequence as emergent authorship;
- define authorial leverage as more narrative richness for a given amount of authoring work;
- establish the historical explicit-formalization bottleneck.

Important boundary: node structure is useful prior art but **node is not the ontology of the world**.

### 4. Player Agency and the Branching Narrative Problem

Its argumentative job is the continuous chain:

1. meaningful consequence creates state-space growth;
2. persistent consequence creates a branching tax;
3. planning/simulation moves but does not erase representation cost;
4. deterministic architectures are useful but bounded by explicit formalization;
5. interactive systems manage complexity through reconvergence and other restrictions;
6. perceived agency can exceed causal agency;
7. explicit formalization is the historical bottleneck;
8. probabilistic models change what must be formalized in advance;
9. probabilistic flexibility does not supply authority;
10. hybrid computation becomes newly practical;
11. agency at scale remains constrained by representation;
12. consequential agency is fundamentally combinatorial;
13. existing designs impose limits;
14. larger worlds exacerbate interaction complexity;
15. human Gamemasters are the analog solution;
16. persistent human Gamemaster labour is economically difficult to scale;
17. machine intelligence can perform much of the open-ended interpretive work.

The current outline contains some conceptual overlap in Section 4 because previously separate material was merged. That is a later editorial cleanup issue, not a reason to re-split the section.

### 5. The Agency-Persistence Gap

Current progression:

- **5.1 The Agency**
- **5.2 Expanded Agency**
- **5.3 The Persistence**
- **5.4 LLMs Are Poorly Suited to Maintaining State**
- **5.5 Naive Applications Create Linear Storage Problems**
- **5.6 The Gap**
- **5.7 Fertile Ground**
- **5.8 Enclave as an Architectural Response**

Critical rhetorical ordering:

- establish what probabilistic systems make possible;
- show that meaningful agency necessarily creates persistent consequences;
- show why LLMs/context alone are unreliable state custodians;
- name the **Agency-Persistence Gap**;
- only then compare complementary deterministic/probabilistic strengths;
- present Enclave as the architectural response.

### 6. Sandbox Games and the Existing Sandbox Capability

Purpose:

- establish that systemic sandboxing already supports enormous spaces of valid emergent world state;
- distinguish bounded interaction vocabulary from literal unlimited freedom;
- show that persistence itself is not the central sandbox limitation;
- distinguish systemic emergence, emergent/player-constructed narrative, and reactive authored narrative;
- identify the missing capability as a **reactive authored narrative sandbox**.

Avoid claiming Enclave invented narrative sandboxing.

### 7. The Enclave System: Overview

Current subsections:

- **7.1 Sandboxing the Narrative**
- **7.2 Three Primitive Families**
- **7.3 Human Authors Define the Knowledge Base**
- **7.4 Nexus Interactions Create Cause and Effect**
- **7.5 Knowledge Control and Classification**
- **7.6 Narrative as Emergent State**
- **7.7 Why It Can Work**

Important accepted ideas:

- Participant actions occur inside a world that already has authoritative state, constraints, and history;
- authors establish the Knowledge Base and possibility space;
- consequences alter the circumstances from which later narrative is produced;
- narrative is evolving state, not movement through a predetermined sequence;
- authorship, conventional computation, and probabilistic interpretation cover complementary problem classes.

### 8. Layers of Authority

Current subsections:

- **8.1 Different Authority for Different Layers**
- **8.2 Authorial Authority**
- **8.3 Knowledge Authority**
- **8.4 Actor Authority**
- **8.5 Action, Resolution, and Consequence**
- **8.6 A Single Source of Truth**

Core framing: authority is **jurisdiction**.

Actors/Participants own attempted action. The persistent system owns authoritative resolution. Authors own the authored possibility space. Probabilistic systems may interpret or propose without silently becoming authoritative.

### 9. Primitives

Section 9 now contains the settled **seven foundational primitives**:

**Knowledge**
- Facts
- Memories
- Events

**Nexuses**
- Loci
- Actors
- Participants

**Classification**
- Domains

The section deliberately ends by handing specialized contextual structures to Section 10.

### 10. Key Derivatives

Settled derivative order:

- **10.1 Derivation From the Foundational Primitives**
- **10.2 Interaction**
- **10.3 Enclaves**
- **10.4 Rank**
- **10.5 Facets**
- **10.6 Combinatorial Enclaves**
- **10.7 Inheritance**

Important distinctions:

- Interaction is an Event characterized by causal process.
- Enclaves are specialized Domains associated with Actor populations.
- Rank is a specialized subordinate Enclave intrinsic to every Enclave.
- Facets represent identifiable entities expressed through multiple independent Enclave hierarchies.
- Combinatorial Enclaves preserve semantic intersection identities.
- Inheritance provides parent-child implication and reduces redundant population computation.
- **Combinatorial identity is cheap; population intersection is expensive.**

### 11. Knowledge Distribution and Access

Section 11 is now the principal information-runtime section.

Current subsections:

- **11.1 Initial Knowledge Distribution**
- **11.2 Knowledge Transmission**
- **11.3 Emergent Diffusion**
- **11.4 Enclave Saturation and Institutional Knowledge**
- **11.5 Institutional Emission**
- **11.6 Information as World State**

Important accepted ideas:

- the authored Knowledge Base is the source from which bounded Actor access is derived;
- transmission may be deterministic, probabilistic, or hybrid;
- canonical and non-canonical Knowledge propagate through the same mechanisms;
- diffusion can naturally create rumours, renown, myths, and legends;
- Saturation is evaluated as a Fact/Enclave/population relationship;
- sufficiently saturated Facts may become Institutional Knowledge;
- Institutional Emission provides a causal abstraction for broad dissemination;
- information distribution itself becomes persistent causal world state.

### 12. Actor Cognition

Section 12 is settled and forms the first half of the central runtime pair.

Current subsections:

- **12.1 Bounded Narrative Agents**
- **12.2 The Persistent Cognitive Actor**
- **12.3 The Actor's Subjective World**
- **12.4 Memory and Cognition**
- **12.5 Context Construction**
- **12.6 The Cognitive Cycle**
- **12.7 Divided Cognitive Responsibility**
- **12.8 Reliquary and the Development of the Enclave Architecture**

Core thesis:

- Enclave is compatible with deterministic simulation;
- its primary design purpose is faithful, bounded, unsupervised narrative agents;
- the Actor persists independently of the model invocation;
- the architecture distinguishes world informational state, Actor-accessible persistent state, and temporary active context;
- Memory preserves Actor-specific continuity and can feed the §9.3 Memory Classification process;
- epistemic boundaries determine what the Actor can know;
- retrieval determines what the Actor is currently attending to;
- context may be progressively expanded during cognition when additional legitimate information becomes relevant;
- the Cognitive Actor determines attempted action, not authoritative outcome;
- Reliquary is presented as important architectural lineage without becoming a theoretical dependency.

### 13. Persistent Cause and Effect

This is the second half of the central runtime pair and is now substantially settled.

Its job is to explain how attempted actions from bounded Cognitive Actors enter the shared world, participate in authoritative causal Interactions, and create persistent circumstances from which later cognition and authored narrative emerge.

Core progression:

- cognition produces an attempted action rather than an authoritative outcome;
- an attempted action enters an Interaction, which §10.2 already defines as an Event characterized by causal process;
- the authoritative world determines the resulting causal process;
- Interactions and other Events persist consequences across physical, informational, social, institutional, and authored narrative state;
- those consequences become causes of later cognition, action, and Events.

The section deliberately distinguishes Enclave's focus on **persistent narrative cause and effect** from the sophisticated systemic/physical causality already provided by sandbox and simulation-heavy games.

It briefly identifies **open-ended action space** as a complementary possibility: probabilistic interpretation may map semantic physical intent onto a finite simulated substrate, but this is not Enclave's principal purpose.

Two additional settled points are important:

- **Temporal cadence:** the narrative world can progress independently of Participant intervention. Actor plans, deadlines, institutions, scheduled developments, and other causal processes may continue unless altered or prevented; Participant inaction can therefore be causally meaningful.
- **Relocated authorial burden:** Enclave does not eliminate authoring work. It moves much of the burden from enumerating paths and reactions into constructing the persistent narrative substrate—Actors, Knowledge, relationships, institutions, motivations, constraints, resources, intended developments, and other authored state—from which realized trajectories emerge.

The seam from Section 12 remains:

> the Cognitive Actor chooses an attempt; the world determines and preserves the resulting causal process.

### 14. Worked Examples

Demonstrate the architecture end-to-end without adding new theory, using two compact, freely available published adventures in radically different genres.

Current pair:

- **Fantasy:** *A Wild Sheep Chase* (Winghorn Press).
  - short, single-session D&D 5E adventure;
  - clear authored trajectory expressed through a small number of scenes;
  - three principal full-fidelity Cognitive Actors are sufficient for the worked analysis: Finethir Shinebright, Ahmed Noke, and Guz;
  - transformed guards can remain lower-fidelity unless individual cognition becomes relevant;
  - the useful divergence is social/informational: Participants can deal with Guz as an Actor, discover a competing perspective on Shinebright and Noke, and approach Noke through negotiation rather than simply arriving at the expected showdown.
- **Science fiction:** *Signals* from the free *Star Trek Adventures* Quickstart.
  - very short and strongly sequential;
  - provides a clean published railroad against which to demonstrate divergence;
  - the full-fidelity Cognitive Actor set can be kept to a handful of narratively consequential individuals, principally the mining-colony leader and one or more Romulan leaders;
  - other colonists and troops can remain deterministic, aggregated, or otherwise lower-fidelity Actors unless an Interaction requires individual cognition;
  - the useful divergence is diplomatic/institutional: contact, rescue, bargaining, deception, or cooperation with Romulan survivors can change what the settlement learns and prevent, redirect, or transform the expected final confrontation.

For both examples:

- treat the published sequence as the **authored trajectory**, not as a script Enclave must preserve;
- identify the original expected path;
- represent the underlying Actors, Knowledge, motives, relationships, locations, resources, and intended developments as authored state;
- trace bounded Actor perspective, Knowledge/Memory, context construction, attempted action, authoritative resolution, Interaction/Event formation, propagation, and persistent consequence;
- follow one plausible Participant intervention that the published material does not explicitly enumerate;
- show the resulting alternate realized path through the same authored narrative substrate;
- finish with a side-by-side primitive and authority trace.

The purpose of using two examples is to make the architecture's genre independence visible while keeping the causal chain small enough to inspect directly. The fantasy walkthrough should deliberately demonstrate minor divergence: the broad published trajectory still occurs, but small persistent differences in knowledge, relationships, preparation, and dialogue create meaningful consequences that a classic branching narrative would rarely enumerate. The science-fiction walkthrough should demonstrate major divergence: an early change in Actor relationships and information invalidates the causal prerequisites of later authored events, so the realized narrative departs substantially from the published sequence without selecting a pre-authored alternate branch. Each walkthrough step should explicitly describe the architecture's actual high-level process—not merely say that Enclave adapts—including attempted action, Interaction and authoritative resolution where applicable, Memory/Knowledge/state updates, bounded context construction and cognition for affected Actors, and the concrete divergence produced by those changes.

### 15. Computational Architecture and Scale

Use the *Signals* major-divergence example as the bounded computational reference, then scale outward.

Current authoritative quantitative basis:

- `docs/signals-section15-consolidated-computational-model-2026-10-08.md`.

Reference population:

- 36 settlement Cognitive Actors;
- 5 surviving Romulan Cognitive Actors;
- 1 remote Starfleet Captain while causally relevant;
- 1 surviving *Susquehanna* distress-source Actor while causally relevant;
- **43 model-driven Cognitive Actors total**;
- **1 human Participant controlling 1 Participant Actor**;
- **44 living Actors total** in the simplified computational reference.

The Participant Actor has **zero Enclave cognition inference**. Participant actions increase inference only through downstream model-driven Actor responses.

The current ordinary-day settlement simulator directly models 36 settlers and produces a median:

- **2,197 Interactions**;
- **1,022 model-driven cognition calls**;
- **3.086M model tokens**.

A first-order 43-Cognitive-Actor extrapolation gives:

- **~2,624 background Interactions**;
- **~1,221 model-driven calls**;
- **~3.69M model tokens**.

Participant sensitivity uses one Participant Actor at 2×, 4×, 6×, and 8× ordinary Actor interaction density. With the explicit provisional fan-out assumption of 0.5 added NPC cognition calls per Participant Interaction, the four scenarios span approximately:

- **2,746–3,112 total Interactions**;
- **1,282–1,465 total model calls**;
- **3.945–4.723M model tokens**.

Use responsibility-specific token profiles:

- social/dialogue/complex cognition: **4,000 input / 250 output**;
- routine Actor↔world cognition: **1,500 input / 80 output**.

For storage, retire the earlier ~1,300 and ~10,000 starting-world estimates. Use:

- **100,000–200,000 semantic/world Knowledge records**;
- **150,000 central**;
- **1,000 prior Memories per living Actor**;
- **44,000 prior Actor Memories**;
- runtime growth derived from Interactions:
  - 2 Event records per Interaction (Interaction Event + resulting Event);
  - 1 generated Fact per Event;
  - 1 Memory per participating Actor per Interaction;
  - ~13,339 generated records / ~123.75 MiB for the 43-Cognitive-Actor background; additional cascading Events are possible but are not assumed in the baseline.

At the conservative **~9.5 KiB/vector-bearing record** GottZ/ctx PostgreSQL + HNSW baseline:

- 100k world Knowledge → **~1.43 GiB** post-session vector-bearing Enclave corpus;
- 150k → **~1.88 GiB**;
- 200k → **~2.33 GiB**.

This is **Enclave-only storage**. It explicitly excludes the game engine, terrain/geometry, rendering assets, audio, animation, physics, collision/navigation, conventional non-Enclave game state, binaries, and other content needed to make the game playable.

Do not assign an invented fixed multiplier to Enclave graph/provenance/relationship overhead. Measure those structures separately in an implementation.

Model-driven cognition, deterministic authority, retrieval, persistence, and storage must remain separately accounted. The theoretical *Free Guy*-style persistent MMO world belongs at the end of the section as a scaling/stress endpoint, not at the beginning.

Supporting files:

- `docs/signals-high-fidelity-computational-workload-2026-10-07.md`;
- `docs/signals-settlement-temporal-contact-simulation-2026-10-07.md`;
- `docs/signals-participant-interaction-sensitivity-2026-10-08.md`;
- `docs/signals-computational-evidence-and-assumptions-2026-10-07.md`;
- `scripts/signals_settlement_sim.py`;
- `data/signals-settlement-sim/`.

The social side of the workload is externally anchored only at order-of-magnitude level using published contact/interaction studies; Actor↔world Interaction rates remain explicit synthetic assumptions. External pricing, hardware, vector-storage formulas, and benchmark evidence remain separated from Enclave modelling assumptions in the evidence ledger.
### 16. Practical Applications

Distinguish **implementation fidelity levels** from **deployment scale**. Treat the three levels as a clear hierarchy of capabilities rather than treating regional or MMO simulation as higher narrative-fidelity levels:

- **16.1 All-or-Nothing Architecture?** Brief explanation of selective implementation and preserved architectural invariants.
- **16.2 Reactive Dialogue (Level 1):** Criterion-Driven Dialogue replacing conventional dialogue trees without removing conventional restrictions on narrative progression; provide selectable dialogue choices in addition to open text. No persistent personal Actor Memory required.
- **16.3 Persistent Characters (Level 2):** add personal Memory, opinions and consequences of Participant relationships, while cautioning against frustrating progression blocks.
- **16.4 Reactive Authored Narrative (Level 3):** first level employing the full Enclave architecture for its intended purpose, without requiring broader systemic/world sandboxing; ordinary game activities can remain conventional.
- **16.5 Partial and Hybrid Implementations:** the concrete hybrid *Signals* assignment approved by the author: standard deterministic activities, Level 1 for ordinary settlers, Level 2 for non-officer Romulans, and selectively active Level 3 cognition for the wounded survivor, Ero Drallen, Romulan captain, a conditional settlement representative, and optionally remote Starfleet. Relevant causal Events and Knowledge access stay authoritative. The narrative divergence is possible, not predetermined.
- **16.6 Practical Computational Implications:** interpret three uniform implementations of *Signals* and Manhattan, plus the *Signals* hybrid, using comparative tables and a concise discussion of narrative fidelity, autonomous inference, persistence, and selective cognition.

Current reproducible calculations are **scripts/signals_section16_fidelity_calculations.py**, **data/signals-section16-fidelity-results.json**, the §18 supplement to **docs/signals-section15-consolidated-computational-model-2026-10-08.md**, and the Section 16.6 supplement to **docs/manhattan-test-scaling-2026-10-08.md**.

Regional scaling, online-world concurrency and the theoretical full-world endpoint are **deployment/engineering topics**, not additional fidelity levels. Their prior outline now lives in **docs/appendix-architecture-scaling-outline.md**, pending separate appendix work.

### 17. Conclusion

Restate:

- the Agency-Persistence problem;
- hybrid authority;
- bounded persistent Actors;
- information as world state;
- persistent causal consequence;
- narrative as an emergent trajectory through authored structure.

## Current architectural climax

Sections **12 and 13** are the central pair around which the preceding architecture converges:

```text
bounded persistent Cognitive Actor
    ->
temporary context and reasoning
    ->
attempted action
    ->
authoritative resolution
    ->
persistent cause and effect
    ->
changed informational/physical world
    ->
later bounded cognition
```

Everything before those sections constructs the vocabulary and machinery required for that loop. Sections after them demonstrate operation through worked examples, scale the same architecture computationally, and then discuss practical application.
