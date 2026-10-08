# Architecture-independent comparison: five possible computational foundations
**Each option is a future experimental hypothesis, not approval to create a digital organism.** The key is to preserve fundamentally different primitives and compare them under meaningful equivalent resource budgets—not to assemble all five into an LLM framework.

## Architecture A — Artificial chemistry with self-maintaining compartments
**Computational substrate:** finite stoichiometric reaction network, spatial diffusion, reaction kinetics, explicit resource/energy inputs, product waste and decay. Optional boundary components are synthesized through internal reactions rather than guaranteed by engine.

1. **Origin:** random or chemically motivated reaction universe; no finished metabolic circuit seeded in the strongest origin-of-organization test.
2. **Persistence:** reaction flux must offset constituent/boundary breakdown under resource constraints.
3. **Environment/resources:** reaction substrate availability, flow, gradients and consumption of high-energy reactants; track conservation.
4. **Lifetime change:** compositional shifts, autocatalytic reorganizations, repair, compartment division; no language model required.
5. **Reproduction/inheritance:** daughter network composition, catalytic organization and possibly template polymers; distinguish compositional resemblance from stable heritable functional variation.
6. **Novelty route:** new autocatalytic subsets, resource conversion, coupled metabolic pathways, selective compartments.
7. **Bottlenecks:** genotype fidelity and loss of acquired function across divisions, engineered reaction topology, computational stiffness, unclear individual boundaries.
8. **Feasibility:** small abstract discrete stochastic reaction models are low-compute; chemically faithful simulations require substantial domain expertise.

