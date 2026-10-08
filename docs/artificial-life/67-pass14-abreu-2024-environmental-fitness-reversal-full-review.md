# Pass 14 — Abreu, Mathur & Petrov (2024): static fitness can reverse after an environmental transition

**2026-10-08 | E2 complete primary Nature Ecology & Evolution main article, Methods, Results/Figures 1–5 and caveats reviewed; NOT experimental reproduction.** Clare I. Abreu, Shaili Mathur and Dmitri A. Petrov, **Environmental memory alters the fitness effects of adaptive mutations in fluctuating environments**, *Nature Ecology & Evolution* 8:1760–1775 (2024), DOI [10.1038/s41559-024-02475-9](https://doi.org/10.1038/s41559-024-02475-9), [full author manuscript on PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC11853131/). Publisher holds exclusive distribution rights; source and public data/code only linked, not mirrored. SRA BioProject **PRJNA1103172** and [author source/data repo](https://github.com/clare-abreu/environmental_memory) NOT downloaded/executed.

## Main hypothesis tested

If organism fitness in alternation A↔B were just the arithmetic mean of static A and static B, memory/history would add nothing. But rapid transitions can change lag/recovery, **making the same genotype's performance depend on the prior environment**, sometimes reversing which environment seems to favor it.

This is **environmentally conditioned fitness of genotypes already evolved in yeast**, not proof the same cell learned an entirely new action in one exposure, nor emergent consciousness.

## Experimental design: never confuse sample levels

- Start with roughly **500,000 barcoded founding yeast lineages**, from a previously constructed strain-library, and conduct selection in **five static** carbon/stressor environments plus **five fluctuating combinations**, spanning ~**168 generations** in serial-batch growth.
- Evolution experiments contained **one or two independent flasks** per selected environment (one Glu–Gal fluctuating replicate); **NOT 500,000 independently repeated evolution experiments**.
- From revived evolution stocks and lineages' barcode-frequency trajectories, researchers isolated **889 uniquely barcoded adaptive-candidate clones**, selected/conditioned by previously achieved fitness. This is **not** 889 unrelated founding genotypes.
- They pooled these clones at **5%** in an ancestor-dominated reference population for **three biological replicates** of short-term fitness assays across **five static and ten fluctuating pair** conditions; the full grid is 15 conditions, not 15 independent ecosystem replications.
- An environment combining lactate+peroxide had **poor fitness-assay replicate correlation** and was excluded from summary analysis, though separately shown. After removing clones with low home fitness the reported core analyzed sample was **695 mutants**, with sensitivity analyses using other thresholds.
- Whole-genome sequencing yielded **352** clone sequences to look for plausible adaptive targets; recurrent mutations in regulators and lag-related systems are clues, **not one causally verified master memory gene**.

## Actual primary quantitative evidence

| Author-reported result | Denominator/control | Why useful / limits |
|---|---|---|
| **30%** of measured non-additivity cases significant under conservative 95%-CI error rule | Compared observed fluctuating fitness to mean static-component fitness; replica uncertainty included | Rejects universal simple-average rule; this is *cases among assays*, not 30% of independent species |
| **53%** of measured environment-component **memory** differences significant at same conservative 95% rule | Compare fitness inside a fluctuating component with fitness for matching static condition | Stronger history sensitivity than net non-additivity; no unique molecular history carrier isolated |
| **29%** of studied fluctuating component cases: opposite static condition better predicts component fitness than current-condition static fitness | Comparator includes 2% reversal under static replicate split; up to 13% for noisier fluctuating replicate comparison | Counterintuitive **fitness reversal** under assay definition, not actual time travel, inversion of raw nutrient physics or proof of clever internal prediction |
| Among top 10% mutants ranked by cross-static fitness differences, reversal fraction **39%**, vs bottom 10% **11%** | Rank analysis within selected mutant pool | Highly context-dependent genetic trade-offs; no generalized common memory policy shown |
| Large history effects despite apparently additive overall fitness | Separate per-component trajectories, not just end-to-end slope | Aggregate fitness can **cancel** large alternating positive and negative shifts and conceal memory |
| Model with altered lag times can reproduce major patterns | Authors fit a **descriptive lag-time shift** (80% towards mean) | Lag shift inferred, not directly verified in every clone; sensing mutation effects correlational |

## Biases and limits

1. **Severe fitness-unit asymmetry:** a pool of barcoded mutants is a population-genetic competitive assay, not single-cell behavior readout. Three fitness replicates do not make the 889 clones independent ecological origins.
2. **Static vs fluctuating environment history:** all transfers include stationary/serial-batch phases, nutrient depletion and externally renewed substrates. The environment immediately *before* growth matters, but direct metabolite/cell-state causality is inferred from modeling/associations, not fully reconstructed.
3. **Clone preselection and partial sequencing:** chosen 889 enriched for adaptive trajectories; 695 after one standard threshold. Cannot infer fraction of random natural microbes with history memory.
4. **Signal overlap:** arbitrary 0.05 fitness exclusion, a 0.05 borderline reversal threshold, and differing variance across static environments require sensitivity checks (performed partially by authors); count cells/clones and assay trajectories at appropriate unit.
5. **Temporal variability / stochasticity:** same mutation may help or hurt following different nutrient sequences; that does not imply new spontaneous learned goals or a universal optimal memory decay controller.
6. **Rights / reproduction:** original public PMC manuscript fully inspected; source data CSV and sequence repository NOT independently reanalyzed; not licensed to mirror copyrighted journal article.

## Cross-study inference for EERC (unverified)

A proposed evolved memory system should not be assessed only by its **average success** on alternating worlds, because gains in one transition may cancel harms in the other. Pre-register separate readouts for:
- A after A, A after B, B after A, B after B, and **unexpected A after long B**;
- per-lineage carried state and reset times, actual transferred material and sensing;
- resource costs, *extinction* and censored transitions, offspring viability and source provenance;
- reversal of a previously advantageous conditional response when ecological correlations invert.

**Most important falsifier:** an allegedly new history-aware policy offers no extra generalization after matching lag dynamics, mutation composition, growth resources and a cheap fixed hysteresis controller.

The source establishes **environment-conditioned fitness**, not a digital organism, new neural or linguistic intelligence, or subjective consciousness.
