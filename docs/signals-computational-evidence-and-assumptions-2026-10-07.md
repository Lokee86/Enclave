# Signals Computational Evidence and Assumptions Ledger

**Date:** 2026-10-07
**Purpose:** Source and calculation ledger for Section 15, *Computational Architecture and Scale*.
**Reference workload:** `docs/signals-high-fidelity-computational-workload-2026-10-07.md`
**Status:** Research/evidence ledger. External measurements, Enclave modelling assumptions, and derived calculations are deliberately separated. **Current authoritative Section 15 arithmetic is in `docs/signals-section15-consolidated-computational-model-2026-10-08.md`. Derived calculations later in this ledger that still use the retired 1,100-call / 10,000-record / six-Participant-Actor model are preserved as historical work and must not be cited as current.**

---

## 1. Why This Document Exists

Section 15 should not present a mixture of benchmark measurements and Enclave-specific estimates as though they have the same evidentiary status.

This ledger therefore separates all quantitative material into three classes:

1. **Externally sourced facts and measurements** — published pricing, hardware specifications, storage formulas, and benchmark results.
2. **Enclave modelling assumptions** — explicit choices made to turn the *Signals* adventure into a computational workload.
3. **Derived calculations** — arithmetic that combines the first two categories.

Unless a quantity is explicitly identified as externally measured, it should be presented in the paper as an estimate, workload assumption, extrapolation, or derived result rather than an empirical Enclave benchmark.

---

## 2. Reference Workload — Enclave Assumptions

The following values come from the internal high-fidelity *Signals* workload. They are not externally benchmarked quantities.

| Quantity | Central assumption |
| --- | ---: |
| Human Participants | 1 |
| Participant-controlled Actors | **1** |
| Model-driven Cognitive Actors | **43** |
| Living in-world Actors in simplified scope | **44** |
| Assumed in-world mission duration | 8 h |
| Semantic/world Knowledge records | **100,000–200,000; 150,000 central** |
| Pre-existing Actor Memories | **44,000** |
| Settlement-control cognition calls, 36 Actors | **1,022 median** |
| 43-Actor background model calls | **~1,221** |
| Participant cognition calls | **0** |
| Participant-sensitivity total calls | **~1,282–1,465** |
| 43-Actor background model tokens | **~3.686M** |
| Participant-sensitivity model tokens | **~3.945–4.723M** |
| Runtime Events, 43-Actor background | **~5,248** (Interaction Event + resulting Event) |
| Runtime Facts, 43-Actor background | **~5,248** (1 Fact/Event assumption) |
| Runtime Actor Memories, 43-Actor background | **~2,843** |
| Deterministic-operation count | **to be regenerated from revised Interaction model** |

The adventure itself is an official Modiphius *Star Trek Adventures* Quickstart containing the self-contained *Signals* adventure and six pre-generated characters. **That source-party size is not the Section 15 computational reference:** the quantitative model intentionally uses **one Participant controlling one Participant Actor**. The transformation from the published adventure into the Enclave workload is our own modelling work.

**Primary adventure source:**
Modiphius Entertainment, *Star Trek Adventures: Quickstart Guide PDF - FREE*.
https://modiphius.net/collections/star-trek-adventures/products/star-trek-adventures-quickstart-guide
Accessed 2026-10-07.

---

## 3. Externally Sourced Computational Evidence

### 3.1 Current hosted-model pricing

OpenAI's current API pricing page lists the following **Standard, short-context** token rates:

| Model | Input / 1M tokens | Cached input / 1M | Output / 1M |
| --- | ---: | ---: | ---: |
| GPT-6 Astra | $10.00 | $1.00 | $50.00 |
| GPT-6 Sol | $2.00 | $0.20 | $10.00 |
| GPT-6 Luna | $0.10 | $0.01 | $0.50 |

These are current prices, not assumptions.

**Primary source:**
OpenAI, *API Pricing*.
https://developers.openai.com/api/docs/pricing
Verified 2026-10-08.

**Use in Section 15:** hosted-token cost calculations.

**Important boundary:** API price does not establish the quality required for a particular Enclave responsibility. Any routing scheme among Astra, Sol, and Luna remains an Enclave design assumption until evaluated.

---

### 3.2 DGX Spark local-inference throughput

NVIDIA publishes batch-size-one inference results for DGX Spark at an input sequence length of 2,048 tokens and output sequence length of 128 tokens:

| Model | Precision/backend | Prompt processing | Token generation |
| --- | --- | ---: | ---: |
| Qwen3 14B | NVFP4 / TRT-LLM | 5,928.95 tok/s | 22.71 tok/s |
| GPT-OSS-20B | MXFP4 / llama.cpp | 3,670.42 tok/s | 82.74 tok/s |
| GPT-OSS-120B | MXFP4 / llama.cpp | 1,725.47 tok/s | 55.37 tok/s |
| Llama 3.1 8B | NVFP4 / TRT-LLM | 10,256.9 tok/s | 38.65 tok/s |

