# Pass 13 primary full-paper review — 2023 first-daughter exception and septin permeability

**2026-10-08 | E2 full primary open article, Figures 1–5, quantified results, methods and limits reviewed; no independent experiment.**

**Source:** Fozia Akhtar, Bastien Brignola, Fabrice Caudron (2023). *Septin Defects Favour Symmetric Inheritance of the Budding Yeast Deceptive Courtship Memory*. International Journal of Molecular Sciences **24**(3):3003. DOI [10.3390/ijms24033003](https://doi.org/10.3390/ijms24033003), [complete PMC full article](https://pmc.ncbi.nlm.nih.gov/articles/PMC9917509/). CC BY 4.0 text. **Research-only**; original biological experiments not repeated, data/code not downloaded.

## Why this follow-up matters

The 2013 and 2022 Whi3 work often gets oversimplified as: "yeast mothers remember, daughters never inherit." The real biology has a **temporally bounded exception**: the first daughter after an escaped mating attempt can inherit refractoriness in nearly half of WT births, with much less frequent inheritance in later daughters. This paper links that nontrivial pattern to **abnormal first division, septin localization, and weakened ER diffusion barrier**, rather than a static binary rule.

The study is a **follow-up by an overlapping research group and same fundamental mating-memory mechanism**, not independent discovery in a different lineage/species. The experimental interventions extend the causal evidence, but should not be pooled as independent taxonomic confirmation.

## Methods and quantitative results checked in full article

1. Experienced MATa budding yeast under microfluidic pheromone stimulation (7 nM; microscopy 16 hours). Wild-type cells entered pheromone refractory escape and resumed budding. Mother daughters numbered by birth order **D1, D2, ...**, not independent mother populations.
2. **D1 size and division duration**: first daughters average cell area **35.7 ± 9.4 μm²** vs second **28.12 ± 5.7 μm²**, further daughters smaller. First divisions take longer; first-cell attachment rate **74.9 ± 2.6%** from **n=103** first daughters from three experiments; only **1 in 103** second daughters attached.
3. **Cdc10 septin** microscopy: **41.5 ± 14.1%** first divisions showed abnormal localization (misplaced bright patches/rings). Such altered septin localization correlated with daughters immediately budding rather than responding to pheromone, consistent with poor barrier confinement. This is correlation for some phenotype transitions.
4. **Shs1 septin deletion:** first daughters **66.9 ± 6.3%** refractory and second daughters **30.4 ± 12.3%**, versus wild type **46.5 ± 4.5%** and **12.2 ± 3.3%** respectively (p=0.0062 and p=0.0169). The same deletion also reduced mother escape efficiency within 16 h (**69.2%** shs1Δ vs **91.5%** WT), demonstrating **pleiotropic selection effects**.
5. **ER membrane barrier photobleaching/FLIP** using Sec61-GFP: after pheromone exposure the barrier index averaged **10.80 ± 9.4** (n=50), versus **12.86 ± 6.1** untreated (n=61), **p=0.0015**. A subset **15 of 50** post-exposure cells had a barrier index below the minimum observed among untreated cells; group means overlap widely.
6. The model proposed (not directly proven for all cases): unusually large cell size and prolonged first division increases time for leakage of Whi3 seeds to daughter, while abnormal septin dynamics lower barrier efficiency. The molecular trigger of septin mislocalization was **not identified**.
7. Authors explicitly distinguish **Whi3 mnemon confinement** from ***prion-like propagation*** when compartmentalization is disrupted, but this article does not itself prove an adaptive evolution of that transition.

## Why mother/daughter state and ecological fitness are different measurements

- Refractory daughters **cannot immediately respond to mating pheromone** and could lose mating opportunities, whereas a mother previously waiting without partner benefits by resuming its cell cycle. This future fitness argument is biologically reasonable but **not directly measured as long-horizon group offspring fitness in this assay**.
- Inheritance frequency is **conditional on mother history, birth order and membrane state**, so a simple permanent 'inherit learning' boolean is scientifically wrong.
- Pleiotropic septin defects affect cell division and size, making a naive comparison 'memory passed => evolution improved' unreliable.
- Measured membrane fluorescence and mother/daughter phenotype are **assays**, not reconstructed next-generation causal fitness functions, cognitive models, or transferred subjective experiences.
- No independent evolution of a division gate or new memory carrier was demonstrated. Gene deletions/fluorescent markers were produced by experimenters.

## Original EERC-T questions this supports without solving

**Hypothesis:** a *selective and state-dependent* transfer interface can be more adaptive than either forced perfect copying of learned state or mandatory erasure.

**Needed future-only causal controls:**
- Compare individual memory retention vs early/leaky daughter passage and measure **long-horizon descendant function** under unpredictable partner/resource availability.
- Test whether the best transfer profile **changes sign** when environmental correlations reverse (trained mother's aversion now wrong).
- Remove septin-dependent gate but **compensate** nonmemory cell-division costs before crediting inherited memory effects.
- Log whole independently evolving world lineage as replication unit; classify daughters by birth order and don't count repeated microscope frames.
- Keep alternative hypothesis that all observed effects arise from cell size, division stress or altered mating readiness, not specifically memory exchange.

**Scientific bottom line:** this is strong **biological proof that partitioning can change memory propagation**, not proof that greater propagation produces autonomy, cognition or a living digital organism. No third-party organism material handled or research-world code executed.
