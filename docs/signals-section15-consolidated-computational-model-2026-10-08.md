# Signals / Section 15 Consolidated Computational Model

**Date:** 2026-10-08
**Purpose:** Authoritative quantitative basis for Section 15 of the Enclave paper.
**Status:** Current working model. Supersedes earlier 1,300/10,000-record scenario-state estimates, six-Participant-Actor accounting, the original ~1,000-call workload, and the contact-only ~695-cycle settlement control.

## 1. Scope and Accounting Boundary

This model estimates the computational and storage burden of the **Enclave implementation only**.

It includes:

- semantic/world Knowledge;
- Actor Memories;
- canonical Events;
- Actor/Knowledge/relationship/provenance structures;
- Domains, Enclaves, Rank, Facets, and Loci;
- retrieval/index structures;
- model-driven Actor cognition;
- deterministic authoritative Enclave operations.

It deliberately excludes the conventional game implementation required to make the environment playable:

- terrain meshes and rendering assets;
- textures, audio, and animation;
- physics/collision/navigation engine data;
- conventional game-state systems outside Enclave;
- application binaries and unrelated deployment content.

The paper therefore must not present the Enclave storage number as total game size.

## 2. Reference Population

The simplified high-fidelity *Signals* reference uses:

- **36 settlement Cognitive Actors**;
- **5 surviving Romulan Cognitive Actors**;
- **1 remote Starfleet Captain** while causally relevant;
- **1 surviving Susquehanna distress-source Actor** while causally relevant;
- **43 model-driven Cognitive Actors total**;
- **1 Participant controlling 1 Participant Actor**;
- **44 living in-world Actors total** for the simplified computational reference.

The published quickstart supplies six player characters. A practical party implementation could treat uncontrolled party members as hybrid Actors that revert to model-driven cognition, but that is outside this reference calculation.

Participant Actor cognition originates outside Enclave:

```
Participant cognition inference = 0
```

Participant actions still create Interactions, authoritative state changes, Events, Memories, Knowledge propagation, and downstream cognition in model-driven Actors.

## 3. Semantic World Knowledge

The earlier ~1,300 and later ~10,000 scenario-record estimates are retired as too sparse for the high-fidelity world being claimed.

Use:

- **100,000–200,000 semantic/world Knowledge records** as the explicit reference envelope;
- **150,000 records** as the central case.

### 3.1 Central 150,000-record breakdown

| Category | Records | Scope |
| --- | ---: | --- |
| Valley geography, ecology, geology, weather, routes, environmental semantics | 30,000 | Semantic representation of the inhabited mountain valley and its natural systems |
| Settlement Facet: structures, infrastructure, facilities, spatial and operational state | 25,000 | Buildings, work areas, mine systems, utilities, defenses, access, services, spatial relationships |
| Objects, equipment, resources, materials, affordances | 15,000 | Tools, weapons, medical resources, supplies, machinery, possessions, usable material state |
| Settlement history, culture, institutions, local Knowledge | 12,000 | Local history, norms, work practices, institutional knowledge, recent incidents, social context |
| Federation and Starfleet history, law, organization, doctrine, procedure | 18,000 | Relevant institutional and historical setting Knowledge |
| Romulan and Vulcan history, culture, politics, doctrine | 16,000 | Relevant historical, cultural, military, and political Knowledge |
| Science, technology, medicine, species, and general setting Knowledge | 17,000 | Engineering, sensors, communications, medicine, species knowledge, relevant technical background |
| Domains, Enclaves, Rank, Facets, and classification relationships | 5,000 | Classification structures and semantic identities required by Enclave |
| Mission, obelisk, Susquehanna, crash, signal, casualties, evidence | 7,000 | Immediate adventure-specific canonical/noncanonical state |
| Canonical Actor/institutional current state, plans, reports, communications, external narrative agents | 5,000 | Current plans, schedules, reports, orders, communications, remote causal agents |
| **Total** | **150,000** | |

