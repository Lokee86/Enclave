# Signals High-Fidelity Reference Workload

**Date:** 2026-10-07; revised 2026-10-08
**Purpose:** Define the current *Signals* workload used by Section 15.
**Status:** Working engineering model. Counts are modelling assumptions or synthetic-simulation outputs unless explicitly sourced.

**Authoritative calculations:** `docs/signals-section15-consolidated-computational-model-2026-10-08.md`

## 1. Reference Scenario

Use the major-divergence *Signals* path developed in Section 14.10.

Reference duration:

- approximately **eight hours of in-world mission time**;
- engineering assumption, not canonical adventure duration.

## 2. Reference Population

Model-driven Cognitive Actors:

| Group | Count |
| --- | ---: |
| Settlement, including Ero Drallen and Drev Katel | ~36 |
| Surviving Romulans: Centurion + 4 Uhlans | 5 |
| Remote Starfleet Captain while causally relevant | 1 |
| Surviving *Susquehanna* distress-source Actor while causally relevant | 1 |
| **Total model-driven Cognitive Actors** | **43** |

Participant reference:

- **1 human Participant**;
- **1 Participant-controlled Actor**;
- **0 Participant cognition inference calls**.

The published quickstart provides six pregenerated player characters. A real party implementation could treat uncontrolled party members as hybrid Cognitive Actors; this simplified computational reference does not.

Inactive/dead historical Actors remain persistent records where narratively required.

Total simplified living population:

```
43 model-driven + 1 Participant Actor = 44 living Actors
```

## 3. High-Fidelity Boundary

Within the adventure's causal scope:

- each living model-driven NPC is individually persistent;
- no crowd/squad aggregation in the baseline;
- Actors maintain independent Knowledge access, Memories, relationships, goals, plans, activity, and location;
- off-screen Actors continue to act when causally relevant;
- Actor↔Actor and Actor↔world Interactions are represented;
- canonical and noncanonical Knowledge remain distinct;
- consequential Interactions become persistent Events/state;
- authoritative physical/rule outcomes remain conventional computation;
- cognition is triggered by interpretation, choice, planning, communication, or reconsideration rather than every simulation tick.

## 4. Starting Persistent State

### 4.1 Semantic/world Knowledge

Use an explicit high-fidelity envelope:

- **100,000–200,000 world Knowledge/state records**;
- **150,000 central**.

Central breakdown:

| Category | Records |
| --- | ---: |
| Valley geography/environment/ecology/geology/weather/routes | 30,000 |
| Settlement Facet, structures, infrastructure, spatial/operational state | 25,000 |
| Objects/equipment/resources/material affordances | 15,000 |
| Settlement history/culture/institutions/local Knowledge | 12,000 |
| Federation/Starfleet history/law/organization/doctrine/procedure | 18,000 |
| Romulan/Vulcan history/culture/politics/doctrine | 16,000 |
| Science/technology/medicine/species/general setting Knowledge | 17,000 |
| Domains/Enclaves/Rank/Facets/classification relationships | 5,000 |
| Mission/obelisk/Susquehanna/crash/signal/casualties/evidence | 7,000 |
| Current canonical Actor/institutional state, plans, reports, communications, external agents | 5,000 |
| **Total** | **150,000** |

This replaces the earlier ~1,300 and ~10,000 starting-state estimates.

### 4.2 Actor history

Assume:

- **1,000 prior persistent Memories per living Actor**;
- **44 living Actors**;
- **44,000 prior Memories**.

### 4.3 Runtime-generated Facts, Events, and Memories

The earlier ~400-Event / ~2,000-Memory estimate is retired.

For storage accounting:

- every Interaction is itself an **Event**;
- resolving that Interaction produces a **resulting Event**;
- additional cascading Events are possible but are **not assumed in the baseline**;
- use **1 generated Fact per Event** as the central first-order assumption;
- persist **1 Memory per participating Actor per Interaction**;
- Facts, Events, and Memories all use the same **9.5 KiB vector-bearing record cost** for this calculation.

