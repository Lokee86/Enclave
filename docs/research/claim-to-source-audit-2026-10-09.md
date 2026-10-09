# Enclave claim-to-source audit — 2026-10-09

## Scope and evidence standard

The audit uses the **current 17-section outline** in docs/paper-outline.md, not the older numbered structure in docs/design-paper.md. The separate machine-readable subsection inventory covers every numbered subsection and identifies the principal supporting citation lines. This document contains **all 61 reference-tagged subsection assessments** and makes **focused, source-specific substantive judgments**, with the strongest attention to consequential empirical and historical claims; it is not a certification that every sentence of the manuscript is verified.

Four different evidentiary relationships must not be conflated:

1. **Direct support:** a primary paper or publisher/author text demonstrates the claimed finding within a defined study, example, or system.
2. **Bounded / analogical support:** the source establishes a narrower phenomenon or useful comparison but not the full breadth of the statement.
3. **Architectural proposal / logical derivation:** Enclave defines an intended rule, ontology, or consequence. Literature can provide precedent, not evidence that Enclave already works.
4. **Conditional model / transfer:** a calculation follows stipulated assumptions or measurements from another system. These are not benchmarks of an implemented Enclave.

**Important limitation:** The 92-entry verification ledger establishes bibliographic identities. This separate source-to-claim pass read accessible primary **abstracts, article text and practitioner pages**, plus the repo's source ledger and computational assumptions, for high-impact citations. It did not comprehensively read and replicate all 92 full texts. Source-access limits for referenced subsections are stated in the consolidated register below; further evidence needs for the other 78 subsections are separately classified.

## Actionable findings — complete priority register

This table is an **action register**, not a list of changes authorized to the paper. It consolidates actionable source/claim limits, research gaps, validation tasks, publication checks and lower-priority attribution issues from the **61 cited-subsection assessments**, the continued review and the **78 untagged-subsection triage**. Related locations share a row when the same action addresses them. Priority indicates risk of overclaiming, not a requirement to rewrite the outline. **The outline remains unchanged.**

| Priority | Outline / scope | Finding or evidence limit | Recommended action |
|---|---|---|---|
| High | §4.6 | **Research pass completed (2026-10-09):** Roth et al. (2012) found *increased* perceived effectance on a second *Façade* exposure; Roth & Vermeulen (2013) found changed player behavior; Fendt et al. (2012) and Cardona-Rivera et al. (2014) studied agency under differently consequential choices, but **none tested perceived-agency decline after discovering reconvergence on replay**. | **Open empirical claim:** do not present declining agency across replays as a measured general law. Keep the reconvergence-discovery effect as a conditional hypothesis unless directly tested. See focused §4.6 resolution below. **Outline not edited.** |
| High | §§3.10, 4.7 | **Research R2 complete; approved §3.10 expansion shipped (2026-10-09).** Hayton (2020) and Porteous (2021) document narrative-domain authoring costs; pre-LLM Bayesian/story/dialogue work disproves universal absence of probabilistic inference. Cooper (1990), Dagum & Luby (1993) and Das (2004) establish additional general-network computational and parameter-acquisition burdens. | **§3.10 editorial correction resolved.** The approved revision distinguishes formal-domain construction from probabilistic implementation costs, with their respective limitations. **§4.7 remains unchanged**, pending independent editorial consideration; neither general commercial non-adoption nor general-purpose modern reliability is established. See R2 and bibliography notes §8.7. |
| High | §§6.6, 7.7 | **R4 comparative research completed (2026-10-09); originality remains qualified.** Concordia, Comme il Faut/Prom Week, Versu and newer Sonder/Bunnyland implementations already cover substantial parts of natural-language action resolution, autonomous authored-social narrative, actor-local observations, persistent authoritative state and event commit. DEL, event sourcing, ReBAC/ABAC and database provenance independently precede component mechanisms. No demonstrated *exclusive* missing capability is established. | **Partially resolved:** cite the closest precedents explicitly; define Enclave's distinct *combination and contracts* (authored trajectory + causal Event authority + epistemic distribution + group/saturation rules). Compare by feature and evidence level, not claims of invention. Uniqueness, full integration and practical gains remain unproven without a detailed specification/implementation. See focused R4 below. **Outline unchanged.** |
| High | §§8, 11, 12.3 | Knowledge access, Actor-local epistemic isolation, propagation, saturation and provenance are **design invariants**, not proven protections. | Specify access/transmission semantics and test unauthorized disclosure, contradictory beliefs, inheritance, source provenance and saturation edge cases. |
| High | §§10.3–10.7 | Combinatorial Enclaves, Rank, Facets and Inheritance have unproven semantics, pruning/complexity bounds and membership correctness. | Give formal definitions and complexity assumptions; prove or test conjunction, inheritance reduction, permission evaluation and adversarial edge cases. |
| High | §§12.6–12.7, 13.1–13.7 | The proposed cognitive-to-Event validation/commit boundary and persistent causal continuation have not been verified end to end. | Build an executable reference or formal model and test Event legality, ordering, world-state consistency, failed Interactions and downstream consequences. |
| High | §§15–16 | Reliquary/Arcana measurements, derived scenarios, model-serving prices and Enclave performance forecasts are different kinds of evidence. | Label measured subsystem results, assumptions, arithmetic and Enclave projections separately; require end-to-end tests before feasibility claims. |
| Medium | §§2.1–2.3 | Human/LLM comparisons generalize beyond sampled idea-generation tasks, narratives, models or reader evaluations. | Limit Wang, Sourati, Tian, Marco and Xu claims to their tested populations, tasks and measures; do not claim universal narrative superiority. |
| Medium | §§2.8, 4.5, 4.13, 6.5 | **R3 partially resolved:** broad literature, author interviews and a 20-title mission study corroborate reconvergence, quest hierarchies and sandbox/narrative tensions, but do **not** measure industry-wide prevalence or cross-quest authored reactivity. | Incorporate vetted R3 sources; keep “commonly/usually” qualified and refrain from universal incapability claims. See focused resolution R3 below. |
| Medium | §3.9 | Drama-manager authorial-leverage studies do not measure Enclave's authoring labour or creative output. | Distinguish the established evaluation criterion from Enclave's proposed leverage; test actual authoring effort before asserting gains. |
| Medium | §4.16 | Ultima Online counselor duties and Matrix Online retrospective live-event accounts do not quantify general GM staffing requirements. | Keep the human-oversight cost analogy specific to the studied programs; seek independent labour data for numerical scaling claims. |
| Medium | §§4.17, 5.1–5.2 | Generative Agents and Snow Globe show **bounded** interaction and agent coordination, not human-GM parity or unrestricted agency. | Frame concurrency, action interpretation and GM analogy as conditional; evaluate supervision, latency, reliability and persistent-world scale. |
| Medium | §§1.2, 5.4 | Long-context/memory studies demonstrate failures for tested models and tasks, not universal model inability. | Give the relevant test conditions and distinguish context failure, memory errors and authoritative state maintenance. |
| Medium | §§5.7, 9.3, 12.4 | Human working/episodic/semantic-memory research is an analogy, not validation of machine mechanisms or Enclave's Memory primitive. | Separate human-memory findings, existing agent-memory implementations and Enclave-specific claims. |
| Medium | §12.1 | Model memorization/extraction evidence shows a possible training-data leakage route, not inevitable scenario spoilers. | Present leakage as a tested risk under specific conditions; distinguish model-parameter memorization from runtime Actor knowledge controls. |
| Medium | §12.5 | No cited benchmark validates Enclave's context selection, relevance weights, breadth or assembly order. | Identify the exact policy as a design proposal and benchmark retrieval quality, legitimate access, cost and position/length effects. |
| Medium | §§5.3, 5.5 | Storage and retained-history estimates depend on record size/retention; no source measures Enclave bytes per meaningful Interaction. | State O(N) assumptions and distinguish database overhead from measured Enclave workloads; benchmark retention, indexing and deduplication. |
| Medium | §§4.12, 4.14 | State-space and persistent-world scaling claims depend on enumerated variables, pruning and concurrency; exact bounds are not provided by narrative citations. | Specify the counted object, possible combinations, inheritance reduction and workload conditions before using numerical complexity claims. |
| Medium | §§6.1, 6.4 | Sandbox maturity and whether persistence is the central limitation are interpretive judgments, not measured industry-wide results. | Describe documented systemic capabilities and narrow the comparison; avoid asserting that world sandboxing or persistence is solved. |
| Medium | §§14.1–14.11 | *A Wild Sheep Chase* and *Signals* divergent trajectories are authored counterfactuals, **not** recorded playtests or Enclave runs. | Label all walkthrough branches as thought experiments until implemented and evaluated. |
| Medium | §15.5 | Reliquary Freshness and Arcana timings are from distinct graph/retrieval systems, not authoritative Enclave Event throughput. | Keep source workload, configuration and provenance attached; measure actual Event processing and actor fan-out before transferring timings. |
| Medium | §15.8 | GPU and hosted inference prices are dated tariffs; price per hour is not evidence of model throughput or quality. | Recheck published provider rates at release, date every quote, and pair cost estimates with independently measured serving throughput. |
| Medium | §15.9 | NVIDIA DGX Spark throughput figures require reproducible primary-source/configuration provenance. | Record exact benchmark URL, model, quantization, hardware, input/output lengths, batch size and measurement conditions; avoid treating as Enclave measurements. |
| Medium | §15.10 | Manhattan population/storage/inference projections are linear extrapolations, not observed city behavior or capacity tests. | Recheck Census baseline, rates, arithmetic, time horizon, concurrency and excluded overhead; keep all assumptions explicit. |
| Medium | §16.6 | Three-level and hybrid *Signals* savings (85.6%, 82.6%, 85.7%) are **within-model**, not measured acceleration or retained narrative quality. | Keep approved outline text untouched; qualify the cost comparison in eventual manuscript prose/figures and validate against implementation when available. |
| Low | §§1.1–1.2, 7.1, 13.2–13.3, 17.1 | Uncited literature syntheses/restatements rely on evidence developed in other sections. | Add internal cross-references to authorial burden, model/authority failures, sandbox precedents and bounded action vocabularies; do not invent fresh citations. |
| Low | §§1.3–1.4, 2.4, 2.11, 17.2, 17.5 | Human-authorship commitments, objectives and closing architecture claims are normative or authorial positions. | Keep them labeled as thesis or intent, not independently measured necessities or established outcomes. |
| Low | §2.2 | Tian studies evaluated story properties; Marco studies readers' evaluation priorities. | Attribute each result to its own study and avoid treating distinct measures as interchangeable. |
| Low | §2.5 | Hammond supports the agency/coherence problem, not an experimental necessity theorem for 'meaningful response'. | Mark the requirement as Enclave's design principle or find a study directly testing that proposition. |
| Low | §2.6 | The narrative-paradox source uses expert elicitation; it does not validate an engine solution. | Use Louchart & Aylett for the problem framing, not claims that a technical remedy works. |
| Low | §§2.7, 4.1–4.3 | Branching and authorial-burden research supports representation costs, but not a universal growth curve or theorem for every narrative. | Separate mathematical examples and Enclave's 'branching tax' synthesis from the empirical findings of Jones and planning research. |
| Low | §2.9 | Perceived agency can change without expanding the underlying action vocabulary. | Keep theoretical agency, perceived agency and observed story reconvergence distinct when citing Day/Zhu, Thue and Stang. |
| Low | §2.10 | The conclusion that constraints affect both author and Participant is an inference from source-documented authoring limits. | Present the two-sided consequence as Enclave's synthesis, not an independent study outcome. |
| Low | §§3.1–3.7 | Narrative architecture, situation prep, node design, proactive antagonists and storylets are genuine **practitioner precedents**, not validated Enclave modules. | Credit the underlying methods while separating world-authoring precedents from proposed canonical Knowledge, causal validation and autonomous Actors. |
| Low | §3.8 | Louchart's purposeful emergent narrative uses bounded authored action ranges and local drama management. | Explain that prior-art boundary and the specific ways Enclave aims to extend interpretation, without claiming the prior approach was equivalent. |
| Low | §4.4 | Behavior-tree/FSM research identifies trade-offs, not blanket failure of established control systems. | Retain conventional controllers/planners as useful foundations and accurately describe their limits. |
| Low | §4.8 | Existing agent demonstrations do not establish unrestricted interpretation of arbitrary participant actions. | Scope probabilistic flexibility to demonstrated environments and supported action types. |
| Low | §§4.9–4.11, 5.8 | PAL, LLM-Modulo and neurosymbolic work establish partial execution/verifier precedents, not Enclave's authoritative narrative pipeline. | Attribute modular execution and verification to those sources; label the full proposal/validation architecture as Enclave's untested transfer. |
| Low | §4.15 | Human-GM scenario prep is practitioner guidance, not machine-scale performance evidence. | Use the tabletop comparison as analogy, not AI-equivalence proof. |
| Low | §5.6 | The 'Agency–Persistence Gap' is the paper's own analytic synthesis. | Explicitly attribute the label and whole construct to this paper; cite component-level evidence separately. |
| Low | §§6.2–6.3 | Emergent sandbox examples establish behavior from implemented rules, not a measured universal ceiling on action vocabularies. | Describe 'bounded interaction vocabulary' as an architectural inference and avoid invented quantitative maxima. |
| Low | §§7.2–10.2, 11, 13 | Primitives, authority layers, diffusion rules and causal semantics are original definitions, not empirical findings. | Check internal semantic consistency and label them proposed rules; citations are not required merely to define a primitive. |
| Low | §12.2 | Park and MemGPT show externalized memory patterns but not a proven persistent Enclave Actor lifecycle. | Use them for architectural precedent only, reserving lifecycle reliability claims for tests. |
| Low | §12.8 | Reliquary is optional proposed infrastructure and its performance claims are internal to its tested workloads. | Cite versioned Reliquary design/benchmark artifacts; do not infer Enclave-wide results. |
| Low | §13.8 | Event-driven processing is a proposed optimization, not an established efficiency result. | Benchmark scheduling, change localization, fan-out and re-evaluation rates before making cost/performance promises. |
| Low | §§14.2, 14.7 | Published adventures are source material rather than evidence of Enclave operation; reproductions may carry additional rights obligations. | Check licensing/permissions for reproduced story text or imagery separately from bibliographic attribution. |
| Low | §§15.1–15.4, 15.6–15.7 | Population, records, tokens and storage figures are conditional first-order model calculations. | Link each number to calculation files, units, input assumptions and exclusions; distinguish model outputs from deployment requirements. |
| Low | §§16.1–16.5 | Reactive Dialogue, Persistent Characters and hybrid Cognitive Actor tiers are proposed deployment patterns. | Present the taxonomy as design options until costs and quality are tested in a working implementation. |
| Low | §§17.3–17.4 | Projected narrative responsiveness and enforced reliability remain future consequences of the proposal. | Retain prospective wording and avoid implying guaranteed narrative quality, reliability or security. |
| Low | Methodology / multiple sections | Some claims were reviewed only against abstracts, snippets or selected pages rather than full methods/results. | Review full texts before relying on fine methodological detail; keep access limitations attached to individual findings. |
| Low | Research bibliography | **Integration completed 2026-10-09:** Jones & Millard (2026) extends the 2024 authorial-burden research stream and explicitly discusses why the single-exposure illusion-of-agency finding may not generalize to replay. | Added the 2026 journal article to the bibliography, noted its relationship to the 2024 paper, and cited §7.5.1 in Appendix D. Treat as critical synthesis, **not independent replay-decay evidence**. |

Actions requiring a change to published prose are recommendations for subsequent editorial review; they were **not** applied to `docs/paper-outline.md`. Findings supported by existing evidence and requiring no additional action remain documented in the subsection assessments below. The [78-subsection source-needs triage](claim-to-source-no-support-triage-2026-10-09.md) retains each untagged subsection's individual classification.
## Focused research resolution R1 — §4.6: repeated play, reconvergence and perceived agency (2026-10-09)

**Question actually being tested by the audit:** Does perceived agency generally diminish across successive playthroughs *because a player discovers that divergent choices reconverge or leave important downstream state unchanged*? This combines three distinct propositions: (i) designers can present meaningful-seeming choices without enduring causal divergence; (ii) on replay, players can discover that limitation; and (iii) the discovery diminishes perceived agency. Evidence for one step does not establish all three.

**Disposition:** **Unsupported as a general empirical replay-effect claim; plausible as a conditional hypothesis; research search completed but direct longitudinal evidence remains missing.** The strongest direct replay experiment found an increase, not a decline, in perceived effectance from first to second exposure. The relevant first-play branching studies establish why choice feedback and distinguishable outcomes matter, but they do not measure the effect of *discovering reconvergence across playthroughs*. This is not a refutation of that more specific hypothesis.

