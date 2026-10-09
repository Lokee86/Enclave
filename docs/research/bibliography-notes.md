# Enclave Research Bibliography Notes

This file is the working source ledger for the Enclave design paper. It is intentionally more descriptive than the publication bibliography in `docs/design-paper.md`.

Use it to track:

- why each source was collected;
- which Enclave claim it can support;
- where it is likely to be cited;
- whether it is essential, supporting, or background;
- what the source does **not** establish, so later drafts do not overclaim it.

Status labels:

- **Essential** — likely to appear in the final paper and carry a major conceptual claim.
- **Supporting** — useful corroboration, comparison, or narrower support.
- **Background** — useful research context, but may not need a final citation.
- **Review** — retained, but the exact claim should be checked against the source before citation.

---

## 1. Human authorship, creative value, and generated narrative

These sources support Section 2 and the surrounding argument that generated output quality and human authorship are separate questions. They should not be used to claim that human authors are categorically better at every local narrative task.

| Source | Role | Supports | Likely use | Status / caution |
| --- | --- | --- | --- | --- |
| Agarwal, Naaman, & Vashistha (2025), *AI suggestions homogenize writing toward Western styles and diminish cultural nuances* | Peer-reviewed HCI | Risks of homogenization and reduced cultural nuance in AI-assisted writing | §2 Human Authorship | **Supporting.** Use for diversity/homogenization, not as proof that AI cannot produce creative text. |
| Appel et al. (2025), *I, ChatGPT: linguistic properties and human experiences of human- versus AI-generated stories* | Peer-reviewed empirical | Reader experience and linguistic differences between human- and AI-generated stories | §2 / §5 research note | **Supporting.** Useful for nuanced comparison of reader response. |
| Bellaiche et al. (2023), *Humans versus AI... artwork* | Peer-reviewed empirical | Human-vs-AI authorship attribution/preferences in creative work | §2 | **Background/Supporting.** Artwork rather than narrative; use only for broader authorship-perception context. |
| Marco, Gonzalo, & Fresno (2025), *The Reader is the Metric* | Peer-reviewed NLP | Reader profiles and textual features can explain conflicting assessments of AI creative writing | §2 | **Supporting.** Helps avoid simplistic "AI is better/worse" claims. |
| Raffloer & Green (2025), *Of love & lasers* | Peer-reviewed empirical | Reader perceptions of AI- versus human-authored narratives | §5 research note | **Supporting.** One of the direct narrative-comparison sources already referenced in the draft. |
| Sears & Weisberg (2026), *Bot or not* | Peer-reviewed empirical | Ability to distinguish and evaluate human- vs AI-written stories | §5 research note | **Supporting.** Already referenced in the draft. |
| Sourati et al. (2026), *The shrinking landscape of linguistic diversity in the age of large language models* | Peer-reviewed empirical | Possible loss of linguistic diversity around LLM-mediated writing | §2 | **Supporting.** Use specifically for diversity effects. |
| Stanko-Kaczmarek, Dera, & Koscielska (2025), *Between the Lines* | Peer-reviewed empirical | Effects of attributed AI/human authorship on poetry perception | §2 | **Background/Supporting.** Poetry rather than interactive narrative. |
| Szabó, Krizsai, & Deme (2026), *The invisible author* | Peer-reviewed sociolinguistic | Human judgments about identifying AI- and human-generated narratives | §2 | **Background/Supporting.** Useful for authorship perception, not narrative architecture. |
| Tian et al. (2024), *Are Large Language Models Capable of Generating Human-Level Narratives?* | Peer-reviewed NLP | Comparative narrative-generation quality | §2 / §5 | **Supporting.** Useful when separating local generative capability from authorship authority. |
| Wang et al. (2026), *A large-scale comparison of divergent creativity in humans and large language models* | Peer-reviewed empirical | Comparative divergent creativity | §2 | **Supporting.** Broader creativity evidence; do not treat as a direct interactive-narrative result. |
| Xu et al. (2025), *Echoes in AI: Quantifying lack of plot diversity in LLM outputs* | Peer-reviewed empirical | Plot diversity limitations in generated narrative | §2 / §4 | **Supporting.** Useful for limitations of unconstrained generated narrative diversity. |

---

## 2. Situation design, world reaction, and Gamemastering practice — Justin Alexander

Alexander is a major practitioner precedent for Enclave, especially the claim that authors can prepare **situations, actors, information, goals, resources, and pressures** rather than exhaustive action branches.

The safe framing is:

> A substantial strand of Alexander's Gamemastery work describes a human-operated reactive narrative practice. Enclave formalizes parts of the reactive work that Alexander leaves to the human GM.

Do **not** claim that Alexander provides Enclave's full architecture. He does not formalize authoritative truth vs information vs belief, provenance, actor-specific epistemic state, proposal-versus-event authority, computational event validation, or automated information diffusion.

### 2.1 Situation over predetermined sequence

| Source | Supports | Likely use | Status / caution |
| --- | --- | --- | --- |
| Alexander (2009), *Don’t prep plots* | Situation design instead of predetermined sequences; goal-oriented opponents; preparation of circumstances rather than specific player responses | §3 core framing; §5 GM analogy | **Essential.** One of the strongest conceptual precedents. |
| Alexander (2026), *Is node-based design prepping a plot?* | Later clarification that node structures describe situations/relationships rather than a predetermined participant sequence | §3 clarification | **Supporting.** Useful to prevent misreading the earlier node material. |
| Alexander (2015), *Don’t prep plots – Tools, not contingencies* | Prepare reusable world/situation tools rather than contingency trees for anticipated actions | §3 adversarial design; §4 branching-cost problem | **Essential.** Very close to Enclave’s “reactive machinery instead of exhaustive branching” argument. |
| Alexander (2018), *Smart prep* | Preparation should maximize reusable value and avoid work that may never matter in play | §3 / §4 authoring cost | **Supporting.** Pairs well with “authorial leverage.” |

### 2.2 Timelines, changing state, and proactive world activity

| Source | Supports | Likely use | Status / caution |
| --- | --- | --- | --- |
| Alexander (2009), *Don’t prep plots: Prepping scenario timelines* | Future events and NPC activity can be prepared conditionally, then revised when player action changes the situation | §3 narrative planning; §5 conditional trajectory | **Essential.** Strong precedent for intended trajectories that are not forced sequences. |
| Alexander (2011), *Advanced node-based design – Part 1: Moving between nodes* | Push as well as pull: the world can proactively act on participants without railroading | §3 actor/world activity; §13 persistent cause and effect | **Essential/Supporting.** Strong bridge to event-triggered actors. |
| Alexander (2015), *Don’t prep plots – “You will rue this day, heroes!”* | Antagonists and consequences should arise from goals, survival, resources, and participant interference rather than preservation of a fixed villain role | §3 adversarial design / actors | **Supporting.** Use for actor goals and reactive opposition, not as a formal actor model. |

### 2.3 Information flow, clues, and revelations

| Source | Supports | Likely use | Status / caution |
| --- | --- | --- | --- |
| Alexander (2008), *Three Clue Rule* | Redundant information pathways and robust discovery; important conclusions should not depend on one fragile path | §3 information architecture; later information sections | **Essential/Supporting.** Generalize carefully beyond mystery scenarios. |
| Alexander (2010), *Node-based scenario design – Part 3: Inverting the Three Clue Rule* | Information can be used to connect multiple loci of potential interaction and avoid brittle progression | §3 information flow | **Supporting.** |
| Alexander (2011), *Advanced node-based design – Part 5: The two prongs of mystery design* | Distinction between information that explains and information that points toward something actionable | §3 / §7–10 | **Supporting.** Useful analogy for different roles of information. |
| Alexander (2018), *Using revelation lists* | Separating revelations/conclusions from the individual clues that may establish them | §3 / §7 truth-information-belief discussion | **Supporting.** Do not claim this equals Enclave belief state; it is an information-design precedent. |
| Alexander (2020), *The secret life of nodes* | Explicitly reframes node design around the acquisition and flow of knowledge; includes proactive nodes/triggers | §3 central synthesis | **Essential.** One of the strongest sources for the information-flow strand. |

### 2.4 Node-based structure and diegetic organization

