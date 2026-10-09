#!/usr/bin/env python3
"""
Synthetic temporal-contact workload model for the Signals settlement.

Purpose
-------
Estimate background contact, Interaction, and cognition workload for the
approximately 36-person settlement used by Section 15 of the Enclave paper.

This is an engineering model, not an empirical social-science model. The
important feature is that workload emerges from:
    schedules -> Locus co-presence -> contact opportunities -> Interactions
    -> cognitive cycles

rather than from an arbitrary number of model calls per Actor.

Uses only the Python standard library.

Example:
    python scripts/signals_settlement_sim.py --runs 10000 --seed 20261007 \
        --output-dir data/signals-settlement-sim
"""

from __future__ import annotations

import argparse
import csv
import json
import math
import random
import statistics
from collections import Counter, defaultdict
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Sequence, Tuple


STEP_MINUTES = 5
START_MINUTE = 8 * 60
END_MINUTE = 16 * 60
ACTOR_COUNT = 36

# Interaction initiation rates are per Actor-hour while co-present with at
# least one other Actor. These are explicit modelling assumptions.
PAIR_INTERACTION_RATE_PER_HOUR = {
    "home": 0.80,
    "work": 0.45,
    "commons": 1.20,
    "transit": 0.10,
    "social": 1.00,
}

# Actor<->world Interaction rates are deliberately much higher than social
# Interaction rates because ordinary work consists primarily of causal
# interactions with tools, materials, systems, terrain, objects, and other
# non-Actor parts of the world. Rates are narrative/simulation-significant
# task interactions per Actor-hour, not motor actions.
WORK_WORLD_INTERACTION_RATE_PER_HOUR = {
    "miner": 11.0,
    "agriculture": 9.0,
    "maintenance": 12.0,
    "logistics": 10.0,
    "security": 7.0,
    "medical": 9.0,
    "administration": 6.0,
    "leadership": 6.0,
}

NONWORK_WORLD_INTERACTION_RATE_PER_HOUR = {
    "home": 4.0,
    "commons": 2.5,
    "transit": 3.0,
    "social": 1.5,
}

# Fraction of Actor<->world Interactions that require a fresh probabilistic
# interpretation/decision instead of being resolved as routine deterministic
# continuation of an existing plan.
WORK_WORLD_COGNITION_PROBABILITY = {
    "miner": 0.16,
    "agriculture": 0.18,
    "maintenance": 0.24,
    "logistics": 0.18,
    "security": 0.22,
    "medical": 0.32,
    "administration": 0.26,
    "leadership": 0.34,
}

NONWORK_WORLD_COGNITION_PROBABILITY = {
    "home": 0.12,
    "commons": 0.08,
    "transit": 0.10,
    "social": 0.06,
}

# Group Interaction initiation rates are per occupied Locus-hour for groups
# of at least three Actors.
GROUP_INTERACTION_RATE_PER_HOUR = {
    "home": 0.25,
    "work": 0.18,
    "commons": 0.65,
    "transit": 0.03,
    "social": 0.50,
}

# Expected cognitive turns are sampled around these ranges. A cognitive turn
# is one Actor requiring a bounded context + probabilistic evaluation.
PAIR_COGNITIVE_TURN_RANGE = {
    "home": (2, 5),
    "work": (1, 4),
    "commons": (2, 6),
    "transit": (1, 2),
    "social": (2, 7),
}

GROUP_COGNITIVE_TURN_RANGE = {
    "home": (3, 8),
    "work": (3, 8),
    "commons": (4, 12),
    "transit": (2, 5),
    "social": (4, 12),
}

RELATIONSHIP_WEIGHT = {
    "household": 4.0,
    "close": 2.5,
    "crew": 2.0,
    "occupation": 1.35,
    "acquaintance": 1.0,
}


@dataclass(frozen=True)
class Actor:
    actor_id: int
    name: str
    household: int
    occupation: str
    crew: str
    work_locus: str
    social_cluster: int
    named_role: str | None = None


