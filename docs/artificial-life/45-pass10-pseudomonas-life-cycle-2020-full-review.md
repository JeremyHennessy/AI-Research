# Pass 10 full-primary review — Rose et al. (2020): group heredity can fail during the dispersal phase

**Reviewed 2026-10-08 | Main article E2, NOT independently reproduced.** Public full-text article, abstract, introduction, figure captions, experimental methods, results, discussion, and reported statistical tests were inspected. The linked PDF appendix and original raw assay tables **were not downloaded or independently reanalysed**.

**Primary:** Caroline J. Rose, Katrin Hammerschmidt, Yuriy Pichugin, Paul B. Rainey (2020). *Meta-population structure and the evolutionary transition to multicellularity.* Ecology Letters 23(9), 1380–1390. DOI [10.1111/ele.13570](https://doi.org/10.1111/ele.13570). [Full publisher HTML](https://onlinelibrary.wiley.com/doi/10.1111/ele.13570) (open access).

## Exact question and critical shared-history warning

Can a **two-phase mat → dispersal propagule → mat** life cycle allow natural selection to act on the whole collective when free-cell propagules from *different collectives* compete?

**DO NOT COUNT AS TWO INDEPENDENT EVOLUTION EXPERIMENTS:** the authors state explicitly that the **2020 non-mixed ecology** treatment was previously published as part of [Hammerschmidt et al. 2014](https://doi.org/10.1038/nature13884), and was run **simultaneously** with the 2020 mixed treatment. The 2020 paper newly contrasts dispersal mixing against that same earlier non-mixed dataset. The 2014 abstract is independently verified; its complete main text was **not** available in this review and is **not assigned E2** by association. The 2020 paper's newly analysed comparison and assays provide independent *analysis and treatment*, not wholly independent replications of 2014.

## Experiment as designed

- Organism: *Pseudomonas fluorescens* strain SBW25. **Wrinkly spreader (WS)** mat forms at air–liquid interface and harvests oxygen; **smooth (SM)** cells arise within mats and provide dispersal phase propagules. The two types and selection environment have highly specific, engineered constraints.
- Each generation: single WS founder → **6-day mat maturation** → recover SM cells → **3-day dispersal** → pick a **single WS colony of the most frequent type** for each next-group founder. Dead groups are replaced with survivor-derived propagules by researchers.
- Two ecologies: **non-mixed SM propagules**, kept within their source lineages, versus **mixed SM propagules**, pooled across surviving groups before dispersal. In both arms all new WS mats are founded by single cells, so differences **are not** from the presence/absence of a single-cell group bottleneck.
- **15 replicate metapopulations of eight competing microcosms per treatment** (120 group positions per arm, not 120 independent metapopulation replicates); **10 full group generations**. At assay: 15 ancestral clones, 15 mixed clones, and 15 non-mixed clones specified; Fig. 2 captions use **n = 14 non-mixed**, versus n=15 ancestor and mixed. The paper does not warrant inventing a reason for the n=14 loss.
- Assays for group fitness were **relative output of focal offspring mats against a neutral-marked reference**, measured across 3 competitions; cell fitness was a **proxy of total cells in mat** at end of maturation, not an all-purpose measure of cell viability or conscious agency.
- Investigated the **WS ↔ SM transition rate**, WS density, SM density and growth rates (additional separate time-series experiments). GLMs for offspring proportions, ANOVAs for cell traits with replicate clone nested in ecology, descriptive correlations, and a simplified population model.

## Author-reported outcomes (main paper §Results / figures)

| Outcome at generation ten versus ancestor | Separate propagules | Mixed propagules |
|---|---|---|
| Group offspring fitness | Increased (χ²=32.660, df=1, p<0.0001) | No statistically significant change (χ²=3.137, df=1, p=0.077) |
| Cell fitness proxy | Decreased (F(1)=10.612, p=0.002) | Increased (F(1)=56.214, p<0.0001) |
| WS-to-SM transition capacity | Marked increase (χ²=114.198, p<0.0001) | Smaller increase (χ²=12.459, p=0.0004) |
| Mat WS density | Decreased (F(1)=8.036, p=0.0065) | Increased (F(1)=9.904, p=0.0027) |

The ancestral WS density vs phenotype transition-rate relationship is **negative** (r=−0.705, p=0.003, N=15). Changes in mixed propagation favor abundant faster-growing cells that may overwhelm lineages better at completing collective reproduction. Group offspring success **cannot** be inferred from local copying rate alone.

## Authors' separate model: NOT another biological replicate

- **600 independent stochastic simulation runs**, 20 whole cycles, with an *imposed* negative covariance between cell growth and transition probability; model also explores dropping that trade-off.
- As reported, opposing trait responses replicate qualitatively *in the model*, including the role of competition during mixing. These **are not** 600 additional wet-lab populations, and the model assumes much of the hypothesized mechanism.
- Supplementary model equations and full parameterization are in Appendix S1 (listed on publisher page), **not audited here**. Record model result as a mechanism check, not an independently verified reproduction.

## Positive evidence vs limitations

**Supported author inference:** lineage separation during the propagule phase can make group-level differential reproduction effective enough for group fitness to increase even as its individual-cell growth proxy declines. The effect is contingent on trade-offs and metapopulation structure. A proto-soma/germ analog can matter.

**What was externally provided:** cyclic culture transfer, single-cell group founder, vessel boundaries, oxygen/air-liquid interface, sampling of dominant WS colony, extinction-replacement rule, competition environment, finite ten-generation endpoint.

**Not established:** self-generated compartments, spontaneous origin of reproduction as such, complete transfer of survival control from humans to evolved collectives, guaranteed persistence after mixing/release, all-cell cooperation, digital organismhood, consciousness, or general intelligence.

**Design caveats:** specific strain/air-liquid niche and deliberately imposed life cycle; group fitness proxy and cell fitness proxy have different units; group offspring counts are relative to a marked reference; mixed competition both changes selection and likely reduces between-group diversity (the last not directly measured). Subsequent claims about natural evolution under unstructured habitat are extrapolation.

**Rights and reproducibility:** link the author-provided full text; no original text or paywalled supplements copied into this repository. Code/raw data not executed. Original 2014 Nature source E1/abstract only in this pass. Paper text includes Appendix S1, Figures S1/S2 and Table S1 references: inspect them before reproducing values at higher precision.

## Translational insight for independent artificial-life work (original proposal, NOT an experimental result)

**The organismal unit may be the entire life cycle, not an active structure in one moment.** Track a collective's intergenerational transition and independently viable descendants. A graph of interacting programs can be cohesive in one frame but **lose its collective identity in a shared memory/replication phase**.

Candidate prospective nulls if *separately authorized*:
1. Identical reproduction/physics with vs without mixing during a dispersal bottleneck; freeze the cost ledger.
2. Measure group progeny **and** component copying separately; no collapsed single fitness score.
3. Preserve all extinct lineages and group-to-group genealogies, distinguish nine-day collective time from hour-scale component time.
4. Compare an externally imposed single-founder boundary to self-maintained, perturbable group boundary; demand daughter group transmission.
5. Control for artificially imposed fitness conflict: do not automatically assume group selection needs child-level self-sacrifice.

**Evidence status:** E2 main text inspection, zero reproduction; no project simulations authorized.
