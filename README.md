# Enclave

**Enclave** is a theoretical architectural framework for reactive actor branching narrative in interactive media.

The central idea is to preserve human authorship while allowing narrative actors to respond dynamically to player actions without requiring authors to manually enumerate every possible dialogue branch or consequence.

The framework separates several responsibilities that generative narrative systems often collapse together:

- **authorial intent** — the world, actors, conflicts, goals, constraints, intended trajectories, and acceptable outcomes;
- **authoritative world state** — what exists, what has actually happened, and which actions or objects are real in the simulation;
- **actor memory and cognition** — the observations, communications, experiences, and conclusions retained by each individual actor;
- **provenance and communication** — the causal paths by which claims are created, recorded, transmitted, transformed, and encountered;
- **event validation** — the boundary that decides whether proposed actions can become authoritative consequences;
- **reactive actors** — actors that respond from their own circumstances, memories, goals, and relationships rather than omniscient world state;
- **selective inference** — language models, decision models, retrieval, and other probabilistic systems used where they add value rather than as the authority over narrative reality.

Enclaves constrain the relationships and channels through which actors can perceive events, communicate, and access records. A statement, rumour, letter, or broadcast can be a real event or object in the world without its contents being true. When an actor encounters one, that encounter becomes part of the actor's own history; later belief and action can develop from that history without creating a separate global information reality.

Actors are intended to be **event-activated rather than continuously simulated**. Background populations can remain aggregate or dormant, while important actors can use progressively richer decision and language systems when an event actually requires them to react.

The design paper is in [docs/design-paper.md](docs/design-paper.md).

## Core proposition

> Authors create the narrative. Actors disrupt it. Events make those disruptions consequential. The system makes the authored world capable of responding.

This repository currently contains the architectural paper only. It is not an implementation specification or production-ready system design.

## Public research snapshot

This public repository contains the paper, working outlines, supporting calculations, research summaries, and reproducible simulation scripts. The local development repository also retains raw benchmark archives, which are not redistributed here, and a third-party reference PDF, which remains available from its original publisher.
