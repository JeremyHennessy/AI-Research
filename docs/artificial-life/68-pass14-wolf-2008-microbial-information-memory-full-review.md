# Pass 14 — Wolf et al. (2008): quantifiable history information is not necessarily adaptive memory

**2026-10-08 | E2 complete published PLOS ONE primary main paper, figures/methods/limits reviewed; independent raw data and MATLAB analytics NOT rerun.** Denise M. Wolf, Lisa Fontaine-Bodin, Ilka Bischofs, Gavin Price, Jay Keasling and Adam P. Arkin, **Memory in Microbes: Quantifying History-Dependent Behavior in a Bacterium**, *PLOS ONE* 3(2):e1700 (2008), DOI [10.1371/journal.pone.0001700](https://doi.org/10.1371/journal.pone.0001700), [complete primary text](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0001700). Published under PLOS public-domain declaration; source still linked rather than copied.

## Exact question

Can a population's *current response* disclose its **past environment**, even after all test samples move to the same new condition? This is a legitimate **information-theoretic memory observable**; whether it was selected to improve later ecological fitness is **a separate untested question**.

## Study design, measurement and denominators

- One genetically engineered **Bacillus subtilis** reporter strain; five starting population densities in each of **two preconditioning media** (LB and GM), producing **ten distinct prehistory conditions**.
- **Three replicate cultures per history**, **30 cultures total**, then transition all into the **same starvation medium**. Source histories are not independent species/genomes, nor is microscopy/instrument timepoint a new experimental population.
- Three reporter/readout types: **PspoIIE-GFP** for sporulation initiation, **PaprE-DsRed** for extracellular degradative enzyme regulation, and **OD600** for cell population growth. **Population-averaged trajectories**, not separately followed single-cell lineages.
- Analysis clustered time-course patterns into trajectory classes and estimated **mutual information** between random past-history category H and observed response Y. Different combinations of reporters overlap, so do **not add their bit scores as independent storage capacity**.
- The authors identify an upper bound of **log2(10)=3.3219 bits** given the **chosen experimental histories**, not a measured upper bound on how many bits a bacterium can store biologically.
- “Transient” observation used approximately the **first eleven hours** after new starvation; “long term” used final **21–24h** slices. The latter is a finite-window operational name, **not indefinite memory**.

## Author-reported results from Fig 5–7 and Methods

| Observable | Short-term I(H;Y) (bits) | Long-window I(H;Y) (bits) | Interpretation |
|---|---:|---:|---|
| PspoIIE sporulation initiation | **1.96** | **0.8813** | Strongest transient response differentiation among histories |
| PaprE extracellular enzyme regulation | **~1.49** | **~0.72** | Distinct aspect of cell prehistory in same starvation regime |
| OD600 growth behavior | **~1.00** | **~0.97** | Less transient detail, detectable long-window signal |
| Two/three reporters jointly | Context specific, **not additive sums** | Pair readouts may contain complementary history | Mutual information must account for correlated responses |

Clustering three distinct responses reveals one can reconstruct aspects of history more reliably from one output than another. In some GM-conditioned subsets, individual past density became **undetectable** in the study's response distribution, whereas high-density LB preparations retained distinct sporulation lag information. Authors estimated sporulation activation after starvation varying roughly **1.5 to 8+ hours** depending on prior growth history.

## Crucial limitations and self-identified counterargument

The paper **does not identify molecular carriers**, nor manipulate their memory independently to show benefit, nor prove cells anticipate a future starvation duration. The authors themselves discuss a less exciting explanation: **metabolic reserves, ribosomes and initially expressed apparatus** make the same subsequent starvation stimulus elicit different dynamics. Their adaptive-game interpretation was explicitly speculative.

Other pitfalls:
- If a phenotype can encode a history label due only to passive initial conditions, a large I(H;Y) does **not** equal a new learned useful cognitive strategy.
- The **clustering and entropy estimator** can introduce discretization and finite-sample bias; no independent replication, confidence interval reconstruction or holdout of history categories was performed by AI-Research.
- Population optical density, sporulation reporter and protease signals measured over **shared cultures**, not independent neural or consciousness features.
- A **permanently useful behavioral policy** can have little measured I(H;Y) when task performance is identical across histories, while a useless stress marker can exhibit high mutual information. **Utility and predictiveness cannot be inferred from bits alone**.

## Relevance to emerging EERC hypotheses

Require at least three distinct metrics:
1. **Trace information:** detectable linkage between prehistory and a measurable state after washout, with unit/estimator baseline and chance controls.
2. **Causal functionality:** ablate state carrier while preserving survival machinery, demonstrate an *independent unfamiliar challenge* benefit with matched resources.
3. **Endogenous origin:** record whether the memory carrier/controller was already wired into the substrate or evolved under the tested ecology.

A scoring design that rewards **maximal mutual information** risks selecting conspicuous history-label storage unrelated to viability, or exploitative correlation caused by a researcher's own tags. Do not use an observer's entropy score as a built-in reward if the goal is investigating unprompted self-organization.

**Reproducibility rights:** E2 full-primary-method review; complete paper open/public-domain declaration checked; files/method scripts cited only, none run. No living digital organism or model weights produced.
