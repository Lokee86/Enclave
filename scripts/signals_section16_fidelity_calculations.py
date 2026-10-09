#!/usr/bin/env python3
"""Reproducible Section 16.6 fidelity comparison; execute from Enclave repository root.

Source assumptions: docs/signals-section15-consolidated-computational-model-2026-10-08.md
and docs/manhattan-test-scaling-2026-10-08.md. Model, NOT execution benchmarks.
"""
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parents[1]
NPC=43
CITY=1_664_862
WORLD_KNOWLEDGE=150_000
PRIOR_MEMORIES=1_000
KIB=9.5
IN_RATE,OUT_RATE=1.07,5.35
SOCIAL_IN,SOCIAL_OUT=4000,250
WORLD_IN,WORLD_OUT=1500,80

# Section 15 frozen eight-simulated-hour background reference.
BG_INTERACTIONS=2624
BG_CALLS=1221
BG_SOCIAL=658
BG_WORLD=563
BG_INPUT=3_476_500
BG_OUTPUT=209_540
BG_MEMORIES=2843
BG_GENERATED=13339
PLAYER_INTERACTIONS=244   # 4x Participant activity; 1 PA per 43 NPC
PLAYER_GENERATED_FULL=1342  # existing rounded section 15 record increment
assert BG_CALLS==BG_SOCIAL+BG_WORLD
assert BG_INPUT==BG_SOCIAL*SOCIAL_IN+BG_WORLD*WORLD_IN
assert BG_OUTPUT==BG_SOCIAL*SOCIAL_OUT+BG_WORLD*WORLD_OUT

# Transparent NEW sensitivity assumptions; not measured rates.
DIALOGUE_FRACTION=.25
CALLS_PER_DIALOGUE=2.0
HYBRID_L1=34
HYBRID_L2=3
HYBRID_L3=4
HYBRID_OTHER=2  # remote captain conditional, distress-source deterministic
HYBRID_FULL_ACTOR_EQUIV=2.5 # Ero 1, captain 1, wounded .25, representative .25
HYBRID_LOW_EVENT_FRACTION=.10
HYBRID_PLAYER_EVENT_FRACTION=.25
HYBRID_PERSISTENT_DIALOGUE_FRACTION=.50
assert HYBRID_L1+HYBRID_L2+HYBRID_L3+HYBRID_OTHER==43

def calls(social,world=0):
 return {'calls':social+world,'input':social*SOCIAL_IN+world*WORLD_IN,'output':social*SOCIAL_OUT+world*WORLD_OUT}

def enrich(c, prior, generated, world_knowledge=None):
 o=dict(c)
 o.update(tokens=o['input']+o['output'],
          usd=o['input']*IN_RATE/1e6+o['output']*OUT_RATE/1e6,
          prior_memories=prior,generated_records=generated,
          runtime_mib=generated*KIB/1024,
          runtime_tib=generated*KIB/1024**3)
 if world_knowledge is not None:
  o.update(world_knowledge=world_knowledge,
           final_records=world_knowledge+prior+generated,
           final_gib=(world_knowledge+prior+generated)*KIB/1024**2)
 return o

def uniform(npcs,participant_count,world_knowledge=None):
 factor=npcs/NPC
 dialogue=participant_count*PLAYER_INTERACTIONS*DIALOGUE_FRACTION
 player_calls=dialogue*CALLS_PER_DIALOGUE
 one=calls(player_calls)
 l1=enrich(one,0,0,world_knowledge)
 l2=enrich(one,npcs*PRIOR_MEMORIES,dialogue,world_knowledge)
 bg={'calls':BG_CALLS*factor,'input':BG_INPUT*factor,'output':BG_OUTPUT*factor}
 l3=enrich({key:bg[key]+one[key] for key in bg},
           (npcs+participant_count)*PRIOR_MEMORIES,
           BG_GENERATED*factor+PLAYER_GENERATED_FULL*participant_count,
           world_knowledge)
 return {'level1':l1,'level2':l2,'level3':l3}

signals=uniform(NPC,1,WORLD_KNOWLEDGE)
player_ratio=CITY/NPC
manhattan=uniform(CITY,player_ratio)

