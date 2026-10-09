# Signals Participant Interaction Sensitivity

**Date:** 2026-10-08
**Purpose:** Sensitivity analysis for one Participant-controlled Actor in the Section 15 *Signals* workload.
**Status:** Explicit engineering scenarios, not an empirical prediction of player behaviour.

## 1. Background Anchor

The 36-settler simulation produces a median:

- **2,197 Interactions**;
- **1,022 model-driven cognition calls**;
- **3.086M model tokens**.

First-order scaling to the complete **43 model-driven Cognitive Actors**:

```
scale = 43 / 36 ≈ 1.19444
```

Rounded background:

- social Interactions: **~195**;
- Actor↔world Interactions: **~2,428**;
- total Interactions: **~2,624**;
- social cognition calls: **~658**;
- Actor↔world cognition calls: **~563**;
- total model-driven calls: **~1,221**;
- model tokens: **~3.686M**.

The scaling is intentionally simple. Romulans may be more active than settlers while the remote Starfleet Actors may be less active.

## 2. Participant Actor

Use **one human Participant controlling one Participant Actor**.

While controlled:

```
Participant cognition inference = 0
```

The Participant Actor still:

- interacts with Actors and the world;
- creates attempted actions;
- undergoes authoritative resolution;
- creates Events/Memories/state changes;
- can trigger model-driven cognition in affected Actors.

A practical party-based game could use hybrid party members that revert to model-driven cognition when not controlled. That is outside this reference case.

## 3. Activity Scenarios

Ordinary Actor interaction density:

```
2,197 / 36 ≈ 61 Interactions / 8 hours
```

Use four sensitivity scenarios:

| Participant activity | Participant Interactions |
| --- | ---: |
| **2×** | ~122 |
| **4×** | ~244 |
| **6×** | ~366 |
| **8×** | ~488 |

## 4. Downstream Cognition Assumption

For sensitivity analysis:

- 25% of Participant Interactions immediately require model-driven interpretation/response/reconsideration;
- each response-bearing Interaction causes an average of 2 model-driven cognition calls.

Equivalent:

```
additional NPC calls = Participant Interactions × 0.25 × 2
                     = Participant Interactions × 0.5
```

This factor is intentionally arbitrary-but-explicit. It is not an empirical player-behaviour parameter.

## 5. Combined Workload

| Participant activity | Participant Interactions | Added NPC calls | Total Interactions | Total model calls |
| --- | ---: | ---: | ---: | ---: |
| **2×** | ~122 | ~61 | **~2,746** | **~1,282** |
| **4×** | ~244 | ~122 | **~2,868** | **~1,343** |
| **6×** | ~366 | ~183 | **~2,990** | **~1,404** |
| **8×** | ~488 | ~244 | **~3,112** | **~1,465** |

Participant cognition calls remain zero in every row.

## 6. Token Volume

Background call split:

- 658 social/complex calls at 4,000 input / 250 output;
- 563 world calls at 1,500 input / 80 output.

Background:

```
input  = 3,476,500
output =   209,540
total  = 3,686,040
```

For a conservative first-order estimate, treat all Participant-induced NPC calls as social/complex 4,000/250 calls.

| Scenario | Added calls | Input | Output | Total tokens |
| --- | ---: | ---: | ---: | ---: |
| Background | — | 3,476,500 | 209,540 | **3,686,040** |
| **2×** | 61 | 3,720,500 | 224,790 | **3,945,290** |
| **4×** | 122 | 3,964,500 | 240,040 | **4,204,540** |
| **6×** | 183 | 4,208,500 | 255,290 | **4,463,790** |
| **8×** | 244 | 4,452,500 | 270,540 | **4,723,040** |

## 7. Runtime Storage Sensitivity

Participant cognition inference is zero, but Participant Interactions still create persistent Enclave records.

For each Participant Interaction, use the first-order storage rule:

- 2 Event records: Interaction Event + resulting Event;
- 2 generated Facts under the one-Fact-per-Event assumption;
- 1 Participant Actor Memory;
- ~0.5 NPC Memories on average from downstream Actor involvement.

That is approximately **5.5 vector-bearing records per Participant Interaction**. Additional cascading Events are possible but are not assumed in the baseline.

Using the ~13,339-record / ~123.75 MiB 43-Actor background runtime:

| Scenario | Added records | Runtime records | Runtime storage |
| --- | ---: | ---: | ---: |
| **2×** | ~671 | **~14,010** | **~129.98 MiB** |
| **4×** | ~1,342 | **~14,681** | **~136.20 MiB** |
| **6×** | ~2,013 | **~15,352** | **~142.43 MiB** |
| **8×** | ~2,684 | **~16,023** | **~148.65 MiB** |

The Participant Actor creates **no cognition inference**, but its Memories and the Events/Facts caused by its actions persist normally.

## 8. Interpretation

The computational asymmetry is:

```
Participant action
 -> Interaction
 -> authoritative resolution
 -> zero Participant cognition calls
 -> zero or more model-driven Actor cognition calls
 -> persistence / propagation
```

Participant activity therefore increases inference cost through **causal fan-out**, not by charging inference to the Participant Actor itself.