| Source | Supports | Likely use | Status / caution |
| --- | --- | --- | --- |
| Alexander (2010), *Node-based scenario design – Part 1: The plotted approach* | Fragility of linear event chains when progression assumes a specific participant action | §3 / §4 | **Essential/Supporting.** |
| Alexander (2010), *Node-based scenario design – Part 2: Choose your own adventure* | Explicit branching can expand combinatorially while still failing to anticipate all participant behavior | §4 branching problem | **Essential/Supporting.** Excellent support for the combinatorial-branching argument. |
| Alexander (2010), *Node-based scenario design – Part 5: Plot vs. node* | Modular meaningful situations can be encountered in different orders while order still has consequences | §3 | **Supporting.** |
| Alexander (2010), *Node-based scenario design – Part 9: Types of nodes* | Nodes are broad “points of interest” and can represent locations, people, organizations, events, activities, etc. | §3 terminology | **Supporting.** Important when explaining that nodes are not merely scenes. |
| Alexander (2020), *The secret life of nodes – Part 2: Node-based campaigns* | Node design scales upward; participant actions can create new campaign nodes | §3 / §5 | **Supporting.** Useful for runtime emergence from authored material. |
| Alexander (2020), *The secret life of nodes – Part 3: Fractal nodes* | Node structures can expand or contract in granularity | §3 / §14 variable fidelity analogy | **Supporting.** Analogy only; not evidence for computational simulation fidelity. |
| Alexander (2020), *The secret life of nodes – Part 4: Nodes aren’t everything* | Node design is only one tool; evolving campaign state and other structures remain distinct | §3 architectural boundaries | **Essential.** Supports the important point that node structure is not world state. |
| Alexander (2020), *The secret life of nodes – Part 5: Naturalistic node design* | Scenario structure can arise from the diegetic relationships among actual people, places, organizations, and events in the fictional world | §3 worldbuilding | **Essential.** Probably the strongest Alexander source for worldbuilding-derived structure. |

### 2.5 Open-ended interaction and game structures

| Source | Supports | Likely use | Status / caution |
| --- | --- | --- | --- |
| Alexander (2012), *Game structures* | Open-ended participant action still requires structures that determine how play proceeds and how actions connect to consequences | §3 / §13 | **Supporting.** Use for the need for interaction machinery, not as a direct computational architecture. |

---

## 3. Narrative architecture and authored worlds

### Jenkins, Henry (2004), *Game Design as Narrative Architecture*

- **Role:** Foundational theory.
- **Supports:** Worlds and spaces can themselves carry narrative structure; designers can act as “narrative architects”; environmental storytelling can embed information, stage events, and provide resources for emergent narrative.
- **Enclave claim supported:** Human authorship can reside upstream in the designed world and its affordances, not only in a fixed event sequence.
- **Likely use:** §3, especially the worldbuilding/intellectual synthesis opening.
- **Status:** **Essential.**
- **Do not overclaim:** Jenkins does not supply Enclave’s authoritative-state, actor-memory, provenance, reactive-actor, or event-validation model.

---

## 4. Storylets and Quality-Based Narrative

### Short, Emily (2019), *Storylets: You Want Them*

- **Role:** Primary practitioner / computational narrative design.
- **Supports:** Authored narrative units can be conditioned on prerequisites and can change shared state; such units can be recombined rather than placed in one explicit branch tree.
- **Enclave claim supported:** Deliberate authored narrative material can remain conditional and state-sensitive without requiring a single predetermined route.
- **Likely use:** §3 and §5.
- **Status:** **Essential.**
- **Do not overclaim:** A storylet is not equivalent to Enclave’s world-state or event model.

### Short, Emily (2019), *Storylets Play Together*

- **Role:** Primary practitioner.
- **Supports:** Storylets can operate across multiple scales and interact through shared state/resources.
- **Enclave claim supported:** Authored arcs and local events can coexist and condition one another without a monolithic branch tree.
- **Likely use:** §3 / §5.
- **Status:** **Supporting.**

### Failbetter Games (2012), *StoryNexus developer diary #2: Fewer spreadsheets, less swearing*

- **Role:** Primary practitioner.
- **Supports:** Quality-Based Narrative as a practical state-conditioned alternative between branch-heavy narrative and fuller simulation.
- **Enclave claim supported:** Mutable state can govern availability of authored narrative opportunities.
- **Likely use:** §3.
- **Status:** **Supporting.**

### Failbetter Games (n.d.), *Echo Bazaar narrative structures, part two*

- **Role:** Primary practitioner.
- **Supports:** Qualities control storylet/branch availability and are changed by completed content.
- **Enclave claim supported:** State-conditioned narrative availability is an established practical authoring technique.
- **Likely use:** §3 / §5.
- **Status:** **Supporting.**
- **Caution:** Verify exact publication date if the final citation style requires one.

---

## 5. Emergent narrative and purposeful authoring

### Louchart, Swartjes, Kriegel, & Aylett (2008), *Purposeful Authoring for Emergent Narrative*

- **Role:** Peer-reviewed interactive narrative research.
- **Supports:** Emergent narrative can be treated as an authoring problem: what should be intentionally specified when the realized sequence is not fixed in advance?
- **Enclave claim supported:** Human authorship and runtime emergence are not opposites; the design problem is where authorial intent is encoded.
- **Likely use:** §3.
- **Status:** **Essential/Supporting.**
- **Do not overclaim:** This does not establish Enclave’s specific solution.

---

## 6. Drama management and authorial leverage

### Chen, Nelson, & Mateas (2009), *Evaluating the Authorial Leverage of Drama Management*

- **Role:** Peer-reviewed interactive narrative research.
- **Supports:** The concept of **authorial leverage**: how much interactive narrative complexity can be obtained for a given amount of authoring effort.
- **Enclave claim supported:** A useful success criterion is not “number of branches,” but meaningful narrative possibility relative to authoring burden.
- **Likely use:** §3 / §4.
- **Status:** **Essential.**
- **Do not overclaim:** Authorial leverage is a useful evaluation concept; it does not prove Enclave will achieve high leverage.

### Nelson, Ashmore, & Mateas (2006), *Authoring an Interactive Narrative with Declarative Optimization-Based Drama Management*

- **Role:** Peer-reviewed computational narrative.
- **Supports:** Runtime systems can respond to participant behavior while using author-declared narrative objectives.
- **Enclave claim supported:** There is precedent for separating authored dramatic intent from the exact realized sequence.
- **Likely use:** §3 / related-work comparison.
- **Status:** **Supporting.**
- **Caution:** Enclave should distinguish itself from systems that allow a drama manager to override causal/world consistency for dramatic optimization.

### Mateas & Stern (2005), *Structuring Content in the Façade Interactive Drama Architecture*

- **Role:** Peer-reviewed computational narrative / system architecture.
- **Supports:** Authored dramatic material can be decomposed into reusable structures that are assembled responsively at runtime.
- **Enclave claim supported:** Responsive narrative realization can be built from authored components rather than a single fixed script.
- **Likely use:** §3 / related work.
- **Status:** **Supporting.**

### Rowe & Lester (2013), *A Modular Reinforcement Learning Framework for Interactive Narrative Planning*

- **Role:** Peer-reviewed computational narrative planning.
- **Supports:** Modular runtime planning/adaptation of interactive narrative.
- **Enclave claim supported:** Computational narrative systems have explored runtime adaptation rather than exhaustive static branching.
- **Likely use:** Related work / §3 supporting citation.
- **Status:** **Supporting.**

---

## 7. Working synthesis for Section 3

The current literature map supports a three-tradition synthesis:

1. **Situation and tabletop reactive design — Alexander**
   - Prepare situations, goals, resources, information, actors, and pressures.
   - Avoid predicting every participant action.
   - Let the world and its actors push back.
   - Organize information and interaction through reusable structures.

2. **Narrative architecture — Jenkins and emergent-narrative scholarship**
   - Human authorship can reside in the designed world, its information, conflicts, affordances, and dramatic possibilities.
   - Runtime emergence does not imply absence of authorial intent.

3. **Computational/state-conditioned narrative — Short, Failbetter, drama-management research**
   - Authored content can be conditionally available from state.
   - Runtime systems can choose, combine, or activate authored material in response to interaction.
   - Authorial leverage provides a useful measure of whether this actually reduces combinatorial authoring burden.

### Planned Section 3 progression

1. **Human authors construct narrative meaning through worlds, not merely sequences.**
   - Open with Jenkins and narrative architecture.
   - Establish that spaces, environments, information, conflict, and affordances can carry deliberate narrative meaning.

2. **Interactive authorship should focus on situations rather than participant-action scripts.**
   - Bring in Alexander's *Don’t Prep Plots*, *Tools, Not Contingencies*, scenario timelines, and goal-oriented opponents.
   - Emphasize that this is not an argument against planning; it is an argument against predicting participant behavior as the primary structure.

3. **Information organizes narrative possibility.**
   - Use Alexander's Three Clue Rule, revelation lists, node-based design, and *The Secret Life of Nodes*, alongside Jenkins' treatment of narrative information embedded in designed spaces.
   - What participants learn changes what they can understand and meaningfully attempt.

4. **Actors give the world motion.**
   - Use Alexander's goal-oriented opponents, proactive nodes, timelines, factions, and reactive antagonists.
   - Adversarial design means establishing what actors want, know, possess, and can do rather than enumerating every possible response.