**Primary source:**
NVIDIA Technical Blog, *How NVIDIA DGX Spark's Performance Enables Intensive AI Tasks*.
https://developer.nvidia.com/blog/how-nvidia-dgx-sparks-performance-enables-intensive-ai-tasks
Accessed 2026-10-07.

**Use in Section 15:** local throughput and latency order-of-magnitude calculations.

**Benchmark boundary:** these are measurements at 2,048 input / 128 output tokens and batch size 1. Calculations for the Enclave 4,000 / 250 reference call are extrapolations and must be labelled as such.

---

### 3.3 DGX Spark hardware envelope

NVIDIA's current DGX Spark specifications include:

- 128 GB LPDDR5X coherent unified memory in the standard NVIDIA configuration;
- 273 GB/s memory bandwidth;
- up to 4 TB NVMe storage;
- 240 W external power supply;
- 140 W GB10 SoC TDP;
- support for inference on models up to 200 billion parameters;
- up to 1 PFLOP FP4 theoretical AI performance with sparsity.

**Primary sources:**
NVIDIA, *DGX Spark*.
https://www.nvidia.com/en-us/products/workstations/dgx-spark/

NVIDIA, *DGX Spark User Guide — Hardware Overview*.
https://docs.nvidia.com/dgx/dgx-spark/hardware.html
Accessed 2026-10-07.

NVIDIA announced in February 2026 that the Founders Edition MSRP increased from **$3,999 to $4,699** because of memory-supply constraints.

**Source:**
NVIDIA Developer Forums, *2/23/2026 Price Change Announcement*.
https://forums.developer.nvidia.com/t/2-23-2026-price-change-announcement/361713
Accessed 2026-10-07.

**Use in Section 15:** one plausible local-development/deployment hardware example.

**Boundary:** model-fit capability and throughput do not demonstrate narrative quality.

---

### 3.4 Datacenter inference throughput

NVIDIA reports a SemiAnalysis InferenceMAX v1 result in which a Blackwell B200 reaches approximately **10,000 aggregate tokens/s per GPU at 50 tokens/s/user** on the Llama 3.3 70B 1K-input/1K-output workload.

NVIDIA also reports substantially higher throughput for GPT-OSS-120B after later speculative-decoding software improvements, illustrating that serving software materially changes achievable throughput.

**Primary / benchmark-report source:**
NVIDIA Technical Blog, *NVIDIA Blackwell Leads on SemiAnalysis InferenceMAX v1 Benchmarks*, 2025-10-13.
https://developer.nvidia.com/blog/nvidia-blackwell-leads-on-new-semianalysis-inferencemax-benchmarks/
Accessed 2026-10-07.

**Independent benchmark context:**
MLCommons, *MLPerf Inference v6.1 Results*, 2026-09-16.
https://mlcommons.org/2026/09/mlperf-inference-v6-1-results/

MLCommons, *Where the Industry Is Investing: A Look at MLPerf Inference v6.1*, 2026-09-17.
https://mlcommons.org/2026/09/chairs-mlperf-inference-v6-1/
Accessed 2026-10-07.

**Use in Section 15:** establish that contemporary datacenter inference can sustain aggregate throughput in the range needed by dense multi-Actor bursts.

**Boundary:** the B200 result uses a different model, precision, sequence shape, serving stack, and batching regime than the Enclave workload. It is a capacity comparison, not a direct Enclave benchmark.

---

### 3.5 Cloud accelerator pricing

AWS Capacity Blocks currently list:

| Instance | Accelerators | Effective hourly rate |
| --- | ---: | ---: |
| p5.4xlarge | 1 × H100 | $5.191/h in listed US regions |
| p5.48xlarge | 8 × H100 | $41.528/h in listed US regions |
| p6-b200.48xlarge | 8 × B200 | $98.84/h in listed US regions |

Capacity Block pricing is reservation pricing and varies by offering/availability.

**Primary sources:**
AWS, *Amazon EC2 Capacity Blocks for ML Pricing*.
https://aws.amazon.com/ec2/capacityblocks/pricing/

AWS Documentation, *Capacity Blocks pricing and billing*.
https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/capacity-blocks-pricing-billing.html
Accessed 2026-10-07.

**Use in Section 15:** dedicated-cloud infrastructure comparison.

**Boundary:** renting a dedicated accelerator for the entire eight-hour adventure is not necessarily economical; the calculation is an infrastructure-envelope comparison, not a recommended deployment.

---

### 3.6 Vector-storage cost

The pgvector project specifies:

- `vector`: **4 × dimensions + 8 bytes** per vector;
- `halfvec`: **2 × dimensions + 8 bytes** per vector;
- HNSW provides approximate nearest-neighbour search and uses more memory than IVFFlat;
- HNSW's default maximum connections per layer `m` is 16;
- vector indexes need not fit entirely in memory, although performance generally improves when they do.

**Primary technical source:**
pgvector project documentation.
https://github.com/pgvector/pgvector
Accessed 2026-10-07.

**Use in Section 15:** reproducible embedding-payload calculations.

**Boundary:** HNSW index overhead depends on dataset, parameters, implementation and database layout. Do not invent one universal percentage for it.