@dataclass(frozen=True)
class ScheduleBlock:
    actor_id: int
    start: int
    end: int
    locus: str
    context: str
    activity: str


@dataclass(frozen=True)
class ContactEpisode:
    actor_a: int
    actor_b: int
    locus: str
    context: str
    start: int
    end: int

    @property
    def duration_minutes(self) -> int:
        return self.end - self.start


@dataclass
class RunSummary:
    run: int
    pair_interactions: int
    group_interactions: int
    social_interactions: int
    world_interactions: int
    total_interactions: int
    social_cognitive_cycles: int
    world_cognition_triggers: int
    world_cognitive_cycles: int
    total_cognitive_cycles: int
    generated_event_records: int
    generated_fact_records: int
    social_memory_records: int
    world_memory_records: int
    total_memory_records: int
    total_generated_vector_records: int


def minute_label(value: int) -> str:
    return f"{value // 60:02d}:{value % 60:02d}"


def build_actors() -> List[Actor]:
    """Build one reproducible 36-person synthetic settlement."""
    occupations = [
        ("miner", 10, "mine"),
        ("agriculture", 6, "greenhouse"),
        ("maintenance", 5, "workshop"),
        ("logistics", 4, "depot"),
        ("security", 4, "security_post"),
        ("medical", 2, "clinic"),
        ("administration", 3, "administration"),
        ("leadership", 2, "administration"),
    ]

    rows: List[Tuple[str, str]] = []
    for occupation, count, base_locus in occupations:
        rows.extend((occupation, base_locus) for _ in range(count))

    actors: List[Actor] = []
    occupation_index: Counter[str] = Counter()

    for actor_id, (occupation, base_locus) in enumerate(rows):
        occupation_index[occupation] += 1

        # Twelve three-person households keep the synthetic population simple
        # and make household contacts explicit.
        household = actor_id // 3

        if occupation == "miner":
            crew = "mine_a" if occupation_index[occupation] <= 5 else "mine_b"
            work_locus = crew
        else:
            crew = f"{occupation}_{(occupation_index[occupation] - 1) // 5 + 1}"
            work_locus = base_locus

        named_role = None
        name = f"Settler {actor_id + 1:02d}"
        if actor_id == 0:
            name = "Ero Drallen"
            named_role = "settlement_leader"
        elif actor_id == 1:
            name = "Drev Katel"
            named_role = "named_settler"

        actors.append(
            Actor(
                actor_id=actor_id,
                name=name,
                household=household,
                occupation=occupation,
                crew=crew,
                work_locus=work_locus,
                social_cluster=actor_id % 6,
                named_role=named_role,
            )
        )

    return actors


def build_schedule(actors: Sequence[Actor]) -> List[ScheduleBlock]:
    """Create a representative eight-hour settlement day.

    The schedule deliberately produces household, work-crew, communal, transit,
    and late-day social contact without requiring every possible Actor subset.
    """
    blocks: List[ScheduleBlock] = []

    for actor in actors:
        home = f"home_{actor.household + 1:02d}"
        route = "mine_path" if actor.work_locus.startswith("mine_") else "central_path"
        social_locus = f"social_{actor.social_cluster + 1:02d}"

        blocks.extend(
            [
                ScheduleBlock(actor.actor_id, 480, 510, home, "home", "household_morning"),
                ScheduleBlock(actor.actor_id, 510, 535, route, "transit", "commute"),
                ScheduleBlock(actor.actor_id, 535, 710, actor.work_locus, "work", "morning_work"),
                ScheduleBlock(actor.actor_id, 710, 725, "central_path", "transit", "to_midday"),
                ScheduleBlock(actor.actor_id, 725, 775, "commons", "commons", "midday_meal"),
                ScheduleBlock(actor.actor_id, 775, 790, "central_path", "transit", "from_midday"),
                ScheduleBlock(actor.actor_id, 790, 925, actor.work_locus, "work", "afternoon_work"),
                ScheduleBlock(actor.actor_id, 925, 960, social_locus, "social", "late_day_social"),
            ]
        )

    return blocks