The exact distribution is illustrative. The central count is an engineering assumption, not a claim that the published adventure literally contains 150,000 authored statements.

The reference should include at least a dozen relevant Domains. Examples include geography, ecology, geology, meteorology, settlement operations, mining/industrial practice, medicine, engineering, communications/sensors, Starfleet operations, Federation civics/history, Romulan military/politics, Vulcan culture/history, and xenotechnology.

At least five Enclaves are expected in the reference representation, including the settlement, Starfleet, Federation, Romulan institutional/military population, and relevant Vulcan institutional/cultural population. The settlement itself is represented as a Facet with its own intersecting Enclave structures.

## 4. Actor History

Use **1,000 pre-existing persistent Memories per living Actor**.

For the simplified 44-Actor reference:

```
44 × 1,000 = 44,000 pre-existing Actor Memories
```

This is an explicit engineering assumption chosen to give each Actor a substantial usable personal history. It is not a claim about human memory capacity.

## 5. Runtime Persistence and Generated Storage

The earlier **~400 Events / ~2,000 Memories** estimate is retired.

For full-fidelity first-order storage accounting:

- every **Interaction is itself an Event**;
- resolving that Interaction produces a **resulting Event**;
- additional cascading Events are possible but are **not assumed in the baseline**;
- central storage assumption: **one generated Fact per Event**;
- each participating Actor retains an Actor-specific Memory of the Interaction;
- Facts, Events, and Memories are all priced at the same **9.5 KiB vector-bearing record cost** for this calculation.

The 10,000-run 36-settler control produces median values of (the combined median is calculated per run, rather than by summing independently computed medians):

- **2,197 Interactions**;
- **4,394 mandatory Interaction/result Event records**;
- **~4,394 Event records**;
- **~4,394 generated Facts**;
- **~2,380 Actor Memories**;
- **11,167 median total generated vector-bearing records**.

At 9.5 KiB/record:

```
11,167 × 9.5 KiB ≈ 103.59 MiB
```

First-order scaling to all **43 model-driven Cognitive Actors** gives approximately:

- **~2,624 Interactions**;
- **~5,248 mandatory Interaction/result Event records**;

- **~5,248 total Event records**;
- **~5,248 generated Facts**;
- **~2,843 Actor Memories**;
- **~13,339 generated vector-bearing records**;
- **~123.75 MiB runtime growth over eight hours**.

Participant cognition inference remains zero, but Participant Interactions still create persistent state. For each Participant Interaction, use:

- **2 Event records**: Interaction Event + resulting Event;
- **2 generated Facts** under the one-Fact-per-Event central assumption;
- **1 Participant Actor Memory**;
- **~0.5 NPC Memories** on average from downstream Actor involvement.

Thus each Participant Interaction adds approximately **5.5 vector-bearing records** before extra cascading Events.

| Participant activity | Participant Interactions | Added records | Total runtime records | Runtime storage |
| --- | ---: | ---: | ---: | ---: |
| Background only | 0 | 0 | **~13,339** | **~123.75 MiB** |
| **2×** | ~122 | ~671 | **~14,010** | **~129.98 MiB** |
| **4×** | ~244 | ~1,342 | **~14,681** | **~136.20 MiB** |
| **6×** | ~366 | ~2,013 | **~15,352** | **~142.43 MiB** |
| **8×** | ~488 | ~2,684 | **~16,023** | **~148.65 MiB** |

The one-Fact-per-Event and 0.5-NPC-Memory assumptions are explicit sensitivity assumptions, not implementation measurements.

## 6. Vector-Bearing Storage

Use **~9.5 KiB per vector-bearing record** as the conservative physical-storage unit.

Historical GottZ/ctx PostgreSQL + HNSW benchmark:

- 102,520 vector-bearing rows;
- context_blocks ≈ 684 MB;
- HNSW ≈ 260–264 MB;
- combined ≈ 948 MB;
- ≈ 9.5 KiB per record.