5. **Conditional authored material preserves deliberate narrative structure.**
   - Use Short's storylets and Failbetter's Quality-Based Narrative.
   - Authored material can become available from state and alter state without requiring a single fixed route.

6. **Existing computational narrative research addresses related problems.**
   - Open with the precedent: Louchart et al. on purposeful authoring for emergent narrative; Chen et al. on authorial leverage; Nelson, Ashmore & Mateas on drama management; Mateas & Stern and Rowe & Lester on responsive runtime narrative systems.
   - Then close the subsection by reiterating the limitation of traditional computational approaches: these systems remain bounded by what their authors explicitly represent as states, content units, transitions, intervention rules, or optimization structures. Greater freedom therefore still drives authoring/state complexity, while purely generative approaches introduce a different problem of authority and consistency.
   - This closing limitation should form the bridge into Enclave rather than opening the subsection.

7. **Enclave formalizes the reactive step.**
   - Transition from precedent into the paper's own architecture.
   - A human GM can simply react to an unexpected situation; a computer requires that reaction to be decomposed into explicit machinery: authoritative world state, actor-specific memory and inference, actor intention/action proposal, event validation, consequences, and the observation or communication paths by which those consequences reach other actors.

A concise Section 3 thesis supported by this source set is:

> Interactive narrative authorship can be understood not as the exhaustive authorship of possible sequences, but as the authorship of a narrative possibility space: its world, actors, relationships, secrets, records, conflicts, resources, dramatic intentions, and conditional developments. Different traditions have approached portions of this problem as situation design, narrative architecture, modular narrative content, emergent narrative, and computational drama management. Enclave brings these concerns together through persistent world state, actor-specific history, causal event validation, and constrained observation and communication.

### Enclave-specific contribution boundary

The sources above support the **problem framing and precedent**, but the following should presently be treated as Enclave’s own architectural synthesis unless separate sources are added:

- authoritative world state distinct from any individual actor's memory or belief;
- provenance-linked claims and transformed retellings;
- actor-specific exposure, memory, inference, and belief;
- actor action proposals distinct from authoritative events;
- validation as the authority boundary between probabilistic actor reasoning and canonical world change;
- local diffusion through observation, communication, records, actors, and media;
- enclave-based access, exposure, and saturation shortcuts;
- event-triggered activation of probabilistic actors;
- the full cycle: actor reasoning → proposal → validation → event → world-state change → exposure/communication → actor memory/belief update → new proposal.

---

## 8. Section 4 research — state-space limits, formalization bottlenecks, and modern probabilistic assessment

This targeted pass addresses the specific gap left after Sections 2–3: evidence that the branching problem is more deeply a **representation and state-space problem**, evidence that traditional symbolic/game-AI approaches encounter authoring and scalability limits as domains become richer, and evidence that modern language-model agents can perform forms of open-ended contextual assessment that previously had to be much more explicitly represented.

### 8.1 Narrative planning is constrained by state-space and domain-model complexity

#### Fisher (2022), *Narrative Planning in Large Domains through State Abstraction and Option Discovery*

- **Role:** Peer-reviewed AIIDE research / direct state-space evidence.
- **Supports:** Narrative planning is normally constrained to relatively small state spaces; deploying intentional/cooperative agent behavior in larger game environments requires abstraction and otherwise incurs significant additional authoring effort.
- **Enclave claim supported:** The scaling problem is not merely a visible tree of written scenes. Computational narrative planning itself encounters difficulty as the represented state space grows.
- **Likely use:** §4 points on state-space growth and why simulation/planning does not automatically eliminate the branching problem.
- **Status:** **Essential for §4.**
- **Do not overclaim:** This is specifically about narrative planning, not proof that every deterministic architecture scales identically.

#### Porteous, Ferreira, Lindsay, & Cavazza (2021), *Automated Narrative Planning Model Extension*

- **Role:** Peer-reviewed planning / interactive narrative.
- **Supports:** Creating narrative planning domains has been identified as a bottleneck; authors must provide enough alternative actions/content to support diversity and robustness, including recovery from user-driven execution failure.
- **Enclave claim supported:** Moving from explicit branches to planning does not remove the authoring tax; the action/predicate domain itself must still contain the alternatives the planner can use.
- **Likely use:** §4 discussion of formalized possibilities and authoring burden.
- **Status:** **Essential.**
- **Do not overclaim:** Planning can generate combinations not individually scripted as plots; the limitation is the need to formally represent the domain from which those combinations are generated.

#### Hayton, Porteous, Ferreira, & Lindsay (2020), *Narrative Planning Model Acquisition from Text Summaries and Descriptions*

- **Role:** Peer-reviewed AAAI research.
- **Supports:** The underlying narrative-domain model is itself a well-documented planning-modeling bottleneck, compounded in interactive narrative because authors are generally not planning-language specialists.
- **Enclave claim supported:** Formal computational narrative requires an explicit machine-readable model of actions/objects/relations before planning can operate over them.
- **Likely use:** §4 as corroboration for Porteous et al. rather than a separate major argument.
- **Status:** **Supporting.**

### 8.2 Traditional game-AI structures improve organization but do not remove explicit behavioral representation

#### Iovino, Scukins, Styrud, Ögren, & Smith (2022), *A Survey of Behavior Trees in Robotics and AI*

- **Role:** Peer-reviewed survey.
- **Supports:** Behavior trees emerged in games partly because finite-state machines scaled poorly and became difficult to extend, adapt, and reuse as agent complexity increased; behavior trees improve modularity by reorganizing transition logic.
- **Enclave claim supported:** The history of game AI already contains successive attempts to manage the scaling problems of explicitly represented behavior.
- **Likely use:** §4 discussion of deterministic/symbolic control structures.
- **Status:** **Essential/Supporting.**
- **Do not overclaim:** Behavior trees can scale much better than FSMs. The paper does not establish that behavior trees “fail”; it shows that architecture changes can manage, but not eliminate, explicit behavior representation.

#### Riedl & Bulitko (2013), *Interactive Narrative: An Intelligent Systems Approach*

- **Role:** Peer-reviewed historical survey / field context.
- **Supports:** Reviews roughly two decades of computational interactive-narrative approaches and frames the field around systems that allow users to influence story direction through computational narrative intelligence.
- **Enclave claim supported:** Useful historical context for showing that planning, drama management, player modeling, and related formal approaches predate LLM-era systems.
- **Likely use:** §4 background or related-work framing.
- **Status:** **Background/Supporting.**
- **Do not overclaim:** Use this as field history, not as the main evidence for a specific scalability limitation.

### 8.3 Modern language models provide a new practical mechanism for open-ended contextual assessment

#### Park et al. (2023), *Generative Agents: Interactive Simulacra of Human Behavior*

- **Role:** Peer-reviewed UIST system paper.
- **Supports:** LLM-centered agents can use natural-language memories, retrieval, reflection, and planning to select behavior in an interactive environment; the evaluated agents produced believable individual and emergent social behavior without every social interaction being encoded as a fixed branch.
- **Enclave claim supported:** Flexible assessment of context, memory, and socially plausible next actions is now computationally practical in a way that can complement conventional state machinery.
- **Likely use:** §4 transition from older explicit representations to modern probabilistic assessment.
- **Status:** **Essential.**
- **Do not overclaim:** Generative Agents does not provide Enclave's authority model and should not be treated as evidence of deterministic correctness or reliable causal state management.

#### Hu et al. (2024; revised 2026), *A Survey on Large Language Model-Based Game Agents*

- **Role:** Broad game-agent survey; revised 2026 and reported as accepted by *ACM Computing Surveys*.
- **Supports:** LLM-based game agents are being used for reasoning, memory, perception-action interaction, coordination, adaptability, and open-ended goal formation in complex game environments.
- **Enclave claim supported:** The shift toward language-model game agents is broader than one prototype and directly targets capabilities that are awkward to enumerate with traditional game-agent structures.
- **Likely use:** §4 broad support for the technological shift.
- **Status:** **Essential/Supporting.**
- **Citation note:** Until a final ACM DOI/citation is available, the publication bibliography uses the arXiv record.

#### Hogan & Brennen (2024), *Open-Ended Wargames with Large Language Models*

> **HIGH-VALUE RECURRING SOURCE — KEEP VISIBLE DURING DRAFTING.**
>
> This paper is unusually close to Enclave's core historical argument from a different domain. It is likely to be useful in more than one section, especially wherever the paper contrasts predefined computational action spaces with open-ended human-style interpretation and adjudication.

- **Role:** Applied research preprint / direct historical comparison / strong conceptual analogue.
- **Core distinction:** The paper contrasts **quantitative games**, where participants choose from defined moves and formal rules determine outcomes, with **qualitative games**, where participants can propose open-ended actions and a human moderator interprets and adjudicates them.
- **Historical relevance:** The authors argue that game automation historically concentrated on the quantitative case because qualitative play requires interpreting unrestricted language and context. Their LLM-based system is presented as a practical way to automate part of that formerly human moderation role.
- **Why this matters for Enclave:** This is strong evidence for the claim that the visible branching problem sits on top of a deeper historical constraint: computers generally needed meaningful actions and responses translated into explicit formal representations before they could act on them.