| Source and access | Design and verified finding | What it does **not** establish |
|---|---|---|
| **Roth, Vermeulen, Vorderer & Klimmt (2012),** [*Exploring Replay Value*](https://doi.org/10.1089/cyber.2011.0437), *Cyberpsychology, Behavior, and Social Networking*, 15(7), 378–381. **Journal abstract and full results/methodology reproduced in the first author's [doctoral dissertation](https://research.vu.nl/ws/portalfiles/portal/42167962/complete%20dissertation.pdf), chapter 5, pp. 111–123 (especially Table 5.1, p. 115).** | **N=50;** same players exposed to *Façade* twice. Perceived **effectance** rose **3.00 → 3.41** (paired comparison **p=.030**, reported significant after the study's false-discovery-rate procedure); flow **2.86 → 3.22** (**p=.001**); usability **3.66 → 3.99** (**p=.001**). Suspense (**p=.860**) and enjoyment (**p=.690**) did not significantly change. **Presence p=.060 was marginal before, and not significant after, multiple-comparison correction**; avoid saying presence was significantly increased. | Not a randomized reconvergence-discovery manipulation; only two short exposures to **one** system; *effectance* is an agency-related experience scale, not objective narrative divergence. Positive second-play effectance does not imply structural replay limits never matter. |
| **Roth & Vermeulen (2013),** [*Breaching Interactive Storytelling's Implicit Agreement*](https://doi.org/10.1007/978-3-319-02756-2_20), *Interactive Storytelling*, pp. 168–173. **Publisher/institutional abstract and reproduced content analysis in Roth's dissertation (same research program and 50 participants).** | Content analysis of **100 captured transcripts / 50 people** over two *Façade* exposures found **less in-character, less meaningful input** on the second play. More engaged/complex input was associated with poorer system responses and negative affect. This establishes behavioral adaptation and limitations of interaction fidelity. | **Not an independent replication** of the 2012 replay sample, nor evidence of falling self-reported agency, and not an experimental test of branch reconvergence. Users can adapt by simplifying their inputs while rating their effectance higher. |
| **Fendt, Harrison, Ware, Cardona-Rivera & Roberts (2012),** [*Achieving the Illusion of Agency*](https://doi.org/10.1007/978-3-642-34851-8_11), *Interactive Storytelling*, pp. 114–125. **[Full author-hosted article](https://www.cs.uky.edu/~sgware/reading/papers/fendt2012achieving.pdf), especially study design and Table 2.** | Three experimental conditions: branching story with feedback; nonbranching story acknowledging choices; nonbranching story with minimal feedback. In **four of five story-level agency comparisons**, branching and nonbranching-with-feedback conditions did **not** significantly differ; **one comparison did** favor genuine branching (the belief the story would have been different after different choices, **p=.030**). Immediate feedback can preserve much perceived agency *on initial exposure* even without lasting divergence. | No repeat-play or subsequent disclosure of the nonbranching structure. **Non-significant differences are not proof of statistical equivalence** or of a replay-proof illusion. |
| **Cardona-Rivera, Robertson, Ware, Harrison, Roberts & Young (2014),** [*Foreseeing Meaningful Choices*](https://doi.org/10.1609/aiide.v10i1.12716), *AIIDE*, 10(1), 9–15. **[Full AAAI paper](https://ojs.aaai.org/index.php/AIIDE/article/download/12716/12564/16233).** | **N=88**, one choose-your-own-adventure experience; participants reported greater agency for decisions they perceived as leading to **meaningfully different situational outcomes**, compared with decisions that seemed equivalent. Results depended on which measure of agency was examined and on the story's choice structure. | Does not show that replay causes agency ratings to decay; measures the relation between *perceived* consequence and agency in a single narrative trajectory. |
| **Stang (2019),** [*“This Action Will Have Consequences”*](https://gamestudies.org/1901/articles/stang), *Game Studies*, 19(1). **Full article.** | Qualitative/critical case analysis of *BioShock* and *The Walking Dead* substantiates **convergence and constrained narrative agency** as design phenomena. | Does **not** measure players repeatedly, quantify a change in perceived agency, or demonstrate a replay-related causal effect. |
| **Jones & Millard (2026),** [*Beyond Authorial Burden*](https://doi.org/10.1145/3757746), *ACM Transactions on the Web*, 20(3), Article 34, especially §7.5.1. **Full publisher HTML.** | Explicitly identifies that Fendt et al. did not retest participants after players learned their choices lacked wider consequences. Argues that illusory agency may become visible on replay in longer works. Valuable **independent critical synthesis and gap identification**. | Its replay prediction is **an argument, not a new empirical manipulation**; do not cite it as experimental proof of declining perceived agency. |

**How the apparently conflicting observations fit together:** Fendt demonstrates that immediate recognition of choices can sustain first-play perceived agency without substantial branching. Cardona-Rivera demonstrates that perceiving choice options as meaningfully distinct matters for agency ratings. Roth demonstrates that one additional exposure can *increase* perceived efficacy as players learn the interface; the paired transcript study also suggests they may reduce the complexity of their input to fit the system. None isolates an experimentally revealed lack of *persistent downstream consequence*. Hence the paper's intuition can survive **as a testable, conditional inference** about discovery of reconvergence, but the stronger statement that it *does* weaken across successive replays is not presently supported.

**Suggested research-safe framing for a later editorial decision (NOT applied to outline):** "Reconverging choices can preserve perceived agency through immediate feedback even when their enduring consequences are limited. Repeated play may expose invariant outcomes and constrain that perception, but existing replay experiments do not establish a general decline; perceived effectance can instead increase as players learn the system." The source-to-claim target is **§4.6**, not the separately evidenced conceptual distinction between actual and perceived agency in §§2.9 and 4.6.

**What would close the causal claim empirically:** Randomly assign comparable players to (A) genuinely branching persistent consequences, (B) immediate feedback with reconverging/invariant outcomes, and ideally (C) bounded reconvergence with persistent local callbacks. Re-expose participants to alternative choices and record **knowledge that earlier choices reconverged**, perceived *local* vs *global* agency at each playthrough, perceived effectance, satisfaction and input adaptation. Follow-up should separate **replay number** from **discovery of structural limits**, which may otherwise be conflated. Until such evidence exists, classify the replay-specific claim as a **hypothesis requiring direct evaluation**, not a confirmed effect.

**Bibliography integration completed (2026-10-09):** Added Roth et al. (2012), Roth & Vermeulen (2013), Fendt et al. (2012), Cardona-Rivera et al. (2014), and Jones & Millard (2026) to the alphabetized publication bibliography in `docs/design-paper.md` (**97 entries**), with cited support in Appendix D and annotated methods/limits in `docs/research/bibliography-notes.md` §13. Publication identities were checked individually for these five additions; the original **92-reference bibliography-verification ledger remains a historical snapshot, not a validation record for all 97 entries**. The research issue remains unresolved empirically; the original outline §4.6 is unchanged.

---

## Focused research resolution R2 — §§3.10 and 4.7: historical formalization and probabilistic interpretation (2026-10-09)

**Research question:** Was the historical bottleneck the need to explicitly represent executable world/action possibilities, or the absence of probabilistic interpretation? These are not equivalent claims. Also distinguish learning a representation from safely committing proposed actions into an authoritative world.

**Disposition: PARTIALLY RESOLVED.** The narrative planning *domain-model/authoring bottleneck* is substantiated by direct research. The general historical assertion that systems lacked efficient probabilistic assessment is contradicted by pre-LLM research in natural-language story/plan inference, dialogue management, and player modeling. Whether broadly learned modern models are reliably capable of arbitrary open-world action adjudication remains untested. **Later editorial update:** The revised §3.10 was approved and applied on 2026-10-09; §4.7 remains unchanged.

| Primary source and access | Evidence relevant to the historical claim | Limit |
|---|---|---|
| **Charniak & Goldman (1993),** [A Bayesian Model of Plan Recognition](https://doi.org/10.1016/0004-3702(93)90060-O), *Artificial Intelligence* 64(1):53–79. Publisher abstract/metadata checked. | Bayesian network inference over candidate plans, implemented in Wimp3 for natural-language story understanding. A direct counterexample to saying probabilistic narrative interpretation did not exist. | Operates over candidate explanations/plans; not unconstrained world-event adjudication. |
| **Mateas & Stern (2005),** [Structuring Content in the Façade Interactive Drama Architecture](https://doi.org/10.1609/aiide.v1i1.18722). AAAI abstract checked; already cited. | Real-time interactive drama with thousands of authored reactive joint-dialogue behaviors and beats coordinated by a drama manager. | Shows considerable authored structures despite open-text interaction; does not justify saying every early system was deterministic. |
| **Chambers & Jurafsky (2010),** [A Database of Narrative Schemas](https://aclanthology.org/L10-1029/), LREC. ACL primary abstract checked. | Learned narrative event and participant schemas from open-domain text, assembling a resource containing roughly 5,000 distinct events. | Learned event structures are not a guaranteed executable world/action model. |
| **Thomson & Young (2010),** [Bayesian Update of Dialogue State: A POMDP Framework for Spoken Dialogue Systems](https://doi.org/10.1016/j.csl.2009.07.003), *Computer Speech & Language* 24(4):562–588. Publisher abstract checked. | Real-time approximate Bayesian dialogue-state updates and policy learning, explicitly addressing the computational intractability of exact POMDP inference. | Strong counterexample to universal impracticality of probabilistic assessment; scoped dialogue state/action representations remain. |
| **Chen & Mooney (2011),** [Learning to Interpret Natural Language Navigation Instructions from Observations](https://doi.org/10.1609/aaai.v25i1.7974), AAAI. Conference abstract checked. | Learned mapping of natural-language navigation commands into executable formal plans in three virtual environments. | Some utterances need not be individually enumerated, but command/world domains are bounded and performance partial. |
| **Yu & Riedl (2013),** [Data-Driven Personalized Drama Management](https://doi.org/10.1609/aiide.v9i1.12665), AIIDE. AAAI abstract checked. | Learned player modeling and manipulation of probabilities of story continuation in a tested interactive-storytelling game. | An explicitly narrative-specific earlier probabilistic approach, operating inside a represented story/choice space. |
| **Hayton et al. (2020),** [Narrative Planning Model Acquisition from Text Summaries and Descriptions](https://doi.org/10.1609/aaai.v34i02.5534), AAAI. Full paper introduction and modeling assumptions examined as well as AAAI abstract; already cited. | Explicitly identifies narrative-domain modeling as difficult; automatically extracts PDDL-style baseline planning models from natural-language synopses, with reported authoring-effort reduction. | Important **earlier partial solution** to representation cost, not unrestricted runtime interpretation. Inputs/outputs and action predicates are constrained. |
| **Porteous et al. (2021),** [Automated Narrative Planning Model Extension](https://doi.org/10.1007/s10458-021-09501-1), *Autonomous Agents and Multi-Agent Systems* 35(2), article 19. University repository abstract checked; already cited. | Explicitly identifies alternative operator/action authoring as a bottleneck and tests automated extensions for plot diversity and recovery following action failure. | Strong evidence of ongoing formalization burden; also a reminder that earlier approaches already automated parts of that work. |

### Resolution by claim

- **§3.10 — formal action/state representation constrains execution:** **Supported with scope.** Planners and drama managers can generate combinations or situations no author enumerated as complete plots, but candidate actions, predicates, transition semantics and consequences operate in a modeled domain. That model may itself be learned or extended.
- **§3.10 — historical lack of efficient probabilistic assessment:** **Contradicted if universal.** Bayesian story inference predates LLMs by decades; approximate probabilistic dialogue management and learned agent/player models likewise have earlier precedents. No defensible universal breakthrough date has been established.
- **§4.7 — explicit formalization was a deeper historical bottleneck:** **Supported for narrative planning and related game-agent architectures.** Hayton and Porteous directly identify the authoring/model-building problem. Not proven as the single dominant limitation of all historical AI systems.
- **§4.7 — human GM interprets unforeseen action without pre-enumerating every case:** **Conceptual comparison, not quantified experiment.** It usefully identifies a capability target; it does not show perfect human adjudication or prove historical impossibility of machine inference.
- **Link to §4.8 — modern models change the authoring boundary:** **Plausible architectural inference.** Broadly pretrained models can propose interpretations/actions without individually scripting every utterance, but they do not thereby guarantee legal actions, world-state fidelity, or safety. Those remain external authority/validation duties in Enclave.

**Earlier research-safe title suggestions (not adopted verbatim):** §3.10, *Formalized narrative systems remain bounded by represented actions and world models*; §4.7, *The persistent bottleneck was constructing and maintaining executable representations.* The subsequently approved §3.10 title is **Limitations of Historical Approaches**. The substantive comparison is **limited domain representation and reliable grounding versus more general learned interpretation**, not historical deterministic computing versus newly invented probabilistic reasoning.

**Bibliography integration:** Added five individually source-checked historical references (Charniak & Goldman 1993; Chambers & Jurafsky 2010; Thomson & Young 2010; Chen & Mooney 2011; Yu & Riedl 2013). Hayton 2020, Porteous 2021 and Mateas & Stern 2005 were already included. Publication bibliography had **102 entries at the time of this R2 pass** and has **105 after the approved §3.10 expansion and three additional computational sources**. The historical 92-entry verification ledger remains unchanged and must not be misrepresented as verifying all 105.

**Status update (2026-10-09):** Research pass complete. The author-approved expansion of **§3.10, “Limitations of Historical Approaches,”** was applied to the outline with the formalization and probabilistic implementation tax distinguished. Cooper (1990), Dagum & Luby (1993), and Das (2004) were added to the publication bibliography (**105 entries**, versus 102 at the original R2 pass), with evidence limits described in bibliography notes §8.7. **§4.7 and all other outline subsections remain unchanged**; evaluation of general-purpose model effectiveness remains future validation.

---

## Focused research resolution R3 — §§4.5 and 6.5: narrative reconvergence, sandboxed worlds and narrative consequence (2026-10-09)

**Scope:** This pass evaluates whether the outline's claims that authored branches reconverge, quests/side stories are structurally compartmentalized, and mechanically open worlds are *usually* less open in authored narrative are supported beyond isolated game examples. Related claims in §§2.8 and 4.13 are affected. **No changes to `docs/paper-outline.md` are authorized or made.**

### Sources examined and evidentiary roles

| Source | Verified finding and relevance | Boundary / access |
|---|---|---|
| [Zaini, Fowler, Amor & Wünsche (2025), *Character-Driven Storytelling Design for Digital Games: A Scoping Review*, *Games and Culture*](https://doi.org/10.1177/15554120251380423) | Full open-access scoping review synthesizing **69 selected peer-reviewed studies** (from 886 initial records). Identifies reconverging branches, linear stories with variations, and emergent storytelling as established approaches. Strong broader-literature corroboration for §4.5's *existence of the pattern*. | Studies of character-driven narrative, **not a representative census of commercial games**. The authors acknowledge genre selection bias and underrepresentation of strategy/simulation games; the review does not quantify how many titles use each structure. |
| [Jones & Millard (2026), *Beyond Authorial Burden*, *ACM Transactions on the Web*](https://doi.org/10.1145/3757746) | Full accessible publisher text describes **14 interviews** with interactive-digital-narrative creators and **8 expert-panel participants**, identifies reuse and scope-reduction strategies, and specifically describes an expert's practice of *collapsing continuities* by merging branches. Supports *authorial motivation and technique* of reconvergence. | Mostly creators of hypertext, text adventure, visual novel and choice-based work; **not a frequency survey of mainstream open-world games**. Also warns that strategies can *shift* rather than reduce authoring labor. |
| [Alexander & Martens (2017), *Deriving Quests from Open World Mechanics*](https://arxiv.org/abs/1705.00341) | Original author abstract explicitly describes quests/objectives in open worlds as generally **hand-authored and overlaid on game mechanics**, motivating derived procedural objectives. Bridges the world-mechanics / authored-objectives distinction. | Original research and system proposal, not a representative survey or evidence that every mechanically meaningful action fails to affect narrative. |
| [Harris & Caldwell (2023 online; journal issue 2024), *A Transfiguration Paradigm for Quest Design*, *Games and Culture*](https://doi.org/10.1177/15554120231170152) | Full open-access academic discussion identifies **task-oriented quest design** as dominant in its surveyed quest-design models and proposes an alternative focus on player-character change. Reinforces that quest structures are often organized around authored task sequences. | Dominance in **quest-design paradigms/models**, not a measured prevalence of all shipped games or inability to react to unexpected combinations. |
| [Xu, Zhang, Yang & Verbrugge (2026), *Deconstructing Open-World Game Mission Design Formula*, arXiv preprint](https://arxiv.org/html/2603.18398) | Inspected HTML full text. Analyzes **2,191 valid missions** (607 main, 1,174 side, 410 POI) from **20 selected high-profile titles** (2011–2025), showing systematic differences in mission composition and main/side/POI narrative emphasis. Much broader **cross-game evidence** for §6.5's *narrative organization*. | **Preprint, not treated as peer-reviewed evidence.** Uses Fandom walkthroughs, GPT-4.1 action extraction, purposively selected well-documented titles, and linearly represented missions; authors explicitly note **branching often linearized** and emergent play/optional/failure paths undercaptured. It **does not measure whether side quests causally affect the central plot** or the prevalence of reactive authored storyworlds. |
| [Grey & Bryson (2011), *Procedural Quests: A Focus for Agent Interaction in Role-Playing-Games*, AISB AI & Games](https://researchportal.bath.ac.uk/en/publications/procedural-quests-a-focus-for-agent-interaction-in-role-playing-g/) | University research record verifies this *counterexample/prior art*: episodic NPC memories, social relationships, gossip/information propagation and emergent quest motivation were proposed/implemented in a research system long before contemporary LLMs. Supports historical contrast between constrained mainstream NPC designs and research alternatives. | University abstract and bibliographic record verified; **not** a quantitative estimate of adoption or proof that current games universally lack these abilities. Relevant to the **separate prior-art novelty review**. |
| [Burgess & Jones (2023), *Exploring how players use emergent narrative in strategy games*, *Entertainment Computing*](https://doi.org/10.1016/j.entcom.2022.100533) | Original abstract reports thematic analysis of **295 Total War forum posts** and **104 survey responses**, describing players' emergent narratives and emotional attachment. Corroborates §6.5's existing recognition of player-constructed systemic narrative. | Does not test ongoing **authored-character response** to unanticipated events; cannot be used to claim emergent narrative is lesser, merely different. |
| [Sullivan (2012), *The Grail Framework: Making Stories Playable on Three Levels in CRPGs*, UCSC thesis](https://escholarship.org/uc/item/004129jn) | University thesis abstract differentiates player, quest, game and world-story layers; argues game-level stories in analyzed CRPG practice are minimally branching, supporting the conceptual separation of local action freedom and macro-level scripted progress. | Dissertation's analytical framing is **not** an industry-scale prevalence count. Full thesis not reviewed in this pass. |
| [Game Developer (2018), *Narrative Design on Open Worlds: Should We Ditch Missions?*](https://www.gamedeveloper.com/design/narrative-design-on-open-worlds-should-we-ditch-missions-) | Practitioner design discussion explicitly separates a generally linear/branching **critical path** from optional freely accessed side activities. Useful independent corroboration of production trade-offs. | Practitioner argument, **not empirical sampling**, and includes countervailing examples of meaningful quest consequences. |

### Claim-level disposition

- **§4.5, branches reconverge / transient variants / explicit restriction of responses — substantially supported as documented design strategies.** The 2025 literature synthesis and 2026 interviews provide broader support than Stang's individual-game case studies. These sources establish that reconvergence and bounded authoring are **recognized, recurring mechanisms**, **not** a measured percentage of games. Claims that side stories *always* remain isolated, NPCs can react *only* through predefined states, or unforeseen combinations *simply have no meaningful response* should be scoped to relevant authored systems; emergent NPC and procedural-quest precedents provide counterexamples.
- **§6.5, mechanically sandboxed worlds versus structured narrative — supported as an important documented design tension and comparative framework.** Alexander/Martens, Harris/Caldwell, Sullivan and the cross-title 2026 mission analysis corroborate the separation between systemic mechanics, authored quests and narrative hierarchy. However, the 2026 preprint **measures mission structure and narrative emphasis, not cross-quest causal integration**. The section's central three-way distinction — systemic emergence, emergent/player-constructed narrative and persistently reactive authored narrative — remains useful as **this paper's synthesis**, not a directly validated, industry-wide taxonomy.
- **The exact words “commonly” (§4.5) and “usually” (§6.5) remain qualified.** Multiple studies document the phenomena across methods, periods and game types, but none supplies a representative denominator for the prevalence of integrated **reactive authored narrative** among shipped games. The new evidence justifies saying the design trade-off is **well documented**, not calculating its prevalence or claiming universality.
- **Do not equate scripted with nonconsequential.** A story can have authored state flags, significant branch endings, cross-quest effects and NPC reactions without dynamically generating wholly new plot structure; conversely, rich systemic emergence does not necessarily involve authored characters and themes absorbing it. Those are different axes to classify before a future comparative study.
- **Counterexample carried forward:** Grey & Bryson (2011) is relevant to the later **prior-art/originality** pass: agent memory, rumor-like propagation and dynamic quests cannot be presented as historically absent or unique to Enclave, even if Enclave's integration and authority model differ.

**Disposition:** **PARTIALLY RESOLVED — substantially stronger literature and multi-title corroboration; a representative prevalence estimate, any universal incapability claim and direct measurement of persistent cross-quest authored response remain unsupported.** No new industry-level quantitative claim should be introduced from a purposively selected mission dataset.

**Recommended editorial options for later approval (none implemented):** Replace unqualified prevalence language with “documented,” “widely discussed in the design literature” or “among the examined titles”; avoid universal claims that all side stories are isolated or all NPC reactions predefined; retain the distinction between mechanically emergent play and reactive authored continuation. No need to weaken the underlying architectural motivation.

**Bibliography disposition:** The additional references above are **candidate additions**, not automatically reconciled into the approved 92-item bibliography. Before incorporation, check bibliographic overlap, DOI/venue/version details, access and relevance; mark Xu et al. (2026) as a **preprint**. The older Stang (2019) and Evans (2024) citations remain relevant illustrative cases.

## Complete referenced-subsection audit — all 61 locations

**This is the authoritative, consolidated subsection-by-subsection audit.** It covers every subsection of the current outline with an explicit `Support:` or equivalent source marker. The original cited-work lines are preserved below; bibliography links are provided from the independently checked 92-entry identification ledger. The evidence assessments distinguish measured results, case studies, practitioner precedent, theory, the paper's own logical inferences, and unverified implementation claims.

**A reviewed subsection is not a verified paragraph.** One original source may support only some of its claims. Source access is stated where recorded; previous reviews often used abstracts or selected excerpts rather than complete papers. Each entry indicates *what the evidence does and does not establish*; no claim is made that all 92 original studies were read end-to-end.


### Section 2 — cited-subsection findings

#### §2.1 — Human creative expression is individual rather than interchangeable.

**Representative claim(s):** Writers bring different linguistic habits, experiences, perspectives, cultural backgrounds, associations, and creative instincts to a work; Human writing carries measurable individual and social signatures, and human creativity shows substantially greater variance at the high-creativity end.
**Cited in outline:** Support: Sourati et al. (2026); Wang et al. (2026).
**Linked source records:** [#80 Sourati, Z., Karimi-Malekabadi, F., Ozcan, M., McDaniel](https://doi.org/10.1038/s41562-026-02550-0); [#89 Wang, D., Huang, D., Shen, H., & Uzzi, B](https://doi.org/10.1038/s41562-025-02331-1)
**Substantive assessment — scope narrowed:** Divergent-idea task is not a general result about narrative authorship
**Source-access record:** prior thematic review; source-level access varied (full article, publisher/author abstract, practitioner page, or indexed excerpt). Consult the section-by-section analysis below for the available specificity; full-text access for every named work is **not** asserted.

#### §2.2 — Narrative depth is created through relationships across the complete work.

**Representative claim(s):** Character, theme, subtext, symbolism, pacing, conflict, foreshadowing, emotional development, turning points, and resolution gain meaning through their relationship to one another; Human-authored stories show greater structural diversity, suspense, arousal, and variation in story arcs; expert-oriented evaluation also places more emphasis on thematic development and rhetorical variety than on surface fluency alone.
**Cited in outline:** Support: Tian et al. (2024); Marco et al. (2025).
**Linked source records:** [#87 Tian, Y., Huang, T., Liu, M., Jiang, D., Spangher, A., ](https://doi.org/10.18653/v1/2024.emnlp-main.978); [#58 Marco, G., Gonzalo, J., & Fresno, V](https://doi.org/10.18653/v1/2025.findings-acl.1304)
**Substantive assessment — bounded support:** Tian concerns evaluated stories; Marco concerns reader priorities
**Source-access record:** prior thematic review; source-level access varied (full article, publisher/author abstract, practitioner page, or indexed excerpt). Consult the section-by-section analysis below for the available specificity; full-text access for every named work is **not** asserted.

#### §2.3 — Independent human authorship produces substantial creative breadth.

**Representative claim(s):** Different authors do not merely produce different wording around the same underlying story; Human-written stories show substantially greater plot-level diversity and much less repetition of plot elements and combinations.
**Cited in outline:** Support: Xu et al. (2025).
**Linked source records:** [#92 Xu, W., Jojic, N., Rao, S., Brockett, C., & Dolan, B](https://doi.org/10.1073/pnas.2504966122)
**Substantive assessment — scope narrowed:** Xu compares original short stories with two specified LLMs and prompts
**Source-access record:** prior thematic review; source-level access varied (full article, publisher/author abstract, practitioner page, or indexed excerpt). Consult the section-by-section analysis below for the available specificity; full-text access for every named work is **not** asserted.

#### §2.5 — Meaningful participation requires meaningful response.

**Representative claim(s):** Participant freedom matters only when the world can react to what the participant does; Agency is not merely the availability of inputs or choices; it is tied to meaningful action and perceivable consequence; Interactive-narrative research explicitly treats the maintenance of agency and narrative coherence as a central design problem.
**Cited in outline:** Support: Hammond, Pain & Smith (2007).
**Linked source records:** [#42 Hammond, S., Pain, H., & Smith, T. J](https://ualresearchonline.arts.ac.uk/id/eprint/21210/)
**Substantive assessment — qualified conceptual support:** Hammond, Pain & Smith explicitly frame agency/coherence as a central interactive-narrative question, but 'meaningful response is required' is Enclave's design norm rather than a result of a controlled study.
**Source-access record:** institutional abstract; principal source documented in the continuation pass: [Source](https://ualresearchonline.arts.ac.uk/id/eprint/21210/). Other listed citations may only have received metadata or abstract-level verification.

#### §2.6 — Interactive narrative places unusual demands on human authorship.

**Representative claim(s):** Unlike conventional narrative, the audience can intervene in the work; Participants may ignore intended paths, alter event order, combine actions unexpectedly, or attempt things the author never anticipated; This unpredictability is a property of the medium, not a deficiency in human authorship.
**Cited in outline:** Support: Louchart & Aylett (2003).
**Linked source records:** [#56 Louchart, S., & Aylett, R](https://doi.org/10.1007/978-3-540-39396-2_41)
**Substantive assessment — direct support bounded:** Louchart & Aylett explicitly define the narrative paradox as the tension between authored plot and participant movement/action freedom. The paper analyzes RPGs through one expert's knowledge elicitation, not a validated game-engine solution.
**Source-access record:** author-hosted full-text PDF pp.1–5; principal source documented in the continuation pass: [Source](https://www.macs.hw.ac.uk/~ruth/Papers/narrative/IVA03-Louchart-Aylett.pdf). Other listed citations may only have received metadata or abstract-level verification.

#### §2.7 — Conventional interactive authoring mechanisms make broad responsiveness increasingly difficult to express.

**Representative claim(s):** Branching creates additional authored content; Persistent choices produce increasing combinations of possible state; More interactions require more conditional logic, alternate descriptions, dialogue, consequences, and testing.
**Cited in outline:** Support: Jones (2022); Jones & Millard (2024).
**Linked source records:** [#51 Jones, J. D](https://doi.org/10.1007/978-3-031-05214-9_4); [#52 Jones, J. D., & Millard, D. E](https://doi.org/10.1145/3648188.3675134)
**Substantive assessment — direct support bounded:** Jones (2022) details exponential branching, combinatorial explosion and scope; Jones & Millard (2024) interview 14 IDN authors. Strong support for types of authoring burden, not a numerical industry-wide growth curve.
**Source-access record:** Jones 2022 abstract and indexed 2024 paper excerpts; principal source documented in the continuation pass: [Source](https://eprints.soton.ac.uk/500739/1/3648188.3675134.pdf). Other listed citations may only have received metadata or abstract-level verification.

#### §2.8 — Conventional interactive authoring mechanisms therefore tend to produce a poor simulacrum of the intended experience.

**Representative claim(s):** One compromise is **pseudo-freeform structure**: the player appears to have broad narrative freedom, but meaningful reactions exist only inside anticipated branches and state combinations; Branches may diverge temporarily and then reconverge, preserving the impression of consequence without supporting permanently divergent narrative states; The other compromise is **open-ended but weakly consequential structure**: the player may explore freely and engage with many optional stories, but those stories often remain compartmentalized from the principal narrative and broader gameplay unless explicitly entered.
**Cited in outline:** Support: Stang (2019); Evans (2024).
**Linked source records:** [#82 Stang, S](https://gamestudies.org/1901/articles/stang); [#35 Evans, M](https://gamestudies.org/2404/articles/evans)
**Substantive assessment — bounded case study:** Stang describes reconvergence in BioShock and The Walking Dead; Evans discusses blended exploratory/linear structures in Subnautica. Neither supports characterizing *all* conventional narratives as a poor simulacrum.
**Source-access record:** full HTML; Evans full HTML; principal source documented in the continuation pass: [Source](https://gamestudies.org/1901/articles/stang). Other listed citations may only have received metadata or abstract-level verification.

#### §2.9 — Research on agency shows that the appearance of freedom can be separated from actual freedom.

**Representative claim(s):** Day & Zhu distinguish **theoretical agency** from **perceived agency**; Thue et al. (2011) provide empirical support for perceived agency increasing without expanding the underlying action space; Stang's analysis of *The Walking Dead* describes branching decisions that repeatedly reconverge.
**Cited in outline:** Support: Day & Zhu (2017); Thue et al. (2011); Stang (2019).
**Linked source records:** [#34 Day, T., & Zhu, J](https://doi.org/10.1145/3102071.3106363); [#86 Thue, D., Bulitko, V., Spetch, M., & Romanuik, T](https://doi.org/10.1609/aiide.v7i1.12437); [#82 Stang, S](https://gamestudies.org/1901/articles/stang)
**Substantive assessment — direct support:** Theoretical versus perceived agency distinguished; narrative reconvergence is case-study supported
**Source-access record:** prior thematic review; source-level access varied (full article, publisher/author abstract, practitioner page, or indexed excerpt). Consult the section-by-section analysis below for the available specificity; full-text access for every named work is **not** asserted.

#### §2.10 — Those limitations constrain both sides of the creative relationship.

**Representative claim(s):** Authors cannot reasonably anticipate and explicitly implement responses to everything a participant might attempt; Participants are consequently limited either to actions for which meaningful responses were implemented, or to broader activities whose effects remain largely outside the consequential narrative; The authorial-burden literature locates this problem in the growth of content, state management, and implementation work rather than in any shortage of human creative capacity.
**Cited in outline:** Support: Jones (2022); Jones & Millard (2024).
**Linked source records:** [#51 Jones, J. D](https://doi.org/10.1007/978-3-031-05214-9_4); [#52 Jones, J. D., & Millard, D. E](https://doi.org/10.1145/3648188.3675134)
**Substantive assessment — authorial synthesis:** Jones/Jones–Millard identify authors' content/structure/tool burdens; constraints on participants logically follow from implemented affordances, but the exact both-sides conclusion is Enclave's interpretation.
**Source-access record:** conference paper excerpts; Jones chapter abstract; principal source documented in the continuation pass: [Source](https://eprints.soton.ac.uk/500739/1/3648188.3675134.pdf). Other listed citations may only have received metadata or abstract-level verification.


### Section 3 — cited-subsection findings

#### §3.1 — Human authorship is expressed through worlds as well as sequences.

**Representative claim(s):** Narrative meaning can be embedded in places, institutions, relationships, histories, conflicts, objects, information, and affordances—not only in a predetermined chain of scenes; A designed environment can carry narrative purpose before a specific traversal through it is known; Different participants can encounter the same authored material in different orders and combinations without stripping it of authorial intent.
**Cited in outline:** Support: Jenkins (2004), *Game Design as Narrative Architecture*.
**Linked source records:** [#48 Jenkins, H](https://electronicbookreview.com/publications/game-design-as-narrative-architecture/)
**Substantive assessment — direct conceptual support:** Jenkins explicitly treats games as narrative architecture where world spaces, staging, information and emergent storytelling carry meaning independently of fixed scene order.
**Source-access record:** original full HTML; principal source documented in the continuation pass: [Source](https://electronicbookreview.com/publications/game-design-as-narrative-architecture/). Other listed citations may only have received metadata or abstract-level verification.

#### §3.2 — Interactive authorship should prepare situations rather than scripts for participant behavior.

**Representative claim(s):** Participant action is inherently difficult to predict exhaustively; The author can instead establish the circumstances from which consequences follow: people, motives, resources, constraints, relationships, locations, and pressures; “Don’t prep plots, prep situations” is the clearest practitioner formulation of this distinction.
**Cited in outline:** Support: Alexander (2009), *Don’t Prep Plots*; Alexander (2015), *Tools, Not Contingencies*.
**Cited in outline:** Supporting: Alexander (2018), *Smart Prep*.
**Linked source records:** [#4 Alexander, J](https://thealexandrian.net/wordpress/4147/roleplaying-games/dont-prep-plots); [#14 Alexander, J](https://thealexandrian.net/wordpress/37422/roleplaying-games/dont-prep-plots-tools-not-contingencies); [#17 Alexander, J](https://thealexandrian.net/wordpress/39885/roleplaying-games/smart-prep)
**Substantive assessment — direct practitioner:** Alexander explicitly advocates prepping situations instead of predetermined plots
**Source-access record:** prior thematic review; source-level access varied (full article, publisher/author abstract, practitioner page, or indexed excerpt). Consult the section-by-section analysis below for the available specificity; full-text access for every named work is **not** asserted.

#### §3.3 — Intended future developments can still be authored without becoming fixed plots.

**Representative claim(s):** Authors can establish likely future events, actor plans, timelines, goals, and dramatic destinations; Those expectations remain conditional on the world continuing to develop in the anticipated way; When participant action changes the situation, future developments are reconsidered from the new state rather than forcibly preserved.
**Cited in outline:** Support: Alexander (2009), *Don’t Prep Plots: Prepping Scenario Timelines*.
**Cited in outline:** Supporting: Alexander (2026), *Is Node-Based Design Prepping a Plot?*
**Linked source records:** [#5 Alexander, J](https://thealexandrian.net/wordpress/4154/roleplaying-games/dont-prep-plots-prepping-scenario-timelines); [#23 Alexander, J](https://thealexandrian.net/wordpress/53341/roleplaying-games/is-node-based-design-prepping-a-plot)
**Substantive assessment — direct practitioner:** Alexander's worked initial and revised scenario timelines show that intended future events are conditional on player interventions. The 2026 post explicitly distinguishes situation from predetermined plot.
**Source-access record:** original full practitioner pages; principal source documented in the continuation pass: [Source](https://thealexandrian.net/wordpress/4154/roleplaying-games/dont-prep-plots-prepping-scenario-timelines). Other listed citations may only have received metadata or abstract-level verification.

#### §3.4 — Information is one of the principal structures through which narrative possibility is organized.

**Representative claim(s):** What participants know determines what they can understand, pursue, question, reveal, conceal, or interfere with; Important information should not depend on one brittle discovery path; Revelations can be separated from the particular clues or routes by which they become available.
**Cited in outline:** Support: Alexander (2008), *Three Clue Rule*; Alexander (2010), *Node-Based Scenario Design – Part 3: Inverting the Three Clue Rule*; Alexander (2018), *Using Revelation Lists*; Alexander (2020), *The Secret Life of Nodes*.
**Linked source records:** [#3 Alexander, J](https://thealexandrian.net/wordpress/1118/roleplaying-games/three-clue-rule); [#8 Alexander, J](https://thealexandrian.net/wordpress/7985/roleplaying-games/node-based-scenario-design-part-3-inverting-the-three-clue-rule); [#16 Alexander, J](https://thealexandrian.net/wordpress/40978/roleplaying-games/random-gm-tip-using-revelation-lists); [#22 Alexander, J](https://thealexandrian.net/wordpress/45263/roleplaying-games/the-secret-life-of-nodes)
**Substantive assessment — direct practitioner:** The Three Clue Rule, inverted rule and revelation lists explicitly separate revelations from any single clue/discovery path; node navigation is built around information flow. Practitioner method, not tested Enclave access control.
**Source-access record:** original full practitioner pages; principal source documented in the continuation pass: [Source](https://thealexandrian.net/wordpress/7985/roleplaying-games/node-based-scenario-design-part-3-inverting-the-three-clue-rule). Other listed citations may only have received metadata or abstract-level verification.

#### §3.5 — Narrative structure can arise from the diegetic organization of the world itself.

**Representative claim(s):** People, places, organizations, events, and activities can become loci of interaction because of their actual relationships in the fictional world; Structure does not have to be imposed purely as an abstract scene graph; “Node” should not become the ontology of the world.
**Cited in outline:** Support: Alexander (2010), *Node-Based Scenario Design – Part 9: Types of Nodes*; Alexander (2020), *Naturalistic Node Design*.
**Linked source records:** [#10 Alexander, J](https://thealexandrian.net/wordpress/8049/roleplaying-games/node-based-scenario-design-part-9-types-of-nodes); [#21 Alexander, J](https://thealexandrian.net/wordpress/45283/roleplaying-games/the-secret-life-of-nodes-part-5-naturalistic-node-design)
**Substantive assessment — direct practitioner:** Alexander's types of nodes and naturalistic node design substantiate world-located interaction/info nodes. Saying a node 'should not become the ontology' is Enclave's architectural inference, not Alexander's tested invariant.
**Source-access record:** original full practitioner pages; principal source documented in the continuation pass: [Source](https://thealexandrian.net/wordpress/45283/roleplaying-games/the-secret-life-of-nodes-part-5-naturalistic-node-design). Other listed citations may only have received metadata or abstract-level verification.

#### §3.6 — Actors give authored situations motion.

**Representative claim(s):** Actors should have goals, resources, relationships, knowledge, and plans rather than simply waiting for a participant to trigger a scripted branch; Opposition and conflict can arise from what actors want and are capable of doing; The world can act **toward** the participant through proactive actors and events rather than remaining passively discoverable.
**Cited in outline:** Support: Alexander (2009), *Don’t Prep Plots*; Alexander (2011), *Advanced Node-Based Design – Part 1: Moving Between Nodes*; Alexander (2015), *You Will Rue This Day, Heroes!*.
**Linked source records:** [#4 Alexander, J](https://thealexandrian.net/wordpress/4147/roleplaying-games/dont-prep-plots); [#11 Alexander, J](https://thealexandrian.net/wordpress/8171/roleplaying-games/advanced-node-based-design-part-1-moving-between-nodes); [#15 Alexander, J](https://thealexandrian.net/wordpress/36383/roleplaying-games/dont-prep-plots-you-will-rue-this-day-heroes-the-principles-of-rpg-villainy)
**Substantive assessment — direct practitioner:** Don't Prep Plots, moving between nodes and villain principles support active antagonists, goals and plans instead of waiting for scripted triggers. Generalization to autonomous AI actors is proposed, not demonstrated.
**Source-access record:** original full practitioner pages; principal source documented in the continuation pass: [Source](https://thealexandrian.net/wordpress/36383/roleplaying-games/dont-prep-plots-you-will-rue-this-day-heroes-the-principles-of-rpg-villainy). Other listed citations may only have received metadata or abstract-level verification.

#### §3.7 — Authored narrative material can be conditional rather than sequential.

**Representative claim(s):** Storylets demonstrate that authored content can exist independently and become available when prerequisites are satisfied; Completed content can alter shared state, which changes what becomes possible next; This permits deliberate narrative arcs without encoding every route through them as a branch tree.
**Cited in outline:** Support: Short (2019), *Storylets: You Want Them*; Short (2019), *Storylets Play Together*.
**Cited in outline:** **Supporting practitioner references:** Failbetter Games, *StoryNexus Developer Diary #2*; *Echo Bazaar Narrative Structures, Part Two*.
**Linked source records:** [#78 Short, E](https://emshort.blog/2019/11/29/storylets-you-want-them/); [#77 Short, E](https://emshort.blog/2019/12/03/storylets-play-together/); [#36 Failbetter Games](https://www.failbettergames.com/news/echo-bazaar-narrative-structures-part-two); [#37 Failbetter Games](https://www.failbettergames.com/news/storynexus-developer-diary-2-fewer-spreadsheets-less-swearing)
**Substantive assessment — direct practitioner:** Storylets and QBN are state-conditioned authored structures
**Source-access record:** prior thematic review; source-level access varied (full article, publisher/author abstract, practitioner page, or indexed excerpt). Consult the section-by-section analysis below for the available specificity; full-text access for every named work is **not** asserted.

#### §3.8 — Emergent sequence is a form of participant authorship within a purposefully authored world.

**Representative claim(s):** Human authors define the world, its meaningful structures, conflicts, actors, information, and possibilities; Participants meaningfully author part of the realized narrative by determining which authored forces they encounter, disrupt, combine, or redirect; The realized sequence can emerge through interaction among authored structures without implying that authorship has disappeared.
**Cited in outline:** Support: Louchart et al. (2008), *Purposeful Authoring for Emergent Narrative*.
**Linked source records:** [#57 Louchart, S., Swartjes, I., Kriegel, M., & Aylett, R](https://doi.org/10.1007/978-3-540-89454-4_35)
**Substantive assessment — direct conceptual support:** Louchart et al. explicitly argue that emergent narrative still requires purposeful authored goals/emotions/actions, while realized stories are shaped by interactor decisions. Distinguish designed action range and local drama management from Enclave's broader ambition.
**Source-access record:** author-hosted full-text PDF pp.1–12; principal source documented in the continuation pass: [Source](https://www.macs.hw.ac.uk/~ruth/Papers/narrative/ICIDS08_louchart.pdf). Other listed citations may only have received metadata or abstract-level verification.

#### §3.9 — Authorial leverage should be understood as increased narrative richness for a given amount of authoring work.

**Representative claim(s):** The objective is not merely to reduce the number of explicit branches; Avoiding the full **branching tax** allows creative effort to be spent on richer characters, relationships, factions, consequential information, authored situations, thematic material, and alternative developments; Narrative possibility and richness can grow faster than the labour required to enumerate paths.
**Cited in outline:** Support: Chen, Nelson & Mateas (2009); Nelson, Ashmore & Mateas (2006); Mateas & Stern (2005); Rowe & Lester (2013).
**Linked source records:** [#32 Chen, S., Nelson, M. J., & Mateas, M](https://doi.org/10.1609/aiide.v5i1.12377); [#61 Nelson, M. J., Ashmore, C., & Mateas, M](https://doi.org/10.1609/aiide.v2i1.18761); [#60 Mateas, M., & Stern, A](https://doi.org/10.1609/aiide.v1i1.18722); [#72 Rowe, J. P., & Lester, J. C](https://doi.org/10.1609/aiide.v9i4.12636)
**Substantive assessment — scope narrowed:** Authorial leverage studies do not measure Enclave
**Source-access record:** prior thematic review; source-level access varied (full article, publisher/author abstract, practitioner page, or indexed excerpt). Consult the section-by-section analysis below for the available specificity; full-text access for every named work is **not** asserted.

#### §3.10 — Existing formalized approaches remain limited by deterministic representation and the historical lack of efficient probabilistic assessment.

**Representative claim(s):** Branches, state machines, storylets, planner actions, drama-manager interventions, and other formal structures can only react to possibilities represented in their state, rules, content, or transition models; They remain bounded by what has been explicitly formalized; The limitation is not only branching itself, but the need for deterministic machinery to decide in advance what situations mean and what responses are available.
**Cited in outline:** Support: Nelson, Ashmore & Mateas (2006); Mateas & Stern (2005); Rowe & Lester (2013); Short (2019); Failbetter Games.
**Linked source records:** [#61 Nelson, M. J., Ashmore, C., & Mateas, M](https://doi.org/10.1609/aiide.v2i1.18761); [#60 Mateas, M., & Stern, A](https://doi.org/10.1609/aiide.v1i1.18722); [#72 Rowe, J. P., & Lester, J. C](https://doi.org/10.1609/aiide.v9i4.12636); [#78 Short, E](https://emshort.blog/2019/11/29/storylets-you-want-them/); [#36 Failbetter Games](https://www.failbettergames.com/news/echo-bazaar-narrative-structures-part-two)
**Substantive assessment — historical claim unproven:** Research cited concerns specific architectures, not exhaustive historical absence of general probabilistic assessment
**Source-access record:** prior thematic review; source-level access varied (full article, publisher/author abstract, practitioner page, or indexed excerpt). Consult the section-by-section analysis below for the available specificity; full-text access for every named work is **not** asserted.


### Section 4 — cited-subsection findings

#### §4.1 — The branching problem is fundamentally a state-space problem, not merely a tree-of-scenes problem.

**Representative claim(s):** Every consequential participant action can alter multiple dimensions of narrative state: relationships, knowledge, beliefs, resources, locations, faction conditions, event eligibility, and future opportunities; Two stories that arrive at the same nominal scene may represent materially different narrative states; As those dimensions accumulate, the number of meaningful combinations grows rapidly.
**Cited in outline:** Support: Jones (2022); Jones & Millard (2024); Fisher (2022).
**Linked source records:** [#51 Jones, J. D](https://doi.org/10.1007/978-3-031-05214-9_4); [#52 Jones, J. D., & Millard, D. E](https://doi.org/10.1145/3648188.3675134); [#38 Fisher, M](https://doi.org/10.1609/aiide.v18i1.21979)
**Substantive assessment — qualified formalization support:** Jones supports combinatorial state burden, Fisher describes state abstraction for narrative planning; the broader claim that all divergence is fundamentally a state-space problem is a mathematical framing, not a specific measured theorem.
**Source-access record:** publisher abstract plus authorial-burden sources; principal source documented in the continuation pass: [Source](https://ojs.aaai.org/index.php/AIIDE/article/view/21979). Other listed citations may only have received metadata or abstract-level verification.

#### §4.2 — Persistent consequence creates the branching tax.

**Representative claim(s):** If earlier actions continue to matter, later narrative material must remain compatible with combinations of earlier state; Cost includes conditional logic, state tracking, alternate dialogue, actor behavior, testing, recovery paths, and content needed to keep divergent states meaningful; Reconvergence reduces that cost precisely because it collapses some persistent divergence.
**Cited in outline:** Support: Jones (2022); Jones & Millard (2024); Alexander (2010), *Node-Based Scenario Design – Part 2: Choose Your Own Adventure*.
**Linked source records:** [#51 Jones, J. D](https://doi.org/10.1007/978-3-031-05214-9_4); [#52 Jones, J. D., & Millard, D. E](https://doi.org/10.1145/3648188.3675134); [#7 Alexander, J](https://thealexandrian.net/wordpress/7961/roleplaying-games/node-based-scenario-design-part-2-choose-your-own-adventure)
**Substantive assessment — direct plus synthesis:** Jones establishes branching and combinatorial burden, and Alexander explains exponential choose-your-own structures; 'branching tax' and exactly which costs persist are Enclave's synthesized terminology.
**Source-access record:** original practitioner article plus Jones research excerpts; principal source documented in the continuation pass: [Source](https://thealexandrian.net/wordpress/7961/roleplaying-games/node-based-scenario-design-part-2-choose-your-own-adventure). Other listed citations may only have received metadata or abstract-level verification.

#### §4.3 — Replacing explicit branches with planning or simulation does not remove the underlying representation problem.

**Representative claim(s):** A planner can generate sequences that were not individually authored as paths; It still needs actions, predicates, objects, relationships, preconditions, and effects represented in a machine-readable domain; The combinatorial problem can be moved into a formal model without disappearing.
**Cited in outline:** Support: Porteous et al. (2021); Hayton et al. (2020); Fisher (2022).
**Linked source records:** [#66 Porteous, J., Ferreira, J. F., Lindsay, A., & Cavazza, ](https://doi.org/10.1007/s10458-021-09501-1); [#43 Hayton, T., Porteous, J., Ferreira, J., & Lindsay, A](https://doi.org/10.1609/aaai.v34i02.5534); [#38 Fisher, M](https://doi.org/10.1609/aiide.v18i1.21979)
**Substantive assessment — direct support:** Narrative planning domain modeling bottleneck established by Hayton and Porteous
**Source-access record:** prior thematic review; source-level access varied (full article, publisher/author abstract, practitioner page, or indexed excerpt). Consult the section-by-section analysis below for the available specificity; full-text access for every named work is **not** asserted.

#### §4.4 — Traditional computational architectures are useful foundations and stepping stones toward richer reactive systems.

**Representative claim(s):** Finite-state machines, behavior trees, planners, drama managers, state-conditioned content, and related techniques provide valuable ways to structure, reuse, constrain, and compose behavior; Drama management and narrative planning improve authorial leverage by selecting, combining, or sequencing authored structures at runtime; These approaches provide deterministic structure, compositional machinery, and authorial control that remain useful.
**Cited in outline:** Support: Iovino et al. (2022); Riedl & Bulitko (2013); Nelson, Ashmore & Mateas (2006); Rowe & Lester (2013); Short (2019); Failbetter Games.
**Linked source records:** [#47 Iovino, M., Scukins, E., Styrud, J., Ögren, P., & Smith](https://doi.org/10.1016/j.robot.2022.104096); [#71 Riedl, M. O., & Bulitko, V](https://doi.org/10.1609/aimag.v34i1.2449); [#61 Nelson, M. J., Ashmore, C., & Mateas, M](https://doi.org/10.1609/aiide.v2i1.18761); [#72 Rowe, J. P., & Lester, J. C](https://doi.org/10.1609/aiide.v9i4.12636); [#78 Short, E](https://emshort.blog/2019/11/29/storylets-you-want-them/)
**Substantive assessment — direct support:** Iovino documents finite-state-machine modularity/scalability issues motivating BTs
**Source-access record:** prior thematic review; source-level access varied (full article, publisher/author abstract, practitioner page, or indexed excerpt). Consult the section-by-section analysis below for the available specificity; full-text access for every named work is **not** asserted.

#### §4.5 — Interactive systems commonly manage complexity by collapsing causal possibility.

**Representative claim(s):** Branches reconverge; Decisions produce temporary variations but return to common states; Side stories remain isolated from the principal narrative.
**Cited in outline:** Support: Stang (2019); Evans (2024).
**Linked source records:** [#82 Stang, S](https://gamestudies.org/1901/articles/stang); [#35 Evans, M](https://gamestudies.org/2404/articles/evans)
**Substantive assessment — bounded case study:** Stang documents reconvergence in named games; Evans documents exploratory activity around constrained authored plots in Subnautica. The word 'commonly' is not a measured prevalence estimate.
**Source-access record:** original full HTML and Evans article; principal source documented in the continuation pass: [Source](https://gamestudies.org/1901/articles/stang). Other listed citations may only have received metadata or abstract-level verification.

#### §4.6 — Perceived agency can compensate for limited causal agency, but that simulation weakens across successive replays.

**Representative claim(s):** Actual or theoretical agency and perceived agency are distinct; Adaptive presentation or reconverging structures can increase perceived agency without proportionally increasing causal freedom; Repeated outcomes, invariant states, and recurring reconvergence become more visible across replay.
**Cited in outline:** Support: Day & Zhu (2017); Thue et al. (2011); Stang (2019). **Audit finding:** cited studies do not verify the replay-specific claim.
**Linked source records:** [#34 Day, T., & Zhu, J](https://doi.org/10.1145/3102071.3106363); [#86 Thue, D., Bulitko, V., Spetch, M., & Romanuik, T](https://doi.org/10.1609/aiide.v7i1.12437); [#82 Stang, S](https://gamestudies.org/1901/articles/stang)
**Substantive assessment — replay hypothesis unresolved after focused 2026-10-09 literature pass:** Day & Zhu, Thue and Stang do not measure repeat-playthrough decline. Roth et al. (2012) instead find increased second-play effectance in *Façade*; Roth & Vermeulen (2013) find altered behavior in the same sample. Fendt et al. (2012) and Cardona-Rivera et al. (2014) show agency-related effects of feedback and anticipated outcomes on single playthroughs. **None directly tests the effect of discovering reconvergent choices through replay.** See focused resolution R1 above.
**Source-access record:** prior thematic review; source-level access varied (full article, publisher/author abstract, practitioner page, or indexed excerpt). Consult the section-by-section analysis below for the available specificity; full-text access for every named work is **not** asserted.

#### §4.7 — The deeper historical bottleneck was explicit formalization.

**Representative claim(s):** Traditional software can execute substantial complexity once meaning has been translated into states, actions, rules, predicates, transitions, or behaviors; The difficult part is turning unforeseen human action or ambiguous social situations into those formal structures; A human gamemaster can interpret intent, determine relevance, consider actor knowledge and goals, judge plausible responses, and decide which rules apply without enumerating those interpretations in advance.
**Cited in outline:** Support: Fisher (2022); Porteous et al. (2021); Hayton et al. (2020); Iovino et al. (2022); Hogan & Brennen (2024).
**Linked source records:** [#38 Fisher, M](https://doi.org/10.1609/aiide.v18i1.21979); [#66 Porteous, J., Ferreira, J. F., Lindsay, A., & Cavazza, ](https://doi.org/10.1007/s10458-021-09501-1); [#43 Hayton, T., Porteous, J., Ferreira, J., & Lindsay, A](https://doi.org/10.1609/aaai.v34i02.5534); [#47 Iovino, M., Scukins, E., Styrud, J., Ögren, P., & Smith](https://doi.org/10.1016/j.robot.2022.104096); [#44 Hogan, D. P., & Brennen, A](https://doi.org/10.48550/arXiv.2404.11446)
**Substantive assessment — bounded historical inference:** Fisher/Porteous/Hayton show domain-model and operator-authoring requirements, and Iovino surveys pre-LLM control formalisms. They do not establish the sole/deepest bottleneck throughout all historical computing or empirically quantify GM equivalence.
**Source-access record:** Porteous full PDF; Hayton/Fisher abstracts; Iovino full survey; principal source documented in the continuation pass: [Source](https://joaoff.com/publication/2021/JAAMAS/jaamas21-modelext.pdf). Other listed citations may only have received metadata or abstract-level verification.

#### §4.8 — Modern probabilistic models materially change what must be formalized in advance.

**Representative claim(s):** Models can interpret open-ended situations, retrieve contextual information, reason over prose descriptions, propose actions, and synthesize plausible candidate events or developments that were not individually enumerated beforehand; This is not limited to language models; Probabilistic judgment can extend the reachable possibility space without requiring every interpretation, actor response, or candidate development to be hand-authored as a branch or symbolic rule.
**Cited in outline:** Support: Park et al. (2023); Hu et al. (2024/2026); Hogan & Brennen (2024).
**Linked source records:** [#65 Park, J. S., O'Brien, J. C., Cai, C. J., Morris, M. R.,](https://doi.org/10.1145/3586183.3606763); [#46 Hu, S., Huang, T., Liu, G., Kompella, R. R., Ilhan, F.,](https://doi.org/10.48550/arXiv.2404.02039); [#44 Hogan, D. P., & Brennen, A](https://doi.org/10.48550/arXiv.2404.11446)
**Substantive assessment — narrow scope:** Park and Hogan demonstrate specific open-ended interactions, not unrestricted feasible actions
**Source-access record:** prior thematic review; source-level access varied (full article, publisher/author abstract, practitioner page, or indexed excerpt). Consult the section-by-section analysis below for the available specificity; full-text access for every named work is **not** asserted.

#### §4.9 — Probabilistic flexibility does not by itself solve narrative authority.

**Representative claim(s):** A model that can plausibly infer or synthesize what might happen can also invent events, actions, facts, or consequences that were never established; Believable behavior is not authoritative causal correctness; Explicit authority boundaries remain necessary.
**Cited in outline:** Support: Hogan & Brennen (2024); Park et al. (2023).
**Linked source records:** [#44 Hogan, D. P., & Brennen, A](https://doi.org/10.48550/arXiv.2404.11446); [#65 Park, J. S., O'Brien, J. C., Cai, C. J., Morris, M. R.,](https://doi.org/10.1145/3586183.3606763)
**Substantive assessment — design synthesis:** Separation from authority is normative; Kambhampati offers external-verifier precedent
**Source-access record:** prior thematic review; source-level access varied (full article, publisher/author abstract, practitioner page, or indexed excerpt). Consult the section-by-section analysis below for the available specificity; full-text access for every named work is **not** asserted.

#### §4.10 — The new opportunity is not to replace deterministic systems, but to augment them and change what they do and how they do it.

**Representative claim(s):** Deterministic systems remain suited to authoritative state, constraints, permissions, event preconditions, persistence, and validated causal effects; Probabilistic systems can handle interpretation, contextual relevance, actor reasoning, plausible intentions, semantic ambiguity, and proposal of responses; Deterministic architectures can shift from enumerating the entire meaningful response space toward validating, constraining, composing, and persisting proposed outcomes.
**Cited in outline:** Support: Marra et al. (2024); Gao et al. (2023); Kambhampati et al. (2024).
**Linked source records:** [#59 Marra, G., Dumančić, S., Manhaeve, R., & De Raedt, L](https://doi.org/10.1016/j.artint.2023.104062); [#39 Gao, L., Madaan, A., Zhou, S., Alon, U., Liu, P., Yang,](https://proceedings.mlr.press/v202/gao23f.html); [#54 Kambhampati, S., Valmeekam, K., Guan, L., Verma, M., St](https://proceedings.mlr.press/v235/kambhampati24a.html)
**Substantive assessment — architectural precedent:** PAL verifies a component-level LLM-to-program-runtime division; LLM-Modulo is explicitly a position paper advocating external verifiers; Marra is a neurosymbolic survey. Enclave's authoritative event handling is an untested transfer.
**Source-access record:** publisher abstracts and position paper; principal source documented in the continuation pass: [Source](https://proceedings.mlr.press/v202/gao23f.html). Other listed citations may only have received metadata or abstract-level verification.

#### §4.11 — The branching problem can therefore be reframed around the computational constraints that branching makes necessary.

**Representative claim(s):** Meaningful divergence creates rapidly increasing combinations of narrative state, authored content, and possible response; Conventional computation historically required much of that meaning to be represented explicitly; Prior narrative architectures remain valuable for reuse, recombination, management, and control.
**Cited in outline:** Support: Marra et al. (2024); Gao et al. (2023); Kambhampati et al. (2024).
**Linked source records:** [#59 Marra, G., Dumančić, S., Manhaeve, R., & De Raedt, L](https://doi.org/10.1016/j.artint.2023.104062); [#39 Gao, L., Madaan, A., Zhou, S., Alon, U., Liu, P., Yang,](https://proceedings.mlr.press/v202/gao23f.html); [#54 Kambhampati, S., Valmeekam, K., Guan, L., Verma, M., St](https://proceedings.mlr.press/v235/kambhampati24a.html)
**Substantive assessment — authorial synthesis:** The combination of formalization constraints and probabilistic proposal/validation is Enclave's reframing. Gao/Kambhampati/Marra give components and philosophy, not an empirically established new boundary for narrative branching.
**Source-access record:** position paper and PAL publisher abstract; principal source documented in the continuation pass: [Source](https://proceedings.mlr.press/v235/kambhampati24a.html). Other listed citations may only have received metadata or abstract-level verification.

#### §4.12 — A Fundamentally Combinatorial Problem Space

**Representative claim(s):** Player agency itself is not the problem; the difficulty comes from attempting to provide **meaningful consequential agency** computationally; Consequential actions can affect world state, relationships, information and beliefs, resources, actor behaviour, future events, and future opportunities; Persistent consequences create new circumstances that later interactions must account for.
**Cited in outline:** Support: Jones (2022); Jones & Millard (2024); Fisher (2022); Porteous et al. (2021); Hayton et al. (2020).
**Linked source records:** [#51 Jones, J. D](https://doi.org/10.1007/978-3-031-05214-9_4); [#52 Jones, J. D., & Millard, D. E](https://doi.org/10.1145/3648188.3675134); [#38 Fisher, M](https://doi.org/10.1609/aiide.v18i1.21979); [#66 Porteous, J., Ferreira, J. F., Lindsay, A., & Cavazza, ](https://doi.org/10.1007/s10458-021-09501-1); [#43 Hayton, T., Porteous, J., Ferreira, J., & Lindsay, A](https://doi.org/10.1609/aaai.v34i02.5534)
**Substantive assessment — logical derivation with precedent:** Jones and formal planning work document branching and state-representation challenges. The precise 'fundamentally combinatorial' result depends on the state variables included; avoid implying a universal operation count.
**Source-access record:** conference paper excerpts plus planning abstracts; principal source documented in the continuation pass: [Source](https://eprints.soton.ac.uk/500739/1/3648188.3675134.pdf). Other listed citations may only have received metadata or abstract-level verification.

#### §4.13 — Existing Designs Reduce the Problem by Imposing Limits

**Representative claim(s):** Existing systems make the problem tractable by limiting the causal space they must support; Common approaches include:; explicitly branching narratives;.
**Cited in outline:** Support: Stang (2019); Day & Zhu (2017); Thue et al. (2011); Evans (2024); Short (2019); Failbetter Games; Alexander (2010), *Node-Based Scenario Design – Part 2: Choose Your Own Adventure*.
**Linked source records:** [#82 Stang, S](https://gamestudies.org/1901/articles/stang); [#34 Day, T., & Zhu, J](https://doi.org/10.1145/3102071.3106363); [#86 Thue, D., Bulitko, V., Spetch, M., & Romanuik, T](https://doi.org/10.1609/aiide.v7i1.12437); [#35 Evans, M](https://gamestudies.org/2404/articles/evans); [#78 Short, E](https://emshort.blog/2019/11/29/storylets-you-want-them/); [#36 Failbetter Games](https://www.failbettergames.com/news/echo-bazaar-narrative-structures-part-two); [#7 Alexander, J](https://thealexandrian.net/wordpress/7961/roleplaying-games/node-based-scenario-design-part-2-choose-your-own-adventure)
**Substantive assessment — documented patterns not prevalence:** Stang, Day/Zhu and Thue support perceived-vs-theoretical agency and reconvergence; Short and Failbetter support conditional content. These document approaches, not statistically establish common prevalence or exact cost.
**Source-access record:** original Stang article; other abstracts/practitioner sources; principal source documented in the continuation pass: [Source](https://gamestudies.org/1901/articles/stang). Other listed citations may only have received metadata or abstract-level verification.

#### §4.14 — Scale Exacerbates the Issue

**Representative claim(s):** Larger game spaces create more actors, locations, objects, institutions, relationships, and possible consequences; The limitation is **not simply the amount of state that can be stored**; Computational systems can maintain enormous persistent worlds.
**Cited in outline:** Support: Fisher (2022); Porteous et al. (2021); Hayton et al. (2020); Iovino et al. (2022); Riedl & Bulitko (2013); Hogan & Brennen (2024).
**Linked source records:** [#38 Fisher, M](https://doi.org/10.1609/aiide.v18i1.21979); [#66 Porteous, J., Ferreira, J. F., Lindsay, A., & Cavazza, ](https://doi.org/10.1007/s10458-021-09501-1); [#43 Hayton, T., Porteous, J., Ferreira, J., & Lindsay, A](https://doi.org/10.1609/aaai.v34i02.5534); [#47 Iovino, M., Scukins, E., Styrud, J., Ögren, P., & Smith](https://doi.org/10.1016/j.robot.2022.104096); [#71 Riedl, M. O., & Bulitko, V](https://doi.org/10.1609/aimag.v34i1.2449); [#44 Hogan, D. P., & Brennen, A](https://doi.org/10.48550/arXiv.2404.11446)
**Substantive assessment — architectural inference:** Planning and BT papers support that represented actions/operators impose a finite actionable vocabulary; MMO-size persistent state and its economic scaling are separate assertions not benchmarked by these citations.
**Source-access record:** Iovino full HTML plus planning papers; principal source documented in the continuation pass: [Source](https://arxiv.org/html/2005.05842v2). Other listed citations may only have received metadata or abstract-level verification.

#### §4.15 — The Analog Solution

**Representative claim(s):** Tabletop and in-person gaming have addressed this problem for decades through the **Gamemaster**; A GM does not need every participant action to have been anticipated beforehand; Instead, the GM interprets attempted action in relation to:.
**Cited in outline:** Support: Alexander (2009), *Don’t Prep Plots*; Alexander (2015), *Tools, Not Contingencies*; Alexander (2009), scenario timelines; Alexander (2012), *Game Structures*; Alexander (2020), *The Secret Life of Nodes*; Hogan & Brennen (2024).
**Linked source records:** [#4 Alexander, J](https://thealexandrian.net/wordpress/4147/roleplaying-games/dont-prep-plots); [#14 Alexander, J](https://thealexandrian.net/wordpress/37422/roleplaying-games/dont-prep-plots-tools-not-contingencies); [#5 Alexander, J](https://thealexandrian.net/wordpress/4154/roleplaying-games/dont-prep-plots-prepping-scenario-timelines); [#13 Alexander, J](https://thealexandrian.net/wordpress/15126/roleplaying-games/game-structures); [#22 Alexander, J](https://thealexandrian.net/wordpress/45263/roleplaying-games/the-secret-life-of-nodes); [#44 Hogan, D. P., & Brennen, A](https://doi.org/10.48550/arXiv.2404.11446)
**Substantive assessment — direct practitioner analogy:** Alexander's situation prep, scenario timelines and game structures describe a GM's adaptation to unanticipated actions. This is practical gamemastering guidance, not proof of AI parity or scalable automation.
**Source-access record:** original full practitioner pages; principal source documented in the continuation pass: [Source](https://thealexandrian.net/wordpress/4147/roleplaying-games/dont-prep-plots). Other listed citations may only have received metadata or abstract-level verification.

#### §4.16 — The Prohibitive Costs of Persistent Human Labour

**Representative claim(s):** Human Gamemasters provide the interpretive flexibility required for broad agency; They do not scale like computational worlds; Human availability is constrained by working hours, attention, concurrency, memory, and server/geographic coverage.
**Cited in outline:** Support: Brown (2000); *Reab v. Electronic Arts* (2002); Thompson (2009); Williams (2009); Park (2003).
**Linked source records:** [#27 Brown, J](https://www.salon.com/2000/09/21/ultima_volunteers/); [#70 Reab v. Electronic Arts, Inc., 214 F.R.D. 623](https://calculators.law/caselaw/decisions/5qJNjDQ68kap/reab-v-electronic-arts-inc); [#85 Thompson, R](https://www.mmorpg.com/editorials/why-mxo-live-content-worked-2000117124); [#90 Williams, S](https://www.mmorpg.com/editorials/another-perspective-on-live-content-2000117156); [#64 Park, A](https://www.gamespot.com/articles/asherons-call/1100-2655688/)
**Substantive assessment — narrow scope:** UO counselors primarily support; Matrix Online accounts are retrospective
**Source-access record:** prior thematic review; source-level access varied (full article, publisher/author abstract, practitioner page, or indexed excerpt). Consult the section-by-section analysis below for the available specificity; full-text access for every named work is **not** asserted.

#### §4.17 — Machine Intelligence as Actors and Situational Overseers

**Representative claim(s):** Modern probabilistic systems can perform many operations that previously required human interpretation; They can:; interpret open-ended actions;.
**Cited in outline:** Support: Park et al. (2023); Hu et al. (2024/2026); Hogan & Brennen (2024); Tian et al. (2024) as secondary support for local generative competence.
**Linked source records:** [#65 Park, J. S., O'Brien, J. C., Cai, C. J., Morris, M. R.,](https://doi.org/10.1145/3586183.3606763); [#46 Hu, S., Huang, T., Liu, G., Kompella, R. R., Ilhan, F.,](https://doi.org/10.48550/arXiv.2404.02039); [#44 Hogan, D. P., & Brennen, A](https://doi.org/10.48550/arXiv.2404.11446); [#87 Tian, Y., Huang, T., Liu, M., Jiang, D., Spangher, A., ](https://doi.org/10.18653/v1/2024.emnlp-main.978)
**Substantive assessment — bounded precedent:** Park et al. (2023) demonstrate believable coordination in a 25-agent social sandbox; Hogan & Brennen (2024) report bounded qualitative wargame cases. Neither establishes historical human-GM labor removal at persistent-world scale; the proposed scope adjustment was reverted from the outline and remains an open recommendation.
**Source-access record:** prior thematic review; source-level access varied (full article, publisher/author abstract, practitioner page, or indexed excerpt). Consult the section-by-section analysis below for the available specificity; full-text access for every named work is **not** asserted.


### Section 5 — cited-subsection findings

#### §5.1 — The Agency

**Representative claim(s):** Machine intelligence removes much of the historical interaction constraint; LLMs can interpret actions that were never explicitly represented beforehand; They can reason over circumstances, intent, motivation, and context without requiring every interpretation to exist as a predefined computational rule.
**Cited in outline:** Support: Hogan & Brennen (2024); Park et al. (2023); Hu et al. (2024/2026); Porteous et al. (2021); Hayton et al. (2020).
**Linked source records:** [#44 Hogan, D. P., & Brennen, A](https://doi.org/10.48550/arXiv.2404.11446); [#65 Park, J. S., O'Brien, J. C., Cai, C. J., Morris, M. R.,](https://doi.org/10.1145/3586183.3606763); [#46 Hu, S., Huang, T., Liu, G., Kompella, R. R., Ilhan, F.,](https://doi.org/10.48550/arXiv.2404.02039); [#66 Porteous, J., Ferreira, J. F., Lindsay, A., & Cavazza, ](https://doi.org/10.1007/s10458-021-09501-1); [#43 Hayton, T., Porteous, J., Ferreira, J., & Lindsay, A](https://doi.org/10.1609/aaai.v34i02.5534)
**Substantive assessment — bounded precedent:** LLM-mediated natural-language action interpretation has bounded empirical precedents (Park et al. 2023; Hogan & Brennen 2024); human-GM parity and removal of broad interaction constraints remain unverified. The proposed conditional wording was reverted from the outline and remains an open recommendation.
**Source-access record:** prior thematic review; source-level access varied (full article, publisher/author abstract, practitioner page, or indexed excerpt). Consult the section-by-section analysis below for the available specificity; full-text access for every named work is **not** asserted.

#### §5.2 — Expanded Agency

**Representative claim(s):** Participants no longer necessarily need to express consequential actions through a predefined interaction vocabulary; The system can potentially interpret what they are trying to accomplish and relate it to existing circumstances; Actors can likewise react to combinations of circumstances that were never specifically scripted.
**Cited in outline:** Support: Hogan & Brennen (2024); Park et al. (2023); Alexander (2009/2015).
**Linked source records:** [#44 Hogan, D. P., & Brennen, A](https://doi.org/10.48550/arXiv.2404.11446); [#65 Park, J. S., O'Brien, J. C., Cai, C. J., Morris, M. R.,](https://doi.org/10.1145/3586183.3606763); [#4 Alexander, J](https://thealexandrian.net/wordpress/4147/roleplaying-games/dont-prep-plots)
**Substantive assessment — design hypothesis from precedents:** Park and Snow Globe demonstrate language-mediated action in limited environments, while Alexander describes flexible human facilitation. Unrestricted consequential interpretation or indefinite simulation remains an Enclave hypothesis.
**Source-access record:** author abstract and bounded agent demonstrations; principal source documented in the continuation pass: [Source](https://arxiv.org/abs/2404.11446). Other listed citations may only have received metadata or abstract-level verification.

#### §5.3 — The Persistence

**Representative claim(s):** **Extensive agency produces extensive persistent consequences and extensive persistence requirements.**; For interactions to be meaningful, their outcomes must persist beyond the duration of the model call; Novel actions may change state, knowledge, beliefs, relationships, possessions, plans, institutions, future event eligibility, and later actor reactions.
**Cited in outline:** Support: Park et al. (2023); Wu et al. (2025), *LongMemEval*; Jones (2022); Jones & Millard (2024); Fisher (2022).
**Linked source records:** [#65 Park, J. S., O'Brien, J. C., Cai, C. J., Morris, M. R.,](https://doi.org/10.1145/3586183.3606763); [#91 Wu, D., Wang, H., Yu, W., Zhang, Y., Chang, K.-W., & Yu](https://proceedings.iclr.cc/paper_files/paper/2025/hash/d813d324dbf0598bbdc9c8e79740ed01-Abstract-Conference.html); [#51 Jones, J. D](https://doi.org/10.1007/978-3-031-05214-9_4); [#52 Jones, J. D., & Millard, D. E](https://doi.org/10.1145/3648188.3675134); [#38 Fisher, M](https://doi.org/10.1609/aiide.v18i1.21979)
**Substantive assessment — logical architecture not measurement:** Maintaining durable world consequences plausibly requires persistent records beyond model calls. Park's memory loop and LongMemEval's dialogue tasks support motivation, but do not measure bytes per meaningful interaction or Enclave history growth.
**Source-access record:** author abstracts, LongMemEval benchmark synopsis; principal source documented in the continuation pass: [Source](https://arxiv.org/abs/2304.03442). Other listed citations may only have received metadata or abstract-level verification.

#### §5.4 — LLMs Are Poorly Suited to Maintaining State

**Representative claim(s):** LLMs are effective interpreters of state but unreliable custodians of it; Their active context is finite; Long-running worlds can produce far more relevant history than can remain active simultaneously.
**Cited in outline:** Support: Liu et al. (2024), *Lost in the Middle*; Bai et al. (2024), *LongBench*; Hsieh et al. (2024), *RULER*; Wu et al. (2025), *LongMemEval*; Hogan & Brennen (2024).
**Linked source records:** [#55 Liu, N. F., Lin, K., Hewitt, J., Paranjape, A., Bevilac](https://doi.org/10.1162/tacl_a_00638); [#25 Bai, Y., Lv, X., Zhang, J., Lyu, H., Tang, J., Huang, Z](https://doi.org/10.18653/v1/2024.acl-long.172); [#45 Hsieh, C.-P., Sun, S., Kriman, S., Acharya, S., Rekesh,](https://arxiv.org/abs/2404.06654); [#91 Wu, D., Wang, H., Yu, W., Zhang, Y., Chang, K.-W., & Yu](https://proceedings.iclr.cc/paper_files/paper/2025/hash/d813d324dbf0598bbdc9c8e79740ed01-Abstract-Conference.html); [#44 Hogan, D. P., & Brennen, A](https://doi.org/10.48550/arXiv.2404.11446)
**Substantive assessment — direct support bounded:** Liu/Wu/Hsieh/Bai benchmark imperfect context use; no proof all LLMs fail every state task
**Source-access record:** prior thematic review; source-level access varied (full article, publisher/author abstract, practitioner page, or indexed excerpt). Consult the section-by-section analysis below for the available specificity; full-text access for every named work is **not** asserted.

#### §5.5 — Naive Applications Create Linear Storage Problems

**Representative claim(s):** If every consequential interaction generates retained information and that information is not discarded, historical storage grows at least proportionally with consequential interaction count: **O(N) retained history** in the naive case; Long-running actors accumulate observations, relationships, beliefs, decisions, event histories, provenance, and state transitions; Actor-specific references, indexes, derived state, and propagation metadata can add further overhead.
**Cited in outline:** Support: Wu et al. (2025), *LongMemEval*; Park et al. (2023); Packer et al. (2023), *MemGPT*; PostgreSQL storage-page and TOAST documentation; SQLite database file-format documentation.
**Linked source records:** [#91 Wu, D., Wang, H., Yu, W., Zhang, Y., Chang, K.-W., & Yu](https://proceedings.iclr.cc/paper_files/paper/2025/hash/d813d324dbf0598bbdc9c8e79740ed01-Abstract-Conference.html); [#65 Park, J. S., O'Brien, J. C., Cai, C. J., Morris, M. R.,](https://doi.org/10.1145/3586183.3606763); [#63 Packer, C., Wooders, S., Lin, K., Fang, V., Patil, S. G](https://arxiv.org/abs/2310.08560); [#67 PostgreSQL Global Development Group](https://www.postgresql.org/docs/current/storage-page-layout.html); [#68 PostgreSQL Global Development Group](https://www.postgresql.org/docs/current/storage-toast.html); [#81 SQLite](https://www.sqlite.org/fileformat.html)
**Substantive assessment — logical deduction:** O(N) storage growth follows stipulated record retention; PostgreSQL/SQLite support overhead only
**Source-access record:** prior thematic review; source-level access varied (full article, publisher/author abstract, practitioner page, or indexed excerpt). Consult the section-by-section analysis below for the available specificity; full-text access for every named work is **not** asserted.

#### §5.6 — The Gap

**Representative claim(s):** **This is the Agency–Persistence Gap.**; Broad agency requires flexible interpretation of unforeseen actions and circumstances; Meaningful agency requires the consequences of those actions to persist.
**Cited in outline:** Support: Enclave synthesis drawing on Hogan & Brennen (2024); Park et al. (2023); Liu et al. (2024); Bai et al. (2024); Hsieh et al. (2024); Wu et al. (2025); Fisher (2022); Porteous et al. (2021).
**Linked source records:** [#44 Hogan, D. P., & Brennen, A](https://doi.org/10.48550/arXiv.2404.11446); [#65 Park, J. S., O'Brien, J. C., Cai, C. J., Morris, M. R.,](https://doi.org/10.1145/3586183.3606763); [#55 Liu, N. F., Lin, K., Hewitt, J., Paranjape, A., Bevilac](https://doi.org/10.1162/tacl_a_00638); [#25 Bai, Y., Lv, X., Zhang, J., Lyu, H., Tang, J., Huang, Z](https://doi.org/10.18653/v1/2024.acl-long.172); [#45 Hsieh, C.-P., Sun, S., Kriman, S., Acharya, S., Rekesh,](https://arxiv.org/abs/2404.06654); [#91 Wu, D., Wang, H., Yu, W., Zhang, Y., Chang, K.-W., & Yu](https://proceedings.iclr.cc/paper_files/paper/2025/hash/d813d324dbf0598bbdc9c8e79740ed01-Abstract-Conference.html); [#38 Fisher, M](https://doi.org/10.1609/aiide.v18i1.21979); [#66 Porteous, J., Ferreira, J. F., Lindsay, A., & Cavazza, ](https://doi.org/10.1007/s10458-021-09501-1)
**Substantive assessment — novel authorial synthesis:** Agency–Persistence Gap is explicitly Enclave's coined analytic synthesis joining agent flexibility, memory limits and symbolic narrative models; none of the citations independently names or validates the entire construct.
**Source-access record:** combined existing individual empirical abstracts and formal-planning precedents; principal source documented in the continuation pass: [Source](https://aclanthology.org/2024.tacl-1.9/). Other listed citations may only have received metadata or abstract-level verification.

#### §5.7 — Fertile Ground

**Representative claim(s):** **This leaves us with two unusually complementary systems.**; durable persistence;; exact representation;.
**Cited in outline:** Support: Cowan (2001); Oberauer et al. (2016); Schacter & Addis (2007); Schacter (2012); Johnson, Hashtroudi & Lindsay (1993); Buschman (2021); Liu et al. (2024); Hsieh et al. (2024); Wu et al. (2025); Gao et al. (2023), *PAL*; Kambhampati et al. (2024), *LLM-Modulo*; Marra et al. (2024).
**Linked source records:** [#33 Cowan, N](https://doi.org/10.1017/S0140525X01003922); [#62 Oberauer, K., Farrell, S., Jarrold, C., & Lewandowsky, ](https://doi.org/10.1037/bul0000046); [#75 Schacter, D. L., & Addis, D. R](https://doi.org/10.1098/rstb.2007.2087); [#74 Schacter, D. L](https://doi.org/10.31887/DCNS.2012.14.1/dschacter); [#49 Johnson, M. K., Hashtroudi, S., & Lindsay, D. S](https://doi.org/10.1037/0033-2909.114.1.3); [#29 Buschman, T. J](https://doi.org/10.1146/annurev-vision-100419-104831); [#55 Liu, N. F., Lin, K., Hewitt, J., Paranjape, A., Bevilac](https://doi.org/10.1162/tacl_a_00638)
**Substantive assessment — cross domain analogy:** Human memory psychology is analogy, not proof of equivalence to LLM failure
**Source-access record:** prior thematic review; source-level access varied (full article, publisher/author abstract, practitioner page, or indexed excerpt). Consult the section-by-section analysis below for the available specificity; full-text access for every named work is **not** asserted.

#### §5.8 — Enclave as an Architectural Response

**Representative claim(s):** Enclave treats the Agency–Persistence Gap as an **architectural boundary**, not as something that can simply be eliminated with a larger model or larger context window; It combines:; persistent computational state;.
**Cited in outline:** Support: Gao et al. (2023), *PAL*; Kambhampati et al. (2024), *LLM-Modulo*; Marra et al. (2024); Hogan & Brennen (2024); Park et al. (2023).
**Linked source records:** [#39 Gao, L., Madaan, A., Zhou, S., Alon, U., Liu, P., Yang,](https://proceedings.mlr.press/v202/gao23f.html); [#54 Kambhampati, S., Valmeekam, K., Guan, L., Verma, M., St](https://proceedings.mlr.press/v235/kambhampati24a.html); [#59 Marra, G., Dumančić, S., Manhaeve, R., & De Raedt, L](https://doi.org/10.1016/j.artint.2023.104062); [#44 Hogan, D. P., & Brennen, A](https://doi.org/10.48550/arXiv.2404.11446); [#65 Park, J. S., O'Brien, J. C., Cai, C. J., Morris, M. R.,](https://doi.org/10.1145/3586183.3606763)
**Substantive assessment — architectural design not tested:** PAL, LLM-Modulo and Marra support division of probabilistic proposals from trusted execution or verification. This motivates Enclave's architecture without establishing its correctness, completeness or efficiency.
**Source-access record:** primary abstracts/position/survey; principal source documented in the continuation pass: [Source](https://proceedings.mlr.press/v202/gao23f.html). Other listed citations may only have received metadata or abstract-level verification.


### Section 6 — cited-subsection findings

#### §6.1 — Sandboxing the World Is Already Highly Developed

**Representative claim(s):** Modern games can support very large spaces of participant action without individually authoring every resulting world configuration; Developers define systems, objects, rules, constraints, and affordances; players combine those elements during play; Runtime interaction can therefore generate valid world states and events that were never individually enumerated beforehand.
**Cited in outline:** Support: Juul (2002), *The Open and the Closed*; Soler-Adillon (2019), *The Open, the Closed and the Emergent*.
**Linked source records:** [#53 Juul, J](https://doi.org/10.26503/dl.v2002i1.9); [#79 Soler-Adillon, J](https://gamestudies.org/1902/articles/soleradillon)
**Substantive assessment — conceptual support:** Juul emergence/progression concept; not measurement of modern sandbox maturity
**Source-access record:** prior thematic review; source-level access varied (full article, publisher/author abstract, practitioner page, or indexed excerpt). Consult the section-by-section analysis below for the available specificity; full-text access for every named work is **not** asserted.

#### §6.2 — Sandbox Systems Already Accommodate Genuine Emergence

**Representative claim(s):** Supported systems can interact in combinations nobody explicitly scripted; A resulting event does not need to have existed as a specific authored branch to be valid if it follows from the underlying systems; Simulation-heavy games can produce character histories, conflicts, losses, alliances, strategic reversals, and other events from systemic interaction.
**Cited in outline:** Support: Juul (2002); Ryan (2018), *Curating Simulated Storyworlds*; Adams (2021), *Characterization and Emergent Narrative in Dwarf Fortress*; Burgess & Jones (2023), *Exploring how players use emergent narrative in strategy games*; Johnson-Bey, Nelson & Mateas (2022), *Neighborly*.
**Linked source records:** [#53 Juul, J](https://doi.org/10.26503/dl.v2002i1.9); [#73 Ryan, J](https://escholarship.org/uc/item/1340j5h2); [#1 Adams, T](https://doi.org/10.1515/9783839453452-007); [#28 Burgess, J., & Jones, C. M](https://doi.org/10.1016/j.entcom.2022.100533); [#50 Johnson-Bey, S., Nelson, M. J., & Mateas, M](https://doi.org/10.1109/CoG51982.2022.9893631)
**Substantive assessment — direct support:** Juul, Adams and Neighborly demonstrate systemic/emergent narrative
**Source-access record:** prior thematic review; source-level access varied (full article, publisher/author abstract, practitioner page, or indexed excerpt). Consult the section-by-section analysis below for the available specificity; full-text access for every named work is **not** asserted.

#### §6.3 — Existing Sandboxes Still Operate Through a Bounded Interaction Vocabulary

**Representative claim(s):** Sandbox capability is not literal unlimited freedom; The world can only directly resolve properties, actions, and interactions represented by its computational systems; A finite ruleset may produce enormous variation while still defining the vocabulary through which that variation occurs.
**Cited in outline:** Support: Juul (2002); Soler-Adillon (2019); Fisher (2022); Porteous et al. (2021); Hayton et al. (2020); Iovino et al. (2022).
**Linked source records:** [#53 Juul, J](https://doi.org/10.26503/dl.v2002i1.9); [#79 Soler-Adillon, J](https://gamestudies.org/1902/articles/soleradillon); [#38 Fisher, M](https://doi.org/10.1609/aiide.v18i1.21979); [#66 Porteous, J., Ferreira, J. F., Lindsay, A., & Cavazza, ](https://doi.org/10.1007/s10458-021-09501-1); [#43 Hayton, T., Porteous, J., Ferreira, J., & Lindsay, A](https://doi.org/10.1609/aaai.v34i02.5534); [#47 Iovino, M., Scukins, E., Styrud, J., Ögren, P., & Smith](https://doi.org/10.1016/j.robot.2022.104096)
**Substantive assessment — formal boundary inference:** Juul/Soler-Adillon discuss broad emergence from bounded rules; narrative planning and BT work operate over implemented operators. The 'bounded interaction vocabulary' conclusion is structural reasoning, not a tested maximum.
**Source-access record:** full original conceptual HTML; model papers; principal source documented in the continuation pass: [Source](https://gamestudies.org/1902/articles/soleradillon). Other listed citations may only have received metadata or abstract-level verification.

#### §6.4 — State Persistence Is Not the Central Sandbox Limitation

**Representative claim(s):** Sandbox worlds can already preserve large quantities of changing state; Objects move, inventories change, resources are consumed, characters die, territories change hands, structures are created or destroyed, and these consequences can remain part of the world; Persistent online worlds further demonstrate that computational state can outlive the interaction or session that created it.
**Cited in outline:** Support: Juul (2002), especially *EverQuest* as a persistent emergent world; existing §5 persistent-world research on *Ultima Online*, *Asheron's Call*, and *The Matrix Online*.
**Linked source records:** [#53 Juul, J](https://doi.org/10.26503/dl.v2002i1.9); [#27 Brown, J](https://www.salon.com/2000/09/21/ultima_volunteers/); [#64 Park, A](https://www.gamespot.com/articles/asherons-call/1100-2655688/)
**Substantive assessment — partial support:** Persistence possible but examples do not establish global centrality of limitation
**Source-access record:** prior thematic review; source-level access varied (full article, publisher/author abstract, practitioner page, or indexed excerpt). Consult the section-by-section analysis below for the available specificity; full-text access for every named work is **not** asserted.

#### §6.5 — Narrative Is Usually Less Sandboxed Than the World

**Representative claim(s):** A game may provide extraordinary systemic freedom while its authored narrative remains comparatively rigid; Modern open-world games commonly combine mechanically rich exploration with a comparatively linear central plot and optional side material; This does **not** mean sandbox systems fail to produce narrative.
**Cited in outline:** Support: Juul (2002); Evans (2024); Ryan (2018); Adams (2021); Burgess & Jones (2023); Grinblat, Manning & Kreminski (2021), *Emergent Narrative and Reparative Play*; Jenkins (2004).
**Linked source records:** [#53 Juul, J](https://doi.org/10.26503/dl.v2002i1.9); [#35 Evans, M](https://gamestudies.org/2404/articles/evans); [#73 Ryan, J](https://escholarship.org/uc/item/1340j5h2); [#1 Adams, T](https://doi.org/10.1515/9783839453452-007); [#28 Burgess, J., & Jones, C. M](https://doi.org/10.1016/j.entcom.2022.100533); [#41 Grinblat, J., Manning, C., & Kreminski, M](https://doi.org/10.1007/978-3-030-92300-6_19)
**Substantive assessment — broad generalization:** Studies distinguish examples but not prevalence of narrative limitations across games
**Source-access record:** prior thematic review; source-level access varied (full article, publisher/author abstract, practitioner page, or indexed excerpt). Consult the section-by-section analysis below for the available specificity; full-text access for every named work is **not** asserted.

#### §6.6 — The Missing Capability Is a Reactive Authored Narrative Sandbox

**Representative claim(s):** Existing research already uses **narrative sandbox** for systems that rely heavily on emergence to produce narrative effects; Enclave's narrower concern is therefore not to claim invention of narrative sandboxing itself; The missing capability identified here is the ability for **deeply authored narrative structures to absorb emergent world events as persistent, meaningful inputs** without requiring every resulting reaction to be explicitly authored beforehand.
**Cited in outline:** Support: Louchart et al. (2008); Jenkins (2004); Short (2019); Failbetter Games; Chen, Nelson & Mateas (2009); Johnson-Bey, Nelson & Mateas (2022); Grinblat, Manning & Kreminski (2021).
**Linked source records:** [#57 Louchart, S., Swartjes, I., Kriegel, M., & Aylett, R](https://doi.org/10.1007/978-3-540-89454-4_35); [#48 Jenkins, H](https://electronicbookreview.com/publications/game-design-as-narrative-architecture/); [#78 Short, E](https://emshort.blog/2019/11/29/storylets-you-want-them/); [#36 Failbetter Games](https://www.failbettergames.com/news/echo-bazaar-narrative-structures-part-two); [#32 Chen, S., Nelson, M. J., & Mateas, M](https://doi.org/10.1609/aiide.v5i1.12377); [#50 Johnson-Bey, S., Nelson, M. J., & Mateas, M](https://doi.org/10.1109/CoG51982.2022.9893631); [#41 Grinblat, J., Manning, C., & Kreminski, M](https://doi.org/10.1007/978-3-030-92300-6_19)
**Substantive assessment — unproven exclusivity:** No exhaustive prior-art proof that architecture is a missing capability
**Source-access record:** prior thematic review; source-level access varied (full article, publisher/author abstract, practitioner page, or indexed excerpt). Consult the section-by-section analysis below for the available specificity; full-text access for every named work is **not** asserted.


### Section 9 — cited-subsection findings

#### §9.3 — Memories

**Representative claim(s):** **Memories** are the persistent record of a particular Actor's interactions, experiences, and identity; Memories preserve the Actor-specific context surrounding what occurred rather than only the transmissible informational content that may be extracted from it; A Memory may contain:.
**Cited in outline:** Support: Tulving (2002); Greenberg & Verfaellie (2010).
**Cited in outline:** **Reference:&#x20;**&#x54;his paper assumes the deployment of a memory architecture similar to the Reliquary system found here: [https://www.github.com/Lokee86/Reliquary](https://www.github.com/Lokee86/Reliquary)
**Linked source records:** [#88 Tulving, E](https://doi.org/10.1146/annurev.psych.53.100901.135114); [#40 Greenberg, D. L., & Verfaellie, M](https://doi.org/10.1017/S1355617710000676)
**Substantive assessment — analogy and architecture:** Episodic/semantic analogy does not validate Enclave primitives
**Source-access record:** prior thematic review; source-level access varied (full article, publisher/author abstract, practitioner page, or indexed excerpt). Consult the section-by-section analysis below for the available specificity; full-text access for every named work is **not** asserted.


### Section 12 — cited-subsection findings

#### §12.1 — Bounded Narrative Agents

**Representative claim(s):** At this point astute readers may have noticed that Enclave's primitives, informational state, Knowledge distribution, Actor relationships, Events, Interactions, and persistent cause and effect can all be represented and resolved through conventional computational systems without probabilistic cognition or resolution; A sufficiently formalized implementation could therefore use Enclave as the informational and causal architecture for a conventional deterministic simulation; The system could even theoretically be applied to a more traditional procedurally generated narrative like those found in Dwarf Fortress.
**Cited in outline:** Support/precedent: Adams (2021); Ryan (2018).
**Cited in outline:** **Support for the underlying memorization risk:** Chang et al. (2023); Carlini et al. (2021).
**Cited in outline:** Support/precedent: Park et al. (2023); Hu et al. (2024; revised 2026); Hogan & Brennen (2024).
**Linked source records:** [#1 Adams, T](https://doi.org/10.1515/9783839453452-007); [#73 Ryan, J](https://escholarship.org/uc/item/1340j5h2); [#31 Chang, K. K., Cramer, M., Soni, S., & Bamman, D](https://doi.org/10.18653/v1/2023.emnlp-main.453); [#30 Carlini, N., Tramèr, F., Wallace, E., Jagielski, M., He](https://www.usenix.org/conference/usenixsecurity21/presentation/carlini-extracting)
**Substantive assessment — bounded support:** Chang/Carlini establish training data memorization possibility, not universal runtime narrative leakage
**Source-access record:** prior thematic review; source-level access varied (full article, publisher/author abstract, practitioner page, or indexed excerpt). Consult the section-by-section analysis below for the available specificity; full-text access for every named work is **not** asserted.

#### §12.2 — The Persistent Cognitive Actor

**Representative claim(s):** The Cognitive Actor is persistent even when no model invocation is active; The model invocation is therefore not the Actor itself, but a temporary cognitive process operating on behalf of that Actor; A Cognitive Actor's persistent state may include:.
**Cited in outline:** Support/precedent: Park et al. (2023); Packer et al. (2023), *MemGPT*; Wu et al. (2025), *LongMemEval*.
**Linked source records:** [#65 Park, J. S., O'Brien, J. C., Cai, C. J., Morris, M. R.,](https://doi.org/10.1145/3586183.3606763); [#63 Packer, C., Wooders, S., Lin, K., Fang, V., Patil, S. G](https://arxiv.org/abs/2310.08560); [#91 Wu, D., Wang, H., Yu, W., Zhang, Y., Chang, K.-W., & Yu](https://proceedings.iclr.cc/paper_files/paper/2025/hash/d813d324dbf0598bbdc9c8e79740ed01-Abstract-Conference.html)
**Substantive assessment — direct precedent:** Park/MemGPT demonstrate external persistent memory pattern, not Enclave
**Source-access record:** prior thematic review; source-level access varied (full article, publisher/author abstract, practitioner page, or indexed excerpt). Consult the section-by-section analysis below for the available specificity; full-text access for every named work is **not** asserted.

#### §12.3 — The Actor's Subjective World

**Representative claim(s):** The authoritative system may represent the complete informational state of the world, but a Cognitive Actor inhabits only a bounded portion of it; The Actor's subjective world is formed from the persistent information that Actor can legitimately know, remember, observe, or access; This may include:.
**Cited in outline:** Support/precedent: Hogan & Brennen (2024), particularly differentiated player history objects and information asymmetry; Park et al. (2023); Hu et al. (2024; revised 2026).
**Linked source records:** [#44 Hogan, D. P., & Brennen, A](https://doi.org/10.48550/arXiv.2404.11446); [#65 Park, J. S., O'Brien, J. C., Cai, C. J., Morris, M. R.,](https://doi.org/10.1145/3586183.3606763); [#46 Hu, S., Huang, T., Liu, G., Kompella, R. R., Ilhan, F.,](https://doi.org/10.48550/arXiv.2404.02039)
**Substantive assessment — partial precedent:** Hogan/Park show differentiated agents; Enclave epistemic enforcement untested
**Source-access record:** prior thematic review; source-level access varied (full article, publisher/author abstract, practitioner page, or indexed excerpt). Consult the section-by-section analysis below for the available specificity; full-text access for every named work is **not** asserted.

#### §12.4 — Memory and Cognition

**Representative claim(s):** Memory and Cognitive Actors are already foundational Enclave concepts; For Cognitive Actors, the Memory primitive necessarily requires a persistent subsystem capable of maintaining Actor-specific experience and state beyond individual inference sessions and making relevant Memory available to cognition; Enclave defines the semantic role of Memory, but it does not need to define the complete internal ontology of the system used to implement it.
**Cited in outline:** Support/precedent: Tulving (2002); Greenberg & Verfaellie (2010); Park et al. (2023); Wu et al. (2025), *LongMemEval*; Packer et al. (2023), *MemGPT*.
**Linked source records:** [#88 Tulving, E](https://doi.org/10.1146/annurev.psych.53.100901.135114); [#40 Greenberg, D. L., & Verfaellie, M](https://doi.org/10.1017/S1355617710000676); [#65 Park, J. S., O'Brien, J. C., Cai, C. J., Morris, M. R.,](https://doi.org/10.1145/3586183.3606763); [#91 Wu, D., Wang, H., Yu, W., Zhang, Y., Chang, K.-W., & Yu](https://proceedings.iclr.cc/paper_files/paper/2025/hash/d813d324dbf0598bbdc9c8e79740ed01-Abstract-Conference.html); [#63 Packer, C., Wooders, S., Lin, K., Fang, V., Patil, S. G](https://arxiv.org/abs/2310.08560)
**Substantive assessment — human memory analogy and agent precedent:** Tulving/Greenberg distinguish episodic and semantic memory in humans; Park, MemGPT and LongMemEval address machine agent history/retrieval. Human-memory theory does not validate Enclave's primitive semantics.
**Source-access record:** MemGPT author abstract; Greenberg publisher abstract; existing cognitive studies; principal source documented in the continuation pass: [Source](https://arxiv.org/abs/2310.08560). Other listed citations may only have received metadata or abstract-level verification.

#### §12.5 — Context Construction

**Representative claim(s):** A Cognitive Actor's complete subjective world will frequently be much larger than the context required, or economically practical, for a single cognitive operation; Context construction therefore creates a bounded working view from that persistent subjective state; It begins by determining what information is available to the Actor and what portions of that information are relevant to the current cognitive operation.
**Cited in outline:** Support: Liu et al. (2024), *Lost in the Middle*; Bai et al. (2024), *LongBench*; Hsieh et al. (2024), *RULER*; Wu et al. (2025), *LongMemEval*; Park et al. (2023); Packer et al. (2023), *MemGPT*.
**Linked source records:** [#55 Liu, N. F., Lin, K., Hewitt, J., Paranjape, A., Bevilac](https://doi.org/10.1162/tacl_a_00638); [#25 Bai, Y., Lv, X., Zhang, J., Lyu, H., Tang, J., Huang, Z](https://doi.org/10.18653/v1/2024.acl-long.172); [#45 Hsieh, C.-P., Sun, S., Kriman, S., Acharya, S., Rekesh,](https://arxiv.org/abs/2404.06654); [#91 Wu, D., Wang, H., Yu, W., Zhang, Y., Chang, K.-W., & Yu](https://proceedings.iclr.cc/paper_files/paper/2025/hash/d813d324dbf0598bbdc9c8e79740ed01-Abstract-Conference.html); [#65 Park, J. S., O'Brien, J. C., Cai, C. J., Morris, M. R.,](https://doi.org/10.1145/3586183.3606763)
**Substantive assessment — architectural recommendation:** Retrieval literature motivates, but does not test this precise context policy
**Source-access record:** prior thematic review; source-level access varied (full article, publisher/author abstract, practitioner page, or indexed excerpt). Consult the section-by-section analysis below for the available specificity; full-text access for every named work is **not** asserted.

#### §12.6 — The Cognitive Cycle

**Representative claim(s):** Cognitive Actors require a mechanism connecting persistent subjective state to temporary cognition and then back to persistent state; A representative cognitive cycle may be:; Different implementations may combine, divide, omit, or deterministically resolve individual stages.
**Cited in outline:** **Support / architectural precedent:** Park et al. (2023); Hogan & Brennen (2024); Gao et al. (2023), *PAL*; Kambhampati et al. (2024), *LLM-Modulo*.
**Linked source records:** [#65 Park, J. S., O'Brien, J. C., Cai, C. J., Morris, M. R.,](https://doi.org/10.1145/3586183.3606763); [#44 Hogan, D. P., & Brennen, A](https://doi.org/10.48550/arXiv.2404.11446); [#39 Gao, L., Madaan, A., Zhou, S., Alon, U., Liu, P., Yang,](https://proceedings.mlr.press/v202/gao23f.html); [#54 Kambhampati, S., Valmeekam, K., Guan, L., Verma, M., St](https://proceedings.mlr.press/v235/kambhampati24a.html)
**Substantive assessment — proposed cycle with precedents:** Park supplies an agent memory/reflection/planning loop; Snow Globe and PAL/LLM-Modulo cover open-ended interaction and verifier separation. The specific Enclave Event validation/commit cycle remains a proposed protocol.
**Source-access record:** author abstracts and position paper; principal source documented in the continuation pass: [Source](https://arxiv.org/abs/2304.03442). Other listed citations may only have received metadata or abstract-level verification.

#### §12.7 — Divided Cognitive Responsibility

**Representative claim(s):** Actor cognition does not require one monolithic probabilistic process; The architecture separates three broad responsibilities:; **Enclave** maintains authoritative world state, Actor-accessible Knowledge, epistemic boundaries, Knowledge-context construction, and Event resolution;.
**Cited in outline:** **Support / architectural precedent:** Gao et al. (2023), *PAL*; Kambhampati et al. (2024), *LLM-Modulo*; Marra et al. (2024); Wu et al. (2025), *LongMemEval*.
**Linked source records:** [#39 Gao, L., Madaan, A., Zhou, S., Alon, U., Liu, P., Yang,](https://proceedings.mlr.press/v202/gao23f.html); [#54 Kambhampati, S., Valmeekam, K., Guan, L., Verma, M., St](https://proceedings.mlr.press/v235/kambhampati24a.html); [#59 Marra, G., Dumančić, S., Manhaeve, R., & De Raedt, L](https://doi.org/10.1016/j.artint.2023.104062); [#91 Wu, D., Wang, H., Yu, W., Zhang, Y., Chang, K.-W., & Yu](https://proceedings.iclr.cc/paper_files/paper/2025/hash/d813d324dbf0598bbdc9c8e79740ed01-Abstract-Conference.html)
**Substantive assessment — direct architectural precedent:** PAL and LLM-Modulo offload reliable execution/verification but not Enclave validation
**Source-access record:** prior thematic review; source-level access varied (full article, publisher/author abstract, practitioner page, or indexed excerpt). Consult the section-by-section analysis below for the available specificity; full-text access for every named work is **not** asserted.


### Section 14 — cited-subsection findings

#### §14.2 — *A Wild Sheep Chase*: The Authored Trajectory

**Representative claim(s):** **Primary source:** Winghorn Press, *A Wild Sheep Chase*, a free single-session D&D 5E adventure for 4th–5th-level parties: https://winghornpress.com/adventures/a-wild-sheep-chase/; The source adventure supplies the authored characters, relationships, conflict, locations, objects, and expected scenario progression used in §§14.2–14.6; the alternate causal sequence in §14.5 is an Enclave demonstration constructed from that authored material; *A Wild Sheep Chase* begins when Finethir Shinebright, a wizard transformed into a sheep, seeks assistance from the Participants.
**Cited in outline:** **Primary source:** Winghorn Press, *A Wild Sheep Chase*, a free single-session D&D 5E adventure for 4th–5th-level parties: https://winghornpress.com/adventures/a-wild-sheep-chase/
**Linked source records:** [Winghorn Press, *A Wild Sheep Chase*](https://winghornpress.com/adventures/a-wild-sheep-chase/)
**Substantive assessment — primary adventure:** Winghorn authored adventure provides the fictional reference, not an Enclave implementation
**Source-access record:** prior thematic review; source-level access varied (full article, publisher/author abstract, practitioner page, or indexed excerpt). Consult the section-by-section analysis below for the available specificity; full-text access for every named work is **not** asserted.

#### §14.7 — *Signals*: The Authored Trajectory

**Representative claim(s):** **Primary source:** Modiphius Entertainment, *Star Trek Adventures: Quickstart Guide*, containing the self-contained adventure *Signals* and six pre-generated player characters: https://modiphius.net/collections/star-trek-adventures/products/star-trek-adventures-quickstart-guide — **the Section 15 computational reference intentionally models only one Participant controlling one Participant Actor.**; The source adventure supplies the mission, Actors, factions, settlement, Romulan opposition, alien artifact, locations, and expected scenario progression used in §§14.7–14.10; the major-divergence sequence in §14.10 is an Enclave demonstration constructed from that authored material; *Signals*, from the *Star Trek Adventures* Quickstart, provides the same problem in a substantially different narrative environment.
**Cited in outline:** **Primary source:** Modiphius Entertainment, *Star Trek Adventures: Quickstart Guide*, containing the self-contained adventure *Signals* and six pre-generated player characters: https://modiphius.net/collections/star-trek-adventures/products/star-trek-adventures-quickstart-guide — **the Section 15 computational reference intentionally models only one Participant controlling one Participant Actor.**
**Linked source records:** [Modiphius, *Star Trek Adventures Quickstart Guide*](https://modiphius.net/collections/star-trek-adventures/products/star-trek-adventures-quickstart-guide)
**Substantive assessment — primary adventure:** Modiphius authored adventure provides Signals reference, not Enclave implementation
**Source-access record:** prior thematic review; source-level access varied (full article, publisher/author abstract, practitioner page, or indexed excerpt). Consult the section-by-section analysis below for the available specificity; full-text access for every named work is **not** asserted.


### Section 15 — cited-subsection findings

#### §15.5 — Deterministic Activity and Authoritative Resolution

**Representative claim(s):** **Authoritative computation:** conventional systems resolve physical state, Loci, possession, rules, communications, Domain/Enclave/Rank/Facet relationships, Knowledge access, causal conditions, and persistence. Distinguish these deterministic responsibilities from model-driven cognition (§15.4); **Small-scale first-order baseline:** the 43-Actor *Signals* workload generates ~2,624 Interactions, ~5,248 Event records and ~13,339 total records per eight simulated hours: approximately **0.091 Interactions/s, 0.182 Events/s and 0.463 records/s**. These are simulated workload counts, **not CPU or database benchmarks**; **Causal expansion:** an Interaction is an Event and produces a resulting Event in the reference model. That result may trigger additional Events, changes and Actor responses, but the model does not simulate those cascades. An illustrative branching factor `b` over `d` generations gives `1 + b + … + b^d` potential occurrences before failed conditions, merging consequences and deduplication. This is a sensitivity example, not a claim that Enclave inherently expands exponentially.
**Cited in outline:** **Evidence and limitations:** these are measurements from Reliquary and Arcana, **not a benchmark of Enclave's world-state implementation or causal fan-out**. Original reports, supporting raw benchmark bundles and SHA-256 provenance are copied into `docs/research/section15-deterministic-evidence/` (see `MANIFEST.md`). The primary comparison is the Reliquary P1 Freshness report.
**Linked source records:** [Internal measured evidence manifest](section15-deterministic-evidence/MANIFEST.md)
**Substantive assessment — transfer limit:** Reliquary/Arcana timings measured in distinct systems, not Enclave Event processing
**Source-access record:** prior thematic review; source-level access varied (full article, publisher/author abstract, practitioner page, or indexed excerpt). Consult the section-by-section analysis below for the available specificity; full-text access for every named work is **not** asserted.

### Further corrections and limitations from the 28-subsection completion pass

These priorities were originally in a separate continuation report and are retained here to avoid losing substantive analysis:

1. **§2.5:** Hammond documents the player-agency/narrative-coherence tension, not a controlled finding that 'meaningful response is necessary'. Keep the latter as an explicit design goal or cite a more direct agency definition.
2. **§2.8 / §4.5 / §4.13:** case studies of reconvergence and open-world authored narratives cannot prove industry-wide prevalence; keep examples and avoid absolute language.
3. **§3.8:** Louchart et al. expressly bound the interactor's options to authored action ranges and use local drama management; this is meaningful prior art and an important **difference** from Enclave's intended interpretation flexibility.
4. **§4.7:** historical formal-model literature supports explicit action-domain bottlenecks but cannot prove universal historical lack of probabilistic alternatives. The existing caveat in §3.10 remains necessary.
5. **§4.10–4.11 and §5.8:** Kambhampati et al. is a position paper; PAL validates modular program execution but not narrative-state authority. Attribute the general design to related precedent, the full protocol to Enclave.
6. **§5.2:** existing bounded generative-agent systems are evidence of *possibility*, not proven GM-like unrestricted agency.
7. **§12.4–12.6:** distinguish neuropsychological analogies, documented machine-agent mechanisms and the proposed Enclave-specific cognitive cycle.

**Research-access limitations recorded in that pass:**
- Full-text pages consulted for Stang, Evans, Jenkins, Soler-Adillon and multiple Alexander articles; full-text author-hosted PDFs for Louchart & Aylett (2003), Louchart et al. (2008) and Porteous et al. (2021).
- Author/publisher abstracts or excerpts rather than complete articles used for several Jones, Fisher, Hayton, human-memory and machine-agent findings. Claims requiring detail from their methods should remain qualified until full-text review.
- This is a claim-to-source **evidence alignment audit**, not an experimental replication, systematic literature review or definitive novelty clearance.


## Claim-to-source review by section

### §1 — Abstract

**Verdict: authorial synthesis.** The agency/persistence problem and three-part division of labor can legitimately be presented as the paper's argument, not as an established empirical discovery. Do not imply the architecture has been implemented or benchmarked.

### §2 — Human authorship and agency

- **§2.1, partial, scope narrowed:** Wang et al. (2026) report higher human variability and right-tail creativity in a large *divergent idea generation* task; they do not compare complete fictional narratives, all human writers, or all modern LLMs. Source: https://www.nature.com/articles/s41562-025-02331-1
- **§2.1, contextual:** Sourati et al. (2026) investigate shrinking linguistic diversity under LLM-mediated writing; this does not alone prove every individual writer produces an identifiable and irreducible style. Source: https://www.nature.com/articles/s41562-026-02550-0
- **§2.2, direct within sampled tasks:** Tian et al. (2024) compare story arcs, affect, suspense and structural diversity in evaluated stories. Marco et al. (2025) instead compare **reader priorities**, finding surface-focused versus holistic evaluative profiles. They are complementary, not interchangeable measures of human narrative superiority. Sources: https://aclanthology.org/2024.emnlp-main.978/ ; https://aclanthology.org/2025.findings-acl.1304/
- **§2.3, direct but bounded, scope narrowed:** Xu et al. (2025) compare 100 short stories and GPT-4/LLaMA-3 generations and report repeated plot-element combinations. The result should be scoped to the tested models and prompts. Source: https://pmc.ncbi.nlm.nih.gov/articles/PMC12415252/
- **§§2.5–2.8, conceptual and case-study support:** Hammond et al. address agency; Stang (2019) critiques moral choices and reconverging decisions in *BioShock* and *The Walking Dead*, and Evans (2024) studies a specific open-world design. Such examples do not establish that conventional game narratives are *universally* ineffective. Sources: https://gamestudies.org/1901/articles/stang ; https://gamestudies.org/2404/articles/evans
- **§2.9, direct conceptual plus experimental precedent:** Day & Zhu distinguish *theoretical* from *perceived* agency; Thue et al. report a 141-participant evaluation of selected story events and perceived agency. They do not demonstrate more actual possible actions. Sources: https://researchdiscovery.drexel.edu/esploro/outputs/conferenceProceeding/Agency-Informing-Techniques-Communicating-Player-Agency/991019167457704721 ; https://ojs.aaai.org/index.php/AIIDE/article/view/12437
- **§§2.4, 2.10–2.11, norm / inference:** choosing human authorship as a requirement and wanting more authorial leverage are the paper's design priorities. No empirical source can prove them necessary for every application.

### §3 — Worldbuilding, adversarial design and authored narrative

- **§§3.1–3.6, direct practitioner and theoretical precedent:** Jenkins identifies narrative architecture in authored spaces; Alexander directly advocates situations, non-forced scenario timelines, information clues, naturalistic nodes and proactive actors. These sources do *not* establish Enclave's canonical knowledge, actor-local memory or event-validating system. Sources: https://electronicbookreview.com/publications/game-design-as-narrative-architecture/ ; https://thealexandrian.net/wordpress/4147/roleplaying-games/dont-prep-plots ; https://thealexandrian.net/wordpress/4154/roleplaying-games/dont-prep-plots-prepping-scenario-timelines ; https://thealexandrian.net/wordpress/45283/roleplaying-games/the-secret-life-of-nodes-part-5-naturalistic-node-design
- **§3.7, direct practitioner precedent:** Emily Short and Failbetter describe conditionally available authored content and quality-based narrative. This supports state-conditioned narrative, *not* Enclave's complete world simulation. Sources: https://emshort.blog/2019/11/29/storylets-you-want-them/ ; https://www.failbettergames.com/news/echo-bazaar-narrative-structures-part-two
- **§3.8, direct conceptual precedent:** Louchart et al. (2008) explicitly investigate the author's function when narrative results emerge. This is theoretical alignment, not an implementation-equivalence or proof of Enclave's benefits. Source: https://research.utwente.nl/en/publications/purposeful-authoring-for-emergent-narrative/
- **§3.9, source-supported criterion with untested extension:** Chen et al. (2009) propose three authorial-leverage evaluation criteria and find leverage for their declarative optimization-based drama manager. It does not quantify Enclave's future authorial burden reduction. **Recommendation not applied to current outline.** Source: https://ojs.aaai.org/index.php/AIIDE/article/view/12377
- **§3.10, historical gap:** planners, drama managers and storylets encode explicit structures, but the universal claim about what probabilistic interpretation was or was not practical over time is not established by those architecture papers. Treat as research-needed, not retrospective fact.

### §4 — Branching, formalization and scale

- **§§4.1–4.3, directly related literature:** Jones' authorial burden work and Hayton/Porteous' narrative-planning papers establish nontrivial authoring and domain-modeling costs. They support a **representation bottleneck**, not an exact complexity bound for all interactive narratives. Sources: https://ojs.aaai.org/index.php/AAAI/article/view/5534 ; https://researchportal.hw.ac.uk/en/publications/automated-narrative-planning-model-extension/
- **§4.4, direct:** Iovino et al. explain how FSM extensibility, reuse and modularity limits motivated behavior trees. Treat trees, planning and conventional automation as useful foundations rather than blanket failures. Source: https://www.sciencedirect.com/science/article/pii/S0921889022000513
- **§§4.5, 4.13, case-based:** Stang's reconvergence examples and Evans' open-world analysis substantiate *particular* ways to bound narrative state. They do not establish an industry-wide prevalence or exact costs. Sources: https://gamestudies.org/1901/articles/stang ; https://gamestudies.org/2404/articles/evans
- **§4.6, unsupported empirical extrapolation:** Day & Zhu, Thue and Stang do not report measured replay-dependent decay in perceived agency. **Recommendation not applied to current outline.** Sources: https://ojs.aaai.org/index.php/AIIDE/article/view/12437 ; https://gamestudies.org/1901/articles/stang
- **§§4.7–4.8, mixed:** Hayton/Porteous establish the practical cost of explicitly authored action/domain models; Park et al. and Hogan & Brennen demonstrate contextual, natural-language actor action in bounded research environments. None establishes unconstrained action or the elimination of all explicit representations. Sources: https://ojs.aaai.org/index.php/AAAI/article/view/5534 ; https://research.google/pubs/generative-agents-interactive-simulacra-of-human-behavior/ ; https://arxiv.org/abs/2404.11446
- **§§4.9–4.11, direct architectural precedent, novel transfer:** PAL offloads arithmetic/program execution to a runtime; LLM-Modulo advocates external verifiers. Neither implements Enclave's truth, world authority, or causal Event boundary. Their authors' positive evidence/arguments support the **division-of-responsibility precedent**, while the proposed narrative transfer remains Enclave's hypothesis. Sources: https://proceedings.mlr.press/v202/gao23f.html ; https://proceedings.mlr.press/v235/kambhampati24a.html
- **§§4.12, 4.14, conditional reasoning:** combinatorial growth follows how states or subsets are defined. A numeric complexity expression must specify the enumerated object and any inheritance/pruning; prior narrative papers do not benchmark Enclave's enumeration algorithms.
- **§4.15, relevant analog:** Alexander's tabletop design demonstrates human adaptation but does not furnish machine-scale performance metrics.
- **§4.16, narrow but credible:** historical source accounts support substantial human oversight costs in selected MMOs. Ultima Online volunteers were mostly counselors/support, *not* all human narrative GMs; Matrix Online retrospective essays describe a particular staffing structure. Source: https://www.salon.com/2000/09/21/ultima_volunteers/
- **§4.17, precedent not implementation:** Generative Agents and Snow Globe show agent-driven responsive environments in limited case studies; they do not verify Enclave's security, causality or scaling. Sources: https://research.google/pubs/generative-agents-interactive-simulacra-of-human-behavior/ ; https://github.com/IQTLabs/snowglobe

### §5 — The Agency–Persistence Gap

- **§§5.1–5.3, synthesis:** persistently consequential agency logically creates information to be retained. The concept/term "Agency–Persistence Gap" is **this paper's synthesis**, not a pre-existing result to attribute to Park or Wu.
- **§5.4, directly supported with experimental boundary:** Liu et al. demonstrate position-dependent failures in long-context question answering/retrieval; LongMemEval evaluates extraction, temporal reasoning, updates and abstention over sustained dialogue; RULER and LongBench benchmark other long-context abilities. These establish actual limits **in evaluated tasks/models**, not a universal theorem that LLMs cannot maintain any state. Sources: https://aclanthology.org/2024.tacl-1.9/ ; https://proceedings.iclr.cc/paper_files/paper/2025/hash/d813d324dbf0598bbdc9c8e79740ed01-Abstract-Conference.html ; https://arxiv.org/abs/2404.06654 ; https://aclanthology.org/2024.acl-long.172/
- **§5.5, valid conditional derivation:** O(N) retained records follow from storing an O(1)-size record for each of N events without discard/dedup; they are not an empirical result established by LongMemEval or database format documentation. PostgreSQL and SQLite show metadata/index overhead; they do not show SQL is unsuitable for Enclave. Sources: https://www.postgresql.org/docs/current/storage-page-layout.html ; https://www.sqlite.org/fileformat.html
- **§5.6, authorial synthesis:** the inferred gap describes design tension and should not be presented as a named construct independently verified by those studies.
- **§5.7, explicitly analogical:** Cowan's three-to-five-chunk short-term memory limit and reconstructive human memory studies concern *humans*, whereas Liu and Wu concern *models*. Similar tradeoffs do not prove identical mechanisms. Source: https://pubmed.ncbi.nlm.nih.gov/11515286/
- **§5.8, architectural proposal:** PAL/LLM-Modulo give useful division-of-responsibility precedents, not performance/safety verification of Enclave.

### §6 — Sandbox systems and narrative

- **§§6.1–6.3, concepts and implementations:** Juul's emergence/progression taxonomy and Soler-Adillon's distinctions support rule-generated possibility spaces; Adams' Dwarf Fortress chapter and Neighborly document simulation-driven emergent narrative. They do not mean world-sandbox engineering is solved. Sources: https://jesperjuul.net/text/openandtheclosed.html ; https://gamestudies.org/1902/articles/soleradillon ; https://www.degruyterbrill.com/document/doi/10.1515/9783839453452-007/html ; https://ieeexplore.ieee.org/document/9893631/
- **§6.4, inferential:** persistent MMO worlds establish that state can outlive a session, but not that persistence is the *only*, *least significant*, or universally solved difficulty in emergent narrative.
- **§6.5, conceptual distinction valid; universal scope not tested:** systemic emergence, player-interpreted narrative, and adaptive authored narrative are distinguishable design targets. Literature supplies examples, not a comprehensive census of industry support for the third.
- **§6.6, Enclave's proposed research gap:** describing the objective precisely is justified; claiming no prior system supplies comparable fidelity requires separate exhaustive work including event sourcing, epistemic logic, knowledge management and agent-native simulation. Narrative literature alone cannot establish novelty.

### §§7–11 — The proposed Enclave architecture and ontology

**Verdict: internally authored formal definitions and design rules, not empirical findings to validate by citation.** The primitive ontology, authority boundaries, identity, Domains, Rank, Facets, derived Interactions, Enclaves, diffusion, saturation and institutional emission are definitions/algorithms proposed by the paper. The audit checks that they are *not* disguised as results established by unrelated sources.

- **§7 (system overview):** the synthesis of rules, knowledge, actors and authored trajectory is a proposal, not a demonstration of working system behavior.
- **§8 (layers of authority):** the author/world/Actor boundaries are a design contract; literature on LLM verifiers offers only partial precedent for how to implement it.
- **§9 (primitives):** the defined ontology and derived relationships need internal semantic consistency, not citation to independent empirical findings.
- **§10 (derivatives):** combinatorial Enclaves, Rank, Inheritance and Facets need proofs or tests of access semantics and algorithmic complexity.
- **§11 (knowledge distribution):** diffusion, saturation, institutional emission and provenance propagation require traceable Event-level validation before correctness is claimed.
- Existing systems with similar concepts must be considered in the prior-art discussion before making a novelty claim.
- Claims of correctness (e.g. preventing unauthorized information transfer, maintaining causal consistency, saturating group knowledge) remain **design invariants**, not proven implementation properties.
- §9.3's episodic/semantic human-memory comparison is a motivating analogy rather than proof of the Enclave Memory primitive.
- Diffusion/saturation algorithms still require formal specification of semantics, complexity and adversarial edge cases; "will automatically preserve consistency" would be unproven without implementation or proofs.
- These sections generally do **not** need ordinary empirical citations after every definition, but do need careful comparison to distributed systems, epistemic logics, provenance and information-flow architectures to defend originality.

### §12 — Actor cognition

- **§12.1, bounded risk evidence:** Chang et al. show that models can memorize published books; Carlini et al. demonstrate extractable training data under specific conditions. This supports a *possible* out-of-context leakage route, not that every model will reveal scenario secrets. Source: https://aclanthology.org/2023.emnlp-main.453/ ; https://www.usenix.org/conference/usenixsecurity21/presentation/carlini-extracting
- **§12.2, architectural precedent:** Park et al. document agent experience records, reflection, retrieval, planning, and 25 simulated agents; MemGPT uses external memory tiers. These establish feasibility of particular patterns, not the reliability of Enclave's persistent Actor lifecycle. Source: https://research.google/pubs/generative-agents-interactive-simulacra-of-human-behavior/ ; https://arxiv.org/abs/2310.08560
- **§12.3, partial analog:** differentiated agent contexts and open-ended multi-agent wargaming illustrate asymmetric knowledge. Enforcing Enclave's exact Actor-local epistemic restrictions is *proposed*, not shown by those experiments. Source: https://arxiv.org/abs/2404.11446
- **§12.4, mixed:** Tulving/Greenberg illuminate episodic versus semantic human memory, not Enclave data structures; Park/MemGPT are actual machine-memory precedents.
- **§12.5, distinct design vs evidence:** long-context evidence motivates bounded context assembly, but the proposal to "provide as much legitimate context as practical" should not be read as a finding that maximal inclusion is always optimal—Liu explicitly demonstrates position and length sensitivity. Context selection and the hierarchy of relevance signals need evaluation.
- **§§12.6–12.7, architectural precedent only:** PAL offloads execution, LLM-Modulo advocates verifier loops. Neither has tested Enclave's precise event-authority cycle, multi-actor permissions or adversarial interaction semantics.
- **§12.8, related internal engineering:** Reliquary may serve as a proposed storage component. Statements about its compression/performance must be attributed to its own measured workloads, not to independent Enclave experiments.

### §§13–14 — Causality and authored walkthroughs

- **§13, design proposal:** event validation, causal continuation and persistence are proposed mechanics. The outline is not entitled to call every kind of consequence automatic or complete without implementation/verification; the graph model can generate branching workload beyond initial events.
- **§14, fictional counterfactual scenarios:** *A Wild Sheep Chase* (Winghorn Press) and *Signals* (Modiphius) supply authored source material. Alternate player actions in the paper are constructed **thought experiments**, not recorded playtests, implemented simulations, or empirical validation that Enclave can generate them reliably.
- Reference media and source licenses/permissions should be handled separately from literature citation identity if reproducing story text or copyrighted imagery. Sources: https://winghornpress.com/adventures/a-wild-sheep-chase/ ; https://modiphius.net/collections/star-trek-adventures/products/star-trek-adventures-quickstart-guide

### §15 — Computational architecture and scale

- **§§15.1–15.4, 15.6–15.7, 15.9–15.10, mathematical scenarios:** figures depend on authored population, interaction/event rates, token budgets, indexing, record sizes, assumed model placement, and other design inputs. They are **first-order calculations**, not measurements of a functioning Enclave MMO.
- **§15.5, related-system measurements:** original Reliquary Freshness and Arcana report actual observations of traversal/query workloads in other systems. They do not establish the CPU/database cost of authoritative Enclave Events, actor fan-out, world-state mutation, or concurrent Participants. Source provenance: docs/research/section15-deterministic-evidence/MANIFEST.md.
- **§15.8, observed retail quotes / model cost arithmetic:** hosted model and GPU prices are date-sensitive listed tariffs. A GPU rental hour does not represent a validated inference throughput or model-quality equivalent. Provider disclosures must be checked again at manuscript release. Source: https://modal.com/pricing
- **Manhattan:** aggregate city-scale quantities are illustrative extrapolations, not population-behavior measurements or capacity tests. Explicit assumed concurrency is essential.

### §16 — Practical applications and fidelity tiers

- **§§16.1–16.5, proposed application levels:** deterministic dialogue, persistent characters and selectively cognitive Actors are design choices derived from Enclave's architecture, not an independently validated product taxonomy.
- **§16.6, conditional cost model:** the same authored corpus and workload assumptions can be used to contrast three uniform levels and the particular Signals hybrid. The 85.6%, 82.6%, and 85.7% savings are **within-model comparisons**, not measured acceleration or a tested preservation of narrative quality.
- The user-approved section is **unchanged** in this audit. At final prose conversion, consider replacing any "establish requirements" language with "estimate under the specified reference workload" and refrain from asserting that the proposed hybrid *demonstrates* maintained narrative fidelity experimentally. Calculation source: scripts/signals_section16_fidelity_calculations.py and data/signals-section16-fidelity-results.json.

### §17 — Conclusion

Restating the architectural thesis is legitimate. Avoid introducing new claims of experimental feasibility, novelty priority, guaranteed narrative fidelity, or measured cost reduction that are not supported by the preceding proposal and conditional models.

## Focused continuation: bounded agent evidence in §§4.17 and 5.1

**Source check (2026-10-09).** Park et al. (2023) evaluate generative agents in a 25-agent sandbox, demonstrating believable local behavior and some emergent social coordination. Hogan & Brennen (2024) present Snow Globe, a system for qualitative wargames, with case studies on incident-response and geopolitical scenarios. Both are legitimate precedents for natural-language agent interactions; neither measures long-duration, thousands-of-agent, unsupervised narrative fidelity or shows that ordinary human gamemastering labor has already been replaced. The paper's prior formulation treated a *potential* reduction as an *accomplished* one.

- **§4.17:** the audit recommended replacing "This removes much of the historical labour constraint" with conditional language and explicit reliability/latency/supervision/concurrency limitations; that edit was later reverted from the outline.
- **§5.1:** the audit recommended replacing "Machine intelligence removes much..." with a conditional capability statement and qualifying the gamemaster-equivalence analogy; those edits were later reverted from the outline.
- **Status:** these are evidence-scope recommendations only. The original outline wording was restored by commit `1a313ec`; no outline changes are authorized by this audit.
- **Evidence checked:** [Park et al., Generative Agents (ACM UIST 2023)](https://doi.org/10.1145/3586183.3606763) (publisher abstract); [Hogan & Brennen, Open-Ended Wargames with Large Language Models (2024)](https://arxiv.org/abs/2404.11446) (author abstract).
- **Related literature surfaced:** [Jones & Millard, *Beyond Authorial Burden* (ACM Transactions on the Web, published August 13, 2026)](https://doi.org/10.1145/3757746) extends the underlying interview work; add to the publication bibliography only after a separate relevance/overlap check against the cited 2024 conference version.

## Focused research resolution R4 — agent-native narrative architecture and originality (§§6.6, 7.7; 2026-10-09)

**Question.** Does available prior art establish that no existing system enables persistent, actor-local epistemic state and autonomous response to emergent consequences inside a deliberately authored narrative world? **Result: no.** Multiple primary research and implementation records precede several aspects individually; some systems closely overlap the proposed *integration*. This is a targeted comparative source pass, **not** a patent novelty search, complete implementation audit, benchmark, or proof that all equivalent systems have been found. The current paper outline was **not** edited.

### Closest narrative and agent-simulation precedents

| Precedent | Directly documented overlap | Boundary of the comparison / evidence status |
|---|---|---|
| **Comme il Faut / Prom Week** (McCoy et al., 2011, 2013; 2014 follow-up) | Authored reusable social rules, cultural/social knowledge, remembered social facts, evolving relations and conditional scene performance reduce enumeration of social branches. | A demonstrated historical narrative/social-physics system, not Enclave's LLM interpretation or proposed graph-wide epistemic delivery. Its existence defeats novelty claims for recombinable authored social narrative itself. |
| **Versu** (Evans & Short, 2014) | Autonomous agents act within authored social practices represented as reactive joint plans, with agent-level utility selection rather than an omniscient fixed screenplay. | Direct precedent for actors responding to authored situations; the retrieved abstract does not establish arbitrary-action interpretation, Enclave-style provenance or institutional diffusion. |
| **Generative Agents** (Park et al., 2023) | Twenty-five agents with individual memory/reflection/planning show emergent social coordination and information sharing in a sandbox. | Empirically bounded demonstration; not a test of durable deterministic event authority or fully authored branching narrative. Already in the bibliography; a relevant but not uniquely nearest comparison. |
| **Concordia** (Vezhnevets et al., 2023; current upstream implementation) | Agent-specific memory, configurable Game Master, action-intention interpretation, event resolution, observation delivery, world-state components, simulation loop and author-specified scene structure. | **Major near-neighbor.** GM components can use LLM resolution and custom logic; the architecture is configurable, so one cannot simply assert it lacks possible deterministic validation. Need explicit source-code comparison to prove any essential Enclave mechanism absent. |
| **Sonder Engine** (public implementation inspected 2026-10-09) | Describes separated objective truth, perception, memory, beliefs, actor-specific contexts, narration, a Director/character decision sequence and a single persistence/commit boundary; includes code, schema and tests. | **Very close applied precedent.** A repository architecture claim, not independent peer-reviewed validation of its correctness or scale. Unlike Enclave's generalized architecture, it describes itself as local single-player interactive fiction. Do not infer Enclave-wide novelty merely from that scope difference. |
| **Bunnyland** (public implementation/specification inspected 2026-10-09) | Persistent ECS world; swappable LLM/human/script/behavior-tree controllers; scoped per-character perceptions and private memory; action validation, atomic commit, shared consequences and events; documented world-contract tests. | **Very close implementation of state/authority separation.** A bounded action-verb surface and game-world focus differ from Enclave's proposed semantic interpretation and authored narrative propagation, but breadth/fidelity differences are not yet established experimentally. |
| **Canonvale / Myriuna** (provider pages inspected 2026-10-09) | Product proposals or early access marketing describe durable world truth, actor-local knowledge, factions, rumors, authored worlds and AI constrained by world state. | Product self-description only, without reviewed public code or independent evaluation; discovery counterexamples to sweeping marketplace absence, not evidence of delivered architectural reliability. |
| **Knowledge-graph-guided generative storytelling** (Pan et al., 2025) | Users edit a structured knowledge graph to steer LLM stories; small user evaluation reports improvements in supported narratives and control. | Direct precedent for author-managed structured story context; not demonstrated multi-actor causal Event/epistemic diffusion architecture. |

### Underlying technical precedents outside narrative literature

| Established field | What it already establishes | What remains Enclave-specific |
|---|---|---|
| **Dynamic epistemic logic** (Baltag/Moss/Solecki tradition; SEP overview) | Formal agent-relative knowledge/belief updates through information-changing events, including private announcements and misdirection; *who may know what* is not new as a research question. | An application-level, scalable knowledge/memory/rumor lifecycle linked to authored narrative meaning and executable Actor context selection is still a proposed integration. |
| **Event sourcing** (Fowler, 2005; AWS pattern) | Durable ordered changes, audit/reconstruction and world state derived from committed events long predate Enclave. | Its particular coupling to meaningful narrative Interactions, author-defined intended developments and Actor-local epistemic consequences. |
| **ReBAC / ABAC** (Fong, 2011; NIST SP 800-162) | Relationship- and attribute-conditioned visibility/authorization policies; group membership inheritance is not in itself a novel security mechanism. | Enclaves/Facets/Inheritance as domain-specific narrative-access and information-distribution semantics, if specified and validated as more than ordinary permission predicates. |
| **Data provenance** (Buneman, Khanna & Tan, 2001) | Tracing where derived information came from is established database work. | An Event-to-Memory-to-Fact chain usable as an Actor's bounded understanding and causal narrative context, with conflicting belief preserved rather than silently converted to truth. |
| **Distributed discrete-event simulation** (e.g., Kim et al., 1997) | Event ordering, causal relationships and parallel simulation synchronization are established computational problems and techniques. | Claimed efficiency of Enclave's proposed locality and simultaneous Cognitive Actors is future evaluation, not a demonstrated historical first. |
| **Organizational/group knowledge** (e.g., Borrelli et al., 2005; Aldewereld et al., 2016) | Shared organizational memory, information exchange and group norms have substantial agent-model precedents. | Enclave's particular saturation-to-group-knowledge promotion threshold, deterministic Actor membership/inheritance behavior and implementation cost need a more targeted comparison and formal proof. |

### Claim-level decisions

1. **§6.6 — partially supported as a *design target*, not as an historically exclusive missing capability.** Narrative social-physics research already addresses reacting to unenumerated combinations through reusable authored structures, while recent systems also separate world state from agent reasoning. The specific combination Enclave describes can be presented as its proposed architectural synthesis. Avoid saying that the ability itself was missing from all prior systems.
2. **§7.7 — substantial component feasibility precedents found.** It is sound to argue that antecedent components have been built or formally studied, conditional on each source's actual scope. This **does not** verify that the assembled Enclave architecture works, nor that its fidelity, cost or authorial leverage is superior. Correct evidentiary verb: “provides precedent for,” not “demonstrates Enclave.”
3. **Most plausible differentiating *research hypothesis*:** a unified authored narrative world in which bounded probabilistic cognition proposes action; authoritative mechanisms validate and commit causal Events; actor-specific Knowledge/Memories are derived under source/location/group conditions; Events affect both institutional information and conditional future authored trajectories. No surveyed source demonstrates precisely this entire combination **under the proposed Enclave contracts**. However absence from the searched source descriptions is **not** proof that no implementation exists.
4. **Potential nonnovel details:** action proposal/commit, event logs, agent private memory, knowledge graphs, belief-versus-truth separation, contextual access rules, authorial social patterns, group norms and information diffusion are individually established. These must **not** be claimed as invented primitives or new general algorithms.
5. **Unresolved originality and validation tests:** define an explicit capability matrix against *Concordia, CiF/Prom Week, Versu, Sonder and Bunnyland*; identify the actual required invariants, executable semantics and negative tests. Test a counterfactual bridge/faction/rumor case spanning: hidden culpability, distinct actor beliefs, time-dependent consequences, group saturation, altered faction plans and persistence after restart. Record authoring effort and invalid knowledge/action rates versus a suitable baseline. Novel *integration* and scientific contribution could then be defended without a universal negative.

**Disposition: R4 research comparison performed; the overbroad historical-exclusivity claim is unsupported; narrower architectural-synthesis claim is defensible as a proposal; practical superiority, exact uniqueness and large-scale correctness remain open.** Do **not** close the row as “proven novel”; do not rewrite the canonical outline without author review.

### Direct sources checked / candidates for bibliography review

Primary publisher abstracts and framework authors' documentation were inspected where accessible; implementation projects were read at README/architecture or specification level, **not** independently executed. **Bibliography update 2026-10-09:** 13 missing publication and software references from this research and §6.6 were checked against primary publisher/author/project metadata and incorporated into the publication bibliography (112 → 125 entries), without duplicating the older references. The 92-item verification ledger remains a **dated snapshot**, not a new verification certificate for all 125 references. The new software/product sources establish documented claims and stated architecture, not independently tested behavior.

- McCoy, Treanor, Samuel, Wardrip-Fruin & Mateas (2011), *Comme il Faut: A System for Authoring Playable Social Models*, AIIDE. https://doi.org/10.1609/aiide.v7i1.12454
- McCoy et al. (2013), *Prom Week*, AIIDE. https://doi.org/10.1609/aiide.v9i1.12662 ; developer note on substantial scene authoring: https://promweek.soe.ucsc.edu/2012/02/09/prom-week-authoring-crafting-procedurally-driven-narratives/
- Evans & Short (2014), *Versu—A Simulationist Storytelling System*, IEEE Transactions on Computational Intelligence and AI in Games. https://doi.org/10.1109/TCIAIG.2013.2287297
- Vezhnevets et al. (2023), *Generative agent-based modeling with actions grounded in physical, social, or digital space using Concordia*. https://arxiv.org/abs/2312.03664 ; official current code/design https://github.com/google-deepmind/concordia ; component guide https://github.com/google-deepmind/concordia/blob/main/concordia/components/README.md
- Park et al. (2023), *Generative Agents: Interactive Simulacra of Human Behavior*. https://doi.org/10.1145/3586183.3606763 (already assessed in the bibliography)
- Sonder Engine, public implementation and code map: https://github.com/N0819/Sonder_Engine ; database and policy contracts: https://github.com/N0819/Sonder_Engine/blob/main/docs/guides/DATABASE.md
- Bunnyland, public implementation: https://github.com/thalismind/bunnyland-server ; world/commit contract: https://github.com/thalismind/bunnyland-server/blob/main/docs/developer/world-contract-v1.md
- Canonvale product description (closed alpha): https://canonvale.com/ ; Myriuna pre-production description: https://myriuna.com/
- Pan et al. (2025), *Guiding Generative Storytelling with Knowledge Graphs*. https://arxiv.org/abs/2505.24803
- Dynamic epistemic logic survey, Stanford Encyclopedia of Philosophy: https://plato.stanford.edu/entries/dynamic-epistemic/
- Fowler (2005), *Event Sourcing*: https://martinfowler.com/eaaDev/EventSourcing.html ; AWS implementation guidance: https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/event-sourcing-pattern.html
- Fong (2011), *Relationship-based access control: protection model and policy language*. https://doi.org/10.1145/1943513.1943539 ; NIST SP 800-162 (2019 revision), *Guide to Attribute Based Access Control*. https://doi.org/10.6028/NIST.SP.800-162
- Buneman, Khanna & Tan (2001), *Why and Where: A Characterization of Data Provenance*. https://doi.org/10.1007/3-540-44503-X_20
- Kim et al. (1997), *Ordering of simultaneous events in distributed DEVS simulation*. https://doi.org/10.1016/S0928-4869(96)00009-2
- Borrelli et al. (2005), *Inter-Organizational Learning and Collective Memory in Small Firms Clusters*. https://jasss.soc.surrey.ac.uk/8/3/4.html ; Aldewereld, Dignum & Vasconcelos (2016), *Group norms for multi-agent organisations*. https://doi.org/10.1145/2882967

## Outstanding source gaps (not solved by the existing 92-item bibliography)

1. **Replay effect (R1 review completed, direct causal gap open):** Roth et al. (2012) find increased perceived effectance after a second *Façade* exposure, while Fendt et al. (2012) and Cardona-Rivera et al. (2014) relate agency to feedback and meaningfully distinct outcomes. **Still needed** for any strong replay-decay claim: controlled repeated-playthrough research measuring players' *discovery of reconvergence* versus genuine persistence. See focused R1 above.
2. **Historical capability:** targeted technology history needed for assertions about probabilistic interpretation being unavailable/impractical across earlier software.
3. **Agent-native environment originality (R4 comparative pass completed, narrower originality claim still open):** Concordia, CiF/Prom Week, Versu, Sonder, Bunnyland, dynamic epistemic logic, access-control research, event sourcing and provenance have now been compared and linked in the focused R4 section. Substantial prior art contradicts exclusivity of most components. Remaining work is a feature-by-feature technical comparison and formal or executable demonstration of Enclave's **specific authored-narrative + causal-event + epistemic-diffusion integration**; an unqualified 'no prior system can do this' claim is unsupported.
4. **End-to-end feasibility:** an Enclave prototype or a formally specified executable reference is needed to measure Event correctness, retrieval leakage, actor-state consistency and inference load.
5. **Generality of sandbox criticism (R3 partially resolved):** 2025 scoping review, 2026 authorial interviews, historical quest research and a 20-title/2,191-mission preprint corroborate recurrent structures and separation of authored quest content from mechanics. **Still needed for prevalence claims:** representative title sampling with explicit coding of cross-quest causal effects and persistently reactive authored narrative; the 2026 study did not measure that property. See R3 above.
6. **Economic comparisons:** deployment prices and independent model-serving capacity must be refreshed for any published cost claim.

## Recommended manuscript evidence language

- "X demonstrates" for a particular controlled outcome **within the investigated system and task**.
- "X provides precedent for" when adapting an existing architecture.
- "We propose / Enclave would" for design rules and unimplemented guarantees.
- "Under the assumed workload, the model estimates" for §§15–16 numbers.
- "We hypothesize" for the repeated-replay effect until direct evidence exists.
- "Related work has explored partial versions" rather than "no system does this" unless prior art has been exhaustively searched.

## Completion update — 2026-10-09

The **complete 61-subsection audit is consolidated above in this document**, incorporating the 28 later judgments and the 33 previously assessed source-tagged subsections. This brings the existing inventory to **64 focused judgments across 139 subsections**: all **61 subsections with an explicit `Support:` marker** and three others. It does **not** mean 61 complete papers were read or that each sentence is fact-checked.

A separate **[78-subsection source-needs triage](claim-to-source-no-support-triage-2026-10-09.md)** distinguishes original definitions, design values, hypothetical examples and conditional computations from historic/empirical claims that need further provenance. No missing-source accusation is inferred merely from the absence of a `Support:` tag; inline URLs and internal calculation documents count as evidence too.

**Remaining evidentiary work:** exact source anchors for general historical or industry-prevalence statements, complete-text checks for studies reviewed from abstracts/excerpts, implementation validation of Enclave-specific invariants, up-to-date provider prices, and traceable DGX Spark benchmark provenance. The user-approved §16.6 prose has not been changed by this completion pass.

## Audit deliverables

- This document: reviewed source-to-claim findings with explicit boundaries, remedy and primary-source links.
- docs/research/claim-to-source-subsection-inventory-2026-10-09.json: mechanically extracted subsection, representative argument, support lines and focused-review status for every subsection, with **unreviewed sections explicitly marked**.
- docs/paper-outline.md: restored to the pre-audit wording in commit `1a313ec`. The evidence-scope concerns at §§2.1, 2.3, 3.9, 4.6, 4.17 and 5.1 remain documented here as recommendations, not outline edits.
- Previous bibliography-verification ledger remains valid but should **not** be mistaken for a claim-to-source audit.

**Bottom line:** Enclave has credible conceptual and technical antecedents for much of its motivation. Its strongest originality statements and practical feasibility claims are **research propositions**, not results already established by references to adjacent work.