### 3.7 Measured memory-storage comparison: Reliquary and historical CTX PostgreSQL

Use **GottZ/ctx** as the CTX source of record. The historical PostgreSQL `context_blocks` benchmark belongs to that repository's storage lineage; do not substitute measurements from `continuity-memory` or any separate CTX/Continuity repository.

For a representative Memory with approximately a 20-byte title and 500-byte content:

| Representation | Approximate size per Memory |
| --- | ---: |
| Reliquary core Memory, without vector | **~0.9–1.0 KiB** |
| Reliquary + 1024d `f32` vector | **~5.0 KiB** |
| Historical CTX PostgreSQL `context_blocks`, table/TOAST/etc. | **~6.8 KiB** |
| Historical CTX PostgreSQL + HNSW | **~9.5 KiB** |

The historical CTX benchmark contained **102,520 vector-bearing rows**:

- `context_blocks`: **~684 MB** total;
  - heap: ~57 MB;
  - TOAST: ~541 MB;
  - remaining relation/index overhead: ~86 MB;
- HNSW: **~260–264 MB**;
- combined: **~948 MB**.

Thus:

```
~948 MB / 102,520 vector-bearing Memories ≈ ~9.5 KiB/Memory
```

The old PostgreSQL representation carried substantially more than the semantic body itself: the 1024d `f32` vector, SQL tuple/storage overhead, arrays, JSONB, hashes, lifecycle/status fields, UUID relationships, timestamps, generated full-text vectors, TOAST framing, and numerous indexes. HNSW added roughly another **~2.6 KiB per Memory**.

Reliquary's approximately **~5 KiB fully vectorized Memory** already includes the dominant 4,096-byte 1024d `f32` embedding. Its non-vector core is only approximately **~0.9–1.0 KiB** for the representative record.

The useful architectural comparison is therefore:

- **purpose-built compact representation:** ~5 KiB per representative fully vectorized Reliquary Memory;
- **general PostgreSQL/vector-store representation:** ~9.5 KiB per representative fully indexed historical CTX Memory.

Reliquary is therefore roughly **half the measured physical footprint** of the historical CTX PostgreSQL representation for this workload, while retaining the same 1024d `f32` vector.

**Evidence status:** these are project benchmark/format measurements. CTX evidence for this paper should be sourced from **GottZ/ctx**. The benchmark provenance should be attached to the final paper citation record before publication.

### 3.8 Empirical social-contact / interaction anchors

These sources are useful only as order-of-magnitude anchors for the **social** side of the settlement model. Their definitions of contact or social interaction are not identical to Enclave's Interaction primitive.

**Mossong et al. (2008), POLYMOD**
- 97,904 recorded contacts;
- mean **13.4 contacts per participant per day** across eight European countries.
- Source: https://journals.plos.org/plosmedicine/article?id=10.1371/journal.pmed.0050074
- Verified 2026-10-08.

**Zhaoyang, Sliwinski & Martire (2018)**
- ecological momentary assessment across adulthood;
- participants reported an average of **2.4 social interactions per assessment**, approximately **12 social interactions per day**.
- Source: https://pmc.ncbi.nlm.nih.gov/articles/PMC6113687/
- Verified 2026-10-08.

**Reconnect (2026)**
- mean **9.1 daily contacts** overall;
- adults averaged **7.8 daily contacts**;
- contact counts were overdispersed, reinforcing substantial person-to-person heterogeneity.
- Source: https://journals.plos.org/plosmedicine/article?id=10.1371/journal.pmed.1005038
- Verified 2026-10-08.

**Boundary:** These studies do not validate the simulator's Actor↔world Interaction rates. Those remain explicit synthetic engineering assumptions.

---

### 3.9 Cloud GPU Rental — Published Rate Snapshots (2026-10-08)

This is the research basis for the open-weight GPU hosting comparison in §15.8. All listed prices are **USD per GPU-hour**, not equivalent model-output prices or guarantees of real-time serving throughput.

- **RunPod Pod rentals:** A40 48 GB **$0.49/h**; A100 PCIe 80 GB **$1.59/h**; RTX Pro 6000 96 GB **$2.09/h**. Eight-hour single-GPU totals: **$3.92**, **$12.72**, **$16.72**. Official page: https://www.runpod.io/pricing (page dated 2026-09-27; checked 2026-10-08).
- **Lambda on-demand single-GPU VMs:** A6000 48 GB **$1.09/h**; H100 PCIe 80 GB **$3.29/h**. Eight-hour single-GPU totals: **$8.72** and **$26.32**. Official page: https://lambda.ai/pricing (checked 2026-10-08).
- **Modal metered GPU capacity:** H100 SXM **$0.001097/second**, equivalent to **$3.9492/active GPU-hour** or **$31.5936 per eight active GPU-hours**. CPU, RAM, volumes, and other charges may be separate. Official page: https://modal.com/pricing (checked 2026-10-08).
- **Vast.ai GPU marketplace:** hosts determine prices, which change with GPU type, location, availability, and host reliability. On-demand, interruptible, reserved, and serverless pricing models are available. No static price is asserted. https://vast.ai/pricing ; https://github.com/vast-ai/docs/blob/main/guides/pricing.mdx (checked 2026-10-08).

