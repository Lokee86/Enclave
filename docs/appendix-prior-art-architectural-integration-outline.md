# Appendix C — Prior Art and Architectural Integration

> **Working appendix outline.** This appendix supports [§6.6, *Integrating Reactive Narratives*](paper-outline.md) and the system overview in §7. Its purpose is comparative—not to claim invention of component techniques or to assert that a complete competing implementation does not exist. This is a research-driven outline for an eventual appendix, not a full-text replication of all source studies, a patent search, or validation of Enclave as working software. The issue-specific evidence audit is recorded in [research R4](research/claim-to-source-audit-2026-10-09.md#focused-research-resolution-r4--agent-native-narrative-architecture-and-originality-66-77-2026-10-09).

## C.1 Scope: What Is Being Compared

- The relevant claim is **architectural integration for reactive human-authored narrative**, not novelty of autonomous agents, narrative sandboxes, state machines, knowledge graphs, or generative text in isolation.
- Distinguish four evidence levels in each comparison:
  - **Demonstrated:** a source reports a concrete implemented system, evaluation, or directly inspectable behavior.
  - **Documented / configurable:** architecture or extension points indicate a possible capability, but the full target workflow has not been demonstrated.
  - **Proposed:** Enclave or another system describes an intended contract without implementation evidence.
  - **Not established:** inspected material does not resolve whether a capability exists; **this must not be treated as proven absence**.
- Assess *what a system can author and represent*, *what actions can be interpreted*, *who can know what*, *who resolves outcomes*, *what consequences persist*, and *what narrative material responds to those changes*.
- Separate originality of a precise integration from claims of technical supremacy, commercial adoption, generality, efficiency, or security. These require different evidence.

## C.2 Earlier Approaches to Emergent Authored Narrative

### C.2.1 Narrative architecture, purposeful emergence, and conditional authored material

- **Jenkins (2004):** authored environments can convey narrative through spatial and systemic organization rather than only traversed plot sequences.
- **Louchart et al. (2008):** purposeful authoring for emergent narrative; supports the tension between authored goals and emergent runtime outcomes.
- **Drama management (Nelson, Ashmore & Mateas, 2006; Chen, Nelson & Mateas, 2009):** reusable state-informed interventions and authorial-leverage questions predate Enclave.
- **Storylets (Short, 2019; Failbetter Games):** authors construct conditional narrative material whose availability responds to represented world state.
- **Boundary:** these precedents justify §6.6's *integration problem*. They do not alone demonstrate Enclave's proposed Actor-specific epistemic propagation, Event authority, or full causal continuation; equally, Enclave cannot claim to invent conditional authored narrative or narrative emergence.

### C.2.2 Social simulation as narrative machinery

- **Comme il Faut / Prom Week (McCoy et al., 2011, 2013):** reusable social norms, knowledge and interaction structures allow authored social material to operate across recombined character relationships and situations. This is a **particularly direct precedent** for reducing the need to write every possible social branch.
- **Versu (Evans & Short, 2014):** autonomous characters select actions within authored social practices represented as reactive joint plans. Social practices supply affordances rather than controlling every Actor decision.
- These systems are closer to Enclave's **authored structures + agent autonomy** proposition than a generic LLM-character demo. Their architecture and design goals must appear explicitly in the paper's related-work discussion.
- The more defensible question is **which additional contracts Enclave proposes**, not whether simulationist storytelling already exists.

## C.3 Modern Agent-Native Simulated Environments

### C.3.1 Generative Agents (Park et al., 2023)

- Demonstrated agent memory, planning/reflection and socially coordinated local behavior in a 25-agent sandbox.
- Precedent for agents receiving differentiated histories and for local interactions to produce broader social effects.
- Study scope does **not** establish Enclave's proposed deterministic validation of every causal Event, bounded access-control correctness, or long-running scale.

### C.3.2 Concordia (Vezhnevets et al., 2023; official framework documentation)

- **Near-neighbor architecture:** agent memory and observations; natural-language intentions; configurable Game Master; interpretation and resolution of actions; recorded world variables; scene scheduling and configurable components.
- Its action/GM separation **directly precedes** an important Enclave pattern. The Game Master can resolve actions through model inference, and the framework's components permit custom resolution strategies.
- A blanket statement that Concordia *cannot* be extended with strict authority or persistent narrative rules would be unjustified without code-level comparison of those extensions.
- Key follow-up: compare how authority, witness perception, contradictory beliefs, provenance, group transmission and authored trajectories are expressed as enforceable interfaces versus application-specific prompts and custom components.

### C.3.3 Sonder Engine

- Public architecture describes objective truth, perception, personal Memory, Belief and narration as distinct layers; private character decision contexts; a Director-mediated outcome stage; and a single durable commit boundary.
- This is a **particularly close applied precedent** for separation between situated cognition and persistent truth.
- Distinguish repository-stated design intent, existing code/tests and independent evidence. Do not claim its invariant holds universally or that it lacks additional functionality based only on introductory documents.

### C.3.4 Bunnyland

- Persistent Entity Component System (ECS) world; human, scripted and model controllers can share validated action pathways; authoritative world mutations, events and restricted perspectives are formally described in its world contract.
- **Important nuance:** Bunnyland explicitly describes its durable authority as ECS state and checkpoints; its operational journal **is not event sourcing**. Do not conflate Event production with event-sourced reconstruction.
- Its action vocabulary is deliberately typed/bounded, making it a useful comparison for Enclave's proposed semantic interpretation of unexpected situations.
- Compare narrative continuity and epistemic/group behavior without assuming the absence of extension capabilities that have not been tested.

### C.3.5 Product-level adjacent claims

- Canonvale and other product descriptions discuss persistent worlds, faction/state memory and model-assisted characters.
- Advertising, pre-production descriptions and inaccessible implementations can establish **commercial interest and advertised goals**, not verified implementation fidelity.
- Such examples should be lower-confidence context, not treated as engineering proof or central scientific prior art.

## C.4 Established Computational Foundations Outside Interactive Narrative

| Research tradition | Established idea relevant to Enclave | Boundary / proposed use |
|---|---|---|
| **Dynamic epistemic logic** | Formal changes to multi-agent Knowledge and Belief under public, private and possibly misleading communication. | Enclave proposes runtime representational and retrieval rules for situated Actors, rather than inventing agent-relative epistemic state. |
| **Event sourcing and event-driven systems** | Committed changes, causal history, materialized current state, and audit/replay. | Enclave defines which resolved Interactions enter the world's authoritative causal record and how that affects future narrative conditions. Do not equate every event journal with event sourcing. |
| **ABAC / ReBAC and information-flow control** | Contextual/relationship-conditioned authorization and restricted information flow. | Enclave's Domains, Enclaves, Facets, Rank and Inheritance have narrative-specific semantics requiring independent specification and security tests. |
| **Database provenance** | Derivation and origin tracing of facts and assertions. | Enclave's proposed Memory/Knowledge transmission could use provenance to preserve conflicting reports and source chains, without turning consensus into canonical truth. |
| **Organizational knowledge and multi-agent communication** | Shared institutional Knowledge, group norms, disclosure and social diffusion. | Saturation and institutional promotion remain proposed Enclave rules; their exact thresholds, scope and correctness cannot be claimed as novel in the abstract. |
| **Distributed discrete-event simulation** | Causal ordering, synchronization and efficient locality of simulated updates. | Proposed Enclave scaling and Actor concurrency need algorithmic bounds and implementation benchmarks. |

## C.5 Comparative Capability Map

**Legend:** **Yes** = specifically documented in inspected material; **Partial** = documented in a bounded form; **Proposal** = Enclave's stipulated design target; **Unverified** = targeted evidence was not sufficient. **Unverified means neither yes nor no.** A complete final matrix requires version-pinned code-level checks; this is a *literature-and-documentation map*.

| Capability | Strong existing precedents | Enclave's proposed integration / remaining comparison |
|---|---|---|
| Reusable authored narrative or social structures | Storylets; CiF/Prom Week; Versu; drama management (**Yes**) | Authored trajectories remain conditional on causally changing world state (**Proposal**). |
| Agent reasoning with individual contextual memory | Generative Agents; Concordia; Sonder; Bunnyland (**Yes/Partial by system**) | Actor contexts constrained by a common knowledge-distribution ontology (**Proposal**). |
| Natural-language action interpretation | Concordia; Sonder (**Yes**), others in bounded forms | Allow interpretation of unanticipated input **without** model authority over world consequences (**Proposal**; arbitrary action freedom not guaranteed). |
| Independently committed authoritative state | Bunnyland; Sonder; configurable Concordia components (**Yes/Partial**) | Treat resolved Events as authoritative and tie them into authored narrative continuation (**Proposal**); not novel in isolation. |
| Witness-specific Knowledge and contradictory Belief | Dynamic epistemic logic; Sonder; restricted Bunnyland perspectives (**Yes/Partial**) | Link perception, Memory provenance, institutional group knowledge and later actor behavior (**Proposal**). |
| Institution/faction information diffusion and Saturation | Multi-agent knowledge exchange, organizational models, graph/rule engines (**Partial across traditions**) | Implement Enclaves, combinatorial membership, thresholds and inheritance with testable semantics (**Proposal**). |
| Demonstrated end-to-end quality or efficiency advantage | No comparable Enclave-versus-baseline trial reviewed | **Unverified** for Enclave; requires implementation and evaluation. |

**Interpretation:** The matrix identifies neither a monopoly nor a proven absence of an entire capability. Its intended use is to isolate *specific proposed interfaces and interactions* for subsequent technical comparison.

## C.6 What Enclave Actually Proposes to Integrate

- **Human-authored possibility space:** persistent characters, institutions, history, information, conflicts, planned developments and thematic material already exist before a Participant intervenes.
- **Authoritative causal boundary:** probabilistic cognition can propose, interpret and articulate actions; the system resolves and commits actual outcomes against shared state and constraints.
- **Epistemic plurality:** each Actor responds from accessible Knowledge, Memories and Beliefs; incorrect testimony and rumor can propagate without redefining canonical world truth.
- **Group-level semantics:** Domains, Enclaves, Facets, Inheritance and Saturation provide proposed ways to address and transmit information across relevant Actor populations, subject to fidelity/performance controls.
- **Narrative continuation:** persistent outcomes make future authored developments possible, impossible, altered or reinterpreted rather than merely choosing one preauthored path.
- These principles are **mutually constraining**. The research contribution, if successfully articulated, is a reusable specification of their interfaces and interaction rather than any single primitive.
- The absence of an identical combination in the surveyed literature is *not evidence of categorical uniqueness*. It is an open originality claim requiring careful delimitation.

## C.7 Comparative Worked Example: A Bridge, a False Report, and a Disrupted Plan

Use one identical story seed across Enclave and candidate baselines:

1. Authors establish a bridge, an imminent shipment, factions with conflicting goals, a scheduled meeting, several Actors with unequal access to information, and a feasible alternate route.
2. A Participant destroys the bridge without being observed by the officer who later needs to move the shipment.
3. A witness sees the destruction but falsely accuses a rival faction; other Actors hear different accounts.
4. The bridge's destruction is an authoritative Event; the accusation is information or Belief, **not** an authoritative change to who destroyed it.
5. The shipment cannot proceed as planned. Depending on available routes, resources, and Actor decisions, the meeting or planned development may be delayed, rerouted or cancelled.
6. Rumor spreads through appropriate contacts and organizations; group-level promotion depends on the explicitly defined Saturation policy, not mere omniscient retrieval.
7. After a save/restart or time advance, Actors' accessible information and the altered plan must remain coherent with the world record.
8. Compare how much of this can be realized **without bespoke per-outcome narrative branches**; identify where each existing framework can use custom extensions. Do not score unstated functionality as absent.

This is a **proposed discriminating test scenario**, not a completed implementation benchmark.

## C.8 Verification Tasks and Claims the Paper Must Not Make

- Produce version-pinned feature/contract comparisons for **Concordia, Comme il Faut, Versu, Sonder and Bunnyland**, including direct code/doc citations and negative cases.
- Specify testable invariants: authority of Events, admissible state changes, Actor knowledge eligibility, provenance preservation, contradictions, permitted information transfer, group-level saturation, and planned-event invalidation.
- Build an executable reference or formal model and validate against counterfactual consequences, knowledge leaks, false reports, overlapping group memberships, concurrency and restored history.
- Report narrative fidelity and authorial effort separately from storage, latency, inference cost and correctness.
- **Do not claim:** Enclave invented emergent narrative; all previous agents were omniscient; no prior system separates LLM reasoning from state; event sourcing, provenance and access control are new; Enclave has already demonstrated improved scale or authorial leverage.
- **Permissible qualified claim:** Enclave *proposes* a unified framework for persistent authored narrative causality and situated Actors, drawing on independently established techniques and placing them under explicit architectural contracts.

## C.9 Sources and Evidence Provenance

Selected direct references, links and implementation documentation for drafting the full appendix. **Bibliography reconciliation completed 2026-10-09:** the 13 missing publication/software references from §6.6 and Appendix C were added to the single alphabetized publication bibliography in `design-paper.md` (112 → 125 entries). Previously cited sources were retained without duplication. The earlier 92-reference verification ledger is a dated snapshot and **does not independently certify** these additions; software repositories and product descriptions remain lower-evidence implementation or marketing sources.

**Narrative and social simulation**
- [Jenkins (2004), *Game Design as Narrative Architecture*](https://web.mit.edu/~21fms/People/henry3/games&narrative.html); Louchart et al. (2008), *Purposeful Authoring for Emergent Narrative* (already mapped in the outline).
- [McCoy et al. (2011), *Comme il Faut: A System for Authoring Playable Social Models*](https://doi.org/10.1609/aiide.v7i1.12454); [McCoy et al. (2013), *Prom Week*](https://doi.org/10.1609/aiide.v9i1.12662).
- [Evans & Short (2014), *Versu—A Simulationist Storytelling System*](https://doi.org/10.1109/TCIAIG.2013.2287297).
- [Short (2019), *Storylets: You Want Them*](https://emshort.blog/2019/11/29/storylets-you-want-them/).

**Generative environments and modern implementations**
- [Park et al. (2023), *Generative Agents*](https://doi.org/10.1145/3586183.3606763).
- [Vezhnevets et al. (2023), Concordia research](https://arxiv.org/abs/2312.03664); [official Concordia repository](https://github.com/google-deepmind/concordia); [component architecture](https://github.com/google-deepmind/concordia/blob/main/concordia/components/README.md).
- [Sonder Engine repository](https://github.com/N0819/Sonder_Engine); [architecture and source-of-truth constraints](https://github.com/N0819/Sonder_Engine/blob/main/AGENTS.md).
- [Bunnyland repository](https://github.com/thalismind/bunnyland-server); [world contract](https://github.com/thalismind/bunnyland-server/blob/main/docs/developer/world-contract-v1.md).

**Supporting computational theory**
- [Stanford Encyclopedia of Philosophy, *Dynamic Epistemic Logic*](https://plato.stanford.edu/entries/dynamic-epistemic/).
- [Fowler (2005), *Event Sourcing*](https://martinfowler.com/eaaDev/EventSourcing.html).
- [NIST SP 800-162, *Guide to Attribute Based Access Control*](https://doi.org/10.6028/NIST.SP.800-162); [Fong (2011), relationship-based access control](https://doi.org/10.1145/1943513.1943539).
- [Buneman, Khanna & Tan (2001), *Why and Where: A Characterization of Data Provenance*](https://doi.org/10.1007/3-540-44503-X_20).

**Audit:** [R4 prior-art research and evidentiary distinctions](research/claim-to-source-audit-2026-10-09.md#focused-research-resolution-r4--agent-native-narrative-architecture-and-originality-66-77-2026-10-09).

**Status:** Appendix C is drafted as an annotated comparative **outline**, with sources reconciled into the publication bibliography and testable distinctions identified. It does not assert an empirically verified Enclave implementation, a completed code-level prior-art evaluation, or experimentally established architectural superiority.
