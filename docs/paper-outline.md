# Event-Driven Systems for Reactive Actor Branching Narrative in Interactive Media

## Paper Outline

> **Canonical working outline.** Once a section is settled, record it here and commit it before moving on. Sections still under discussion must be clearly marked as working rather than left only in chat history.

## 1. Abstract

### 1.1 Interactive narrative traditionally trades participant freedom against authorial control.
- Greater meaningful freedom creates more branches, dialogue states, contingencies, and consequences that must be anticipated and implemented.

### 1.2 Generative models expand reactive possibilities but create new authority problems.
- Characters can acquire knowledge they should not possess.
- World state can become inconsistent.
- Causality can drift.
- Authored narrative coherence can be lost.

### 1.3 The proposed architecture separates human authorship, authoritative state, reactive actors, and probabilistic assistance.
- Human authors define the narrative world, actors, knowledge, conflicts, motivations, relationships, intended events, and possible outcomes.
- An authoritative state, information, and event system maintains narrative reality and governs propagation of claims, observations, beliefs, and consequences.
- Reactive actors respond using only the information, beliefs, and state available to them.
- Probabilistic models may interpret input, assist decisions, retrieve context, and generate dialogue without independently defining narrative reality.

### 1.4 Core objective
- Preserve human authorship while making authored narrative responsive without requiring every possible response to be authored in advance.

---

## 2. Human Authorship as a Design Requirement

### 2.1 Human creative expression is individual rather than interchangeable.
- Writers bring different linguistic habits, experiences, perspectives, cultural backgrounds, associations, and creative instincts to a work.
- Human writing carries measurable individual and social signatures, and human creativity shows substantially greater variance at the high-creativity end.
- **Support:** Sourati et al. (2026); Wang et al. (2026).

### 2.2 Narrative depth is created through relationships across the complete work.
- Character, theme, subtext, symbolism, pacing, conflict, foreshadowing, emotional development, turning points, and resolution gain meaning through their relationship to one another.
- Human-authored stories show greater structural diversity, suspense, arousal, and variation in story arcs; expert-oriented evaluation also places more emphasis on thematic development and rhetorical variety than on surface fluency alone.
- **Support:** Tian et al. (2024); Marco et al. (2025).

### 2.3 Independent human authorship produces substantial creative breadth.
- Different authors do not merely produce different wording around the same underlying story.
- Human-written stories show substantially greater plot-level diversity and much less repetition of plot elements and combinations.
- **Support:** Xu et al. (2025).

### 2.4 Human authorship is therefore a design requirement of this architecture.
- The objective is to preserve **deep, meaningful stories with breadth and depth that challenge and push the edges of philosophy**, while preserving the creative perspectives, long-range intent, and diversity produced by individual humans.
- Human authorship supplies the larger creative purpose within which interactive events acquire meaning.

### 2.5 Meaningful participation requires meaningful response.
- Participant freedom matters only when the world can react to what the participant does.
- Agency is not merely the availability of inputs or choices; it is tied to meaningful action and perceivable consequence.
- Interactive-narrative research explicitly treats the maintenance of agency and narrative coherence as a central design problem.
- **Support:** Hammond, Pain & Smith (2007).

### 2.6 Interactive narrative places unusual demands on human authorship.
- Unlike conventional narrative, the audience can intervene in the work.
- Participants may ignore intended paths, alter event order, combine actions unexpectedly, or attempt things the author never anticipated.
- This unpredictability is a property of the medium, not a deficiency in human authorship.
- The tension between pre-authored narrative and user freedom has long been described as the **narrative paradox**.
- **Support:** Louchart & Aylett (2003).

### 2.7 Conventional interactive authoring mechanisms make broad responsiveness increasingly difficult to express.
- Branching creates additional authored content.
- Persistent choices produce increasing combinations of possible state.
- More interactions require more conditional logic, alternate descriptions, dialogue, consequences, and testing.
- Jones identifies **exponential branching**, **combinatorial explosion**, and finite implementation scope as major sources of authorial burden; Jones & Millard later grounded that model in interviews with practicing interactive-narrative authors.
- **Support:** Jones (2022); Jones & Millard (2024).

### 2.8 Conventional interactive authoring mechanisms therefore tend to produce a poor simulacrum of the intended experience.
- One compromise is **pseudo-freeform structure**: the player appears to have broad narrative freedom, but meaningful reactions exist only inside anticipated branches and state combinations.
- Branches may diverge temporarily and then reconverge, preserving the impression of consequence without supporting permanently divergent narrative states.
- The other compromise is **open-ended but weakly consequential structure**: the player may explore freely and engage with many optional stories, but those stories often remain compartmentalized from the principal narrative and broader gameplay unless explicitly entered.
- The first offers constrained consequential freedom.
- The second offers broader activity with limited narrative consequence.
- Both approximate a deeply reactive world without fully providing one.
- **Support:** Stang (2019); Evans (2024).

### 2.9 Research on agency shows that the appearance of freedom can be separated from actual freedom.
- Day & Zhu distinguish **theoretical agency** from **perceived agency**.
- Thue et al. (2011) provide empirical support for perceived agency increasing without expanding the underlying action space.
- Stang's analysis of *The Walking Dead* describes branching decisions that repeatedly reconverge.
- Conventional systems can successfully simulate a greater degree of narrative freedom than they actually implement.
- **Support:** Day & Zhu (2017); Thue et al. (2011); Stang (2019).

### 2.10 Those limitations constrain both sides of the creative relationship.
- Authors cannot reasonably anticipate and explicitly implement responses to everything a participant might attempt.
- Participants are consequently limited either to actions for which meaningful responses were implemented, or to broader activities whose effects remain largely outside the consequential narrative.
- The authorial-burden literature locates this problem in the growth of content, state management, and implementation work rather than in any shortage of human creative capacity.
- **Support:** Jones (2022); Jones & Millard (2024).

### 2.11 The architectural problem is therefore not how to diminish human authorship, but how to extend its reach.
- Better interactive authoring mechanisms should allow human-authored worlds, characters, motivations, conflicts, and narrative intentions to respond coherently across a much larger range of participant behavior.
- Greater participant freedom and deeper human authorship should reinforce one another rather than compete.
- **Closing thesis:** *The limitation is not human creativity, but the machinery through which human creativity is currently made interactive.*

---

## 3. Authoring as Worldbuilding, Adversarial Design, and Narrative Planning

### 3.1 Human authorship is expressed through worlds as well as sequences.
- Narrative meaning can be embedded in places, institutions, relationships, histories, conflicts, objects, information, and affordances—not only in a predetermined chain of scenes.
- A designed environment can carry narrative purpose before a specific traversal through it is known.
- Different participants can encounter the same authored material in different orders and combinations without stripping it of authorial intent.
- **Support:** Jenkins (2004), *Game Design as Narrative Architecture*.
- **Possible supporting reference:** Louchart et al. (2008), *Purposeful Authoring for Emergent Narrative*.

### 3.2 Interactive authorship should prepare situations rather than scripts for participant behavior.
- Participant action is inherently difficult to predict exhaustively.
- The author can instead establish the circumstances from which consequences follow: people, motives, resources, constraints, relationships, locations, and pressures.
- “Don’t prep plots, prep situations” is the clearest practitioner formulation of this distinction.
- This does **not** mean abandoning narrative planning. It means avoiding dependence on one predicted sequence of participant actions.
- **Support:** Alexander (2009), *Don’t Prep Plots*; Alexander (2015), *Tools, Not Contingencies*.
- **Supporting:** Alexander (2018), *Smart Prep*.

### 3.3 Intended future developments can still be authored without becoming fixed plots.
- Authors can establish likely future events, actor plans, timelines, goals, and dramatic destinations.
- Those expectations remain conditional on the world continuing to develop in the anticipated way.
- When participant action changes the situation, future developments are reconsidered from the new state rather than forcibly preserved.
- This maps well to Enclave’s notion of an **authored trajectory** rather than a fixed event sequence.
- **Support:** Alexander (2009), *Don’t Prep Plots: Prepping Scenario Timelines*.
- **Supporting:** Alexander (2026), *Is Node-Based Design Prepping a Plot?*

### 3.4 Information is one of the principal structures through which narrative possibility is organized.
- What participants know determines what they can understand, pursue, question, reveal, conceal, or interfere with.
- Important information should not depend on one brittle discovery path.
- Revelations can be separated from the particular clues or routes by which they become available.
- Node-based design increasingly becomes a design of **knowledge flow**, rather than simply a map of scenes.
- **Support:** Alexander (2008), *Three Clue Rule*; Alexander (2010), *Node-Based Scenario Design – Part 3: Inverting the Three Clue Rule*; Alexander (2018), *Using Revelation Lists*; Alexander (2020), *The Secret Life of Nodes*.
- **Jenkins connection:** environmental storytelling also treats narrative space as a distribution mechanism for information.

### 3.5 Narrative structure can arise from the diegetic organization of the world itself.
- People, places, organizations, events, and activities can become loci of interaction because of their actual relationships in the fictional world.
- Structure does not have to be imposed purely as an abstract scene graph.
- “Node” should not become the ontology of the world.
- **Support:** Alexander (2010), *Node-Based Scenario Design – Part 9: Types of Nodes*; Alexander (2020), *Naturalistic Node Design*.
- **Boundary reference:** Alexander (2020), *Nodes Aren’t Everything*.
- **Takeaway:** node structure and evolving world state are not the same thing.

### 3.6 Actors give authored situations motion.
- Actors should have goals, resources, relationships, knowledge, and plans rather than simply waiting for a participant to trigger a scripted branch.
- Opposition and conflict can arise from what actors want and are capable of doing.
- The world can act **toward** the participant through proactive actors and events rather than remaining passively discoverable.
- Adversarial design becomes constructing actors and institutions capable of meaningful response rather than predicting every way a participant can break the plot.
- **Support:** Alexander (2009), *Don’t Prep Plots*; Alexander (2011), *Advanced Node-Based Design – Part 1: Moving Between Nodes*; Alexander (2015), *You Will Rue This Day, Heroes!*.

### 3.7 Authored narrative material can be conditional rather than sequential.
- Storylets demonstrate that authored content can exist independently and become available when prerequisites are satisfied.
- Completed content can alter shared state, which changes what becomes possible next.
- This permits deliberate narrative arcs without encoding every route through them as a branch tree.
- **Support:** Short (2019), *Storylets: You Want Them*; Short (2019), *Storylets Play Together*.
- **Supporting practitioner references:** Failbetter Games, *StoryNexus Developer Diary #2*; *Echo Bazaar Narrative Structures, Part Two*.
- **Distinction:** Alexander’s nodes mainly organize loci of interaction and information; storylets organize conditionally available authored narrative material.

### 3.8 Emergent sequence is a form of participant authorship within a purposefully authored world.
- Human authors define the world, its meaningful structures, conflicts, actors, information, and possibilities.
- Participants meaningfully author part of the realized narrative by determining which authored forces they encounter, disrupt, combine, or redirect.
- The realized sequence can emerge through interaction among authored structures without implying that authorship has disappeared.
- **Support:** Louchart et al. (2008), *Purposeful Authoring for Emergent Narrative*.

### 3.9 Authorial leverage should be understood as increased narrative richness for a given amount of authoring work.
- The objective is not merely to reduce the number of explicit branches.
- Avoiding the full **branching tax** allows creative effort to be spent on richer characters, relationships, factions, consequential information, authored situations, thematic material, and alternative developments.
- Narrative possibility and richness can grow faster than the labour required to enumerate paths.
- **Support:** Chen, Nelson & Mateas (2009); Nelson, Ashmore & Mateas (2006); Mateas & Stern (2005); Rowe & Lester (2013).

### 3.10 Limitations of Historical Approaches

- Traditional computational narrative approaches rely on explicitly represented states, actions, predicates, transitions, behaviors, or authored content to determine what can occur within their systems.
- These approaches can generate outcomes and combinations that were never individually authored, but the operations available to them remain bounded by their underlying representations.
- Consequently, the deeper limitation is not simply the enumeration of narrative branches, but the requirement to establish machine-interpretable representations of possible actions, situations, relationships, and consequences.
- This limitation was not exclusively deterministic:
  - Bayesian plan recognition demonstrated probabilistic interpretation of actions and narrative circumstances as early as 1993.
  - Probabilistic dialogue systems and data-driven drama management demonstrated contextual inference and adaptive behavior within bounded domains.
  - Learned narrative schemas and automated planning-model acquisition demonstrated that formal representations could themselves be generated or extended rather than entirely hand-authored.
- Historical probabilistic approaches introduced substantial implementation burdens of their own:
  - **Computational complexity:** General Bayesian-network inference is NP-hard, and even approximation is computationally difficult for broad classes of problems. Practical implementations often required simplifying assumptions, restricted dependencies, or specialized inference algorithms.
  - **Model construction:** Probabilistic systems required representations of relevant variables, dependencies, and conditional probabilities. In conventional Bayesian networks, the number of parameters required by conditional probability tables can grow exponentially with the number of parent variables.
  - **Knowledge acquisition and calibration:** Obtaining reliable probability estimates required expert knowledge, sufficiently representative training data, or specialized learning procedures, introducing additional development and maintenance costs.
  - **Domain restrictions:** Managing these costs often required limiting the possible states, actions, relationships, and dependencies that a system could evaluate, constraining the generality of its interpretations.
- Probabilistic techniques could reduce the burden of explicitly authoring individual responses, but frequently replaced portions of that burden with probabilistic model construction, parameterization, inference optimization, and validation.
- These developments reduced the burden of explicit formalization without eliminating the dependence on domain representations, executable action models, or predefined mechanisms for evaluating consequences.
- The historical challenge was therefore not the absence of probabilistic inference, but the difficulty of applying sufficiently general, computationally practical, and reliable interpretation to situations that had not been individually anticipated or formally represented.
- Modern generative models materially change this relationship by allowing candidate interpretations and responses to be synthesized from broader learned knowledge and contextual information.
- This does not eliminate the need for formal representation of authoritative world state or deterministic evaluation of consequences. It changes which parts of the interpretive process must be explicitly authored.
- **Historical support:** Charniak & Goldman (1993); Mateas & Stern (2005); Chambers & Jurafsky (2010); Thomson & Young (2010); Chen & Mooney (2011); Yu & Riedl (2013); Hayton et al. (2020); Porteous et al. (2021).
- **Computational and implementation support:** Cooper (1990); Dagum & Luby (1993); Das (2004); Thomson & Young (2010).
- **Additional architectural support:** Nelson, Ashmore & Mateas (2006); Rowe & Lester (2013); Short (2019); Failbetter Games.
- **Research qualification:** The historical formalization and computational bottlenecks are documented. Their contribution to commercial adoption rates, and the degree to which modern generative models overcome them, remain application-dependent.

---

## 4. Player Agency and the Branching Narrative Problem

### 4.1 The branching problem is fundamentally a state-space problem, not merely a tree-of-scenes problem.
- Every consequential participant action can alter multiple dimensions of narrative state: relationships, knowledge, beliefs, resources, locations, faction conditions, event eligibility, and future opportunities.
- Two stories that arrive at the same nominal scene may represent materially different narrative states.
- As those dimensions accumulate, the number of meaningful combinations grows rapidly.
- **Support:** Jones (2022); Jones & Millard (2024); Fisher (2022).

### 4.2 Persistent consequence creates the branching tax.
- If earlier actions continue to matter, later narrative material must remain compatible with combinations of earlier state.
- Cost includes conditional logic, state tracking, alternate dialogue, actor behavior, testing, recovery paths, and content needed to keep divergent states meaningful.
- Reconvergence reduces that cost precisely because it collapses some persistent divergence.
- **Support:** Jones (2022); Jones & Millard (2024); Alexander (2010), *Node-Based Scenario Design – Part 2: Choose Your Own Adventure*.

### 4.3 Replacing explicit branches with planning or simulation does not remove the underlying representation problem.
- A planner can generate sequences that were not individually authored as paths.
- It still needs actions, predicates, objects, relationships, preconditions, and effects represented in a machine-readable domain.
- The combinatorial problem can be moved into a formal model without disappearing.
- **Support:** Porteous et al. (2021); Hayton et al. (2020); Fisher (2022).

### 4.4 Traditional computational architectures are useful foundations and stepping stones toward richer reactive systems.
- Finite-state machines, behavior trees, planners, drama managers, state-conditioned content, and related techniques provide valuable ways to structure, reuse, constrain, and compose behavior.
- Drama management and narrative planning improve authorial leverage by selecting, combining, or sequencing authored structures at runtime.
- These approaches provide deterministic structure, compositional machinery, and authorial control that remain useful.
- The opportunity is to augment them with probabilistic assessment.
- **Support:** Iovino et al. (2022); Riedl & Bulitko (2013); Nelson, Ashmore & Mateas (2006); Rowe & Lester (2013); Short (2019); Failbetter Games.

### 4.5 Interactive systems commonly manage complexity by collapsing causal possibility.
- Branches reconverge.
- Decisions produce temporary variations but return to common states.
- Side stories remain isolated from the principal narrative.
- NPC reactions are restricted to manageable predefined states.
- Unanticipated combinations simply have no meaningful response.
- **Support:** Stang (2019); Evans (2024).

### 4.6 Perceived agency can compensate for limited causal agency, but that simulation weakens across successive replays.
- Actual or theoretical agency and perceived agency are distinct.
- Adaptive presentation or reconverging structures can increase perceived agency without proportionally increasing causal freedom.
- Repeated outcomes, invariant states, and recurring reconvergence become more visible across replay.
- **Support:** Day & Zhu (2017); Thue et al. (2011); Stang (2019).

### 4.7 The deeper historical bottleneck was explicit formalization.
- Traditional software can execute substantial complexity once meaning has been translated into states, actions, rules, predicates, transitions, or behaviors.
- The difficult part is turning unforeseen human action or ambiguous social situations into those formal structures.
- A human gamemaster can interpret intent, determine relevance, consider actor knowledge and goals, judge plausible responses, and decide which rules apply without enumerating those interpretations in advance.
- **Support:** Fisher (2022); Porteous et al. (2021); Hayton et al. (2020); Iovino et al. (2022); Hogan & Brennen (2024).

### 4.8 Modern probabilistic models materially change what must be formalized in advance.
- Models can interpret open-ended situations, retrieve contextual information, reason over prose descriptions, propose actions, and synthesize plausible candidate events or developments that were not individually enumerated beforehand.
- This is not limited to language models.
- Probabilistic judgment can extend the reachable possibility space without requiring every interpretation, actor response, or candidate development to be hand-authored as a branch or symbolic rule.
- **Support:** Park et al. (2023); Hu et al. (2024/2026); Hogan & Brennen (2024).

### 4.9 Probabilistic flexibility does not by itself solve narrative authority.
- A model that can plausibly infer or synthesize what might happen can also invent events, actions, facts, or consequences that were never established.
- Believable behavior is not authoritative causal correctness.
- Explicit authority boundaries remain necessary.
- **Support:** Hogan & Brennen (2024); Park et al. (2023).

### 4.10 The new opportunity is not to replace deterministic systems, but to augment them and change what they do and how they do it.
- Deterministic systems remain suited to authoritative state, constraints, permissions, event preconditions, persistence, and validated causal effects.
- Probabilistic systems can handle interpretation, contextual relevance, actor reasoning, plausible intentions, semantic ambiguity, and proposal of responses.
- Deterministic architectures can shift from enumerating the entire meaningful response space toward validating, constraining, composing, and persisting proposed outcomes.
- **Support:** Marra et al. (2024); Gao et al. (2023); Kambhampati et al. (2024).

### 4.11 The branching problem can therefore be reframed around the computational constraints that branching makes necessary.
- Meaningful divergence creates rapidly increasing combinations of narrative state, authored content, and possible response.
- Conventional computation historically required much of that meaning to be represented explicitly.
- Prior narrative architectures remain valuable for reuse, recombination, management, and control.
- Modern probabilistic inference changes which parts of interpretation, reaction, and event synthesis must be enumerated beforehand.
- The goal is not to eliminate meaningful divergence, but to reduce the amount of explicit computational structure each possible divergence requires.
- What remains is to combine that flexibility with authoritative state, causality, and persistent narrative coherence.
- **Support:** Marra et al. (2024); Gao et al. (2023); Kambhampati et al. (2024).


### 4.12 A Fundamentally Combinatorial Problem Space

- Player agency itself is not the problem; the difficulty comes from attempting to provide **meaningful consequential agency** computationally.
- Consequential actions can affect world state, relationships, information and beliefs, resources, actor behaviour, future events, and future opportunities.
- Persistent consequences create new circumstances that later interactions must account for.
- The resulting problem is fundamentally a **state-space and representation problem**, not merely a visible tree of narrative branches.
- **Support:** Jones (2022); Jones & Millard (2024); Fisher (2022); Porteous et al. (2021); Hayton et al. (2020).

### 4.13 Existing Designs Reduce the Problem by Imposing Limits

- Existing systems make the problem tractable by limiting the causal space they must support.
- Common approaches include:
  - explicitly branching narratives;
  - pseudo-agency through reconvergence;
  - broader genuine agency whose effects remain narratively shallow;
  - combinations of these approaches.
- These are rational engineering responses to the combinatorial problem.
- The difficult part is not simply an unexpected action, but the **persistence of its unaccounted consequences and the reactions those consequences should subsequently produce**.
- **Support:** Stang (2019); Day & Zhu (2017); Thue et al. (2011); Evans (2024); Short (2019); Failbetter Games; Alexander (2010), *Node-Based Scenario Design – Part 2: Choose Your Own Adventure*.

### 4.14 Scale Exacerbates the Issue

