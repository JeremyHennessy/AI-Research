# Existing systems: lessons rather than recipes
**Research depth:** primary abstracts/official pages and a complete online review of Taylor (2015). Individual lab findings remain author-reported, not replicated in AI-Research.

## Timeline and mechanisms
| System / source | Substrate and minimal mechanism | What was actually demonstrated | What is **not** demonstrated |
|---|---|---|---|
| [Tierra — Ray 1991](https://tomray.me/pubs/index.html) | Self-copying instruction sequences in bounded virtual CPU/memory ecology; mutations and selection for computational resources | Digital evolution, parasites/cheating/ecological interactions in an instruction ecosystem | Unconstrained self-maintenance or indefinitely increasing functional sophistication |
| [Avida — Ofria & Wilke 2004](https://doi.org/10.1162/106454604773563612) | Virtual CPU programs copy genomes and compete under controlled resource/logic-task settings | Precise heritability, evolution and experiment reproducibility | That a logic task is *intrinsic* to an organism rather than a human-defined reward |
| [Evolution of complex features — Lenski et al. 2003](https://doi.org/10.1038/nature01568) | Avida lineages build up instructions supporting difficult logic operations | Mutational stepping stones and historical contingency can produce complex adaptive features in this substrate | General, sustained open-ended evolution or consciousness |
| [Lenia — Chan 2018/2019](https://arxiv.org/abs/1812.05433) | Continuous-valued spatial cellular automata with local convolution/growth laws | Diverse localized motile/persistent patterns | Genetic heredity, intrinsic metabolism, robust ecological evolution across one common physics |
| [Flow-Lenia 2023](https://arxiv.org/abs/2212.07906) | Mass-conservative local flow plus localized rule parameters | More discoverable localized patterns and common-world multi-species potential | Proof of natural-life-like open-ended evolution |
| [Flow-Lenia 2025](https://arxiv.org/abs/2506.08569) | Matter transport, embedded local parameters and evolution/activity probes | Authors report richer intrinsic evolutionary dynamics and multiple species in shared simulations | Indefinite innovation, metabolic closure, universal lifelike evolution |
| [Growing Neural Cellular Automata — 2020](https://doi.org/10.23915/distill.00023) | Same learned local update shared by cells; persistent/regenerating morphogenesis | Target-pattern growth and regeneration under training | A self-derived body target, genetics or reproduction arising without external loss |
| [Outlier binary CA — 2025](https://doi.org/10.1162/artl_a_00449) | An evolved binary local rule; sparse random initialization | Authors report emergent self-replicating forms at two scales | Sustained inheritance of *new capabilities* or open-ended complexity |
| [PBT–NCA — Berdica et al. 2026](https://arxiv.org/abs/2604.11248) | Population-based meta-optimization over neural cellular automata using novelty/diversity objectives | Authors report diverse self-organizing motifs and avoidance of frozen/noisy collapse | Intrinsic Darwinian open-endedness: external novelty/diversity pressure is explicitly imposed |
| [ASAL — Kumar et al. 2024](https://arxiv.org/abs/2412.17799) | Foundation-model evaluator searches across CA/Lenia/Boids and other substrates | Authors report broad automated discovery and novelty | Source of life-like agency *within* discovered pattern; human-aligned model scoring is not endogenous survival |
| [ASAL++ — Baid et al. 2025](https://arxiv.org/abs/2509.22447) | Foundation model proposes changing evolutionary targets from visual history | Improved visual novelty/coherence in studied Lenia search | That organism's goals originated internally without external planner |
| [POET — Wang et al. 2019](https://arxiv.org/abs/1901.01753) | Co-evolves learning environment challenges and corresponding policy solvers, transfers stepping stones | Complex/diverse skills emerge under coupled curriculum | A biological organism, metabolism or inherited reproduction |
| [Artificial chemistry — Liu & Sumpter 2018](https://doi.org/10.1074/jbc.RA118.003795) | Reaction network models conserving mass and accounting for kinetic/energetic constraints | Collective autocatalysis and self-replicating networks can arise in model universes | All necessary material cell properties, open-ended evolution, or real chemical origin-of-life replication |
| [GARD model — 2023](https://www.sciencedirect.com/science/article/pii/S2666386423001522) | Lipid/composition-based catalytic networks and reproduction attractors | Model links dynamic attractors and compositional self-reproduction | General evolvable genomes or unrestricted novelty |
| [OEE workshop — Taylor et al. 2016](https://doi.org/10.1162/ARTL_A_00210) | Cross-system theoretical comparison and research agenda | Multiple non-equivalent "open-endedness" definitions and hallmarks identified | A single agreed metric or universal recipe |
| [Taylor 2015 — full paper read](https://arxiv.org/abs/1507.07403) | Five conceptual requirements for open-ended dynamics | A detailed argument about reproduction, evolvability and ecological drive | Experimental proof those conditions are universally sufficient |

## What Tierra and Avida *did not* solve
They did not derive their computational physics from organisms. A virtual CPU instruction set, protected memory, insertion/reaper logic, scheduler, mutation distribution and resource economy are imposed by the designer. Taylor notes that write-protected individuals become isolated, limiting interaction possibilities, while the absence of endogenous degradation can make active repair unnecessary.

This is a major **tradeoff**: execution and protected memory make evolution measurable and reproducible; the same safeguards may suppress ecological interference, repair and the development of new organismal boundaries. **Hypothesis:** more permeable but noncatastrophically robust resource coupling may provide a new niche dimension. Test carefully with controlled damage and collapse, not by assuming unprotected memory is superior.

## Avida's strongest scientific value
The [2003 Nature experiment](https://doi.org/10.1038/nature01568) is important because complex logic functions appeared by cumulative lineage changes and historical stepping stones. It demonstrates evolutionary novelty in a *specified* instruction/reward landscape. It does not demonstrate that arbitrary cognitive tasks would emerge without those incentives, nor that the ecosystem will grow more complex forever.

Use Avida as a baseline for descent, recombination/variation, lineage tracking and ecological resource competition. Don't adopt logic-function bonus rewards in a new "intrinsic life" experiment without explicitly naming the intervention.

## Lenia: why appearances can be misleading
A moving localized structure can be a nonlinear attractor of a cellular rule. Motility and damage resilience may be emergent physical-like behavior, but unless heredity, boundary upkeep, energy/resource flow and adaptive selection are separately tested, calling it an independently evolving organism is premature. Many original Lenia "species" live under different parameter settings (worlds), preventing direct interaction without mechanisms such as Flow-Lenia's local parameters.

## Flow-Lenia: what changes technically
- **Matter conservation:** transport redistributes a constrained concentration rather than simply growing/clipping arbitrary amounts.
- **Affinity-gradient flow:** local convolution/growth fields guide movement together with concentration-driven diffusion; the update must numerically preserve total mass subject to boundary/transport conventions.
- **Parameter localization:** rule parameters become part of local dynamic state, allowing neighbors with distinct effective update laws to meet and interact.
- **Environmental extensions:** replenishing consumable resources and dissipation introduce endogenous costs, but *rates, resource definitions and physical laws* remain designer specified.
- **Empirical test:** compare Lenia and Flow-Lenia with identical initial-mass distributions and computational budgets; vary mass conservation, localized rules and resource dependence independently.

Source: [Flow-Lenia full public text](https://arxiv.org/abs/2506.08569); see [architecture comparison](03-architecture-comparison.md). Its publication reports evolutionary activity metrics, not a confirmed unlimited evolutionary engine.

## 2025–2026 discoveries to track *skeptically*
- **Outlier 2025** is especially valuable because it reports **emergent two-level self-replication** from a binary rule without engineering a dedicated large cellular state set; still need heredity and functionality controls.
- **PBT–NCA 2026** uses a composite externally imposed novelty/diversity driver. That is a worthy machine-search result, not a counterexample to the worry about scripted objectives.
- **ASAL/ASAL++** explore discovery by vision-language models. Even if visual novelty continues for many frames, the image embedding/target proposal can be biased to what humans consider interesting.
- **Cultural open-endedness** is a [proposed alternative](https://arxiv.org/abs/2203.13050) to exclusively genetic evolution; information may transmit horizontally and cumulatively, but culturally copied instructions do not alone create self-maintaining organisms.

## Historical negative or limiting evidence
- [Standish 2002](https://arxiv.org/abs/nlin/0210027) reports that a size-neutral Tierra run produced organism growth in length **without corresponding growth in his complexity measure**.
- [Open-Endedness for the Sake of Open-Endedness, 2019](https://doi.org/10.1162/artl_a_00289) argues simplistic evolving systems can satisfy formal OEE definitions while lacking biological richness: labels must be backed by meaningful functional diversity.
- [OEE York workshop 2016](https://doi.org/10.1162/ARTL_A_00210) stresses pluralism: ongoing adaptation, evolutionary innovation, increased maximum complexity and major transitions are distinct metrics.
- [2026 PBT–NCA](https://arxiv.org/abs/2604.11248) explicitly describes sensitivity and collapse into frozen or noisy regimes, motivating an **externally specified** objective—not a solution to all intrinsic-selection problems.

## Source fidelity
For each historical system capture exact implementation revision and data/software license before running any old code. The literature above is a selected corpus; there is no independent reproduction or live world execution in this repository. Follow [primary source bibliography](08-source-bibliography.md).
