# Addendum B — Combinatorial Enclaves, Inheritance, and Computational Reduction

> **Working outline.** This addendum formalizes the combinatorial problem introduced by Combinatorial Enclaves and explores hierarchy-aware strategies for preserving semantic combination depth without brute-force population computation.

## B.1 Why Combinatorial Enclaves Exist

- Actors may belong to multiple Enclaves simultaneously.
- Narratively useful populations often arise from intersections rather than one Enclave alone.
- Examples:
  - `Intelligence + NorthernCommand`;
  - `Intelligence + VancouverIsland`;
  - role + region + institution combinations.
- These intersections should remain semantically addressable even when they resolve to populations already implied by hierarchy.

## B.2 Worst-Case Combination Space

For `n` independently combinable Enclaves, the number of non-empty subset identities is:

```text
2^n - 1
```

This growth is exponential.

Important distinction:

> **Combinatorial identity is cheap; population intersection is expensive.**

The architecture should preserve valid semantic identities without blindly materializing every population intersection.

## B.3 Inheritance

Inheritance provides parent-child implication.

Example:

```text
Military -> Army
Army -> Intelligence
Army -> NorthernCommand
```

If an Actor belongs to `Intelligence`, it also belongs to `Army` and `Military`.

Inheritance is transitive.

## B.4 Semantic Identity Must Not Collapse

Even when hierarchy implies equivalent populations, distinct combination identities remain valid.

For example:

- `Intelligence`;
- `Army + Intelligence`;
- `Military + Intelligence`;
- `Military + Army + Intelligence`;

may all resolve to the same Actor population while remaining distinct semantic/addressable identities.

Implementation may alias them to the same population representation.

## B.5 Example Reduction

With:

- Military;
- Army;
- Intelligence;
- NorthernCommand;

there are fifteen possible non-empty combination identities.

Because of Inheritance, many combinations require no new population calculation.

Distinct population sets may collapse primarily to:

- Military;
- Army;
- Intelligence;
- NorthernCommand;
- Intelligence ∩ NorthernCommand.

The exact count depends on the hierarchy and real memberships.

The point is not that Inheritance guarantees one fixed reduction factor; it removes redundant population work implied by known hierarchy.

## B.6 Actor-Derived Enumeration

Preferred strategy:

- derive relevant Combinatorial Enclave vocabulary from actual Actor memberships;
- avoid asking each Fact to enumerate the entire Enclave power set;
- normalize combination ordering so equivalent identities resolve canonically;
- index valid combinations for reuse by Facts, retrieval, Saturation, and access logic.

This preserves useful combinations that actually occur in the world without requiring global brute-force generation.

## B.7 Skip-Generation Combinations

Transitive Inheritance means combinations need not explicitly contain every ancestor.

Example:

`Military + Intelligence`

remains a valid identity even though `Intelligence` already implies `Army` and `Military`.

Ancestor closure can determine population equivalence without deleting semantic identity.

## B.8 Facets and Comparison Scope

Facets can help identify meaningful multi-hierarchy entity contexts.

They may reduce pointless comparison by grouping independent Enclave hierarchies around an identifiable entity.

However, Facets should not be treated as an absolute prohibition on cross-Facet combinations if a cross-context intersection is semantically meaningful.

The exact comparison/indexing policy is implementation-dependent.

## B.9 Concurrency and Practical Thresholds

Concurrency can accelerate population-intersection work, but it does not change the exponential worst-case identity space.

Practical implementations should prefer algorithmic reduction before relying on parallel brute force.

Earlier design discussion considered keeping directly compared Enclave sets relatively small (preferably under roughly twenty, certainly avoiding unconstrained large power sets), but this is an engineering heuristic rather than a theoretical limit.

Any numerical threshold should be benchmarked against:

- Actor population size;
- representation;
- indexing strategy;
- hardware;
- hierarchy density;
- caching;
- update frequency.

## B.10 Interaction With Saturation

Saturation may be evaluated against increasingly broad Combinatorial Enclaves.

Efficient population resolution therefore matters directly to institutional diffusion.

A system should be able to ask:

- what is the relevant population for this Combinatorial Enclave?
- how many members currently possess this Fact?
- has the Saturation Threshold been reached?

without rebuilding every intersection from scratch.

## B.11 Formalization Tasks

Future formal treatment should examine:

- canonical combination identity;
- ancestor closure;
- population-equivalence classes;
- deduplicated population representation;
- incremental updates when Actor membership changes;
- cache invalidation;
- sparse vs dense hierarchy behavior;
- worst-case and typical-case bounds;
- Actor-derived enumeration algorithms;
- indexing strategies;
- concurrency/parallel evaluation;
- benchmark methodology.

## B.12 Scope Boundary

This addendum should formalize computation without changing the ontology.

Section 10 defines what Combinatorial Enclaves and Inheritance **mean**.

Addendum B explains how an implementation might make them computationally tractable.