- Larger game spaces create more actors, locations, objects, institutions, relationships, and possible consequences.
- The limitation is **not simply the amount of state that can be stored**.
- Computational systems can maintain enormous persistent worlds.
- The historical bottleneck is meaningful **interaction with that state**.
- Conventional software generally needs actions and responses represented in computationally usable forms: rules, predicates, state transitions, planner actions, behaviour trees, commands, dialogue conditions, or explicit mechanics.
- A world can therefore contain enormous persistent state while exposing a comparatively narrow vocabulary of meaningful state-changing operations.
- **Support:** Fisher (2022); Porteous et al. (2021); Hayton et al. (2020); Iovino et al. (2022); Riedl & Bulitko (2013); Hogan & Brennen (2024).

### 4.15 The Analog Solution

- Tabletop and in-person gaming have addressed this problem for decades through the **Gamemaster**.
- A GM does not need every participant action to have been anticipated beforehand.
- Instead, the GM interprets attempted action in relation to:
  - the present situation;
  - established world facts;
  - previous events;
  - rules and constraints;
  - actor knowledge;
  - motivations;
  - ongoing plans;
  - plausible consequences.
- The GM reasons **from the existing world outward**, rather than selecting only from a predetermined catalogue of valid interactions.
- Gamemastering and authorship frequently overlap but are not equivalent roles.
- **Support:** Alexander (2009), *Don’t Prep Plots*; Alexander (2015), *Tools, Not Contingencies*; Alexander (2009), scenario timelines; Alexander (2012), *Game Structures*; Alexander (2020), *The Secret Life of Nodes*; Hogan & Brennen (2024).

### 4.16 The Prohibitive Costs of Persistent Human Labour

- Human Gamemasters provide the interpretive flexibility required for broad agency.
- They do not scale like computational worlds.
- Human availability is constrained by working hours, attention, concurrency, memory, and server/geographic coverage.
- Persistent online worlds have repeatedly supplemented automated machinery with human intervention.
- Those experiments demonstrate both the **value** of human situational oversight and its **economic scaling problem**.
- Tabletop-like responsiveness for large persistent populations effectively makes flexibility an ongoing labour service.
- **Support:** Brown (2000); *Reab v. Electronic Arts* (2002); Thompson (2009); Williams (2009); Park (2003).

### 4.17 Machine Intelligence as Actors and Situational Overseers

- Modern probabilistic systems can perform many operations that previously required human interpretation.
- They can:
  - interpret open-ended actions;
  - infer participant intent;
  - identify contextual relevance;
  - reason over natural-language descriptions;
  - retrieve relevant history;
  - infer actor motivations;
  - propose behaviour;
  - adapt to novel combinations of circumstances;
  - generate natural dialogue and responses.
- They can operate both as **actors within the world** and as **situational interpreters or overseers**.
- Unlike human GMs, they can potentially perform these operations concurrently and continuously at computational scale.
- This removes much of the historical labour constraint on broad interpretation.
- **Support:** Park et al. (2023); Hu et al. (2024/2026); Hogan & Brennen (2024); Tian et al. (2024) as secondary support for local generative competence.

## 5. The Agency–Persistence Gap

### 5.1 The Agency
- Machine intelligence removes much of the historical interaction constraint.
- LLMs can interpret actions that were never explicitly represented beforehand.
- They can reason over circumstances, intent, motivation, and context without requiring every interpretation to exist as a predefined computational rule.
- This approaches the interpretive capability historically supplied by human Gamemasters.
- **Support:** Hogan & Brennen (2024); Park et al. (2023); Hu et al. (2024/2026); Porteous et al. (2021); Hayton et al. (2020).

### 5.2 Expanded Agency
- Participants no longer necessarily need to express consequential actions through a predefined interaction vocabulary.
- The system can potentially interpret what they are trying to accomplish and relate it to existing circumstances.
- Actors can likewise react to combinations of circumstances that were never specifically scripted.
- The practical causal possibility space can therefore extend beyond what developers enumerated beforehand.
- **Support:** Hogan & Brennen (2024); Park et al. (2023); Alexander (2009/2015).

### 5.3 The Persistence
- **Extensive agency produces extensive persistent consequences and extensive persistence requirements.**
- For interactions to be meaningful, their outcomes must persist beyond the duration of the model call.
- Novel actions may change state, knowledge, beliefs, relationships, possessions, plans, institutions, future event eligibility, and later actor reactions.
- Each consequential interaction therefore creates information that future interactions may depend upon.
- Increasing agency means increasing quantities of potentially relevant historical state.
- **Support:** Park et al. (2023); Wu et al. (2025), *LongMemEval*; Jones (2022); Jones & Millard (2024); Fisher (2022).

### 5.4 LLMs Are Poorly Suited to Maintaining State
- LLMs are effective interpreters of state but unreliable custodians of it.
- Their active context is finite.
- Long-running worlds can produce far more relevant history than can remain active simultaneously.
- **Keeping a fact inside context does not guarantee that the model will reliably use it.**
- Models may overlook relevant information, apply it inconsistently, conflate entities, lose temporal or causal relationships, contradict previously established information, or reconstruct details inaccurately.
- Larger context windows improve capacity but do not transform probabilistic inference into reliable persistent state maintenance.
- **Support:** Liu et al. (2024), *Lost in the Middle*; Bai et al. (2024), *LongBench*; Hsieh et al. (2024), *RULER*; Wu et al. (2025), *LongMemEval*; Hogan & Brennen (2024).

### 5.5 Naive Applications Create Linear Storage Problems
- If every consequential interaction generates retained information and that information is not discarded, historical storage grows at least proportionally with consequential interaction count: **O(N) retained history** in the naive case.
- Long-running actors accumulate observations, relationships, beliefs, decisions, event histories, provenance, and state transitions.
- Actor-specific references, indexes, derived state, and propagation metadata can add further overhead.
- Merely storing everything does not solve persistence.
- Growing state must still be indexed, retrieved, scoped, deduplicated, temporally interpreted, associated with correct entities, and distinguished from superseded or contradictory information.
- External memory solves **capacity** more readily than **relevance**.
- Database implementation details illustrate additional physical overhead beyond semantic payload: tuple/record headers, page metadata, row pointers, indexes, overflow structures, and other bookkeeping.
- **Support:** Wu et al. (2025), *LongMemEval*; Park et al. (2023); Packer et al. (2023), *MemGPT*; PostgreSQL storage-page and TOAST documentation; SQLite database file-format documentation.
- **Claim boundary:** the O(N) growth follows architecturally from retaining records; database sources support physical overhead, not the asymptotic claim itself.

### 5.6 The Gap
- **This is the Agency–Persistence Gap.**
- Broad agency requires flexible interpretation of unforeseen actions and circumstances.
- Meaningful agency requires the consequences of those actions to persist.
- Increased interpretive freedom creates increasing quantities of persistent state.
- The systems now capable of supplying that interpretive flexibility are poorly suited to reliably maintaining the resulting world state.
- A system that improvises but cannot reliably preserve the consequences of that improvisation cannot maintain a coherent persistent world.
- A system that preserves everything exactly but can only act on predefined interactions cannot provide broad meaningful agency.
- **Support:** Enclave synthesis drawing on Hogan & Brennen (2024); Park et al. (2023); Liu et al. (2024); Bai et al. (2024); Hsieh et al. (2024); Wu et al. (2025); Fisher (2022); Porteous et al. (2021).
- **Terminology:** *Agency–Persistence Gap* is introduced by this paper.

### 5.7 Fertile Ground
- **This leaves us with two unusually complementary systems.**

**Conventional computational systems — strengths**
- durable persistence;
- exact representation;
- identity;
- provenance;
- large-scale storage;
- indexing and retrieval;
- reproducibility;
- explicit constraints;
- deterministic execution;
- consistent rule application.

**Conventional computational systems — weaknesses**
- poor improvisation;
- weak semantic interpretation without explicit machinery;
- poor handling of ambiguity;
- difficulty interpreting novel human action;
- adaptation generally requires formal representation;
- meaningful operations largely have to be specified beforehand.

**Probabilistic / interpretive systems, including humans and modern machine intelligence — strengths**
- improvisation;
- contextual reasoning;
- adaptation;
- semantic interpretation;
- ambiguity handling;
- generalization;
- intent recognition;
- analogical reasoning;
- response to novel circumstances.

**Probabilistic / interpretive systems — weaknesses**
- limited active information capacity;
- imperfect exact recall;
- susceptibility to interference;
- inconsistent application of remembered information;
- weaker provenance/source tracking;
- weaker exact identity management;
- reconstruction rather than exact replay;
- poor large-scale persistent state maintenance without external machinery.

- Humans exhibit this tradeoff in working-memory limits and reconstructive memory.
- LLMs exhibit it through finite/effectively limited context, retrieval failures, and inconsistent application of supplied state.
- **The strengths of each system align unusually closely with the weaknesses of the other.**
- **Support:** Cowan (2001); Oberauer et al. (2016); Schacter & Addis (2007); Schacter (2012); Johnson, Hashtroudi & Lindsay (1993); Buschman (2021); Liu et al. (2024); Hsieh et al. (2024); Wu et al. (2025); Gao et al. (2023), *PAL*; Kambhampati et al. (2024), *LLM-Modulo*; Marra et al. (2024).

### 5.8 Enclave as an Architectural Response

- Enclave treats the Agency–Persistence Gap as an **architectural boundary**, not as something that can simply be eliminated with a larger model or larger context window.
- It combines:
  - persistent computational state;
  - broad probabilistic interpretation;
  - reactive actors;
  - human-authored narrative structure;
  - persistent information and belief;
  - deterministic authority and validation.
- Probabilistic systems perform the work they are strong at:
  - interpretation;
  - contextual judgment;
  - actor reasoning;
  - ambiguity resolution;
  - proposal generation.
- Conventional computational systems perform the work they are strong at:
  - authoritative state;
  - persistence;
  - identity;
  - provenance;
  - constraints;
  - validation;
  - durable consequences.
- The result is not intended to replace deterministic computation with LLMs or replace authors with models.
- It is intended to allow each component to operate where its strengths are most useful.
- **Support:** Gao et al. (2023), *PAL*; Kambhampati et al. (2024), *LLM-Modulo*; Marra et al. (2024); Hogan & Brennen (2024); Park et al. (2023).

- **Transition:** If interpretation, persistent state, human authorship, and actor behaviour are distinct responsibilities, who or what is authoritative over each?

→ **§6. Sandbox Games and the Existing Sandbox Capability**

---

## 6. Sandbox Games and the Existing Sandbox Capability

### 6.1 Sandboxing the World Is Already Highly Developed

- Modern games can support very large spaces of participant action without individually authoring every resulting world configuration.
- Developers define systems, objects, rules, constraints, and affordances; players combine those elements during play.
- Runtime interaction can therefore generate valid world states and events that were never individually enumerated beforehand.
- This is the core achievement of systemic sandboxing: broad variation emerges from a finite authored substrate.
- **Support:** Juul (2002), *The Open and the Closed*; Soler-Adillon (2019), *The Open, the Closed and the Emergent*.

### 6.2 Sandbox Systems Already Accommodate Genuine Emergence

- Supported systems can interact in combinations nobody explicitly scripted.
- A resulting event does not need to have existed as a specific authored branch to be valid if it follows from the underlying systems.
- Simulation-heavy games can produce character histories, conflicts, losses, alliances, strategic reversals, and other events from systemic interaction.
- Players routinely interpret these events as meaningful stories.
- Existing research therefore demonstrates both **systemic emergence** and **emergent narrative**.
- **Support:** Juul (2002); Ryan (2018), *Curating Simulated Storyworlds*; Adams (2021), *Characterization and Emergent Narrative in Dwarf Fortress*; Burgess & Jones (2023), *Exploring how players use emergent narrative in strategy games*; Johnson-Bey, Nelson & Mateas (2022), *Neighborly*.

### 6.3 Existing Sandboxes Still Operate Through a Bounded Interaction Vocabulary

- Sandbox capability is not literal unlimited freedom.
- The world can only directly resolve properties, actions, and interactions represented by its computational systems.
- A finite ruleset may produce enormous variation while still defining the vocabulary through which that variation occurs.
- Increasing physical, object, AI, social, or interaction fidelity expands that vocabulary without eliminating the underlying representational boundary.
- This is why a player may freely combine supported mechanics while still being unable to perform or communicate an otherwise plausible action the software has no representation for.
- **Support:** Juul (2002); Soler-Adillon (2019); Fisher (2022); Porteous et al. (2021); Hayton et al. (2020); Iovino et al. (2022).

### 6.4 State Persistence Is Not the Central Sandbox Limitation

- Sandbox worlds can already preserve large quantities of changing state.
- Objects move, inventories change, resources are consumed, characters die, territories change hands, structures are created or destroyed, and these consequences can remain part of the world.
- Persistent online worlds further demonstrate that computational state can outlive the interaction or session that created it.
- The more important limitation is what the rest of the system is capable of **doing with that state**.
- A state change can be perfectly preserved while remaining narratively meaningless if characters, institutions, events, and authored material have no mechanism for interpreting or reacting to it.
- **Support:** Juul (2002), especially *EverQuest* as a persistent emergent world; existing §5 persistent-world research on *Ultima Online*, *Asheron's Call*, and *The Matrix Online*.

### 6.5 Narrative Is Usually Less Sandboxed Than the World

- A game may provide extraordinary systemic freedom while its authored narrative remains comparatively rigid.
- Modern open-world games commonly combine mechanically rich exploration with a comparatively linear central plot and optional side material.
- This does **not** mean sandbox systems fail to produce narrative.
- Simulation-heavy and strategy games demonstrably produce rich **emergent narratives** from play, and players can become strongly attached to characters and events that arose systemically.
- The distinction is between:
  - **systemic emergence** — the world produces unenumerated events;
  - **emergent/player-constructed narrative** — players interpret those events as stories;
  - **reactive authored narrative** — existing authored characters, conflicts, information, themes, and planned developments absorb those events and continue responding coherently.
- Existing sandbox systems are very strong at the first and can be very strong at the second.
- The third remains much harder because narrative consequence requires state to acquire social, informational, causal, and contextual meaning.
- A destroyed bridge is comparatively easy to persist.
- It is much harder to represent that:
  - one faction blames another for destroying it;
  - an NPC knows the player was responsible;
  - another actor believes a false account;
  - a planned event is no longer possible;
  - supply routes or political plans change;
  - later authored material should acquire a different meaning because of what happened.
- This is not a failure of sandbox design. It reflects that **systemic world consequence and persistent authored narrative consequence are different problems**.
- **Support:** Juul (2002); Evans (2024); Ryan (2018); Adams (2021); Burgess & Jones (2023); Grinblat, Manning & Kreminski (2021), *Emergent Narrative and Reparative Play*; Jenkins (2004).

### 6.6 The Missing Capability Is a Reactive Authored Narrative Sandbox

- Existing research already uses **narrative sandbox** for systems that rely heavily on emergence to produce narrative effects.
- Enclave's narrower concern is therefore not to claim invention of narrative sandboxing itself.
- The missing capability identified here is the ability for **deeply authored narrative structures to absorb emergent world events as persistent, meaningful inputs** without requiring every resulting reaction to be explicitly authored beforehand.
- The systemic sandbox provides the conceptual model:
  - developers author rules and structures rather than every resulting world state;
  - runtime interaction determines which valid configurations actually occur.
- The corresponding narrative question is whether authors can define:
  - facts;
  - actors;
  - motivations;
  - information;
  - relationships;
  - conflicts;
  - events;
  - constraints;
  - intended developments;
  - thematic structures;
  such that those authored elements remain meaningful when participants create circumstances the author never individually enumerated.
- This is not unrestricted procedural storytelling.
- It is a system in which human-authored narrative material can become possible, impossible, redirected, reinterpreted, or transformed as persistent consequences accumulate.
- Existing work already provides partial precedents:
  - purposeful authoring for emergent narrative;
  - narrative architecture;
  - state-conditioned storylets;
  - drama management and authorial leverage;
  - social-simulation sandboxes for emergent narrative.
- Enclave proposes to combine those ideas with the Agency–Persistence solution developed in §5.
- **Support:** Louchart et al. (2008); Jenkins (2004); Short (2019); Failbetter Games; Chen, Nelson & Mateas (2009); Johnson-Bey, Nelson & Mateas (2022); Grinblat, Manning & Kreminski (2021).

- **Transition:** Sandbox systems already demonstrate that authors can construct a bounded substrate capable of generating outcomes they did not individually enumerate. The remaining question is what architecture allows authored **narrative meaning** to behave the same way while preserving state, authority, information, and intent.

→ **§7. The Enclave System: Overview**

---

## 7. The Enclave System: Overview

### 7.1 Sandboxing the Narrative

- Section 6 established that sandbox systems can generate enormous spaces of valid world state and emergent events without requiring developers to enumerate every resulting configuration.
- Historically, granting participants comparable freedom within **deeply authored narrative** has faced distinct limitations and has not achieved the same flexibility.
- Games such as *Dwarf Fortress*, *The Sims*, *Neighborly*, and other narrative or simulation sandboxes demonstrate that complex and meaningful stories can emerge from systemic interaction.
- These systems are important precedents, but they are primarily **emergent narratives**: much of the story is discovered or constructed from what the simulation produces. Deeply authored narrative material generally does not possess the same freedom to absorb arbitrary participant actions and continue developing coherently.
- **Direct support:** Ryan (2018), *Curating Simulated Storyworlds*; Adams (2021), *Characterization and Emergent Narrative in Dwarf Fortress*; Johnson-Bey, Nelson & Mateas (2022), *Neighborly*; Grinblat, Manning & Kreminski (2021); Burgess & Jones (2023).
- **Enclave is intended to bring genuine sandbox flexibility to deep, deliberately authored narrative.**
- Instead of constructing sequenced end-to-end narratives that necessarily prescribe participant actions in one form or another, authors construct **narrative worlds**.
- They write those narratives as though the participants are inhabitants of the world rather than the center around which every event must be arranged.
- Authors provide an extensive narrative substrate containing:
  - characters;
  - factions and institutions;
  - relationships;
  - motivations and goals;
  - conflicts;
  - world facts;
  - information and secrets;
  - locations;
  - resources;
  - constraints;
  - intended developments;
  - possible events;
  - narrative goals and themes.
- Enclave then provides the architecture that allows those authored elements to remain active as the world changes:
  - persistent computational systems preserve what exists, what has happened, and what information is present;
  - actors participate from their own knowledge, relationships, motivations, and circumstances;
  - authored developments respond to changing conditions rather than occupying fixed positions in a sequence;
  - probabilistic systems interpret novel situations and participant actions that could not reasonably be enumerated beforehand;
  - consequential outcomes become part of the persistent world and can influence later actors and authored developments.
- **Closing point:** Enclave shifts interactive narrative from **authoring paths for participants to traverse** toward **authoring a persistent narrative world capable of interpreting, preserving, and responding to what participants actually do within it**.

### 7.2 Three Primitive Families

- Enclave represents the running narrative world independently of any current model invocation or Actor interpretation.
- Enclave organizes its foundational primitive ontology into three families: **Knowledge**, **Nexuses**, and **Classification**.
- The **Knowledge** family contains **Facts**, **Memories**, and **Events**.
- The **Nexuses** family contains **Loci**, **Actors**, and **Participants**.
- The **Classification** family contains **Domains**.
- Facts within the Knowledge family can represent both:
  - **canonical information** — information accepted by the authoritative system as describing what exists or has occurred;
  - **non-canonical information** — claims, observations, reports, communications, rumours, records, beliefs, misinformation, and other information that exists within the narrative world without necessarily being true.
- Qualification as information is therefore distinct from authority.
- A false report can exist persistently within the world without becoming true merely because it is represented by the system.
- Likewise, a canonical Fact can describe authoritative world state without its availability through a Locus implying recognition or acceptance of that truth; Cognitive Actors may still believe, doubt, reject, or misunderstand it.
- Knowledge persists independently of whether any Actor expresses or acts upon it.
- Individual Loci, Actors, and Participants may therefore retain, expose, receive, or transmit only subsets of the Knowledge represented by the system.
- This separation allows the world to retain a single authoritative state while simultaneously supporting incomplete, conflicting, distorted, outdated, or false information within it.
- Persistent Knowledge survives individual interactions and model calls, providing continuity across the narrative.
- Probabilistic systems therefore are not relied upon to maintain state.
- This directly addresses the Agency–Persistence gap established in §5.

### 7.3 Human Authors Define the Knowledge Base

- Human authors define the initial contents and structure of the persistent narrative world to create the initial **Knowledge Base**:
  - people;
  - institutions;
  - relationships;
  - facts;
  - secrets;
  - conflicts;
  - motivations;
  - information;
  - resources;
  - places;
  - intended developments;
  - possible events;
  - constraints;
  - themes.
- These authored elements form the initial Knowledge base from which the running narrative develops.
- Authors can establish what they expect or intend to happen without prescribing the sequence through which it must happen.
- Authorship therefore defines the *narrative possibility space* by establishing the world, its information, its pressures, and the conditions under which future developments may occur.
- The realized narrative may subsequently diverge from the author’s anticipated trajectory and modify the **Knowledge Base** through **Memories** and **Events.**
- This treats authored Knowledge as a persistent substrate rather than as a predetermined sequence of narrative states.
- Support: §§2–4

### 7.4 Nexus Interactions Create Cause and Effect