36-settler control median:

- ~2,197 Interactions;
- ~4,394 mandatory Interaction/result Event records;

- **~4,394 Event records**;
- **~4,394 generated Facts**;
- ~2,380 Memories;
- **11,167 median generated vector-bearing records**;
- **~103.59 MiB**.

Scaled 43-Cognitive-Actor background:

- ~2,624 Interactions;
- ~5,248 mandatory Interaction/result Event records;

- **~5,248 total Event records**;
- **~5,248 generated Facts**;
- ~2,843 Memories;
- **~13,339 generated records**;
- **~123.75 MiB**.

Participant sensitivity raises total runtime storage to approximately **129.98–148.65 MiB** across the 2×–8× activity envelope.

## 5. Storage

Working physical vector-bearing-record cost:

- **~9.5 KiB/record**;
- historical GottZ/ctx PostgreSQL + HNSW benchmark;
- Reliquary ~5 KiB fully vectorized Memory retained only as efficiency comparison.

Ordinary 43-Cognitive-Actor background formula:

```
vector records = world Knowledge
               + 44,000 prior Memories
               + 13,339 runtime-generated Events/Facts/Memories
               = W + 57,339
```

| World Knowledge | Records | Vector-bearing storage |
| ---: | ---: | ---: |
| 100,000 | 157,339 | ~1.43 GiB |
| **150,000** | **207,339** | **~1.88 GiB** |
| 200,000 | 257,339 | ~2.33 GiB |

Runtime-generated records alone are approximately **123.75 MiB** in the background case and **129.98–148.65 MiB** across the Participant activity scenarios.

Additional Enclave graph/provenance/relationship/index/replication structures are not assigned an invented multiplier and must be measured separately.

Game-engine/assets/terrain/rendering/audio/physics/navigation/application storage are explicitly outside the Enclave calculation.

## 6. Ordinary Settlement Workload

The reproducible simulator is:

- `scripts/signals_settlement_sim.py`

Data:

- `data/signals-settlement-sim/`

Detailed methodology:

- `docs/signals-settlement-temporal-contact-simulation-2026-10-07.md`

Median 10,000-run result for 36 settlers:

| Metric | Median | P05–P95 |
| --- | ---: | ---: |
| Social Interactions | 163 | 143–183 |
| Actor↔world Interactions | 2,033 | 1,959–2,109 |
| **Total Interactions** | **2,197** | **2,120–2,275** |
| Social cognition calls | 551 | 474–631 |
| Actor↔world cognition calls | 471 | 429–513 |
| **Total cognition calls** | **1,022** | **935–1,112** |
| Generated Event records | **4,394** | **4,244–4,548** |
| Generated Fact records | **4,394** | **4,244–4,548** |
| Generated Memory records | **2,380** | **2,294–2,467** |

Per settlement Actor:

- ~61 Interactions / eight hours;
- ~28.4 cognition calls / eight hours.

## 7. 43-Cognitive-Actor Background Estimate

Scale the 36-settler control by:

```
43 / 36 ≈ 1.19444
```

Rounded:

- **~195 social Interactions**;
- **~2,428 Actor↔world Interactions**;
- **~2,624 total background Interactions**;
- **~658 social/complex cognition calls**;
- **~563 Actor↔world cognition calls**;
- **~1,221 model-driven calls**.

This is an explicit simple extrapolation. It does not claim the Romulans and remote Starfleet Actors have identical activity distributions to settlers.

## 8. Token Profiles

Social/dialogue/complex cognition:

- 4,000 input;
- 250 output.

Routine Actor↔world cognition:

- 1,500 input;
- 80 output.

43-Actor background:

```
input  = 3,476,500
output =   209,540
total  = 3,686,040 ≈ 3.69M tokens
```

## 9. Participant-Controlled Actor