def schedule_lookup(
    actors: Sequence[Actor], blocks: Sequence[ScheduleBlock]
) -> Dict[int, Dict[int, Tuple[str, str]]]:
    """Map actor -> time step -> (locus, context)."""
    result: Dict[int, Dict[int, Tuple[str, str]]] = {
        actor.actor_id: {} for actor in actors
    }

    for block in blocks:
        for minute in range(block.start, block.end, STEP_MINUTES):
            result[block.actor_id][minute] = (block.locus, block.context)

    return result


def relationship_kind(a: Actor, b: Actor) -> str:
    if a.household == b.household:
        return "household"
    if a.social_cluster == b.social_cluster:
        return "close"
    if a.crew == b.crew:
        return "crew"
    if a.occupation == b.occupation:
        return "occupation"
    return "acquaintance"


def build_contact_episodes(
    actors: Sequence[Actor],
    lookup: Dict[int, Dict[int, Tuple[str, str]]],
) -> List[ContactEpisode]:
    """Merge continuous pairwise co-presence into temporal contact episodes."""
    open_contacts: Dict[Tuple[int, int, str, str], int] = {}
    episodes: List[ContactEpisode] = []

    for minute in range(START_MINUTE, END_MINUTE, STEP_MINUTES):
        occupants: Dict[Tuple[str, str], List[int]] = defaultdict(list)
        for actor in actors:
            locus_context = lookup[actor.actor_id].get(minute)
            if locus_context is not None:
                occupants[locus_context].append(actor.actor_id)

        active_keys = set()
        for (locus, context), ids in occupants.items():
            ids.sort()
            for i in range(len(ids)):
                for j in range(i + 1, len(ids)):
                    key = (ids[i], ids[j], locus, context)
                    active_keys.add(key)
                    open_contacts.setdefault(key, minute)

        ended = [key for key in open_contacts if key not in active_keys]
        for key in ended:
            start = open_contacts.pop(key)
            a, b, locus, context = key
            episodes.append(
                ContactEpisode(a, b, locus, context, start, minute)
            )

    for key, start in list(open_contacts.items()):
        a, b, locus, context = key
        episodes.append(ContactEpisode(a, b, locus, context, start, END_MINUTE))

    episodes.sort(key=lambda e: (e.start, e.locus, e.actor_a, e.actor_b))
    return episodes


def weighted_choice(
    rng: random.Random,
    candidates: Sequence[int],
    weights: Sequence[float],
) -> int:
    total = sum(weights)
    target = rng.random() * total
    cumulative = 0.0
    for candidate, weight in zip(candidates, weights):
        cumulative += weight
        if cumulative >= target:
            return candidate
    return candidates[-1]


def bernoulli_rate(
    rng: random.Random,
    per_hour_rate: float,
    step_minutes: int = STEP_MINUTES,
) -> bool:
    # Convert a Poisson-process rate to the probability of >=1 occurrence in
    # this discrete interval.
    p = 1.0 - math.exp(-per_hour_rate * step_minutes / 60.0)
    return rng.random() < p


def poisson_count(
    rng: random.Random,
    per_hour_rate: float,
    step_minutes: int = STEP_MINUTES,
) -> int:
    """Sample an event count for one interval.

    Knuth's algorithm is adequate here because all per-step lambdas are small.
    Unlike a Bernoulli trial, this permits several world Interactions inside
    one five-minute interval.
    """
    lam = per_hour_rate * step_minutes / 60.0
    threshold = math.exp(-lam)
    product = 1.0
    count = 0
    while product > threshold:
        count += 1
        product *= rng.random()
    return count - 1


def world_interaction_parameters(actor: Actor, context: str) -> Tuple[float, float]:
    if context == "work":
        return (
            WORK_WORLD_INTERACTION_RATE_PER_HOUR[actor.occupation],
            WORK_WORLD_COGNITION_PROBABILITY[actor.occupation],
        )
    return (
        NONWORK_WORLD_INTERACTION_RATE_PER_HOUR[context],
        NONWORK_WORLD_COGNITION_PROBABILITY[context],
    )


