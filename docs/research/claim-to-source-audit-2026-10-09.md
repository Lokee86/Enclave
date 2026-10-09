# Enclave claim-to-source audit — 2026-10-09

## Scope and evidence standard

The audit uses the **current 17-section outline** in docs/paper-outline.md, not the older numbered structure in docs/design-paper.md. The separate machine-readable subsection inventory covers every numbered subsection and identifies the principal supporting citation lines. The present document makes **focused, source-specific substantive judgments**, with the strongest attention to consequential empirical and historical claims; it is not a certification that every sentence of the manuscript is verified.

Four different evidentiary relationships must not be conflated:

1. **Direct support:** a primary paper or publisher/author text demonstrates the claimed finding within a defined study, example, or system.
2. **Bounded / analogical support:** the source establishes a narrower phenomenon or useful comparison but not the full breadth of the statement.
3. **Architectural proposal / logical derivation:** Enclave defines an intended rule, ontology, or consequence. Literature can provide precedent, not evidence that Enclave already works.
4. **Conditional model / transfer:** a calculation follows stipulated assumptions or measurements from another system. These are not benchmarks of an implemented Enclave.

**Important limitation:** The 92-entry verification ledger establishes bibliographic identities. This separate source-to-claim pass read accessible primary **abstracts, article text and practitioner pages**, plus the repo's source ledger and computational assumptions, for high-impact citations. It did not comprehensively read and replicate all 92 full texts. The subsections without primary source review are transparently tagged as such in the companion inventory.

## Findings requiring the greatest care

| Priority | Outline | Evidence assessment | Action / claim boundary |
|---|---|---|---|
| High | §4.6 | **Replay effect unsupported as an empirical finding.** Day & Zhu separate theoretical from perceived agency; Thue et al. test perceived agency using a 141-person study; Stang studies branching and reconvergence. None establishes a longitudinal decline over repeated playthroughs. | Reframe replay effect as hypothesis, and label cited research as supporting agency and reconvergence only. **Applied to outline.** |
| High | §3.10 | **Historical absence claim not established.** Studies of explicit narrative authoring models do not prove that general-purpose probabilistic interpretation was historically absent or impractical across computer science. | Keep the design comparison; do not state a sweeping historical impossibility without historical review. The outline already contains an explicit research note. |
| High | §6.6 | **Exclusivity/novelty not demonstrated.** The proposed combination may address a meaningful gap, but Neighborly, Generative Agents, open-ended wargames, narrative planners, event-based simulation, and storylets already implement related parts. | State Enclave's proposed integration precisely; avoid claiming invention of narrative sandboxing or proving absence of any equivalent without wider technical prior-art research. |
| High | §15–16 | **Estimated and transferred workload, not system benchmark.** Actual Reliquary/Arcana tests measure different graph/retrieval functions. Signals/Manhattan comparisons are conditional forecasts using modeled cognitive rates and retention assumptions. | Maintain separate labels for measured external subsystems, derived workload counts, prices, and projected Enclave resource needs. Do not advertise computational feasibility as experimentally established. |
| Medium | §§2.1–2.3 | **Human-vs-LLM generalizations were broader than study populations.** Wang measures divergent idea-generation rather than story quality; Tian examines sampled narrative texts; Xu evaluates selected GPT-4/LLaMA-3 generations. | Narrowed the two overbroad bullets in §§2.1 and 2.3. **Applied to outline.** |
| Medium | §3.9 | **Authorial leverage is a criterion, not an Enclave result.** Chen et al. experimentally compare drama-management authoring policies, not this architecture. | Recast Enclave's expected leverage as a future objective. **Applied to outline.** |
| Medium | §6.5 | **Prevalence claim broader than available case studies.** Stang, Evans, Adams, and emergent-narrative literature establish examples and conceptual distinctions, not the frequency with which narrative is less sandboxed across all games. | Preserve as an interpretive synthesis with carefully chosen exemplars, not a measured industry-wide statistic. |
| Medium | §12.5 | **The exact context-assembly policy is an architectural design recommendation.** Long-context benchmarks show access limits; they do not validate the proposed sequencing, breadth, or relative weights of Enclave's relevance signals. | Keep boundaries, retrieval priorities and progressivity as proposed design, not a source-established optimal retrieval algorithm. |
| Medium | §4.16 | **Human labour evidence is narrow and mixed.** Ultima Online counselors largely provided customer/community support; Matrix Online interviews describe a particular live-events production arrangement. | Retain the scaling analogy; avoid saying the figures measure 1:1 tabletop Gamemaster coverage or general MMO staffing requirements. |
| Medium | §12.1 | **Training-data leakage is a possibility, not a universal behavior.** Chang et al. and Carlini et al. document memorization/extraction under particular tests, not inevitable spoilers from every model. | Preserve a risk formulation and differentiate parameter memory from Enclave runtime epistemic state. |
| Medium | §5.7 | **Human-memory evidence is analogical.** Cowan et al. establish limited working-memory capacity; Liu/Wu establish LLM limitations in their respective tests. | Do not claim a single mechanism explains the two systems or that all probabilistic systems inherit the same failure modes. |
| Medium | §16.6 | **Conditional numbers need their assumptions in view.** The published numerical comparison is consistent with the supporting model, but neither fictional scenario establishes realized resource requirements. | Preserve the user-approved section unchanged in this pass. The issue is documented for final manuscript wording and figure captions. |

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
- **§3.9, source-supported criterion with untested extension:** Chen et al. (2009) propose three authorial-leverage evaluation criteria and find leverage for their declarative optimization-based drama manager. It does not quantify Enclave's future authorial burden reduction. **Corrected outline wording.** Source: https://ojs.aaai.org/index.php/AIIDE/article/view/12377
- **§3.10, historical gap:** planners, drama managers and storylets encode explicit structures, but the universal claim about what probabilistic interpretation was or was not practical over time is not established by those architecture papers. Treat as research-needed, not retrospective fact.