Comparability constraints: a continuously allocated eight-hour GPU is billed for capacity whether busy or idle; metered compute can reduce active-time charges but may entail cold starts. One physical GPU must still be verified to fit the selected model/quantization/KV cache and meet concurrency and causal-burst latency targets. Multi-GPU requirements multiply the rental cost. Storage, CPUs, network traffic, management, security, and operations are excluded from these simple GPU-only totals. Hosted API Astra/Sol/Luna and rented open-weight models are not presumed to deliver equivalent quality.

## 4. Explicit Enclave Modelling Assumptions

These values are **not externally measured facts**.

### 4.1 Responsibility-specific probabilistic calls

The earlier assumption that every cognitive cycle uses the same **4,000 input / 250 output** token shape is retired as too coarse.

Use separate first-order workload units:

- **Social/dialogue/complex Actor cognition:** approximately **4,000 input / 250 output tokens**;
- **Routine Actor↔world cognition:** approximately **1,500 input / 80 output tokens**.

Actor↔world calls are expected to be smaller because they normally require a narrow local context: the current task, relevant object/system state, immediate goals/constraints, and a short interpretation or action decision rather than a large conversational/social context.

These remain explicit modelling assumptions rather than implementation measurements. More complex world-facing situations may use the larger profile, while trivial deterministic world Interactions require no probabilistic call at all.

Both profiles include retrieved Actor-accessible state in the input-token budget and exclude hidden chain-of-thought or private reasoning from persistent narrative state.

### 4.2 Routed high-fidelity API configuration

For an illustrative architecturally routed configuration:

- **70% Luna** — extraction, lightweight interpretation, routine low-risk decisions;
- **25% Sol** — substantive Actor cognition and dialogue;
- **5% Astra** — unusually difficult reasoning or high-stakes synthesis.

This distribution is an **illustrative routing policy**, not a measured optimum.

### 4.3 Dense-scene burst

Use a stress case of:

- **12 Cognitive Actors reacting within the same causal window**;
- one 4,000-input / 250-output call each;
- target completion window: **10 seconds**.

This is an Enclave responsiveness target chosen to expose causal fan-out. It is not derived from the adventure text or from a benchmark.

### 4.4 Storage-model correction

The earlier 1,024–1,280-byte generic record assumptions are **withdrawn as a high-fidelity physical-storage model**.

They mixed semantic payload size with physical database cost and materially understated:

- vector storage;
- ANN index storage;
- PostgreSQL heap/TOAST overhead;
- secondary retrieval indexes;
- graph/provenance structures;
- Actor-specific history.

The earlier ~1,300 and ~10,000 starting-world estimates are retired as too sparse for the full-fidelity reference. The current workload uses **100,000–200,000 semantic/world Knowledge records, with 150,000 central**, separately from **44,000 pre-existing Actor Memories**.

For the main §15 physical-storage calculations, use **~9.5 KiB per vector-bearing Memory** as the conservative working unit. This is the measured historical CTX PostgreSQL + HNSW result across 102,520 rows.

Reliquary's approximately **~5.0 KiB** fully vectorized Memory remains useful as an efficiency comparison showing what a purpose-built representation can save, but it is not the baseline used for Enclave scaling calculations.

The 9.5 KiB figure is still an approximation tied to that measured representation; individual narrative records vary in text, provenance, links, temporal metadata, graph participation, and indexing requirements. CTX evidence for this paper comes from **GottZ/ctx**.

### 4.5 Pre-existing Actor-history assumption

For the high-fidelity *Signals* reference, assume **1,000 pre-existing persistent Memories per living Actor**.

This is an explicit engineering assumption rather than a claim about human memory capacity. Its purpose is to provide a substantial, narratively useful personal-history corpus that is simple to scale.

The simplified computational reference contains **44 living in-world Actors**:

- 43 model-driven Cognitive Actors;
- 1 Participant-controlled Actor whose cognition is external but whose history still persists in Enclave.

Therefore:

```
44 Actors × 1,000 prior Memories = 44,000 pre-existing Memories
```

Use **150,000 semantic/world Knowledge records** as the central world-state case.

Runtime persistence is derived from the Interaction workload:

- every Interaction is itself one Event;
- every Interaction produces one resulting Event;
- central assumption: one generated Fact per Event;
- one Memory per participating Actor per Interaction.

For the first-order 43-Cognitive-Actor background:

- ~2,624 Interactions;
- ~5,248 mandatory Interaction/result Events;
- ~5,248 total Events;
- ~5,248 generated Facts;
- ~2,843 runtime Actor Memories;
- ~13,339 runtime-generated vector-bearing records.

Central post-session vector-bearing corpus:

```
150,000 + 44,000 + 13,339 = 207,339 records
```

At the conservative working value of **9.5 KiB per vector-bearing record**:

```
207,339 × 9.5 KiB ≈ 1,923.9 MiB ≈ 1.88 GiB
```

