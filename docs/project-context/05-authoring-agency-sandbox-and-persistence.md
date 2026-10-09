# Authoring, Agency, Sandboxing, and Persistence

## Authoring situations rather than Participant scripts

Important practitioner framing from Justin Alexander:

- do not depend on one predicted sequence of Participant actions;
- prepare situations;
- establish people, motives, resources, constraints, relationships, places, pressures, timelines, and likely developments;
- information flow is a major organizing structure;
- nodes can organize loci of interaction without becoming the ontology of the world.

Enclave extends this logic into a persistent computational architecture.

Authors can establish **intended trajectories**:

- plans;
- goals;
- expected developments;
- conditional Events;
- antagonist intentions;
- dramatic destinations.

These remain conditional on the world developing in compatible ways.

## Branching is a state-space problem

The paper should not trivialize branching as merely a tree-of-scenes issue.

Meaningful Participant or Actor action can alter:

- relationships;
- location;
- resources;
- Knowledge;
- belief;
- Actor plans;
- institutional state;
- future Event eligibility;
- later dialogue;
- future opportunities.

Persistent consequence means later narrative must remain compatible with combinations of earlier state.

That is the branching tax.

Traditional systems manage it through:

- reconvergence;
- restricted action vocabularies;
- shallow consequence;
- isolated side content;
- explicit state rules;
- state machines;
- behaviour trees;
- planners;
- drama managers;
- conditionally available authored content.

These are useful techniques, not failures. Their historical limitation is that meaning generally had to be explicitly formalized.

## Gamemaster analogy

Human Gamemasters demonstrate that broad agency and authored narrative can coexist.

A GM can interpret an unforeseen action relative to:

- current circumstances;
- established world Facts;
- prior Events;
- rules;
- Actor Knowledge;
- goals;
- plans;
- plausible consequences.

The GM reasons outward from the world rather than only selecting from a predetermined interaction catalogue.

The problem is scale. Persistent human GM coverage is constrained by:

- attention;
- working hours;
- concurrency;
- memory;
- staffing;
- geographic/server coverage;
- cost.

Historical persistent-world/live-content examples are used as evidence that human intervention is valuable but economically difficult to scale.

## Machine intelligence changes the formalization bottleneck

Probabilistic systems can perform much of the interpretation previously requiring humans:

- interpret open-ended input;
- infer intent;
- reason over prose;
- identify relevance;
- retrieve context;
- infer Actor motivation;
- propose behaviour;
- generate dialogue;
- adapt to novel combinations of circumstances.

This increases practical agency without requiring every interpretation to exist as a predefined rule.

The important modern possibility is not merely "generated dialogue." It is a **bounded narrative agent** operating on behalf of a persistent Cognitive Actor.

Such an agent can reason from:

- authored identity;
- persistent Memory;
- accumulated Knowledge;
- relationships;
- goals;
- current circumstances;
- incomplete/false beliefs;
- legitimate informational access.

The agent can therefore improvise while remaining situated inside a deeply authored world.

## The Agency-Persistence Gap

Broad agency requires flexible interpretation of unforeseen actions.

Meaningful agency requires the consequences of those actions to persist.

Increased interpretive freedom therefore creates increasing quantities of relevant persistent state.

The systems that supply interpretive flexibility are poor sole custodians of that state.

This is the **Agency-Persistence Gap**.

### Deterministic/computational strengths

- durable persistence;
- exact representation;
- identity;
- chronology;
- indexing;
- retrieval;
- constraints;
- validation;
- reproducibility;
- consistent rule application.

### Deterministic/computational weaknesses

- poor semantic improvisation;
- weak handling of ambiguity without explicit machinery;
- difficulty interpreting novel human action;
- adaptation usually requires formal representation.

### Probabilistic/interpretive strengths

- improvisation;
- contextual reasoning;
- semantic interpretation;
- ambiguity handling;
- generalization;
- intent recognition;
- analogical reasoning;
- adaptation to novel circumstances.

### Probabilistic/interpretive weaknesses

- finite/effectively limited active context;
- imperfect exact recall;
- interference;
- inconsistent use of supplied information;
- weak inherent provenance/identity guarantees;
- reconstruction rather than exact replay;
- unreliable large-scale persistent state maintenance without external machinery.

The rhetorical comparison belongs **after** the gap has been established.

## Enclave as response

Enclave treats the gap as an architectural boundary.

Probabilistic systems do what they are good at:

- interpretation;
- contextual judgement;
- Actor reasoning;
- ambiguity resolution;
- proposal generation;
- natural expression.

Conventional systems do what they are good at:

- persistence;
- identity;
- canonical state;
- validation;
- constraints;
- exact history;
- durable consequence.

Human authors provide meaning and possibility.

The resulting Actor/runtime distinction is:

> **the Actor is persistent; the model invocation is temporary.**

The Actor's identity, Knowledge, Memory, relationships, goals, and consequences remain outside the context window.

## Sandbox argument

World sandboxing is already highly developed:

- broad combinatorial outcomes can emerge from finite rules and affordances;
- unenumerated world Events can still be valid;
- persistent simulation can maintain enormous state.

The limitation is not that sandbox games cannot produce stories. They can produce strong **emergent narrative**.

The distinction the paper needs is:

- **systemic emergence** — simulation produces unenumerated Events;
- **emergent/player-constructed narrative** — Participants interpret those Events as stories;
- **reactive authored narrative** — authored characters, conflicts, information, themes, and planned developments absorb those Events and continue coherently.

Enclave targets the third.

The aim is to sandbox **authored narrative consequence** in the same broad sense that simulations sandbox world consequence.

## The central coupling

The architecture ultimately couples two mechanisms:

### Bounded independent cognition

Cognitive Actors operate from persistent, incomplete, Actor-specific subjective state.

A narrative agent can interpret circumstances and choose an attempted action without being granted omniscient author/world context.

### Persistent narrative cause and effect

The attempted action is resolved by authoritative systems.

Consequences become persistent Events/state and alter the physical/informational world from which later Actors reason.

This loop creates the desired narrative property:

```text
authored world
    ->
bounded unsupervised Actor response
    ->
persistent consequence
    ->
changed authored world
    ->
new bounded Actor response
```

The resulting possibility space is combinatorial rather than explicitly authored as a branch tree.