- Narrative state merely describes the current world, but for the system to work actions must have consequences.
- Actions alter circumstances and introduce new information.
- New information alters the Knowledge available through Loci and may change the circumstances under which Actors act.
- Those changes can themselves become causes of subsequent changes.
- Effects can therefore propagate beyond the interaction in which they originated.
- **Loci**, **Actors**, and **Participants** are the vehicles of these actions and changes.
- Physical and informational consequences operate alongside one another:
  - a bridge is destroyed; travel becomes impossible;
  - a shipment fails to arrive; an actor observes the destruction;
  - another hears an incorrect account; a faction changes its plans;
  - an intended meeting cannot occur; later narrative circumstances diverge accordingly.
- Authored conditions and Actor/Participant actions are evaluated against this changing world rather than against a fixed narrative sequence.
- This creates new behaviours and circumstances through exposure to new information via Loci.
- Participant actions become consequential not because the author wrote a branch for them, but because **the effects of those actions alter the circumstances from which subsequent narrative is produced**.
- Enclave treats narrative progression as a continuing chain of cause and effect through persistent world state, rather than as movement through a predetermined sequence of authored events.

### 7.5 Knowledge Control and Classification

- A persistent Knowledge Base of meaningful scale cannot be treated as an undifferentiated collection of information.

- Enclave therefore organizes Knowledge through **Domains**: broad semantic classifications representing major areas of knowledge within the world.

- Domains may describe areas such as:

  - Medicine;
  - Engineering;
  - Navigation;
  - Law;
  - History;
  - Politics;
  - Military doctrine;
  - Geography;
  - Chemistry;
  - other classic or authored areas of knowledge relevant to the narrative world.

- Domain classification describes **what a piece of Knowledge concerns**, not whether that Knowledge is true, authoritative, believed, or currently available to any particular Actor.

- A single item of Knowledge may therefore belong to more than one Domain when it concerns multiple areas of the world.

- For example, Knowledge concerning the collapse of a bridge may simultaneously concern Engineering, Transportation, Local Geography, and potentially Politics or Military activity depending on the circumstances surrounding the Event.

- Human authors assign Domains to the initial Knowledge Base as part of constructing the narrative world.

- Knowledge introduced later through **Memories** and **Events** is likewise classified into appropriate Domains as the Knowledge Base changes.

- Further granularity is provided by **Enclaves** and **Rank.**

- **Domains**, **Facets**, and **Enclaves** form the **Classification** family and provide a persistent organizational structure across both authored and emergent Knowledge.

- This allows later systems to reason over relevant portions of the Knowledge Base without requiring every Actor, Locus, or probabilistic process to operate against the complete body of available information.

### 7.6 Narrative as Emergent State

- As a result, narrative is not represented as a sequence of scenes, branches, or states through which the system advances.

- The realized narrative is instead the continuously evolving state produced by interaction between:

  - the human-authored **Knowledge Base**;
  - authored intentions, conflicts, pressures, and possible developments;
  - Actor and Participant actions;
  - Events and Memories produced through those interactions;
  - persistent cause and effect;
  - the distribution and availability of Knowledge through Loci;
  - the organization and relevance of that Knowledge through Domains, Enclaves, and Rank.

- Human authors therefore establish a narrative *possibility space* rather than enumerating the narrative branches that may occur within it.

- Intended developments can remain present as authored pressures, plans, conditions, and possibilities without being guaranteed outcomes.

- Actor and Participant actions change the Knowledge Base and world circumstances from which those intended developments are subsequently evaluated.

- The narrative at any given moment is therefore both:

  - the history of what has already occurred; and
  - the present set of circumstances from which future developments can emerge.

- Divergence does not require the system to select a different pre-authored branch. It occurs naturally when persistent consequences alter the conditions under which subsequent actions, Events, and authored possibilities are evaluated.

- Human authorship remains embedded throughout this process because the world, its Knowledge, its Actors, its conflicts, and its meaningful possibilities provide the authorial structure from which Participants co-author the realized narrative through their actions and consequences.

- The resulting narrative is therefore neither a fixed plot nor unconstrained procedural generation. It is an **emergent trajectory through a persistently authored narrative world**.

### 7.7 Why It Can Work

- Existing approaches demonstrate that the individual capabilities required by Enclave are already viable, but each addresses only part of the larger problem.

- Modern sandbox systems are highly effective at:

  - maintaining large persistent worlds;
  - resolving interactions through deterministic rules;
  - preserving systemic cause and effect;
  - producing emergent outcomes from combinations of represented mechanics.

- Their limitation is not persistence or emergence, but **interpretive breadth**. Actions and consequences remain bounded by mechanics, states, and interactions that the system has been designed to recognize.

- Conventional authored narrative systems solve a different problem well:

  - preserving deliberate narrative meaning;
  - maintaining authorial intent;
  - constructing characters, conflicts, themes, and planned developments;
  - producing carefully controlled dramatic structure.

- Their limitation is **branching cost**. As Participant agency increases, meaningful alternatives must increasingly be anticipated, authored, implemented, and maintained across divergent state.

- Probabilistic systems provide capabilities that neither approach historically possessed:

  - interpretation of open-ended Participant actions;
  - contextual and semantic reasoning;
  - Cognitive Actor reasoning;
  - adaptation to combinations of circumstances that were never explicitly enumerated;
  - generation of appropriate responses within novel situations.

- Their limitation is almost the inverse of conventional computation: they are poorly suited to being the sole authority over persistent world state, chronology, identity, provenance, and long-term causal continuity.

- Enclave does not attempt to replace any of these approaches. It combines their complementary strengths while assigning their weaknesses elsewhere.

- Human authors provide:

  - narrative meaning and thematic intent;
  - characters, institutions, conflicts, and motivations;
  - the initial Knowledge Base;
  - intended developments and narrative pressures;
  - the meaningful possibility space within which the narrative develops.

- Persistent computational systems provide:

  - authoritative world state;
  - durable identity and chronology;
  - persistent Facts, Memories, and Events;
  - deterministic constraints;
  - causal continuity;
  - Knowledge classification, availability, and propagation.

- Probabilistic systems provide:

  - interpretation of open-ended situations;
  - contextual relevance;
  - semantic flexibility;
  - Cognitive Actor reasoning;
  - interpretation of Participant actions;
  - adaptation to circumstances that were not explicitly anticipated.

- Loci prevent the existence of Knowledge from implying universal access to it.

- Domains, Enclaves, and Rank organize and constrain what portions of the Knowledge Base are relevant within a particular context.

- Events and Memories allow Participant and Actor activity to modify the persistent Knowledge Base without transferring authority over that state to the probabilistic systems interpreting those activities.

- The resulting separation allows probabilistic systems to determine **what an action means** without independently determining **what is true**, while persistent systems can determine **what occurred** without having to encode every possible semantic interpretation in advance.

- Likewise, human authors can construct a deeply authored narrative world without constructing every narrative branch that might arise within it.

- Enclave therefore does not eliminate branching. It moves branching out of an explicitly authored tree and into the interactions between persistent state, Knowledge distribution, Actor and Participant agency, and subsequent Events.

- **Enclave combines the persistence and exactness of conventional computation, the interpretive flexibility of probabilistic systems, and the narrative depth of human authorship so that each system operates primarily within the class of problems it handles well.**

- The result is a deeply authored narrative environment capable of absorbing unforeseen Participant action while preserving persistent consequence, coherent world state, and authorial structure.

## 8. Layers of Authority

### 8.1 Different Authority for Different Layers

- Enclave depends on systems with radically different capabilities operating over the same persistent narrative world.

- For those systems to operate together, **capability must remain distinct from authority**.

- Enclave treats authority as a form of **jurisdiction**: each layer controls a specific class of decisions while remaining constrained by decisions belonging to other layers.

- Human authors possess authority over the authored structure and intended narrative possibility space.

- The persistent computational system possesses authority over canonical Knowledge, persistent state, and accepted Events.

- Actors possess authority over the actions available to them within the circumstances and capabilities presented by the world.

- Participants introduce an additional boundary because their cognition occurs outside Enclave. They can contribute unpredictable actions, claims, deductions, and information, but those contributions enter the same authority structure as those produced internally.

- Probabilistic systems possess broad interpretive capability. They may:

  - determine the likely meaning of open-ended input;
  - reason over ambiguous circumstances;
  - infer relevance;
  - construct Cognitive Actor responses;
  - propose interpretations, actions, or new information.

- They do not hold authority over critical or persistent state.

- Authority instead transfers between layers through explicit interactions.

- A Participant may state that the king is dead.

- A probabilistic system may correctly interpret that statement as a claim about the king.

- An Actor may hear and believe the claim.

- A Locus may propagate it throughout the world.

- None of those events mean that the king is actually dead.

- Conversely, an authoritative Event establishing the king's death does not make every Actor immediately aware of it, cause every Actor to believe it, or determine how Actors respond.

- The same narrative development can therefore simultaneously have:

  - an authoritative state;
  - distributed information about that state;
  - conflicting beliefs about that information;
  - probabilistic interpretations of its significance;
  - Actor and Participant responses to those interpretations.

- These are not competing versions of the world. They are different layers exercising different forms of authority over the same world.

- This separation creates one coherent system capable of maintaining consistent authority over a large and evolving **Knowledge Base** by allowing every layer to contribute where its capabilities are strongest.

- Authority follows capability.

### 8.2 Authorial Authority

- Human authors possess authority over the authored structure from which the narrative develops.

- This includes:

  - people and institutions;
  - relationships and conflicts;
  - motivations and goals;
  - secrets and information;
  - Domains, Enclaves, and other authored classifications;
  - intended developments;
  - constraints and possibilities;
  - thematic and narrative purpose.

- This forms the initial **Knowledge Base**.

- Authorial authority establishes the initial conditions and meaningful *possibility space* of the narrative.

- It does not require the author to determine the realized sequence of Events in advance.

- Intended developments may therefore exist as authorial intent without possessing runtime inevitability.

- Participant and Actor actions can alter the circumstances under which authored intentions are evaluated, redirecting or preventing developments without removing the human authorship embedded in the world.

- Runtime systems operate upon and extend this authored structure rather than replacing it.

### 8.3 Knowledge Authority

- Enclave distinguishes between **information that exists within the world** and **information the system accepts as canonical**.

- Knowledge may represent:

  - established facts;
  - world state;
  - authored facts;
  - observations;
  - communications;
  - records;
  - rumours;
  - beliefs;
  - misinformation;
  - incomplete or outdated accounts;
  - inferred or fabricated information.

- However the existence of Knowledge does not necessarily grant that Knowledge authority.

- The persistent computational system maintains the authoritative distinction between canonical and non-canonical Knowledge.

- **Canonical Knowledge** represents what the authoritative system currently accepts as true of the persistent world and narrative state.

- **Non-canonical Knowledge** may persist, propagate, influence Actors, and produce consequences without becoming authoritative truth.

- Probabilistic systems may interpret existing Knowledge or generate candidate information, but plausibility alone does not make that information canonical.

- Cognitive Actors may believe, doubt, reject, misunderstand, or reinterpret Knowledge without altering its authoritative status by doing so.

- Participants may likewise introduce claims or interpretations through external cognition without automatically changing canonical Knowledge.

- Knowledge authority therefore maintains the critical story barrier between what is known, and what is true.

### 8.4 Actor Authority

- Actors possess authority over their own actions within the limits of the capabilities available to them.

- Those actions may originate through:

  - deterministic logic;
  - probabilistic reasoning;
  - Participant input;
  - environmental or mechanical processes;
  - combinations of these mechanisms.

- Actor authority does **not** impart authority over consequences.

- An Actor firing a weapon can infer its consequences, but does not determine them.

- A Participant may state a claim without making the claim true.

- An institution may issue an order while lacking assurance that order is obeyed.

- A machine may perform an operation whose input depends on circumstances outside its control, failing if those circumstances are not met.

- Failure is itself eligible to become part of canonical history.

- Actors determine what they do; authoritative resolution determines what those actions cause.

### 8.5 Action, Resolution, and Consequence

- Actors enter a narrative world that already possesses authoritative state, constraints, and history.

- Consequences are therefore resolved against the world as it currently exists.

- Resolution may consider:

  - location;
  - physical possibility;
  - Actor capabilities;
  - available resources;
  - permissions and access;
  - relationships;
  - timing;
  - environmental conditions;
  - simultaneous or conflicting Events;
  - deterministic rules;
  - other authoritative constraints represented by the system.

- Open-ended actions may require probabilistic interpretation before they can be evaluated, but interpretation and resolution remain separate responsibilities.

- Interpretation provides the machine-readable representation required by the authoritative system to evaluate an otherwise open-ended action.

- A probabilistic system may determine that a Participant's natural-language action means an attempt to intimidate a guard, sabotage a machine, reveal a secret, or perform some other semantically meaningful action.

- The authoritative system then evaluates that interpreted action against the persistent world.

- Resolution may produce:

  - success;
  - failure;
  - partial success;
  - an unintended consequence;
  - no meaningful change;
  - one or more new Events.

- Accepted outcomes become **Events**, which modify the persistent world and Knowledge Base.

- Events may:

  - establish new canonical Knowledge;
  - change existing world state;
  - instantiate, alter, or remove Actors;
  - transmit Knowledge through Loci;
  - alter later conditions and possibilities;
  - create circumstances from which further actions arise.

- This separation allows Enclave to accept arbitrarily expressive actions without granting the system interpreting those actions authority to rewrite the world.

### 8.6 A Single Source of Truth

- Enclave ultimately maintains one authoritative account of the running world.

- One that does **not** require every Actor to possess the same information or every item of Knowledge to agree.

- Multiple contradictory accounts can coexist within the Knowledge Base.

- Different Actors may receive different information, remember different Events, reach different conclusions, or deliberately communicate falsehoods.

- A false account may propagate widely.

- An outdated account may remain historically significant.

- An Actor may confidently believe something that canonical Knowledge establishes as false.

- These disagreements exist **within one authoritative world rather than creating competing authoritative worlds**.

- This creates a classic Single-Source-of-Truth version of the world from which all systems can operate.

- Traditional computational systems maintain that authority and expose only relevant portions of the world through Loci and other controlled interfaces.

- Probabilistic systems and Cognitive Actors interpret those limited perspectives rather than receiving unrestricted authority over global state.

- Events feed resolved consequences back into the persistent world, allowing canonical state to change without abandoning continuity or provenance.

- Enclave can therefore support broad generative and interpretive freedom while retaining a singular persistent answer to the question:

  **What actually happened?**

- This authority model allows belief, misinformation, ambiguity, interpretation, and disagreement to remain narratively meaningful without sacrificing a coherent underlying reality.

---

## 9. Primitives

### 9.1 Seven Foundational Primitives

- Enclave is constructed around seven foundational primitives.

- The seven primitives are organized into three families:

  **Knowledge**

  - **Facts** - persistent representations of information within the narrative world;
  - **Memories** - Actor-specific records of identity and history;
  - **Events** - authoritative occurrences within the world and records of their effects.

  **Nexuses**

  - **Loci** - points through which Knowledge can be retained, received, exposed, transmitted, or acted upon;
  - **Actors** - agents capable of acting upon the narrative world;
  - **Participants** - Cognitive Actors whose reasoning originates outside Enclave.

  **Classification**

  - **Domains** - semantic classifications describing what Knowledge concerns.

- The three families describe complementary dimensions of the same narrative system:

  - Knowledge describes **what information, experience, and occurrence persist**;
  - Nexuses describe **where information is situated or exchanged and where agency enters the world**;
  - Classification describes **how Knowledge is semantically organized and made relevant**.

- Together they operate over one persistent **Knowledge Base** and one authoritative running world.

---

### 9.2 Facts

- **Facts** are persistent computational representations of information that exist within Enclave.

- Facts are deterministic representations rather than probabilistic recollection.

- The term *fact* is architectural and does not imply truth.

- A Fact may represent:

  - authoritative world state;
  - observations;
  - claims;
  - reports;
  - records;
  - rumours;
  - testimony;
  - beliefs;
  - deductions;
  - misinformation;
  - lies;
  - outdated information;
  - incomplete information;
  - other narratively meaningful information.

- The existence of a Fact and the authority of that Fact are therefore separate properties.

- **Canonical Facts** represent information the authoritative system accepts as true of the persistent world.

- **Non-canonical Facts** represent information that exists within the world without necessarily being true.

- A false rumour can therefore persist as a Fact, propagate between Actors, alter behaviour, and produce real consequences without becoming canonical.

- Likewise, a canonical Fact may exist without being available to any particular Actor.

- Facts therefore answer neither:

  - **who knows this?**
  - nor **who believes this?**

- Those questions are represented through the relationships between Facts and the Nexus family.

- Facts are stored independently from individual Actors wherever practical.

- Multiple Actors may therefore reference the same persistent Fact rather than requiring duplicated copies of the underlying information.

- This provides a common persistent informational substrate while allowing different Actors to possess radically different informational perspectives.

---

### 9.3 Memories

- **Memories** are the persistent record of a particular Actor's interactions, experiences, and identity.

- Memories preserve the Actor-specific context surrounding what occurred rather than only the transmissible informational content that may be extracted from it.

- A Memory may contain:

  - who was present;
  - what was said;
  - what the Actor observed;
  - what actions occurred;
  - sequence;
  - location;
  - circumstances;
  - emotional or contextual information;
  - relationships to existing Knowledge;
  - relationships to Events;
  - details that may never become narratively important.

- Memories are therefore generally richer and potentially much higher-volume than the shared Knowledge they reference or produce, increasing with the Actor's prominence in the narrative.

- A Memory does not automatically become transmissible Knowledge.

- When narratively meaningful information appears within a Memory, the system may determine whether that information:

  - corresponds to existing Knowledge;
  - modifies or contextualizes existing Knowledge (applies mainly to generated Knowledge);
  - represents genuinely new Knowledge;
  - is too insignificant to require broader persistent representation.

- Where a Memory refers to existing Knowledge, the Memory can be substituted for a reference to that Knowledge to avoid duplicating the underlying fact.

- Where a Memory contains genuinely novel and narratively relevant information, that information may enter the Knowledge Base.

- Memory-derived Knowledge generally non-canonical.

- It may enter as:

  - testimony;
  - belief;
  - rumour;
  - inference;
  - misunderstanding;
  - fabrication;
  - speculation;
  - or another lower-authority form of Knowledge.

- Memories therefore provide one route by which the narrative world can acquire information that was never explicitly authored and did not originate through authoritative world-state resolution.

- Memories also contain the authored Actor specific context necessary for Cognitive actors to create and maintain a consistent persistent identity.

- The distinction between Memories and broader Knowledge resembles the established distinction between episodic and semantic memory established by Tulving, Greenberg & Verfaellie:

  - episodic memory preserves contextual experience;
  - semantic memory represents information independently of a particular remembered episode.

- **Support:** Tulving (2002); Greenberg & Verfaellie (2010).

- **Reference:&#x20;**&#x54;his paper assumes the deployment of a memory architecture similar to the Reliquary system found here: [https://www.github.com/Lokee86/Reliquary](https://www.github.com/Lokee86/Reliquary)

---

### 9.4 Events

- **Events** are the persistent authoritative record of occurrences accepted as having happened within the narrative world.

- Where Facts may be canonical or non-canonical, an Event records an authoritative occurrence and its consequences.

- Events arise when actions are resolved against authoritative world state.

- Their inputs may originate through:

  - deterministic systems;
  - Actor actions;
  - Participant actions;
  - probabilistic interpretation;
  - environmental processes;
  - authored conditional developments;
  - combinations of these mechanisms;
  - anything else that may interact with the narrative substrate.

- Probabilistic interpretation may determine what an open-ended action or circumstance means, but it does not itself establish an Event.

- The Event exists only once the resulting occurrence has been accepted by the authoritative system.

- An Event therefore records both:

  - what occurred;
  - and the authoritative consequences produced by that occurrence.

- Events may:

  - change existing world state;
  - create, alter, or remove Loci;
  - instantiate, alter, or remove Actors;
  - alter relationships;
  - change resources or circumstances;
  - transmit or expose Knowledge;
  - satisfy or invalidate conditions;
  - create conditions for later Events;
  - make authored developments possible, impossible, or materially different.

- Facts spawned from Events always enter the system as canonical.

- An Event occurring does **not** make every Actor aware of it.

- Knowledge concerning the Event must still be acquired through appropriate Loci.

- Different Actors may therefore subsequently receive:

  - accurate Knowledge concerning the Event;
  - incomplete Knowledge;
  - distorted Knowledge;
  - false explanations;
  - conflicting reports;
  - or no Knowledge of the Event at all.

- Those informational consequences remain distinct from the authoritative Event itself.

- Events therefore provide the principal runtime mechanism by which action and changing circumstances become persistent canonical history.

---

### 9.5 Loci

- **Loci** are points through which Knowledge can be retained, received, exposed, transmitted, or acted upon.

- A Locus describes a point of information availability or exchange within the narrative world, not a capacity for cognition or action.

- Examples may include:

  - books;
  - letters;
  - records;
  - archives;
  - libraries;
  - computer terminals;
  - databases;
  - recordings;
  - artifacts;
  - communication systems;
  - other represented information-bearing entities or interaction contexts.

- A Locus can preserve, expose, or transmit Knowledge without understanding or believing it.

- Knowledge may therefore persist and propagate independently of any Cognitive Actor.

- A piece of Knowledge may exist within the global Knowledge Base while remaining available through only a small number of Loci.

- Knowledge availability is therefore represented through relationships with points of availability or interaction rather than through global assignment.

- A Locus may:

  - acquire Knowledge;
  - retain Knowledge;
  - expose Knowledge;
  - transmit Knowledge;
  - cease exposing Knowledge;
  - lose access to Knowledge;
  - become inaccessible;
  - be created;
  - be altered;
  - be destroyed.

