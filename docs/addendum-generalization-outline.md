# Addendum A — Generalization Beyond Interactive Narrative

> **Working outline.** The main paper is intentionally framed around interactive media. This addendum considers which parts of Enclave describe a more general architecture for reactive Actors operating within controlled persistent information environments.

## A.1 Narrative Terminology as a Domain-Specific Surface

Several Enclave concepts can be expressed without narrative-specific assumptions.

At a generalized level:

- **Facts** remain persistent information;
- **Memories** remain Actor-specific persistent experiential/identity state;
- **Events** remain authoritative occurrences;
- **Loci** remain points through which information can be retained, received, exposed, transmitted, or acted upon;
- **Actors** remain persistent causal entities;
- **Participants** become externally reasoned Actors;
- **Domains** remain semantic classification;
- **Interactions** remain Events characterized by causal process;
- **Enclaves** remain population-linked specialized Domains;
- **Rank** remains a specialized subordinate Enclave;
- **Facets** remain identifiable entities expressed through multiple independent Enclave hierarchies;
- **Combinatorial Enclaves** remain intersections of contextual populations;
- **Inheritance** remains parent-child implication and a computational reduction mechanism.

The seven foundational primitives remain separate from these derived structures.

## A.2 Environment Architecture Rather Than Agent Memory

Enclave should be distinguished from systems whose primary purpose is to improve the memory of one agent.

Its central concern is the structure of the **environment in which many persistent Actors operate**.

The environment controls:

- authoritative state;
- information availability;
- provenance;
- causal consequence;
- access boundaries;
- persistent shared history;
- institutional information;
- information distribution.

Individual agent memory is one component of a larger persistent information architecture.

This is the core of the **agent-native environment layer** framing.

## A.3 Persistent Bounded Autonomous Actors

The generalized architecture distinguishes:

1. complete authoritative/environment informational state;
2. persistent Actor-accessible subjective state;
3. temporary active context for one cognitive operation.

A generalized Actor can therefore persist independently of any model invocation.

The model, decision process, or controller may be replaceable while:

- identity;
- Memory;
- Knowledge;
- relationships;
- access;
- goals;
- consequences;

remain persistent.

General rule:

> **Epistemic boundaries determine what an Actor can know; retrieval determines what the Actor is presently attending to.**

## A.4 Autonomous Multi-Agent Systems

The architecture may apply to environments containing multiple autonomous software agents.

Different agents can operate from different Knowledge while sharing one authoritative system state.

Events provide a common mechanism for accepting persistent consequences.

Enclaves, Rank, Facets, Combinatorial Enclaves, and Inheritance may map to combinations of:

- organizational membership;
- service boundaries;
- roles;
- permissions;
- expertise;
- geography;
- institutional affiliation;
- operational context.

The useful distinction is not that every software system should literally adopt Enclave terminology, but that many-agent environments benefit from persistent external state and bounded Actor-local cognition.

## A.5 Information Distribution as Operational State

Information distribution can itself be persistent operational state.

A generalized implementation may represent:

- which agents know a datum;
- which repositories expose it;
- which organizations have institutionalized it;
- which populations receive it;
- which contradictory versions coexist.

Saturation and Institutional Emission can generalize into abstractions for broad information diffusion where simulating every individual contact is unnecessarily expensive.

Canonical/authoritative truth remains separate from distribution or consensus.

## A.6 Simulation and Training Environments

Persistent information asymmetry and causal state may be useful for:

- training simulations;
- synthetic societies;
- organizational simulations;
- operational exercises;
- adversarial simulations;
- digital-world modelling.

Actors can be given bounded perspectives rather than direct access to simulator truth.

The architecture is compatible with:

- deterministic Agents;
- probabilistic Agents;
- mixed Agent populations;
- variable cognitive fidelity.

## A.7 Robotics and Embodied Systems

In embodied environments:

- Loci may map to sensors, communication systems, records, or shared data stores;
- Events may represent accepted changes in the environment;
- Knowledge may distinguish observation from authoritative state;
- Actor reasoning can remain separate from state estimation and authority;
- temporary planning context can remain distinct from persistent robot/agent state.

Further work would be required to address:

- uncertainty;
- sensor error;
- real-time control;
- safety-critical authority;
- competing state estimates.

## A.8 Organizational and Institutional Systems

Enclaves naturally generalize to organizations and sub-organizations.

Rank can represent role/access depth.

Facets can represent entities—such as facilities, campuses, municipalities, or operational sites—whose relevant populations span multiple independent organizational hierarchies.

Knowledge propagation can model how information moves through institutions without assuming universal awareness.

Saturation / Institutional Knowledge / Institutional Emission can represent the transition from local knowledge to institutionalized dissemination.

Authoritative truth can remain separate from organizational belief or consensus.

## A.9 Generalized Architectural Form

The generalized architecture can be described as:

> **an event-driven system for reactive Actors operating within a controlled persistent information environment.**

Its core invariants are:

- persistent authoritative state exists outside Actor cognition;
- information availability is distinct from information truth;
- Actors operate from bounded perspectives;
- Actor identity persists independently of temporary cognitive context;
- probabilistic interpretation does not automatically alter authoritative state;
- Actors choose attempts and authoritative systems resolve consequences;
- consequences become persistent through Events;
- information can propagate independently of truth;
- different Actors can inhabit different informational perspectives while sharing one authoritative environment.

Generalized runtime:

```text
persistent bounded Actor state
    ->
temporary cognition / decision
    ->
attempted action
    ->
authoritative resolution
    ->
persistent Event / consequence
    ->
changed shared + informational state
```

## A.10 Questions for Further Work

- Which Enclave primitives/derivatives are genuinely domain-independent?
- Which exist specifically because interactive narrative requires them?
- How should uncertainty alter canonical/non-canonical distinctions in real-world systems?
- How do formal security/permission systems interact with Enclaves and Rank?
- How should competing authoritative systems be represented where no single source of truth exists?
- What parts of the architecture map naturally onto distributed agent infrastructure?
- How much narrative-specific terminology should be retained in a generalized formal model?
- Which real-world systems require stronger guarantees than the narrative architecture assumes?