def simulate_one_run(
    run_index: int,
    rng: random.Random,
    actors: Sequence[Actor],
    lookup: Dict[int, Dict[int, Tuple[str, str]]],
) -> RunSummary:
    actor_map = {actor.actor_id: actor for actor in actors}

    pair_events = set()
    group_interactions = 0
    social_cycles = 0
    world_interactions = 0
    world_cognition_triggers = 0
    world_cycles = 0
    social_memory_records = 0
    world_memory_records = 0

    for minute in range(START_MINUTE, END_MINUTE, STEP_MINUTES):
        occupants: Dict[Tuple[str, str], List[int]] = defaultdict(list)
        for actor in actors:
            item = lookup[actor.actor_id].get(minute)
            if item is not None:
                occupants[item].append(actor.actor_id)

        # Actor<->world activity. Routine life is dominated by causal
        # interactions with the environment rather than by conversations:
        # operating tools, moving materials, traversing terrain, manipulating
        # systems, examining conditions, handling objects, and completing task
        # steps. Most continue deterministically; a minority require fresh
        # cognition or create a consequential canonical Event.
        for (locus, context), ids in occupants.items():
            for actor_id in ids:
                actor = actor_map[actor_id]
                rate, cognition_probability = world_interaction_parameters(
                    actor, context
                )
                count = poisson_count(rng, rate)
                world_interactions += count
                # Full-fidelity storage model: the acting Actor retains one
                # Memory of each world Interaction.
                world_memory_records += count

                for _ in range(count):
                    if rng.random() < cognition_probability:
                        world_cognition_triggers += 1
                        # Most world-facing decisions are one bounded
                        # evaluation; complex ones occasionally require a
                        # follow-up evaluation.
                        world_cycles += 1 + int(rng.random() < 0.22)

        # Actor-limited pair interactions. Each Actor gets an initiation
        # opportunity; this avoids the unrealistic combinatorial assumption
        # that all co-present pairs interact independently.
        for (locus, context), ids in occupants.items():
            if len(ids) < 2:
                continue

            initiation_rate = PAIR_INTERACTION_RATE_PER_HOUR[context]
            for actor_id in ids:
                if not bernoulli_rate(rng, initiation_rate):
                    continue

                candidates = [other for other in ids if other != actor_id]
                actor = actor_map[actor_id]
                weights = [
                    RELATIONSHIP_WEIGHT[
                        relationship_kind(actor, actor_map[other])
                    ]
                    for other in candidates
                ]
                partner = weighted_choice(rng, candidates, weights)

                # Same pair in same five-minute step is one interaction episode,
                # even if both Actors independently initiate.
                pair = tuple(sorted((actor_id, partner)))
                event_key = (minute, locus, pair[0], pair[1])
                if event_key in pair_events:
                    continue
                pair_events.add(event_key)
                # Both participating Actors retain an individual Memory of
                # the shared Interaction.
                social_memory_records += 2

                lo, hi = PAIR_COGNITIVE_TURN_RANGE[context]
                social_cycles += rng.randint(lo, hi)

        # Locus-level group interactions (crew coordination, communal
        # conversation, household discussion). These are one Interaction with
        # several participants, not every possible participant subset.
        for (locus, context), ids in occupants.items():
            if len(ids) < 3:
                continue
            group_rate = GROUP_INTERACTION_RATE_PER_HOUR[context]
            if not bernoulli_rate(rng, group_rate):
                continue

            group_interactions += 1
            max_size = min(8, len(ids))
            group_size = rng.randint(3, max_size)
            participants = rng.sample(ids, group_size)
            # Group Interaction is one Event but one Memory per participant.
            social_memory_records += len(participants)

            lo, hi = GROUP_COGNITIVE_TURN_RANGE[context]
            base_turns = rng.randint(lo, hi)
            # Larger groups create more potential cognition but not O(2^n).
            scale = max(1.0, len(participants) / 4.0)
            social_cycles += max(1, round(base_turns * scale))

    pair_interactions = len(pair_events)
    social_interactions = pair_interactions + group_interactions
    total_interactions = social_interactions + world_interactions

    # Ontology/storage accounting:
    # - an Interaction is itself an Event;
    # - resolution of that Interaction produces a resulting Event;
    # - therefore the first-order baseline is two Event records per Interaction;
    # - additional cascading Events may occur beyond this baseline but are not
    #   included here;
    # - central storage assumption: one generated Fact per Event;
    # - Memories are per participating Actor, tracked above.
    generated_event_records = total_interactions * 2
    generated_fact_records = generated_event_records
    total_memory_records = social_memory_records + world_memory_records
    total_generated_vector_records = (
        generated_event_records
        + generated_fact_records
        + total_memory_records
    )

    return RunSummary(
        run=run_index,
        pair_interactions=pair_interactions,
        group_interactions=group_interactions,
        social_interactions=social_interactions,
        world_interactions=world_interactions,
        total_interactions=total_interactions,
        social_cognitive_cycles=social_cycles,
        world_cognition_triggers=world_cognition_triggers,
        world_cognitive_cycles=world_cycles,
        total_cognitive_cycles=social_cycles + world_cycles,
        generated_event_records=generated_event_records,
        generated_fact_records=generated_fact_records,
        social_memory_records=social_memory_records,
        world_memory_records=world_memory_records,
        total_memory_records=total_memory_records,
        total_generated_vector_records=total_generated_vector_records,
    )