##### Architecture analogue

Their Snow Globe system uses:
- **player agents** that receive a persona, game history, and situation, then propose open-ended natural-language actions;
- **team agents** that aggregate multiple player responses;
- a **control agent** that acts as moderator/adjudicator;
- textual **history objects** that can differ between players, allowing information asymmetry.

The resulting loop is approximately:

```text
history / situation
        ↓
actor interpretation
        ↓
open-ended action proposal
        ↓
LLM moderator / adjudication
        ↓
new narrated outcome
        ↓
updated history
```

That is close to one half of Enclave's intended runtime, but the authority boundary is importantly different.

##### Important Enclave contrast

In Snow Globe, the probabilistic moderator largely determines what happened by generating the adjudicated outcome. The paper explicitly recognizes that the same generative freedom needed for plausible adjudication can also produce unwanted invention, including actions or developments that were not actually supplied by participants.

That gives us a useful contrast:

```text
HOGAN & BRENNEN

actor proposal
    ↓
LLM adjudication
    ↓
generated outcome becomes game history
```

versus:

```text
ENCLAVE

actor proposal
    ↓
authoritative validation / causal machinery
    ↓
canonical event
    ↓
state consequences
    ↓
narrative realization
```

This makes the paper useful for **both halves** of Enclave's argument:
1. probabilistic models make open-ended action interpretation and contextual response practical;
2. probabilistic adjudication alone does not provide a sufficiently reliable authority boundary for persistent narrative reality.

##### Particularly useful historical example

The paper compares its approach with RAND-era automated wargaming work in which qualitative descriptions had to be converted into explicit computational models. Hogan & Brennen use this comparison to argue that modern language models can consume prose descriptions/personas directly instead of requiring the same degree of manual translation into formal decision machinery.

This is a strong supporting example for:

> **The historical bottleneck was not merely insufficient computation. It was the requirement to translate meaningful human behavior and open-ended situations into formal machine-readable representations before software could reason over them.**

Use that formulation carefully: the paper supports it as a concrete historical example, not as proof that every pre-LLM system had the same limitation.

##### Possible recurring uses in the Enclave paper

- **§3 — prior computational approaches and the historical limitation:** evidence for the transition from explicitly represented response spaces to open-ended probabilistic assessment.
- **§4 — branching/state-space problem:** supports the argument that predefined action spaces are a deeper constraint than visible branch trees.
- **§5 — gamemaster analogy / authored trajectory:** Snow Globe provides a direct computational moderator analogue, useful for showing what part of human GM work can now be delegated to probabilistic inference.
- **§6 and later architecture sections — authority boundary:** useful counterexample for why Enclave separates probabilistic proposal/interpretation from authoritative event validation.
- **Conclusion / significance:** potentially useful as outside-domain evidence that this technological transition is broader than videogame narrative.

##### Experimental result worth remembering

The authors vary natural-language leader personas and observe materially different emergent outcomes across repeated runs. This is useful evidence that prose-level actor characterization can affect downstream simulated behavior without those behaviors being enumerated as fixed branches.

Do **not** use the reported run frequencies as calibrated probabilities; the authors themselves caution against interpreting them that way.

- **Status:** **High-value recurring supporting source.**
- **Caution:** This is an arXiv preprint rather than a peer-reviewed publication. Pair historical/technical claims with peer-reviewed sources such as Park et al., Fisher, Porteous et al., Iovino et al., or the Hu et al. survey where possible.
- **Do not overclaim:** The paper does not provide Enclave's separation between authoritative world state and actor-specific history, its provenance model, persistent actor-memory machinery, or deterministic event authority. Its value is precisely that it demonstrates the new probabilistic capability while exposing the remaining authority problem.

### 8.4 Broader technical precedent for hybrid probabilistic–symbolic architecture

#### Gao et al. (2023), *PAL: Program-Aided Language Models*

- **Role:** Peer-reviewed ICML systems paper / strong division-of-labour precedent.
- **Supports:** PAL uses an LLM to interpret a natural-language problem and generate executable intermediate steps, but delegates actual solution execution to a conventional runtime such as Python because the model can make logical and arithmetic errors even when its decomposition is useful.
- **Enclave claim supported:** Probabilistic interpretation and synthesis do not need to replace deterministic machinery; they can change its role by supplying candidate structure while exact execution remains outside the model.
- **Likely use:** §4 points 10–11; later authority-boundary discussion.
- **Status:** **Essential/Supporting.**
- **Do not overclaim:** PAL concerns mathematical/symbolic reasoning, not persistent simulated world state. Its value is architectural precedent for splitting flexible interpretation from exact execution.

#### Kambhampati et al. (2024), *Position: LLMs Can’t Plan, But Can Help Planning in LLM-Modulo Frameworks*

- **Role:** Peer-reviewed ICML position paper / unusually direct architecture precedent.
- **Supports:** LLMs are treated as approximate knowledge sources coupled bidirectionally with external model-based verifiers. The authors explicitly argue for combining LLM flexibility with symbolic/model-based verification rather than treating either as sufficient alone.
- **Enclave claim supported:** Existing deterministic or symbolic systems can be **augmented and repurposed** as validators, verifiers, and formal reasoning machinery around probabilistically generated interpretations or proposals.
- **Likely use:** §4 points 10–11; later event-validation and authority sections.
- **Status:** **Essential for the hybrid-architecture argument.**
- **Particularly useful formulation:** Their framework extends model-based planning/reasoning toward more flexible knowledge, problem, and preference specifications while retaining external verification.
- **Do not overclaim:** This is a planning/reasoning framework, not a narrative-state architecture, and the paper's claim that LLMs cannot plan independently is a position within an active research debate.

#### Marra, Dumančić, Manhaeve, & De Raedt (2024), *From Statistical Relational to Neurosymbolic Artificial Intelligence: A Survey*

- **Role:** Peer-reviewed *Artificial Intelligence* survey / broad field-level support.
- **Supports:** Neuro-symbolic AI explicitly studies integration of neural learning with symbolic reasoning rather than replacement of one paradigm by the other.
- **Enclave claim supported:** The proposed deterministic/probabilistic division belongs to a broader technical direction in which statistical flexibility and symbolic structure are intentionally combined to exploit complementary strengths.
- **Likely use:** §4 points 10–11 as general support; possibly related-work framing.
- **Status:** **Essential/Supporting.**
- **Do not overclaim:** The survey supports hybridization at a general architectural level, not Enclave's specific allocation of narrative responsibilities.

### 8.5 Revised claim boundary for Section 4

The research supports a **narrower and stronger** version of the historical argument than “determinism was the problem” by itself:

> Traditional computational narrative and game-agent architectures generally require important states, actions, predicates, transitions, behaviors, or intervention options to be represented in advance. Planning and modular behavior architectures can recombine those representations and substantially improve authorial leverage, but the literature still identifies state-space scale, domain-model construction, alternative-content authoring, and behavioral complexity as recurring bottlenecks. Modern language-model agents add a practical mechanism for interpreting open-ended natural-language situations, retrieving context, reasoning about them, and proposing plausible behavior without requiring every interpretation or response to be individually enumerated.

This supports the Section 4 transition we want:

**meaningful branching creates increasingly demanding representation and state-management requirements → prior architectures improve the management of that explicit structure → probabilistic inference changes which parts must be enumerated → deterministic machinery can remain responsible for authoritative consequences.**

The sources do **not** support saying that probabilistic reasoning was nonexistent before LLMs, that all prior systems were purely deterministic, or that modern probabilistic models solve narrative authority and consistency by themselves.

---

## 9. Section 5 research — persistent worlds and the labour cost of human gamemastering

The important distinction for Section 5 is **not** that persistent worlds have failed to exist. Persistent online worlds plainly exist and some have run for decades. The rarer thing is a persistent world with **continuous human adjudication at tabletop-GM granularity**. Historical attempts repeatedly expose the same scaling problem: human gamemasters, event actors, moderators, and storytellers can only adjudicate a finite number of players, places, and situations at once, so continuous coverage becomes a staffing problem.

### 9.1 Ultima Online — volunteer labour made persistent human oversight possible, but not sustainably

#### Brown (2000), *Volunteer revolt*

