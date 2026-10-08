# Emergence and evolutionary stagnation: mechanisms, confounders, failures

**Do not optimize a simulation for appearing alive.** The question is whether general local constraints are sufficient for continued novel, self-maintaining organization—and why many historical substrates fail.

## 1. Emergence requires a causal question
A global pattern is *weakly emergent* in a descriptive sense when it arises from many interacting local rules and is not obvious from an individual rule. This does not imply life, intelligence, mind, autonomous evolution, or a new causal law.

Stronger claims should pass:
- **Perturbation:** change local elements and watch whether larger organization repairs or fails.
- **Intervention on mechanism:** break presumed repair/replication/transport process and test predicted loss.
- **Novel environment:** change resource gradients, topology, contact partners or disturbances not selected during tuning.
- **Designer-ablation:** remove specialized reward or externally scheduled "life" cues.
- **Competing null:** compare inert attractors, random physical systems, replayed rules, and externally reset animations.

Read [Emergence in Artificial Life](https://doi.org/10.1162/artl_a_00397), [Taylor's five OEE requirements](https://arxiv.org/abs/1507.07403), [Workshop pluralism](https://doi.org/10.1162/ARTL_A_00210).

## 2. Important design decisions and the false claims they can produce

| Designer decision | Why it may help | What it can accidentally script | Proposed ablation |
|---|---|---|---|
| Seed a viable replicator | Allows experiments on inheritance immediately | Implies an origin-of-replication mechanism exists | Random seeds; separately study probability of spontaneous origin |
| Protected memory / engine respawn | Prevents catastrophic death | Eliminates need for endogenous repair | Memory interference/damage variants with safety bounds |
| Fixed per-step energy bonus | Prevents trivial collapse | Artificially grants metabolic maintenance | Conservation with decay/throughput accounting |
| Image resemblance loss | Produces graceful morphologies | Hardcodes a "creature" body | Remove image loss; test alternate hidden morphologies |
| Logic-task CPU rewards | Evolves useful computation | Predefines intelligent task demands | Unrewarded viability niches and alternative task families |
| Global hand-selected mutation rate | Controls exploration | Conceals evolvability of heredity | Evolving/mixed rates and matched mutation-budget controls |
| Top-down complexity score | Drives visible novelty | Exploits scoring function; selects only expected forms | Zero weight, blind evaluator, independent novelty definitions |
| Engine enforces individual boundaries | Makes counting easy | Predefines identity/immune system | Dynamically discovered boundaries with split/merge ambiguity |
| Finite action/interaction set | Makes worlds practical | Fixes sensorimotor evolution's upper bound | Nested/new compound actions vs static affordances |
| Forced resource replenishment | Sustains runs | Artificial niche cycling | Compare constant, seasonally forced, and organism-modified supply |
| Automatic archive injection | Prevents extinct lineages staying extinct | Separates apparent continual novelty from biology-like dynamics | No-archive reintroduction condition |

**The challenge isn't to eliminate design:** every computational substrate has rules. It is to identify which rules produce unexpected *functional* outcomes without encoding their detailed solutions.

## 3. Scientific bottleneck inventory
| Bottleneck | Candidate reason | Prior research strategy | Strength of evidence | What would falsify the explanation? |
|---|---|---|---|---|
| B01 Stagnation | Viable mutations lead to dead ends, poor locality between genotype and function | [Taylor 2015](https://arxiv.org/abs/1507.07403), mutation path analysis, neutral networks | Theory/synthesis | Comparable landscapes with viable pathways stagnate equally |
| B02 No true ecological novelty | Isolation / protected memory / single resource removes niche opportunities | [Digital evolution ecology review](https://www.frontiersin.org/journals/ecology-and-evolution/articles/10.3389/fevo.2021.750779/full) | Published reviews and model studies | Resource-exchange/biotic interventions do not alter adaptation |
| B03 Fragile self-maintenance | No endogenous repair, excessive disruptive interference | [Taylor 2015](https://arxiv.org/abs/1507.07403), [NCA repair](https://doi.org/10.23915/distill.00023) | Hypothesis and supervised repair demonstrations | Robust recovery under hidden perturbations without designer repair |
| B04 No robust heritability | Phenotype varies but descendants do not retain viable innovations | [Avida](https://doi.org/10.1162/106454604773563612), [Flow-Lenia](https://arxiv.org/abs/2506.08569) | Solid inheritance in digital programs; speculative in free-form fields | Controlled cross-generation trait fidelity remains at chance |
| B05 Complexity ceiling | Fixed instruction set or predefined genotype→phenotype mapping restricts new parts | [Major transitions](https://doi.org/10.1038/374227a0), [Taylor 2015](https://arxiv.org/abs/1507.07403) | Evolutionary theory; system-specific caveat | Hierarchical capabilities continue emerging with static encoding |
| B06 Collapse / extinction | Resource scarcity, mutation load, weak ecological buffering | [Avida ecology](https://www.frontiersin.org/journals/ecology-and-evolution/articles/10.3389/fevo.2021.750779/full), [PBT-NCA](https://arxiv.org/abs/2604.11248) | Published simulations with different controls | Stable populations survive perturbations with minimal buffering |
| B07 Visual novelty only | Variation lies in aesthetics or encoding not useful new function | [ASAL](https://arxiv.org/abs/2412.17799), [OEE critique 2019](https://doi.org/10.1162/artl_a_00289) | Published positive search and conceptual counterexample | Novel forms also acquire reproducible new counterfactual functions |
| B08 No learning selection | Lifetime plasticity incurs costs without future benefit | [Active inference](https://arxiv.org/abs/2002.12636), [EWC](https://arxiv.org/abs/1612.00796) | Indirect / cross-domain | Plastic lineages outcompete fixed ones on changing unseen hazards |
| B09 Shared-world impossibility | Different rules define isolated physics and prevent competition | [Flow-Lenia](https://arxiv.org/abs/2212.07906) | Paper-reported partial solution | Coexisting local rules fail to interact under changed resource regimes |
| B10 Coevolutionary stasis | Predation/competition oscillations with no escalating function | [POET](https://arxiv.org/abs/1901.01753), [York OEE](https://doi.org/10.1162/ARTL_A_00210) | Proposed mechanism, limited transfer | Ecological novelty persists once special complexity bonus removed |
| B11 Metrics are gameable | Novelty/complexity evaluator can be exploited or arbitrarily saturated | [OEE critique](https://doi.org/10.1162/artl_a_00289), [PBT-NCA](https://arxiv.org/abs/2604.11248) | Strong methodological concern | Independent function tests rise with novelty score under blind conditions |
| B12 Computing budget | Small finite worlds saturate possible interactions | [Taylor 2015](https://arxiv.org/abs/1507.07403) | Logical constraint, not sole explanation | Larger budgets alone reproduce robust innovation across seeds |

### Major correction to a common intuition
Evolution by natural selection does **not** intrinsically seek maximal intelligence or structural complexity. [Szathmáry and Maynard Smith (1995)](https://doi.org/10.1038/374227a0) explicitly caution against assuming universal complexity increase. Simpler lineages can survive better. The relevant question is *under what selectable conditions* sensing, memory and cognition become useful rather than costly.

## 4. Openness versus mechanisms: do not equate infinite time and OEE
At least five observational endpoints are separable:
1. Sustained **population turnover**.
2. Cumulative **adaptive innovations** with controls for neutral drift.
3. Increased **functional repertoire** and ability to exploit unseen resources or environments.
4. Evolved **new levels of individuality**, such as stable symbiosis/group reproduction.
5. Changed **evolvability**—new mechanisms of heredity, development, variation and discovery.

A system that oscillates or produces fractally complex visuals can satisfy (1) but not (2–5). A system with scripted novelty rewards may satisfy (2) or (3) only when driven by its designer. Different OEE researchers disagree on what is necessary; define each endpoint before measuring.

## 5. Ecological intervention matrix
**Factorial future study:**
- Resource diversity: one vs multiple nutrients with byproducts.
- Heterogeneity: homogeneous world vs spatial patches.
- Competition: alone, competition, cross-feeding, predator/parasite analogues.
- Variability: static vs stochastic seasons vs organism-caused change.
- Heritable organization: frozen rules vs parameters transmitted locally vs evolutionary programs.
- Development: fixed body vs constituent replacement and repair.

For each condition measure survival, persistence, diversity, new functional affordances, lineage branching, and ability to recover from disturbances. Track random extinctions and degenerate resource cycles, and control for total physical and compute budget.

**Caution:** adding complexity to the environment can produce visually interesting trajectories without increasing the organism's learned causal/behavioral competencies.

## 6. Emerging cross-disciplinary connection
A low-dimensional self-maintaining body might acquire **useful predictive memory** through selection if environmental survival depends on delayed information and repeated perturbations. This links:
- [autopoiesis](https://doi.org/10.1016/0303-2647(74)90031-8),
- [ecological evolutionary niches](https://www.frontiersin.org/journals/ecology-and-evolution/articles/10.3389/fevo.2021.750779/full),
- [active inference/exploration](https://arxiv.org/abs/2002.12636),
- [long-term memory benchmarks](../13-memory-world.md).

**Unverified hypothesis:** such ecological selection could favor increasingly predictive internal states *without predefined human tasks*. Falsify by showing the same "memory" under shuffled cues, or that delayed information does not improve viability. Avoid calling a predictive process conscious.