- A Locus need not correspond to one fixed category of world entity. Depending on implementation, the relevant Locus may be an information-bearing object, an ambient observation context, presence at an Event, an involved entity, or another point of interaction.

- These roles allow information flow and cause-and-effect narrative emergence.

---

### 9.6 Actors

- **Actors** are entities capable of acting upon the narrative world.

- Action is the defining distinction.

- An Actor may use some combination of:

  - current state;
  - capabilities;
  - circumstances;
  - available Knowledge;
  - deterministic logic;
  - probabilistic reasoning;
  - external Participant input;

  to determine what it does.

- Actors may be **Simple** or **Cognitive**.

- Simple Actors may include:

  - deterministic NPCs;
  - automated machines;
  - vehicles;
  - factories and productive systems;
  - infrastructure;
  - persistent natural phenomena;
  - other represented entities capable of consequential action.

- Simple Actors do not possess open-ended cognition.

- Their behaviour instead follows deterministic rules, schedules, state transitions, environmental conditions, or other represented mechanisms.

- Cognitive Actors can additionally:

  - interpret Knowledge;
  - reason over circumstances;
  - form beliefs;
  - make decisions;
  - communicate;
  - pursue goals;
  - revise previous conclusions;
  - generate novel claims, deductions, or interpretations.

- Actors are not omniscient.

- They act using their available capabilities, circumstances, and Knowledge made available through ambient or directly accessible Loci rather than from complete authoritative Knowledge.

- Domains, Enclaves, Rank, Memories, observations, and present circumstances may further determine which portions of the Knowledge Base are relevant or available to a particular Actor.


### 9.7 Participants

- **Participants** are Cognitive Actors whose cognition originates outside Enclave.

- In interactive media they are generally the human players.

- Enclave therefore does not possess direct authority over or complete visibility into Participant cognition.

- A Participant may:

  - observe information;
  - remember or forget it;
  - believe or reject it;
  - notice implications the system never explicitly presented;
  - make deductions;
  - misunderstand information;
  - reinterpret previous information;
  - deliberately deceive another Actor;
  - introduce entirely novel reasoning or information.

- Enclave can authoritatively record what Knowledge was made available to a Participant.

- It can likewise record the actions and communications a Participant externalizes.

- It cannot authoritatively determine what the Participant internally:

  - remembers;
  - believes;
  - understands;
  - infers;
  - intends;

  unless that cognition is subsequently expressed through observable action or communication.

- Participant cognition therefore creates an external interpretive boundary:

  `Knowledge exposure → external cognition → Participant action or communication → Enclave`

- Once externalized, Participant actions and communications enter the same authority structure as other Actor activity.

- A Participant may introduce previously nonexistent non-canonical Knowledge by communicating a novel claim.

- That Knowledge may then:

  - enter another Actor's Memory;
  - be associated with or modify existing Knowledge;
  - propagate through Loci;
  - influence Actor behaviour;
  - acquire substantial narrative importance.

- Participant action can change canonical reality only through authoritatively resolved consequences.

---

### 9.8 Domains

- **Domains** are broad semantic classifications describing what Knowledge concerns.

- Examples may include:

  - Medicine;
  - Engineering;
  - Navigation;
  - Law;
  - History;
  - Politics;
  - Geography;
  - Chemistry;
  - Military doctrine;
  - other broad authored areas of knowledge.

- Domains describe **subject matter**.

- They do not determine:

  - truth;
  - canonical authority;
  - belief;
  - ownership;
  - availability;
  - Actor membership.

- A single item of Knowledge may belong to multiple Domains.

- Knowledge concerning the destruction of a bridge, for example, might concern:

  - Engineering;
  - Transportation;
  - Geography;
  - Military;
  - Politics.

- Domains provide the broad semantic structure through which the Knowledge Base can be organized and searched without treating all persistent information as equally relevant.

- Domain relationships may apply to both authored and runtime-generated Knowledge.

- Human authors establish the Domain structure of the initial Knowledge Base.

- New Knowledge, created by Memories and Events, can subsequently be classified into that structure as the narrative develops.

- Domains provide the foundational classification structure of the Knowledge Base.

- More specialized contextual classifications derived from Domains are addressed in the following section.

---

### 9.9 Primitive Interaction

- The seven foundational primitives are organized into three families describing complementary dimensions of one persistent narrative system.

  **Knowledge**

  - **Facts** - What information exists within the system, and what authority does that information possess?
  - **Memories** - What Actor-specific history, experience, and context should persist?
  - **Events** - What occurrence has been authoritatively accepted as having happened, and what consequences followed?

  **Nexuses**

  - **Loci** - Through what point can Knowledge be retained, received, exposed, transmitted, or acted upon?
  - **Actors** - What persistent entity is capable of action?
  - **Participants** - What Cognitive Actor derives its reasoning from outside Enclave?

  **Classification**

  - **Domains** - Within what semantic or classificatory context does Knowledge belong?

- These relationships overlap rather than partitioning the world into mutually exclusive categories.

- A Cognitive Actor can simultaneously:

  - possess Memories;
  - interact with Knowledge spanning multiple Domains;
  - receive and transmit Knowledge through Loci;
  - take actions that resolve into Events.

- Ordinary narrative activity can therefore cross all three primitive families.

- Knowledge may also enter the system directly through human authorship or other authoritative initialization and therefore does **not** need to originate from either a Memory or an Event.

  - this type of Knowledge augmentation would generally include additions such as expansion content or DLC.

- Likewise, a Locus does not need to be an Actor, an Actor does not need to be Cognitive, and a Fact does not need to belong to any particular Domain.

- The primitives therefore provide composable relationships rather than mandatory sequential stages.

- **Facts provide persistent information.**

- **Memories preserve Actor-specific history.**

- **Events preserve authoritative occurrence and consequence.**

- **Loci provide informational presence, transmission, and points of interaction.**

- **Actors provide causal agency.**

- **Participants provide external cognition and agency.**

- **Domains provide the foundational classification of Knowledge.**

- Together these primitives allow one Knowledge Base to support:

  - authoritative world state;
  - persistent history;
  - asymmetric information;
  - contradictory and false information;
  - Actor-specific perspective;
  - semantic classification and bounded relevance;
  - emergent Knowledge;
  - external Participant agency;
  - persistent cause and effect;
  - deterministic authority over what actually occurred.

- More specialized structures for organizing Knowledge around Actor populations, access, hierarchy, and other contextual relationships are derived from these foundational primitives and are addressed in the following section.

- The resulting architecture allows the Knowledge Base to expand through human authorship, Actor activity, Participant input, Memory, and Events without requiring any individual Actor or probabilistic system to maintain the authoritative world itself.

---

## 10. Key Derivatives

### 10.1 Derivation From the Foundational Primitives

- The seven foundational primitives describe the basic entities and relationships required by the architecture.
- Several additional concepts arise naturally through specialization, composition, or relationship between those primitives.
- These concepts are important enough to require explicit definition but do not represent additional foundational primitives.
- The principal derivatives are:
  - Interactions;
  - Enclaves;
  - Rank;
  - Facets;
  - Combinatorial Enclaves;
  - Inheritance.

---

### 10.2 Interaction

- **Interaction** is a derivative form of Event characterized by causal process.
- Events record authoritative occurrence and consequence.
- Interaction identifies the causal process through which an occurrence develops.
- Actors participate in Interactions.
- An Interaction may be represented at different levels of fidelity.
- What appears as one Interaction at one level of simulation may contain many lower-level Interactions and Events at another.
- The degree of causal decomposition is therefore an implementation and fidelity concern rather than a requirement of the ontology.

---

### 10.3 Enclaves

- **Enclaves** are specialized Domains associated with Actor populations.
- Where Domains classify Knowledge semantically, Enclaves extend classification by relating bodies of Knowledge to specific contextual populations.
- Enclaves will frequently be cross-Domain.
- An Enclave may draw relevant Knowledge from several Domains simultaneously.
- Enclaves may represent:
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
- Actors may belong to multiple Enclaves simultaneously.
- Enclave membership can contribute to:
  - Knowledge availability;
  - institutional access;
  - contextual relevance;
  - expected familiarity;
  - plausible exposure;
  - plausible transmission routes;
  - permissions;
  - social relationships.
- Enclave membership does not imply universal Knowledge among members.
- Knowledge must still reach Actors through appropriate mechanisms.
- Leaving an Enclave does not erase Knowledge already acquired through it.
- Enclaves may contain or descend from other Enclaves, producing hierarchy.

---

### 10.4 Rank

- **Rank** is a specialized subordinate Enclave intrinsic to every Enclave.
- Each Enclave possesses its own Rank structure. Recommended to be expressed in system by numerical scale.
- Rank regulates differentiated Knowledge access and related contextual relationships within its parent Enclave.
- Rank operates through the same basic mechanisms as other Enclave relationships rather than requiring a separate foundational classification primitive.

---

### 10.5 Facets

- **Facets** represent identifiable entities whose relevant context is expressed through multiple independent Enclave hierarchies.
- A Facet is not merely a broad category of Enclaves.
- It represents one entity viewed through several distinct organizational, social, geographic, institutional, or other Enclave structures.
- The same represented concept will generally simultaneously exist as:
  - a separate Enclave within a hierarchy;
  - a Facet containing or relating several independent hierarchies.
- A city provides the clearest example.
- `Nanaimo` may exist as a Geographic Enclave within:
  - `Canada → British Columbia → Vancouver Island → Nanaimo`
- The represented entity Nanaimo may also function as a Facet containing or relating independent Enclave hierarchies associated with:
  - municipal government;
  - policing;
  - criminal organizations;
  - foreign diplomats;
  - schools;
  - healthcare;
  - businesses;
  - neighbourhood organizations;
  - religious communities;
  - other locally situated institutions or populations.
- These hierarchies are meaningfully related through the same entity but do not necessarily share one valid parent authority hierarchy.
- If a set of classifications can be truthfully represented as one Enclave hierarchy, a Facet may be unnecessary.

---

### 10.6 Combinatorial Enclaves

- **Combinatorial Enclaves** represent the conjunction or intersection of two or more Enclaves.
- They identify populations satisfying all included Enclave conditions.
- Examples may include:
  - `Intelligence + NorthernCommand`;
  - `Intelligence + VancouverIsland`;
  - other combinations spanning one or several Enclave hierarchies.
- Enclave ordering should not change combinatorial identity.
- Equivalent combinations should therefore resolve to one canonical identity.
- Combinatorial Enclaves may cross hierarchy boundaries.
- The full semantic identity of a Combinatorial Enclave remains valid even when its resulting Actor population is identical to that of another combination.

---

### 10.7 Inheritance

- **Inheritance** describes parent-child relationships between Enclaves.
- Membership in a child Enclave implies membership in its parent Enclave.
- Inheritance is transitive through all ancestors.
- For example:
  - `Military → Army`;
  - `Army → Intelligence`;
  - `Army → NorthernCommand`.
- Membership in `Intelligence` therefore also implies membership in `Army` and `Military`.
- Inheritance preserves the distinct semantic identity of every Enclave and Combinatorial Enclave.
- A combination such as `Military + Intelligence` remains a valid combinatorial identity even where its Actor population is identical to `Intelligence`.
- Likewise, `Military + Army + Intelligence` may remain addressable despite requiring no additional population intersection.
- Inheritance therefore allows multiple combinatorial identities to reference the same underlying population representation.
- Parent-child implication eliminates many redundant population calculations.
- In the example:
  - `Military`;
  - `Army`;
  - `Intelligence`;
  - `NorthernCommand`;
    generate fifteen possible non-empty combinatorial identities.
- Under Inheritance, many of those identities resolve to already-known populations.
- The genuinely new intersection may only be:
  - `Intelligence + NorthernCommand`.
- The important distinction is therefore:
  - **combinatorial identity is cheap;**
  - **population intersection is expensive.**
- Full combinatorial depth can consequently be preserved without independently calculating every combination.
- Actor-derived combination generation, transitive inheritance, reuse of equivalent population sets, and restricted comparison at appropriate hierarchy levels can substantially reduce practical computational burden.
- Inheritance is included for consideration mainly because a set of `n` independently combinable Enclaves permits up to `2^n - 1` non-empty combinations.
- Naively evaluating all possible combinations therefore creates exponential computational growth and severely limits practical implementation.
- Inheritance is therefore used to reduce the computational burden through hierarchy-aware computation.
- The detailed mathematics and implementation strategies for combinatorial reduction are addressed in Addendum B.

---

## 11. Knowledge Distribution and Access

> This section describes how Knowledge is initially distributed, becomes available to Actors, propagates through the world, becomes institutionally established, and remains distinct from authoritative truth.

### 11.1 Initial Knowledge Distribution

- The existing Knowledge Base presents a universal source of truth representing all Knowledge within the narrative possibility space.
- Some knowledge may be universally accessible depending on the setting, but most is not intended to be known by every actor in the narrative.
- The initial model is and organized and fully-authored graph of Domains > Facets > Enclaves & Combinatorial Enclaves > Ranks > Memory
- The Knowledge accessible to a given Actor is calculated during instantiation and is determined by the Actor's pre-written Knowledge graph, which is built from cumulative Enclave membership and Rank and Domain Ranks, as well as any authored, generated, or assigned Actor specific Knowledge.
- Initial availability may therefore be derived from:
  - physical location;
  - institutional membership;
  - profession;
  - social relationships;
  - Enclave membership;
  - Rank;
  - possession of or access to a particular Locus;
  - prior history;
  - authored personal Knowledge;
  - other world-specific relationships.
- Enclave relationships allow initial Knowledge access to be described structurally as a graph rather than authored independently for every Actor.
- Inheritance allows relationships associated with parent Enclaves to apply appropriate access to members of descendant Enclaves.
- Combinatorial Enclaves allow more specific access relationships to be associated with Actors satisfying several contextual conditions simultaneously.
- Facets may provide the broader entity context through which several otherwise independent Enclave hierarchies become relevant to the same Actor or circumstance.
- These relationships define what Knowledge an Actor could reasonably possess at the beginning of the simulation.
- They do specifically imply that every Actor within an Enclave has different access to Facts associated with it.
- Initial distribution should therefore represent bounded Actor perspective rather than provide a complete copy of authoritative world state.
- Shared Knowledge should be referenced rather than duplicated wherever practical.

### 11.2 Knowledge Transmission

- Knowledge moves through Interactions involving Actors, Participants, and Loci.
- Transmission occurs when Knowledge becomes newly available through an interaction or point of exposure.
- Transmission may occur through:
  - direct communication;
  - observation;
  - written or recorded information;
  - artifacts;
  - institutional records;
  - communication systems;
  - computational systems;
  - environmental evidence;
  - other authored or emergent mechanisms.
- A Locus may expose Knowledge without possessing cognition or belief.
- An Actor may acquire Knowledge from a Locus without accepting that Knowledge as true.
- A Participant may acquire Knowledge externally and later reintroduce it through action or communication.
- Transmission therefore concerns exposure and availability rather than truth or belief.
- Canonical and non-canonical Knowledge may propagate through the same mechanisms.
- A false rumour may therefore spread farther and faster than the canonical Knowledge that contradicts it, or it may not.
- It's important to note that this transmission can be simulated through primarily probabilistic means, or it can be done entirely deterministically through classic contact algorithms, or a combination of both.

### 11.3 Emergent Diffusion

- Once acquired, Knowledge may subsequently be retransmitted through other Actors, Participants, and Loci.
- Facts can therefore continue moving through the world long after the Event or Interaction that introduced them.
- Diffusion may be shaped by:
  - social relationships;
  - geographic proximity;
  - Enclave membership;
  - Rank;
  - Inheritance;
  - communication infrastructure;
  - Actor behaviour;
  - institutional processes;
  - Knowledge relevance;
  - time.
- Different Actors may transmit:
  - the original Fact;
  - an incomplete version;
  - a distorted version;
  - a derived interpretation;
  - a contradictory claim;
- In this way rumours, renown, myths, and even legends can develop naturally in long lived enough simulations.
- Different portions of the world may consequently develop radically different informational states while remaining part of one authoritative world.
- Ordinary diffusion can be simulated to any degree of fidelity required by or possible for the implementation.
- Emergent diffusion therefore allows local actions to acquire broad narrative consequence without requiring explicitly authored propagation trees.

### 11.4 Enclave Saturation and Institutional Knowledge

- **Saturation** describes the degree to which a particular item of Knowledge has propagated through the Actor population of an Enclave.
- It is a cost-efficiency method meant to abstract widespread institutional transmission where individual propagation would provide little additional narrative or product value.
- Saturation is therefore a relationship between:
  - a Fact;
  - an Enclave;
  - and the relevant Actor population within that Enclave.
- Saturation provides both:
  - a narrative model for information becoming commonly established within a population;
  - a computational mechanism for reducing large numbers of individual propagation relationships with a higher-level institutional relationship.
- As Actors independently acquire the same Fact, its saturation within the relevant Enclave increases.
- Saturation is evaluated against escalating Combinatorial Enclaves to simulate constrained institutional spreading through regions or other types of sectors.
- Saturation is evaluated against the narrowest meaningful contextual population first and reaches upward through broader populations as a Fact spreads.
- A Fact may therefore be highly saturated within one subordinate or Combinatorial Enclave while remaining rare or emergent elsewhere.
- Saturation does not require every Actor within and Enclave to possess the Fact. It is instead controlled by and arbitrary Saturation Threshold.
- The specific Saturation Threshold is an implementation and world-design decision.
- When a Fact reaches an appropriate saturation threshold within an Enclave, it becomes **Institutional Knowledge** of that Enclave.
- Institutional Knowledge represents information that has become sufficiently established within an organization, community, profession, region, or other Enclave that the Enclave itself can reasonably act as a continuing source of that Knowledge.

### 11.5 Institutional Emission

- Institutionalization does not necessarily imply that every member immediately knows the Fact.
- This is one possible result of Saturation, but higher fidelity simulations may choose to exclusively employ Institutional Emission instead
- Instead, the Enclave may begin to **emit** the Fact through ordinary institutional mechanisms.
- Emission may represent:
  - briefings;
  - records;
  - orders;
  - routine communication;
  - professional practice;
  - organizational documentation;
  - public notices;
  - announcements;
  - publications;
  - shared repositories;
  - training;
  - cultural repetition;
  - other contextually appropriate channels.
- Eligibility may still depend on:
  - Enclave membership;
  - Rank;
  - access to relevant Loci;
  - other contextual constraints.
- Participants are not automatically granted Institutional Knowledge merely because an Enclave has institutionalized it.
- A Participant must still encounter the Knowledge through an appropriate Locus, Actor, Event, or other represented interaction.
- Because of this Emission is a standard consequence of Saturation, regardless of fidelity level.
- Institutional Knowledge can weaken, disappear, become inaccessible, or be superseded if the represented world provides mechanisms for those changes.
  - This would generally be modelled through disaster, colonializing, aging Enclave membership, or other narratively relevant means.
- Institutional emission therefore provides a causal abstraction for large-scale information distribution rather than a global synchronization mechanism.

### 11.6 Information as World State

- Information becomes part of the distributed persistent state of the simulated world.
- The system does not only represent:
  - what is true;
  - what has happened;
  - where Actors and objects are;
  - and other conventional world state.
- It also represents the narrative informational state of that world, including:
  - what Knowledge exists;
  - where that Knowledge is available;
  - which Actors possess or have encountered it;
  - which Loci expose it;
  - which Enclaves have institutionalized it;
  - where it is being emitted;
  - how broadly it has propagated;
  - which competing or contradictory versions exist.
- These relationships can therefore be stored, queried, changed, and persisted in the same manner as other world state.
- For the stated goal of a sandboxed narrative change in information distribution is consequently a genuine change in the state of the world.
- An Actor learning a Fact, an institution adopting a rumour, a record being destroyed, or a population becoming saturated with particular Knowledge may be narratively consequential even where no physical state has changed.
- Informational state itself becomes causal:
  - Actors may act because of what they know;
  - Actors may act because of what they incorrectly believe;
  - institutions may respond to Institutional Knowledge;
  - access to Knowledge may enable or prevent later Interactions;
  - the spread or suppression of Knowledge may alter future Events.
- The authoritative system is therefore responsible for preserving **the state of evolving narrative information**, not merely authoritative canonical truth.
- Canonicality remains an independent property of that Knowledge.
- Institutional emission may therefore distribute false, incomplete, distorted, or outdated Knowledge as readily as accurate Knowledge.
- A false belief may therefore be authoritatively represented as widespread world state without becoming authoritative truth.
- Likewise, canonical Knowledge may remain obscure, inaccessible, disputed, or entirely unknown to most Actors.
- This allows Enclave to maintain one authoritative world while simultaneously preserving many different informational perspectives within it.
- Information can therefore participate in ordinary deterministic persistence and causality without requiring probabilistic systems to remember or reconstruct who knew what.

---

## 12. Actor Cognition

> This section describes the function and operation of LLM driven or assisted Cognitive Actors.

### 12.1 Bounded Narrative Agents

- At this point astute readers may have noticed that Enclave's primitives, informational state, Knowledge distribution, Actor relationships, Events, Interactions, and persistent cause and effect can all be represented and resolved through conventional computational systems without probabilistic cognition or resolution.
- A sufficiently formalized implementation could therefore use Enclave as the informational and causal architecture for a conventional deterministic simulation.
- The system could even theoretically be applied to a more traditional procedurally generated narrative like those found in Dwarf Fortress.
- **Support / precedent:** Adams (2021); Ryan (2018).
- Its primary design purpose, however, is to provide the persistent structure necessary for faithful, bounded, and unsupervised narrative agents to operate within the *narrative design space safely*.
- These agents are intended to operate as inhabitants of the authored world rather than as omniscient narrative generators.
- Each agent reasons from its own persistent position within the world granting it a unique perspective.
- That perspective is generated from its collective Knowledge and Memories, together forming a unique experience.
- That experience may include:
  - its relationships;
  - its Enclave memberships;
  - its Rank;
  - its accessible Loci;
  - its current circumstances;
  - its goals;
  - its incomplete or incorrect beliefs;
  - any other Actor relevant context
