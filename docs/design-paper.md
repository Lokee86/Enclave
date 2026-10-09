# Event-Driven Systems for Reactive Actor Branching Narrative in Interactive Media

> **ARCHIVAL / SUPERSEDED DRAFT.** This file preserves an earlier paper draft and is not the canonical source for current Enclave architecture or section structure. Use `docs/paper-outline.md` and `docs/project-context/` for current decisions.


## 1. Abstract

Interactive narrative traditionally trades player freedom against authorial control. The more ways a player can meaningfully interact with a story, the more branches, dialogue states, contingencies, and consequences authors must anticipate and implement.

Generative models make it possible to respond to interaction without manually authoring every possible line or branch, but systems that delegate narrative authority to those models introduce different problems: characters can acquire knowledge they should not possess, world state can become inconsistent, causality can drift, and the authored narrative itself can lose coherence.

This paper proposes a different architecture.

Human authors create the narrative world, its actors, conflicts, motivations, relationships, intended events, and possible outcomes. Persistent computational state records what exists and what has happened, while each actor retains its own history of observations, communications, experiences, and conclusions. Reactive actors respond from that local history and their current circumstances. Language models and other probabilistic models may interpret player input, assist actor decision-making, retrieve relevant context, and generate natural dialogue, but they do not independently define narrative reality.

The goal is not to automate authorship. It is to make authored narrative **responsive without requiring every possible response to be authored in advance**.

---

## 2. Human Authorship as a Design Requirement

### Working outline

1. **Human creative expression is individual rather than interchangeable.**
   - Writers bring different linguistic habits, experiences, perspectives, cultural backgrounds, associations, and creative instincts to a work.
   - Human writing carries measurable individual and social signatures, and human creativity shows substantially greater variance at the high-creativity end.
   - **Support:** Sourati et al. (2026); Wang et al. (2026).

2. **Narrative depth is created through relationships across the complete work.**
   - Character, theme, subtext, symbolism, pacing, conflict, foreshadowing, emotional development, turning points, and resolution gain meaning through their relationship to one another.
   - Human-authored stories show greater structural diversity, suspense, arousal, and variation in story arcs; expert-oriented evaluation also places more emphasis on thematic development and rhetorical variety than on surface fluency alone.
   - **Support:** Tian et al. (2024); Marco et al. (2025).

3. **Independent human authorship produces substantial creative breadth.**
   - Different authors do not merely produce different wording around the same underlying story.
   - Human-written stories show substantially greater plot-level diversity and much less repetition of plot elements and combinations.
   - **Support:** Xu et al. (2025).

4. **Human authorship is therefore a design requirement of this architecture.**
   - The objective is to preserve **deep, meaningful stories with breadth and depth that challenge and push the edges of philosophy**, while preserving the creative perspectives, long-range intent, and diversity produced by individual humans.
   - Human authorship supplies the larger creative purpose within which interactive events acquire meaning.

5. **Meaningful participation requires meaningful response.**
   - Participant freedom matters only when the world can react to what the participant does.
   - Agency is not merely the availability of inputs or choices; it is tied to meaningful action and perceivable consequence.
   - Interactive-narrative research explicitly treats the maintenance of agency and narrative coherence as a central design problem.
   - **Support:** Hammond, Pain & Smith (2007).

6. **Interactive narrative places unusual demands on human authorship.**
   - Unlike conventional narrative, the audience can intervene in the work.
   - Participants may ignore intended paths, alter event order, combine actions unexpectedly, or attempt things the author never anticipated.
   - This unpredictability is a property of the medium, not a deficiency in human authorship.
   - The tension between pre-authored narrative and user freedom has long been described as the **narrative paradox**.
   - **Support:** Louchart & Aylett (2003).

7. **Conventional interactive authoring mechanisms make broad responsiveness increasingly difficult to express.**
   - Branching creates additional authored content.
   - Persistent choices produce increasing combinations of possible state.
   - More interactions require more conditional logic, alternate descriptions, dialogue, consequences, and testing.
   - Jones identifies **exponential branching**, **combinatorial explosion**, and finite implementation scope as major sources of authorial burden; Jones & Millard later grounded that model in interviews with practicing interactive-narrative authors.
   - **Support:** Jones (2022); Jones & Millard (2024).

8. **Conventional interactive authoring mechanisms therefore tend to produce a poor simulacrum of the intended experience.**
   - One compromise is **pseudo-freeform structure**: the player appears to have broad narrative freedom, but meaningful reactions exist only inside anticipated branches and state combinations.
   - Branches may diverge temporarily and then reconverge, preserving the impression of consequence without supporting permanently divergent narrative states.
   - The other compromise is **open-ended but weakly consequential structure**: the player may explore freely and engage with many optional stories, but those stories often remain compartmentalized from the principal narrative and broader gameplay unless explicitly entered.
   - The first offers constrained consequential freedom.
   - The second offers broader activity with limited narrative consequence.
   - Both approximate a deeply reactive world without fully providing one.
   - **Support:** Stang (2019) for branching-and-converging false choices; Evans (2024) for open-world structures in which exploratory freedom and numerous optional side quests coexist with a comparatively linear main plot.

9. **Research on agency shows that the appearance of freedom can be separated from actual freedom.**
   - Day & Zhu distinguish **theoretical agency**—the autonomy the system actually affords—from **perceived agency**—how much influence the player feels they possess. Their work specifically examines techniques for changing perceived agency without changing theoretical agency.
   - Thue et al. (2011) provide empirical support for this distinction. In a 141-participant study, participants experienced a high-agency story structure while the system selected different subsequent events for different groups. Event sequences selected to better match player preferences produced significantly greater perceived agency without expanding the underlying action space.
   - Stang's analysis of *The Walking Dead* describes a related commercial design pattern: branching decisions repeatedly reconverge, allowing choices to feel highly consequential while many distinct paths ultimately return to largely the same outcomes.
   - Together, this research supports a precise point: **conventional systems can successfully simulate a greater degree of narrative freedom than they actually implement.**
   - This is a useful design achievement, but also evidence of the underlying limitation: perceived reactivity can be increased without actually expanding the causal space of the narrative.
   - **Support:** Day & Zhu (2017); Thue et al. (2011); Stang (2019).

10. **Those limitations constrain both sides of the creative relationship.**
    - Authors cannot reasonably anticipate and explicitly implement responses to everything a participant might attempt.
    - Participants are consequently limited either to actions for which meaningful responses were implemented, or to broader activities whose effects remain largely outside the consequential narrative.
    - The authorial-burden literature locates this problem in the growth of content, state management, and implementation work rather than in any shortage of human creative capacity.
    - **Support:** Jones (2022); Jones & Millard (2024).

11. **The architectural problem is therefore not how to diminish human authorship, but how to extend its reach.**
    - Better interactive authoring mechanisms should allow human-authored worlds, characters, motivations, conflicts, and narrative intentions to respond coherently across a much larger range of participant behavior.
    - Greater participant freedom and deeper human authorship should reinforce one another rather than compete.
    - **Closing thesis:** *The limitation is not human creativity, but the machinery through which human creativity is currently made interactive.*

---

## 3. Authoring as Worldbuilding, Adversarial Design, and Narrative Planning

### Working outline

1. **Human authorship is expressed through worlds as well as sequences.**
   - Narrative meaning can be embedded in places, institutions, relationships, histories, conflicts, objects, information, and affordances—not only in a predetermined chain of scenes.
   - A designed environment can carry narrative purpose before a specific traversal through it is known.
   - Different participants can encounter the same authored material in different orders and combinations without stripping it of authorial intent.
   - **Support:** Jenkins (2004), *Game Design as Narrative Architecture*.
   - **Possible supporting reference:** Louchart et al. (2008), *Purposeful Authoring for Emergent Narrative*.

2. **Interactive authorship should prepare situations rather than scripts for participant behavior.**
   - Participant action is inherently difficult to predict exhaustively.
   - The author can instead establish the circumstances from which consequences follow: people, motives, resources, constraints, relationships, locations, and pressures.
   - “Don’t prep plots, prep situations” is the clearest practitioner formulation of this distinction.
   - This does **not** mean abandoning narrative planning. It means avoiding dependence on one predicted sequence of participant actions.
   - **Support:** Alexander (2009), *Don’t Prep Plots*; Alexander (2015), *Tools, Not Contingencies*.
   - **Supporting:** Alexander (2018), *Smart Prep*.

3. **Intended future developments can still be authored without becoming fixed plots.**
   - Authors can establish likely future events, actor plans, timelines, goals, and dramatic destinations.
   - Those expectations remain conditional on the world continuing to develop in the anticipated way.
   - When participant action changes the situation, future developments are reconsidered from the new state rather than forcibly preserved.
   - This maps well to Enclave’s notion of an **authored trajectory** rather than a fixed event sequence.
   - **Support:** Alexander (2009), *Don’t Prep Plots: Prepping Scenario Timelines*.
   - **Supporting:** Alexander (2026), *Is Node-Based Design Prepping a Plot?*

4. **Information is one of the principal structures through which narrative possibility is organized.**
   - What participants know determines what they can understand, pursue, question, reveal, conceal, or interfere with.
   - Important information should not depend on one brittle discovery path.
   - Revelations can be separated from the particular clues or routes by which they become available.
   - Node-based design increasingly becomes a design of **knowledge flow**, rather than simply a map of scenes.
   - **Support:** Alexander (2008), *Three Clue Rule*; Alexander (2010), *Node-Based Scenario Design – Part 3: Inverting the Three Clue Rule*; Alexander (2018), *Using Revelation Lists*; Alexander (2020), *The Secret Life of Nodes*.
   - **Jenkins connection:** environmental storytelling also treats narrative space as a distribution mechanism for information.

5. **Narrative structure can arise from the diegetic organization of the world itself.**
   - People, places, organizations, events, and activities can become loci of interaction because of their actual relationships in the fictional world.
   - Structure does not have to be imposed purely as an abstract scene graph.
   - This is particularly important for Enclave because “node” should not become the ontology of the world.
   - **Support:** Alexander (2010), *Node-Based Scenario Design – Part 9: Types of Nodes*; Alexander (2020), *Naturalistic Node Design*.
   - **Boundary reference:** Alexander (2020), *Nodes Aren’t Everything*.
   - Important takeaway: **node structure and evolving world state are not the same thing.**