Reliquary's representative fully vectorized Memory is approximately **~5 KiB** and may be used as an efficiency comparison, not as the baseline.

### 6.1 Storage range

Before runtime growth:

```
starting records = world Knowledge + 44,000 prior Actor Memories
```

For the central 150,000-world-Knowledge case:

```
150,000 + 44,000 = 194,000 starting records
≈ 1.76 GiB
```

Add the derived **~13,339-record / ~123.75 MiB** 43-Cognitive-Actor background runtime:

| World Knowledge | Post-session records | Post-session storage |
| ---: | ---: | ---: |
| 100,000 | 157,339 | **~1.43 GiB** |
| 150,000 | 207,339 | **~1.88 GiB** |
| 200,000 | 257,339 | **~2.33 GiB** |

At the central 150,000-world-Knowledge case:

| Participant activity | Final records | Final vector storage |
| --- | ---: | ---: |
| Background only | 207,339 | **~1.878 GiB** |
| **2×** | 208,010 | **~1.885 GiB** |
| **4×** | 208,681 | **~1.891 GiB** |
| **6×** | 209,352 | **~1.897 GiB** |
| **8×** | 210,023 | **~1.903 GiB** |

This does **not** yet include Enclave-specific non-vector structures that are not already represented inside the benchmarked record cost:

- Actor-to-Knowledge associations;
- Actor-to-Actor relationships;
- provenance edges;
- Domain/Enclave/Rank/Facet membership and hierarchy;
- Locus relationships;
- additional implementation-specific indexes;
- replication/backups where used.

Those structures must be measured separately in an implementation rather than assigned an invented fixed multiplier.

## 7. Settlement Control Simulation

Implementation:

- `scripts/signals_settlement_sim.py`

Generated dataset/results:

- `data/signals-settlement-sim/actors.csv`
- `data/signals-settlement-sim/schedule.csv`
- `data/signals-settlement-sim/contact_episodes.csv`
- `data/signals-settlement-sim/runs.csv`
- `data/signals-settlement-sim/summary.json`

Method/results:

- `docs/signals-settlement-temporal-contact-simulation-2026-10-07.md`

The simulator models an eight-hour ordinary day for the 36-person settlement at five-minute temporal resolution.

It distinguishes:

- Actor↔Actor social/group Interactions;
- Actor↔world Interactions with tools, materials, objects, systems, terrain, resources, and tasks;
- deterministic/routine world Interactions;
- world Interactions requiring fresh cognition;
- consequential world Events.

A 10,000-run Monte Carlo simulation with seed `20261007` produces:

| Metric | Median | P05 | P95 |
| --- | ---: | ---: | ---: |
| Pair Interactions | 152 | 133 | 173 |
| Group Interactions | 10 | 5 | 16 |
| Social Interactions | 163 | 143 | 183 |
| Actor↔world Interactions | 2,033 | 1,959 | 2,109 |
| **Total Interactions** | **2,197** | **2,120** | **2,275** |
| Social cognitive cycles | 551 | 474 | 631 |
| Actor↔world cognitive cycles | 471 | 429 | 513 |
| **Total cognitive cycles** | **1,022** | **935** | **1,112** |

Per settlement Actor over eight hours:

```
2,197 / 36 ≈ 61.0 Interactions
1,022 / 36 ≈ 28.4 cognitive cycles
```

The simulator is an engineering model. Its world-Interaction rates are synthetic assumptions and are not claimed as empirical human-behaviour measurements.

## 8. Social-Interaction Research Anchors

The social side of the synthetic model is at least order-of-magnitude compatible with empirical daily-interaction/contact literature, while definitions differ substantially across studies.

