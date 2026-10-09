# Decisions, Non-Goals, and Open Questions

## Settled or strongly accepted decisions

### Title

Current title:

*Event-Driven Systems for Reactive Actor Branching Narrative in Interactive Media*

### Human authorship comes first

The paper should establish the value and role of human authorship before introducing the architecture.

Do not frame Enclave as replacing writers.

### Worldbuilding / situation design precedes technical architecture

The paper should show how human authors already think in terms of worlds, situations, Actors, information, pressures, and intended developments before presenting Enclave.

### Branching and agency are one continuous problem

Section 4 is:

**Player Agency and the Branching Narrative Problem**

Do not restore the older split into two adjacent sections.

### The Agency-Persistence Gap is Section 5

The argument must derive the gap before presenting the complementary strengths comparison.

### Sandbox games deserve their own section

World sandboxing is a major precedent.

The paper should not imply sandbox games have no narrative. It should distinguish emergent narrative from **reactive authored narrative**.

### The system overview follows the sandbox section

The narrative-sandbox argument leads directly into the Enclave overview.

### Authority is layered

Capability and authority are different.

- Authors own authored possibility.
- Actors/Participants own attempted action.
- The persistent system owns canonical state and Event resolution.
- Probabilistic systems interpret/propose without becoming sovereign over truth.

### Single authoritative world

Actor disagreement, false information, belief, rumour, institutional consensus, and misinformation do not create multiple canonical realities.

The authoritative system may contain records of false information while remaining the single source of truth in the software-architecture sense.

### Seven foundational primitives

The current foundational ontology is:

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

This supersedes:

- the earlier three-foundational-primitives-plus-six-derivatives framing;
- the temporary three-families-of-three model.

### Six key derivatives

Section 10 currently recognizes:

1. Interaction
2. Enclave
3. Rank
4. Facet
5. Combinatorial Enclave
6. Inheritance

These are important derived structures, not additional foundational primitives.

### Interaction definition

Canonical current formulation:

> **An Interaction is an Event characterized by causal process.**

Do not burden the definition with unnecessary Actor restatement or over-specify causal decomposition. Fidelity determines how deeply causal process is represented.

### Enclave definition

An Enclave is a specialized Domain associated with an Actor population.

Enclaves may be cross-Domain and generally participate in a single inheritance hierarchy.

Enclave membership affects access/relevance/exposure relationships but does not imply universal Knowledge or shared consciousness.

### Rank

Rank is a specialized subordinate Enclave intrinsic to every Enclave.

Do not redesign it as a standalone foundational primitive.

A numerical representation is currently recommended in the paper.

### Facet

Facet now has a much narrower and clearer meaning than older drafts.

A Facet represents an **identifiable entity** whose relevant context is expressed through multiple independent Enclave hierarchies.

A city is the canonical example.

Do not revert to treating "Military," "Profession," etc. as generic Facet buckets merely because they are broad categories. If one ordinary Enclave hierarchy can represent the structure truthfully, a Facet may be unnecessary.

### Combinatorial Enclaves and Inheritance

Combinatorial Enclaves preserve full semantic intersection identities.

Inheritance provides parent-child implication and permits reuse of equivalent Actor populations.

Do not collapse semantic combination identities merely because Inheritance makes their populations equal.

Key phrase:

> **Combinatorial identity is cheap; population intersection is expensive.**

Detailed reduction mathematics belongs in Addendum B.

### Locus remains abstract

Do not force Locus into a universal world-object primitive.

A Locus is a point through which Knowledge may be retained, received, exposed, transmitted, or acted upon.

### No Enclave data model yet

The paper should not imply that the ontology is already a finalized schema.

Relations/edges may become explicit in a concrete implementation, but the theory currently defines semantic roles and invariants rather than storage structures.

### Initial Knowledge graph is demonstrative

Section 11.1 currently describes an authored graph in the form:

`Domains > Facets > Enclaves & Combinatorial Enclaves > Ranks > Memory`

This is demonstrative conceptual structure, not a claim that every implementation must store one literal strict hierarchy in that exact form.

Do not "correct" the phrase **source of truth** merely because some contained Facts may be false. It is being used in the conventional software-architecture sense.

### Knowledge transmission is implementation-flexible

Transmission may be:

- probabilistic;
- deterministic via conventional contact algorithms;
- hybrid.

Do not imply LLM inference is required for information propagation.

### Saturation is now settled at the architectural level

Saturation is **not** Actor promotion.

It describes the degree to which a particular Fact has propagated through the relevant Actor population of an Enclave.

A Fact may be highly saturated in a narrow subordinate/Combinatorial Enclave while remaining rare elsewhere.

The exact Saturation Threshold remains implementation/world-design dependent.

### Institutional Knowledge and Institutional Emission

When a Fact reaches the chosen Saturation Threshold within an Enclave, it may become **Institutional Knowledge**.

Institutionalization means the Enclave can act as a continuing source of the Fact.

**Institutional Emission** is the normal propagation consequence and may represent briefings, records, orders, announcements, training, publications, cultural repetition, etc.

Institutionalization does not necessarily synchronize every member instantly.

Participants do not automatically inherit Institutional Knowledge and must encounter it through represented interactions.

### Information is world state

The distribution of information is part of persistent world state.

The authoritative system may preserve:

- who knows what;
- where a Fact exists;
- which Loci expose it;
- which Enclaves institutionalize it;
- where it is emitted;
- how far it has spread;
- which contradictory versions coexist.

Canonicality remains independent from distribution.

### Enclave is compatible with deterministic simulation

The architecture does not require probabilistic cognition.

A fully formalized deterministic implementation can use the same ontology, information-flow, and causal machinery.

### Primary design purpose is bounded narrative agents

Despite deterministic compatibility, the primary design purpose is to support **faithful, bounded, unsupervised narrative agents** attached to Actors.

These agents operate as inhabitants of the authored world rather than omniscient narrative generators.

### The Cognitive Actor is persistent; the model invocation is not

This is now a major Section 12 invariant.

Persistent Actor identity/state exists independently of any particular model call.

A model invocation is a temporary cognitive process serving the Actor.

This permits:

- model replacement;
- stepped/model-specific calls;
- dormant Actors;
- local/cheap inference;
- deterministic substitutes;
- long-lived identity outside context windows.

### Three informational scopes

Keep distinct:

1. complete world informational state;
2. persistent Actor-accessible subjective state;
3. temporary active context for one cognitive operation.

Canonical formulation:

> **Epistemic boundaries determine what an Actor can know; retrieval determines what the Actor is presently attending to.**

### Narrative-agent authority

A narrative agent determines what the Actor **attempts**.

It does not independently decide what actually happens.

The attempted action returns to authoritative systems for resolution.

This is the seam between Sections 12 and 13.

### Context is disposable

The prompt is temporary.

The inference session is temporary.

The model may be replaceable.

The Actor persists through external identity, Knowledge, Memory, relationships, state, and consequences.

### Reliquary is optional

Reliquary is a strong potential memory substrate and useful reference architecture, but Enclave does not depend on it.

## Terminology and framing to avoid

### Do not say Participant/Actor "enters" a narrative world by default

Prefer that **Actor actions occur within a narrative world that already possesses authoritative state, constraints, and history.**

### Do not call node the ontology

Nodes are useful authoring/design precedent, not Enclave's world ontology.

### Do not claim branching is not the problem

Branching/state divergence is real.

The contribution is reducing how much explicit authoring/formalization each possible divergence requires.

### Do not claim LLMs solve persistence

Context access is not reliable long-term state ownership.

### Do not collapse exposure, belief, and truth

They are distinct.

### Do not claim Enclave invented narrative sandboxing

Prior work exists. Enclave's narrower claim concerns **deeply authored narrative absorbing emergent consequences**.

### Do not over-security-frame bounded context

The framing is narrative authority/access and epistemic fidelity.

A bounded context prevents leakage from Enclave's own omniscient world state, but a third-party pretrained model may still possess source material from training data.

### Do not over-specify implementation

Exact algorithms for transmission, saturation thresholds, forgetting, belief revision, retrieval, model selection, and storage remain implementation choices unless later formalized.

### Do not revive old Facet semantics

Facets are not generic buckets such as "Military," "Profession," or "Geography" merely because those classify related Enclaves.

Facet is now entity-centric and multi-hierarchy.

## Superseded/historical structures

The following may appear in older files and should not be revived without reconsideration:

- Section 4 titled only "The Branching-Narrative Problem";
- separate old agency/branching sections;
- standalone sections organized around "Truth / Information / Belief" as foundational ontology;
- Knowledge/Nexuses/Domains as three foundational primitives plus six derivatives;
- symmetric three-families-of-three primitives;
- Enclave and Rank as foundational Classification primitives;
- Facets as broad category buckets;
- Actor-oriented Saturation/promotion;
- automatic Rank promotion as the primary Saturation consequence;
- a separate late "From Human Gamemastering to Computational Gamemastering" section as mandatory structure;
- a data-model-like interpretation of Locus/Nexus requiring every world entity to be explicitly cast as one;
- the old Section 12 structure centered mostly on retrieval mechanics.

Earlier design exploration used explicit flag-based propagation/promotion ideas. Some implementation inspiration remains, but the current architecture is more precise: Saturation applies to Facts within Enclave populations and can produce Institutional Knowledge/Emission.

An early authoring premise also described writing the underlying narrative "as if there were no players" and giving major characters complete subjective narratives. The evolved framing is broader: authors construct the narrative world, intended trajectories, Actors, information, pressures, and possible developments; Participants then inhabit and disrupt that authored world.

## Working / unresolved questions

### Belief representation

Current preferred abstraction:

- Memory preserves experience;
- Facts persist information;
- belief is Actor-specific interpretation/stance.

The paper still needs to decide how much formal detail belief deserves.

### Forgetting and decay

Default conceptual assumption is persistence of Actor history.

Forgetting can exist but should require explicit mechanism.

Institutional Knowledge can also weaken/disappear/become inaccessible through modeled circumstances.

Exact mechanisms remain unresolved.

### Relationship formalization

Relationships are important but currently incidental at the Enclave-theory level.

If a later formal data model is developed, decide whether relationships become explicit graph edges, Facts, records, or a mixture.

### Cognitive-cycle formalism

Section 12.5 currently gives an illustrative cycle, not a mandatory execution protocol.

Further drafting should decide whether the final paper needs a formal state machine/pseudocode or whether the conceptual sequence is sufficient.

### Section 13 causal architecture

Section 13 is now substantially settled as the second half of the central runtime pair with Section 12.

Key decisions:

- attempted action remains the Actor-side output of cognition;
- once that attempt enters the world, **Interaction** is the causal unit;
- an Interaction is already an Event characterized by causal process and should not be treated as a pre-Event stage;
- failure generally still constitutes an Interaction/Event in the theory, while implementations may choose not to persist trivial failures at lower fidelity;
- the section focuses on **persistent narrative cause and effect**, not on re-solving physical sandbox causality;
- open-ended physical action interpretation is a complementary possibility, not Enclave's principal purpose;
- **temporal cadence** is part of narrative sandboxing: the world may continue progressing without Participant intervention, making inaction causally meaningful;
- authorial burden is not removed but relocated from enumerating paths and reactions into constructing the persistent narrative substrate from which causal histories emerge.

### Combinatorial reduction mathematics

The conceptual mechanism is settled, but formal bounds/algorithms should be developed in Addendum B rather than overloading Section 10.

### Training-data leakage

If the publication-leak caveat remains in final Section 12 prose, it should be independently sourced.

The runtime architecture can prevent omniscient context leakage from Enclave state, but cannot guarantee that a third-party pretrained model has never seen published source material.

### Generalization

The agent-native controlled-information-environment framing remains promising, but should stay primarily in an addendum/future work unless it can be included without diluting the narrative thesis.

### Open implementation details

Intentionally left to implementations:

- exact Event validation;
- transmission rules;
- Saturation thresholds;
- Domain taxonomy;
- Enclave construction;
- Rank representation;
- Facet storage/association;
- Combinatorial Enclave indexing;
- Inheritance representation;
- retrieval algorithms;
- prompt/context construction;
- model routing;
- variable simulation fidelity;
- authoring UI;
- storage engine;
- distributed execution.

## One-sentence architectural invariant

Enclave lets probabilistic systems **interpret and propose**, lets Actors and Participants **choose attempts**, lets deterministic/persistent systems **decide and preserve what actually happened**, and lets human authors **define the meaningful world in which those consequences matter**.