- **Role:** Contemporary reporting on *Ultima Online*'s counselor program and resulting wage dispute.
- **Supports:** UO relied on a large volunteer workforce for ongoing player support in a persistent world. Reporting described roughly 500 counselors, minimum scheduled shifts, and at least one senior volunteer reporting workloads of up to 40 hours per week.
- **Enclave claim supported:** Human oversight of a persistent world can be supplied by people, but continuous availability scales into substantial recurring labour.
- **Likely use:** §5 when explaining why D&D-like gamemaster availability has rarely been economically sustainable in persistent commercial worlds.
- **Status:** **Essential/Supporting.**
- **Caution:** Counselors were primarily support/community staff, not all full narrative GMs. Use them as evidence for the labour economics of persistent human oversight, not as proof that every counselor performed tabletop-style adjudication.

#### Reab v. Electronic Arts, Inc. (2002)

- **Role:** Legal record.
- **Supports:** The UO Counselor Program became the subject of litigation alleging that structured volunteer work should have been compensated as employment; the court record identifies the program's formal schedules and its termination in 2001.
- **Enclave claim supported:** Volunteer labour is not a frictionless substitute for paid continuous staffing in a commercial persistent world.
- **Likely use:** §5 footnote or supporting citation if the wage/legal point is stated strongly.
- **Status:** **Supporting.**

### 9.2 The Matrix Online — unusually direct evidence of live-GM scaling limits

#### Thompson (2009), *Why MxO Live Content Worked*

- **Role:** First-person retrospective by a former *Matrix Online* Live Events Team member.
- **Supports:** An eight-person Live Events Team was only just sufficient to make live events manageable across nine servers. Scheduling across servers and regions sometimes required twelve- or fourteen-hour days; one major story event required the whole team to work fourteen hours a day for ten days. The article also describes the planning cycle, event preparation, and difficulty of reaching enough players.
- **Enclave claim supported:** Even a purpose-built commercial MMO with dedicated live storytellers incurred heavy recurring labour merely to provide periodic human-driven events, never mind continuous 24/7 D&D-style adjudication.
- **Likely use:** §5 core evidence.
- **Status:** **Essential.**
- **Key implication:** Coverage scales with human presence. A live actor can only inhabit so many characters, servers, time zones, and scenes at once.

#### Williams (2009), *Another Perspective on Live Content*

- **Role:** First-person retrospective by a former *Matrix Online* Live Events Gamemaster.
- **Supports:** Williams identifies scaling as the central failure mode of live events: finite human actors could not serve a large enough fraction of the player base to remain cost-effective while maintaining professional quality. He explicitly describes some one-on-one interactions as impressive but uneconomical and concludes that planning, staffing, and live execution made the model difficult to justify as a use of staffing dollars.
- **Enclave claim supported:** This is unusually direct practitioner evidence for the economic bottleneck behind persistent human gamemaster operations.
- **Likely use:** §5 core evidence; potentially conclusion/significance.
- **Status:** **Essential.**
- **Do not overclaim:** Williams is discussing live MMO events, not every possible persistent-world architecture. The value is that the same concurrency problem becomes even more severe for continuous individual adjudication.

### 9.3 Asheron's Call — even periodic world change imposed sustained production pressure

#### Park (2003), *Asheron's Call*

- **Role:** GameSpot feature/interview with producer Scott Herrington.
- **Supports:** Asheron's Call maintained an unusually dynamic persistent world through monthly world-changing events. Herrington described an eight-person event team operating under what amounted to permanent crunch, finishing one event and immediately beginning the next.
- **Enclave claim supported:** Even when human creative intervention is reduced from continuous adjudication to monthly authored world updates, sustained world responsiveness remains labour intensive.
- **Likely use:** §5 supporting example.
- **Status:** **Essential/Supporting.**
- **Important distinction:** Asheron's Call is closer to persistent **authored intervention** than persistent gamemaster adjudication. That distinction actually strengthens the argument: the less demanding model was still expensive in human effort.

### 9.4 Persistent worlds do exist; continuous human-GM coverage is the missing layer

Community persistent worlds such as *Neverwinter Nights* servers demonstrate that a world can remain online continuously and can support human DMs, live events, and long-lived roleplay communities. These cases frequently rely heavily on volunteer builders, writers, administrators, and DMs rather than commercially staffed 24/7 gamemaster coverage.

The safe claim for the paper is therefore:

> **Persistent simulations are technically achievable. What has historically been difficult to sustain is persistent, responsive human gamemastering at the granularity of tabletop play, because the world's availability can scale computationally while human adjudication scales with paid or volunteer labour hours.**

This creates an important Section 5 bridge into Enclave:
- automated game systems made persistent worlds economically possible by handling ordinary operation;
- human GMs remained valuable for ambiguity, exceptions, live narrative intervention, and world-level judgment;
- but continuous human availability does not scale with persistent online participation;
- probabilistic systems create the possibility of making some of those previously labour-bound gamemaster operations continuously available;
- authoritative deterministic systems can retain the world-integrity functions that should not be delegated wholesale to probabilistic inference.

---

### 9.5 Long-context access is not equivalent to reliable maintained state

#### Liu et al. (2024), *Lost in the Middle: How Language Models Use Long Contexts*

- **Role:** Peer-reviewed TACL study / direct evidence that information can remain inside context and still be used unreliably.
- **Supports:** Model performance depends strongly on where relevant information appears inside a long prompt; performance often drops substantially when needed information is located in the middle, including for models explicitly designed for long context.
- **Enclave claim supported:** Keeping a fact inside the nominal context window does **not** guarantee that the model will reliably retrieve or apply it. This directly supports §5.7.4's distinction between context availability and maintained state.
- **Likely use:** §5.7.4 *LLMs Are Poorly Suited to Maintaining State*.
- **Status:** **Essential.** This is the cleanest existing source for the claim that “the fact was in context” is not enough.
- **Do not overclaim:** The paper evaluates retrieval and question answering, not persistent simulated-world state. Use it to establish unreliable utilization of available context, not to claim that every model will forget every middle-position fact.

#### Bai et al. (2024), *LongBench: A Bilingual, Multitask Benchmark for Long Context Understanding*

- **Role:** Peer-reviewed ACL long-context benchmark.
- **Supports:** Across 21 datasets and multiple task types, evaluated models continued to struggle as contexts became longer; retrieval/context-compression methods help but do not eliminate long-context limitations.
- **Enclave claim supported:** Increasing nominal context size reduces one capacity constraint but does not make long-context understanding or state use uniformly reliable.
- **Likely use:** §5.7.4 as corroboration for Liu et al.; possibly §5.7.5 when motivating retrieval rather than full-history prompting.
- **Status:** **Essential/Supporting.**

#### Hsieh et al. (2024), *RULER: What's the Real Context Size of Your Long-Context Language Models?*

- **Role:** Widely used long-context benchmark / preprint.
- **Supports:** Models that perform nearly perfectly on simple needle-in-a-haystack retrieval can suffer large degradation as context length and task complexity increase. In the original 17-model evaluation, only about half maintained the paper's satisfactory-performance threshold at 32K despite all claiming context windows of at least 32K.
- **Enclave claim supported:** Advertised context capacity and effective usable context are different quantities; long contexts become especially unreliable when multiple pieces of information must be traced, aggregated, or related.
- **Likely use:** §5.7.4.
- **Status:** **High-value supporting source.**
- **Caution:** The original paper remains an arXiv publication. Pair with peer-reviewed Liu et al. and Bai et al. for the core claim.

#### Wu et al. (2025), *LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory*

- **Role:** Peer-reviewed ICLR benchmark / direct sustained-interaction memory evidence.
- **Supports:** Tests information extraction, multi-session reasoning, temporal reasoning, knowledge updating, and abstention across long interaction histories. The paper reports roughly a 30% accuracy drop for commercial assistants and long-context LLMs on memorizing information across sustained interactions. It explicitly decomposes long-term memory into **indexing, retrieval, and reading** stages and shows that memory-system design changes materially affect performance.
- **Enclave claim supported:** Long-running interaction cannot be reduced to “put the history in context.” Persistent memory becomes an information-management architecture involving indexing, retrieval, temporal scoping, and model reading accuracy.
- **Likely use:** §5.7.3–§5.7.5, especially the transition from persistent consequence to external memory and retrieval.
- **Status:** **Essential.** Probably the strongest new source for the Agency–Persistence Gap itself.

#### Packer et al. (2023), *MemGPT: Towards LLMs as Operating Systems*

- **Role:** Systems preprint / architectural precedent for external memory tiers.
- **Supports:** Treats limited LLM context as analogous to constrained working memory and moves information between in-context and external memory tiers to support document analysis and multi-session conversation beyond the native context window.
- **Enclave claim supported:** Externalizing memory is an established response to context limits, but doing so necessarily introduces explicit memory-management operations rather than eliminating the persistence problem.
- **Likely use:** §5.7.3–§5.7.5.
- **Status:** **Supporting.** Prefer LongMemEval for empirical long-term-memory claims.

### 9.6 External memory shifts the problem into indexing, retrieval, and relevance management

The combined evidence from Park et al. (2023), MemGPT, and LongMemEval supports a useful distinction for §5.7:

> **External storage solves capacity more readily than it solves relevance.** Once state exceeds active context, a system must decide what to store, how to represent it, how to index it, what to retrieve, how to resolve updates or contradictions, and what subset the model is allowed to read for the current operation.

This is important for Enclave because the paper should **not** argue that external memory is ineffective. The stronger point is that external memory converts one problem into a set of explicit information-management problems. LongMemEval's indexing/retrieval/reading decomposition is especially useful because it empirically demonstrates that these design choices materially affect downstream memory accuracy.

### 9.7 Naive persistence has unavoidable storage growth, and general-purpose databases add physical overhead

The asymptotic claim should be stated as an architectural consequence rather than attributed to a database paper:

> If each consequential interaction creates at least one retained event, record, or actor-memory reference and those records are not discarded, historical storage grows at least linearly with the number of consequential interactions: **O(N)**.

That claim does not require a database citation. Database documentation is useful for the **constant-factor amplification** around it.

#### PostgreSQL database page and tuple layout

- **Role:** Primary technical documentation.
- **Supports:** PostgreSQL heap rows have a fixed-size tuple header of about **23 bytes on most machines**, plus optional metadata and user data. Each stored item also consumes a **4-byte item identifier** on its page, while each page has a **24-byte page header**. Indexes add additional B-tree structures and therefore additional stored keys/pointers. PostgreSQL's own documentation explicitly notes that indexes improve retrieval but add overall system overhead.
- **Enclave claim supported:** Fine-grained persistent facts and relationships have physical bookkeeping costs beyond their semantic payload. A world containing enormous numbers of tiny state records may therefore spend substantial storage on representation, indexing, and addressing rather than only on narrative content.
- **Likely use:** §5.7.5 research note or footnote; later implementation/storage discussion if retained.
- **Status:** **Supporting / illustrative, not central.**
- **Do not overclaim:** This does **not** establish that PostgreSQL, SQL, or B-trees are unsuitable for Enclave. It only demonstrates that general-purpose structured storage has non-zero per-record/page/index overhead.

#### PostgreSQL TOAST documentation

- **Role:** Primary technical documentation.
- **Supports:** Large variable-length values may be compressed or moved out-of-line into secondary storage; an on-disk TOAST pointer itself occupies 18 bytes. This is another concrete example of indirection and storage-management metadata introduced by general-purpose persistence machinery.
- **Enclave claim supported:** Physical persistence can introduce additional references and metadata even where the logical datum is conceptually singular.
- **Likely use:** Storage-overhead note only.
- **Status:** **Background/Supporting.**

#### SQLite database file format

- **Role:** Primary technical documentation.
- **Supports:** SQLite stores tables and indexes as B-trees with page headers, per-cell pointer arrays, record headers, type varints, row identifiers, and optional overflow pages. Each SQL index corresponds to a separate index B-tree, with an entry corresponding to the indexed table row.
- **Enclave claim supported:** Storage overhead is not PostgreSQL-specific. Even a compact embedded database carries structural metadata for records, pages, keys, and indexes; indexing additional dimensions of narrative state duplicates some representational material in exchange for efficient retrieval.
- **Likely use:** §5.7.5 supporting footnote if a database example is useful.
- **Status:** **Supporting.**

**Safe §5.7.5 framing:**

- naive append-only persistence produces at least linear growth in retained history;
- actor-specific references, relationships, derived state, and indexes can add further growth and constant-factor amplification;
- storing state is only half the problem, because future operations must efficiently recover the *relevant* state from that growing corpus;
- avoid claiming that a particular database class is inherently incapable of handling the workload unless later benchmarking establishes that separately.

### 9.8 Human cognition supplies a useful analogue for the same flexibility–persistence tradeoff

#### Cowan (2001), *The Magical Number 4 in Short-Term Memory: A Reconsideration of Mental Storage Capacity*

- **Role:** Major cognitive-science review.
- **Supports:** Under controlled conditions, the focus of attention / short-term capacity is limited to roughly three to five chunks, with an average near four.
- **Enclave claim supported:** Human interpretive flexibility does not imply large active information capacity. Human Gamemasters also depend on selective attention, long-term memory, notes, rules texts, and other external aids rather than holding a complete world state actively in mind.
- **Likely use:** §5.7.7 *Fertile Ground*.
- **Status:** **Essential/Supporting.**

#### Oberauer et al. (2016), *What Limits Working Memory Capacity?*

- **Role:** Peer-reviewed Psychological Bulletin review.
- **Supports:** Working memory has robust capacity limitations; interference among representations provides a strong account of many observed limits.
- **Enclave claim supported:** Human active information management is constrained and interference-prone even though humans remain highly capable contextual interpreters.
- **Likely use:** §5.7.7 corroboration.
- **Status:** **Supporting.**

#### Schacter (2012), *Constructive Memory: Past and Future*; Schacter & Addis (2007), *The Cognitive Neuroscience of Constructive Memory*

- **Role:** Cognitive-neuroscience reviews.
- **Supports:** Human episodic memory is constructive rather than a literal replay of stored experience and is consequently susceptible to distortion and error; the same constructive machinery also supports flexible recombination and simulation of possible future events.
- **Enclave claim supported:** The comparison between human and machine interpretive systems should not be “humans have bad memory.” The more interesting parallel is that flexible reconstruction and improvisation coexist with imperfect exact recall.
- **Likely use:** §5.7.7.
- **Status:** **Essential/Supporting.**

#### Johnson, Hashtroudi, & Lindsay (1993), *Source Monitoring*

- **Role:** Foundational Psychological Bulletin review.
- **Supports:** Human judgments about the origin/source of remembered information are inferential and can be misattributed; source monitoring is flexible but error-prone.
- **Enclave claim supported:** Humans are not naturally reliable provenance databases. Exact tracking of who said what, where information originated, and whether something was perceived, inferred, or imagined requires cognitive work and is subject to error.
- **Likely use:** §5.7.7 when contrasting human interpretation with computational provenance/identity management.
- **Status:** **Supporting.**

#### *Balancing Flexibility and Interference in Working Memory* (2021)

- **Role:** Peer-reviewed Annual Review article.
- **Supports:** Working memory's ability to flexibly maintain arbitrary representations is paired with severe capacity limits; the review explicitly links flexibility and interference as consequences of the same underlying representational machinery.
- **Enclave claim supported:** This is an unusually apt conceptual analogue for §5.7.7's “Fertile Ground” argument: flexible cognition and exact large-scale maintenance are not simply independent virtues, and systems optimized for flexible representation may incur interference/capacity costs.
- **Likely use:** §5.7.7.
- **Status:** **High-value supporting source.**

### 9.9 Revised evidence map for §5.7

1. **The Agency** — Hogan & Brennen; Park et al.; Hu et al.
2. **Expanded Agency** — Hogan & Brennen; Park et al.; Alexander as human-GM precedent.
3. **The Persistence** — Park et al.; LongMemEval; MemGPT; existing state-space/branching literature.
4. **LLMs Are Poorly Suited to Maintaining State** — **Liu et al. (Lost in the Middle); Bai et al. (LongBench); Hsieh et al. (RULER); Wu et al. (LongMemEval).**
5. **Naive Applications Create Linear Storage Problems** — architectural O(N) argument; LongMemEval/MemGPT for the resulting retrieval problem; PostgreSQL and SQLite documentation for physical overhead examples.
6. **The Gap** — Enclave synthesis of the supported premises above; introduce *Agency–Persistence Gap* as the paper's own term.
7. **Fertile Ground** — Gao et al. (PAL); Kambhampati et al. (LLM-Modulo); Marra et al. (neuro-symbolic AI); Cowan, Schacter, Johnson et al. for the human cognition side of the complementary-strengths comparison.

The resulting argument is substantially better supported than the earlier version. The strongest empirical claim is no longer merely that LLM context is finite. It is that **even information still present inside a supported context window may be retrieved or applied unreliably, and sustained-interaction memory becomes a separate indexing/retrieval/reading problem once history grows.**

---

## 10. Section 6 research — sandbox capability, emergence, and the narrative asymmetry

Section 6 should make a narrower claim than “sandbox games have not solved narrative.” Existing sandbox and simulation-heavy games plainly produce rich **emergent narrative**. The stronger distinction is between:

1. **systemic emergence** — rules, objects, agents, and mechanics combine to produce world states and events that were not individually authored;
2. **player-constructed/emergent narrative** — players interpret those events as meaningful stories;
3. **deeply authored narrative responsiveness** — pre-authored characters, conflicts, information, themes, and intended developments absorb unanticipated systemic events as persistent inputs and continue responding coherently.

Enclave is primarily concerned with the third problem while building on the first two.

### 10.1 Juul (2002), *The Open and the Closed: Games of Emergence and Games of Progression*