World-Knowledge sensitivity after the ordinary eight-hour background run:

- 100,000 → 157,339 total records → ~1.43 GiB;
- 150,000 → 207,339 → ~1.88 GiB;
- 200,000 → 257,339 → ~2.33 GiB.

The eight-hour runtime-generated contribution alone is:

```
13,339 × 9.5 KiB ≈ 123.75 MiB
```

This is the vector-bearing narrative layer of the **Enclave implementation**.

For Section 15, total Enclave storage is modelled as:

```
Enclave storage =
    vector_bearing_narrative_storage
  + graph_relationship_provenance_storage
  + additional_indexes_operational_overhead
  + replication_backups
```

The 9.5 KiB/record working value applies only to the vector-bearing narrative records.

**Scope boundary:** this estimate deliberately excludes the conventional game/simulation implementation required to make *Signals* playable, including engine data, terrain/geometry, graphics, audio, animation, physics, collision/navigation structures, conventional game-state storage, and application binaries.

---

> **Historical arithmetic notice (2026-10-08):** Sections 5 onward contain several derivations built from the superseded ~1,100 uniform-call workload. They are retained to preserve the research trail, but the current mixed-call calculations, Participant sensitivity, storage totals, and cost tables are in `docs/signals-section15-consolidated-computational-model-2026-10-08.md`. Do not cite the old 1,100-call figures as current.

## 5. Derived Inference Workload

### 5.1 Session token volume

Given:

```
calls = 1,100
input/call = 4,000 tokens
output/call = 250 tokens
```

Derived:

```
input tokens = 1,100 × 4,000 = 4,400,000
output tokens = 1,100 × 250 = 275,000
total tokens = 4,675,000
```

Over eight hours:

- average input processing demand: **152.8 input tok/s**;
- average generated-output demand: **9.55 output tok/s**;
- combined arithmetic average: **162.3 tokens/s**;
- mean probabilistic call arrival rate: **0.0382 calls/s**, or approximately **one call every 26.2 seconds** across the entire simulated world.

These averages are useful for total capacity but conceal burst concurrency.

---

## 6. Derived Hosted API Cost

Using current Standard short-context prices and the 4.4M input / 0.275M output workload:

### 6.1 Naive frontier-everything case

All calls on GPT-6 Astra:

```
4.4 × $10 + 0.275 × $50
= $44 + $13.75
= $57.75
```

**Derived cost: $57.75 per eight-hour *Signals* session.**

### 6.2 All-Sol comparison

```
4.4 × $2 + 0.275 × $10
= $8.80 + $2.75
= $11.55
```

**Derived cost: $11.55/session.**

### 6.3 All-Luna lower-bound comparison

```
4.4 × $0.10 + 0.275 × $0.50
= $0.44 + $0.1375
= $0.5775
```

**Derived cost: approximately $0.58/session.**

This is a price calculation, **not** a claim that Luna alone provides sufficient narrative quality.

### 6.4 Illustrative routed high-fidelity case

Routing assumption:

- 70% Luna;
- 25% Sol;
- 5% Astra.

Weighted rates:

```
input = 0.70($0.10) + 0.25($2) + 0.05($10)
      = $1.07 / 1M tokens

output = 0.70($0.50) + 0.25($10) + 0.05($50)
       = $5.35 / 1M tokens
```

Session:

```
4.4 × $1.07 + 0.275 × $5.35
= $4.708 + $1.47125
= $6.17925
```

**Derived illustrative routed cost: approximately $6.18/session.**

The difference between $57.75 and $6.18 demonstrates the potential importance of model routing without changing the number of Actors, cognitive cycles, Memories, Events, or consequences represented by Enclave.

It does **not** prove the routing policy is quality-equivalent; that requires evaluation.

---

## 7. Derived Burst Requirement

For twelve simultaneous Actor calls:

```
12 × 4,000 = 48,000 input tokens
12 × 250 = 3,000 output tokens
total = 51,000 tokens
```

If all twelve are required to complete within ten seconds, the simple combined-work target is:

```
51,000 / 10 = 5,100 aggregate tokens/s
```

Broken out:

- **4,800 input tok/s** of prompt processing averaged over the ten-second window;
- **300 output tok/s** of generation averaged over the ten-second window.

This is a workload target, not a direct GPU benchmark metric. Real serving systems separate prefill and decode, batch concurrent requests, and may use disaggregated serving.

The B200 InferenceMAX result of ~10,000 tok/s/GPU at 50 tok/s/user on a different 70B workload demonstrates that **contemporary datacenter hardware operates in the same or a greater aggregate-throughput regime**, but does not prove that one B200 will meet this exact Enclave burst under the same latency target.

---

## 8. Derived DGX Spark Local-Inference Illustration

The following extrapolation uses NVIDIA's batch-size-one measurements but assumes approximately linear token-processing time from the measured 2,048/128 workload to the Enclave 4,000/250 reference call.

That is useful for order-of-magnitude reasoning only.

### 8.1 GPT-OSS-20B

Published:

- prompt processing = 3,670.42 tok/s;
- generation = 82.74 tok/s.

