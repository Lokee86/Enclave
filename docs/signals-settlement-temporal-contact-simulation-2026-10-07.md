# Signals Settlement Temporal-Contact and World-Interaction Simulation

**Date:** 2026-10-07; revised 2026-10-08
**Purpose:** Derive an ordinary-day settlement workload from simulated activity rather than arbitrary calls per Actor.
**Status:** Reproducible synthetic engineering model; not an empirical human-behaviour model.

## 1. Model

The model follows:

```
schedule
 -> Locus occupancy
 -> Actor↔Actor contact opportunity
 -> social/group Interaction
 -> cognition where required

activity
 -> Actor↔world Interaction
 -> deterministic continuation OR fresh cognition
 -> consequential Event where applicable
```

It deliberately avoids enumerating arbitrary Actor subsets.

For 36 settlers:

```
C(36,2) = 630 possible unique Actor pairs
```

Group Interactions are represented directly as multi-Actor Interactions rather than all possible subgroups.

## 2. Synthetic Settlement

The generated settlement contains:

- 36 Cognitive Actors;
- 12 three-person households;
- mining, agriculture, maintenance, logistics, security, medical, administration, and leadership occupations;
- work crews;
- household/social relationships;
- home, work, commons, transit, and social Loci;
- an eight-hour schedule;
- Ero Drallen and Drev Katel inside the 36-person population.

Files:

- `data/signals-settlement-sim/actors.csv`
- `data/signals-settlement-sim/schedule.csv`
- `data/signals-settlement-sim/contact_episodes.csv`
- `data/signals-settlement-sim/runs.csv`
- `data/signals-settlement-sim/summary.json`
- `scripts/signals_settlement_sim.py`

## 3. Temporal Contact

Resolution: **5 minutes**.

Continuous pairwise co-presence is merged into contact episodes rather than counted once per tick.

Current synthetic schedule:

- possible unique pairs: 630;
- pairs co-present at least once: 630;
- merged contact episodes: 2,522;
- aggregate pair co-presence: 1,416 pair-hours.

The shared communal meal causes every pair to become co-present at least once. Co-presence is only an opportunity and does not imply a direct Interaction.

## 4. Social Interaction Model

Pair Interaction initiation rates per Actor-hour:

| Context | Rate |
| --- | ---: |
| Home | 0.80 |
| Work | 0.45 |
| Commons | 1.20 |
| Transit | 0.10 |
| Social | 1.00 |

Group Interaction rates per occupied Locus-hour:

| Context | Rate |
| --- | ---: |
| Home | 0.25 |
| Work | 0.18 |
| Commons | 0.65 |
| Transit | 0.03 |
| Social | 0.50 |

Partner weights:

| Relationship | Weight |
| --- | ---: |
| Household | 4.0 |
| Close/social cluster | 2.5 |
| Same crew | 2.0 |
| Same occupation | 1.35 |
| Other acquaintance | 1.0 |

Cognitive turns per social Interaction are sampled by context. This means an Interaction can require several model evaluations rather than exactly one.

## 5. Actor↔World Interaction Model

Ordinary life contains substantially more Interaction with tools, materials, objects, terrain, resources, and systems than direct social Interaction.

Work Interaction rates per Actor-hour:

| Occupation | Rate |
| --- | ---: |
| Miner | 11 |
| Agriculture | 9 |
| Maintenance | 12 |
| Logistics | 10 |
| Security | 7 |
| Medical | 9 |
| Administration | 6 |
| Leadership | 6 |

Non-work world Interaction rates:

| Context | Rate / Actor-hour |
| --- | ---: |
| Home | 4.0 |
| Commons | 2.5 |
| Transit | 3.0 |
| Social | 1.5 |

Only a minority require fresh cognition.

Work cognition probability per world Interaction:

| Occupation | Probability |
| --- | ---: |
| Miner | 0.16 |
| Agriculture | 0.18 |
| Maintenance | 0.24 |
| Logistics | 0.18 |
| Security | 0.22 |
| Medical | 0.32 |
| Administration | 0.26 |
| Leadership | 0.34 |

Non-work cognition probability:

| Context | Probability |
| --- | ---: |
| Home | 0.12 |
| Commons | 0.08 |
| Transit | 0.10 |
| Social | 0.06 |

These Actor↔world rates and cognition probabilities are synthetic engineering assumptions. No empirical claim is made for them.

For persistence accounting, every Interaction is itself an Event and authoritative resolution produces one resulting Event. Additional cascading Events are possible in a real world, but the baseline does not assign an arbitrary probability to them.

