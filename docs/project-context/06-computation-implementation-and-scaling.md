# Computation, Implementation, and Scaling

## Architecture is implementation-independent

Enclave should specify invariants and responsibilities rather than one concrete stack.

Potential implementations may vary in:

- storage;
- graph model;
- Event processing;
- classification;
- retrieval;
- transmission;
- belief representation;
- decision models;
- language models;
- authoring tools.

Reliquary is a plausible memory/storage substrate because the design benefits from persistent deduplicated information, references, graph relationships, historical storage, provenance, and selective retrieval.

Reliquary is **not** an architectural dependency.

## No Enclave data model yet

The paper currently has:

- a seven-primitive ontology;
- six key derivatives;
- authority rules;
- an information-flow architecture;
- a working Cognitive Actor runtime model;
- causal interaction principles;
- scaling principles.

It does not yet prescribe:

- entity schemas;
- edge schemas;
- storage layout;
- record identifiers;
- database choice;
- serialization;
- query language;
- one graph representation.

Do not turn the ontology into a database specification.

## Persistent Cognitive Actor

A major runtime invariant is:

> **The Actor is persistent; the model invocation is not.**

A Cognitive Actor's persistent identity may include:

- authored character/personality;
- Knowledge;
- Memories;
- relationships;
- goals/motivations;
- Enclave membership;
- Rank;
- physical/social circumstances;
- prior actions and consequences.

This state exists outside any particular inference session.

Consequences:

- cognition can stop/resume without reconstructing identity from scratch;
- models can be swapped without changing the Actor;
- different operations can use different models;
- inactive Actors need not consume continuous inference;
- deterministic behaviour can substitute where probabilistic cognition adds little value.

## Three informational scopes

The current runtime model distinguishes:

1. **complete world informational state** — everything the authoritative system represents;
2. **persistent Actor-accessible/subjective state** — what a particular Actor can legitimately know, remember, observe, or access;
3. **temporary active context** — the subset assembled for one cognitive operation.

This distinction should remain explicit.

A useful formulation is:

> **Epistemic boundaries determine what an Actor can know; retrieval determines what the Actor is presently attending to.**

Retrieval must never treat semantic relevance as permission to cross the Actor's epistemic boundary.

## Subjective world

A Cognitive Actor's subjective world may include:

- acquired Facts;
- Memories;
- Enclave-derived Knowledge;
- Rank-derived access;
- accessible Loci;
- relationships;
- current location/circumstances;
- goals;
- known recent Events;
- incomplete, distorted, outdated, or false Knowledge.

This subjective state persists even when the Actor is not currently receiving inference.

Different Actors can inhabit different informational worlds while sharing the same authoritative reality.

## Context construction

A long-lived Actor may accumulate far more Knowledge/Memory than should enter one invocation.

Temporary context can therefore be assembled from factors such as:

- current Interaction/trigger;
- current Actors/Participants;
- location and circumstances;
- goals/motivations;
- relevant Knowledge;
- relevant Memories;
- causally related Events;
- relationships;
- accessible Loci;
- provenance;
- recency/temporal relevance;
- unresolved plans/conflicts.

The context should contain enough of the Actor's world to reason faithfully without attempting to reproduce the entire persistent Actor.

The model's general pretrained knowledge remains an outside source unless an implementation constrains it further. The paper explicitly acknowledges the risk that published narrative material could appear in model training data; avoiding that completely may require an internally controlled model.

## Cognitive cycle

Section 12 uses the following representative cycle:

```text
trigger
  ->
identify Cognitive Actor
  ->
construct bounded context
  ->
retrieve relevant Knowledge / Memory
  ->
interpret Actor-local circumstances
  ->
reason from identity / goals / beliefs / constraints
  ->
select or propose action
  ->
express dialogue/behaviour if needed
  ->
submit attempted action to authoritative systems
  ->
resolve world consequence / Event
  ->
return appropriate consequences to Actor/world
  ->
update Memory and persistent informational state
  ->
discard temporary context
```

The stages are illustrative, not mandatory.

The critical authority boundary is:

- the narrative agent determines **what the Actor attempts**;
- authoritative systems determine **what actually happens**.

This is the seam between Sections 12 and 13.

## Divided cognitive responsibility

The cognitive cycle need not be one monolithic probabilistic call.

Different stages may use:

- deterministic systems;
- retrieval/index systems;
- small local models;
- larger general models;
- specialized decision models;
- dedicated interpretation models;
- dedicated dialogue models;
- combinations.

Separate operations may perform:

- retrieval;
- relevance assessment;
- Knowledge extraction;
- Memory classification;
- intent interpretation;
- deliberation;
- Actor decision-making;
- dialogue generation;
- consequence proposal.

Model choice is therefore an implementation/fidelity decision, not part of Actor identity.

Expensive inference can be reserved for difficult semantic reasoning while routine behaviour remains cheap or deterministic.

## Persistent Memory

Memory is the Actor-specific continuity layer.

Shared Events happen in the world; each Actor may remember them differently according to what it perceived and experienced.

Memory may preserve:

- encounters;
- conversations;
- observations;
- interpretations;
- decisions;
- successes/failures;
- relationships;
- emotionally/motivationally relevant experiences;
- unresolved plans/conflicts.

Relevant Memories can be retrieved later instead of keeping the Actor's entire life in active context.

Persistence and present salience are separate properties. A Memory may become less likely to enter routine context without becoming false, invalid, forgotten, or deleted, and later circumstances may make old Memory salient again.

This allows Actor history to grow without forcing model context to grow proportionally while preserving long-range recall.

Reliquary is one plausible reference architecture for durable Actor Memory, semantic retrieval, temporal relationships, deduplication, provenance, and persistence outside context.

## Reliquary as a Section 12 reference architecture

The current Section 12 treatment should discuss Reliquary directly rather than merely naming it.

Relevant architectural correspondences:

- Reliquary keeps durable Memory outside model context/inference.
- It separates source-history retrieval, semantic Memory retrieval, graph traversal, provenance expansion, and context composition.
- Memory-Web retrieval can combine vector similarity with graph-derived Community routing instead of uniformly searching/loading an entire history.
- Provenance can expand a retrieved Memory back to supporting source history.
- Its scope architecture keeps ownership, access, and retrieval/composition as separate questions.
- Its Freshness mechanism demonstrates **salience without deletion**:
  - old Memories may become stale/dormant while remaining stored and retrievable;
  - Freshness is not truth, contradiction, confidence, validity, or archival state;
  - accepted use and related activity can reinforce older Memory.
- This maps directly onto the Section 12 distinction:
  - epistemic boundaries determine what belongs to an Actor's subjective world;
  - retrieval/salience determine what the Actor attends to now.

Reliquary remains illustrative rather than normative. Enclave still owns the requirements for Actor-specific epistemic access, world information distribution, and Event authority. Another implementation may satisfy the same requirements with different memory, graph, salience, or retrieval machinery.

## Context is disposable

Model context is not the Actor and not the world.

The prompt is temporary.

The inference session is temporary.

The model itself may be replaceable.

The Actor remains persistent because external systems retain identity, Knowledge, Memory, relationships, state, actions, and consequences.

This is a direct response to the Agency-Persistence Gap.

## Event-driven activation

Actors do not need to think continuously.

Possible activation triggers:

- Participant enters perceptual range;
- new Fact becomes available;
- timer/scheduled obligation fires;
- relationship changes;
- Enclave/institution issues order;
- owned resource changes;
- watched condition becomes true;
- Event targets Actor/relevant Enclave;
- internal goal reaches a decision point.

Background Actors can remain dormant until relevant.

This makes Enclave resemble an event-driven distributed system more than a continuously inferred society.

## Variable simulation fidelity

Different Actors can operate at different fidelity:

```text
aggregate population
    ->
lightweight persistent Actor
    ->
rules / utility decision
    ->
small local model
    ->
high-capability reasoning model
```

Narrative importance and computational cost should be separable from total population size.

A background Actor may never receive individual inference.

A recurring NPC may use compact state and a cheap decision model.

A pivotal character may receive expensive reasoning.

## Local dialogue inference

Once the system already knows:

- speaker identity;
- accessible information;
- current belief;
- goal;
- recent Event;
- selected action/decision;

natural dialogue realization may be comparatively cheap.

Frontier-scale inference need not be the default.

## Combinatorial Enclave scaling

A set of `n` independently combinable Enclaves admits up to:

```text
2^n - 1
```

non-empty Combinatorial Enclave identities.

The architecture should preserve useful semantic combination identity without blindly calculating every population intersection.

Current principles:

- derive relevant combinations primarily from actual Actor memberships rather than Fact power sets;
- preserve canonical semantic identities;
- use Inheritance to reuse equivalent populations;
- allow transitive ancestor implication;
- avoid recalculating intersections already implied by hierarchy;
- use Facets to structure meaningful multi-hierarchy entity contexts without flattening them into one tree.

Important distinction:

> **Combinatorial identity is cheap; population intersection is expensive.**

Detailed mathematics/reduction strategies should live in Addendum B.

## Participants and combinatorial/saturation machinery

Participants should not be silently treated as ordinary simulated population members for automatic saturation/institutional shortcuts.

A Participant acquires and transmits Knowledge through represented interactions.

This preserves the external-cognition boundary.

## Saturation as scaling

Saturation/Institutional Knowledge is partly a narrative mechanism and partly a computational compression mechanism.

Once a Fact is sufficiently widespread within a relevant Enclave population, the system can represent it as Institutional Knowledge and use Institutional Emission rather than simulating every routine pairwise contact.

This trades individual propagation fidelity for an explicit causal abstraction.

## Scaling concern: persistent Memory

Broad agency generates more historical state.

Naively retaining consequential interaction creates at least linear growth in retained history with interaction count.

Storage capacity alone does not solve the problem. The system must also support:

- indexing;
- deduplication;
- temporal interpretation;
- relevance;
- correct identity/entity association;
- source/provenance;
- contradiction;
- supersession;
- bounded retrieval.

External memory solves capacity more readily than relevance.

This is why Enclave separates persistent state from model context.
