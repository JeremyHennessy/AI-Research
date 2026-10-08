# New counterexamples and measurement challenges: 2025–2026 research

**2026-10-08 | Primary-source review at E1 only.** This review combines official publication abstracts/pages and an institution's ALIFE 2026 conference record. It does **not** claim the complete methods, supplementary appendices, or underlying experiments have been independently replicated.

## 1. ToLSim: one unbounded-looking statistic, other hallmarks stagnant

**Paper:** Théo de Pinho and Lana Sinapayen, [*A speciation simulation that partly passes open-endedness tests*](https://arxiv.org/abs/2603.01701) (March 2026, arXiv:2603.01701).

**Authors' investigated construct:** *Tree of Life Simulation* (ToLSim) with components defined as individual genes, analyzed using evolutionary activity statistics for **Tokyo type-1 open-ended evolution** (T1 OEE).

**Abstract-level result:** authors report an **unbounded total cumulative evolutionary activity statistic**, but **bounded total and median normalized cumulative activity** and **persistently zero new evolutionary activity**, leading them to conclude that the model does **not** pass the considered open-endedness criterion. They explicitly propose redoing the analysis with *individuals or species rather than genes* as components.

**Do not overgeneralize:** "unbounded" here is the authors' statistical interpretation from a finite or model-based observation; it does not prove infinite time. Changing the unit of analysis changes the measured property and may change the verdict. The authors' own conclusion is conditional on chosen OEE definition and component identity.

**Actionable consequence:** preregister open-ended metrics at gene, individual, species, **and functional-organizational process** levels if they can be identified independently, and calculate rates over multiple held-out windows. Require agreement with measured new niche functions and lineage transfer; reject a single summary index as "life achieved."

## 2. ALIFE 2026: macro-level NCA order need not reveal micro-level complexity

**Paper:** James Stovold, Mia-Katrin Kvalsund, Michael Ludwig, Varun Sharma, Alexander Mordvintsev, [*Visualising the Attractor Landscape of Neural Cellular Automata*](https://doi.org/10.1162/ISAL.a.952) (ALIFE 2026, Waterloo, August 17, 2026). [Author institution's archival entry](https://repositum.tuwien.at/handle/20.500.12708/231190).

**Authors' methods in the abstract:** PCA, dense and sparse autoencoders, topological data analysis/persistent homology, applied to neural CA dynamic states.

**Authors' finding:** whole-NCA *macroscopic* state attractors can have relatively simple low-dimensional structure, while local *cell-level* states often show a more complex manifold requiring richer methods.

**Not proven:** that microscopically intricate state trajectories correspond to independently meaningful biology, memory, functional cognition, or individuals. A complex manifold is a property of the chosen state representation and estimator.

**Research discriminator:** estimate complexity at spatial/cellular scales and at the level of causal processes. Use held-out trajectories, fixed measurement bandwidth, periodic oscillator controls, and targeted interventions on proposed information-bearing states. Ask whether that complexity improves **predictions of repair, viability or lineage innovation**.

## 3. A review clarifying reproduction versus replication

**Paper:** Hiroki Sayama and Chrystopher L. Nehaniv, [*Self-Reproduction and Evolution in Cellular Automata: 25 Years After Evoloops*](https://doi.org/10.1162/artl_a_00451), *Artificial Life* 31(1), 81–95 (2025). 

**Conceptual distinction drawn by authors:** one can obtain self-copying patterns without the broader forms of self-reproduction necessary for heritable nontrivial variation. Under the more demanding **von Neumann criterion**, reliable inheritance with structural variation matters; **Langton-style loops** represent another constructive criterion and may not satisfy the stronger one.

**Research consequence:** future "offspring" recognition needs a **typed transmission channel**, mutations that alter organization/function in descendants, and checks that those variants remain viable. Engine-level copy APIs and reproducing images should be scored separately.

## 4. Autopoiesis origins: a glider isn't a membrane-bound cell

**Paper:** Randall D. Beer, [*An Investigation into the Origin of Autopoiesis*](https://doi.org/10.1162/artl_a_00307), *Artificial Life* 26(1), 5–22 (2020). 

**Author's actual scope:** Game of Life gliders are treated as **toy** bounded persistent entities. Statistical mechanics relates the number of gliders in random initial grids to processes of creation, persistence and destruction; the article explicitly frames this as development of conceptual tools for *organization-first* origin-of-life research.

**Key boundary:** a Game of Life glider's self-producing organization is an **interpretive model**; the work does not show molecular metabolism, true heritable genomes or sentient identity.

**Discriminator:** jointly measure process dependency networks and response to targeted deletion of a process component. Compare with passive gliders, oscillators and self-assembling but non-reproducing structures. Note that the *model physics* itself determines what gliders are possible.

## 5. Inheritance can suffer error catastrophe

**Paper:** Doron Segré, Barak Shenhav, Ron Kafri, Doron Lancet, [*The molecular roots of compositional inheritance*](https://doi.org/10.1006/jtbi.2001.2440), *Journal of Theoretical Biology* 213(3), 481–491 (2001).

**Primary abstract finding:** fidelity of compositional inheritance in GARD-like molecular assembly models depends on distribution of catalytic rate enhancements and assembly size. For particular **normal-distributed** catalytic accelerations, the authors report frequent "compositional error catastrophes" making compositional information transfer impossible; a suitable lognormal distribution yields high fidelity in their studied model.

**Limitation:** model- and parameter-dependent theoretical/simulation finding, not empirical proof that living cells require such a distribution or that digital heredity can be made reliable by copying its exact distribution.

**Discriminator:** compare parent/offspring genotype/organizational fidelity across wide catalytic coefficient distributions, assembly sizes and environmental noise; hold mutation/opportunity budget fixed. If "offspring" only resemble parents because they share an imposed medium, actual heredity is unproven.

## 6. Extinction under environmental disruption deserves equal attention

**Paper:** Hanna Derets and Chrystopher L. Nehaniv, [*Survival and Evolutionary Adaptation of Populations Under Disruptive Habitat Change: A Study With Darwinian Cellular Automata*](https://doi.org/10.1162/artl_a_00457), *Artificial Life* 31(1), 106–123 (2025).

**Abstract-level study:** spatial probabilistic cellular ecology with genetic-algorithm-like mutation/selection and locally degrading resources; investigates parameter thresholds separating adaptation/survival from extinction. Source describes an available open-source implementation, **not inspected in this research pass**.

**Research consequence:** study **failure regions** (resource scarcity, habitat fragmentation, spatial isolation and mutation load), not just parameter combinations where interesting populations survive. Do not secretly stabilize the environment for preferred lineages through repeated replenishment or rescue logic.

## 7. Neural self-application fixpoints are not a complete organism

**Paper:** Thomas Gabor et al., [*Self-Replication in Neural Networks*](https://doi.org/10.1162/artl_a_00359), *Artificial Life* 28(2), 205–223 (2022).

**Author's mechanism:** neural networks output or transform other networks' weights; self-application can produce fixed points, while self-training and artificial "network soups" introduce additional dynamics. Article studies noise resilience.

**Critical alternative explanation:** a mathematical **fixed point** is not by itself heritable adaptive reproduction. Weight equality `N = N◁N` does not imply a distinct resource-dependent daughter that persists and evolves. This is useful as a null example to protect against overcounting digital self-replication.

**Discriminator:** independently instantiated daughter with viability cost, mutation/heredity, and useful new functions on hidden challenges, compared against static fixed-point equations.

## 8. Cross-paper lesson: a ladder of stronger claims
1. Spatial pattern or statistical attractor.
2. Repeated/durable pattern.
3. Internally maintained organization with resource-dependent causal repair.
4. Distinct descendant process with informational inheritance.
5. Adaptation and new heritable functions under ecology.
6. Continued functional/organizational novelty across long windows.

**A system can qualify at one level while failing higher levels; none proves consciousness.**

### What we have not verified
The ToLSim full method, ALIFE 2026 NCA implementation, GARD distributions, and remaining primary papers are E1 metadata/abstract review. No independent run, code execution, simulator, organism or statistically replicated negative result is claimed. Sources may warrant paper-version/license and supplementary audits.