## 6. Monte Carlo Run

Command:

```powershell
python scripts/signals_settlement_sim.py --runs 10000 --seed 20261007 --output-dir data/signals-settlement-sim
```

Results:

| Metric | Mean | Median | P05 | P95 |
| --- | ---: | ---: | ---: | ---: |
| Pair Interactions | 152.6 | 153 | 133 | 173 |
| Group Interactions | 10.2 | 10 | 5 | 16 |
| Social Interactions | 162.9 | 163 | 143 | 184 |
| Actor↔world Interactions | 2,034.2 | 2,034 | 1,962 | 2,108 |
| **Total Interactions** | **2,197.0** | **2,197** | **2,122** | **2,274** |
| Social cognitive cycles | 551.8 | 551 | 474 | 633 |
| World-cognition triggers | 385.8 | 386 | 354 | 418 |
| Actor↔world cognitive cycles | 470.8 | 471 | 430 | 513 |
| Generated Event records | 4,394.0 | 4,394 | 4,244 | 4,548 |
| Generated Fact records | 4,394.0 | 4,394 | 4,244 | 4,548 |
| Generated Actor Memories | 2,380.1 | 2,380 | 2,294 | 2,467 |
| **Total generated vector-bearing records** | **11,168.1** | **11,167** | **10,783** | **11,557** |
| **Total cognitive cycles** | **1,022.6** | **1,022** | **935** | **1,112** |

Per Actor over eight hours:

```
2,197 / 36 ≈ 61.0 Interactions
1,022 / 36 ≈ 28.4 cognitive cycles
```

## 7. Token Profiles

Use:

- social/dialogue/complex cognition: **4,000 input / 250 output**;
- routine Actor↔world cognition: **1,500 input / 80 output**.

For the median 36-Actor control:

```
social:
551 × 4,000 = 2,204,000 input
551 ×   250 =   137,750 output

world:
471 × 1,500 =   706,500 input
471 ×    80 =    37,680 output

total:
2,910,500 input
175,430 output
3,085,930 model tokens
```

## 8. Empirical Social-Interaction Anchors

These studies do not define Interaction exactly as Enclave does, but they give an external order-of-magnitude check for ordinary human social exposure:

- Mossong et al. (2008), POLYMOD: mean **13.4 contacts/person/day**.
- Zhaoyang et al. (2018): approximately **12 social interactions/day** in an adult EMA sample.
- Reconnect (2026): mean **9.1 daily contacts** overall and **7.8 for adults**, with overdispersion.

Sources:

- https://journals.plos.org/plosmedicine/article?id=10.1371/journal.pmed.0050074
- https://pmc.ncbi.nlm.nih.gov/articles/PMC6113687/
- https://journals.plos.org/plosmedicine/article?id=10.1371/journal.pmed.1005038

The simulator's social assumptions remain synthetic. Epidemiological contact and Enclave Interaction are not interchangeable.

## 9. Participant Boundary

The Section 15 reference now uses **one Participant controlling one Participant Actor**.

Participant Actor cognition is external:

```
Participant cognition calls = 0
```

Participant actions can nevertheless cause model-driven Actors to interpret, respond, plan, or reconsider. That workload is treated separately in:

- `docs/signals-participant-interaction-sensitivity-2026-10-08.md`

## 10. Limitations

- schedules are fixed across Monte Carlo runs;
- households are uniform;
- world Interaction rates are assumed;
- social rates are only loosely externally anchored;
- remote communication is not yet simulated explicitly;
- personalities are simplified;
- settlement topology is synthetic;
- the current control day has no Participant/Romulan crisis injection;
- the 43-Actor full-scope workload is extrapolated rather than directly simulated.

The model should therefore be used as a transparent workload generator, not as a claim that 1,022 is the true cognitive-cycle count of a real settlement.

## 11. Runtime Persistence Accounting

For storage:

- an Interaction is itself an Event;
- resolution produces a second, resulting Event;
- use one generated Fact per Event as the central first-order assumption;
- participating Actors retain Actor-specific Memories of the Interaction;
- additional cascading Events are possible but are not assumed in the baseline.

For the median 36-settler control:

```
2,197 Interactions
→ 4,394 Interaction/result Events
→ 4,394 generated Facts
+ 2,380 Actor Memories

combined median generated records = 11,167 (per-run median, not sum of component medians)
```

At **9.5 KiB/record**:

```
11,167 × 9.5 KiB ≈ 103.59 MiB
```

Thus the ordinary eight-hour settlement control generates roughly **104 MiB of vector-bearing Enclave history**.