6. **Actors give authored situations motion.**
   - Actors should have goals, resources, relationships, knowledge, and plans rather than simply waiting for a participant to trigger a scripted branch.
   - Opposition and conflict can arise from what actors want and are capable of doing.
   - The world can also act **toward** the participant through proactive actors and events rather than remaining passively discoverable.
   - This is a better framing of adversarial design: not “predict every way the participant can break the plot,” but “construct actors and institutions capable of meaningful response.”
   - **Support:** Alexander (2009), *Don’t Prep Plots*; Alexander (2011), *Advanced Node-Based Design – Part 1: Moving Between Nodes*; Alexander (2015), *You Will Rue This Day, Heroes!*.
   - **Supporting:** Alexander’s scenario-timeline material.

7. **Authored narrative material can be conditional rather than sequential.**
   - Storylets demonstrate that authored content can exist independently and become available when prerequisites are satisfied.
   - Completed content can alter shared state, which changes what becomes possible next.
   - This permits deliberate narrative arcs without encoding every route through them as a branch tree.
   - **Support:** Short (2019), *Storylets: You Want Them*; Short (2019), *Storylets Play Together*.
   - **Supporting practitioner references:** Failbetter Games, *StoryNexus Developer Diary #2*; *Echo Bazaar Narrative Structures, Part Two*.
   - Useful distinction: **Alexander’s nodes mainly organize loci of interaction and information; storylets organize conditionally available authored narrative material.**

8. **Emergent sequence is a form of participant authorship within a purposefully authored world.**
   - Human authors define the world, its meaningful structures, conflicts, actors, information, and possibilities.
   - Participants meaningfully author part of the realized narrative by determining which authored forces they encounter, disrupt, combine, or redirect.
   - The realized sequence can therefore emerge through interaction among authored structures without implying that authorship has disappeared.
   - **Support:** Louchart et al. (2008), *Purposeful Authoring for Emergent Narrative*.
   - **Jenkins connection:** narrative architecture provides a useful account of how authored meaning can persist even when traversal and event order are not fixed.

9. **Authorial leverage should be understood as increased narrative richness for a given amount of authoring work.**
   - The objective is not merely to reduce the number of explicit branches.
   - If authors do not have to pay the full **branching tax** for every meaningful possibility, the same creative effort can instead be spent on richer characters, deeper relationships, more factions, more consequential information, more authored situations, more thematic material, and more alternative developments.
   - This is the practical promise of authorial leverage: narrative possibility and richness can grow faster than the labour required to enumerate paths.
   - Existing computational narrative systems already explore parts of this idea through drama management, modular dramatic content, and runtime narrative planning.
   - **Support:** Chen, Nelson & Mateas (2009), *Evaluating the Authorial Leverage of Drama Management*; Nelson, Ashmore & Mateas (2006); Mateas & Stern (2005); Rowe & Lester (2013).

10. **Existing formalized approaches remain limited by deterministic representation and the historical lack of efficient probabilistic assessment.**
    - Branches, state machines, storylets, planner actions, drama-manager interventions, and other formal structures can only react to possibilities represented in their state, rules, content, or transition models.
    - These systems can reorganize and select authored material at runtime, but they ultimately remain bounded by what has been explicitly formalized.
    - The fundamental limitation is therefore not only branching itself, but the need for deterministic machinery to decide in advance what situations mean and what responses are available.
    - Historically, general-purpose computation did not provide an efficient mechanism for making flexible probabilistic assessments of novel participant actions, ambiguous situations, actor intentions, and context in the way a human gamemaster can.
    - Modern probabilistic models provide a practical mechanism for making those assessments without requiring every interpretation and response to be enumerated beforehand.
    - This is the missing capability that allows the reactive step to be formalized differently from earlier systems, while leaving authoritative state and consequences under deterministic control.
    - **Support for existing formalized approaches:** Nelson, Ashmore & Mateas (2006); Mateas & Stern (2005); Rowe & Lester (2013); Short (2019); Failbetter Games.
    - **Research note:** the historical claim about the absence or impracticality of general-purpose probabilistic assessment should be independently sourced before final prose if stated as a historical fact.

---

## 4. The Branching-Narrative Problem

### Working outline

1. **The branching problem is fundamentally a state-space problem, not merely a tree-of-scenes problem.**
   - Every consequential participant action can alter multiple dimensions of narrative state: relationships, knowledge, beliefs, resources, locations, faction conditions, event eligibility, and future opportunities.
   - Two stories that arrive at the same nominal scene may therefore represent materially different narrative states.
   - As those dimensions accumulate, the number of meaningful combinations grows rapidly.
   - **Support:** Jones (2022); Jones & Millard (2024); Fisher (2022).

2. **Persistent consequence creates the branching tax.**
   - If earlier actions continue to matter, later narrative material must remain compatible with combinations of earlier state.
   - The cost is not only additional prose or scenes, but conditional logic, state tracking, alternate dialogue, actor behavior, testing, recovery paths, and content needed to keep divergent states meaningful.
   - Reconvergence reduces that cost precisely because it collapses some persistent divergence.
   - **Support:** Jones (2022); Jones & Millard (2024); Alexander (2010), *Node-Based Scenario Design – Part 2: Choose Your Own Adventure*.

3. **Replacing explicit branches with planning or simulation does not remove the underlying representation problem.**
   - A planner can generate sequences that were not individually authored as paths.
   - But the planner still needs its actions, predicates, objects, relationships, preconditions, and effects represented in a machine-readable domain.
   - Porteous et al. identify construction of those narrative planning domains as an authoring bottleneck; Hayton et al. likewise treat acquisition of the underlying planning model as a significant problem.
   - The combinatorial problem can therefore be moved into a formal model without disappearing.
   - **Support:** Porteous et al. (2021); Hayton et al. (2020); Fisher (2022).

4. **Traditional computational architectures are useful foundations and stepping stones toward richer reactive systems.**
   - Finite-state machines, behavior trees, planners, drama managers, state-conditioned content, and related techniques all provide valuable ways to structure, reuse, constrain, and compose behavior.
   - Behavior trees, for example, emerged partly because large finite-state machines become difficult to extend and reuse; modularity makes explicit behavior considerably easier to manage.
   - Drama management and narrative planning similarly improve authorial leverage by selecting, combining, or sequencing authored structures at runtime.
   - These approaches should not be framed as failures. They provide much of the deterministic structure, compositional machinery, and authorial control that remains useful going forward.
   - The opportunity is to augment them with probabilistic assessment so that they can access possibilities that were previously difficult or uneconomical to formalize explicitly.
   - **Support:** Iovino et al. (2022); Riedl & Bulitko (2013); Nelson, Ashmore & Mateas (2006); Rowe & Lester (2013); Short (2019); Failbetter Games.

5. **Interactive systems commonly manage complexity by collapsing causal possibility.**
   - Branches reconverge.
   - Decisions produce temporary variations but return to common states.
   - Side stories remain isolated from the principal narrative.
   - NPC reactions are restricted to manageable predefined states.
   - Unanticipated combinations simply have no meaningful response.
   - These are sensible engineering solutions to a real combinatorial problem.
   - **Support:** Stang (2019); Evans (2024).

6. **Perceived agency can compensate for limited causal agency, but that simulation weakens across successive replays.**
   - A system does not necessarily have to implement enormous causal freedom for participants to feel influential.
   - Research distinguishes actual or theoretical agency from perceived agency, and adaptive presentation or reconverging structures can increase the latter without proportionally increasing the former.
   - On an initial playthrough, hidden reconvergence and bounded consequence can successfully preserve the impression of a much larger possibility space.
   - Across successive replays, repeated outcomes, invariant states, and recurring reconvergence become increasingly visible, exposing the limits of the implemented causal space and weakening the simulation of freedom.
   - **Support:** Day & Zhu (2017); Thue et al. (2011); Stang (2019).

7. **The deeper historical bottleneck was explicit formalization.**
   - Traditional software can execute substantial complexity once relevant meaning has been translated into states, actions, rules, predicates, transitions, or behaviors.
   - The difficult part is turning an unforeseen human action or ambiguous social situation into those formal structures.
   - A human gamemaster can interpret what the participant meant, determine what matters, consider what different actors know and want, judge plausible responses, and decide which rules apply without enumerating those interpretations in advance.
   - Historically, those interpretive steps generally had to be encoded much more explicitly for software.
   - **Support:** Fisher (2022); Porteous et al. (2021); Hayton et al. (2020); Iovino et al. (2022); Hogan & Brennen (2024).

8. **Modern probabilistic models materially change what must be formalized in advance.**
   - Language models can interpret open-ended natural-language situations, retrieve contextual information, reason over prose descriptions, propose actions, and synthesize plausible new candidate events or developments that were not individually enumerated beforehand.
   - This capability is not limited to language models. Large or small learned models can also provide bounded probabilistic judgments for non-language tasks where explicit deterministic enumeration is impractical.
   - These models can therefore extend the reachable possibility space without requiring every interpretation, actor response, or candidate development to be hand-authored as a branch or symbolic rule.
   - **Support:** Park et al. (2023); Hu et al. (2024/2026); Hogan & Brennen (2024).

9. **Probabilistic flexibility does not by itself solve narrative authority.**
   - A model that can plausibly infer or synthesize what might happen can also invent events, actions, facts, or consequences that were never established.
   - Believable behavior is not the same thing as authoritative causal correctness.
   - The same probabilistic capability that expands the possible response space therefore creates a requirement for explicit authority boundaries around what actually becomes canonical.
   - **Support:** Hogan & Brennen (2024); Park et al. (2023).

