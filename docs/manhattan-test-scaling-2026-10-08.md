# The Manhattan Test — Section 15.10 Scaling Worksheet

**Date:** 2026-10-08
**Purpose:** Reproducible first-order extrapolation of the *Signals* workload to urban scale. This is **not** a simulated Manhattan population, implementation benchmark, or cost quotation.

## Population and baseline

- 2025 U.S. Census Bureau estimate, New York County (Manhattan): **1,664,862** residents. Source: https://www.census.gov/quickfacts/fact/table/newyorkcountynewyork/PST045225 (checked 2026-10-08).
- Section 15 *Signals* background population: **43 Cognitive Actors**, excluding one separately modelled Participant Actor.
- Scaling factor: **1,664,862 / 43 = 38,717.72093023256**.
- Eight simulated hours: **28,800 seconds**.
- Same synthetic per-Actor activity and persistence rates at all scales. No additional urban-specific model, and **no validation of uniform activity**.

## Baseline figures reused

| Quantity per 43 Actors / 8 h | Value |
| --- | ---: |
| Interactions | 2,624 |
| Event records (two per Interaction) | 5,248 |
| Generated Facts (one per Event assumption) | 5,248 |
| Generated records including Memories | 13,339 |
| Storage per generated record | 9.5 KiB |
| Model inference calls | 1,221 |
| Input tokens | 3,476,500 |
| Output tokens | 209,540 |
| Total tokens | 3,686,040 |

All quantities are first-order background approximations except the counted model reference inputs. Participant causal fan-out is not scaled into this city baseline.

## Recalculation

For each quantity **Q**, Manhattan Q ≈ Q_43 × (1,664,862 / 43).

| Manhattan metric | Eight-hour total | Mean per simulated second |
| --- | ---: | ---: |
| Interactions | ~101,595,300 | ~3,528 |
| Generated Event records | ~203,190,599 | ~7,055 |
| Generated vector-bearing records | ~516,455,679 | ~17,932 |
| Model-driven inference calls | ~47,274,337 | ~1,641 |
| Input tokens | ~134.602 billion | ~4.674 million |
| Output tokens | ~8.113 billion | ~281,698 |
| Input + output tokens | ~142.715 billion | ~4.955 million |

**Eight-hour newly generated storage:** 516,455,679 × 9.5 KiB / (1024³ KiB/TiB) ≈ **4.569 TiB**.
**Simulated day** at unchanged intensity: 4.569 × 3 ≈ **13.708 TiB**.
**Simulated 365-day year** at unchanged intensity: 4.569 × 3 × 365 / 1024 ≈ **4.886 PiB**.
**Starting personal Memory only:** 1,664,862 × 1,000 × 9.5 KiB / (1024³ KiB/TiB) ≈ **14.730 TiB**.

**Illustrative hosted inference cost:** model mix assumes 70% Luna, 25% Sol and 5% Astra and the same per-million token pricing as §15.8. Weighted input price = **$1.07/M**, weighted output = **$5.35/M**. Thus ~134,602.157M input × $1.07/M + ~8,112.911M output × $5.35/M = **~$187,428 per eight simulated hours**.

**Single-request hardware scale illustration:** ~281,698 output tokens/s divided by published DGX Spark GPT-OSS-20B output generation rate of 82.74 tokens/s ≈ **3,405× single-request generation throughput**. This ratio is **not a GPU-count estimate**, since hardware, batching, serving optimization, KV cache, model requirements, latency and concurrency differ.

## Scope and interpretation

- Excludes city-specific world Knowledge, extra relationship/provenance indexes, game-engine storage, visitors and commuters, large causal cascades, additional cognition/internal Memory inference, and hosting operations.
- The assumptions may greatly overestimate independent per-Actor activity or storage growth: they extrapolate the activity density of a small, narratively relevant cast to a whole city.
- Uniform 24-hour intensity additionally exaggerates long-term totals if Actors sleep or have quiet periods.
- Conversely, high fan-out, crowd-scale information diffusion, and operational cost may grow nonlinearly and are not represented.
- The proposed architecture is **tractable at bounded narrative scale under these assumptions**, but the unmodified model becomes **impractical at urban scale**. This motivates Section 16's consideration of architectural adaptation and variable simulation fidelity.

## Section 16.6 — Uniform-Fidelity Implementation Comparison (2026-10-08)

This is an extension of the preceding **background-only** Manhattan Test; the original background figures above are **unchanged**. Eight simulated hours, **1,664,862 NPCs**, and the same first-order per-NPC §15 activity assumptions apply.

### Additional Participant-density assumption

Neither Reactive Dialogue nor Persistent Characters has a meaningful fixed inference rate per NPC: inference depends on **active Participants**, not total NPC population. For a controlled comparison with *Signals*, assume **one active Participant Actor per 43 NPCs**, or about **38,718 simultaneous Participants** for Manhattan, each at **4× ordinary Actor activity** (244 Interactions, 25% dialogue, two 4,000/250-token responses per dialogue). This is an illustrative, exceptionally large concurrent-Participant population — **not** an empirical player-population estimate. With *P* active Participants, Level 1 and 2 cost **122 × P dialogue calls**; if *P* is zero, conversational inference is zero regardless of Manhattan's NPC count.

### Comparative eight-hour workload

| Uniform level | Model calls | Model tokens | Routed inference cost (USD) | New vector-bearing rows | Generated vector storage |
| --- | ---: | ---: | ---: | ---: | ---: |
| Level 1 — Reactive Dialogue | 4,723,562 | 20.075B | $26,535 | 0 | 0.000 TiB |
| Level 2 — Persistent Characters | 4,723,562 | 20.075B | $26,535 | 2,361,781 | 0.021 TiB |
| Level 3 — full narrative architecture | 51,997,899 | 162.790B | $213,963 | 568,414,861 | 5.029 TiB |

- **Level 1** includes only reactive dialogue inference and no new vector-bearing NPC Memories or routine Enclave Events. It still requires conventional world-state storage and any authored dialogue/Knowledge corpus.
- **Level 2** has identical dialogue inference, plus approximately **2,361,781 new NPC Memories** (**21.40 GiB**) for the active Participants' dialogue. Giving **all 1,664,862 NPCs 1,000 pre-existing Memories** already requires **14.730 TiB** of vector-bearing historical Memory, before authorship, new Memory, relationship indexes or game-engine state.
- **Level 3** includes the original §15 **background-only** ~47.27 million autonomous calls, ~142.715 billion tokens and ~4.569 TiB generated vector records, **plus** the 38,718 Participants' direct and downstream interactions. At this particular density it becomes **~51.998 million calls**, **~162.790 billion tokens**, and **~5.029 TiB** of newly generated vector records. The §15 background-only cost figures should **not** be overwritten with this Player-inclusive scenario.
- The table prices *new records only*. **City-scale authored/world Knowledge remains unspecified**, and the total Manhattan Enclave corpus cannot therefore be computed responsibly. It excludes additional graph and provenance structures, network/synchronization, actual inference-serving capacity, causal bursts, player-side client work and the game engine.
- **Interpretation:** Levels 1–2 are driven by Participant conversation volume; Level 3 incurs background autonomous cognition from all represented Cognitive Actors. Actual shared-world scaling, zone boundaries and parallel Event processing belong in a future scaling Appendix/Addendum.

Calculation source: scripts/signals_section16_fidelity_calculations.py; machine-readable results: data/signals-section16-fidelity-results.json; assumptions inherited from docs/signals-section15-consolidated-computational-model-2026-10-08.md.