- The agent therefore does not receive the narrative world as the authoritative system knows it.
- It receives the world from the perspective that a specific entity can know and experience it.
- This bounded perspective allows probabilistic cognition to operate independently without requiring continuous human supervision while remaining constrained by authored character, persistent history, and actual informational access.
- An agent may consequently:
  - interpret unfamiliar circumstances;
  - react to Participant behaviour that was never explicitly anticipated;
  - form plans;
  - communicate;
  - misunderstand;
  - deceive;
  - remember;
  - adapt its behaviour;
  - and respond to consequences generated elsewhere in the world.
- Because those responses are generated from a persistent, bounded perspective rather than from omniscient narrative context, different agents may respond to the same circumstances in radically different but internally faithful ways.
- No single omniscient narrative context also eliminates secret and narrative leaks. A bounded narrative agent cannot accidentally tell a participant something that it never knew.
  - The risk and danger of a popular publication polluting source model training data is a known, accepted, and largely unmitigable issue short of maintaining an internal model.
  - **Support for the underlying memorization risk:** Chang et al. (2023); Carlini et al. (2021).
- Human authors therefore do not need to enumerate every possible reaction of every Actor to every possible future state.
- Instead, they author the world, the Actors, their histories, relationships, motivations, Knowledge, constraints, and goals from which reactions can be produced.
- The resulting possibility space is combinatorial rather than explicitly branched.
- A deeply authored narrative world can therefore support an effectively unbounded number of emergent narrative trajectories without requiring an equally unbounded quantity of pre-authored branches.
- The central architectural problem becomes ensuring that each independent agent receives **enough of its own context to reason faithfully about the world, but never information it should not possess**.
- This requires a strict distinction between:
  - the complete informational state of the world;
  - the persistent informational state available to a particular agent;
  - the temporary subset of that state assembled for a particular cognitive operation.
- These narrative agents are generally intended to be attached to Actors to create sophisticated, high fidelity Cognitive Actors.
- There are however some stray edge use cases for these agents such as a passive observational Narrator.
- The remainder of this paper will assume that Cognitive Actors are given to be driven by narrative agents and will serve as the principal vehicle for the concepts discussed in this sub-section.
- **Support / precedent:** Park et al. (2023); Hu et al. (2024; revised 2026); Hogan & Brennen (2024).

### 12.2 The Persistent Cognitive Actor

- The Cognitive Actor is persistent even when no model invocation is active.
- The model invocation is therefore not the Actor itself, but a temporary cognitive process operating on behalf of that Actor.
- A Cognitive Actor's persistent state may include:
  - authored character and personality;
  - Knowledge;
  - Memories;
  - relationships;
  - goals and motivations;
  - Enclave memberships;
  - Rank;
  - physical and social circumstances;
  - prior actions and their consequences.
- This persistent state exists independently of any particular inference session.
- Cognitive activity can therefore stop and resume without requiring the Actor to be reconstructed from scratch.
- Different cognitive operations may use different probabilistic models or deterministic systems without changing the identity of the Actor they serve.
- An implementation may therefore:
  - change models over time;
  - use cheaper or local models for routine cognition;
  - reserve more capable models for difficult interpretation or decision-making;
  - suspend cognition while the Actor is inactive;
  - substitute deterministic behaviour where probabilistic reasoning provides little value.
- The Actor remains the same persistent entity because identity, Knowledge, Memory, relationships, and state are maintained outside the model invocation.
- **Support / precedent:** Park et al. (2023); Packer et al. (2023), *MemGPT*; Wu et al. (2025), *LongMemEval*.

### 12.3 The Actor's Subjective World

- The authoritative system may represent the complete informational state of the world, but a Cognitive Actor inhabits only a bounded portion of it.
- The Actor's subjective world is formed from the persistent information that Actor can legitimately know, remember, observe, or access.
- This may include:
  - acquired Facts;
  - Memories;
  - Enclave-derived Knowledge;
  - Rank-derived access;
  - accessible Loci;
  - relationships;
  - current location and circumstances;
  - current goals;
  - recent Events known to the Actor;
  - incomplete, outdated, distorted, or false Knowledge.
- This subjective state is persistent and exists whether or not the Actor is currently being cognitively simulated.
- The Actor's subjective world may therefore differ substantially from:
  - authoritative world state;
  - the subjective world of another Actor;
  - the information available to a Participant.
- Enclave therefore distinguishes three informational scopes:
  - the complete informational state of the world;
  - the persistent informational state available to a particular Actor;
  - the temporary subset of that state assembled for a particular cognitive operation.
- Epistemic boundaries determine what an Actor can know.
- Retrieval later determines what the Actor is presently attending to.
- A Cognitive Actor cannot reason from information that is outside its subjective world merely because that information would be narratively convenient.
- **Support / precedent:** Hogan & Brennen (2024), particularly differentiated player history objects and information asymmetry; Park et al. (2023); Hu et al. (2024; revised 2026).

### 12.4 Memory and Cognition

- Memory and Cognitive Actors are already foundational Enclave concepts.
- For Cognitive Actors, the Memory primitive necessarily requires a persistent subsystem capable of maintaining Actor-specific experience and state beyond individual inference sessions and making relevant Memory available to cognition.
- Enclave defines the semantic role of Memory, but it does not need to define the complete internal ontology of the system used to implement it.
- At the Enclave level, Memory must be able to preserve Actor-specific narrative history such as:
  - encounters;
  - conversations;
  - observations;
  - interpretations;
  - decisions;
  - successes and failures;
  - emotionally or motivationally relevant experiences;
  - relationships to Facts and Events;
  - prior plans and unresolved conflicts.
- Events occur in the shared world, but different Actors may form different Memories of those Events according to their authored and constructed context.
- Memory therefore provides continuity that cannot be supplied by shared Knowledge alone.
- New Memories become part of the Actor's persistent subjective state and may influence cognition long after the original Interaction has ended.
- The complete Memory history does not need to occupy active context continuously.
- A suitable Memory implementation must instead make relevant portions of that history available when later circumstances make them useful.
- Persistence and present salience are separate properties.
- A Memory may remain part of the Actor's history while becoming unlikely to enter routine cognition.
- Later circumstances may make that same Memory relevant again.
- Reduced salience does not imply that the Memory became:
  - false;
  - invalid;
  - deleted;
  - contradicted;
  - or necessarily forgotten.
- This permits Actor history to grow without forcing model context to grow proportionally while increasing the effectiveness of long-range recall.
- Enclave does not require a particular:
  - memory graph;
  - vector database;
  - retrieval algorithm;
  - salience mechanism;
  - consolidation process;
  - summarization hierarchy;
  - decay model;
  - reinforcement model.
- Those mechanisms belong to the implementation of the Memory/cognitive subsystem rather than to Enclave's foundational ontology.
- The architectural requirement is therefore not a particular memory technology, but a persistent Actor-specific Memory capability sufficient to preserve continuity across cognitive episodes as well as being able to support the Memory Classification pipeline described in §9.3 for Memory-to-Fact transformations.
- **Support / precedent:** Tulving (2002); Greenberg & Verfaellie (2010); Park et al. (2023); Wu et al. (2025), *LongMemEval*; Packer et al. (2023), *MemGPT*.

### 12.5 Context Construction

- A Cognitive Actor's complete subjective world will frequently be much larger than the context required, or economically practical, for a single cognitive operation.
- Context construction therefore creates a bounded working view from that persistent subjective state.
- It begins by determining what information is available to the Actor and what portions of that information are relevant to the current cognitive operation.
- Where the Actor's complete available subjective state fits economically within the available context, it may simply be supplied.
- Pruning becomes necessary only when legitimate Knowledge and Memory exceed practical cognitive or computational limits.
- This establishes a general principle:
  - **provide as much legitimate context as practical and remove information only when scale requires selection.**
- Context construction draws from two closely related persistent sources:
  - **Knowledge context**, constructed by Enclave from the informational state legitimately available to the Actor;
  - **Memory context**, contributed by the Actor's Memory system from its persistent experiential history.
- Enclave remains responsible for the Actor's epistemic boundary.
- Information unavailable to the Actor must never enter cognitive context regardless of how relevant a retrieval mechanism considers it.
- Within that boundary, candidate Knowledge should be selected through several complementary forms of relevance rather than a single global score.
- These may include:
  - involvement in the current Event or Interaction;
  - causal relationships to the current circumstances;
  - shared Actors, Participants, or referents;
  - Enclave membership and Rank;
  - accessible or relevant Loci;
  - provenance and source relationships;
  - goals, plans, and unresolved state;
  - temporal relevance;
  - Actor activity;
  - semantic similarity;
  - active exploratory retrieval where stronger structural routes are insufficient.
- Memory systems may perform comparable selection over experiential history, using the current Enclave context as a primary relevance signal.
- Structural and semantic selection serve different purposes.
- Strong structural relationships can justify inclusion even where semantic similarity is weak, while semantic or exploratory retrieval can expose relevant information not connected through obvious authored relationships.
- Temporal interpretation is particularly important.
- Context construction should distinguish **source chronology** from **content-valid time**: when an Actor learned something is not necessarily when that information is true.
- Knowledge may describe historical, current, future, superseded, bounded, or temporally unresolved states.
- Consequently, information should not become irrelevant merely because it is old, nor become relevant merely because it is recent.
- Current circumstances, represented chronology, activity, and content-valid time provide more useful signals.
- Information may also vary in salience without changing in validity.
- Frequently used, newly relevant, causally active, or strongly connected information may be more likely to enter routine context, while inactive information may recede without being deleted, invalidated, or forgotten.
- The initial working context also need not anticipate every piece of information later reasoning may require.
- Cognition may expose a missing causal relationship, prior Event, relevant Actor, temporal question, or body of Knowledge or Memory that requires further examination.
- Context can then expand toward that information while remaining inside the Actor's epistemic boundary.
- This produces a progressive context process:
  - construct the broadest practical initial view;
  - narrow it only when scale requires;
  - reason from that view;
  - retrieve additional Knowledge or Memory when reasoning establishes a need for it.
- Deterministic systems can perform access enforcement, structural routing, temporal interpretation, and other well-defined selection operations, reserving probabilistic cognition for semantic judgement.
- Exclusion from a particular context therefore means only that information is not presently receiving cognitive attention.
- It does not remove that information from the Actor's subjective world.
- Context is consequently a **temporary field of attention over a much larger persistent subjective state**.
- **Support:** Liu et al. (2024), *Lost in the Middle*; Bai et al. (2024), *LongBench*; Hsieh et al. (2024), *RULER*; Wu et al. (2025), *LongMemEval*; Park et al. (2023); Packer et al. (2023), *MemGPT*.

### 12.6 The Cognitive Cycle

- Cognitive Actors require a mechanism connecting persistent subjective state to temporary cognition and then back to persistent state.
- A representative cognitive cycle may be:
  1. an Event, Interaction, schedule, internal goal, or other condition triggers cognition;
  2. the relevant Cognitive Actor is identified;
  3. Enclave establishes the Actor's current informational boundary and constructs an initial Knowledge context;
  4. the Actor's Memory system contributes relevant experiential context;
  5. those sources are composed into a bounded working context;
  6. the narrative agent interprets the current circumstances and reasons from the Actor's identity, goals, Knowledge, Memories, and constraints;
  7. additional Knowledge or Memory may be retrieved where reasoning establishes a need for it;
  8. the Actor selects or proposes an action;
  9. dialogue, communication, or other behaviour is expressed where required;
  10. the attempted action is submitted to authoritative systems for resolution;
  11. resulting Events, state changes, and information exposure are returned to the world and affected Actors;
  12. relevant experience is persisted into Memory and may subsequently enter the Memory Classification pipeline.
- Different implementations may combine, divide, omit, or deterministically resolve individual stages.
- Not every cognitive operation requires probabilistic inference.
- Not every Event requires every affected Actor to reason immediately.
- The critical authority boundary remains unchanged:
  - the Cognitive Actor determines what it attempts;
  - the authoritative system determines what actually happens.
- Cognition therefore remains bounded by persistent state on both sides:
  - it begins from an Actor's existing subjective world;
  - and its consequences return to persistent world state, Knowledge, and Memory.
- **Support / architectural precedent:** Park et al. (2023); Hogan & Brennen (2024); Gao et al. (2023), *PAL*; Kambhampati et al. (2024), *LLM-Modulo*.

### 12.7 Divided Cognitive Responsibility

- Actor cognition does not require one monolithic probabilistic process.
- The architecture separates three broad responsibilities:
  - **Enclave** maintains authoritative world state, Actor-accessible Knowledge, epistemic boundaries, Knowledge-context construction, and Event resolution;
  - **the Memory system** maintains persistent experiential state and contributes relevant Memory context;
  - **the narrative agent** performs interpretation, reasoning, planning, communication, and action selection from the context supplied to it.
- Each of these responsibilities may itself combine deterministic and probabilistic mechanisms.
- Deterministic systems are generally preferable where the required operation can be represented reliably, including:
  - access enforcement;
  - structural traversal;
  - temporal interpretation;
  - retrieval routing;
  - state maintenance;
  - validation;
  - persistence.
- Probabilistic systems are most useful where the problem requires:
  - interpretation;
  - ambiguity handling;
  - semantic judgement;
  - contextual reasoning;
  - planning under incomplete information;
  - generation of novel responses.
- This division allows expensive inference to be reserved for operations that benefit from it.
- **Support / architectural precedent:** Gao et al. (2023), *PAL*; Kambhampati et al. (2024), *LLM-Modulo*; Marra et al. (2024); Wu et al. (2025), *LongMemEval*.

### 12.8 Reliquary and the Development of the Enclave Architecture

- Enclave's **theory** does not require Reliquary.
- The Enclave ontology and its architectural principles can be implemented using other persistent Memory and cognitive architectures.
- The development of Enclave's applied architecture, however, was substantially informed by work on Reliquary.
- Reliquary began as a separate effort to solve persistent cognition: how an intelligent system could retain a growing experiential history outside model context, retrieve the portions relevant to present activity, preserve provenance and temporal meaning, and maintain continuity across otherwise disposable inference sessions.
- Work on those problems exposed a number of architectural distinctions that became directly important to Enclave.
- These include:
  - persistent state as distinct from temporary cognitive context;
  - information availability as distinct from present attention;
  - semantic and structural relevance as complementary retrieval mechanisms;
  - provenance as part of persistent meaning rather than incidental metadata;
  - source chronology as distinct from content-valid time;
  - salience as distinct from truth or persistence;
  - progressive context construction rather than dependence on one-shot retrieval;
  - deterministic routing and constraint enforcement around probabilistic semantic judgement;
  - the ability for large bodies of inactive information to remain recoverable without remaining continuously present.
- Reliquary also provided practical experience with the consequences of these distinctions at scale.
- Its development required mechanisms for:
  - provenance-preserving Memory;
  - semantic and structural retrieval;
  - temporal interpretation;
  - changing salience without deletion;
  - higher-order organization and synthesis;
  - bounded candidate selection;
  - progressive context construction over persistent state.
- Enclave inverts the perspective of several lessons produced by that work, extending principles developed for internal agent architecture outward to the informational and cognitive organization of an authored narrative world.
- In particular, the theory of Actor context construction developed in this section follows the same underlying principle: **preserve the larger persistent state, determine what is legitimately available, select what deserves present attention, and expand that attention when cognition establishes a need for additional information.**
- Reliquary is therefore not merely an example of an architecture that happens to satisfy Enclave's requirements. It is one of the principal practical systems from whose treatment of persistent cognition, Memory, salience, temporal context, retrieval, and bounded context construction the applied Enclave architecture was derived.
- This lineage does not make Reliquary a theoretical dependency, nor does it make Reliquary's internal ontology part of Enclave's own. It means that mechanisms developed through practical work on persistent cognition were abstracted, inverted where appropriate, and incorporated into the broader Enclave architecture.
- Consequently, while another system may satisfy the same theoretical requirements, **Reliquary or a highly analogous persistent Memory and context architecture is strongly recommended for an applied Enclave implementation.**

Section 12 establishes how a Cognitive Actor maintains a bounded, persistent subjective existence while reasoning through temporary cognitive contexts. The remaining question is how the actions produced by that cognition alter the shared world and become persistent causes of later Events. That problem is addressed in §13.

---

## 13. Persistent Cause and Effect

> Section 12 established how a Cognitive Actor can maintain a bounded, persistent subjective existence while reasoning through temporary cognitive contexts. This section describes the other half of that architecture: how actions produced by that cognition enter the shared world, participate in causal Interactions, and create persistent circumstances from which later narrative develops.

### 13.1 From Cognition to Causality

- A Cognitive Actor may interpret its circumstances, reason from its Knowledge and Memory, and determine what it intends to do.
- At the end of that cognitive process, however, the world has not necessarily changed.
- The output of cognition is an **attempted action**.
- An attempted action represents what the Actor is trying to cause rather than an authoritative statement of what occurred.
- This is the practical expression of the authority boundary established in §8:
  - the Actor determines what it attempts;
  - the authoritative system determines what actually happens.
- When an attempted action enters the shared world, it becomes input to an **Interaction** between the Actor and the circumstances upon which it is acting.
- As established in §10.2, an Interaction is an **Event characterized by causal process**.
- Interaction therefore provides the bridge between subjective Actor intent and authoritative cause and effect.

  `bounded cognition → attempted action → Interaction → persistent consequence`

### 13.2 The Existing Sandbox

- Section 6 established that sandbox and simulation-heavy games already provide sophisticated persistent systemic and physical cause and effect.
- Enclave does not attempt to replace that machinery.
- Its principal concern is **persistent narrative cause and effect**: allowing the informational, social, institutional, and authored meaning of systemic consequences to persist and influence later Actors and developments.
- Existing sandbox causality can therefore serve as part of the substrate upon which Enclave operates.

### 13.3 Open-ended Action Space

- Existing sandbox systems may support enormous combinatorial possibility while still exposing a finite vocabulary of explicitly represented actions and interactions.
- The same probabilistic capabilities used by Enclave for narrative interpretation suggest a complementary possibility outside Enclave's principal scope: allowing Actors or Participants to express physical intent semantically rather than selecting only from that predefined vocabulary.
- For example:
  - "Jam the chair under the door handle."
  - "Use the curtain as an improvised rope."
  - "Knock the shelf over to block the hallway."
- A probabilistic interpreter could relate that intent to:
  - represented objects;
  - available affordances;
  - Actor capabilities;
  - conventional mechanics;
  - combinations of operations already available to the simulation.
- The result would not itself determine what happens.
- It would translate open-ended intent into a form capable of participating in an authoritative Interaction.
- This could provide an **effectively open-ended action vocabulary over a finite simulated substrate**.
- The underlying simulation would remain bounded by what it can actually represent and resolve, with greater systemic fidelity supporting a correspondingly broader range of meaningful actions.
- This is **not the principal purpose of Enclave**.
- Enclave is primarily concerned with **narrative sandboxing**: interpreting and preserving the narrative consequences produced by Interactions throughout a continuing world.
- Open-ended physical action is instead another possibility created by the broader division between probabilistic interpretation and authoritative computational resolution.

### 13.4 Action and Consequence

- Once an attempted action enters the world, the relevant question is no longer simply what the Actor intended, but **what Interaction actually occurs**.
- An Interaction incorporates the attempted action into the causal circumstances against which it must be resolved.
- Those circumstances may include:
  - Actor capabilities;
  - physical conditions;
  - resources;
  - location;
  - timing;
  - relationships;
  - permissions;
  - actions by other Actors;
  - existing Events;
  - authored constraints;
  - conventional simulation.
- The resulting causal process may differ substantially from the Actor's intention.
- An attempt may:
  - succeed;
  - partially succeed;
  - fail;
  - become impossible;
  - produce unintended effects;
  - provoke another Actor;
  - expose new information;
  - trigger some other causal process.
- Failure does not mean that nothing happened.
- A failed attempt itself generally constitutes a meaningful Interaction and therefore an Event.
- Probabilistic systems may assist in:
  - interpreting intent;
  - identifying relevant circumstances;
  - proposing causal relationships;
  - adjudicating ambiguous situations where deterministic machinery is insufficient.
- The exact resolution mechanism is implementation-dependent.
- The authority relationship is not.
- The Actor supplies action; the world determines the resulting causal process.

### 13.5 Making it Real

- Because an Interaction is an Event characterized by causal process, an authoritatively resolved Interaction is already part of the authoritative history of the world.
- It does not need to subsequently be converted into a separate Event simply to become real.
- The Interaction records that a causal process occurred and may establish consequences including changes to:
  - physical state;
  - Actor state;
  - relationships;
  - resources;
  - Loci;
  - Knowledge availability;
  - institutional circumstances;
  - authored conditions;
  - future Event eligibility.
- An Interaction may also cause additional Events whose significance extends beyond the original causal process.
- Facts spawned from Events enter the system as canonical as described earlier.
- Informational exposure remains governed by the Knowledge-distribution mechanisms described in §11.
- Most importantly, authoritative Events do more than preserve what happened.
- **They create new circumstances capable of becoming causes.**
- A physical consequence may produce an informational consequence.
- Information may alter Actor behaviour.
- Changed behaviour may produce another Interaction.
- Institutional response may alter circumstances for distant Actors or later authored developments.
- For example:

  `bridge destroyed`
  `→ route unavailable`
  `→ shipment does not arrive`
  `→ absence is noticed`
  `→ information propagates`
  `→ plans change`
  `→ later Actors encounter different circumstances`

