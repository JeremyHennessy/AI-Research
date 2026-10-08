# Flow-Lenia (2025) — complete public-paper methods and results audit

**Evidence: E2 (literature review, not independent reproduction)** · Read 2026-10-08 · [arXiv HTML version 1](https://arxiv.org/html/2506.08569v1) (10 June 2025) · [Journal DOI 10.1162/artl_a_00471](https://doi.org/10.1162/artl_a_00471), *Artificial Life* 31(2), 228–248 (2025). The arXiv manuscript is CC BY 4.0. All experimental measurements below are **authors' reports**, not new tests here. [Precursor JAX code source](https://github.com/erwanplantec/FlowLenia) pinned previously to `dce428c6b0c5079a06e5606fb7b5ac1fe1323bc5`, **not proven to exactly reproduce the 2025 paper's environment variants**.

## Executive finding: resource-normalized evolutionary-activity conclusions reverse

The authors report **larger raw count-based and non-neutral evolutionary activity** in food and dissipative variants than vanilla (Mann–Whitney reported p<10^-5). **But food and dissipative variants do not preserve global total matter**: they add or remove matter. When evolutionary activity is divided by total system mass, the ranking reverses, and dissipative activity is markedly lower. At the end of simulations food and vanilla activity can approach similar values, though vanilla's time-averaged corrected score is higher. These are **different estimands**, not logically contradictory results.

**Our inference:** extra matter inflow can inflate a mass-weighted "evolution" proxy without proving new inherited functions. Any future ALife study must report **raw and mass-normalized** activity together, plus organismal repair, phenotype and lineage outcomes. This is not evidence that resource constraints always reduce true evolutionary novelty; the experiment's implementation and metrics differ.

Source: [full paper §5.3 / Figure 10](https://arxiv.org/html/2506.08569v1#S5.SS3), [§6 Discussion](https://arxiv.org/html/2506.08569v1#S6).

## 1. Mathematical mechanism: what mass conservation actually means
Baseline Lenia activation is `A^t`, with convolution kernels `K_i`, growth nonlinearities `G_i`, and an update adding clipped `dt U^t`. Flow-Lenia **reinterprets** `U^t` as an affinity field, **moving** existing mass instead of creating/destroying matter through a clipped growth update.

For channel i:
```text
A_sum(x) = sum_i A_i(x)
alpha(x) = clamp( (A_sum(x)/beta_A)^n, 0, 1 )
F_i(x) = (1 - alpha(x)) * grad U_i(x) - alpha(x) * grad A_sum(x)
```
The Sobel-estimated affinity gradient drives motion; the opposing mass-gradient spreads dense matter. Reintegration tracking sends each cell's mass to overlapping target cells with a normalized square transport distribution. Because outgoing mass fractions sum to 1, the *ideal base transport step* conserves total matter; this can be affected by discretization/boundary implementations and changes in environmental variants.

Paper equations: [§3 equations (5–6)](https://arxiv.org/html/2506.08569v1#S3). The authors report a **Tesla T4 255±3.11 microsecond/step** example for 128×128 cells, one channel and ten kernels. This is a **single specified kernel/hardware setting**, not a general throughput guarantee.

### Why "species" can coexist
A parameter field `P^t(x)` moves along with matter. When multiple source cells with different parameter values contribute mass to one target cell, a **stochastic softmax over incoming mass** selects the target parameter; another evaluated variation uses deterministic argmax. The authors choose this because it permits one parameter-associated population to acquire matter from others; a simple averaging mixture would continuously generate new parameter types.

Crucial: the dynamic field `P` is **a transmitted local rule descriptor**, not a biologically validated genome or independent organism lineage. More importantly, **global kernel parameters are not all made local**: dynamic kernels at every location would defeat efficient shared convolution. Read [§3.1](https://arxiv.org/html/2506.08569v1#S3.SS1).

## 2. Separate the paper's three experimental regimes

| Regime | Actual selection / environment | Evidence outcome | What cannot be credited |
|---|---|---|---|
| **Random search** | 105 sampled parameter sets, identical settings compared with Lenia, 150-step rollout | Flow-Lenia more commonly yields localized persistent-looking patterns rather than explosion/vanishing | Heritable evolution, independently evolved behavior |
| **Directed search** | **Four researcher-defined fitness objectives:** directed motion, angular motion, navigating obstacles, chemotaxis; OpenES population 16; Adam LR .01; one/two channels | Locomotion / steering / chemotaxis behaviors can be found with evolution strategies | Intrinsic fitness with no externally selected objective |
| **Intrinsic-evolution setting** | Local stochastic parameters, mutation beams, interacting parameter-associated matter; vanilla vs food/dissipative conditions | Time-varying parameter occupancy/activity and qualitative competitive/mixed dynamics | Guaranteed true species identity, organismal lifetime learning, indefinite innovation |

Source: [§4 methods](https://arxiv.org/html/2506.08569v1#S4) and [§5 results](https://arxiv.org/html/2506.08569v1#S5).

## 3. Reproduction-grade *reported* settings for intrinsic-evolution experiments
- Time horizon: **500,000 simulation steps**; reports repeat **five independent seeds**. Every **100 steps** recorded for memory practicality.
- Default initialization: **3 channels, 5 kernels per channel pair → 45 kernels**, with **64** independently placed initial **20×20** patches.
- Mutation: externally sampled **10×10** spatial "beams" add Gaussian `N(0,1)` perturbation to local rule parameter map, with adjustable `p_mut`. Beam regions grant mutants a critical mass of adjacent cells; this is a designed mutation operator, not intrinsic evolution of a mutation mechanism.
- **Vanilla:** fixed global amount of matter, competing locally parameter-defined patches, no food source; matter redistributes/converts between parameter categories.
- **Dissipative:** a beam removes matter/parameter types; another injects an **entire new random 20×20 creature patch**, restricted to a **100×100 corner** input zone, at controlled `p_diss`. That is *externally created biological-looking novelty*, not a daughter independently produced by an existing organism.
- **Food:** matter decays at fixed rate `r_decay`, new `5×5` food squares appear stochastically on a food map `Psi`; authors seed **32 patches** initially, then add new food patches with probability `p_food` per step. Food and matter colocated in a cell convert at `r_digest`; kernels can sense food.

These environment definitions are central to causal attribution. Mass conservation in the **base flow operator** does **not** imply conservation of global total matter once removal, injections and food conversion are active.

Source: [§4.3 settings and model variations](https://arxiv.org/html/2506.08569v1#S4.SS3).

## 4. Exactly what "evolutionary activity" counts

The authors define a **component** as one unique point `p` in high-dimensional parameter space. Distinct parameter tuples—even differing infinitesimally, and even if they give identical observable behaviors—are **different species** under the metric. The mass `M(p,t)` associated with parameter `p` is its occupancy-like weight.

- **Count activity** increments by that parameter's associated matter while it exists.
- **Non-neutral activity** increments on increases in its *proportion* of the total parameter-associated matter, weighted by global mass and squared fractional change.
- **Diversity** is based on pairwise distances between parameter vectors, not demonstrated biological function.
- **PCA "phylogenetic trees"** depict projected parameter trajectories, not necessarily observed parent/child phenotype descent.

The paper recognizes this species-definition weakness in its own discussion and suggests phenotype-aware definitions and clustering coherent parameter bundles.

**Critical confounds:** adding mass inflates raw EA; replacing matter with random patches creates new parameter categories by designer mechanism; exact continuous vector identity can count an arbitrary near-duplicate as "new species"; visual trees are not authenticated genealogy. No organism-level **independent heritable function assay** is reported.

Source: [§4.3.3 activity equations](https://arxiv.org/html/2506.08569v1#S4.SS3.SSS3), [§5.3 results](https://arxiv.org/html/2506.08569v1#S5.SS3), [§6 discussion](https://arxiv.org/html/2506.08569v1#S6).

## 5. Secondary findings, with bounded interpretation
- Authors observe common spatially localized forms under mass conservation. This is a useful **regularization effect** that simplifies pattern search. It can also select persistent static attractors rather than autonomous maintenance.
- Their 5-seed study shows **sublinear** increase in parameter-type count with `p_mut`, which the authors interpret as competition and regulation; alternatively, finite carrying capacity and mutation-selection balance may also contribute.
- In vanilla, higher mutation rates associate with lower mass-weighted activity; the study fits reported power slopes approximately **-0.5** non-neutral (`R²=.75`) and **-0.71** count-based (`R²=.71`). These are empirical fits in that simulation family, not universal laws.
- Paper figures show apparent cooperation and multispecies cohabitation; no independent lineage/repair/counterfactual symbiosis evidence is supplied.
- Parameter map values can wander far outside the normal initialization distribution; adding externally sampled patches in the dissipative condition may then *lower* observed parameter diversity. This exposes a second serious comparability issue.

## 6. Verdict by scientific question

| Claim | Evidence in the paper | Our interpretation |
|---|---|---|
| Exact local matter-conserving transport | Equations and JAX implementation description | **Method described**; numerical mass-residual reproduction not run |
| Multi-parameter coexisting dynamics | Spatial snapshots and parameter trajectories | **Supported within its simulations**; species semantics disputed |
| Evolutionary activity varies with ecology | Quantitative 5-seed experiments | **Author reported**, but raw and normalized metrics reverse |
| Spontaneously reproducing organisms with heredity | Not independently demonstrated | **Unresolved** |
| Endogenous energy-consuming repair | Food/dissipation externally managed | **Unresolved** |
| Open-ended, indefinite evolution | Finite experiments, parameter metrics | **Not established** |
| Emergent intelligence/consciousness | No independent measure | **Not established** |

## 7. Future smallest decisive falsifiers (not implemented)
1. Compare **mass-normalized vs raw** evolutionary activity at equal global mass in vanilla/dissipative/food variants; use proper independent **world-level** confidence intervals, no independent-frame pseudo-replication.
2. Replace parameter-exact species count with phenotype and transmitted lineage-aware metrics; test against mixing-induced false branches.
3. Restrict mutation to **offspring-derived** local patches (vs random beams) and independently test whether newly arising functions persist across daughters.
4. Freeze external food/respawn and run a fully accountable energy/resource ledger; ablate one repair pathway at a time.
5. Compare static attractors under the same conservation law with resource-maintaining entities; avoid fitness/appearance-based labels.

**Source audit limit:** Entire arXiv v1 HTML main text including math, methods, results and discussion read. Journal typesetting, any off-page supplementary files, and JAX code behavior were **not** independently replicated. Thus E2, not E3, is justified.