def percentile(values: Sequence[float], p: float) -> float:
    ordered = sorted(values)
    if not ordered:
        raise ValueError("percentile requires values")
    rank = (len(ordered) - 1) * p
    low = math.floor(rank)
    high = math.ceil(rank)
    if low == high:
        return float(ordered[low])
    frac = rank - low
    return ordered[low] * (1 - frac) + ordered[high] * frac


def describe(values: Sequence[int]) -> Dict[str, float]:
    return {
        "mean": statistics.fmean(values),
        "median": statistics.median(values),
        "p05": percentile(values, 0.05),
        "p25": percentile(values, 0.25),
        "p75": percentile(values, 0.75),
        "p95": percentile(values, 0.95),
        "min": min(values),
        "max": max(values),
    }


def write_actor_csv(path: Path, actors: Sequence[Actor]) -> None:
    with path.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=list(asdict(actors[0]).keys()))
        writer.writeheader()
        for actor in actors:
            writer.writerow(asdict(actor))


def write_schedule_csv(path: Path, blocks: Sequence[ScheduleBlock]) -> None:
    fields = ["actor_id", "start", "end", "start_time", "end_time", "locus", "context", "activity"]
    with path.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=fields)
        writer.writeheader()
        for block in blocks:
            writer.writerow(
                {
                    "actor_id": block.actor_id,
                    "start": block.start,
                    "end": block.end,
                    "start_time": minute_label(block.start),
                    "end_time": minute_label(block.end),
                    "locus": block.locus,
                    "context": block.context,
                    "activity": block.activity,
                }
            )


def write_contacts_csv(path: Path, episodes: Sequence[ContactEpisode]) -> None:
    fields = [
        "actor_a",
        "actor_b",
        "locus",
        "context",
        "start",
        "end",
        "start_time",
        "end_time",
        "duration_minutes",
    ]
    with path.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=fields)
        writer.writeheader()
        for ep in episodes:
            writer.writerow(
                {
                    "actor_a": ep.actor_a,
                    "actor_b": ep.actor_b,
                    "locus": ep.locus,
                    "context": ep.context,
                    "start": ep.start,
                    "end": ep.end,
                    "start_time": minute_label(ep.start),
                    "end_time": minute_label(ep.end),
                    "duration_minutes": ep.duration_minutes,
                }
            )