# §16.5 fidelity roster; use full-Actor equivalent duty cycle instead of
# counting eligible full Actors as continuously thinking.
fraction=HYBRID_FULL_ACTOR_EQUIV/NPC
bg_s=BG_SOCIAL*fraction
bg_w=BG_WORLD*fraction
active_interactions=BG_INTERACTIONS*fraction
low_interactions=BG_INTERACTIONS-active_interactions
included_bg=active_interactions+HYBRID_LOW_EVENT_FRACTION*low_interactions
bg_rows=4*included_bg+BG_MEMORIES*fraction
player_dialogues=PLAYER_INTERACTIONS*DIALOGUE_FRACTION
player_consequential=PLAYER_INTERACTIONS*HYBRID_PLAYER_EVENT_FRACTION
player_rows=(4*player_consequential+player_consequential+
             player_dialogues*HYBRID_PERSISTENT_DIALOGUE_FRACTION)
hybrid=enrich(calls(bg_s+player_dialogues*CALLS_PER_DIALOGUE,bg_w),
              (HYBRID_L2+HYBRID_L3)*PRIOR_MEMORIES,bg_rows+player_rows,
              WORLD_KNOWLEDGE)
assert round(signals['level3']['calls'])==1343
assert round(signals['level3']['tokens'])==4_204_540
assert round(signals['level3']['generated_records'])==14681
assert round(signals['level1']['calls'])==122
assert round(signals['level2']['generated_records'])==61
assert hybrid['calls']<signals['level3']['calls']
assert hybrid['generated_records']<signals['level3']['generated_records']

output={'metadata':{'simulated_hours':8,'manhattan_npcs':CITY,
 'manhattan_participants':player_ratio,'signals_participants':1,
 'participant_activity':'4x / 244 interactions per active Participant',
 'world_knowledge_signals':WORLD_KNOWLEDGE,'kib_per_vector_record':KIB,
 'usd_million_input':IN_RATE,'usd_million_output':OUT_RATE},
 'assumptions':{'dialogue_fraction':DIALOGUE_FRACTION,
 'calls_per_dialogue':CALLS_PER_DIALOGUE,
 'hybrid_full_actor_equivalents':HYBRID_FULL_ACTOR_EQUIV,
 'hybrid_low_fidelity_event_fraction':HYBRID_LOW_EVENT_FRACTION,
 'hybrid_participant_consequential_fraction':HYBRID_PLAYER_EVENT_FRACTION,
 'hybrid_persistent_npc_dialogue_fraction':HYBRID_PERSISTENT_DIALOGUE_FRACTION},
 'signals':dict(signals,hybrid=hybrid),'manhattan':manhattan,
 'hybrid_accounting':{'full_background_interactions':active_interactions,
 'low_background_interactions':low_interactions,'included_background_interactions':included_bg,
 'background_rows':bg_rows,'participant_rows':player_rows,
 'background_model_calls':bg_s+bg_w,'participant_model_calls':player_dialogues*CALLS_PER_DIALOGUE}
}
out=ROOT/'data/signals-section16-fidelity-results.json'
out.write_text(json.dumps(output,indent=2)+'\n',encoding='utf-8')
for label,rows in [('Signals',output['signals']),('Manhattan',output['manhattan'])]:
 print(label)
 for level,metric in rows.items():
  print(level, 'calls',round(metric['calls']),'tokens',round(metric['tokens']),
        'USD',round(metric['usd'],2),'newrows',round(metric['generated_records']),
        'MiB',round(metric['runtime_mib'],2))
print('PASS: calculations and invariants; data:',out)


def fmt_num(x):
    return f"{x:,.0f}"
def fmt_small(x, n=2):
    return f"{x:,.{n}f}"
def mk_signals_rows():
    name={'level1':'Level 1 — Reactive Dialogue','level2':'Level 2 — Persistent Characters',
          'level3':'Level 3 — full narrative architecture','hybrid':'Hybrid Level 3 — approved §16.5 roster'}
    return '\n'.join(
        f"| {name[k]} | {fmt_num(v['calls'])} | {fmt_small(v['tokens']/1e6,3)}M | "
        f"${fmt_small(v['usd'])} | {fmt_num(v['generated_records'])} | "
        f"{fmt_small(v['runtime_mib'])} MiB | {fmt_small(v['final_gib'],3)} GiB |"
        for k,v in output['signals'].items()
    )
def mk_manhattan_rows():
    name={'level1':'Level 1 — Reactive Dialogue','level2':'Level 2 — Persistent Characters',
          'level3':'Level 3 — full narrative architecture'}
    v=output['manhattan']
    return '\n'.join(
        f"| {name[k]} | {fmt_num(t['calls'])} | {fmt_small(t['tokens']/1e9,3)}B | "
        f"${fmt_num(t['usd'])} | {fmt_num(t['generated_records'])} | "
        f"{fmt_small(t['runtime_tib'],3)} TiB |"
        for k,t in v.items()
    )