Extrapolated 4,000 / 250 call:

```
prefill = 4,000 / 3,670.42 = 1.09 s
decode  = 250 / 82.74 = 3.02 s
total   ≈ 4.11 s/call
```

If all 1,100 calls were executed serially:

```
1,100 × 4.11 s ≈ 4,522 s ≈ 75.4 min
```

That is about **15.7% of an eight-hour session** in simple serial-equivalent accelerator time.

### 8.2 GPT-OSS-120B

Published:

- prompt processing = 1,725.47 tok/s;
- generation = 55.37 tok/s.

Extrapolated reference call:

```
prefill = 4,000 / 1,725.47 = 2.32 s
decode  = 250 / 55.37 = 4.52 s
total   ≈ 6.83 s/call
```

Serial-equivalent total:

```
1,100 × 6.83 s ≈ 7,517 s ≈ 125.3 min
```

That is about **26.1% of an eight-hour session** in simple serial-equivalent accelerator time.

### 8.3 Interpretation

These calculations support a limited claim:

> The average *Signals* inference volume is not inherently too large for contemporary desktop-class local inference hardware.

They do **not** establish:

- that the local models have sufficient Actor-cognition quality;
- that latency remains acceptable during dense multi-Actor bursts;
- that performance scales linearly at the longer sequence;
- that batch-size-one throughput predicts concurrent serving;
- that one DGX Spark is necessarily the preferred implementation.

Dense fan-out, rather than average session volume, is the stronger local-compute challenge.

---

## 9. Persistent Storage — Corrected Physical Model

The earlier 4.9 MB structured-payload / 10–16 MB vectorized calculation is **retired**. It described a compact logical payload, not a credible high-fidelity physical store.

### 9.1 Measured implementation envelope

For the paper's main storage calculations, use the conservative historical CTX PostgreSQL measurement of **~9.5 KiB per vector-bearing Memory** as the working physical-storage unit. Reliquary remains useful as an efficiency comparison, but not as the baseline.

```
Reliquary fully vectorized Memory        ≈ 5.0 KiB/record
Historical CTX PostgreSQL + HNSW Memory ≈ 9.5 KiB/record
```

Illustrative corpus sizes:

| Vector-bearing narrative records | Working storage estimate at 9.5 KiB/record |
| ---: | ---: |
| 3,700 | ~34 MiB |
| 10,000 | ~93 MiB |
| 25,000 | ~232 MiB |
| 50,000 | ~464 MiB |
| 100,000 | ~928 MiB |

These figures describe the representative Memory record plus its vectorized retrieval representation at the measured implementation points. Enclave-specific graph structures, additional provenance, replication, backups, and other system-level state must still be added where applicable.

### 9.2 Purpose-built comparison

The historical CTX benchmark measured approximately **948 MB across 102,520 vector-bearing rows**, or roughly **9.5 KiB per Memory all-in with HNSW**.

The analogous Reliquary record is approximately **5 KiB** even with the same-size 1024d `f32` embedding. Because the raw vector itself consumes 4,096 bytes, most of Reliquary's per-Memory footprint is the embedding rather than the semantic record structure.

Without the vector, the contrast is much larger:

- Reliquary representative core Memory: **~0.9–1.0 KiB**;
- historical CTX PostgreSQL physical row: **~6.8 KiB** before HNSW.

This comparison demonstrates that physical storage is architecture-dependent. For consistency, however, §15 will use the measured **~9.5 KiB/Memory** historical CTX PostgreSQL + HNSW result as its conservative working value and mention Reliquary only as evidence that purpose-built storage can be materially denser.

The CTX comparison in this paper is anchored to **GottZ/ctx** and its PostgreSQL storage benchmark.

### 9.3 The unresolved variable is corpus density

The current storage model uses **100,000–200,000 semantic/world Knowledge records (150,000 central)** plus **44,000 pre-existing Actor Memories**. A genuinely persistent Actor may carry:

- prior episodic Memories;
- personal biography;
- beliefs and claims;
- learned institutional Knowledge;
- relationship history;
- plans and obligations;
- provenance and temporal links.

Consequently, the paper should not state a single high-fidelity *Signals* storage number until a pre-existing history density is chosen explicitly.

Instead:

```
Signals storage =
  shared world/scenario state
+ Σ Actor histories
+ runtime Events
+ runtime Memories
+ Knowledge/relationship/graph edges
+ retrieval/index overhead
+ operational database overhead
```

### 9.4 Current defensible conclusion

The adventure's **runtime growth alone** is modest, but the complete high-fidelity narrative corpus may reasonably range from tens or hundreds of megabytes into low gigabytes depending on the amount of pre-existing Actor history represented.

The previous claim that high-fidelity *Signals* state was inherently only 10–16 MB was not justified and should not appear in the paper.

---

## 10. Derived Retrieval and Deterministic Operation Rates

Spread uniformly over eight hours:

### Retrieval

```
3,000 retrieval operations / 28,800 s ≈ 0.104 retrievals/s
40,000 candidate records / 28,800 s ≈ 1.39 candidate records/s
```