- No author needs to have written that complete causal chain beforehand.
- Each stage only needs to be representable by the appropriate layer of the world.
- This is the difference between merely persisting state and persisting **narrative consequence**.

### 13.6 Conditional Developments

- Earlier sections established that authors may define intended developments without requiring a fixed sequence.
- Persistent cause and effect supplies the runtime mechanism that makes those developments genuinely conditional.
- When an authored development becomes relevant, it is evaluated against the causal history and current state that actually exist.
- Prior Interactions and Events may therefore make the development:
  - possible;
  - impossible;
  - altered;
  - differently understood;
  - consequential in an entirely different way.
- Authored intention remains present, but persistent causal history determines the circumstances under which it can be realized.
- The architecture therefore preserves authorial planning without requiring the world to return to an intended trajectory after divergence.
- Conditional developments introduce an additional dimension of narrative sandboxing: **temporal cadence**.
- The world can continue progressing independently of Participant intervention.
- Actor plans, deadlines, institutional activity, scheduled developments, and other causal processes may continue unless circumstances alter or prevent them.
- Participant intervention can therefore interrupt, redirect, accelerate, or prevent an existing causal process rather than serving as the trigger that causes the world to begin moving.
- Participant inaction can itself be causally meaningful because it may allow an existing process to continue toward its consequence.
- The narrative world therefore progresses around Participants rather than waiting for them.

### 13.7 Branching as Causality

- The branching problem described in §4 does not disappear.
- What changes is how divergence is represented.
- Enclave does not require every narrative divergence to correspond to an explicitly authored branch.
- Instead, divergence accumulates through causal history:
  - different Interactions produce different Events and state;
  - different state produces different Actor perspectives;
  - different perspectives produce different decisions;
  - different decisions produce different Interactions;
  - those Interactions further change the world.
- The cumulative result is narrative branching produced by persistent causal state rather than exhaustive path enumeration.

  `different causal history`
  `→ different world`
  `→ different Actor perspective`
  `→ different action`
  `→ different Interaction`
  `→ further divergence`

- Branching becomes an emergent property of persistent causal history.
- Enclave therefore relocates much of the authorial burden from pre-authoring paths and their reactions into constructing the persistent narrative substrate from which those paths can emerge.
- That authorial substrate includes Actors, Knowledge, relationships, institutions, motivations, constraints, resources, intended developments, and other authored state.
- Runtime causal Interaction, Actor cognition, and persistent world state determine how those authored elements combine into the realized narrative.
- The authorial burden is therefore not eliminated; it is redirected from predicting and enumerating sequences toward authoring the people, pressures, circumstances, causes, and possibilities capable of producing meaningful sequences.

### 13.8 Event-Driven Persistence

- Persistent cause and effect does not require the entire world to be continuously reevaluated.
- Interactions and other Events identify meaningful changes in authoritative state and therefore provide natural triggers for further processing.
- Those changes can trigger reevaluation only where they may matter, including:
  - affected Actors;
  - relevant Cognitive Actors;
  - Knowledge availability;
  - Loci;
  - resources;
  - authored conditions;
  - scheduled developments;
  - future Event eligibility.
- Unrelated portions of the world need not respond.
- Narrative consequence can therefore propagate according to causal relevance rather than through continuous universal simulation.
- This event-driven structure provides the conceptual bridge into the computational scaling questions addressed in §14.

Together with the material established in §12:

`persistent world`
`→ bounded Actor perspective`
`→ cognition`
`→ attempted action`
`→ Interaction / authoritative causal resolution`
`→ persistent Event and consequence`
`→ changed world`
`→ new bounded Actor perspectives`

The narrative therefore does not advance because the system selects the next authored branch. It advances because **Actors create Interactions, and the world preserves their consequences as causes of what can happen next.**

---
## 14. Worked Examples

> **Working section.** The preceding sections describe Enclave abstractly; the following examples demonstrate the architecture operating on existing authored narratives. Each begins with a published adventure, treats its expected sequence as an authored trajectory, and then follows a realized sequence produced when Participant action changes the circumstances from which later Actors act.

### 14.1 From Authored Trajectory to Realized Narrative

- Each example begins with a conventional published adventure containing:
  - an established world state;
  - characters with motivations and information;
  - an expected sequence of developments;
  - an intended resolution.
- That material can be represented without preserving its expected sequence as mandatory.
- The published adventure becomes the **authored trajectory**: what is expected to occur if circumstances develop approximately as anticipated.
- Participant intervention can instead alter the circumstances from which later developments arise.
- The important comparison is therefore not between an authored adventure and generated narrative.
- It is between:
  - the narrative trajectory anticipated by the original authored structure; and
  - a different realized trajectory produced from substantially the same authored material.

### 14.2 *A Wild Sheep Chase*: The Authored Trajectory

- **Primary source:** Winghorn Press, *A Wild Sheep Chase*, a free single-session D&D 5E adventure for 4th–5th-level parties: https://winghornpress.com/adventures/a-wild-sheep-chase/
- The source adventure supplies the authored characters, relationships, conflict, locations, objects, and expected scenario progression used in §§14.2–14.6; the alternate causal sequence in §14.5 is an Enclave demonstration constructed from that authored material.
- *A Wild Sheep Chase* begins when Finethir Shinebright, a wizard transformed into a sheep, seeks assistance from the Participants.
- Shinebright identifies his former apprentice, Ahmed Noke, as responsible for his transformation and asks the Participants to help recover the Wand of True Polymorph.
- Noke's ally Guz and a group of transformed creatures attempt to recover Shinebright.
- The expected progression carries the Participants from:
  - their encounter with Shinebright;
  - through conflict with Guz;
  - to Shinebright's explanation of the situation;
  - to Noke's home;
  - to confrontation with Noke;
  - and ultimately to resolution of Shinebright's transformation and control of the wand.
- The adventure nevertheless contains more narrative information than this sequence alone expresses.
- Shinebright and Noke have a shared history.
- Shinebright's treatment of Noke contributed to their conflict.
- Noke possesses motives that cannot be reduced to simply opposing the Participants.
- Guz is personally loyal to Noke.
- The conflict therefore already contains multiple Actors with different histories, loyalties, information, and interpretations of the same circumstances.

### 14.3 *A Wild Sheep Chase* as Persistent Narrative State

- Under Enclave, the adventure is represented primarily through the circumstances that produce its expected trajectory rather than through the trajectory itself.
- Shinebright exists as a Cognitive Actor with:
  - his history with Noke;
  - his knowledge of the wand;
  - his memory of his transformation;
  - his objectives;
  - his interpretation of Noke;
  - his current physical condition.
- Noke independently possesses:
  - his history with Shinebright;
  - his own interpretation of that relationship;
  - knowledge of the transformation;
  - control of the wand;
  - relationships with Guz and his transformed servants;
  - his own motives and intended actions.
- Guz possesses his own bounded perspective:
  - loyalty to Noke;
  - knowledge obtained through that relationship;
  - whatever he has personally observed;
  - immediate objectives concerning Shinebright and the Participants.
- The transformed guards, wand, locations, and physical circumstances remain part of authoritative world state without necessarily requiring independent cognition.
- The expected confrontation with Noke remains possible because the conditions that originally produced it still exist.
- It is no longer necessary for the system to require that confrontation merely because it is the next authored scene.

### 14.4 A Different Interaction Produces a Different Trajectory

- The initial encounter with Guz provides an immediate point at which Participant behaviour can depart from the expected trajectory.
- Participants may communicate with Guz, capture him, allow him to surrender, bargain with him, or otherwise create an Interaction that is not exhausted by defeating him.
- Guz's response is constrained by:
  - his loyalty to Noke;
  - what he knows;
  - what has happened during the encounter;
  - what the Participants communicate;
  - his own circumstances and objectives.
- Information obtained from Guz can change the Participants' understanding of Shinebright before they ever meet Noke.
- The Participants may consequently approach Noke without accepting Shinebright's account as complete.
- Noke encounters Participants whose behaviour and knowledge differ from those anticipated by the original trajectory.
- His response can depend upon:
  - what happened to Guz;
  - what information has reached him;
  - what the Participants know;
  - what they demand or offer;
  - whether Shinebright is present;
  - whether Noke believes cooperation, deception, escape, or violence best serves his objectives.
- The original confrontation remains possible.
- Other outcomes also become possible from the same authored material:
  - negotiation over Shinebright's restoration;
  - an agreement concerning the wand;
  - assistance to Noke;
  - rejection of both wizards;
  - escape;
  - betrayal;
  - or a confrontation arising for reasons substantially different from those anticipated by the published sequence.
- No new branch needs to have been authored for each of these possibilities.
- The divergence arises because the existing Actors are allowed to respond to changed circumstances while their actions and consequences persist.

### 14.5 Minor Divergence Walkthrough: The Same Adventure in a Different State

- This example deliberately preserves the broad authored trajectory.
- The divergence consists of small causal changes that remain meaningful but would rarely justify individually authored branches in a conventional branching narrative.

**Step 1 — The adventure begins normally.**
- Shinebright reaches the Participants, communicates his account, and asks for help.
- The Participants agree to become involved.
- **Architectural process:**
  - Shinebright's communication occurs as an Interaction between a Cognitive Actor and the Participants.
  - The persistent system records what was communicated and what the Participants did in response.
  - Relevant Actor Memories and informational relationships are updated.
  - No authoritative state or authored condition has yet changed enough to redirect the expected trajectory.
  - The next relevant Actors therefore continue operating from substantially the state anticipated by the adventure.
- **Resulting divergence:** None yet. The authored trajectory remains the natural continuation of the current state.

**Step 2 — The encounter with Guz ends differently.**
- Combat begins as expected, but once Guz is injured the Participants stop pressing the attack.
- They tell him they are willing to hear Noke's side and allow him to withdraw rather than killing or capturing him.
- **Architectural process:**
  - The Participants' attempted actions and communication enter an Interaction with Guz.
  - Combat resolution remains authoritative: Guz's injuries, position, and ability to withdraw are determined by the game world's normal rules.
  - The Interaction persists as an Event describing what actually occurred.
  - Guz receives Memories of being spared and of the Participants' stated willingness to hear Noke.
  - The Participants likewise retain the encounter and any information Guz communicated.
  - Any novel claims become non-canonical Facts associated with their sources rather than silently becoming canonical truth.
  - Guz's relationship and current assessment of the Participants are now different inputs to later cognition.
- **Resulting divergence:** Guz survives, carries new information, and no longer necessarily treats the Participants as straightforward enemies. This is a small change, but it alters the state entering later scenes.

**Step 3 — Guz returns to Noke.**
- Guz reports that the Participants are travelling with Shinebright but deliberately spared him and asked to hear Noke's account.
- **Architectural process:**
  - Guz's report is a new Interaction.
  - Noke gains a Memory of Guz's report and access to the information contained in it.
  - The report remains attributed to Guz; Noke can believe, doubt, or reinterpret it rather than receiving it as omniscient world truth.
  - Noke's next cognitive cycle is constructed from his existing Knowledge and Memories plus this new information.
  - His goals and relationship to Shinebright have not changed, but his model of the approaching Participants has.
- **Resulting divergence:** The expected meeting with Noke is still likely to occur, but Noke is now preparing for people who may be negotiable rather than assuming that Shinebright has simply recruited hostile proxies.

**Step 4 — Noke changes his immediate plan.**
- Noke tells Guz not to initiate another attack unless the Participants become hostile and keeps the wand close while preparing to speak with them.
- **Architectural process:**
  - Noke's cognition produces an attempted action based on his updated bounded context.
  - The world resolves that action deterministically where possible: Guz receives the instruction, defensive preparations change, and Noke's immediate behaviour changes.
  - Those changes become persistent state.
  - Any future retrieval or context construction for Guz or Noke now includes the changed instruction and preparation rather than the original expected posture.
  - The system has not selected a special "negotiation branch"; it has simply preserved the consequences of Noke acting on new information.
- **Resulting divergence:** The same location and same central conflict remain ahead, but the encounter has different initial conditions.

**Step 5 — Shinebright learns that the Participants spoke with Guz.**
- During the journey, the Participants tell Shinebright they intend to hear Noke's account before acting.
- Shinebright becomes defensive and presses his own interpretation of the apprenticeship more aggressively.
- **Architectural process:**
  - The Participants' statement becomes an Interaction with Shinebright.
  - Shinebright gains a Memory that the Participants are questioning his account.
  - His current context now combines that Memory with his existing self-perception, history with Noke, objectives, and fear of losing the Participants' support.
  - His cognitive response is generated from that bounded perspective.
  - What he says becomes new persistent information available to the Participants, but does not alter canonical truth merely because he asserts it.
- **Resulting divergence:** The journey itself remains the same, but the Participants arrive with a more complicated informational picture and Shinebright arrives knowing his credibility is contested.

**Step 6 — The Participants arrive at Noke's home.**
- The broad published trajectory has not been abandoned.
- Noke does not immediately treat them as indistinguishable from Shinebright and allows a tense conversation before violence begins.
- **Architectural process:**
  - Context is constructed separately for Noke, Guz, and Shinebright from their different Memories, Knowledge, relationships, and current circumstances.
  - Each Cognitive Actor therefore enters the same physical Interaction with a different subjective world.
  - Dialogue and attempted actions are generated from those bounded contexts.
  - The authoritative system continues to own physical state, possession of the wand, positioning, injuries, and any rule-governed outcomes.
  - New claims, concessions, threats, or promises are persisted as they occur.
- **Resulting divergence:** The authored destination is preserved, but the scene is not semantically identical to the published version because all three major Actors enter it with altered histories.

**Step 7 — The central problem receives a slightly different resolution.**
- The Participants still seek Shinebright's restoration and still have to resolve control of the wand.
- After hearing both sides, they persuade Noke to restore Shinebright while refusing to immediately return the wand to either wizard.
- **Architectural process:**
  - Persuasion, agreement, restoration, and transfer or retention of the wand occur through successive Interactions.
  - Rule-governed outcomes are resolved authoritatively.
  - The restoration becomes a canonical Event and changes physical world state.
  - The agreement and treatment of each Actor become persistent Memories.
  - Ownership or custody of the wand is updated as canonical state.
  - Later contexts for Shinebright, Noke, Guz, and the Participants are therefore built from a world in which the same central crisis was resolved through a different causal history.
- **Resulting divergence:** The adventure reaches substantially the same structural endpoint, but Guz survives, Noke has been heard rather than simply defeated, Shinebright's credibility has changed, and custody of the wand may differ. These are meaningful consequences that a conventional branching design would often collapse rather than enumerate.

- None of these changes is individually dramatic enough to justify the cost of a traditional authored branch.
- Collectively, however, they make the Participants' actions meaningfully consequential.
- The realized narrative feels responsive because the architecture preserves small causal differences instead of collapsing them back into an identical state.

### 14.6 Persistent Consequence in the Fantasy Example

- The divergent Interaction does more than change a conversation.
- Guz remembers his treatment by the Participants.
- Participants acquire information they did not possess in the original trajectory.
- Shinebright may learn that his account has been questioned.
- Noke may learn that Guz was captured, harmed, released, persuaded, or assisted.
- Subsequent Actor decisions therefore occur from different bounded perspectives.
- Actions taken during those decisions create further Events and alter canonical world state.
- The narrative continues from those consequences rather than returning automatically to the original sequence.
- The authored material remains central throughout:
  - the same characters;
  - the same relationships;
  - the same history;
  - the same wand;
  - the same transformation;
  - the same underlying conflict.
- What changes is the realized causal path through that material.

### 14.7 *Signals*: The Authored Trajectory

- **Primary source:** Modiphius Entertainment, *Star Trek Adventures: Quickstart Guide*, containing the self-contained adventure *Signals* and six pre-generated player characters: https://modiphius.net/collections/star-trek-adventures/products/star-trek-adventures-quickstart-guide — **the Section 15 computational reference intentionally models only one Participant controlling one Participant Actor.**
- The source adventure supplies the mission, Actors, factions, settlement, Romulan opposition, alien artifact, locations, and expected scenario progression used in §§14.7–14.10; the major-divergence sequence in §14.10 is an Enclave demonstration constructed from that authored material.
- *Signals*, from the *Star Trek Adventures* Quickstart, provides the same problem in a substantially different narrative environment.
- The Participants investigate the disappearance of the runabout *Susquehanna* and an unusual signal originating near Seku VI.
- The expected mission progression leads through:
  - arrival and investigation;
  - transport to the surface;
  - conflict with Romulan forces;
  - discovery of evidence concerning the missing Starfleet mission and a crashed Romulan vessel;
  - contact with a mining settlement;
  - investigation of an alien obelisk;
  - renewed Romulan interference;
  - and final resolution around the artifact.
- The expected sequence is driven by an already-authored set of circumstances:
  - Starfleet objectives;
  - Romulan objectives;
  - casualties and survivors;
  - the settlement;
  - the alien structure;
  - limited information about what has occurred;
  - competing interests surrounding the signal and artifact.
- These circumstances can produce the published trajectory without requiring that trajectory to remain mandatory.

### 14.8 *Signals* as Persistent Narrative State

- Under Enclave, Starfleet, Romulan, and settlement perspectives remain distinct.
- Individual Cognitive Actors know only what their histories, affiliations, observations, communications, and Memories make available to them.
- Institutional relationships provide additional structure:
  - Starfleet personnel operate within Starfleet knowledge and objectives;
  - Romulan Actors operate within their own military and political context;
  - settlement Actors possess local knowledge and interests unavailable to either outside group.
- The missing runabout, casualties, crashed vessel, obelisk, communications conditions, and physical environment remain authoritative state.
- Hostility between Starfleet and Romulan forces is therefore a consequence of history, institutional relationships, current objectives, and local circumstances.
- It does not need to exist as a rule that every encounter between the two groups must become combat.

### 14.9 Contact with the Romulans Changes the Mission

- Participants may choose to communicate with surviving Romulans rather than treating them exclusively as combatants.
- They may:
  - capture and question a survivor;
  - provide medical assistance;
  - negotiate access;
  - exchange information;
  - deceive them;
  - establish a temporary truce;
  - or cooperate against a problem perceived as more important than their existing hostility.
- Any such Interaction changes the informational state of the adventure.
- A Romulan Actor may learn things that the published trajectory assumes the Romulans do not yet know.
- Starfleet Participants may acquire information earlier or through a different source.
- Information may subsequently reach other Romulans, Starfleet personnel, or the settlement.
- Those Actors then make decisions from circumstances different from those anticipated by the original mission sequence.
- The expected confrontation at the obelisk can consequently be:
  - preserved;
  - prevented;
  - accelerated;
  - delayed;
  - transformed into a standoff;
  - transformed into negotiation;
  - or replaced by temporary cooperation.
- As in the fantasy example, the system has not generated an unrelated replacement narrative.
- The same authored conflict, artifact, characters, institutions, locations, and objectives produce a different realized path because earlier Events changed the state from which later Actors acted.

### 14.10 Major Divergence Walkthrough: Leaving the Authored Trajectory

- This example deliberately does the opposite of the fantasy example.
- A relatively early Participant decision changes the conditions supporting the published sequence so substantially that the expected later scenes cease to be the natural continuation of the world.

**Step 1 — The first Romulan encounter begins as expected.**
- Starfleet Participants encounter hostile Romulan personnel on Seku VI.
- During the confrontation, one Romulan is badly injured and isolated from the rest.
- **Architectural process:**
  - Participant actions and Romulan actions are interpreted as attempted actions within the current Interaction.
  - Combat and physical consequences are resolved by the authoritative game systems.
  - Injuries, positions, deaths, escape routes, and possession remain canonical state rather than model-generated assumptions.
  - Surviving Cognitive Actors receive Memories of what they directly observed.
  - Because the state still matches the assumptions of the authored trajectory, no later authored development has yet become implausible.
- **Resulting divergence:** None of consequence yet. The expected sequence remains causally supported.

**Step 2 — The Participants rescue the injured Romulan.**
- They provide medical assistance and take the survivor prisoner rather than allowing the encounter to end with the Romulans simply removed as opposition.
- **Architectural process:**
  - The rescue is resolved against authoritative physical state: whether the Romulan survives, can be moved, and can communicate is determined by the game rules and current circumstances.
  - The rescue persists as an Event.
  - The Romulan gains Memories of being saved by Starfleet personnel.
  - The Participants gain access to a Cognitive Actor who carries Romulan Knowledge unavailable through their existing information channels.
  - Relationship state and future context for the prisoner now include direct evidence that conflicts with a simplistic expectation of inevitable hostility.
- **Resulting divergence:** A new informational and social connection now exists between two sides that the published trajectory largely keeps separated.

**Step 3 — Interrogation becomes an exchange of information.**
- The Participants establish that the Romulan force has also suffered losses and is pursuing its own objectives concerning the signal and the situation on the planet.
- They reveal enough of their own investigation to establish that neither side fully understands what has happened.
- **Architectural process:**
  - Each statement is stored as attributed information rather than canonicalized automatically.
  - Novel claims become non-canonical Facts associated with their speaker, provenance, and relevant Domains or Enclaves.
  - The prisoner evaluates Starfleet claims from Romulan Knowledge, personal observation, institutional assumptions, and the Memory of having been rescued.
  - The Participants likewise evaluate the prisoner's statements against their own Knowledge.
  - Subsequent context construction on both sides can retrieve the new information without erasing uncertainty or disagreement.
