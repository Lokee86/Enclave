# Appendix C — The Replay Horizon: Epistemic Discovery and the Limits of Perceived Agency

> **Working appendix outline.** This appendix develops the argument introduced in §4.6 without altering that section. It separates (1) observable limits of fixed authored narrative structures, (2) a Participant's growing knowledge of those limits, and (3) the empirical question of how that knowledge changes perceived agency. It is a theoretical supplement, not a claim that a replay-dependent psychological decline has already been demonstrated.

## C.1 Perceived Agency, Causal Agency, and Epistemic Possibility

- **Causal agency** concerns which different, persistent consequences a Participant can actually produce through their choices under the world rules.
- **Perceived agency** concerns the Participant's subjective experience of having meaningful influence. Immediate acknowledgement, framing, and feedback can affect it without altering later world state.
- **Epistemic possibility** concerns the range of distinct outcomes that the Participant currently believes may be available.
- These concepts can diverge:
  - a system may respond convincingly while reconverging to the same outcome;
  - an uninformed Participant may underestimate genuine alternatives;
  - an experienced Participant may know every available outcome yet still deliberately choose among them.
- The relevant question is not simply *how many endings exist?* It is how knowledge of possible outcomes and their **causal differences** changes with interaction.
- Distinguish novelty, enjoyment, replay value, perceived influence, and actual consequence. A decline in one does not prove a decline in another.
- **Research boundary:** Day & Zhu (2017), Thue et al. (2011), Fendt et al. (2012), and Cardona-Rivera et al. (2014) provide related agency concepts and bounded empirical results, not a completed theory of replay exhaustion.

## C.2 The Initial Discovery Effect

- **First encounter:** the Participant sees only one realized trajectory and may reasonably suppose that alternative choices would produce meaningfully different consequences.
- **Second encounter:** choosing differently can reveal that the system responds, providing positive evidence of influence that was previously only anticipated.
- **Later encounters:** alternative paths may continue to be revealed, or previously unseen branches may become harder to find.
- Hypothesis: perceived agency can initially **increase** through demonstrated difference, even if the complete authored possibility space is bounded.
- This is compatible with **Roth et al. (2012)**:
  - fifty participants encountered the interactive drama *Façade* twice;
  - self-reported *effectance* rose on the second exposure;
  - this supports neither indefinite growth nor the specific idea that discovery of an alternative branch caused the change.
- **Roth & Vermeulen (2013)** examined the same replay program and found less in-character/complex input on second exposure: a Participant may learn how to work within an interface while simultaneously learning its limitations.
- **Crucial qualification:** the source evidence covers two exposures in one environment, not a long series of playthroughs or a direct manipulation of revealed reconvergence.

## C.3 Narrative Exhaustion and the Replay Horizon

- A **fixed authored branching narrative** can be represented as a finite set of distinguishable consequential outcomes under a declared observation window and criterion of difference. This does **not** assert that every interactive world or generative system has a tractably finite space.
- Define:
  - `O`: the fixed set of consequential outcome classes that the system can realize under the chosen comparison criterion;
  - `D_n`: outcome classes that the Participant has actually discovered after `n` completed playthroughs;
  - `U_n = |O \ D_n|`: the number of distinct outcome classes not yet encountered.
- Assuming every observed outcome belongs to `O` and discoveries are retained, `D_n` can only grow, so `U_{n+1} ≤ U_n`.
- **Conditional exhaustion result:** if exploration actually covers all of `O`, then `U_n = 0` thereafter. This follows from the finite-set definition; it is not a measured psychological result.
- **Not automatic:** infinitely many replays do not guarantee exhaustiveness if the Participant repeats the same route. Under independent sampling with strictly positive probability for every outcome class, the probability of complete coverage tends toward one as replay count grows; that extra sampling assumption must be stated.
- Introduce the **replay horizon** as the point or interval where *newly accessible meaningful differences become sufficiently rare or are believed to be exhausted* for the Participant's practical exploration.
  - This is **not necessarily** the moment every hidden branch has been discovered.
  - A tenth playthrough finding nothing new is evidence of diminishing **observed** novelty, not proof that `U_n=0`.
  - In very large spaces, the horizon may never be reached by a typical Participant.