Evidence: [Liu & Sumpter 2018](https://doi.org/10.1074/jbc.RA118.003795), [Synthetic protocell biology](https://pmc.ncbi.nlm.nih.gov/articles/PMC2442389/), [GARD compositional replication](https://www.sciencedirect.com/science/article/pii/S2666386423001522). **Avoid claiming biochemical metabolism** when resources are digital counters or reactions are abstract.

**Crucial falsifier:** if compartment repair and inheritance persist just as often after breaking internal reaction feedback loops, apparent autopoiesis came from engine-level rules instead of self-organization.

## Architecture B — Instruction-based digital evolutionary ecology
**Substrate:** programs in a sandboxed virtual instruction set, bounded memory/compute/space, lineage copying, mutation and environmental resource interactions (Tierra/Avida family).

1. **Origin:** seed minimal replicator or search for a replicator; explicitly differentiate the two.
2. **Persistence:** execution resources and allocated memory; require reproduction before decay/replacement.
3. **Environment/resources:** CPU quota, memory, multiple resources, competition, byproducts, ecology and migration.
4. **Lifetime change:** optional mutable local memory and computation; baseline often has little within-lifetime learned policy.
5. **Reproduction/inheritance:** executed copy loops and occasional mutation, insertions/deletions or recombination.
6. **Novelty route:** new instruction sequences, ecological strategies, novel niche creation, host/parasite/cross-feeding and modular cooperation.
7. **Bottlenecks:** hard-coded virtual CPU, protected memory, narrow instructions, fitness/task rewards, complex instruction genotype fragility.
8. **Feasibility:** CPU-friendly at small population/world sizes; longer evolutionary generations may be needed to distinguish drift from adaptation.

Evidence: [Ray Tierra](https://tomray.me/pubs/index.html), [Ofria/Wilke Avida](https://doi.org/10.1162/106454604773563612), [Lenski et al.](https://doi.org/10.1038/nature01568), [Taylor's critique](https://arxiv.org/abs/1507.07403).

**Crucial falsifier:** evolved "intelligence" disappears when the external reward for human-designed logic tasks is removed while maintaining comparable survival opportunities.

## Architecture C — Conservative spatial fields / continuous cellular life
**Substrate:** continuously valued cell fields, local kernels, gradients, transport, field mass conservation, spatially localized parameter variation (Lenia/Flow-Lenia).

1. **Origin:** random spatial conditions + fixed local physics; patterns emerge as attractors.
2. **Persistence:** nonlinear maintenance of localized field distribution, possible repair under perturbation.
3. **Resources:** mass-conserving transport, injected food field and dissipation in variants, spatial availability and competition.
4. **Lifetime change:** shape transformation, motility, fusion/fission, local parameter/state adaptation.
5. **Reproduction/inheritance:** splitting patterns can appear, but heritable unit identity, genotype/phenotype and variation **must be measured**.
6. **Novelty route:** distinct local rules, multi-species interaction, ecological niche construction and stable new morphologies.
7. **Bottlenecks:** phenotypes tied to manually selected kernels, beauty ≠ function, missing hereditary lineage, fragile mass bookkeeping and boundary/individual tracking.
8. **Feasibility:** small grids on CPU/GPU, convolution/transport costs increase with field size and precision.

Evidence: [Chan Lenia](https://arxiv.org/abs/1812.05433), [Flow-Lenia 2023](https://arxiv.org/abs/2212.07906), [Flow-Lenia 2025](https://arxiv.org/abs/2506.08569), [Outlier 2025](https://doi.org/10.1162/artl_a_00449).

**Crucial falsifier:** if patterns are stable but cannot pass new repair/lineage/resource-adaptation tests beyond an identical fixed-rule attractor, there is no demonstrated new organismal evolution.

## Architecture D — Developmental/neural cellular automaton
**Substrate:** local neural-update function shared by cells, hidden cell-state channels and local communication; recurrent growth and regeneration. This explicitly allows learned rules, but the architecture itself could be neural or non-neural.

1. **Origin:** random cells/policies or trained update rule; record any predefined target morphology or hidden reward.
2. **Persistence:** distributed state transitions preserve/rebuild pattern after cell removal.
3. **Resources:** optional explicit chemical/energy fields, growth/decay cost.
4. **Lifetime change:** recurrent cell state, plasticity, developmental feedback and repair.
5. **Reproduction/inheritance:** transfer learned rule parameter(s) or growing cell constituents; distinguish weight-copy API from biological analog of inheritance.
6. **Novelty route:** developmental plasticity, modular tissues, morphological/behavioral selection, local evolution of rule parameters.
7. **Bottlenecks:** fixed differentiable image target, externally optimized parameter search, unstable gradients, collapse to frozen/noisy state, missing reproductive lineage.
8. **Feasibility:** small local CNN-like rules and 2D worlds feasible on consumer GPUs; manual no-LM controls on CPU.

Evidence: [Growing NCA](https://doi.org/10.23915/distill.00023), [PBT–NCA 2026](https://arxiv.org/abs/2604.11248).

**Crucial falsifier:** regeneration only works for the specifically trained image or damage pattern; under hidden perturbations, a fixed NCA fails despite visually impressive demos.

## Architecture E — Co-evolving organism/environment niches
**Substrate:** populations of environment generators/constraints and populations of organisms/learners that modify each other's success landscape. POET supplies a concrete stepping-stone method; ordinary models may or may not use genetics.

1. **Origin:** paired seeds for body/policy and environment; strictly define which aspects are *externally designed*.
2. **Persistence:** viability within evolving resource/habitat conditions, not a human-selected single finish line.
3. **Environment/resources:** environment mutation, migration, biotic competition, changing food/cost/physics niches.
4. **Lifetime change:** learning or structural regulation in particular habitats.
5. **Reproduction/inheritance:** only if the organisms possess an actual inherited replicative process; POET's policy optimization is **not** equivalent.
6. **Novelty route:** ecological niche generation, escalating interactions, transfer between niches, functional/organizational transitions.
7. **Bottlenecks:** novelty as reward, environment drift beyond solveability, degenerate arms races, solver overfitting, arbitrary curricula.
8. **Feasibility:** toy procedural environments and simple optimizers can be low compute; evaluation of true independence/novelty is harder.

Evidence: [POET](https://arxiv.org/abs/1901.01753), [ASAL](https://arxiv.org/abs/2412.17799), [ASAL++](https://arxiv.org/abs/2509.22447), [Niche/ecology in Avida](https://www.frontiersin.org/journals/ecology-and-evolution/articles/10.3389/fevo.2021.750779/full).

**Crucial falsifier:** apparent progression collapses after removing human-written complexity/visual reward while preserving feasible selection conditions.

## Comparison before experimental authorization

| Question | A chemistry | B programs | C fields | D NCA | E co-evolving niches |
|---|---|---|---|---|---|
| Self-maintaining boundary plausible? | Strong conceptual path, costly | Often weak/engine-protected | Spatial localized, not necessarily active upkeep | Learned regeneration; target-dependent | Depends on body substrate |
| Inherited information natural? | Challenging compositional/template | Strong | Often unclear | Only with explicit inheritance design | Requires separate substrate |
| Ecological relations possible? | Chemical exchange | Yes; memory/CPU constraints | Yes via overlapping fields | Yes, if rule/media allows | Central |
| Unscripted emergent target? | Viability constraints | Can avoid task bonuses | Can avoid aesthetic fitness | Training loss often externally specified | Often explicit novelty/curriculum |
| Low-resource initial experiment? | Discrete reactions yes | Yes, CPU | Yes, small field | Yes, small model | Yes, toy worlds |
| Key blind spot | Fidelity of organization/inheritance | Predefined ISA and protected CPU | No robust genotype/phenotype | Human-specified training targets | External novelty mechanism |

**Research-only recommendation:** do **not** select a winner now. The best first comparison should hold budget constant and apply **the same operational tests** (persistence, repair, lineage, adaptation, new functions) while preserving each substrate's distinct primitives. A system may satisfy only a subset; count that explicitly rather than combining unrelated metrics into a magical "alive" score.