- Mossong et al. (2008), POLYMOD: **97,904 contacts**, mean **13.4 contacts/person/day** across eight European countries.
- Zhaoyang, Sliwinski & Martire (2018): adults reported approximately **12 social interactions/day** in ecological momentary assessment.
- Reconnect (2026): overall mean **9.1 daily contacts**; adults averaged **7.8**, and contact counts were explicitly overdispersed.

These data should not be used to equate an epidemiological "contact" with an Enclave Interaction. They support the general scale and heterogeneity of ordinary social contact, not the Actor↔world workload.

Sources are recorded in the evidence ledger and source list below.

## 9. 43-Cognitive-Actor Background Extrapolation

The control simulation directly models only the 36 settlers.

For a simple first-order *Signals* background estimate, scale the control workload by:

```
43 / 36 ≈ 1.19444
```

This treats the five Romulans and two remote Starfleet Actors as having the same average activity density as settlers. That is intentionally simple: the Romulans may be denser, while the remote Starfleet Actors may be quieter.

Rounded background estimate:

| Quantity | 43 Cognitive Actors |
| --- | ---: |
| Social Interactions | ~195 |
| Actor↔world Interactions | ~2,428 |
| **Total Interactions** | **~2,624** |
| Social cognition calls | ~658 |
| Actor↔world cognition calls | ~563 |
| **Total model-driven cognition calls** | **~1,221** |

Participant cognition calls are not included because they are always zero.

## 10. Responsibility-Specific Token Profiles

The earlier one-size-fits-all 4,000-input/250-output call is retired.

Use:

### Social / dialogue / complex cognition

- **4,000 input tokens**
- **250 output tokens**
- **4,250 total tokens**

### Routine Actor↔world cognition

- **1,500 input tokens**
- **80 output tokens**
- **1,580 total tokens**

The world-facing profile is smaller because most such decisions require a narrow local context rather than a broad conversational/social context.

These are modelling assumptions, not measured Enclave prompt distributions.

### 10.1 43-Actor background token volume

Using 658 social calls and 563 Actor↔world calls:

```
social input  = 658 × 4,000 = 2,632,000
social output = 658 ×   250 =   164,500

world input   = 563 × 1,500 =   844,500
world output  = 563 ×    80 =    45,040

total input   = 3,476,500
total output  =   209,540
total tokens  = 3,686,040 ≈ 3.69M
```

## 11. Participant Activity Sensitivity

Use **one Participant controlling one Participant Actor**.

The ordinary-Actor interaction anchor is approximately **61 Interactions/eight hours**.

Model four explicit Participant activity levels:

| Participant activity | Participant Interactions |
| --- | ---: |
| 2× ordinary Actor | ~122 |
| 4× ordinary Actor | ~244 |
| 6× ordinary Actor | ~366 |
| 8× ordinary Actor | ~488 |

Participant cognition inference remains:

```
0 calls
```

### 11.1 Downstream NPC fan-out assumption

For sensitivity analysis only, assume:

- **25%** of Participant Interactions require immediate model-driven Actor response/reconsideration;
- each response-bearing Interaction creates an average of **2 NPC cognition calls**.

Thus:

```
additional model-driven calls ≈ Participant Interactions × 0.5
```

This is explicitly arbitrary-but-transparent sensitivity modelling, not an empirical player-behaviour result.

### 11.2 Combined scenarios

Using the ~2,624 Interaction / ~1,221-call 43-Actor background:

| Participant activity | Participant Interactions | Added NPC calls | Total Interactions | Total model calls |
| --- | ---: | ---: | ---: | ---: |
| **2×** | ~122 | ~61 | **~2,746** | **~1,282** |
| **4×** | ~244 | ~122 | **~2,868** | **~1,343** |
| **6×** | ~366 | ~183 | **~2,990** | **~1,404** |
| **8×** | ~488 | ~244 | **~3,112** | **~1,465** |

Treat the added NPC calls conservatively as social/complex 4,000/250-token calls:

| Participant activity | Input tokens | Output tokens | Total model tokens |
| --- | ---: | ---: | ---: |
| Background only | 3.477M | 0.210M | **3.686M** |
| **2×** | 3.721M | 0.225M | **3.945M** |
| **4×** | 3.965M | 0.240M | **4.205M** |
| **6×** | 4.209M | 0.255M | **4.464M** |
| **8×** | 4.453M | 0.271M | **4.723M** |

## 12. Hosted API Cost Sensitivity

Verified 2026-10-08 Standard short-context prices per 1M tokens:

| Model | Input | Output |
| --- | ---: | ---: |
| GPT-6 Astra | $10.00 | $50.00 |
| GPT-6 Sol | $2.00 | $10.00 |
| GPT-6 Luna | $0.10 | $0.50 |

Illustrative 70% Luna / 25% Sol / 5% Astra weighted rates:

```
input  = $1.07 / 1M
output = $5.35 / 1M
```

| Scenario | All Astra | All Sol | All Luna | 70/25/5 routed |
| --- | ---: | ---: | ---: | ---: |
| Background | $45.24 | $9.05 | $0.45 | $4.84 |
| **2× Participant** | $48.44 | $9.69 | $0.48 | $5.18 |
| **4× Participant** | $51.65 | $10.33 | $0.52 | $5.53 |
| **6× Participant** | $54.85 | $10.97 | $0.55 | $5.87 |
| **8× Participant** | $58.05 | $11.61 | $0.58 | $6.21 |

These are price calculations only. They do not establish that the cheaper models provide equivalent narrative quality.

### 12.1 GPU Rental Alternative (2026-10-08 USD Reference)

A directly rented GPU running an open-weight inference stack is an alternative to token-billed API service. The following are advertised GPU charges, not verified serving benchmarks; eight-hour totals assume a single GPU allocated or active for eight hours.

| Provider / mode | GPU | VRAM | USD/hour | 8 GPU-hours |
| --- | --- | ---: | ---: | ---: |
| RunPod Pod | A40 | 48 GB | $0.49 | $3.92 |
| RunPod Pod | A100 PCIe | 80 GB | $1.59 | $12.72 |
| RunPod Pod | RTX Pro 6000 | 96 GB | $2.09 | $16.72 |
| Lambda single-GPU VM | A6000 | 48 GB | $1.09 | $8.72 |
| Lambda single-GPU VM | H100 PCIe | 80 GB | $3.29 | $26.32 |
| Modal metered GPU | H100 SXM | 80 GB | ~$3.95 | ~$31.59 |

Sources checked 2026-10-08:

- RunPod Pods: https://www.runpod.io/pricing
- Lambda Cloud instances: https://lambda.ai/pricing
- Modal (H100 GPU $0.001097/second, before CPU/RAM): https://modal.com/pricing
- Vast.ai marketplace (dynamic host-defined rates, no stable quotation): https://vast.ai/pricing and https://github.com/vast-ai/docs/blob/main/guides/pricing.mdx

These are **single-GPU rental/active-hour charges**, not cost-per-token equivalents: model quantization, KV-cache footprint, batching, parallel requests, latency, multiple GPUs, boot and idle time, CPU/RAM, storage, bandwidth, software operations, and provider availability change feasibility and end-to-end cost. Compare hardware-hosted open-weight quality and reliability separately from the hosted Astra/Sol/Luna price table.

## 13. Local Inference Capacity Comparison

Published DGX Spark batch-size-one measurements at 2,048 input / 128 output include:

| Model | Prompt tok/s | Generation tok/s |
| --- | ---: | ---: |
| GPT-OSS-20B | 3,670.42 | 82.74 |
| GPT-OSS-120B | 1,725.47 | 55.37 |

Simple extrapolation to the two Enclave call profiles:

### GPT-OSS-20B

- social 4,000/250 call ≈ **4.11 s**
- world 1,500/80 call ≈ **1.38 s**
- 43-Actor background if executed serially ≈ **58.0 min**
- 8× Participant scenario if added calls also execute serially ≈ **74.7 min**