10. **The new opportunity is not to replace deterministic systems, but to augment them and change what they do and how they do it.**
    - Deterministic systems remain well suited to authoritative state, physical and institutional constraints, permissions, event preconditions, persistence, and validated causal effects.
    - Probabilistic systems can handle interpretation of unforeseen participant actions, contextual relevance, actor reasoning, plausible intentions, semantic ambiguity, and proposal of responses that were never explicitly enumerated.
    - Existing deterministic architectures can therefore shift from trying to enumerate the entire meaningful response space toward validating, constraining, composing, and persisting outcomes proposed through probabilistic assessment.
    - This division of labour has direct precedent in broader AI research: neuro-symbolic systems combine learned models with symbolic reasoning; PAL delegates exact execution to a conventional runtime after an LLM interprets and decomposes the problem; and LLM-Modulo explicitly couples approximate LLM knowledge with external model-based verifiers.
    - This preserves the strengths of prior computational approaches while allowing them to reach narrative possibilities that were previously inaccessible or too expensive to encode.
    - **Support:** Marra et al. (2024); Gao et al. (2023); Kambhampati et al. (2024).

11. **The branching problem can therefore be reframed around the computational constraints that branching makes necessary.**
    - Branching is and remains the practical problem: meaningful divergence creates rapidly increasing combinations of narrative state, authored content, and possible response.
    - As those branches and state combinations accumulate, the system must distinguish them, preserve their consequences, determine which content and rules apply, and carry those differences forward into future interaction.
    - Historically, conventional computation required much of that meaning to be represented explicitly as states, predicates, transitions, behaviors, or other formal structures.
    - Prior narrative architectures greatly improve the reuse, recombination, and management of those representations, and remain valuable components of future systems.
    - Modern probabilistic inference changes which parts of interpretation, reaction, and event synthesis must be enumerated beforehand.
    - Broader neuro-symbolic and LLM-plus-symbolic work supports the same architectural direction: learned systems can supply flexible interpretation or candidate structure while conventional reasoning, execution, or verification machinery retains formal control over correctness and admissibility.
    - Reframed this way, the goal is not to eliminate meaningful divergence, but to reduce the amount of explicit computational structure that each possible divergence requires.
    - What remains is to combine that flexibility with authoritative state, causality, and persistent narrative coherence.
    - **Support:** Marra et al. (2024); Gao et al. (2023); Kambhampati et al. (2024).

---

## 5. Player Agency and the Branching Narrative Problem

The narrative begins with an authored world and some intended trajectory.

Characters have plans. Factions pursue goals. Conflicts develop. Events are expected to lead into other events. The author may have one preferred outcome, several possible outcomes, or merely a broad direction.

A useful analogy is the tabletop gamemaster.

A gamemaster does not normally enumerate every possible action a player could take. Instead, they establish the world, its actors, secrets, conflicts, motivations, likely events, and intended direction. Players interfere with those plans, and the gamemaster interprets the resulting consequences while attempting to preserve both narrative coherence and the internal logic of the world.

Persistent online worlds have repeatedly attempted to add comparable human gamemaster operations, but the labour does not scale cleanly with continuous play. *Ultima Online* relied on large volunteer programs for player support and live in-world activity; contemporary reporting described roughly 500 counselors, scheduled minimum shifts, and individual volunteers working workloads approaching full-time employment before wage disputes helped make the arrangement legally and economically untenable (Brown, 2000). *The Matrix Online* employed a dedicated Live Events Team to interact with players as story characters and advance the world in real time, but former team members later described the model as difficult to scale even across nine servers: an eight-person team sometimes worked twelve- to fourteen-hour days, including fourteen-hour days for ten consecutive days during a major event, while live actors could only be present in a finite number of places at once (Thompson, 2009; Williams, 2009). Even *Asheron's Call*, which updated its persistent world through monthly story events rather than continuous human adjudication, used an eight-person event team that its producer described as operating under effectively permanent crunch (Park, 2003).

These examples do not show that persistent worlds are impossible. They show a narrower problem: **persistent human adjudication at tabletop-gamemaster granularity is expensive, difficult to distribute across players and time zones, and hard to sustain continuously.** As a result, persistent worlds have generally depended on automated rules and static or periodically updated content, with human gamemastering appearing intermittently rather than remaining continuously available.

This architecture allows the author to perform much of that role **pre-emptively**.

> **Research note for this section:** Experimental work on generated versus human-authored stories has found that generated stories can equal or exceed human stories on immediate reader-response measures such as transportation, enjoyment, appreciation, character identification, perceived quality, and absorption in some conditions. Other experiments find no entertainment difference or greater transportation for human-authored stories. This is useful here because the gamemaster model does not require generated narrative realization to be inferior; it separates strong moment-to-moment realization from responsibility for the larger authored trajectory. See Raffloer & Green (2025), Sears & Weisberg (2026), and Appel et al. (2025).

An author may establish:

```text
A -> B -> C -> D -> E
```

as an intended sequence.

Player interference may instead produce:

```text
A -> B -> X -> C' -> F
```

The purpose of the system is not necessarily to force the story back toward `C -> D -> E`.

Its purpose is to determine how the authored world reacts coherently when the intended sequence is disrupted.

### Trajectory as conditional structure

The intended trajectory should therefore be understood less as a fixed script than as a graph of authored possibilities and goals.

An authored event can carry conditions such as:

```text
preconditions
trigger conditions
required actors
required locations
required information
world-state predicates
time windows
invalidating conditions
effects
follow-up opportunities
narrative purpose
```

For example:

```text
EVENT: Vale joins the Crown

requires:
    Vale leadership remains intact
    Crown envoy reaches Vale
    Vale believes alliance is preferable
    no mutually exclusive alliance already exists

effects:
    Crown gains Vale support
    rebellion loses diplomatic leverage

narrative purpose:
    narrow the conflict before the final campaign
```

If one prerequisite fails, the event does not need to be awkwardly forced into existence. The system can mark it unavailable and expose the changed state to other authored events, actor plans, or fallback structures.

This lets authors encode not only **what they expect to happen**, but also **why an event is possible and what dramatic function it serves**.

A trajectory can therefore contain hard dependencies, soft preferences, optional beats, mutually exclusive events, recovery paths, and several acceptable endpoints without requiring every intervening actor response to be explicitly scripted.

This also creates a possible additional dimension: **live narrative intervention**.

A writer, designer, or gamemaster could potentially alter an active narrative during play by introducing:

- new events;
- new information;
- new characters;
- new motivations;
- changed faction plans;
- additional conflicts;
- responses to unexpected player behaviour.

Those additions could enter the same state, event, and information structures as material authored before play.

This allows live in-play narrative development without requiring the system itself to become narratively autonomous.

---

## 6. Different Authority for Different Layers

The architecture assigns different kinds of decisions to the systems best suited to make them. These are **authority boundaries**, not separate versions of reality.

```text
AUTHOR
defines the narrative world, intent,
actors, conflicts and possibilities

        ↓

PERSISTENT WORLD / EVENT STATE
records what exists, what happened,
and which consequences became canonical

        ↓

REACTIVE ACTORS
respond from their own circumstances,
memories, relationships, goals and beliefs

        ↓

LANGUAGE / DECISION MODELS
interpret, reason, retrieve and express
where probabilistic inference is useful
```

A model may determine how a character interprets an ambiguous situation, which response they are likely to attempt, or how they express anger.

It does not independently determine that:

- a murder occurred;
- a character witnessed or learned a secret;
- a door became unlocked;
- a faction changed allegiance;
- an item exists;
- a mission succeeded;
- a plausible statement became an authoritative world fact merely because the model produced it.

The important boundary is therefore straightforward: probabilistic systems may **interpret and propose**; authoritative systems determine what actually occurs and persists.

---

## 7. World State, Actor Memory, and Claims

The architecture only needs two fundamental persistent perspectives:

```text
WORLD STATE
what exists and what has actually happened

ACTOR HISTORY
what a particular actor has experienced,
observed, been told, read, inferred or concluded
```

Claims move between those perspectives through ordinary events and objects.

A conversation is an event. A letter is an object. A broadcast occurs. A witness observes something. If any of those things actually happen, their existence belongs to authoritative world history.

Their **content does not automatically become true**.

For example:

```text
World state:
    The western bridge is intact.
    A forged military report exists.

Report:
    "The western bridge collapsed at dawn."

Byron:
    reads the report
    retains the encounter in memory
    may conclude that the bridge is destroyed
```

Nothing requires a third global reality called "information."

The forged report is real because the document exists. Its proposition is false because the bridge remains intact. Byron's encounter with the report is real because he read it. Byron's belief is actor-local because it is his interpretation of what he encountered.

The same pattern covers eyewitness testimony, rumours, propaganda, mistaken inference, incomplete observation, outdated records, and deliberate lies.

Provenance describes the causal path by which a claim arose and reached an actor. Belief describes what the actor currently makes of their own remembered evidence. Neither has authority to rewrite world state merely by becoming widespread.

This also preserves the useful implementation properties of the earlier design. Shared records or claims can still be globally deduplicated where appropriate, while actors retain references to the encounters that matter to them. Deduplication is a storage strategy, however, not a separate ontological layer.

Reactive narrative therefore depends on a simple asymmetry: **the world has one authoritative history, while different actors possess different histories of that world.**

---

## 8. Claims, Records, and Provenance

Claims arise through ordinary world events and records.

Some propositions are established by the author as facts of the world before interaction begins:

```text
The duke secretly funds the rebellion.
```

Other facts arise because an authoritative event occurs during play:

```text
The player publicly accused the duke at the banquet.
```

Actors can also produce claims about the world:

```text
"The duke fled the capital."
```

That statement might be:

- a truthful eyewitness report;
- a mistaken inference;
- a deliberate lie;
- a forged document;
- a rumour derived from another rumour.

The important persistent question is not simply what the sentence says, but **where it came from and how it was encountered**.

A provenance record may identify:

```text
claim content
source
creation event
time
location
medium
derivation
reliability metadata
supersession relationships
```

An event-derived world fact need not have been authored verbatim beforehand, nor does it need to have been freely invented by a language model. It exists because something authoritative happened.

An actor-generated statement is different: the **act of making the statement** can be canonical even when the proposition expressed by it is unverified or false.

For example:

```text
world event:
    Byron tells Elena that the bridge collapsed

claim carried by the event:
    "The bridge collapsed."

authoritative world state:
    bridge remains intact

Elena's actor history:
    heard Byron claim that the bridge collapsed
```

The architecture therefore preserves the difference between **an event being real** and **the content of a statement being true**.

Event history, records, and actor encounters can remain persistent. Later events may supersede, contradict, reinterpret, or contextualize earlier records without rewriting what actually happened.

---

## 9. Enclaves and Initial Access

Characters belong to overlapping social and contextual groupings referred to here as **enclaves**.

An enclave can represent almost any meaningful population:

```text
region
government
faction
guild
military unit
profession
family
religion
social class
political group
criminal network
organization
community
```

A character may belong to many enclaves simultaneously.

For example:

```text
Lord Byron

Northern Province
Nobility
House Byron
Royal Court
Opposition Faction
Merchant Investor
```

Enclaves provide a natural mechanism for establishing **initial access to information**.

A military order might initially be available only to people belonging to the appropriate army, command structure, and location.

A guild secret may initially be available to senior guild members.

A public proclamation may begin with a much broader audience.

Enclave membership therefore provides a compact way of defining who plausibly begins with access to a claim, record, briefing, or other source without individually assigning it to every character.

Membership should not be treated as magical shared consciousness. An enclave can define eligibility, expected exposure, institutional access, or distribution scope, while the implementation still decides whether a particular actor has actually encountered and retained a given item.

This distinction becomes especially important when enclave membership changes. Joining an organization may grant access to its archives or briefings, but it need not retroactively make every member aware of everything any member has ever known.

---

## 10. Exposure, Communication, and Emergent Diffusion

Claims spread when concrete carriers interact.

If actor A remembers a claim and encounters actor B under circumstances where A chooses or is expected to communicate it, B can acquire a new remembered encounter.

```text
A remembers claim
   ↓
A encounters B
   ↓
A communicates claim
   ↓
B records encounter
   ↓
B may update belief
```

Hearing a claim and believing it are separate transitions.

B may accept the claim, reject it, remain uncertain, compare it with other evidence, or repeat it without believing it.

Once B remembers the claim, B can become another carrier.

```text
A -> B -> C -> D
```

This creates emergent diffusion from local interactions rather than from a global rule that assigns knowledge to actors.

Overlapping enclave memberships create bridges between communities.

For example:

```text
Royal Army
    ↓
soldier
    ↓
soldier's family
    ↓
merchant sibling
    ↓
Merchant Guild
    ↓
another region
```

The system does not need an LLM to decide that a claim "should spread."

It spreads because carriers actually communicate or expose one another to it.

### Information-bearing objects and records

People are not the only carriers.

Information can also be transmitted through objects and media:

```text
message scroll
letter
book
ledger
newspaper
recording
radio
terminal
hard drive
database
network
broadcast
```

An object can contain claims directly or references to shared records.

Access may itself be conditional:

```text
Encrypted Drive

contains:
I18
I44
I91

requires:
credential
OR encryption key
OR sufficient technical capability
```

The general transmission model therefore includes:

```text
actor -> actor
actor -> item
item -> actor
item -> item
broadcast -> population
```

Communication may also transform a claim. Retelling can omit details, summarize, reinterpret, mistranslate, or deliberately falsify content. When that transformation is narratively significant, the transformed claim should receive its own persistent record with provenance linking it to its source rather than silently mutating the original.

The large-scale behaviour resembles a cellular automaton or Game-of-Life system: complex information patterns can emerge from simple local transmission rules.

---

## 11. Enclave Saturation

As information spreads, a sufficiently large proportion of an enclave may encounter the same claim.

At that point, the claim can begin behaving differently within that population.

It may effectively become:

- common professional knowledge;
- public knowledge;
- institutional doctrine;
- a widespread rumour;
- assumed background information;
- a contested claim everyone has heard.

Saturation describes **distribution**, not truth and not unanimous belief.

An enclave can be saturated with a false rumour. It can also be saturated with a true statement that many members distrust.

This makes saturation useful as a computational shortcut. Once exposure crosses an implementation-defined threshold, the system may no longer need to model every ordinary transmission event individually within that enclave. It can treat exposure as presumptive while preserving exceptions for isolated, newly arrived, disconnected, or otherwise unusual actors.

The precise mechanism can vary dramatically according to setting.

A tightly organized military command, isolated medieval village, modern professional community, television network, and internet-connected population should not propagate information in the same way.

Saturation is therefore an architectural concept rather than a prescribed algorithm.

---

## 12. Persistent Actor Memory and Belief

When a character encounters something, that encounter becomes part of the character's persistent history.

An implementation may store the remembered encounter directly or as a compact reference to a shared event, claim, or record.

```text
NPC Byron

remembered encounters:
E18
E44
E91
E103
...
```

Exposure, retention, and belief are distinct concepts.

```text
conditions permit exposure
        ↓
actor encounters event / claim / record
        ↓
encounter persists in actor history
        ↓
actor may form or revise belief
```

If Byron later leaves the Royal Court, he does not suddenly lose what he learned while he was there.

Likewise, changing belief does not require deleting the underlying memory. Byron may first accept a claim, later encounter contradictory evidence, and then decide the earlier claim was probably false while retaining the memory that it was made.

An implementation can therefore model actor cognition as relationships among persistent events, records, and remembered encounters rather than destructive mutation of history.

Forgetting or loss still requires explicit circumstances.

Depending on the narrative, those might include:

- ordinary forgetting;
- memory degradation;
- deliberate memory manipulation;
- neurological injury;
- deletion of stored digital information;
- magical intervention;
- other setting-specific mechanisms.

The default assumption is persistence of actor history, with belief remaining actor-specific and revisable.

---

## 13. Actor Memory and State Retrieval

A significant character could eventually accumulate thousands or millions of remembered encounters, relationships, observations, communications, inferences, and belief revisions.

Those records cannot necessarily be treated as one tightly packed prompt-sized list if the system must retrieve relevant context efficiently.

Physical storage may remain highly compact, but logical organization should support retrieval across dimensions such as:

```text
subject
person
location
event
faction
chronology
relationship
source
provenance
belief state
confidence
contradiction
current narrative relevance
```

Retrieval must respect the same authority and access boundaries as the simulated world.

A character-facing query may search:

```text
the actor's own remembered encounters
actor-specific beliefs and inferences
records the actor can currently access
currently perceivable world state
```

while excluding:

```text
authoritative state the actor has not perceived
other actors' private memories
unencountered secrets
author-only planning state
future events
```

This is an authority and access property of the narrative system, not merely a prompt-engineering preference.

The architecture does not prescribe a specific database or memory implementation.

A system such as Reliquary could potentially serve as one implementation substrate because of its emphasis on persistent, deduplicated, graph-related memory and deterministic retrieval, but Reliquary is not required by the theoretical architecture.

---

## 14. Bounded Searchable Context and Divided Model Responsibility

A reactive model does not necessarily need to receive a fully assembled deterministic prompt for every generation.

The stronger requirement is that the **searchable context available to the model is constrained by authoritative world state and the particular actor's own access and history**.

A character may possess an enormous history of encountered information and belief changes.

The model should be able to operate over the subset that character is actually permitted to use without gaining access to privileged world information.

A possible flow is:

```text
actor-accessible information
        ↓
bounded searchable context
        ↓
retrieval
        ↓
decision / reasoning
        ↓
response
```

The retrieval boundary can therefore do much of the work normally pushed into prompt construction.

It can answer a question such as:

```text
What information relevant to the current situation
could this actor plausibly remember or discover now?
```

without exposing the model to the complete canonical state of the world.

There is substantial room here for stepped calls and divided responsibilities.

For example:

```text
player input
    ↓
semantic interpretation
    ↓
authorized retrieval
    ↓
actor belief / decision update
    ↓
action proposal
    ↓
rules validation
    ↓
authoritative event
    ↓
dialogue / presentation
```

Different stages can use different mechanisms.

A small classifier may interpret intent.

A retrieval engine may locate relevant information.

A decision model may determine likely character behaviour.

A conventional rules system may determine whether the proposed action is possible and what authoritative consequences follow.

A language model may then express the validated behaviour naturally, or it may generate dialogue earlier if that dialogue is itself treated as a proposal subject to validation.

The key invariant is not that every generation receives one perfectly deterministic context packet.

It is that probabilistic systems operate inside a **bounded narrative information environment** and cannot silently acquire authority merely by producing plausible text.

---

## 15. Event-Driven Reactive Actor Branching

The central branching mechanism is interaction between actors, proposed actions, validated events, and consequences.

Players, NPCs, factions, systems, and other narrative actors can form intentions and attempt actions.

An attempted action is not automatically an authoritative event.

The system first evaluates it against current state and rules.

```text
actor decision
    ↓
action proposal
    ↓
validation
    ↓
accepted / rejected / modified outcome
    ↓
authoritative event
    ↓
state + information changes
    ↓
new actor reactions
```

This boundary is critical when probabilistic models participate in actor decision-making.

A model may propose:

```text
"Byron opens the vault."
```

The authoritative system determines whether Byron:

- is actually present;
- can reach the vault;
- possesses a key;
- knows the combination;
- has permission;
- is physically capable of opening it;
- is interrupted by another event.

The model is therefore allowed to be generative without becoming sovereign over causality.

A player likewise does more than choose between prewritten branches.

The player's behaviour becomes part of the causal structure from which future narrative develops.

Reactive NPCs are not merely dialogue generators. They may propose or perform consequential actions such as:

- reveal information;
- hide information;
- lie;
- report another character;
- leave;
- attack;
- cooperate;
- refuse;
- alter a plan;
- warn a faction;
- move an item;
- destroy evidence;
- create or transform information.

When an action is validated, the resulting event may update several persistent domains at once:

```text
world state
relationships
inventory
location
event history
created records or communications
actor exposure / memory
actor-local belief
future event eligibility
narrative trajectory
```

These domains do not all have the same authority. World and event state record what actually occurred; memory and belief record what a particular actor encountered or concluded from it.

The complete cycle becomes:

```text
AUTHORED TRAJECTORY
        ↓
CURRENT STATE
        ↓
ACTOR INTERACTION
        ↓
REACTIVE DECISION
        ↓
ACTION PROPOSAL
        ↓
VALIDATED EVENT
        ↓
CONSEQUENCE
        ↓
ALTERED TRAJECTORY
```

The resulting branch is neither simply pre-scripted nor freely generated.

It emerges from an authored world reacting to actor behaviour through an authoritative causal layer.

This is the central idea behind **reactive actor branching**.

---

## 16. Computational Model and Scaling

The architecture does not require continuously running large language models for every actor.

Most persistent simulation work remains suitable for conventional computation:

```text
event processing
state transitions
information references
enclave membership
contact detection
information transmission
indexes
timers
inventory
location
permissions
relationships
```

Probabilistic inference can be reserved for places where it provides value.

### Event-triggered activation

Persistent actors do not need to be continuously "thinking."

Most can remain dormant until something relevant happens.

```text
event occurs
    ↓
affected actors / enclaves identified
    ↓
relevant state and information retrieved
    ↓
only necessary actors are activated
    ↓
decisions or reactions evaluated
```

A distant shopkeeper with no connection to an event requires no model call and possibly no computation at all beyond persistent storage.

An actor may become active because:

- the player enters perceptual range;
- the actor receives new information;
- a timer or scheduled obligation fires;
- a relationship changes;
- a faction issues an order;
- an owned resource changes state;
- a watched condition becomes true;
- another event explicitly targets the actor or one of the actor's enclaves.

This makes the architecture closer to an event-driven distributed system than to a continuously simulated society.

### Variable simulation fidelity

Not every actor requires the same level of simulation.

A practical implementation may support several fidelity levels:

```text
aggregate population state
        ↓
lightweight persistent actor state
        ↓
rules / utility decision
        ↓
small local model
        ↓
high-capability reasoning model
```

An unimportant background actor may never require individual inference.

A recurring NPC may use a compact persistent state plus a cheap decision model.

A major character in a pivotal scene may justify much more expensive reasoning.

The important point is that **narrative importance and computational cost can be decoupled from population size**.

### Cheap local dialogue inference

Much everyday dialogue may be relatively easy to generate once the system has already established:

- who is speaking;
- what information they have encountered;
- what they currently believe;
- what they want;
- what just happened;
- what decision they have made.

Producing a natural line of dialogue from that state may be suitable for comparatively small, inexpensive, locally hosted models.

Frontier-scale inference need not be the default.

More capable models can be reserved for:

- difficult reasoning;
- ambiguous interaction;
- major narrative moments;
- complex characters;
- unusual situations.

### Decision models

Decision models can provide another layer between deterministic rules and natural-language generation.

```text
CONVENTIONAL ENGINE
world state / events / rules / access
        ↓
DECISION MODEL
what should this actor attempt?
        ↓
VALIDATION
what can actually happen?
        ↓
LANGUAGE MODEL
how is the result expressed?
```

Different models can therefore perform fundamentally different jobs.

A practical system may combine:

```text
deterministic computation
small local language models
specialized decision models
larger reasoning models
retrieval systems
```

The purpose is not to replace conventional computing with inference.

It is to use inference specifically where the combinatorial variability of human interaction makes rigid authored logic expensive or unnatural.

---

## 17. Worked Narrative Example

A worked example can demonstrate the complete architecture through one relatively small disruption of an authored plan.

### Authored setup

Suppose the author establishes the following intended trajectory:

```text
A. Northern Fortress holds
        ↓
B. Royal army redeploys east
        ↓
C. Player is sent to negotiate with House Vale
        ↓
D. Vale joins the Crown
        ↓
E. Rebellion is isolated
```

The world also contains several relevant enclaves:

```text
Northern Army
Royal Court
House Vale
Merchant Guild
Northern Province
```

The author establishes a private military weakness at the fortress, but only the Northern Army command structure initially has access to that information.

### Authoritative disruption

During play, the fortress actually falls before the expected redeployment.

That creates an authoritative event:

```text
E1042:
Northern Fortress captured by rebel forces
```

The event updates world state and creates information derived from direct observation and military reporting.

```text
I2201:
"Northern Fortress has fallen."

source:
Northern Army dispatch

derived from:
E1042
```

The claim is true because it is derived from an authoritative event, but an actor still learns it only if the event, report, or later communication actually reaches that actor rather than by reading global state.

### Diffusion

A surviving soldier receives `I2201`.

The soldier tells a sibling.

The sibling belongs to the Merchant Guild.

The sibling summarizes the report while speaking to a trader, producing a distinct derived claim:

```text
I2208:
"The rebels have broken the northern defenses."

derived from:
I2201
```

The new statement is not identical to the original dispatch. It has its own provenance and may support somewhat different interpretations.

A merchant carries `I2208` south.

Another actor exaggerates it:

```text
I2214:
"The entire northern army has been destroyed."

derived from:
I2208

status:
unverified
```

The architecture can now preserve the real event, a reliable report, a summary, and a false exaggeration simultaneously while keeping each actor's exposure to them distinct from authoritative world state.

### Player intervention

The player encounters `I2208` before the Royal Court's official messenger arrives.

The player travels directly to House Vale and claims that the Crown is losing the war.

Lady Vale retrieves only information she is permitted to access:

```text
I2208
prior reports of northern instability
her knowledge of Crown troop strength
her relationship history with the player
her current political goals
```

She does not receive the hidden authoritative world state or the author's intended future sequence.

A decision process concludes that she should delay committing to the Crown.

That decision produces an action proposal:

```text
Lady Vale postpones the alliance
and orders scouts north.
```

The event system validates that she has the authority and resources to do so.

The accepted action creates new authoritative events.

Those events alter:

```text
House Vale's diplomatic state
the Crown's available support
future military options
new information available to Vale scouts
the eligibility of later authored events
```

The original trajectory:

```text
A -> B -> C -> D -> E
```

has now become something closer to:

```text
A -> X -> C' -> Y -> ?
```

The system does not invent an unconstrained replacement story.

It computes consequences inside the authored world, while the author may already have prepared fallback goals, alternate events, recovery paths, or multiple acceptable outcomes.

This single example demonstrates:

```text
authored trajectory
authoritative world state
information provenance
enclave-based access
local diffusion
information transformation
false claims
persistent actor belief
bounded retrieval
actor decision-making
action proposals
event validation
branching consequences
```

The branch emerges because actors reacted to information produced by a real event, not because a model was asked to improvise the next chapter.

---

## 18. Potential Implementations and Applications

The framework is intentionally implementation-independent.

Different systems could use substantially different:

- storage engines;
- event systems;
- enclave models;
- information and belief indexes;
- decision models;
- language models;
- transmission algorithms;
- authoring tools.

Reliquary may represent one suitable memory substrate for an implementation because the architecture benefits from canonical deduplicated records, persistent references, graph relationships, large historical stores, provenance, and selective retrieval.

The broader architecture, however, does not depend upon it.

Likewise, the framework is not tied to one genre or specific kind of interactive experience. Any narrative system containing persistent actors, authoritative state, asymmetric information, interaction, and authored causality could potentially make use of the model.

Possible applications include:

- role-playing games;
- immersive simulations;
- strategy games with persistent characters and factions;
- interactive fiction;
- live-service narrative worlds;
- educational or training simulations;
- hybrid tabletop/digital experiences;
- author-operated live narrative environments.

The same architecture can support very different degrees of generation. One implementation might use models only for dialogue realization. Another might use them for interpretation and actor decisions while keeping all state transitions conventional. A third might avoid language models entirely and still use enclaves, information provenance, event validation, and reactive actor branching.

The architectural claim is therefore broader than any particular model stack.

---

## 19. From Human Gamemastering to Computational Gamemastering

### Working outline

- Human gamemasters perform several functions simultaneously: maintain world state, remember prior events, distinguish what different characters know and believe, interpret unexpected participant actions, adjudicate what is possible, determine consequences, portray characters, improvise dialogue, advance actor plans, manage pacing, and preserve broader narrative intent.
- Human GMs can move fluidly between these different kinds of reasoning without formally separating them.
- In particular, a human GM can usually distinguish implicitly between:
  - what is actually true;
  - what has merely been claimed;
  - what a character knows;
  - what a character believes;
  - what a character intends to do;
  - whether that attempted action succeeds;
  - what consequences follow;
  - how those consequences alter later plans.
- Human GMs can also respond to participant behaviour that was never anticipated because they reason from the underlying situation rather than requiring a prepared branch.

- Unrestricted language models superficially resemble gamemasters because they are unusually capable at the most visible GM functions:
  - interpreting free-form participant input;
  - reasoning about ambiguous social situations;
  - improvising dialogue;
  - deriving plausible character responses;
  - expressing those responses naturally.
- Those capabilities solve precisely the open-ended interpretive problems that traditional deterministic software handles poorly.
- But they do not by themselves supply the less visible authoritative functions of gamemastering:
  - durable world state;
  - epistemic separation;
  - causal adjudication;
  - chronology;
  - permissions and physical constraints;
  - persistent consequences;
  - stable long-range narrative planning.
- A human GM can keep these distinctions implicitly. A computational gamemaster requires them to be made explicit.

- Enclave therefore decomposes the implicit work of a human GM into explicit architectural responsibilities:
  - what actually exists and happened -> authoritative world state and persistent events;
  - what a particular actor encountered -> persistent actor history;
  - what an actor makes of those encounters -> actor-local inference and belief;
  - actor intent -> actor reasoning and action proposals;
  - GM adjudication -> event validation;
  - consequences -> authoritative state transitions;
  - future plans -> conditional trajectories and triggers;
  - improvisation and portrayal -> probabilistic inference and language generation.

- The same properties that make unrestricted language models inadequate as complete gamemasters are also what make this architecture newly practical.
- Traditional software could already provide reliable state, rules, persistence, and causality, but was poorly suited to interpreting arbitrary participant language and deriving plausible responses to unforeseen situations.
- Modern probabilistic models provide that missing interpretive layer.
- Enclave is therefore enabled by the combination:
  - deterministic systems provide authority, persistence, and causality;
  - probabilistic systems provide interpretation, contextual reasoning, actor response, and natural expression.
