# Authority, Interaction, and Information Flow

## Authority as jurisdiction

Enclave requires systems with different capabilities to operate over one world. Capability must remain separate from authority.

Authority is best described as **jurisdiction**.

### Authorial authority

Human authors control the authored structure and intended possibility space:

- initial world;
- characters;
- institutions;
- relationships;
- conflicts;
- motives;
- secrets;
- narrative pressures;
- intended developments;
- possible Events;
- thematic purpose;
- acceptable outcomes.

Authors may intend trajectories without guaranteeing them.

### Knowledge / world authority

The persistent computational system controls:

- canonical Facts;
- accepted Events;
- persistent state;
- identity;
- chronology;
- causal consequence;
- validation of attempted actions;
- the persistent state of information distribution.

Probabilistic systems can interpret canonical state and propose action, but do not silently mutate authoritative reality merely by producing plausible output.

### Actor authority

Actors and Participants control **what they attempt**, not the authoritative result.

An Actor can decide to:

- communicate;
- investigate;
- attack;
- refuse;
- cooperate;
- move;
- deceive;
- reveal information;
- hide information;
- alter plans;
- attempt any other supported action.

The attempted action is then resolved against authoritative circumstances.

## Core causal boundary

The central pipeline is:

```text
Actor/Participant cognition
        ->
attempted action
        ->
authoritative resolution
        ->
Event / persistent consequence
        ->
changed physical and informational world state
        ->
new Actor circumstances and perspectives
        ->
later cognition and interaction
```

Probabilistic interpretation may help determine **what an action means** and what an Actor attempts.

The persistent system determines **what actually happened**.

This is one of Enclave's strongest invariants.

## Single source of truth

Enclave maintains one authoritative running world.

Actors may disagree about it.

Facts inside the world may be false.

Participants may lie.

Records may be outdated.

Memories may be incomplete.

Institutions may adopt false Knowledge.

None of those conditions create multiple authoritative worlds.

This permits **epistemic plurality without ontological plurality**.

"Source of truth" is used in the ordinary software-architecture sense: one authoritative state system may contain records representing false claims without making those claims canonically true.

## Interaction

Interaction is no longer a foundational primitive.

It is a key derivative:

> **An Interaction is an Event characterized by causal process.**

An Event records authoritative occurrence and consequence. An Interaction emphasizes the causal process through which the occurrence develops.

At one fidelity level, "Bill fell and broke his ankle" may be represented as one Event/Interaction. At another, the system may represent many constituent causal processes.

That decomposition is an implementation/fidelity concern.

## Initial Knowledge distribution

The authored Knowledge Base is the universal source from which bounded Actor Knowledge/access is derived.

The current Section 11 framing uses a **demonstrative** authored graph:

```text
Domains > Facets > Enclaves & Combinatorial Enclaves > Ranks > Memory
```

This is not a mandatory database hierarchy.

Actor-accessible Knowledge can be calculated during instantiation from the Actor's authored graph, cumulative Enclave membership, Rank relationships, Domain Rank relationships as currently described in the outline, Actor-specific Knowledge, history, Loci, and other world-specific relationships.

Important distinction:

- the world may contain Knowledge;
- an Actor may have legitimate access to some of it;
- only a subset need be active in cognition at a particular moment.

## Knowledge transmission

Knowledge moves through Interactions involving Actors, Participants, and Loci.

Transmission can occur through:

- direct communication;
- observation;
- records;
- artifacts;
- communication systems;
- computational systems;
- environmental evidence;
- institutional mechanisms;
- other authored/emergent mechanisms.

Transmission may be simulated:

- probabilistically;
- deterministically through conventional contact/propagation algorithms;
- through hybrid mechanisms.

Transmission concerns exposure/availability, not truth.

Canonical and non-canonical Facts can propagate through the same mechanisms.

## Exposure is not belief

Keep distinct:

1. a Fact exists;
2. a Locus can expose it;
3. an Actor encounters it;
4. the encounter may become part of Memory;
5. the Actor may believe, reject, doubt, reinterpret, distort, or repeat it.

A false rumour can therefore be:

- persistent;
- widely exposed;
- widely believed;
- institutionally adopted;
- causally significant;

without becoming canonical.