- **Resulting divergence:** Both sides now possess information earlier, from different sources, and with different credibility than the authored sequence assumes.

**Step 4 — The prisoner becomes a communication path to the remaining Romulans.**
- The Participants use the prisoner to propose a temporary ceasefire for the investigation.
- The remaining Romulan leadership accepts a narrowly bounded truce because its current circumstances make cooperation preferable to immediately renewed combat.
- **Architectural process:**
  - The proposal propagates through an actual communication path rather than being globally available.
  - The receiving Romulan leader gains only the information transmitted through that path plus whatever that Actor already knows.
  - A fresh cognitive cycle evaluates the proposal against Romulan goals, casualties, resources, distrust of Starfleet, and the prisoner's report.
  - Acceptance becomes an attempted action by that Actor.
  - Once communicated and resolved, the ceasefire becomes persistent social and informational state affecting both sides.
  - Authored future developments whose causal assumptions included continued separation or immediate hostility are reevaluated against the new state.
- **Resulting divergence:** This is the decisive break. The later authored Romulan attack is not arbitrarily cancelled; the state that made that attack the natural next development no longer exists.

**Step 5 — Starfleet and Romulan Actors approach the settlement together.**
- The mining settlement now encounters a mixed delegation rather than a purely Starfleet party followed later by hostile Romulan activity.
- **Architectural process:**
  - Arrival creates new Interactions between the delegation and settlement Actors.
  - Ero Drallen's context is constructed from settlement Knowledge, current local conditions, observable Starfleet/Romulan cooperation, and whatever each side communicates.
  - Drallen has no access to private Memories or information that has not reached the settlement.
  - His cognition produces a response from that bounded state.
  - Any permissions, refusals, warnings, or new information then persist and propagate through the participants actually involved.
- **Resulting divergence:** A scene the published adventure did not anticipate can occur coherently because the Actor is responding to the present world, not selecting from a list of pre-authored encounter variants.

**Step 6 — Investigation of the obelisk occurs under a three-sided political relationship.**
- Starfleet, Romulan, and settlement Actors all possess different objectives and different information.
- The central tension becomes whether the temporary coalition survives disagreement over access, interpretation, risk, and control.
- **Architectural process:**
  - Each Cognitive Actor receives a different context derived from that Actor's Knowledge, Memories, institutional Enclaves, relationships, and current observations.
  - Their models may therefore recommend incompatible actions even though all are reasoning about the same canonical physical object and world state.
  - Attempted actions enter shared Interactions and are resolved by the authoritative systems.
  - Resulting Events create additional Memories and Facts and may alter institutional or interpersonal relationships.
  - The system continues to use the original authored artifact, motives, and institutional conflict; only their current configuration has changed.
- **Resulting divergence:** The narrative has departed substantially from the expected sequence while remaining anchored in the same authored material.

**Step 7 — The expected final assault never occurs.**
- Because the relevant Romulan Actors are already present under negotiated terms, there is no separate hostile force arriving to recreate the published climax.
- Instead, the crisis is resolved through the unstable cooperation surrounding the obelisk.
- **Architectural process:**
  - The system does not treat authored future events as mandatory timeline entries.
  - The prerequisites and causal conditions associated with the expected assault are checked against current state.
  - Continued truce, changed Actor locations, shared information, casualties, and current objectives make that event inapplicable in its authored form.
  - No replacement branch must be selected.
  - Cognition and causal resolution simply continue from the world that now exists until another Actor action or Event changes it again.
- **Resulting divergence:** The published climax disappears for causal reasons rather than because the system chose an alternate ending.

**Step 8 — A new resolution emerges from the changed state.**
- The Participants broker a limited information-sharing arrangement, ensure the injured Romulans can withdraw, and leave the settlement with all three groups holding different interpretations of what occurred.
- **Architectural process:**
  - The agreements, departures, custody or access arrangements, and physical outcomes are persisted as canonical Events and state.
  - Each Cognitive Actor retains only that Actor's own Memories and accessible Knowledge of the resolution.
  - Institutional Knowledge may subsequently propagate through Starfleet, Romulan, or settlement channels according to the same distribution mechanisms described earlier in the paper.
  - Future authored developments involving any of these Actors or institutions begin from this new state rather than from the original adventure's intended ending.
- **Resulting divergence:** The realized narrative is structurally different from the published adventure, yet it was produced by the same authored Actors, institutions, locations, conflict, and artifact.

- This is the point at which Enclave differs most sharply from classic branching.
- A conventional implementation would generally need an explicit alternate route for the truce, joint arrival, three-sided investigation, missing assault, and replacement resolution.
- Enclave instead treats each change as persistent state and allows later Actors and Events to respond to the world that actually resulted.

### 14.11 The Same Architecture Across Different Narrative Worlds

- The two adventures differ substantially in setting, genre, institutions, technology, tone, scope, and immediate conflict.
- Their realized divergence nevertheless follows the same basic causal structure:

  **authored circumstances**  
  → **bounded Actor perspectives**  
  → **Participant intervention**  
  → **Interaction**  
  → **authoritative resolution**  
  → **new Memories, Knowledge, and state**  
  → **changed Actor context**  
  → **new attempted action**  
  → **persistent Event and consequence**  
  → **divergent realized narrative**

- Neither example requires the original authored trajectory to be discarded.
- The trajectory remains the natural result of the original circumstances when Participants do not substantially alter them.
- Enclave instead allows the trajectory to cease being binding once those circumstances change.
- The author continues to supply the narrative substance.
- Participant action changes how that substance is encountered, combined, interpreted, and resolved.
- The result is not freedom from authored narrative.
- It is **authored narrative capable of surviving meaningful deviation from its anticipated path**.

---

## 15. Computational Architecture and Scale

> **Working section.** Begin with the bounded high-fidelity *Signals* reference, quantify Enclave storage and cognition, then scale the same architecture toward the theoretical full-world endpoint. Current calculations live in `docs/signals-section15-consolidated-computational-model-2026-10-08.md`.

### 15.1 High-Fidelity Reference Workload: *Signals*

- Use the major-divergence *Signals* walkthrough from §14.10.
- Assume approximately eight hours of **simulated in-game time**, not eight hours of wall-clock gameplay. Game-time dilation can compress or extend the corresponding real-time processing window; skipping or aggregating activity changes the assumed simulation fidelity.
- Simplified computational population:
  - **36 settlement Cognitive Actors**;
  - **5 surviving Romulan Cognitive Actors**;
  - **1 remote Starfleet Captain** while causally relevant;
  - **1 surviving *Susquehanna* distress-source Actor** while causally relevant;
  - **43 model-driven Cognitive Actors total**;
  - **1 human Participant controlling 1 Participant Actor**;
  - **44 living Actors total** in the simplified reference.
- Participant Actor cognition originates outside Enclave:
  - **Participant cognition calls = 0**.
- A real party implementation may use hybrid party Actors that revert to model-driven cognition when not directly controlled; that case is outside this reference calculation.
- High fidelity inside the causal scope means:
  - no crowd/squad aggregation;
  - persistent individual Actors;
  - Actor↔Actor and Actor↔world Interactions;
  - independent Memories, Knowledge access, relationships, goals, plans, activity and location;
  - valid causal information propagation;
  - persistent consequential Events;
  - authoritative deterministic world resolution.
- Settlement control simulation:
  - 36 Actors;
  - 10,000 Monte Carlo runs;
  - median **2,197 Interactions**;
  - median **1,022 model-driven cognition calls**;
  - **~2.911M input / ~0.175M output = ~3.086M total tokens**, using responsibility-specific token profiles.
- First-order 43-Cognitive-Actor background extrapolation:
  - **~2,624 Interactions**;
  - **~1,221 model-driven calls**;
  - **~3.477M input / ~0.210M output = ~3.686M total tokens**.
- Participant activity sensitivity:
  - 2×, 4×, 6×, 8× ordinary Actor interaction density;
  - **~2,746–3,112 total Interactions**;
  - **~1,282–1,465 total model calls**;
  - **~3.721–4.453M input / ~0.225–0.271M output = ~3.945–4.723M total tokens**.
- Supporting material:
  - `docs/signals-high-fidelity-computational-workload-2026-10-07.md`;
  - `docs/signals-settlement-temporal-contact-simulation-2026-10-07.md`;
  - `docs/signals-participant-interaction-sensitivity-2026-10-08.md`;
  - `scripts/signals_settlement_sim.py`;
  - `data/signals-settlement-sim/`.

### 15.2 What Actually Consumes Computation

- Separate:
  - Actor↔Actor social/communicative cognition;
  - Actor↔world cognition;
  - deterministic authoritative operations;
  - retrieval/context construction;
  - persistence/indexing;
  - Knowledge propagation.
- Most world Interactions do not require probabilistic cognition.
- Actor↔world activity dominates Interaction count but usually uses narrower cognition when inference is required.
- Participant cognition itself creates no Enclave inference load.
- Participant actions increase inference only through causal fan-out into model-driven Actors.
- **This analysis intentionally declines any considerations for use of inference in the Enclave or Memory implementation itself.**
- One canonical Event may create multiple Actor Memories without duplicating the Event.

### 15.3 Persistent State and Storage Cost

- Scope is **Enclave-only storage**.
- Explicitly exclude:
  - terrain/game-engine data;
  - rendering assets;
  - audio/animation;
  - physics/collision/navigation;
  - conventional non-Enclave game state;
  - application binaries and unrelated deployment content.

#### 15.3.1 Semantic World Knowledge

- Retire the earlier ~1,300 and ~10,000 starting-state estimates as too sparse.
- Use:
  - **100,000–200,000 world Knowledge/state records** as the envelope;
  - **150,000** as the central case.
- Central 150k breakdown:
  - 30k valley geography/environment/ecology/geology/weather/routes;
  - 25k settlement Facet, structures, infrastructure, facilities and spatial/operational state;
  - 15k objects/equipment/resources/material affordances;
  - 12k settlement history/culture/institutions/local Knowledge;
  - 18k Federation/Starfleet history/law/organization/doctrine/procedure;
  - 16k Romulan/Vulcan history/culture/politics/doctrine;
  - 17k science/technology/medicine/species/general setting Knowledge;
  - 5k Domains/Enclaves/Rank/Facets/classification relationships;
  - 7k mission/obelisk/*Susquehanna*/crash/signal/casualties/evidence;
  - 5k current canonical Actor/institutional state, plans, reports, communications and external agents.
- Include at least a dozen relevant Domains, at least five Enclaves, and the settlement Facet.
- Shared canonical Knowledge remains deduplicated.

#### 15.3.2 Actor Histories

- **1,000 pre-existing Memories per living Actor**.
- Simplified reference:
  - **44 living Actors**;
  - **44,000 prior Actor Memories**.

#### 15.3.3 Runtime Growth

- Replace the old ~400-Event / ~2,000-Memory guess with persistence derived from the Interaction workload.
- For storage accounting:
  - every Interaction is itself **1 Event**;
  - every Interaction also produces **1 resulting Event**;
  - use **1 generated Fact per Event** as the central assumption;
  - persist **1 Memory per participating Actor per Interaction**;
  - price Facts, Events, and Memories equally at **9.5 KiB/record**.
- 36-settler control median:
  - ~2,197 Interactions;
  - ~4,394 mandatory Interaction/result Events;

  - **~4,394 Events**;
  - **~4,394 generated Facts**;
  - ~2,380 Memories;
  - **11,167 generated records**;
  - **~103.59 MiB**.
- 43-Cognitive-Actor background:
  - ~2,624 Interactions;
  - ~5,248 mandatory Interaction/result Events;

  - **~5,248 Events**;
  - **~5,248 generated Facts**;
  - ~2,843 Memories;
  - **~13,339 generated records**;
  - **~123.75 MiB**.
- Participant activity sensitivity raises runtime-generated storage to approximately **129.98–148.65 MiB** across the 2×–8× envelope.




#### 15.3.4 Physical Record Cost

- Conservative working unit:
  - **~9.5 KiB per vector-bearing record**.
- Historical GottZ/ctx PostgreSQL + HNSW benchmark:
  - 102,520 rows;
  - ~684 MB context_blocks;
  - ~260–264 MB HNSW;
  - ~948 MB combined;
  - ~9.5 KiB/record.
- Reliquary ~5 KiB fully vectorized Memory is an efficiency comparison, not the baseline.

#### 15.3.5 Storage Formula

- Let **W** = world Knowledge/state records.

```
records = W + 44,000 prior Memories + 13,339 background runtime-generated records
        = W + 57,339
```

- 100k world Knowledge → 157,339 records → **~1.43 GiB**.
- 150k world Knowledge → 207,339 records → **~1.88 GiB**.
- 200k world Knowledge → 257,339 records → **~2.33 GiB**.
- Runtime-generated Facts/Events/Memories alone → **~123.75 MiB** background, **~129.98–148.65 MiB** with Participant activity.
- Add Enclave graph/provenance/relationship structures and implementation-specific overhead separately rather than inventing a multiplier.

### 15.4 Cognitive Simulation Cost

- Use responsibility-specific token profiles rather than one universal call shape.
- **Social/dialogue/complex cognition:** 4,000 input / 250 output tokens.
- **Routine Actor↔world cognition:** 1,500 input / 80 output tokens.
- The 43 Cognitive Actors produce approximately 1,221 model calls during an ordinary eight-hour period.
- The single Participant Actor requires **zero cognition inference**. Additional calls arise from Cognitive Actors responding to Participant Interactions.

**Eight-hour inference workload**

| Scenario | Model calls | Input tokens | Output tokens | Total tokens |
| --- | ---: | ---: | ---: | ---: |
| 43-Actor background | ~1,221 | 3.477M | 0.210M | **3.686M** |
| Participant @ 2x background activity | ~1,282 | 3.721M | 0.225M | **3.945M** |
| Participant @ 4x | ~1,343 | 3.965M | 0.240M | **4.205M** |
| Participant 6× | ~1,404 | 4.209M | 0.255M | **4.464M** |
| Participant 8× | ~1,465 | 4.453M | 0.271M | **4.723M** |

At 8× Participant activity, the additional NPC cognition beyond background amounts to approximately:

- **244 additional model calls**
- **976,000 additional input tokens**
- **61,000 additional output tokens**
- **1.037M additional tokens overall**

These are estimated volumes of model-driven Actor inference, not Participant cognition or inference internal to Enclave's Memory infrastructure.

- Dense causal fan-out remains more important than session-average throughput.
- Retain the 12-Actor / 10-second social-cognition burst as a stress case.

### 15.5 Deterministic Activity and Authoritative Resolution

- **Authoritative computation:** conventional systems resolve physical state, Loci, possession, rules, communications, Domain/Enclave/Rank/Facet relationships, Knowledge access, causal conditions, and persistence. Distinguish these deterministic responsibilities from model-driven cognition (§15.4).
- **Small-scale first-order baseline:** the 43-Actor *Signals* workload generates ~2,624 Interactions, ~5,248 Event records and ~13,339 total records per eight simulated hours: approximately **0.091 Interactions/s, 0.182 Events/s and 0.463 records/s**. These are simulated workload counts, **not CPU or database benchmarks**.
- **Causal expansion:** an Interaction is an Event and produces a resulting Event in the reference model. That result may trigger additional Events, changes and Actor responses, but the model does not simulate those cascades. An illustrative branching factor `b` over `d` generations gives `1 + b + … + b^d` potential occurrences before failed conditions, merging consequences and deduplication. This is a sensitivity example, not a claim that Enclave inherently expands exponentially.
- **Traversal cost:** determining consequences requires identifying affected Actors, Loci, relationships, Knowledge dependencies and applicable conditions. Work depends on the number of *nodes and edges actually examined*, graph density, causal depth, indexing, filtering and reuse. Bounded reachability does not require enumeration of every possible path.
- **Measured comparison from Reliquary Freshness propagation** (single-host, matched release-mode observations; propagation time only):

| Graph and propagation scenario | Original | Grouped-origin traversal | Improvement |
| --- | ---: | ---: | ---: |
| 1,084 nodes / 7,029 edges; eight roots in one Community | 42.047 ms | 2.374 ms | **17.71×** |
| Same graph; roots in different Communities | 40.582 ms | 17.183 ms | **2.36×** |
| 2,810 nodes / 22,464 edges; roots of unknown Community | 45.284 ms | 4.332 ms | **10.45×** |

- **Why topology and implementation matter:** in a separate 2,048-node synthetic test, grouping eight same-Community roots preserved the **same 184 recipients** while reducing examined edges from **9,687 to 1,482 (6.54× fewer)**. The original real-graph baseline also demonstrated a deliberately broad event reaching **1,079 of 1,084 nodes**. These are Freshness propagation workloads, **not typical Enclave Event frequencies**.
- **Large-graph reference:** Arcana's evaluated repository graph contained ~1.125 million nodes and ~2.367 million edges. A bounded neighbour request took **0.237 ms**, while a scoped architecture-summary request took **~2.024 seconds**. These are fundamentally different one-off queries under warm filesystem cache conditions, not comparable per-Event timings. Reliquary's batch tests additionally show that concurrent independent Events can benefit from parallel execution, without implying within-Event or whole-operation acceleration.
- **Combined growth factor:** total deterministic cost depends on the number of originating Interactions, the additional consequences that become Events, and the traversal and state-resolution work required per Event. Small first-order counts can therefore conceal broad cascades, while bounded traversal, deduplication and shared search work can reduce cost without sacrificing correctness.
- **Evidence and limitations:** these are measurements from Reliquary and Arcana, **not a benchmark of Enclave's world-state implementation or causal fan-out**. Original reports, supporting raw benchmark bundles and SHA-256 provenance are copied into `docs/research/section15-deterministic-evidence/` (see `MANIFEST.md`). The primary comparison is the Reliquary P1 Freshness report.
- **Conclusion:** ordinary deterministic activity looks manageable at bounded *Signals* scale. The primary scaling uncertainty is **the breadth and depth of Event consequences and the cost of discovering and resolving them**, which requires actual Enclave implementation measurements.

### 15.6 Temporal Fidelity and Event-Driven Cognition

- Full-time Cognitive Actors do not imply continuous inference.
- Actors can continue existing plans and routine actions deterministically.
- Invoke cognition when:
  - new information arrives;
  - circumstances change;
  - an Interaction requires interpretation;
  - a choice/replanning point occurs;
  - communication requires semantic response.
- Event-triggered cognition preserves fidelity better than arbitrary fixed-frequency inference.

### 15.7 Locality and Causal Reach

- Use Loci, communication channels, relationships, institutions, Domains and Enclaves to bound causal reach.
- Only Actors actually affected by an Event require reevaluation.
- Locus occupancy also supplies the contact topology used by the settlement workload model.
- Locality avoids global recomputation without requiring loss of persistent representation.

### 15.8 Model Routing and Costs

#### 15.8.1 Hosted API Inference

- Model capability can be routed by responsibility.
- Illustrative route:
  - 70% Luna;
  - 25% Sol;
  - 5% Astra.
- Verified 2026-10-08 Standard short-context rates:
  - Astra $10/M input, $50/M output;
  - Sol $2/M input, $10/M output;
  - Luna $0.10/M input, $0.50/M output.
- 43-Actor background:
  - all Astra ~**$45.24**;
  - all Sol ~**$9.05**;
  - all Luna ~**$0.45**;
  - illustrative routed ~**$4.84**.
- 8× Participant scenario:
  - all Astra ~**$58.05**;
  - all Sol ~**$11.61**;
  - all Luna ~**$0.58**;
  - illustrative routed ~**$6.21**.
- These are price calculations, not quality-equivalence claims. Hosted API charges scale with input and output tokens, rather than GPU allocation time.

#### 15.8.2 Renting GPUs for Open-Weight Inference

- A second deployment option is to rent GPU capacity and operate an open-weight model-serving stack directly.
- The following are illustrative **USD rental rates checked 2026-10-08**. Eight-hour figures assume **one GPU allocated for the entire eight-hour reference session**, or eight active GPU-hours for usage-metered services.

| Provider / mode | Example GPU | VRAM | GPU rental/hour | Eight GPU-hours |
| --- | --- | ---: | ---: | ---: |
| RunPod Pods | A40 | 48 GB | $0.49 | **$3.92** |
| RunPod Pods | A100 PCIe | 80 GB | $1.59 | **$12.72** |
| RunPod Pods | RTX Pro 6000 | 96 GB | $2.09 | **$16.72** |
| Lambda Cloud / single-GPU VM | A6000 | 48 GB | $1.09 | **$8.72** |
| Lambda Cloud / single-GPU VM | H100 PCIe | 80 GB | $3.29 | **$26.32** |
| Modal / pay-per-second GPU | H100 SXM | 80 GB | ~$3.95 | **~$31.59** |

- **RunPod:** fixed-allocation Pods and separately priced serverless inference workers; GPU class, rental tier, and inventory affect availability. Source: https://www.runpod.io/pricing
- **Lambda Cloud:** on-demand GPU VMs; single-GPU pricing above, with larger multi-GPU instances available. Source: https://lambda.ai/pricing
- **Modal:** execution-driven GPU rental billed by the second. Its H100 GPU rate is $0.001097/second (~$3.95/active hour); separately metered CPU, RAM, and storage may add costs. Source: https://modal.com/pricing
- **Vast.ai:** an alternative marketplace with host-set, changing prices and on-demand, interruptible, reserved, and serverless options. Omit a fixed quote because actual offers depend on host, location, and supply. Sources: https://vast.ai/pricing and https://github.com/vast-ai/docs/blob/main/guides/pricing.mdx
- **Pricing interpretation:** a GPU reserved for eight hours costs eight times its hourly rate even if inference is intermittent; usage-driven serverless deployment may reduce active-time charges but has start-up/availability trade-offs. Interruptible capacity may serve background/replay jobs but is less appropriate for Participant-facing, latency-sensitive reactions.
- **Capacity interpretation:** eight rented GPU-hours do **not** establish that one GPU can serve all inference within the eight-hour scenario. Verify model weights and quantization fit in VRAM alongside KV cache, then benchmark prefill, generation, batching, concurrency, and burst latency. Multi-GPU hosting increases the rental total.
- GPU rental excludes some or all CPU/RAM, persistent storage, networking, setup and maintenance, model licensing, security/data-residency controls, and operating labor; check provider-specific billing terms.
- The hosted API comparison includes a different model family and service model. GPU rental costs **cannot** be interpreted as providing equivalent output quality, latency, or reliability; they are alternative architectural cost envelopes, not apples-to-apples inference quotes.

