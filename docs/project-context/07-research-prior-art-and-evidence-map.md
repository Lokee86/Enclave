# Research, Prior Art, and Evidence Map

This file records **what the existing research corpus is for**. Detailed citations and notes remain in `docs/research/bibliography-notes.md`.

The paper should distinguish prior art from Enclave's own synthesis. Do not claim novelty for concepts that already have established terminology.

## Human authorship and generated narrative

Purpose:

- support the claim that human-authored work has distinctive creative breadth, structural variation, thematic/rhetorical characteristics, and authorial signatures;
- avoid simplistic claims that generated text is always experienced as inferior;
- preserve countervailing evidence where generated stories can perform competitively on some reader-experience measures.

Use this literature to support **human authorship as a design requirement**, not an absolute claim that models cannot generate enjoyable prose.

## Justin Alexander: situation design and node-based practice

Key practitioner concepts:

- "Don't Prep Plots" / prepare situations;
- scenario timelines;
- tools rather than contingencies;
- Three Clue Rule;
- revelation lists;
- node-based scenario design;
- naturalistic nodes;
- nodes are not everything;
- world activity and proactive Actors.

Use Alexander as precedent for:

- world-first authoring;
- situations over predicted Participant paths;
- information flow;
- authored future intention without fixed sequence;
- diegetic organization.

Boundary: Enclave is not simply an automated node-based campaign system, and node is not the world's ontology.

Retained artifact:

`docs/research/justin-alexander-node-based-design.pdf`

## Narrative architecture and authored worlds

**Henry Jenkins — Game Design as Narrative Architecture**

Role:

- support spatial/world-based narrative authorship;
- support information distributed through designed environments;
- reinforce that narrative meaning can be embedded in a world rather than only a sequence.

## Storylets / quality-based narrative

**Emily Short** and **Failbetter Games**

Role:

- precedent for conditionally available authored narrative;
- authored material need not occupy fixed sequence positions;
- shared state can control what becomes available next.

Distinction:

- Alexander nodes mainly organize loci of interaction/information;
- storylets organize conditionally available authored content;
- Enclave adds persistent world change, Actor-local information, authority, and open-ended interpretation.

## Emergent narrative and purposeful authoring

**Louchart et al. — Purposeful Authoring for Emergent Narrative**

Role:

- support the idea that emergent sequence can coexist with deliberate authorship;
- support Participant authorship inside a purposefully authored world.

## Drama management and authorial leverage

Sources include work by Chen, Nelson, Mateas, Stern, Rowe, Lester.

Role:

- prior art for runtime selection/composition of authored narrative structures;
- support authorial leverage;
- show attempts to get more realized narrative from finite authored material.

Enclave distinction:

- persistent epistemic state;
- external authority;
- independent bounded Actors;
- open-ended interpretation;
- persistent causal consequence.

## Narrative planning / explicit formalization

Sources include Fisher, Porteous et al., Hayton et al., Riedl & Bulitko, and behaviour-tree literature such as Iovino et al.

Role:

- support state-space/domain complexity;
- show planners/formal architectures remain bounded by represented actions, predicates, states, or behaviours;
- support the historical formalization bottleneck.

Do not dismiss these approaches. They are useful foundations and stepping stones.

## Generative agents / LLM game agents / open-ended wargames

Sources include:

- Park et al., *Generative Agents*;
- Hu et al., survey of LLM-based game agents;
- Hogan & Brennen, open-ended wargames.

Role:

- support practical open-ended semantic interpretation;
- support Actor reasoning and response;
- provide comparison points for model-driven agents.

Current Enclave distinction:

- the environment itself is adapted to persistent agent participation;
- canonical state and authority remain external to the model;
- the Actor persists independently of any model invocation;
- Actor-local epistemic state is architectural rather than merely prompt context;
- a temporary context is assembled from that bounded persistent state;
- attempted action is separated from authoritative resolution.

Section 12 is now stabilized enough to use these sources directly as precedent while preserving the distinctions above.

## Hybrid probabilistic-symbolic systems

Sources include PAL, LLM-Modulo, and neurosymbolic AI survey work.

Role:

- support the broader architectural precedent of assigning probabilistic and deterministic systems different responsibilities;
- support proposal/interpretation + validation/execution division.

## Persistent worlds and live human intervention

Sources already collected around Ultima Online, The Matrix Online, and Asheron's Call.

Role:

- show that human intervention/live narrative can add value;
- show the staffing/economic difficulty of persistent human Gamemaster coverage.

## Long context and persistent memory

Sources include:

- *Lost in the Middle*;
- LongBench;
- RULER;
- LongMemEval;
- MemGPT.

Role:

- support the claim that larger context is not equivalent to reliable persistent state;
- support retrieval/external-memory architecture;
- motivate the Agency-Persistence Gap;
- support the distinction between persistent Actor state and temporary active context.

## Human memory analogy

Sources include Cowan, Oberauer et al., Schacter, Schacter & Addis, Johnson/Hashtroudi/Lindsay, and working-memory/interference research.

Role:

- analogy for flexibility/persistence tradeoffs;
- support separation of contextual experience, semantic information, and source/provenance.

Use carefully: human memory is an analogy, not proof of LLM behaviour.

## Sandbox / emergence literature

Sources include Juul, Soler-Adillon, Ryan, Adams on *Dwarf Fortress*, Burgess & Jones, Evans on *Subnautica*, *Neighborly*, and Grinblat/Manning/Kreminski.

Role:

- establish systemic emergence and emergent narrative;
- establish bounded interaction vocabularies;
- distinguish world sandboxing from reactive authored narrative;
- avoid overclaiming novelty around "narrative sandbox."

The current Section 12 opening additionally uses *Dwarf Fortress* as an example of a more traditional procedurally generated narrative architecture to which Enclave could theoretically be applied even without probabilistic cognition.

## Episodic vs semantic memory

Sources:

- Tulving;
- Greenberg & Verfaellie.

Role:

- support the conceptual distinction between Actor-specific Memory and generalized/transmissible Facts;
- support Memory as persistent subjective history without implying the analogy defines implementation.

## Commercial / generalized prior-art note

Most contemporary agent memory frameworks identified so far are **agent-centric** rather than environment-centric.

The important Enclave distinction is an **agent-native environment layer**: making the environment itself suitable for persistent autonomous Actors before any one Actor begins reasoning.

Palantir Ontology remains a comparatively close commercial partial analogue because it models operational entities, relationships, and actions, but it is not equivalent to Enclave's narrative/epistemic architecture.

This comparison remains a working research direction and should be independently sourced before publication use.

## Section 12 evidence status

The Section 12 citation pass should rely primarily on the existing research corpus rather than expanding the bibliography unnecessarily.

### Persistent Actor state and external memory — covered

Use:

- Park et al. (2023), *Generative Agents*;
- Wu et al. (2025), *LongMemEval*;
- Packer et al. (2023), *MemGPT*.

These support persistent memory/retrieval architectures and long-lived agent state outside one active prompt. Enclave's exact persistent-Actor ontology remains its own synthesis.

### Bounded/asymmetric Actor perspective — covered as precedent

Use:

- Hogan & Brennen (2024), especially differentiated player history objects and information asymmetry;
- Park et al. (2023);
- Hu et al. (2024; revised 2026).

These establish practical agent operation from differentiated histories, memory, and perception/action context. They do not establish Enclave's exact epistemic-authority rule.

### Context construction and long-context limitations — strongly covered

Use:

- Liu et al. (2024), *Lost in the Middle*;
- Bai et al. (2024), *LongBench*;
- Hsieh et al. (2024), *RULER*;
- Wu et al. (2025), *LongMemEval*;
- Packer et al. (2023), *MemGPT*.

These support the distinction between nominal context capacity, effective use of context, persistent memory, indexing/retrieval, and temporary active context.

### Divided cognitive responsibility — covered as architectural precedent

Use:

- Gao et al. (2023), *PAL*;
- Kambhampati et al. (2024), *LLM-Modulo*;
- Marra et al. (2024), neurosymbolic AI survey;
- Park et al. (2023) and Hogan & Brennen (2024) for agent-system examples.

These support hybrid decomposition and external validation/execution without implying that any of them already implement Enclave.

### Memory analogy — covered

Use:

- Tulving (2002);
- Greenberg & Verfaellie (2010).

These support the episodic/semantic analogy already used in §9.3 and carried into §12.4.

### Training-data narrative leakage — newly sourced

Use:

- Chang et al. (2023), *Speak, Memory: An Archaeology of Books Known to ChatGPT/GPT-4*;
- Carlini et al. (2021), *Extracting Training Data from Large Language Models*.

The narrow supported claim is that model parameters can retain information from training sources—including published books—independently of runtime context. This supports the caveat that Enclave's runtime epistemic boundary cannot guarantee absence of source knowledge already encoded in a third-party model.

Do **not** cite these papers as proving that leakage is inevitable for every model, that every publication is memorized, or that mitigation is impossible.

### Institutional information diffusion — still open

If Section 11's Saturation / Institutional Knowledge / Institutional Emission mechanism is formalized beyond architectural proposal, look for adjacent literature in information diffusion, organizational knowledge, epidemic/contact propagation, threshold models, and institutional communication.

The paper can present Enclave's synthesis without pretending the underlying mathematics is novel.