### §4 — Branching, formalization and scale

- **§§4.1–4.3, directly related literature:** Jones' authorial burden work and Hayton/Porteous' narrative-planning papers establish nontrivial authoring and domain-modeling costs. They support a **representation bottleneck**, not an exact complexity bound for all interactive narratives. Sources: https://ojs.aaai.org/index.php/AAAI/article/view/5534 ; https://researchportal.hw.ac.uk/en/publications/automated-narrative-planning-model-extension/
- **§4.4, direct:** Iovino et al. explain how FSM extensibility, reuse and modularity limits motivated behavior trees. Treat trees, planning and conventional automation as useful foundations rather than blanket failures. Source: https://www.sciencedirect.com/science/article/pii/S0921889022000513
- **§§4.5, 4.13, case-based:** Stang's reconvergence examples and Evans' open-world analysis substantiate *particular* ways to bound narrative state. They do not establish an industry-wide prevalence or exact costs. Sources: https://gamestudies.org/1901/articles/stang ; https://gamestudies.org/2404/articles/evans
- **§4.6, unsupported empirical extrapolation:** Day & Zhu, Thue and Stang do not report measured replay-dependent decay in perceived agency. **Changed to a clearly identified authorial prediction.** Sources: https://ojs.aaai.org/index.php/AIIDE/article/view/12437 ; https://gamestudies.org/1901/articles/stang
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

## Outstanding source gaps (not solved by the existing 92-item bibliography)

1. **Replay effect:** empirical repeated-playthrough agency comparison, if the paper wishes to make a general causal claim.
2. **Historical capability:** targeted technology history needed for assertions about probabilistic interpretation being unavailable/impractical across earlier software.
3. **Agent-native environment novelty:** directly compare epistemic multi-agent systems, information-flow control, event sourcing, data provenance, knowledge graphs and distributed simulation—not only agent memory frameworks.
4. **End-to-end feasibility:** an Enclave prototype or a formally specified executable reference is needed to measure Event correctness, retrieval leakage, actor-state consistency and inference load.
5. **Generality of sandbox criticism:** literature surveying relative prevalence of reactive authored-narrative systems versus mechanically sandboxed games.
6. **Economic comparisons:** deployment prices and independent model-serving capacity must be refreshed for any published cost claim.

## Recommended manuscript evidence language

- "X demonstrates" for a particular controlled outcome **within the investigated system and task**.
- "X provides precedent for" when adapting an existing architecture.
- "We propose / Enclave would" for design rules and unimplemented guarantees.
- "Under the assumed workload, the model estimates" for §§15–16 numbers.
- "We hypothesize" for the repeated-replay effect until direct evidence exists.
- "Related work has explored partial versions" rather than "no system does this" unless prior art has been exhaustively searched.

## Audit deliverables

- This document: reviewed source-to-claim findings with explicit boundaries, remedy and primary-source links.
- docs/research/claim-to-source-subsection-inventory-2026-10-09.json: mechanically extracted subsection, representative argument, support lines and focused-review status for every subsection, with **unreviewed sections explicitly marked**.
- docs/paper-outline.md: narrowly corrected §2.1, §2.3, §3.9 and §4.6 without rewriting the architecture or approved §16.6.
- Previous bibliography-verification ledger remains valid but should **not** be mistaken for a claim-to-source audit.

**Bottom line:** Enclave has credible conceptual and technical antecedents for much of its motivation. Its strongest originality statements and practical feasibility claims are **research propositions**, not results already established by references to adjacent work.
