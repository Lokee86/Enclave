# Ontology and Primitives

## Latest settled model

The current ontology contains **seven foundational primitives in three families**.

### Knowledge family

1. **Facts**
2. **Memories**
3. **Events**

### Nexus family

4. **Loci**
5. **Actors**
6. **Participants**

### Classification family

7. **Domains**

This supersedes both:

- the older "Knowledge / Nexuses / Domains as three foundational primitives plus six derivatives" framing;
- the later temporary "three families of three primitives" framing in which Enclaves and Rank were treated as foundational.

The important result is that the foundation is intentionally small. More specialized operational structures are derived from these primitives in Section 10.

## Why three families

The three families answer complementary dimensions of the system:

- **Knowledge:** what information, experience, and occurrence persist?
- **Nexuses:** where is information situated/exchanged and where can agency enter the world?
- **Classification:** within what semantic context does Knowledge belong?

The families are conceptual, not a storage hierarchy.

## 1. Facts

Facts are discrete persistent informational representations.

"Fact" is an architectural term and does **not** necessarily mean objectively true.

A Fact may represent:

- canonical world state;
- observation;
- report;
- claim;
- rumour;
- testimony;
- belief statement;
- deduction;
- misinformation;
- lie;
- outdated information;
- incomplete information;
- prediction;
- plan;
- other narratively meaningful propositions.

Therefore:

- existence is separate from truth;
- persistence is separate from authority;
- availability is separate from belief.

Canonical Facts are accepted by the authoritative system as true of the persistent world. Non-canonical Facts may exist, propagate, become institutionalized, and cause real behaviour without becoming true.

Facts should generally be stored independently of individual Actors where practical so multiple Actors can reference shared Knowledge without unnecessary duplication.

## 2. Memories

Memories are Actor-specific persistent records of interaction, experience, identity, and subjective history.

A Memory may preserve:

- who was present;
- what was said;
- what was observed;
- actions and sequence;
- location and circumstances;
- emotional/contextual information;
- references to Facts;
- references to Events;
- interpretations;
- unresolved plans or conflicts;
- Actor-specific authored context;
- details that may never become globally important.

Memories contain the authored Actor-specific context necessary for Cognitive Actors to create and maintain a consistent persistent identity.

Memory is richer and generally higher-volume than shared Facts.

A Memory does not automatically become transmissible Fact/Knowledge. Significant information in a Memory may:

- correspond to an existing Fact;
- contextualize an existing Fact;
- introduce a genuinely new Fact;
- remain only inside the Memory.

Memory-derived novel Facts are normally non-canonical unless later validated by authoritative mechanisms.

The conceptual distinction resembles the established episodic/semantic memory distinction:

- Memory preserves contextual experience;
- Facts represent information independently of a particular remembered episode.

Reliquary is a possible memory substrate and useful architectural reference, but Enclave does not depend on Reliquary.

## 3. Events

Events are authoritative persistent records of occurrences accepted as having happened in the running world.

An Event is not merely a claim that something happened.

Inputs to Event resolution may come from:

- deterministic systems;
- Actor actions;
- Participant actions;
- environmental processes;
- authored conditional developments;
- probabilistic interpretation;
- combinations of those mechanisms.

The Event exists only after authoritative resolution.

Events may:

- change world state;
- create/remove/alter represented entities;
- alter relationships;
- change resources or circumstances;
- expose Facts;
- satisfy or invalidate conditions;
- create eligibility for later Events;
- make authored developments possible, impossible, or materially different.

Events create authoritative history. They do **not** imply universal awareness.

Facts spawned from Events are canonical, but Actors may later possess accurate, partial, distorted, false, conflicting, or no information about the Event.

## 4. Loci

A Locus is a point within the narrative world through which Knowledge may be retained, received, exposed, transmitted, or acted upon.

Depending on implementation, a Locus may correspond to:

- ambient observation;
- presence at an Event;
- an entity participating in an Event;
- a physical or informational object;
- an interaction context;
- a book, archive, terminal, recording, broadcast system, etc.

A Locus does not need to be an Actor.

The paper should not force Locus into a universal world-object ontology unless an implementation needs that.

The family is called **Nexuses**; **Locus** is the foundational primitive name.

## 5. Actors

Actors are persistent represented entities capable of acting upon the world.

Action is the defining property.

Actors may be:

- **Simple** — deterministic/rule-driven systems, machines, vehicles, factories, infrastructure, persistent natural phenomena, conventional NPCs;
- **Cognitive** — persistent Actors driven or assisted by narrative agents capable of interpretation, reasoning, planning, communication, adaptation, and novel response.

Actors are not omniscient.

They act using some combination of:

- current state;
- capabilities;
- circumstances;
- accessible Knowledge;
- Memories;
- deterministic logic;
- probabilistic reasoning;
- external Participant input.

Actor authority ends at attempted action. The authoritative world resolves consequences.

For Cognitive Actors, the Actor persists independently of any individual model invocation.

## 6. Participants

Participants are Cognitive Actors whose cognition originates outside Enclave.

In interactive media they are generally human players.

Enclave can authoritatively record:

- what was presented/exposed to a Participant;
- what the Participant externally says;
- what the Participant externally does.

It cannot authoritatively know internal Participant:

- memory;
- belief;
- understanding;
- inference;
- intention;

unless that cognition is externalized.

Participant cognition is therefore an external interpretive boundary.

Participants are not automatically granted Institutional Knowledge merely because an Enclave has institutionalized it; they still encounter Knowledge through represented mechanisms.