def write_runs_csv(path: Path, runs: Sequence[RunSummary]) -> None:
    fields = list(asdict(runs[0]).keys())
    with path.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=fields)
        writer.writeheader()
        for run in runs:
            writer.writerow(asdict(run))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--runs", type=int, default=10_000)
    parser.add_argument("--seed", type=int, default=20261007)
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("data/signals-settlement-sim"),
    )
    args = parser.parse_args()

    if args.runs < 1:
        raise SystemExit("--runs must be >= 1")

    actors = build_actors()
    blocks = build_schedule(actors)
    lookup = schedule_lookup(actors, blocks)
    contacts = build_contact_episodes(actors, lookup)

    rng = random.Random(args.seed)
    runs = [
        simulate_one_run(i + 1, rng, actors, lookup)
        for i in range(args.runs)
    ]

    output_dir = args.output_dir
    output_dir.mkdir(parents=True, exist_ok=True)

    write_actor_csv(output_dir / "actors.csv", actors)
    write_schedule_csv(output_dir / "schedule.csv", blocks)
    write_contacts_csv(output_dir / "contact_episodes.csv", contacts)
    write_runs_csv(output_dir / "runs.csv", runs)

    unique_pairs = {
        (ep.actor_a, ep.actor_b)
        for ep in contacts
    }
    contact_minutes = sum(ep.duration_minutes for ep in contacts)

    metrics = {
        "pair_interactions": describe([r.pair_interactions for r in runs]),
        "group_interactions": describe([r.group_interactions for r in runs]),
        "social_interactions": describe([r.social_interactions for r in runs]),
        "world_interactions": describe([r.world_interactions for r in runs]),
        "total_interactions": describe([r.total_interactions for r in runs]),
        "social_cognitive_cycles": describe([r.social_cognitive_cycles for r in runs]),
        "world_cognition_triggers": describe([r.world_cognition_triggers for r in runs]),
        "world_cognitive_cycles": describe([r.world_cognitive_cycles for r in runs]),
        "total_cognitive_cycles": describe([r.total_cognitive_cycles for r in runs]),
        "generated_event_records": describe([r.generated_event_records for r in runs]),
        "generated_fact_records": describe([r.generated_fact_records for r in runs]),
        "social_memory_records": describe([r.social_memory_records for r in runs]),
        "world_memory_records": describe([r.world_memory_records for r in runs]),
        "total_memory_records": describe([r.total_memory_records for r in runs]),
        "total_generated_vector_records": describe([r.total_generated_vector_records for r in runs]),
    }

    summary = {
        "model": "Signals synthetic settlement temporal-contact model",
        "seed": args.seed,
        "runs": args.runs,
        "population": len(actors),
        "duration_hours": (END_MINUTE - START_MINUTE) / 60,
        "step_minutes": STEP_MINUTES,
        "possible_unique_pairs": len(actors) * (len(actors) - 1) // 2,
        "observed_unique_contact_pairs": len(unique_pairs),
        "contact_episodes": len(contacts),
        "aggregate_pair_contact_hours": contact_minutes / 60,
        "assumptions": {
            "pair_interaction_rate_per_hour": PAIR_INTERACTION_RATE_PER_HOUR,
            "group_interaction_rate_per_hour": GROUP_INTERACTION_RATE_PER_HOUR,
            "work_world_interaction_rate_per_hour": WORK_WORLD_INTERACTION_RATE_PER_HOUR,
            "nonwork_world_interaction_rate_per_hour": NONWORK_WORLD_INTERACTION_RATE_PER_HOUR,
            "work_world_cognition_probability": WORK_WORLD_COGNITION_PROBABILITY,
            "nonwork_world_cognition_probability": NONWORK_WORLD_COGNITION_PROBABILITY,
            "pair_cognitive_turn_range": PAIR_COGNITIVE_TURN_RANGE,
            "group_cognitive_turn_range": GROUP_COGNITIVE_TURN_RANGE,
            "relationship_weight": RELATIONSHIP_WEIGHT,
        },
        "metrics": metrics,
    }

    with (output_dir / "summary.json").open("w", encoding="utf-8") as fh:
        json.dump(summary, fh, indent=2)
        fh.write("\n")

    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
