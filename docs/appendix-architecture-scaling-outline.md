# Appendix — Scaling and Deployment of the Enclave Architecture

> **Working appendix outline.** These regional, persistent-world and full-world simulation topics were relocated from the former §§16.6–16.8 so §16 can focus on implementation levels and their measured/modelled requirements. The full appendix has not been drafted.

## Regional Simulation

- High-fidelity simulation can be limited to:
  - active regions;
  - important Actors;
  - nearby Enclaves;
  - narratively relevant systems.
- Distant or inactive areas may use:
  - compressed simulation;
  - deterministic schedules;
  - aggregate state;
  - event-triggered reactivation.
- The same principle already appears in miniature in §14: only the handful of Actors capable of changing the immediate narrative require full cognitive treatment.
- This allows much of the benefit of a persistent world without the full cost of §15's upper-bound scenario.

## Persistent Online Worlds

- MMO and shared-world applications can use Enclave to preserve:
  - world history;
  - faction state;
  - Actor memory;
  - information diffusion;
  - consequences of Participant activity;
  - changing authored conditions.
- The causal pattern demonstrated by the §14 adventures remains the same even when many Participants encounter the world at different times.
- Different Participants may encounter different informational perspectives on the same shared canonical world.

## Full-World Simulation

- The *Free Guy*-style simulation explored in §15 should be treated as the extreme endpoint of a fidelity spectrum rather than the default target.
- Practical implementations can occupy any point between:
  - conventional scripted interaction;
  - persistent reactive characters;
  - faction-scale simulation;
  - regional simulation;
  - persistent world simulation;
  - full-world Cognitive Actor simulation.
- The same primitive architecture demonstrated in §14 can support each level while changing the amount of computation devoted to individual Actors and world regions.

---