s1=signals['level1'];s2=signals['level2'];s3=signals['level3']
h=hybrid
saved_calls=100*(1-h['calls']/s3['calls'])
saved_tokens=100*(1-h['tokens']/s3['tokens'])
saved_rows=100*(1-h['generated_records']/s3['generated_records'])
doc_signals=f"""## 18. Section 16.6 — Implementation-Level and Hybrid Cost Comparison (2026-10-08)

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
{mk_signals_rows()}

**Interpretation:** the low-level applications remain conversational rather than autonomously cognitive; their calls are driven by Participant activity, not by the settlement's ordinary work. The final-corpus column holds world Knowledge fixed, while actor-specific starting histories differ: 0 personal Memories in Level 1, 43,000 in Level 2, 44,000 (including the Participant Actor) in full Level 3, and 7,000 for the hybrid's four eligible Level 3 plus three Level 2 NPCs. The physical 9.5 KiB/record benchmark prices the vector-bearing corpus only; independent graph, provenance, interface, and engine costs are excluded.

### 18.3 Explicit §16.5 *Signals* hybrid model

- **Roster:** 34 ordinary settlers (Level 1); 3 ordinary Romulans (Level 2); 4 potentially full Cognitive Actors (Ero Drallen, Romulan captain, wounded Romulan and one conditional settlement representative); one remote Starfleet captain available only upon conditional activation; one deterministic distress-source Actor. There are **43 NPCs** in all, plus the human Participant Actor.
- **Eight-hour activation schedule for this illustrative calculation:** Ero and the Romulan captain at 100% reference background cognitive activity; wounded Romulan at 25%; secondary representative at 25%; remote captain at 0% unless activated. These are **2.5 full-Actor-equivalent duty periods**, **not measured character behaviour**, producing approximately **{fmt_small(output['hybrid_accounting']['background_model_calls'])} autonomous model calls** before Participant dialogue.
- **Ordinary conventional world activity remains:** all 43 NPCs collectively perform the same ~2,624 synthetic background Interactions. The active-equivalent narrative cast accounts for **{fmt_small(output['hybrid_accounting']['full_background_interactions'])}** Interactions in full Enclave event accounting; provisionally **10%** of the other **{fmt_small(output['hybrid_accounting']['low_background_interactions'])}** routine Interactions create consequential Enclave Events. This yields about **{fmt_num(output['hybrid_accounting']['included_background_interactions'])}** Enclave-recorded background Interactions (two Event plus two Fact records each), plus approximately **165** background full-Actor Memories.
- **Participant activity:** of 244 Interactions, assume **25%** are consequential and receive full 2-Event/2-Fact recording. Persist a Participant Memory for each consequential Interaction; provisionally **50%** of the 61 dialogue Interactions concern Level 2/3 NPCs and create a separate NPC Memory. All Participant-triggered dialogue still costs **122 model calls**, whatever the NPC's fidelity. These fractions are sensitivity choices, not empirically validated rates.
- **Generated-record derivation:** **{fmt_small(output['hybrid_accounting']['background_rows'])} background rows + {fmt_small(output['hybrid_accounting']['participant_rows'])} Participant-associated rows = {fmt_small(h['generated_records'])} rows**, rounded to ~{fmt_num(h['generated_records'])}. Event relevance is *categorical*: a causally relevant Event must be retained even if the provisional 10%/25% assumptions underestimate its frequency. Unrecorded conventional actions remain resolved by the ordinary game engine.
- **Result at matched Participant activity:** {fmt_num(h['calls'])} versus {fmt_num(s3['calls'])} model calls (**{fmt_small(saved_calls,1)}% fewer**); {fmt_small(h['tokens']/1e6,3)}M versus {fmt_small(s3['tokens']/1e6,3)}M tokens (**{fmt_small(saved_tokens,1)}% fewer**); about {fmt_num(h['generated_records'])} versus {fmt_num(s3['generated_records'])} generated vector records (**{fmt_small(saved_rows,1)}% fewer** under the event-filter assumptions).
- Fidelity may change during the narrative. A wounded Romulan who rejoins his comrades can cease autonomous cognition while remaining in authoritative state. If the Starfleet captain or another representative becomes consequential, the active-equivalent and model-call budget must rise accordingly.

### 18.4 Limits and reproducibility

These are *sensitivity calculations*, not recorded dialogue frequencies, causal Event probabilities, inference latencies, an executable Enclave benchmark, or a prediction of NPC behaviour. Both lower-level dialogue engagement and hybrid Event capture must be measured in an actual game. Memory extraction, retrieval, vector indexing, context assembly, graph traversal, synchronization, batching, model quality, burst concurrency, and external game-engine storage are not priced as separate operations.

Reproduce the exact figures using **scripts/signals_section16_fidelity_calculations.py**, which emits **data/signals-section16-fidelity-results.json**. The existing **docs/manhattan-test-scaling-2026-10-08.md** now contains the parallel urban comparison. This leaves distributed scaling and partitioning analysis for the planned Appendix/Addendum rather than repeating §15.

"""
city2=manhattan['level2'];city3=manhattan['level3']
prior_tib=CITY*PRIOR_MEMORIES*KIB/1024**3
city_doc=f"""## Section 16.6 — Uniform-Fidelity Implementation Comparison (2026-10-08)

This is an extension of the preceding **background-only** Manhattan Test; the original background figures above are **unchanged**. Eight simulated hours, **{fmt_num(CITY)} NPCs**, and the same first-order per-NPC §15 activity assumptions apply.

### Additional Participant-density assumption

Neither Reactive Dialogue nor Persistent Characters has a meaningful fixed inference rate per NPC: inference depends on **active Participants**, not total NPC population. For a controlled comparison with *Signals*, assume **one active Participant Actor per 43 NPCs**, or about **{fmt_num(player_ratio)} simultaneous Participants** for Manhattan, each at **4× ordinary Actor activity** (244 Interactions, 25% dialogue, two 4,000/250-token responses per dialogue). This is an illustrative, exceptionally large concurrent-Participant population — **not** an empirical player-population estimate. With *P* active Participants, Level 1 and 2 cost **122 × P dialogue calls**; if *P* is zero, conversational inference is zero regardless of Manhattan's NPC count.

### Comparative eight-hour workload

| Uniform level | Model calls | Model tokens | Routed inference cost (USD) | New vector-bearing rows | Generated vector storage |
| --- | ---: | ---: | ---: | ---: | ---: |
{mk_manhattan_rows()}

- **Level 1** includes only reactive dialogue inference and no new vector-bearing NPC Memories or routine Enclave Events. It still requires conventional world-state storage and any authored dialogue/Knowledge corpus.
- **Level 2** has identical dialogue inference, plus approximately **{fmt_num(city2['generated_records'])} new NPC Memories** (**{fmt_small(city2['runtime_mib']/1024,2)} GiB**) for the active Participants' dialogue. Giving **all {fmt_num(CITY)} NPCs 1,000 pre-existing Memories** already requires **{fmt_small(prior_tib,3)} TiB** of vector-bearing historical Memory, before authorship, new Memory, relationship indexes or game-engine state.
- **Level 3** includes the original §15 **background-only** ~47.27 million autonomous calls, ~142.715 billion tokens and ~4.569 TiB generated vector records, **plus** the {fmt_num(player_ratio)} Participants' direct and downstream interactions. At this particular density it becomes **~{fmt_small(city3['calls']/1e6,3)} million calls**, **~{fmt_small(city3['tokens']/1e9,3)} billion tokens**, and **~{fmt_small(city3['runtime_tib'],3)} TiB** of newly generated vector records. The §15 background-only cost figures should **not** be overwritten with this Player-inclusive scenario.
- The table prices *new records only*. **City-scale authored/world Knowledge remains unspecified**, and the total Manhattan Enclave corpus cannot therefore be computed responsibly. It excludes additional graph and provenance structures, network/synchronization, actual inference-serving capacity, causal bursts, player-side client work and the game engine.
- **Interpretation:** Levels 1–2 are driven by Participant conversation volume; Level 3 incurs background autonomous cognition from all represented Cognitive Actors. Actual shared-world scaling, zone boundaries and parallel Event processing belong in a future scaling Appendix/Addendum.

Calculation source: scripts/signals_section16_fidelity_calculations.py; machine-readable results: data/signals-section16-fidelity-results.json; assumptions inherited from docs/signals-section15-consolidated-computational-model-2026-10-08.md.

"""

def replace_append(path, heading, part):
    text=path.read_text(encoding='utf-8')
    if heading in text:
        text=text[:text.index(heading)]
    path.write_text(text.rstrip()+'\n\n'+part.rstrip()+'\n',encoding='utf-8')

replace_append(ROOT/'docs/signals-section15-consolidated-computational-model-2026-10-08.md',
               '## 18. Section 16.6 — Implementation-Level',doc_signals)
replace_append(ROOT/'docs/manhattan-test-scaling-2026-10-08.md',
               '## Section 16.6 — Uniform-Fidelity',city_doc)
print('PASS: Existing Signals and Manhattan research calculation documents extended for section 16.6')