- The architectural objective is not to replace the human GM with one model, but to reproduce the **division of cognitive labour** that makes human gamemastering effective while assigning each responsibility to the computational mechanism best suited to it.

**Core proposition:** Enclave is enabled by the fact that modern probabilistic models can perform much of the flexible interpretive work traditionally supplied by a human gamemaster, while the architecture compensates for the fact that those models cannot reliably perform the gamemaster's authoritative functions.

---

## 20. Conclusion

The fundamental objective of this architecture is not to generate stories in place of authors.

It is to make authored stories capable of reacting to combinations of interaction that would be impractical to manually enumerate.

Human authors establish narrative reality, actors, conflicts, plans, secrets, records, constraints, and intended outcomes.

Authoritative world and event state preserves causality and records what actually happened. Each actor separately retains the observations, communications, experiences, and conclusions that reached them.

Actors react to changing circumstances from that actor-specific history and from the world state they can currently perceive or affect.

Probabilistic models can provide interpretation, decision support, retrieval, reasoning, and natural expression where those capabilities are useful, while validated events remain the mechanism by which narrative reality changes.

The result is a branching narrative whose individual responses may never have been explicitly written, while the narrative itself remains grounded in human-authored structure.

The architecture can therefore be summarized as:

```text
AUTHORED WORLD
      +
INTENDED TRAJECTORY
      +
AUTHORITATIVE STATE
      +
ASYMMETRIC INFORMATION & BELIEF
      +
EVENT VALIDATION
      +
REACTIVE ACTORS
      +
SELECTIVE INFERENCE
      =
RESPONSIVE BRANCHING NARRATIVE
```

The central proposition is simple:

**Authors create the narrative. Actors disrupt it. Events make those disruptions consequential. The system makes the authored world capable of responding.**

*This paper presents a theoretical architectural framework rather than a complete implementation specification. Details such as exact transmission rules, enclave saturation, belief revision, forgetting, retrieval strategies, authoring tools, simulation fidelity, and model-selection policies are intentionally left to individual implementations.*

---

## Bibliography

Adams, T. (2021). Characterization and emergent narrative in Dwarf Fortress. In B. Suter, R. Bauer, & M. Kocher (Eds.), *Narrative Mechanics: Strategies and Meanings in Games and Real Life* (pp. 151–160). transcript Verlag. https://doi.org/10.1515/9783839453452-007

Agarwal, D., Naaman, M., & Vashistha, A. (2025). AI suggestions homogenize writing toward Western styles and diminish cultural nuances. *Proceedings of the 2025 CHI Conference on Human Factors in Computing Systems*, Article 1117, 1–21. https://doi.org/10.1145/3706598.3713564

Alexander, J. (2008, May 8). Three Clue Rule. *The Alexandrian*. https://thealexandrian.net/wordpress/1118/roleplaying-games/three-clue-rule

Alexander, J. (2009, March 23). Don’t prep plots. *The Alexandrian*. https://thealexandrian.net/wordpress/4147/roleplaying-games/dont-prep-plots

Alexander, J. (2009, March 23). Don’t prep plots: Prepping scenario timelines. *The Alexandrian*. https://thealexandrian.net/wordpress/4154/roleplaying-games/dont-prep-plots-prepping-scenario-timelines

Alexander, J. (2010, May 27). Node-based scenario design – Part 1: The plotted approach. *The Alexandrian*. https://thealexandrian.net/wordpress/7949/roleplaying-games/node-based-scenario-design-part-1-the-plotted-approach

Alexander, J. (2010, May 28). Node-based scenario design – Part 2: Choose your own adventure. *The Alexandrian*. https://thealexandrian.net/wordpress/7961/roleplaying-games/node-based-scenario-design-part-2-choose-your-own-adventure

Alexander, J. (2010, May 31). Node-based scenario design – Part 3: Inverting the Three Clue Rule. *The Alexandrian*. https://thealexandrian.net/wordpress/7985/roleplaying-games/node-based-scenario-design-part-3-inverting-the-three-clue-rule

Alexander, J. (2010, June 4). Node-based scenario design – Part 5: Plot vs. node. *The Alexandrian*. https://thealexandrian.net/wordpress/8008/roleplaying-games/node-based-scenario-design-part-5-plot-vs-node

Alexander, J. (2010, June 14). Node-based scenario design – Part 9: Types of nodes. *The Alexandrian*. https://thealexandrian.net/wordpress/8049/roleplaying-games/node-based-scenario-design-part-9-types-of-nodes

Alexander, J. (2011, October 3). Advanced node-based design – Part 1: Moving between nodes. *The Alexandrian*. https://thealexandrian.net/wordpress/8171/roleplaying-games/advanced-node-based-design-part-1-moving-between-nodes

Alexander, J. (2011, October 17). Advanced node-based design – Part 5: The two prongs of mystery design. *The Alexandrian*. https://thealexandrian.net/wordpress/8202/roleplaying-games/advanced-node-based-design-part-5-the-two-prongs-of-mystery-design

Alexander, J. (2012, April 2). Game structures. *The Alexandrian*. https://thealexandrian.net/wordpress/15126/roleplaying-games/game-structures

Alexander, J. (2015, June 18). Don’t prep plots – Tools, not contingencies. *The Alexandrian*. https://thealexandrian.net/wordpress/37422/roleplaying-games/dont-prep-plots-tools-not-contingencies

Alexander, J. (2015, January 5). Don’t prep plots – “You will rue this day, heroes!” (The principles of RPG villainy). *The Alexandrian*. https://thealexandrian.net/wordpress/36383/roleplaying-games/dont-prep-plots-you-will-rue-this-day-heroes-the-principles-of-rpg-villainy

Alexander, J. (2018, October 29). Random GM tip – Using revelation lists. *The Alexandrian*. https://thealexandrian.net/wordpress/40978/roleplaying-games/random-gm-tip-using-revelation-lists

Alexander, J. (2018, May 26). Smart prep. *The Alexandrian*. https://thealexandrian.net/wordpress/39885/roleplaying-games/smart-prep

Alexander, J. (2020, October 14). The secret life of nodes – Part 2: Node-based campaigns. *The Alexandrian*. https://thealexandrian.net/wordpress/45268/roleplaying-games/the-secret-life-of-nodes-part-2-node-based-campaigns

Alexander, J. (2020, October 21). The secret life of nodes – Part 3: Fractal nodes. *The Alexandrian*. https://thealexandrian.net/wordpress/45272/roleplaying-games/the-secret-life-of-nodes-part-3-fractal-nodes

Alexander, J. (2020, October 28). The secret life of nodes – Part 4: Nodes aren’t everything. *The Alexandrian*. https://thealexandrian.net/wordpress/45278/roleplaying-games/the-secret-life-of-nodes-part-4-nodes-arent-everything

Alexander, J. (2020, November 4). The secret life of nodes – Part 5: Naturalistic node design. *The Alexandrian*. https://thealexandrian.net/wordpress/45283/roleplaying-games/the-secret-life-of-nodes-part-5-naturalistic-node-design

Alexander, J. (2020, October 9). The secret life of nodes. *The Alexandrian*. https://thealexandrian.net/wordpress/45263/roleplaying-games/the-secret-life-of-nodes

Alexander, J. (2026, February 22). Is node-based design prepping a plot? *The Alexandrian*. https://thealexandrian.net/wordpress/53341/roleplaying-games/is-node-based-design-prepping-a-plot

Alexander, R., & Martens, C. (2017). Deriving quests from open world mechanics. *Proceedings of the 12th International Conference on the Foundations of Digital Games*, Article 12, 1–7. https://doi.org/10.1145/3102071.3102098

Appel, M., Malecki, W. P., Messingschlager, T. V., & Winkler, J. R. (2025). I, ChatGPT: linguistic properties and human experiences of human- versus AI-generated stories. *Humanities and Social Sciences Communications, 12*, 1892. https://doi.org/10.1057/s41599-025-06341-2

Bai, Y., Lv, X., Zhang, J., Lyu, H., Tang, J., Huang, Z., Du, Z., Liu, X., Zeng, A., Hou, L., Dong, Y., Tang, J., & Li, J. (2024). LongBench: A bilingual, multitask benchmark for long context understanding. *Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)*, 3119–3137. https://doi.org/10.18653/v1/2024.acl-long.172

Bellaiche, L., Shahi, R., Turpin, M. H., Ragnhildstveit, A., Sprockett, S., Barr, N., Christensen, A., & Seli, P. (2023). Humans versus AI: whether and why we prefer human-created compared to AI-created artwork. *Cognitive Research: Principles and Implications, 8*, 42. https://doi.org/10.1186/s41235-023-00499-6

Brown, J. (2000, September 21). Volunteer revolt. *Salon*. https://www.salon.com/2000/09/21/ultima_volunteers/

Burgess, J., & Jones, C. M. (2023). Exploring how players use emergent narrative in strategy games. *Entertainment Computing, 44*, 100533. https://doi.org/10.1016/j.entcom.2022.100533

Buschman, T. J. (2021). Balancing flexibility and interference in working memory. *Annual Review of Vision Science, 7*, 367–388. https://doi.org/10.1146/annurev-vision-100419-104831

Cardona-Rivera, R. E., Robertson, J., Ware, S. G., Harrison, B., Roberts, D. L., & Young, R. M. (2014). Foreseeing meaningful choices. *Proceedings of the AAAI Conference on Artificial Intelligence and Interactive Digital Entertainment, 10*(1), 9–15. https://doi.org/10.1609/aiide.v10i1.12716

Carlini, N., Tramèr, F., Wallace, E., Jagielski, M., Herbert-Voss, A., Lee, K., Roberts, A., Brown, T., Song, D., Erlingsson, Ú., Oprea, A., & Raffel, C. (2021). Extracting training data from large language models. *Proceedings of the 30th USENIX Security Symposium*. https://www.usenix.org/conference/usenixsecurity21/presentation/carlini-extracting