## 7. Domains

Domains are semantic classifications describing what Knowledge concerns.

Examples:

- Medicine;
- Engineering;
- Law;
- Navigation;
- History;
- Politics;
- Geography;
- Chemistry;
- Military doctrine.

Domains describe subject matter, not:

- truth;
- authority;
- belief;
- ownership;
- availability;
- Actor membership.

A Fact may belong to multiple Domains.

Domains are intentionally the sole foundational Classification primitive.

# Key Derivatives

The following concepts are important enough to define explicitly but are not foundational primitives.

## Interaction

**Interaction is an Event characterized by causal process.**

Events preserve authoritative occurrence and consequence. Interaction identifies the causal process through which an occurrence develops.

At theoretical fidelity an Interaction ultimately arises through action, but the degree to which a causal process is decomposed into lower-level Interactions and Events is an implementation/fidelity concern.

## Enclave

An **Enclave** is a specialized Domain associated with an Actor population.

Where Domains classify Knowledge semantically, Enclaves extend classification by relating bodies of Knowledge to bounded contextual populations.

Enclaves may represent:

- geographic populations;
- organizations;
- institutions;
- professions;
- communities;
- cultures;
- religions;
- factions;
- social groups;
- other bounded contextual populations.

Enclaves are frequently cross-Domain.

Membership can contribute to:

- initial Knowledge availability;
- institutional access;
- contextual relevance;
- expected familiarity;
- plausible exposure/transmission;
- permissions;
- social relationships.

Membership does not imply universal Knowledge and leaving an Enclave does not erase acquired Knowledge or Memory.

An ordinary Enclave generally participates in a single inheritance hierarchy.

## Rank

**Rank is a specialized subordinate Enclave intrinsic to every Enclave.**

Each Enclave has its own Rank structure. A numerical scale is the current recommended system representation.

Rank regulates differentiated Knowledge access and related contextual relationships within the parent Enclave while using the same basic Enclave mechanisms rather than requiring a separate foundational classification primitive.

Do not redesign Rank as a standalone primitive.

## Facet

A **Facet** represents an identifiable entity whose relevant context is expressed through multiple independent Enclave hierarchies.

A Facet is not merely a category or optimization bucket. It corresponds conceptually to an entity in the represented world.

A city is the clearest current example.

`Nanaimo` may simultaneously be:

- a Geographic Enclave in `Canada -> British Columbia -> Vancouver Island -> Nanaimo`;
- a Facet relating independent Enclave hierarchies associated with municipal government, policing, criminal organizations, foreign diplomats, schools, healthcare, businesses, neighbourhood organizations, religious communities, and other locally situated populations.

Practical rule:

> If everything underneath a concept can truthfully be represented as descendants of one Enclave hierarchy, a Facet may be unnecessary. If one identifiable entity must be represented through several independent Enclave hierarchies, a Facet becomes useful.

## Combinatorial Enclave

A **Combinatorial Enclave** represents the conjunction/intersection of two or more Enclaves.

Examples:

- `Intelligence + NorthernCommand`;
- `Intelligence + VancouverIsland`.

Ordering should not change combination identity.

Combinatorial Enclaves may cross hierarchy boundaries.

Full semantic combination identity remains valid even when two different combinations resolve to the same Actor population.

For `n` independently combinable Enclaves, the worst-case number of non-empty combination identities is `2^n - 1`.

## Inheritance

Inheritance describes parent-child relationships between Enclaves.

Membership in a child implies membership in its parent and transitively through all ancestors.

Example:

```text
Military -> Army
Army -> Intelligence
Army -> NorthernCommand
```

Membership in `Intelligence` therefore implies `Army` and `Military`.

Inheritance does **not** collapse semantic Combinatorial Enclave identities. Instead, multiple identities may reuse the same underlying population representation.

This yields the important distinction:

> **Combinatorial identity is cheap; population intersection is expensive.**

Inheritance is therefore used to reduce the practical computational burden of an otherwise exponential combination space through hierarchy-aware reuse and elimination of redundant intersections.

Detailed combinatorial mathematics and reduction strategies belong in Addendum B.

# Stress-test result: no additional foundational primitive currently required

Several candidate concepts remain representable without expanding the foundation.

### World state

Represented by canonical Facts plus Events and their consequences.

### Belief

Belief is Actor-specific epistemic stance toward accessible Facts and remembered experience. It does not currently require a universal standalone primitive.

### Claims, rumours, lies, deductions

These are Facts with different status/provenance/canonicality, not new primitive classes.

### Action

Action is part of causal interaction. Attempted actions become authoritative only through Event resolution.

### Causality

Represented through Events, Interactions, Facts, state changes, and subsequent action.

### Provenance

Important, but representable through relationships/metadata among Facts, Memories, Events, Actors, Participants, and Loci.

### Time

A property/dimension of persistent records and state.

### Identity

Persistent infrastructure required by Actors and other entities, not itself a narrative primitive.

### Goals, intentions, plans, desires

Actor state/Knowledge interpreted through cognitive machinery.

### Relationships

Important everywhere and potentially first-class in a concrete graph/data implementation, but not currently required as a universal foundational primitive.

# Ontology vs data model

Do not conflate the ontology with a storage schema.

The seven foundational primitives and six key derivatives describe **semantic roles the architecture needs to reason about**.

They do not dictate:

- tables;
- graph edges;
- IDs;
- object hierarchies;
- storage layout;
- serialization;
- index design;
- one relationship model.

Those belong to implementation.
