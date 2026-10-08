# Pass 16 — Rotrattanadumrong & Yokobayashi (2022): RNA neutral networks, exhaustive paths and human-guided search

**Reviewed 2026-10-08 | E2 complete openly published Nature Communications primary manuscript, Figures/Results, Methods and Data/Code statements inspected through the [original journal public text](https://www.nature.com/articles/s41467-022-32538-z) and [PMC counterpart](https://pmc.ncbi.nlm.nih.gov/articles/PMC9385714/).** CC BY 4.0. Supplementary tables/figures and the deposited sequencing/Zenodo analysis code NOT independently executed or recalculated. No organism or research AI trained in AI-Research.

**Primary:** Rachapun Rotrattanadumrong and Yohei Yokobayashi. *Experimental exploration of a ribozyme neutral network using evolutionary algorithm and deep learning*. Nature Communications **13**:4847 (2022), DOI [10.1038/s41467-022-32538-z](https://doi.org/10.1038/s41467-022-32538-z).

## What is experimentally established

- Authors selected a small, **pre-existing ligase ribozyme** and used high-throughput activity measurements plus an **experimenter-designed mutation/recombination/selection algorithm** to explore sequences under an externally chosen ligase activity threshold.
- Across the project, the authors experimentally screened **over 120,000 sequence variants**. These assays are individual genotype measurements; **not** 120,000 evolving organisms, independently reproduced life histories or novel biological origins.
- From an evolved candidate differing from the original by **16 nucleotide positions**, they experimentally measured **all 2^16=65,536 genetic combinations** between the two endpoints, finding **many neutral paths** of single changes connecting them despite potential deleterious neighbors. The map establishes the existence of a large measured neutral genotype subnetwork in the tested space.
- The candidate was reached through **seven iterative laboratory rounds** with experiments informing the next design and a **final computationally generated eighth generation**. The last stage used a **human-programmed multilayer-perceptron classifier** and **100 rounds of in-silico evolution** before experimentally screening candidates.
- The authors classified relative activity at an **external threshold of RA ≥ 0.2** as neutral vs deleterious. The threshold has specific measurement/assay meaning; a path's neutral status cannot be assumed for every nutrient, physical stress or RNA replication capability.
- The authors deposited raw sequencing via **PRJNA863914** and processed sequence/activity plus reproducibility code at **Zenodo DOI 10.5281/zenodo.6945203**. Existence of public data/code is a provenance fact; independent code/data reproduction was **not** performed.

## The critical negative boundary

**This is not a spontaneous evolution of biological freedom.** The experimental reaction, genotype design grammar, ribozyme native function, mutation operators, assay classification, fitness threshold, ML evaluator and target functional endpoint were all defined by researchers. A classifier trained on measured data is an **external guide**; computational search steps do not establish that an organism invented its own controller, reproduced its collective offspring, or autonomously created a new metabolic niche.

**Good positive result:** high-dimensional genotype landscapes can contain interconnected regions of sufficiently functional variants; such regions make some distant phenotypes accessible without forcing a lineage through fully non-functional intermediate genotypes. This is useful **evidence of reachability under specific externally fixed criteria**, not proof of indefinite open-ended complexity.

### Contrast to other Pass 16 sources

- [Hayden et al. 2011 E2](81-pass16-hayden-2011-cryptic-rna-variation-full-review.md): two historically diversified ribozyme populations **adapted faster to new substrate** than undiversified WT, including intermolecular rescue of one otherwise inactive component. Those are experimentally measured *outcomes* of cryptic variation.
- **2022 mapped network**: experimentally tests the existence of mutational paths and explores them with a trained model. This is independent RNA sample history but not independently reproducing evolved organism groups.
- [Beaumont 2009 E2](79-pass16-beaumont-2009-history-dependent-switch-full-review.md): phenotype switching possible in original background but can have the wrong fitness sign. Distinguish genotype/phenotype space connectivity from **selection accessibility**.

## Suggested future tests — research only

The EERC-06 hypothesis should demand both **behavioral capability** and **selectable ecological viability** under inherited ancestral conditions, with fixed mutation/physics/energy costs. Compare a naturally self-produced function to **external ML-guided search**, **handcoded neutral threshold**, and **forced reproduction** positive controls. Require source-specific costs, blank controls and all lineages, not just a sequence graph or an impressive novel structure.

**Rights and evidence:** complete original main journal paper E2, full supplements/raw code not run, external guided selection explicitly identified, no E3 reproduction. No AI weights, trained model or simulator created by our work.