Chambers, N., & Jurafsky, D. (2010). A database of narrative schemas. *Proceedings of the Seventh International Conference on Language Resources and Evaluation (LREC'10)*. https://aclanthology.org/L10-1029/

Chang, K. K., Cramer, M., Soni, S., & Bamman, D. (2023). Speak, memory: An archaeology of books known to ChatGPT/GPT-4. *Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing*, 7312–7327. https://doi.org/10.18653/v1/2023.emnlp-main.453

Charniak, E., & Goldman, R. P. (1993). A Bayesian model of plan recognition. *Artificial Intelligence, 64*(1), 53–79. https://doi.org/10.1016/0004-3702(93)90060-O

Chen, D. L., & Mooney, R. J. (2011). Learning to interpret natural language navigation instructions from observations. *Proceedings of the AAAI Conference on Artificial Intelligence, 25*(1), 859–865. https://doi.org/10.1609/aaai.v25i1.7974

Chen, S., Nelson, M. J., & Mateas, M. (2009). Evaluating the authorial leverage of drama management. *Proceedings of the AAAI Conference on Artificial Intelligence and Interactive Digital Entertainment, 5*(1), 136–141. https://doi.org/10.1609/aiide.v5i1.12377

Cooper, G. F. (1990). The computational complexity of probabilistic inference using Bayesian belief networks. *Artificial Intelligence, 42*(2–3), 393–405. https://doi.org/10.1016/0004-3702(90)90060-D

Cowan, N. (2001). The magical number 4 in short-term memory: A reconsideration of mental storage capacity. *Behavioral and Brain Sciences, 24*(1), 87–114. https://doi.org/10.1017/S0140525X01003922

Dagum, P., & Luby, M. (1993). Approximating probabilistic inference in Bayesian belief networks is NP-hard. *Artificial Intelligence, 60*(1), 141–153. https://doi.org/10.1016/0004-3702(93)90036-B

Das, B. (2004). Generating conditional probabilities for Bayesian networks: Easing the knowledge acquisition problem. *arXiv preprint cs/0411034*. https://arxiv.org/abs/cs/0411034

Day, T., & Zhu, J. (2017). Agency informing techniques: Communicating player agency in interactive narratives. *Proceedings of the International Conference on the Foundations of Digital Games (FDG '17)*, Article 56, 1–4. https://doi.org/10.1145/3102071.3106363

Evans, M. (2024). Too Afraid to Go Deeper: Creating Pervasive Dread Through Blended Design Structures in *Subnautica* and *Subnautica: Below Zero*. *Game Studies, 24*(4). https://gamestudies.org/2404/articles/evans

Failbetter Games. (2010, March 3). Echo Bazaar narrative structures, part two. https://www.failbettergames.com/news/echo-bazaar-narrative-structures-part-two

Failbetter Games. (2012, August 5). StoryNexus developer diary #2: Fewer spreadsheets, less swearing. https://www.failbettergames.com/news/storynexus-developer-diary-2-fewer-spreadsheets-less-swearing

Fendt, M. W., Harrison, B., Ware, S. G., Cardona-Rivera, R. E., & Roberts, D. L. (2012). Achieving the illusion of agency. In *Interactive Storytelling: 5th International Conference, ICIDS 2012* (Lecture Notes in Computer Science, Vol. 7648, pp. 114–125). Springer. https://doi.org/10.1007/978-3-642-34851-8_11

Fisher, M. (2022). Narrative planning in large domains through state abstraction and option discovery. *Proceedings of the AAAI Conference on Artificial Intelligence and Interactive Digital Entertainment, 18*(1), 299–302. https://doi.org/10.1609/aiide.v18i1.21979

Gao, L., Madaan, A., Zhou, S., Alon, U., Liu, P., Yang, Y., Callan, J., & Neubig, G. (2023). PAL: Program-aided language models. *Proceedings of the 40th International Conference on Machine Learning, 202*, 10764–10799. https://proceedings.mlr.press/v202/gao23f.html

Greenberg, D. L., & Verfaellie, M. (2010). Interdependence of episodic and semantic memory: Evidence from neuropsychology. *Journal of the International Neuropsychological Society, 16*(5), 748–753. https://doi.org/10.1017/S1355617710000676

Grey, J., & Bryson, J. J. (2011). Procedural quests: A focus for agent interaction in role-playing-games. In *Proceedings of the AISB 2011 Symposium: AI & Games* (pp. 3–10). https://researchportal.bath.ac.uk/en/publications/procedural-quests-a-focus-for-agent-interaction-in-role-playing-g/

Grinblat, J., Manning, C., & Kreminski, M. (2021). Emergent narrative and reparative play. In *Interactive Storytelling* (pp. 208–216). Springer. https://doi.org/10.1007/978-3-030-92300-6_19

Hammond, S., Pain, H., & Smith, T. J. (2007). Player Agency in Interactive Narrative: Audience, Actor & Author. In *Proceedings of AISB '07: Artificial and Ambient Intelligence* (pp. 386–393). https://ualresearchonline.arts.ac.uk/id/eprint/21210/

Harris, S., & Caldwell, N. (2024). A transfiguration paradigm for quest design. *Games and Culture, 19*(4), 493–512. https://doi.org/10.1177/15554120231170152

Hayton, T., Porteous, J., Ferreira, J., & Lindsay, A. (2020). Narrative planning model acquisition from text summaries and descriptions. *Proceedings of the AAAI Conference on Artificial Intelligence, 34*(02), 1709–1716. https://doi.org/10.1609/aaai.v34i02.5534

Hogan, D. P., & Brennen, A. (2024). Open-ended wargames with large language models. *arXiv preprint arXiv:2404.11446*. https://doi.org/10.48550/arXiv.2404.11446

Hsieh, C.-P., Sun, S., Kriman, S., Acharya, S., Rekesh, D., Jia, F., Zhang, Y., & Ginsburg, B. (2024). RULER: What's the real context size of your long-context language models? *arXiv preprint arXiv:2404.06654*. https://arxiv.org/abs/2404.06654

Hu, S., Huang, T., Liu, G., Kompella, R. R., Ilhan, F., Tekin, S. F., Xu, Y., Yahn, Z., & Liu, L. (2024). A survey on large language model-based game agents. *arXiv preprint arXiv:2404.02039*. https://doi.org/10.48550/arXiv.2404.02039

Iovino, M., Scukins, E., Styrud, J., Ögren, P., & Smith, C. (2022). A survey of behavior trees in robotics and AI. *Robotics and Autonomous Systems, 154*, 104096. https://doi.org/10.1016/j.robot.2022.104096

Jenkins, H. (2004). Game design as narrative architecture. *Electronic Book Review*. https://electronicbookreview.com/publications/game-design-as-narrative-architecture/

Johnson, M. K., Hashtroudi, S., & Lindsay, D. S. (1993). Source monitoring. *Psychological Bulletin, 114*(1), 3–28. https://doi.org/10.1037/0033-2909.114.1.3

Johnson-Bey, S., Nelson, M. J., & Mateas, M. (2022). Neighborly: A sandbox for simulation-based emergent narrative. *2022 IEEE Conference on Games (CoG)*, 425–432. https://doi.org/10.1109/CoG51982.2022.9893631

Jones, J. D. (2022). Authorial Burden. In C. Hargood, D. E. Millard, A. Mitchell, & U. Spierling (Eds.), *The Authoring Problem: Challenges in Supporting Authoring for Interactive Digital Narratives* (pp. 47–63). Springer International Publishing. https://doi.org/10.1007/978-3-031-05214-9_4

Jones, J. D., & Millard, D. E. (2024). Experiencing The Authorial Burden. In *Proceedings of the 35th ACM Conference on Hypertext and Social Media (HT '24)* (pp. 78–87). Association for Computing Machinery. https://doi.org/10.1145/3648188.3675134

Jones, J. D., & Millard, D. E. (2026). Beyond authorial burden. *ACM Transactions on the Web, 20*(3), Article 34, 1–23. https://doi.org/10.1145/3757746

Juul, J. (2002). The open and the closed: Games of emergence and games of progression. In F. Mäyrä (Ed.), *Computer Games and Digital Cultures Conference Proceedings* (pp. 323–329). Tampere University Press. https://doi.org/10.26503/dl.v2002i1.9

Kambhampati, S., Valmeekam, K., Guan, L., Verma, M., Stechly, K., Bhambri, S., Saldyt, L. P., & Murthy, A. B. (2024). Position: LLMs can’t plan, but can help planning in LLM-Modulo frameworks. *Proceedings of the 41st International Conference on Machine Learning, 235*, 22895–22907. https://proceedings.mlr.press/v235/kambhampati24a.html

Liu, N. F., Lin, K., Hewitt, J., Paranjape, A., Bevilacqua, M., Petroni, F., & Liang, P. (2024). Lost in the middle: How language models use long contexts. *Transactions of the Association for Computational Linguistics, 12*, 157–173. https://doi.org/10.1162/tacl_a_00638

Louchart, S., & Aylett, R. (2003). Solving the Narrative Paradox in VEs—Lessons from RPGs. In *Intelligent Virtual Agents 2003* (pp. 244–248). Springer. https://doi.org/10.1007/978-3-540-39396-2_41

Louchart, S., Swartjes, I., Kriegel, M., & Aylett, R. (2008). Purposeful authoring for emergent narrative. In *Interactive Storytelling: First Joint International Conference on Interactive Digital Storytelling (ICIDS 2008)* (Lecture Notes in Computer Science, Vol. 5334, pp. 273–284). Springer. https://doi.org/10.1007/978-3-540-89454-4_35

Marco, G., Gonzalo, J., & Fresno, V. (2025). The Reader is the Metric: How Textual Features and Reader Profiles Explain Conflicting Evaluations of AI Creative Writing. *Findings of the Association for Computational Linguistics: ACL 2025*, 25432–25449. https://doi.org/10.18653/v1/2025.findings-acl.1304

Marra, G., Dumančić, S., Manhaeve, R., & De Raedt, L. (2024). From statistical relational to neurosymbolic artificial intelligence: A survey. *Artificial Intelligence, 328*, 104062. https://doi.org/10.1016/j.artint.2023.104062

Mateas, M., & Stern, A. (2005). Structuring content in the Façade interactive drama architecture. *Proceedings of the AAAI Conference on Artificial Intelligence and Interactive Digital Entertainment, 1*(1), 93–98. https://doi.org/10.1609/aiide.v1i1.18722

Nelson, M. J., Ashmore, C., & Mateas, M. (2006). Authoring an interactive narrative with declarative optimization-based drama management. *Proceedings of the AAAI Conference on Artificial Intelligence and Interactive Digital Entertainment, 2*(1), 127–129. https://doi.org/10.1609/aiide.v2i1.18761

Oberauer, K., Farrell, S., Jarrold, C., & Lewandowsky, S. (2016). What limits working memory capacity? *Psychological Bulletin, 142*(7), 758–799. https://doi.org/10.1037/bul0000046

Packer, C., Wooders, S., Lin, K., Fang, V., Patil, S. G., Stoica, I., & Gonzalez, J. E. (2023). MemGPT: Towards LLMs as operating systems. *arXiv preprint arXiv:2310.08560*. https://arxiv.org/abs/2310.08560

Park, A. (2003, April 14). Asheron's Call. *GameSpot*. https://www.gamespot.com/articles/asherons-call/1100-2655688/

Park, J. S., O'Brien, J. C., Cai, C. J., Morris, M. R., Liang, P., & Bernstein, M. S. (2023). Generative agents: Interactive simulacra of human behavior. *Proceedings of the 36th Annual ACM Symposium on User Interface Software and Technology*, Article 2, 1–22. https://doi.org/10.1145/3586183.3606763

Porteous, J., Ferreira, J. F., Lindsay, A., & Cavazza, M. (2021). Automated narrative planning model extension. *Autonomous Agents and Multi-Agent Systems, 35*(2), Article 19. https://doi.org/10.1007/s10458-021-09501-1

PostgreSQL Global Development Group. (n.d.-a). Database page layout. *PostgreSQL Documentation*. https://www.postgresql.org/docs/current/storage-page-layout.html

PostgreSQL Global Development Group. (n.d.-b). TOAST. *PostgreSQL Documentation*. https://www.postgresql.org/docs/current/storage-toast.html

Raffloer, G., & Green, M. C. (2025). Of love & lasers: Perceptions of narratives by AI versus human authors. *Computers in Human Behavior: Artificial Humans, 5*, 100168. https://doi.org/10.1016/j.chbah.2025.100168

Reab v. Electronic Arts, Inc., 214 F.R.D. 623 (D. Colo. 2002). https://calculators.law/caselaw/decisions/5qJNjDQ68kap/reab-v-electronic-arts-inc

Riedl, M. O., & Bulitko, V. (2013). Interactive narrative: An intelligent systems approach. *AI Magazine, 34*(1), 67–77. https://doi.org/10.1609/aimag.v34i1.2449

Roth, C., Vermeulen, I., Vorderer, P., & Klimmt, C. (2012). Exploring replay value: Shifts and continuities in user experiences between first and second exposure to an interactive story. *Cyberpsychology, Behavior, and Social Networking, 15*(7), 378–381. https://doi.org/10.1089/cyber.2011.0437

Roth, C., & Vermeulen, I. (2013). Breaching interactive storytelling's implicit agreement: A content analysis of *Façade* user behaviors. In *Interactive Storytelling: 6th International Conference, ICIDS 2013* (Lecture Notes in Computer Science, Vol. 8230, pp. 168–173). Springer. https://doi.org/10.1007/978-3-319-02756-2_20

Rowe, J. P., & Lester, J. C. (2013). A modular reinforcement learning framework for interactive narrative planning. *Proceedings of the AAAI Conference on Artificial Intelligence and Interactive Digital Entertainment, 9*(4), 57–63. https://doi.org/10.1609/aiide.v9i4.12636

Ryan, J. (2018). *Curating simulated storyworlds* [Doctoral dissertation, University of California, Santa Cruz]. eScholarship. https://escholarship.org/uc/item/1340j5h2

Sanchez, V. (2018, August 31). Narrative design on open worlds: Should we ditch missions? *Game Developer*. https://www.gamedeveloper.com/design/narrative-design-on-open-worlds-should-we-ditch-missions-

Schacter, D. L. (2012). Constructive memory: Past and future. *Dialogues in Clinical Neuroscience, 14*(1), 7–18. https://doi.org/10.31887/DCNS.2012.14.1/dschacter

Schacter, D. L., & Addis, D. R. (2007). The cognitive neuroscience of constructive memory: Remembering the past and imagining the future. *Philosophical Transactions of the Royal Society B: Biological Sciences, 362*(1481), 773–786. https://doi.org/10.1098/rstb.2007.2087

Sears, S., & Weisberg, D. S. (2026). Bot or not: Can people tell the difference between stories written by a human or by an AI system? *Judgment and Decision Making, 21*, e21. https://doi.org/10.1017/jdm.2026.10042

Short, E. (2019, December 3). Storylets play together. *Emily Short's Interactive Storytelling*. https://emshort.blog/2019/12/03/storylets-play-together/

Short, E. (2019, November 29). Storylets: You want them. *Emily Short's Interactive Storytelling*. https://emshort.blog/2019/11/29/storylets-you-want-them/

Soler-Adillon, J. (2019). The open, the closed and the emergent: Theorizing emergence for videogame studies. *Game Studies, 19*(2). https://gamestudies.org/1902/articles/soleradillon

Sourati, Z., Karimi-Malekabadi, F., Ozcan, M., McDaniel, C., Ziabari, A., Trager, J., Tak, A. N., Chen, M., Morstatter, F., & Dehghani, M. (2026). The shrinking landscape of linguistic diversity in the age of large language models. *Nature Human Behaviour*. https://doi.org/10.1038/s41562-026-02550-0

SQLite. (n.d.). Database file format. *SQLite Documentation*. https://www.sqlite.org/fileformat.html

Stang, S. (2019). “This Action Will Have Consequences”: Interactivity and Player Agency. *Game Studies, 19*(1). https://gamestudies.org/1901/articles/stang

Stanko-Kaczmarek, M., Dera, L., & Koscielska, H. (2025). “Between the Lines”: Perceptions of Poetry With Authorship Attributed to Artificial Intelligence or Humans – A Comparative Analysis. *The Journal of Creative Behavior, 59*(3), e1513. https://doi.org/10.1002/jocb.1513

Sullivan, A. M. (2012). *The Grail framework: Making stories playable on three levels in CRPGs* [Doctoral dissertation, University of California, Santa Cruz]. eScholarship. https://escholarship.org/uc/item/004129jn

Szabó, G., Krizsai, F., & Deme, A. (2026). The invisible author: Citizen sociolinguistic perspectives on identifying human and AI-generated narrative texts. *Social Sciences & Humanities Open, 13*, 102646. https://doi.org/10.1016/j.ssaho.2026.102646

Thomson, B., & Young, S. (2010). Bayesian update of dialogue state: A POMDP framework for spoken dialogue systems. *Computer Speech & Language, 24*(4), 562–588. https://doi.org/10.1016/j.csl.2009.07.003

Thompson, R. (2009, July 27). Why MxO live content worked. *MMORPG.com*. https://www.mmorpg.com/editorials/why-mxo-live-content-worked-2000117124

Thue, D., Bulitko, V., Spetch, M., & Romanuik, T. (2011). A Computational Model of Perceived Agency in Video Games. *Proceedings of the AAAI Conference on Artificial Intelligence and Interactive Digital Entertainment, 7*(1), 91–96. https://doi.org/10.1609/aiide.v7i1.12437

Tian, Y., Huang, T., Liu, M., Jiang, D., Spangher, A., Chen, M., May, J., & Peng, N. (2024). Are Large Language Models Capable of Generating Human-Level Narratives? *Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing*, 17659–17681. https://doi.org/10.18653/v1/2024.emnlp-main.978

Tulving, E. (2002). Episodic memory: From mind to brain. *Annual Review of Psychology, 53*, 1–25. https://doi.org/10.1146/annurev.psych.53.100901.135114

Wang, D., Huang, D., Shen, H., & Uzzi, B. (2026). A large-scale comparison of divergent creativity in humans and large language models. *Nature Human Behaviour, 10*, 531–540. https://doi.org/10.1038/s41562-025-02331-1

Williams, S. (2009, August 4). Another perspective on live content. *MMORPG.com*. https://www.mmorpg.com/editorials/another-perspective-on-live-content-2000117156

Wu, D., Wang, H., Yu, W., Zhang, Y., Chang, K.-W., & Yu, D. (2025). LongMemEval: Benchmarking chat assistants on long-term interactive memory. *Proceedings of the International Conference on Learning Representations (ICLR 2025)*. https://proceedings.iclr.cc/paper_files/paper/2025/hash/d813d324dbf0598bbdc9c8e79740ed01-Abstract-Conference.html

Xu, K., Zhang, Y., Yang, B., & Verbrugge, C. (2026). Deconstructing open-world game mission design formula: A thematic analysis using an action-block framework. *Proceedings of the 2026 CHI Conference on Human Factors in Computing Systems*, Article 450, 1–31. https://doi.org/10.1145/3772318.3790625

Xu, W., Jojic, N., Rao, S., Brockett, C., & Dolan, B. (2025). Echoes in AI: Quantifying lack of plot diversity in LLM outputs. *Proceedings of the National Academy of Sciences, 122*(35), e2504966122. https://doi.org/10.1073/pnas.2504966122

Yu, H., & Riedl, M. (2013). Data-driven personalized drama management. *Proceedings of the AAAI Conference on Artificial Intelligence and Interactive Digital Entertainment, 9*(1), 191–197. https://doi.org/10.1609/aiide.v9i1.12665

Zaini, A., Fowler, A., Amor, R., & Wünsche, B. C. (2025). Character-driven storytelling design for digital games: A scoping review. *Games and Culture*. https://doi.org/10.1177/15554120251380423