Likewise a canonical Fact may exist without any particular Actor knowing it.

## Emergent diffusion

Once acquired, Knowledge may continue to move long after the Event or Interaction that introduced it.

Diffusion may be shaped by:

- social relationships;
- geography;
- Enclave membership;
- Rank;
- Inheritance;
- communication infrastructure;
- Actor behaviour;
- institutional processes;
- relevance;
- time.

Actors may retransmit:

- the original Fact;
- an incomplete version;
- a distorted version;
- a derived interpretation;
- a contradictory claim.

This allows rumours, renown, myths, and legends to arise naturally in sufficiently long-lived simulations.

Different regions, institutions, communities, or Actor populations may develop radically different informational states while sharing one authoritative world.

## Transformation and provenance

Communication can transform information through:

- omission;
- summary;
- reinterpretation;
- mistranslation;
- exaggeration;
- deliberate falsification.

When narratively meaningful, transformed Facts should persist separately rather than silently mutate their source.

The world can simultaneously retain:

- authoritative Event;
- accurate report;
- partial summary;
- distorted account;
- fabricated explanation.

Provenance remains important even though it is not a foundational primitive.

## Enclave Saturation and Institutional Knowledge

**Saturation** describes the degree to which a particular Fact has propagated through the relevant Actor population of an Enclave.

It is both:

- a narrative model for information becoming commonly established in a population;
- a cost-efficiency mechanism that can replace large numbers of low-value individual propagation relationships with a higher-level institutional relationship.

Saturation is therefore a relationship among:

- a Fact;
- an Enclave;
- the relevant Actor population within that Enclave.

Saturation is evaluated against the narrowest meaningful contextual population first and can move upward through broader populations as the Fact spreads.

Combinatorial Enclaves are useful for modelling constrained spread across regions, roles, institutions, or other intersecting contexts.

A Fact may be highly saturated in one subordinate or Combinatorial Enclave and remain rare elsewhere.

Saturation does not require every Actor to possess the Fact. It is controlled by an implementation/world-design **Saturation Threshold**.

When that threshold is reached, the Fact may become **Institutional Knowledge** of the Enclave.

Institutional Knowledge means the Enclave itself can reasonably act as a continuing source of that Knowledge.

## Institutional Emission

Institutionalization does not necessarily grant the Fact instantly to every member.

Instead, the Enclave may **emit** the Fact through ordinary institutional mechanisms such as:

- briefings;
- records;
- orders;
- routine communication;
- professional practice;
- documentation;
- public notices;
- announcements;
- publications;
- shared repositories;
- training;
- cultural repetition.

Eligibility may still depend on:

- Enclave membership;
- Rank;
- Loci;
- other contextual constraints.

Participants are not automatically granted Institutional Knowledge. They must still encounter it through an appropriate represented interaction/source.

Institutional Emission is a standard consequence of Saturation regardless of fidelity level, though a low-fidelity implementation may simply assign Knowledge directly while a higher-fidelity implementation may model emission/contact more explicitly.

Institutional Knowledge can weaken, disappear, become inaccessible, or be superseded through narratively represented mechanisms.

## Information as world state

Information distribution is part of the persistent state of the simulated world.

The system can authoritatively represent:

- what Knowledge exists;
- where it is available;
- which Actors possess/encountered it;
- which Loci expose it;
- which Enclaves have institutionalized it;
- where it is emitted;
- how broadly it has propagated;
- which contradictory versions coexist.

For a sandboxed narrative, a change in information distribution is therefore a genuine change in world state.

Informational state itself becomes causal:

- Actors act because of what they know or incorrectly believe;
- institutions act on Institutional Knowledge;
- access enables/prevents Interactions;
- spread/suppression changes future Events.

The authoritative system preserves **the evolving narrative informational state**, not merely canonical truth.

## Cause and effect

Physical and informational consequences coexist.

Example:

- a bridge is destroyed;
- travel becomes impossible;
- a shipment fails to arrive;
- one Actor observes the destruction;
- another hears a false explanation;
- an institution adopts that explanation;
- a faction changes plans;
- an intended meeting becomes impossible;
- later narrative conditions diverge.

Participant and Actor action matter because consequences persist and change the circumstances from which subsequent narrative is produced—not because the author wrote a special branch for that exact action.