### Persistent-state creation

```
400 Events / 28,800 s ≈ 0.0139 Events/s
2,000 Memories / 28,800 s ≈ 0.0694 Memories/s
2,000 Knowledge edges / 28,800 s ≈ 0.0694 edge writes/s
```

### Authoritative operations

```
2,750 state operations / 28,800 s ≈ 0.0955 operations/s
```

These arithmetic averages are extremely low operation counts for conventional storage/CPU systems.

No claim should yet be made about exact milliseconds or CPU-seconds per authoritative operation because Enclave has not supplied an implementation benchmark for those operations. The defensible conclusion at this stage is about **operation count**, not an invented per-operation runtime.

---

## 11. Dedicated Cloud Infrastructure Envelope

Using current AWS Capacity Block rates, if hardware were reserved for the entire eight-hour session:

### One H100 p5.4xlarge

```
8 h × $5.191/h = $41.528
```

**~$41.53 for eight hours of dedicated H100 capacity.**

### Eight-B200 p6-b200.48xlarge

```
8 h × $98.84/h = $790.72
```

**~$790.72 for eight hours of the eight-GPU B200 instance.**

These numbers illustrate why a small Enclave deployment should not be equated with reserving a large datacenter server for the whole play session. Hosted token billing or local hardware can exploit the workload's low average duty cycle much more efficiently.

---

## 12. Local Energy Envelope

The DGX Spark has a 240 W power supply. Treating 240 W as a deliberately conservative sustained wall-power ceiling for eight hours:

```
0.240 kW × 8 h = 1.92 kWh
```

This is an **upper-envelope energy calculation based on power-supply capacity**, not measured session consumption.

At an illustrative electricity price:

- $0.10/kWh → **$0.19**;
- $0.20/kWh → **$0.38**.

The electricity price is intentionally left as a variable because local tariffs differ.

Capital cost is separate from marginal energy cost.

---

## 13. Sensitivity Analysis

The hosted routed-cost equation is:

```
Cost =
  (calls × input_tokens_per_call / 1,000,000 × weighted_input_rate)
+ (calls × output_tokens_per_call / 1,000,000 × weighted_output_rate)
```

For the illustrative 70/25/5 routing:

- weighted input = $1.07/M;
- weighted output = $5.35/M.

### Effect of 100 additional cognitive calls

At 4,000 input / 250 output each:

**+$0.562/session** approximately.

### Effect of adding 1,000 input tokens to every call

Additional 1.1M input tokens:

**+$1.177/session** approximately.

### Effect of adding 100 output tokens to every call

Additional 110,000 output tokens:

**+$0.589/session** approximately.

### What dominates cost?

For this workload:

1. **Model selection/routing** has the largest price multiplier.
2. **Number of cognitive calls** scales both input and output cost linearly.
3. **Context size** is important because every cognitive cycle pays its prompt cost.
4. **Output length** has disproportionate cost per token because generation prices exceed input prices.
5. Retrieval and persistent-state operation counts are too small at adventure scale to compete with inference economically unless implemented pathologically.

---

## 14. High Fidelity Is Not the Same as Maximum Compute

This distinction is central to Section 15.

### Techniques that can reduce computation without inherently reducing narrative fidelity

Provided they are implemented correctly:

- model routing by responsibility and difficulty;
- deterministic resolution of authoritative world mechanics;
- event-triggered cognition instead of fixed-rate model polling;
- bounded retrieval instead of inserting the entire world state into each prompt;
- prompt/prefix caching;
- batching where latency permits;
- semantic and structured indexes;
- smaller specialist models for extraction/classification;
- storing one canonical Event while creating distinct Actor Memories/references to it;
- avoiding persistence of private model reasoning that is not narrative state.

These techniques change **how efficiently the same narrative state is processed**.

### Techniques that may actually reduce fidelity

Depending on use:

- aggregating individually relevant Actors into crowds;
- suspending an off-screen Actor who remains causally active;
- discarding Actor-specific Memories that would affect later behaviour;
- compressing Knowledge so aggressively that distinctions/provenance are lost;
- reducing cognition frequency when circumstances should reasonably cause reconsideration;
- ignoring propagation because the affected Actor is not currently visible;
- deleting meaningful consequences to keep state small.

These techniques change **what the world represents or remembers**, not merely how cheaply it computes.

---

## 15. Current Bottleneck Assessment for *Signals*

Based on the central workload and current evidence:

### 1. Probabilistic inference — dominant

- millions of tokens rather than thousands of operations;
- expensive relative to ordinary persistence;
- latency-sensitive during Actor fan-out;
- highly sensitive to model choice and routing.

### 2. Retrieval/context construction — secondary but architecturally important

- low operation count at *Signals* scale;
- unlikely to dominate hardware cost;
- essential to correctness because it bounds what each Actor can know;
- becomes more important with long histories and large worlds.

### 3. Persistence/storage — secondary at adventure scale, but architecture-dependent