### GPT-OSS-120B

- social 4,000/250 call ≈ **6.83 s**
- world 1,500/80 call ≈ **2.31 s**
- 43-Actor background if executed serially ≈ **96.7 min**
- 8× Participant scenario ≈ **124.4 min**

These are arithmetic extrapolations from a different benchmark sequence shape and do not establish quality, concurrency, or latency under an actual Enclave serving stack.

The more important runtime risk remains burst concurrency and causal fan-out rather than eight-hour average throughput.

## 14. Dense Causal Burst

Retain the existing stress case:

- 12 Cognitive Actors reacting inside one causal window;
- one social/complex 4,000-input/250-output call each;
- target completion window: 10 seconds.

Arithmetic demand:

```
input  = 12 × 4,000 = 48,000 tokens
output = 12 ×   250 =  3,000 tokens

10-second window:
4,800 input tok/s
300 output tok/s
```

Do not compare the summed 5,100 token/s directly to a single benchmark throughput number without separating prompt processing, generation, batching, and concurrency.

## 15. What Remains Provisional

The following remain modelling assumptions rather than empirical Enclave measurements:

- 150,000 central world-Knowledge records;
- 1,000 prior Memories per living Actor;
- 2 Event records per Interaction: Interaction Event + resulting Event;
- 1 generated Fact per Event;
- 1 Memory per participating Actor per Interaction;
- Actor↔world Interaction rates;
- world-cognition probabilities;
- 4,000/250 and 1,500/80 token profiles;
- 43/36 extrapolation for the seven non-settlement Cognitive Actors;
- Participant 2×/4×/6×/8× activity levels;
- Participant causal fan-out factor of 0.5 NPC calls/Interaction;
- illustrative model routing.

The settlement Monte Carlo output is reproducible given the code and seed, but it remains the output of a synthetic model.

## 16. Research and Evidence Sources

### Published adventure

Modiphius Entertainment, *Star Trek Adventures: Quickstart Guide — Signals*.
https://modiphius.net/collections/star-trek-adventures/products/star-trek-adventures-quickstart-guide

### Social contact / interaction

Mossong, J. et al. (2008), *Social Contacts and Mixing Patterns Relevant to the Spread of Infectious Diseases*, PLOS Medicine.
https://journals.plos.org/plosmedicine/article?id=10.1371/journal.pmed.0050074

Zhaoyang, R., Sliwinski, M. J., & Martire, L. M. (2018), *Age Differences in Adults' Daily Social Interactions: An Ecological Momentary Assessment Study*, Psychology and Aging.
https://pmc.ncbi.nlm.nih.gov/articles/PMC6113687/

Reconnect survey (2026), *Social contact patterns in the United Kingdom following the COVID-19 pandemic*, PLOS Medicine.
https://journals.plos.org/plosmedicine/article?id=10.1371/journal.pmed.1005038

### Model pricing

OpenAI API Pricing, verified 2026-10-08.
https://platform.openai.com/pricing

### Local inference

NVIDIA, *How NVIDIA DGX Spark's Performance Enables Intensive AI Tasks*.
https://developer.nvidia.com/blog/how-nvidia-dgx-sparks-performance-enables-intensive-ai-tasks

### Cloud accelerator cost

AWS, *Amazon EC2 Capacity Blocks for ML Pricing*.
https://aws.amazon.com/ec2/capacityblocks/pricing/

### Vector representation

pgvector documentation.
https://github.com/pgvector/pgvector

### Storage benchmark

Historical **GottZ/ctx** PostgreSQL + HNSW project benchmark retained in:
- `docs/signals-computational-evidence-and-assumptions-2026-10-07.md`

### Additional inference benchmark context

MLCommons MLPerf Inference results and NVIDIA/SemiAnalysis InferenceMAX references are retained in the evidence ledger.

## 17. Canonical Support Files