- **Role:** Foundational game-studies theory / primary conceptual source for §6.1–§6.3.
- **Publication:** *Computer Games and Digital Cultures Conference Proceedings*, Tampere University Press / DiGRA, 2002. DOI: 10.26503/dl.v2002i1.9.
- **Supports:** Distinguishes **emergence**, where a relatively small set of rules combines to produce large amounts of variation, from **progression**, where serial challenges and solutions are explicitly prescribed. Juul applies the distinction to *EverQuest*, describing it as an open/emergent world containing progression-based quests.
- **Enclave claim supported:** Broad systemic possibility does not require designers to enumerate every resulting world state. A finite ruleset can create very large spaces of valid play. At the same time, progression-oriented narrative structures can remain comparatively prescribed inside an emergent world.
- **Likely use:** §6.1 existing sandbox capability; §6.2 genuine emergence; §6.5 world/narrative asymmetry.
- **Status:** **Essential.**
- **Do not overclaim:** Juul does not argue that sandboxing is “solved,” nor does he provide Enclave’s narrative-state architecture. His emergence/progression distinction is the useful precedent.

### 10.2 Soler-Adillon (2019), *The Open, the Closed and the Emergent: Theorizing Emergence for Videogame Studies*

- **Role:** Peer-reviewed *Game Studies* theoretical refinement.
- **Supports:** Distinguishes openness from emergence more carefully than a simple open/closed binary; treats games as possibility spaces whose systemic interactions can produce self-organization or novelty.
- **Enclave claim supported:** Sandbox capability should be described as a bounded possibility space rather than literal unlimited freedom. “Open” and “emergent” are related but not identical.
- **Likely use:** §6.1–§6.3, especially the bounded-interaction-vocabulary caveat.
- **Status:** **Essential/Supporting.**
- **Do not overclaim:** Use this to sharpen terminology, not to claim all open-world games are emergent in the strict theoretical sense.

### 10.3 Ryan (2018), *Curating Simulated Storyworlds*

- **Role:** Doctoral dissertation / major computational-narrative treatment of emergent narrative.
- **Supports:** Defines a major emergent-narrative approach as simulating a storyworld and allowing narrative to arise from character activity rather than directly generating a pre-specified story. Discusses *The Sims* and *Dwarf Fortress* as important successful examples.
- **Enclave claim supported:** Simulation-heavy worlds can already produce meaningful stories from events that were not individually scripted. This demonstrates that narrative can arise from systemic state change without a pre-authored branch sequence.
- **Likely use:** §6.2 and §6.5.
- **Status:** **Essential/Supporting.**
- **Important distinction:** Ryan is strong evidence that **emergent narrative exists**. Enclave should therefore distinguish emergent/player-interpreted narrative from persistent responsiveness of deeply authored narrative structures.

### 10.4 Adams (2021), *Characterization and Emergent Narrative in Dwarf Fortress*

- **Role:** Primary practitioner chapter by the creator of *Dwarf Fortress*.
- **Publication:** In Suter, Bauer & Kocher (eds.), *Narrative Mechanics: Strategies and Meanings in Games and Real Life*, pp. 151–160. DOI: 10.1515/9783839453452-007.
- **Supports:** Practitioner account of characterization and emergent narrative in one of the canonical simulation-heavy games.
- **Enclave claim supported:** Rich character- and event-driven stories can emerge from interacting simulation systems without those stories being authored as explicit branches.
- **Likely use:** §6.2 / §6.5 as a concrete practitioner example.
- **Status:** **Supporting.**

### 10.5 Burgess & Jones (2023), *Exploring how players use emergent narrative in strategy games*

- **Role:** Peer-reviewed empirical study in *Entertainment Computing* 44, 100533. DOI: 10.1016/j.entcom.2022.100533.
- **Supports:** Analysis of 295 forum posts and 104 survey respondents around the *Total War* series found that players created detailed emergent narratives, used them to provide context and motivation, and developed strong emotional attachment to units and characters.
- **Enclave claim supported:** Systemic gameplay can produce narratives that players experience as meaningful even when those narratives are not supplied through a linear authored story.
- **Likely use:** §6.2 and §6.5.
- **Status:** **Essential/Supporting.**
- **Do not overclaim:** The paper demonstrates player-created/emergent narrative, not a system in which a deeply authored plot automatically incorporates every emergent event.

### 10.6 Evans (2024), *Too Afraid to Go Deeper: Creating Pervasive Dread Through Blended Design Structures in Subnautica and Subnautica: Below Zero*

- **Role:** Peer-reviewed *Game Studies* analysis / already present elsewhere in the Enclave source set.
- **Supports:** Characterizes a common modern open-world form as mechanically complex and freely explorable while narrative often centers on a comparatively linear main plot plus optional side quests.
- **Enclave claim supported:** World/systemic openness and narrative openness are separable dimensions. A highly sandboxed or open world can coexist with much more constrained authored narrative progression.
- **Likely use:** §6.5.
- **Status:** **Essential for the modern open-world asymmetry.**

### 10.7 Johnson-Bey, Nelson, & Mateas (2022), *Neighborly: A Sandbox for Simulation-Based Emergent Narrative*

- **Role:** Peer-reviewed IEEE Conference on Games system paper. DOI: 10.1109/CoG51982.2022.9893631.
- **Supports:** Presents a customizable community-scale social-simulation engine explicitly intended as a **sandbox for simulation-based emergent narrative**, reconstructing and generalizing the earlier *Talk of the Town* system.
- **Enclave claim supported:** “Narrative sandbox” and simulation-based emergent storytelling are established computational-narrative research directions rather than terminology invented solely for Enclave.
- **Likely use:** §6.2 and §6.6.
- **Status:** **Essential/Supporting.**
- **Do not overclaim:** Neighborly is a social-simulation authoring tool, not Enclave’s architecture for persistent authored narrative authority, information provenance, or reactive event structure.

### 10.8 Grinblat, Manning, & Kreminski (2021), *Emergent Narrative and Reparative Play*

- **Role:** Peer-reviewed ICIDS chapter, *Interactive Storytelling*, pp. 208–216. DOI: 10.1007/978-3-030-92300-6_19.
- **Supports:** Explicitly discusses **narrative sandbox games** as games that rely heavily on emergence to create narrative effects and examines how players construct meaning from deliberately incomplete artifacts and systemic output.
- **Enclave claim supported:** Narrative sandboxing already exists as a meaningful category, particularly where emergence and player interpretation produce narrative effects.
- **Likely use:** §6.5–§6.6.
- **Status:** **Supporting.**
- **Important distinction:** Their use of “narrative sandbox” is broader than Enclave’s specific goal. Enclave should define its narrower interest in persistent, deeply authored narrative structures reacting to emergent events.

### 10.9 Existing Enclave sources that carry directly into Section 6

#### Jenkins (2004), *Game Design as Narrative Architecture*
- Worlds and spaces can contain authored narrative information and affordances.
- Useful for the bridge from systemic world design toward authored narrative embedded in the world.
- **Likely use:** §6.5–§6.6.

#### Louchart, Swartjes, Kriegel, & Aylett (2008), *Purposeful Authoring for Emergent Narrative*
- Emergent narrative can be treated as an **authoring problem**: what should deliberately be specified when the realized sequence is not fixed?
- Strong precedent for §6.6’s question of how human authorship can survive emergence.
- **Likely use:** §6.6.
- **Status:** **Essential.**

#### Short (2019) and Failbetter Games
- State-conditioned storylets demonstrate that authored narrative material can already be made available, disabled, or altered according to mutable state.
- **Likely use:** §6.5–§6.6 as practical precedent for authored narrative responding to world conditions.

#### Chen, Nelson, & Mateas (2009)
- Authorial leverage provides a way to evaluate whether systemic/runtime machinery increases meaningful narrative possibility relative to authoring effort.
- **Likely use:** §6.6.

#### Fisher (2022); Porteous et al. (2021); Hayton et al. (2020); Iovino et al. (2022)
- Existing Section 4 research establishes that computational possibility remains bounded by represented states, actions, predicates, behaviors, and models.
- **Likely use:** §6.3 to keep “sandbox freedom” technically bounded rather than treating it as unrestricted action.

### 10.10 Recommended Section 6 claim boundary

The evidence supports the following formulation:

> **Sandbox and simulation-heavy games have already demonstrated that authored systems can support very large spaces of emergent world state and can generate rich emergent narratives without designers enumerating every resulting event. The remaining asymmetry is that deeply authored narrative structures are usually less able than the surrounding simulation to absorb arbitrary emergent events as persistent, semantically meaningful inputs.**

This is stronger and safer than claiming that games have “solved world sandboxing but not narrative” without qualification.

The section should explicitly distinguish:

- **systemic emergence** — unenumerated outcomes arise from represented rules and mechanics;
- **emergent/player-authored narrative** — players construct meaningful stories from those outcomes;
- **reactive authored narrative** — existing authored characters, information, conflicts, events, and trajectories continually reinterpret and respond to those outcomes.