### 15.9 Inference Capacity and Real-Time Feasibility

- Distinguish **aggregate throughput across the eight simulated hours** from **response latency** when multiple Actors need cognition simultaneously. Sufficient total throughput does not guarantee a responsive game.
- Published NVIDIA DGX Spark batch-size-one results (2,048 input / 128 output):

| Model | Prompt processing | Output generation |
| --- | ---: | ---: |
| GPT-OSS-20B | ~3,670 input tok/s | ~82.7 output tok/s |
| GPT-OSS-120B | ~1,725 input tok/s | ~55.4 output tok/s |

- Extrapolate separately to the §15.4 profiles: social/complex cognition **4,000 input / 250 output**; routine Actor↔world cognition **1,500 input / 80 output**.
- **GPT-OSS-20B:**
  - social ~4.1 seconds/call; world ~1.4 seconds/call;
  - serial execution of the complete 43-Actor background workload ~58 minutes;
  - serial execution including the 8× Participant activity scenario ~75 minutes.
- **GPT-OSS-120B:**
  - social ~6.8 seconds/call; world ~2.3 seconds/call;
  - serial background workload ~97 minutes;
  - serial 8× Participant scenario ~124 minutes.
- These are arithmetic extrapolations from a *different benchmark sequence shape*, not measured Enclave latency, concurrency, or quality. They assume no batching benefits and do not account for other system work.
- At 1:1 simulated/wall-clock time, aggregate inference may fit in eight hours, but **several seconds per individual response** can still disrupt interactive play. Game-time acceleration (§15.1) increases wall-clock throughput demand.
- **Dense causal burst:** twelve Cognitive Actors require social cognition within ten seconds:
  - 12 × 4,000 = **48,000 input tokens**, and 12 × 250 = **3,000 output tokens**;
  - sustaining the ten-second window requires **4,800 input tok/s** and **300 output tok/s** in aggregate, before overhead.
- These burst demands cannot be verified from single-request benchmarks alone. Evaluate batching, simultaneous requests, queuing, memory/KV cache, quantization, and serving architecture.
- Multiple GPUs, smaller or specialist models, model routing (§15.8), and background/asynchronous cognition change capacity and latency, with quality and fidelity trade-offs.
- **The deployment requirement is not merely to complete eight hours' worth of inference, but to deliver each cognition result when the simulation requires it.**

### 15.10 The Manhattan Test

- *Signals*' bounded reference—43 Cognitive Actors over eight simulated hours—requires ~2,624 Interactions, ~123.75 MiB in generated records, ~1,221 inference calls, and ~3.686M tokens. At this scale the burden appears manageable; that says little about a conventional, continuously populated world.
- Take Manhattan's **1,664,862 estimated 2025 residents** (U.S. Census Bureau, https://www.census.gov/quickfacts/fact/table/newyorkcountynewyork/PST045225): **~38,718 times** the 43-Actor reference. Extend the *same per-Actor* activity and record-generation assumptions linearly—not a validated simulation of city life.

| Cognitive Actors | Interactions / 8h | Generated storage / 8h | Model calls / 8h | Total tokens / 8h |
| --- | ---: | ---: | ---: | ---: |
| 43 (*Signals*) | ~2,624 | ~123.75 MiB | ~1,221 | ~3.686M |
| 1,000 | ~61,000 | ~2.81 GiB | ~28,400 | ~85.7M |
| 10,000 | ~610,000 | ~28.1 GiB | ~284,000 | ~857M |
| 100,000 | ~6.10M | ~281 GiB | ~2.84M | ~8.57B |
| 1,664,862 (Manhattan) | **~101.6M** | **~4.57 TiB** | **~47.3M** | **~142.7B** |

- **Storage (§15.3):** 1,000 pre-existing Memories per Manhattan Actor would consume ~14.7 TiB. At unchanged activity, generated data adds ~13.7 TiB per simulated day and ~4.9 PiB per simulated year. These figures exclude the much larger world-specific Knowledge base and additional indexes, graphs, and infrastructure.
- **Deterministic processing and locality (§§15.2, 15.5–15.7):** averages reach ~3,528 Interactions, ~7,055 Events, and ~17,932 generated records per simulated second. Raw writes alone are not necessarily prohibitive; propagation, retrieval, graph traversal, synchronization, and causal fan-out are unmeasured. Locality cannot stop cumulative global history growth.
- **Cognition (§15.4):** ~47.3M model calls require ~134.6B input and ~8.11B output tokens per eight-hour period; average demand is ~4.67M input and ~282,000 output tokens per simulated second, before causal bursts.
- **Routing, rental, and hardware (§§15.8–15.9):** at the illustrative 70/25/5 hosted routing rates, the API bill alone approaches **$187,000 per eight simulated hours**. Renting accelerators changes billing but not the required capacity; average output demand is ~3,400 times the published GPT-OSS-20B DGX Spark *single-request* generation rate. This is not an estimate of GPU count.
- **Temporal fidelity (§15.1):** figures represent eight hours of simulated *in-game* time. Time-dilation mechanics can increase or reduce the live computational burden by changing how quickly those hours elapse relative to wall-clock time.
- The linear extension is intentionally an extreme stress test: it assumes Manhattan Actors behave like the *Signals* cast, and omits commuters, visitors, variable activity, model-quality requirements, and additional storage overhead.
- Supporting calculations and assumptions: `docs/manhattan-test-scaling-2026-10-08.md`.
- **Conclusion:** Enclave's unmodified high-fidelity architecture appears manageable in small bounded environments but rapidly becomes impractical at urban scale. A persistent, fully cognitive Manhattan is not a feasible interactive-media deployment under current technological and economic constraints. **Section 16 explores architectural adaptations and different fidelity levels for practical applications.**

## 16. Practical Applications

> **Working section.** This section should return from the theoretical ceiling explored in §15 to realistic implementations, using the two §14 adventures as recurring examples of what each deployment tier would add or omit.

### 16.1 Enclave Is Not an All-or-Nothing Architecture

- A game does not need to simulate an entire persistent world at maximum fidelity to benefit from the architecture.
- Individual layers can be introduced progressively.
- Fidelity can be chosen according to:
  - genre;
  - budget;
  - player count;
  - narrative importance;
  - hardware constraints;
  - desired persistence.
- Each tier below should be illustrated by what it would mean for *A Wild Sheep Chase* and *Signals*, so the reader can compare capability rather than only abstraction.

### 16.2 Reactive Dialogue

- A low-complexity implementation can use:
  - bounded NPC Knowledge;
  - persistent Memories;
  - controlled retrieval;
  - probabilistic dialogue generation.
- The underlying game may otherwise remain conventional.
- In the §14 examples, this alone allows Shinebright, Noke, Guz, Ero Drallen, or a Romulan leader to answer unforeseen questions without acquiring Knowledge they should not possess.
- This can improve:
  - continuity;
  - knowledge discipline;
  - recognition of prior interactions;
  - context-sensitive dialogue.

### 16.3 Persistent Characters

- A deeper implementation can add:
  - Actor-specific Memories;
  - changing relationships;
  - persistent beliefs;
  - learned Knowledge;
  - limited off-screen action;
  - Actor initiative.
- The §14 divergences become persistent rather than being forgotten when the conversation ends.
- Characters can preserve meaningful continuity across repeated encounters.

### 16.4 Reactive Authored Narrative

- The core intended application combines:
  - authored narrative worlds;
  - persistent causal state;
  - Actor agency;
  - Knowledge propagation;
  - conditional authored developments;
  - probabilistic interpretation of unforeseen Participant behaviour.
- This is the level at which the alternate §14 paths are fully supported without requiring the original adventure to enumerate them.
- It provides the strongest direct response to the Agency–Persistence Gap described earlier in the paper.

#### Factions and Institutions

- Enclaves and Rank support:
  - factional information;
  - institutional permissions;
  - rumours;
  - organizational responses;
  - internal information asymmetry;
  - political or economic consequences.
- *Signals* provides the obvious institutional case through Starfleet, Romulan, and settlement interests.
- The same machinery can represent guild, magical, civic, or other institutional consequences in the fantasy example.
- Participant action can affect groups rather than only individual NPCs.

### 16.5 Partial and Hybrid Implementations

- The implementation levels described above need not be applied uniformly throughout a game.
- An implementation of the complete Enclave architecture may combine conventional deterministic NPCs, Reactive Dialogue, Persistent Characters, and fully autonomous Cognitive Actors within the same narrative environment.
- The appropriate fidelity depends on an Actor's narrative function, causal significance, and expected interactions with Participants.
- Lower-fidelity Actors can still participate in the authoritative world, possess relevant state, receive information where supported, and become involved in consequential Events.
- The objective is not to eliminate narrative complexity, but to concentrate expensive cognition where independent interpretation and decision-making can meaningfully influence the narrative.
- The major-divergence *Signals* example from §14.10 can be implemented using exactly this approach.

#### Proposed Hybrid Implementation of *Signals*

**Conventional Deterministic Activity**

- Ordinary NPC activity remains governed by conventional game systems:
  - movement and schedules;
  - routine work and settlement operations;
  - ordinary combat and physical interactions;
  - resource management;
  - established orders and behaviours.
- No model invocation is required simply because an NPC performs an ordinary action.
- Deterministic state and relevant consequential Events remain available to the higher-fidelity narrative system.

**Level 1 — Reactive Dialogue for Ordinary NPCs**

- All remaining ordinary settlers, guards, workers, and other cannon-fodder NPCs receive Reactive Dialogue.
- They can respond conversationally to Participants within their available Knowledge and authored roles.
- They do not independently deliberate, revise plans, or initiate model-driven behaviour.
- Inference occurs only when a Participant initiates a relevant dialogue Interaction.
- Their ordinary activities remain conventionally scripted or deterministic.
- The settlement can therefore appear conversationally responsive without maintaining dozens of autonomous Cognitive Actors.
- They hold no personal Memories of Interactions with Participants and can know nothing about them beyond what has been added to the Knowledge Base.
- These Actors may nevertheless acquire Knowledge through deterministic mechanisms, including information about its source or provenance, without requiring autonomous cognition or persistent Actor-specific Memories.

**Level 2 — Persistent Characters for Ordinary Romulan Personnel**

- Surviving non-officer Romulans, excluding the wounded survivor central to the divergence, receive Persistent Character capabilities.
- They retain Memories of Participant Interactions, develop opinions, and adjust their subsequent behaviour toward those Participants.
- Their cognition is restricted to Participant-facing Interactions rather than autonomous routine activity or off-screen planning.
- Orders, movement, combat, and ordinary military behaviour continue through conventional game systems.
- Persistent relationships allow earlier treatment by Participants to influence later dialogue without requiring independent continuous cognition.

**Level 3 — Fully Cognitive Narrative Actors**

- Reserve the complete Enclave cognitive cycle for the characters whose independent decisions can materially change the authored trajectory:
  - **the wounded Romulan survivor**, whose rescue and cooperation may initiate the divergence;
  - **Ero Drallen and other principal settlement representatives**, whose responses determine settlement cooperation and access;
    - excepting Ero Drallen, most of these characters can additionally be granted full narrative-altering cognition capabilities only when necessary.
  - **the Romulan captain**, whose decisions determine whether the surviving force accepts a ceasefire or resumes hostilities;
  - **potentially the remote Starfleet captain**, when communication, orders, or institutional decisions become causally relevant.
- These Actors retain the full cognitive capabilities and informational constraints described in §§12–13.
- They may evaluate newly received Knowledge, revise goals, initiate actions, and respond independently to consequential Events.
- Full cognitive fidelity need not be a permanent designation.
  - The wounded Romulan initially requires full cognition because his decisions may fundamentally redirect the narrative.
  - If he dies, is rescued by his comrades, or otherwise returns to them, full cognition is no longer required unless subsequent circumstances make him narratively consequential again.
  - If the Participants instead rescue and engage with him, full cognition remains available while his independent interpretation and decisions are relevant.
  - Changes in cognitive fidelity do not invalidate his established Knowledge, previous actions, or their persistent consequences.
  - Authorial conditions can therefore govern when individual Actors receive or relinquish full cognitive capabilities as narrative circumstances develop.

**Preserving the Authored Narrative**

- This hybrid configuration can reproduce the divergence demonstrated in §14 without predetermining the decisions of its Cognitive Actors:
  - the wounded Romulan may remember being rescued and exchange information with the Participants;
  - a proposal may reach Romulan leadership through a legitimate communication path;
  - the Romulan captain can independently evaluate the proposal and determine whether to accept or reject a temporary ceasefire;
  - settlement representatives can react to an unexpected joint delegation if cooperation is established;
  - changing relationships and circumstances may invalidate the prerequisites of the expected final assault.
- None of these developments requires autonomous cognition from the settlement's ordinary inhabitants or the Romulan rank and file.
- Knowledge access, consequential state changes, and Event authority remain consistent across the boundary between conventional and Cognitive Actors.
- The architecture preserves the possibility of coherent narrative divergence, not any particular outcome.
- The same level of narrative reactivity demonstrated in §14 can therefore be supported with substantially fewer autonomous Cognitive Actors than the high-fidelity reference in §15.

### 16.6 Practical Computational Implications

- The full-fidelity simulations examined in §15 establish the computational requirements of continuously supporting an entire population of permanently Cognitive Actors. They do not establish the minimum requirements for an Enclave implementation.

- The three implementation levels described in section 16.5 impose substantially different computational burdens, despite operating within otherwise identical game environments.

- At Levels 1 and 2, probabilistic inference is primarily driven by Participant interaction. The surrounding population can continue functioning through conventional deterministic systems without independently generating inference workloads.

- Persistent Characters introduce additional Memory, retrieval, and relationship-management requirements, but these need not translate into additional model invocations.

- At Level 3, Actors can exercise independent cognition in response to circumstances and Events without direct Participant involvement. This introduces an ongoing computational demand determined by the activity and cognitive requirements of the Actors themselves.

- The number of represented Actors therefore becomes substantially less important than **the number requiring cognition, the circumstances that activate it, and the frequency with which it occurs**.

**Computational Comparison — *Signals***

- Applying these distinctions to the 43-NPC *Signals* reference produces markedly different computational requirements over the same eight simulated hours.
- The comparison uses the 4× Participant activity scenario established in §15, with additional dialogue-frequency assumptions detailed in the supporting calculations.

| Implementation                        | Model Calls | Model Tokens | Inference Cost (USD) | Generated Records | Generated Storage |
| ------------------------------------- | ----------: | -----------: | -------------------: | ----------------: | ----------------: |
| Level 1 — Reactive Dialogue           |         122 |       0.519M |                $0.69 |                 0 |             0 MiB |
| Level 2 — Persistent Characters       |         122 |       0.519M |                $0.69 |                61 |          0.57 MiB |
| Level 3 — Reactive Authored Narrative |       1,343 |       4.205M |                $5.53 |            14,681 |        136.20 MiB |
| Hybrid Level 3 (§16.5)                |       \~193 |     \~0.733M |              \~$0.97 |           \~2,100 |       \~19.48 MiB |

- These implementations represent fundamentally different capabilities rather than interchangeable means of producing the same experience.
- The additional computational burden of Level 3 is associated primarily with autonomous Actor cognition and the persistent causal history supporting it, rather than conversational responsiveness alone.
- The hybrid *Signals* implementation established in §16.5 demonstrates how these requirements change when the complete architecture is applied selectively.
- Conventional deterministic behaviour continues to handle most ordinary activity, while independent cognition is reserved for the Actors and circumstances capable of materially altering the narrative.
- Relative to a uniformly full-fidelity implementation, this represents reductions of approximately:
  - **85.6% in model calls;**
  - **82.6% in token consumption;**
  - **85.7% in generated vector-bearing records.**
- Despite these reductions, the hybrid implementation retains the architectural capabilities necessary to support the major narrative divergence demonstrated in §14.10.
- **Reducing the computational fidelity of the surrounding simulation need not reduce the narrative fidelity available to consequential Actors and Events.**
- The savings arise from avoiding unnecessary cognition and detailed recording of routine activity, not from relaxing the authority or causal consistency of the narrative system.

**Computational Comparison — Manhattan**

- The Manhattan Test demonstrates how the differences between implementation levels become increasingly consequential as the represented population grows.
- The comparison retains the population and per-Actor assumptions established in §15, supplemented by an illustrative population of approximately 38,718 concurrently active Participants for calculating dialogue-driven inference at Levels 1 and 2.
- Each Participant is assigned the same activity assumptions used in the *Signals* comparison.

| Implementation                        | Model Calls | Model Tokens | Inference Cost (USD) | Generated Records | Generated Storage |
| ------------------------------------- | ----------: | -----------: | -------------------: | ----------------: | ----------------: |
| Level 1 — Reactive Dialogue           |    \~4.724M |    \~20.075B |            \~$26,535 |                 0 |                 0 |
| Level 2 — Persistent Characters       |    \~4.724M |    \~20.075B |            \~$26,535 |          \~2.362M |       \~21.40 GiB |
| Level 3 — Reactive Authored Narrative |   \~51.998M |   \~162.790B |           \~$213,963 |        \~568.415M |       \~5.029 TiB |

- At Levels 1 and 2, inference requirements remain principally dependent on Participant engagement, even when enormous NPC populations are represented.
- At Level 3, autonomous cognition introduces substantial background computational requirements independently of Participant activity.
- The resulting distinction is between **a large world populated by characters capable of responding to Participants** and **a large world populated by Actors independently interpreting and responding to their circumstances**.
- The Level 1 and 2 Manhattan estimates depend on the assumed active Participant population; NPC population alone cannot establish their inference demand.
- The Manhattan Level 2 comparison also excludes approximately 14.73 TiB of pre-existing personal Memories under the §15 assumption of 1,000 Memories per NPC.
- A city-scale representation does not inherently require city-scale autonomous cognition.

**Computational Boundaries**

- Reductions in inference and generated history do not eliminate the computational requirements of authored Knowledge, existing persistent history, retrieval, authoritative Event processing, or conventional game systems.
- In the hybrid *Signals* comparison, retaining the same authored Knowledge Base produces a substantially smaller reduction in total storage than in inference or newly generated records.
- Inference savings and storage savings are therefore not necessarily proportional.
- The numerical comparisons remain conditional estimates derived from the assumptions established in §15 and the additional dialogue, activation, and Event-frequency assumptions documented in the supporting calculations. They do not constitute measured implementation performance.
- Nevertheless, they demonstrate that the computational requirements of Enclave's intended narrative architecture need not approach those of its theoretical high-fidelity applications.
- **The practical computational boundary is not the total size of the represented world, but the extent to which that world must exercise independent cognition and preserve its consequences at high fidelity.**
- Regional partitioning, distributed processing, concurrent Participants, and other implementation concerns associated with much larger environments are considered separately in the Appendix B.

---

## 17. Conclusion

> **Working section.**

### 17.1 Restate the Problem

- Interactive narrative has historically traded broad Participant agency against persistent authored consequence.
- Conventional computation preserves state but struggles with unforeseen semantic interpretation.
- Probabilistic systems provide interpretive flexibility but are unreliable as the sole authority over persistent world state.

### 17.2 Restate the Architectural Response

- Enclave separates:
  - human authorship;
  - persistent authority;
  - Knowledge;
  - information access;
  - Actor agency;
  - Participant agency;
  - probabilistic interpretation.
- Its primitives provide a persistent narrative substrate in which those responsibilities can interact without collapsing into one system.

### 17.3 Restate the Narrative Consequence

- Human authors construct the world, its conflicts, Actors, information, pressures, and meaningful possibilities.
- Participants act within that world without being limited to enumerated narrative branches.
- Persistent consequences alter the circumstances from which subsequent authored and emergent activity develops.
- Narrative therefore emerges as a trajectory through an authored world rather than as traversal through an authored tree.

### 17.4 Restate the Engineering Consequence

- Model context does not need to contain the world.
- Probabilistic systems do not need to maintain authoritative state.
- Actors do not require omniscient Knowledge.
- Authors do not need to enumerate every response.
- Persistent computational systems and probabilistic systems can each operate primarily within the class of problems they handle well.

### 17.5 Closing Claim

- The central claim of Enclave is not that probabilistic models can replace authored narrative.
- It is that persistent computation, controlled information, probabilistic interpretation, and human authorship can be combined so that authored narrative acquires substantially greater capacity to absorb Participant agency.
- The intended result is **a deeply authored world whose narrative can remain coherent while responding persistently to actions its authors never individually anticipated**.

---

## Appendix C — The Replay Horizon: Epistemic Discovery and the Limits of Perceived Agency

> **Working appendix:** [The Replay Horizon outline](appendix-replay-horizon-outline.md). A theoretical extension of §4.6 examining initial increases in perceived agency, the eventual exhaustion of discoverable outcomes in fixed finite narrative systems, epistemic calibration, and the still-unproven psychological effect of discovering reconvergence.