- Separate exhaustion of **new discoveries** from persistence of the **ability to select already-known outcomes**.

## C.4 Epistemic Calibration and Convergence

- The Participant constructs a mental model of the system's possible consequences. That model can initially understate or overstate the system's actual branching and causal boundaries.
- Repeated interaction supplies observations that can calibrate the mental model:
  - **confirmation:** a new branch or consequential change shows that a choice matters;
  - **reconvergence:** different apparent choices lead to materially equivalent later state;
  - **invariance:** an apparently relevant decision leaves the consequential state unchanged;
  - **unresolved uncertainty:** some unvisited routes remain merely possible, not known.
- **Proposed two-phase account, not a universal curve:**
  - early discovery may increase confidence that actions have meaningful effects;
  - continued exploration can reveal limits of authored consequence and correct earlier overestimation;
  - ultimately, learning can plateau rather than drive a monotonic fall in overall agency.
- If an earlier subjective sense of freedom **depended on an overestimate** of causal alternatives, discovering a smaller possibility space supplies a reason to revise that estimate downward. It does *not* force enjoyment, effectance, or agency over **known alternatives** to decline.
- A replay of a fully understood narrative may still provide intentional agency: players can choose the desired known ending. The loss, if any, concerns **undiscovered or falsely anticipated consequences**, not the mere fact of informed choice.
- **Fendt et al. (2012)** found that some linear experiences acknowledging choices produced agency ratings similar to branching narratives on an initial test, although this did not establish equivalence; the study did not measure what happened when users discovered the structure.
- **Cardona-Rivera et al. (2014)** found that anticipated meaningful differences between choices matter for agency judgments. It does not demonstrate a replay-dependent decline.
- **Jones & Millard (2026)** explicitly question whether illusion-of-agency results hold after participants learn that choices lack wider consequences; treat this as a reasoned research observation, **not** a measured longitudinal effect.

## C.5 Consequences for Reactive Narrative Architectures

- Traditional fixed branching represents consequential alternatives primarily through authored conditional paths, scenes, flags, or outcome structures. Reconvergence is often an intentional and useful design technique.
- Such systems are not necessarily shallow: a finite system can contain substantial meaningful variation, and a player can preserve meaningful choice among known outcomes.
- Enclave proposes a different **mechanism of narrative possibility**:
  - Actors and Participants act within a persistent, authored world;
  - attempted actions enter authoritative Interactions and Events;
  - consequences modify canonical world circumstances, Actor Memories, available Knowledge, relationships, and subsequent opportunities;
  - later narrative develops from that changing state rather than selecting only among authored scene branches.
- This may postpone or change what constitutes the replay horizon: discovering one trajectory need not reveal every further consequence of intervening in the same authored situation.
- Do **not** equate generative flexibility with unlimited agency or infinite meaningful outcomes:
  - authored world constraints still apply;
  - supported actions, resolution rules, and computational budgets remain bounded;
  - a system can generate surface novelty without producing persistent consequential difference;
  - any advantage over authored branching is **proposed**, not established by the replay studies.
- The theoretically relevant comparison is **consequence diversity under repeated intervention**, not raw counts of text generations, endings, or dialogue variations.
- Connect the appendix to §§4.6, 5, 7, 8, 12 and 13 without recasting Enclave's architectural proposal as an experimentally demonstrated replay outcome.

## C.6 Testable Predictions and Research Design

- Distinguish the following candidate hypotheses:
  - **H1 — initial discovery:** an alternative playthrough revealing meaningful differences can increase perceived agency relative to the first exposure.
  - **H2 — reconvergence discovery:** learning that apparently distinct choices converge on equivalent consequential states reduces *perceived causal breadth* relative to learning that they remain distinct.
  - **H3 — conditional replay horizon:** diminishing new discoveries predicts lower *anticipated possibility* only when the Participant infers that little meaningful causal variation remains.
  - **H4 — architecture-dependent persistence:** when consequences continue to alter future opportunities, repeated intervention may maintain perceived causal breadth longer than a structurally comparable reconvergent narrative.
