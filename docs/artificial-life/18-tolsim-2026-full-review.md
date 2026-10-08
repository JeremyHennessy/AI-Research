# ToLSim (2026) — complete open-endedness test, methods, results and appendix audit

**E2: full public arXiv v1 HTML read; not independently replicated.** Authors Théo de Pinho and Lana Sinapayen. [Full public paper](https://arxiv.org/html/2603.01701v1), dated **2 March 2026**. [Author-linked code](https://github.com/LanaSina/speciation), [paper-linked dataset on Figshare](https://doi.org/10.6084/m9.figshare.31443793). Code contents and dataset were **not downloaded, run or independently audited** in this review.

## Central result: only the weakest activity trend partly passes

The authors apply steps 1–3 of a **Tokyo Type-1 OEE** test (as operationalized by Alastair Channon) to evolutionary activity measures for *Tree of Life Simulation* (ToLSim). They report:
- **20 independent runs**, each **2,000,000 time steps**.
- **Total cumulative activity** apparently "unbounded" in **8 runs**, bounded in **4**, and inconclusive in **8**, based on **visual trend classification**.
- **Normalized total and median cumulative activity bounded** in **all 20**; often decreasing/negative.
- **New activity** not persistently positive in **any run**, generally zero.
- **0 / 20 runs** passed the stricter **step-3 criterion** in their gene-level representation.

**Critical wording:** the paper does **not** mathematically prove boundedness/unboundedness in an infinite-time system. It bins finite trajectories visually. The authors explicitly acknowledge this limitation. This is good evidence of **failure under their specific finite test**, not proof that no form of evolutionary open-endedness can ever arise from ToLSim.

Source: [§3 methods](https://arxiv.org/html/2603.01701v1#S3), [§4 / appendix results](https://arxiv.org/html/2603.01701v1#S4).

## 1. What ToLSim's "organisms" are and what is designed
ToLSim spawns random initial agents. Some become viable lineages after replication, drawing energy from predation; agents also lose energy on motion, failed predation, reproduction and being alive. Their behavior is **not unstructured self-originated physics**. The substrate defines a grid, hereditary properties, energy exchange and death/reproduction rules.

Heritable parameters listed include **speed**, **maxEnergy**, **kidEnergy**, **nKids**, **pgmDeath**, **matForKids**, and **sensors**. Components for this study's evolutionary test were the *gene parameter values* of the first six, **excluding sensor structures** as component identity. Offspring cloning has a nominal **50%** chance of being selected for mutation; each mutant hereditary trait independently has a **60%** chance of changing. These are developer-defined, not evolved mutagenic rules.

**Interpretation:** this world is interesting as a reproducible population/lineage system, but evolution of new ecological information can be missed if the metric ignores structural sensor innovations. Conversely, numerical changes in a continuously varying scalar may inflate apparent gene diversity without functional novelty.

Source: [§2 ToLSim mechanics](https://arxiv.org/html/2603.01701v1#S2), [§3 component definition](https://arxiv.org/html/2603.01701v1#S3).

## 2. Tokyo-Type 1 quantitative test: what is compared

### Step 1, raw cumulative activity
For component i, activity increment is `Δ_i(t)=1` if component exists in the evolving system at time t, zero otherwise. Its accumulated activity resets to zero when no longer present. The global `A_cum(t)=Σ_i a_i(t)` measures retained prior presence/turnover. Sustained accumulation does not distinguish random survival/drift from adaptive success.

### Steps 2–3, neutral "shadow model" baseline
An **additional neutral model** runs births/deaths corresponding to the real population, except it chooses components for those events randomly. It periodically resets its state/history from the evolving population (paper suggests e.g. **every 1000 time steps**) to keep the neutral comparison locally matched.

Normalized per-component activity:
```text
Δ_i^N(t) = Δ_i^real(t) - Δ_i^shadow(t)
a_i^N(t) = retained cumulative normalized activity while i exists
A_cum^N(t) = sum_i a_i^N(t)  (over present real components)
median_A_cum^N(t) = median_i a_i^N(t)
A_new^N(t) = normalized cumulative activity of newly adaptively-significant components / diversity
```
Step-3 Tokyo T1 pass condition requires **both normalized total and median cumulative activities unbounded** *and* **persistently positive new activity**. Its "adaptively significant" definition is tied to the shadow-baseline activity threshold, not an independent biological assay. If new activity remains zero, the criterion fails regardless of raw persistence.

**No conflation:** this shadow subtraction is different from Flow-Lenia's **total-mass normalization**, and different again from PBT-NCA's **fitness-based novelty archive**.

Source: [§3.1–3.3 definitions/equations](https://arxiv.org/html/2603.01701v1#S3).

## 3. Exact results, including ambiguity
| Trend as classified by authors | Run count / 20 | Interpretation |
|---|---:|---|
| Raw total cumulative apparently unbounded | **8** | Visual classification based on finite observation |
| Raw total cumulative bounded | **4** | Apparent plateau |
| Raw total cumulative unclear | **8** | Ambiguous finite trend |
| Normalized total cumulative bounded | **20** | None meets stronger test |
| Normalized median cumulative bounded | **20** | None meets stronger test |
| New normalized activity persistently positive | **0** | Sufficient for 20/20 step-3 failures |

In the appendix, each of 20 rows is marked `Null` for the new activity outcome. The exact number of simulated steps **must not** be reinterpreted as an actual bound on potential complexity. Authors note trends were classified by eyesight and recommend more systematic estimators.

Source: [§4 results + Table 1](https://arxiv.org/html/2603.01701v1#S4), [§5 conclusion](https://arxiv.org/html/2603.01701v1#S5).

## 4. Major limitations acknowledged or inferred
- **Metric representation:** selected gene values are not individuals/species; alternative unit may change results. Authors directly request tests with individuals and species.
- **Metric sampling/statistics:** trend categories judged by eye; not a pre-registered slope/bound test with uncertainty.
- **Shadow process:** random component deaths/births and resetting approximate a neutral baseline, but may not preserve all correlations/dynamics of the underlying population.
- **World design:** map size, energy input and per-step maintenance cost may suppress innovations.
- **Population drift vs adaptation:** raw accumulated presence does not imply new functional invention.
- **Functional evolution:** no independent de novo ecological capability transferred to descendants is established by raw gene activity alone.

## 5. Proposed future *research-only* checks
1. Use the authors' published dataset (subject to rights and scope approval later) for independent **statistics-only** recomputation; compare authors' visual labels to preregistered changepoint/slope/censoring methods. That would be a **reanalysis** of recorded observations, not a new organism.
2. Repeat component statistics defined at **gene, agent, species, and process** levels, with independently justified lineage rules; compare sensitivity to segmentation.
3. Run random-lineage/shadow variants to test dependency on normalization and reset interval; report negative scores and uncertainty.
4. Add blind **functional affordance assays**: can descendants do something their ancestors could not under a previously unseen resource/interaction test? A mere scalar mutation is not functional novelty.
5. Study ecological parameters (world size, resources, cost of being alive) with a prespecified budget and repeated independent worlds—but only in a **future separately authorized** experimental project.

**Source depth and rights:** complete arXiv v1 HTML (including methods, figures described in captions, conclusions and appendix table) reviewed. Source code and Figshare dataset not executed; no correction/retraction status beyond present public record established. E2 only.