- runtime growth from one eight-hour adventure is modest;
- the complete physical corpus depends primarily on how much pre-existing Actor history is represented;
- the conservative working storage value is **~9.5 KiB per vector-bearing Memory**, taken from the historical CTX PostgreSQL + HNSW benchmark;
- tens of thousands of vector-bearing narrative records therefore move naturally into the tens-to-hundreds-of-megabytes range, with 100,000 records approaching **~928 MiB** at the working baseline;
- storage is still unlikely to dominate probabilistic inference cost for one adventure, but that conclusion should be demonstrated from an explicit corpus-density assumption rather than from the retired 10–16 MB estimate.

### 4. Deterministic authoritative computation — lowest demonstrated burden

- only ~2,750 central state operations in the reference run;
- the current evidence supports describing the operation count as small;
- exact CPU cost should await an Enclave implementation benchmark rather than being fabricated.

---

## 16. What We Can Defensibly Say Now

With assumptions stated explicitly, Section 15 can already support claims of the following form:

> Under the central high-fidelity *Signals* workload, approximately 1,100 probabilistic calls at 4,000 input and 250 output tokens each produce roughly 4.675 million model tokens across an eight-hour adventure. At current standard API prices, running every call on GPT-6 Astra would cost approximately $57.75, while an illustrative 70% Luna / 25% Sol / 5% Astra routing policy would cost approximately $6.18. Storage cannot yet be reduced to one defensible session total because the dominant unknown is the amount of pre-existing Actor history represented. For calculation, §15 uses the measured historical CTX PostgreSQL + HNSW result of approximately **~9.5 KiB per vector-bearing Memory** as the conservative working storage unit. Average inference throughput is modest; the harder compute problem is burst fan-out when many Cognitive Actors react to one causally important Event.

We can also defensibly state:

> Published DGX Spark results indicate that contemporary desktop AI hardware can process the *average* inference volume of the adventure within the eight-hour play window. This does not establish that any particular local model supplies sufficient narrative reasoning quality, nor that a single desktop system meets every dense-scene latency target.

These are derived engineering claims with traceable assumptions, not Enclave implementation benchmarks.

---

## 17. What Still Requires Measurement

Before final publication, ideally benchmark an Enclave prototype for:

1. actual prompt-token distribution by cognitive responsibility;
2. actual output-token distribution;
3. number of model calls produced by a real *Signals* playthrough;
4. retrieval query count and candidate-set size;
5. context-build latency;
6. DB record and index sizes in the chosen implementation;
7. Event/Memory write amplification;
8. local-model quality by responsibility;
9. burst latency with 5, 10, 20, and 40 simultaneously reacting Actors;
10. effectiveness of routing/caching/batching;
11. deterministic event-resolution throughput;
12. end-to-end cost under identical narrative outcomes.

Those measurements would convert this section from a defensible computational model into an empirical Enclave benchmark.

---

## 18. Scaling Formulas for Later Section 15 Work

Let:

- (C) = cognitive calls;
- (I) = mean input tokens/call;
- (O) = mean output tokens/call;
- (P_i) = input price per million tokens;
- (P_o) = output price per million;
- (M) = number of Memories;
- (E) = Events;
- (K) = Knowledge-association writes;
- (R) = retrieval operations.

Then:

### Token volume

```
T_input  = C × I
T_output = C × O
T_total  = C × (I + O)
```

### Hosted cost

```
Cost = (C × I / 1e6 × P_i) + (C × O / 1e6 × P_o)
```

For routed models, replace (P_i) and (P_o) with workload-weighted prices or calculate each route separately.

### Average session throughput

For session length (S) seconds:

```
average_input_tps  = C × I / S
average_output_tps = C × O / S
```

### Persistent payload

```
Storage =
  Facts × bytes_per_Fact
+ Memories × bytes_per_Memory
+ Events × bytes_per_Event
+ edges × bytes_per_edge
+ Actor_state
+ relationships
+ embeddings
+ implementation_overhead
```

### pgvector embedding payload

For (D) dimensions and (V) vectors:

```
float32 vector bytes = V × (4D + 8)
halfvec bytes        = V × (2D + 8)
```

These equations should be reused when Section 15 moves from one *Signals* adventure to larger populations instead of inventing a separate accounting model.

---

## 19. Source Quality Notes

### Primary / authoritative
- Modiphius — adventure publication.
- OpenAI — current API pricing.
- NVIDIA — DGX Spark specifications and published local benchmark measurements.
- AWS — current Capacity Block pricing.
- pgvector project — storage representation formulas.
- MLCommons — standardized inference benchmark program/results.

### Vendor-reported benchmark requiring caution
- NVIDIA reporting SemiAnalysis InferenceMAX results. The methodology is reproducible/open, but NVIDIA is also the hardware vendor. Use the result as a hardware-capacity reference rather than as a neutral universal performance claim.

### Enclave-derived
All scenario workload counts, token assumptions, storage-record sizes, routing proportions, burst windows, and resulting cost/storage arithmetic unless explicitly sourced above.

---

## 20. Research Record

Research verified against live sources on **2026-10-07**. Because API prices, cloud prices, model availability, and inference software change rapidly, Section 15 should preserve the date attached to contemporary cost/performance claims.