Enclave’s contribution is primarily aimed at the third category.

---

## 11. Section 12 — Actor Cognition: citation map

This section reuses the existing corpus wherever possible. The strongest supporting literature is already present in the project and covers four distinct needs: persistent agent memory, bounded/asymmetric information, long-context/retrieval limits, and hybrid probabilistic/deterministic execution.

### 11.1 Persistent Cognitive Actors and memory outside one invocation

#### Park et al. (2023), *Generative Agents: Interactive Simulacra of Human Behavior*

- **Existing source; promoted for §12 use.**
- **Supports:** persistent natural-language memory streams, retrieval, reflection, and planning used by long-lived agents in an interactive environment.
- **Likely use:** §12.1–§12.4 and §12.6.
- **Claim boundary:** supports persistent agent state and memory-driven behavior, not Enclave's authority model or exact Actor ontology.

#### Packer et al. (2023), *MemGPT: Towards LLMs as Operating Systems*

- **Existing source; supporting precedent.**
- **Supports:** explicit separation of limited active context from external persistent memory and movement of information between them.
- **Likely use:** §12.2, §12.4, §12.5.
- **Claim boundary:** architectural precedent rather than direct evidence for narrative Actors.

#### Wu et al. (2025), *LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory*

- **Existing source; essential for §12.**
- **Supports:** sustained interaction requires indexing, retrieval, reading, temporal reasoning, and knowledge updating; long-term memory quality depends materially on memory-system design.
- **Likely use:** §12.2, §12.4, §12.5, §12.7.
- **Claim boundary:** evaluates long-term assistant memory, not Enclave's world-state authority.

### 11.2 Bounded perspective and asymmetric information

#### Hogan & Brennen (2024), *Open-Ended Wargames with Large Language Models*

- **Existing source; high-value analogue.**
- **Supports:** agents can receive personas, differentiated textual histories, and asymmetric information while proposing open-ended actions.
- **Likely use:** §12.1, §12.3, §12.6.
- **Claim boundary:** the system does not provide Enclave's persistent epistemic-state or Event-authority model.

#### Hu et al. (2024; revised 2026), *A Survey on Large Language Model-Based Game Agents*

- **Existing source; field-level support.**
- **Supports:** memory, reasoning, perception-action interaction, adaptability, coordination, and open-ended goal formation are established design concerns in LLM-based game agents.
- **Likely use:** §12.1, §12.3.
- **Claim boundary:** broad survey evidence, not support for Enclave's specific epistemic boundary.

### 11.3 Long context, retrieval, and selective attention

#### Liu et al. (2024), *Lost in the Middle: How Language Models Use Long Contexts*

- **Existing source; essential.**
- **Supports:** information can remain inside the nominal context window while still being used unreliably, especially depending on position.
- **Likely use:** §12.5.
- **Enclave relevance:** directly supports the distinction between persistent availability and present effective attention/use.

#### Bai et al. (2024), *LongBench: A Bilingual, Multitask Benchmark for Long Context Understanding*

- **Existing source; supporting.**
- **Supports:** longer nominal contexts do not eliminate long-context understanding limitations; retrieval/compression methods remain useful.
- **Likely use:** §12.5.

#### Hsieh et al. (2024), *RULER: What's the Real Context Size of Your Long-Context Language Models?*

- **Existing source; supporting.**
- **Supports:** effective usable context can be materially smaller than nominal context, especially for more complex retrieval/aggregation tasks.
- **Likely use:** §12.5.

### 11.4 Divided cognitive responsibility and external validation

#### Gao et al. (2023), *PAL: Program-Aided Language Models*

- **Existing source; strong architectural precedent.**
- **Supports:** probabilistic interpretation/decomposition can be separated from exact conventional execution.
- **Likely use:** §12.6–§12.7.
- **Claim boundary:** mathematical/symbolic task domain, not narrative simulation.

#### Kambhampati et al. (2024), *Position: LLMs Can't Plan, But Can Help Planning in LLM-Modulo Frameworks*

- **Existing source; strong architectural precedent.**
- **Supports:** LLM proposal/knowledge generation can be wrapped in external model-based validation and reasoning.
- **Likely use:** §12.6–§12.7 and the §12→§13 authority seam.
- **Claim boundary:** planning framework rather than persistent narrative state.

#### Marra et al. (2024), *From Statistical Relational to Neurosymbolic Artificial Intelligence: A Survey*

- **Existing source; field-level support.**
- **Supports:** combining statistical/neural flexibility with symbolic reasoning is an established broader architectural direction.
- **Likely use:** §12.7.
- **Claim boundary:** general hybrid-AI precedent only.

### 11.5 Episodic/semantic memory analogy

#### Tulving (2002), *Episodic Memory: From Mind to Brain*

- **Role:** peer-reviewed review article in *Annual Review of Psychology*, 53:1–25. DOI: 10.1146/annurev.psych.53.100901.135114.
- **Supports:** episodic memory as memory for personally experienced events, distinct from semantic/general knowledge.
- **Likely use:** §9.3 and §12.4.
- **Status:** **Essential/Supporting analogy.**
- **Claim boundary:** human-memory theory is an analogy for Enclave's Memory/Knowledge distinction, not proof that agent memory should copy human neurocognition.

#### Greenberg & Verfaellie (2010), *Interdependence of Episodic and Semantic Memory: Evidence from Neuropsychology*

- **Role:** peer-reviewed review in *Journal of the International Neuropsychological Society*, 16(5):748–753. DOI: 10.1017/S1355617710000676.
- **Supports:** distinction and interdependence between event/episodic memory and general/semantic knowledge.
- **Likely use:** §9.3 and §12.4.
- **Status:** **Supporting.**
- **Claim boundary:** supports the conceptual analogy, not the Memory Classification pipeline itself.

### 11.6 Training-data memorization and narrative leakage

#### Chang, Cramer, Soni, & Bamman (2023), *Speak, Memory: An Archaeology of Books Known to ChatGPT/GPT-4*

- **Role:** peer-reviewed EMNLP 2023 paper, pp. 7312–7327. DOI: 10.18653/v1/2023.emnlp-main.453.
- **Supports:** the evaluated models exhibited memorization of a wide collection of published/copyrighted books, with memorization related to how frequently passages appeared on the web.
- **Enclave claim supported:** runtime epistemic isolation cannot guarantee that a pretrained third-party model lacks latent knowledge of a published narrative source.
- **Likely use:** §12.1 training-data caveat.
- **Status:** **Essential for this caveat.**
- **Claim boundary:** establishes memorization/latent source knowledge, not that every model contains every publication or that mitigation is impossible.

#### Carlini et al. (2021), *Extracting Training Data from Large Language Models*

- **Role:** peer-reviewed 30th USENIX Security Symposium paper, pp. 2633–2650.
- **Supports:** large language models can memorize and expose verbatim examples from training data under querying.
- **Enclave claim supported:** general evidence that model parameters can retain training-source information independently of runtime context.
- **Likely use:** §12.1 training-data caveat as corroboration.
- **Status:** **Supporting.**
- **Claim boundary:** GPT-2 extraction/security study; not specifically a narrative or book-knowledge experiment.

### 11.7 Dwarf Fortress / deterministic simulation precedent

Existing Section 6 sources carry directly into §12.1:

- Ryan (2018), *Curating Simulated Storyworlds*;
- Adams (2021), *Characterization and Emergent Narrative in Dwarf Fortress*.

Use these only to support the claim that rich narrative can emerge from simulation-heavy/procedural systems without requiring LLM cognition. The statement that Enclave itself could be implemented deterministically remains an architectural property of Enclave rather than an empirical claim supplied by these sources.

### 11.8 Section 12 claim boundary

The literature supports the following surrounding claims:

- persistent external memory and retrieval are established agent-system patterns;
- long nominal context does not guarantee reliable use of all available information;
- agent systems can operate from differentiated histories and asymmetric information;
- probabilistic interpretation can be coupled to external deterministic/symbolic execution and validation;
- pretrained models may retain information from published source material.

The following remain **Enclave synthesis** and should not be attributed to those sources as prior art without qualification:

- the exact three-scope model of world state → Actor subjective state → active context;
- Enclave's epistemic authority boundary;
- the Memory Classification pipeline;
- the specific Cognitive Cycle;
- the separation among Enclave, Memory system, and narrative-agent jurisdiction;
- the rule that Actor cognition selects an attempted action while the authoritative system owns the accepted Event.

---

## 12. Publication bibliography rule

The bibliography in `docs/design-paper.md` should remain a normal publication bibliography: clean citation records, alphabetized by author/organization, without these annotations.

This file is the place to preserve research intent, claim mapping, source status, and cautions so those do not get lost during drafting.