Current Section 15 quantitative work should be read in this order:

1. `docs/signals-section15-consolidated-computational-model-2026-10-08.md` — authoritative current calculations.
2. `docs/signals-settlement-temporal-contact-simulation-2026-10-07.md` — settlement simulation method/results.
3. `scripts/signals_settlement_sim.py` — reproducible simulator.
4. `data/signals-settlement-sim/` — generated dataset and Monte Carlo results.
5. `docs/signals-participant-interaction-sensitivity-2026-10-08.md` — Participant sensitivity derivation.
6. `docs/signals-computational-evidence-and-assumptions-2026-10-07.md` — external evidence ledger and historical derivations.

## 18. Section 16.6 — Implementation-Level and Hybrid Cost Comparison (2026-10-08)

These calculations **extend the Section 15 reference**; they do not replace it. All figures cover **eight simulated hours**, with **one Participant Actor at the 4× activity scenario** (244 Participant Interactions). All three uniform levels apply to the *same 43 NPC population*, and the hybrid applies the specific §16.5 cast allocation. They are conditional engineering projections, not implementation benchmarks.

### 18.1 Shared assumptions and scope

- Reuse §15's 43-Actor background of **2,624 Interactions**, **1,221 model calls**, **3,686,040 model tokens**, **13,339 generated records** and **44,000 pre-existing Memories** for the **full Level 3 baseline**; its 4× Participant extension adds **122 model calls**, **518,500 tokens**, and **1,342 generated records**, exactly as previously reported.
- **New dialogue assumption:** 25% of each Participant's 244 Interactions initiate dialogue, with **two model responses per dialogue**, each using §15's social-response profile (4,000 input, 250 output tokens). All levels therefore incur the **same 122 Participant-initiated dialogue model calls** before any autonomous cognition. A model call here is an assumed single response, not necessarily a completed conversation.
- **Uniform Level 1:** no personal Actor Memories and no autonomous cognition; routine state persists conventionally. Deterministic updates to available Knowledge and provenance are possible. This model counts no *new vector-bearing Enclave Event or Memory rows* from ordinary gameplay; that is **not zero game-state storage**.
- **Uniform Level 2:** the same dialogue-call workload plus **one newly stored NPC Memory per dialogue** (61 in this 4× case); opinion/relationship updates are costed as deterministic. All 43 NPCs are assigned §15's deliberately heavy **1,000 pre-existing Memories each**, even though Level 2 does not require any particular count.
- **Uniform Level 3:** all 43 NPCs are fully Cognitive, plus one human-controlled Participant Actor; full §15 Event, Fact and Memory accounting applies. The Participant's own historical Memories are represented, but its cognition is never model-billed.
- **Authored-world comparison:** hold §15's central **150,000 vector-bearing Knowledge records** constant for *Signals* across all four configurations, so the totals isolate changes in cognition and Memory. This conservative shared dataset is **not** a requirement for dialogue-only games or a claim that Level 1 needs the complete Enclave ontology.
- The same illustrative 2026-10-08 model routing ($1.07/million input and $5.35/million output) prices each row. There is no asserted quality parity or GPU equivalence.

### 18.2 *Signals* uniform levels and hybrid

| Implementation | Model calls | Model tokens | Routed inference cost (USD) | New vector-bearing rows | Runtime vector storage | Final corpus, incl. shared Knowledge and prior Memory |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Level 1 — Reactive Dialogue | 122 | 0.518M | $0.69 | 0 | 0.00 MiB | 1.359 GiB |
| Level 2 — Persistent Characters | 122 | 0.518M | $0.69 | 61 | 0.57 MiB | 1.749 GiB |
| Level 3 — full narrative architecture | 1,343 | 4.205M | $5.53 | 14,681 | 136.20 MiB | 1.891 GiB |
| Hybrid Level 3 — approved §16.5 roster | 193 | 0.733M | $0.97 | 2,100 | 19.48 MiB | 1.441 GiB |