- **H1–H4 are proposed predictions, not established results.** H2 and H3 are closest to §4.6's original intuition; H4 would require empirical Enclave-like implementations.
- Suggested study:
  - compare (A) genuine branching with persistent divergent outcomes, (B) choices receiving convincing immediate feedback but converging later, and optionally (C) stateful systemic consequences with bounded but continuing causal variation;
  - make otherwise comparable sequences available over multiple sessions;
  - separate **number of replays** from **explicit/implicit discovery of reconvergence**;
  - track novel consequential states actually visited, perceived future possibilities, perceived effectance, choice satisfaction, awareness of structural limits, and engagement;
  - preregister definitions of a *meaningfully distinct consequence* and the temporal window over which persistence matters.
- Control for mastery of the interface, familiarity, narrative comprehension, player motivation, voluntary self-selection into many replays, and simple boredom.
- A cross-sectional comparison of first-time and tenth-time players would be weaker than within-participant trajectories or randomized revelation of narrative constraints.
- Negative or mixed findings would be informative: participants may learn the system, value known outcomes, and experience agency without novelty.

## C.7 Evidentiary and Editorial Boundaries

- **Deductive result:** under the stated fixed, finite, exhaustively explored outcome model, undiscovered outcome classes eventually reach zero.
- **Empirical results:** agency can differ from underlying causal divergence; feedback and anticipated meaningful consequences affect agency ratings in bounded experimental settings; effectance increased over two *Façade* exposures in one study.
- **Interpretation/hypothesis:** discovering reconvergence across repeated play may reduce a Participant's perceived space of meaningful consequences.
- **Unverified Enclave application:** reactive, persistent causal state may expand or preserve replay-time meaningful variation more effectively than enumerated paths.
- The appendix should **not** assert that tenth-playthrough agency must diminish, or that the particular source experiments prove long-horizon replay decay.
- §4.6 remains as written; the separate [claim-to-source audit](research/claim-to-source-audit-2026-10-09.md#focused-research-resolution-r1--46-repeated-play-reconvergence-and-perceived-agency-2026-10-09) records the evidence dispute and full research disposition.

### Research references to reconcile at bibliography stage

- Roth, C., Vermeulen, I., Vorderer, P., & Klimmt, C. (2012). [*Exploring Replay Value: Shifts and Continuities in User Experiences Between First and Second Exposure to an Interactive Story*](https://doi.org/10.1089/cyber.2011.0437).
- Roth, C., & Vermeulen, I. (2013). [*Breaching Interactive Storytelling's Implicit Agreement*](https://doi.org/10.1007/978-3-319-02756-2_20).
- Fendt, M. W., Harrison, B., Ware, S. G., Cardona-Rivera, R. E., & Roberts, D. L. (2012). [*Achieving the Illusion of Agency*](https://doi.org/10.1007/978-3-642-34851-8_11).
- Cardona-Rivera, R. E., Robertson, J., Ware, S. G., Harrison, B., Roberts, D. L., & Young, R. M. (2014). [*Foreseeing Meaningful Choices*](https://doi.org/10.1609/aiide.v10i1.12716).
- Stang, S. (2019). [*“This Action Will Have Consequences”: Interrogating Player Agency and Choice in Video Games*](https://gamestudies.org/1901/articles/stang).
- Jones, C., & Millard, D. E. (2026). [*Beyond Authorial Burden*](https://doi.org/10.1145/3757746).
- Existing §4.6 references: Day & Zhu (2017); Thue et al. (2011); Stang (2019). The audit's source-access and support limits remain applicable.

> **Status:** Working appendix outline only. Sources listed here are research candidates; no bibliography edits and no rewrite of §4.6 are implied.