Participant cognition originates outside Enclave:

```
Participant cognition calls = 0
```

Participant actions still create:

- Actor↔world Interactions;
- Actor↔Actor/group Interactions;
- authoritative resolution;
- Events;
- Memories;
- Knowledge propagation;
- model-driven NPC cognition when affected Actors interpret/respond/reconsider.

Use four activity scenarios relative to ~61 ordinary Actor Interactions/eight hours:

| Participant activity | Participant Interactions |
| --- | ---: |
| 2× | ~122 |
| 4× | ~244 |
| 6× | ~366 |
| 8× | ~488 |

Sensitivity fan-out assumption:

```
25% response-bearing × 2 NPC calls each
= 0.5 added NPC calls / Participant Interaction
```

| Scenario | Added NPC calls | Total Interactions | Total model calls | Input tokens | Output tokens | Total tokens |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| **2×** | ~61 | ~2,746 | ~1,282 | ~3.721M | ~0.225M | **~3.945M** |
| **4×** | ~122 | ~2,868 | ~1,343 | ~3.965M | ~0.240M | **~4.205M** |
| **6×** | ~183 | ~2,990 | ~1,404 | ~4.209M | ~0.255M | **~4.464M** |
| **8×** | ~244 | ~3,112 | ~1,465 | ~4.453M | ~0.271M | **~4.723M** |

Detailed derivation:

- `docs/signals-participant-interaction-sensitivity-2026-10-08.md`

## 10. Probabilistic Work Boundary

Inference is counted only for model-driven Actor cognition.

Section 15 intentionally declines to model inference potentially used internally by:

- Enclave implementation;
- Memory implementation;
- retrieval/indexing infrastructure;
- synthesis/compression systems.

Participant cognition is likewise outside Enclave inference.

## 11. Deterministic / Authoritative Work

Conventional computation remains responsible for:

- combat/rule resolution;
- damage/injury and medical state;
- movement/Locus change;
- possession/custody;
- physical systems;
- communications connectivity;
- event-condition evaluation;
- Domain/Enclave/Rank/Facet relationships;
- Knowledge-access/propagation rules;
- persistence/indexing.

The old ~2,750 deterministic-operation estimate is retained only as historical arithmetic in the evidence ledger; the revised Interaction model implies that authoritative-operation counts should eventually be regenerated from the simulator rather than fixed independently.

## 12. Research Anchors

Social contact/interactions:

- Mossong et al. 2008: mean 13.4 contacts/person/day.
- Zhaoyang et al. 2018: approximately 12 social interactions/day.
- Reconnect 2026: 9.1 daily contacts overall, 7.8 for adults, with overdispersion.

These support order-of-magnitude plausibility only; they do not define Enclave Interaction.

Full source URLs and external compute/storage evidence are maintained in:

- `docs/signals-section15-consolidated-computational-model-2026-10-08.md`;
- `docs/signals-computational-evidence-and-assumptions-2026-10-07.md`.

## 13. Current Central Reference

For Section 15 calculations, use:

- **43 model-driven Cognitive Actors**;
- **1 Participant Actor**;
- **0 Participant cognition calls**;
- **44 living Actors**;
- **150,000 central world Knowledge records**;
- **44,000 prior Actor Memories**;
- **~1.88 GiB vector-bearing Enclave corpus** after the ordinary eight-hour background run at the 150k world-Knowledge central case;
- **~2,624 background Interactions**;
- **~1,221 background model calls**;
- **~3.477M input + ~0.210M output = ~3.686M background model tokens**;
- Participant activity sensitivity from **2× to 8×**, giving:
  - **~2,746–3,112 total Interactions**;
  - **~1,282–1,465 total model calls**;
  - **~3.721–4.453M input + ~0.225–0.271M output = ~3.945–4.723M total model tokens**.

The Participant activity range is an explicit sensitivity envelope rather than a prediction of one correct play style.