**Interpretation:** the low-level applications remain conversational rather than autonomously cognitive; their calls are driven by Participant activity, not by the settlement's ordinary work. The final-corpus column holds world Knowledge fixed, while actor-specific starting histories differ: 0 personal Memories in Level 1, 43,000 in Level 2, 44,000 (including the Participant Actor) in full Level 3, and 7,000 for the hybrid's four eligible Level 3 plus three Level 2 NPCs. The physical 9.5 KiB/record benchmark prices the vector-bearing corpus only; independent graph, provenance, interface, and engine costs are excluded.

### 18.3 Explicit §16.5 *Signals* hybrid model

- **Roster:** 34 ordinary settlers (Level 1); 3 ordinary Romulans (Level 2); 4 potentially full Cognitive Actors (Ero Drallen, Romulan captain, wounded Romulan and one conditional settlement representative); one remote Starfleet captain available only upon conditional activation; one deterministic distress-source Actor. There are **43 NPCs** in all, plus the human Participant Actor.
- **Eight-hour activation schedule for this illustrative calculation:** Ero and the Romulan captain at 100% reference background cognitive activity; wounded Romulan at 25%; secondary representative at 25%; remote captain at 0% unless activated. These are **2.5 full-Actor-equivalent duty periods**, **not measured character behaviour**, producing approximately **70.99 autonomous model calls** before Participant dialogue.
- **Ordinary conventional world activity remains:** all 43 NPCs collectively perform the same ~2,624 synthetic background Interactions. The active-equivalent narrative cast accounts for **152.56** Interactions in full Enclave event accounting; provisionally **10%** of the other **2,471.44** routine Interactions create consequential Enclave Events. This yields about **400** Enclave-recorded background Interactions (two Event plus two Fact records each), plus approximately **165** background full-Actor Memories.
- **Participant activity:** of 244 Interactions, assume **25%** are consequential and receive full 2-Event/2-Fact recording. Persist a Participant Memory for each consequential Interaction; provisionally **50%** of the 61 dialogue Interactions concern Level 2/3 NPCs and create a separate NPC Memory. All Participant-triggered dialogue still costs **122 model calls**, whatever the NPC's fidelity. These fractions are sensitivity choices, not empirically validated rates.
- **Generated-record derivation:** **1,764.10 background rows + 335.50 Participant-associated rows = 2,099.60 rows**, rounded to ~2,100. Event relevance is *categorical*: a causally relevant Event must be retained even if the provisional 10%/25% assumptions underestimate its frequency. Unrecorded conventional actions remain resolved by the ordinary game engine.
- **Result at matched Participant activity:** 193 versus 1,343 model calls (**85.6% fewer**); 0.733M versus 4.205M tokens (**82.6% fewer**); about 2,100 versus 14,681 generated vector records (**85.7% fewer** under the event-filter assumptions).
- Fidelity may change during the narrative. A wounded Romulan who rejoins his comrades can cease autonomous cognition while remaining in authoritative state. If the Starfleet captain or another representative becomes consequential, the active-equivalent and model-call budget must rise accordingly.

### 18.4 Limits and reproducibility

These are *sensitivity calculations*, not recorded dialogue frequencies, causal Event probabilities, inference latencies, an executable Enclave benchmark, or a prediction of NPC behaviour. Both lower-level dialogue engagement and hybrid Event capture must be measured in an actual game. Memory extraction, retrieval, vector indexing, context assembly, graph traversal, synchronization, batching, model quality, burst concurrency, and external game-engine storage are not priced as separate operations.

Reproduce the exact figures using **scripts/signals_section16_fidelity_calculations.py**, which emits **data/signals-section16-fidelity-results.json**. The existing **docs/manhattan-test-scaling-2026-10-08.md** now contains the parallel urban comparison. This leaves distributed scaling and partitioning analysis for the planned Appendix/Addendum rather than repeating §15.
