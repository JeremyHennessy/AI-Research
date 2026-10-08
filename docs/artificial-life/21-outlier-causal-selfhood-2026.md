# Outlier reexamined: causal distributed self-replication (2026)

**E2 — complete public arXiv v1 methods/results/discussion review, with peer-reviewed journal publication checked.** This is an **independent follow-up by different authors**, not an independent model reproduction executed in AI-Research.

**Source:** Arend Hintze and Clifford Bohm, *Rethinking self-replication: detecting distributed selfhood in the outlier cellular automaton*. [Open arXiv full text v1, 11 August 2025](https://arxiv.org/html/2508.08047) · [npj Complexity 3:11, published 16 February 2026](https://doi.org/10.1038/s44260-026-00074-2). [Published journal page](https://www.nature.com/articles/s44260-026-00074-2). arXiv preprint is marked **CC BY-NC-SA 4.0**; check journal version rights separately. No text or code archived from the paper.

## 1. Central improvement over Yang's observation
Yang reported visually repeated clusters and formations. Hintze & Bohm define **self-replication by causal dependence** rather than reappearing shape.

**Definition:** parent entity produces **at least two equal-pattern offspring**, each causally dependent on parent but **not on one another**. Thus:
- a repeating oscillator is a single continuing process, not two separate children;
- a glider moving across the grid is **not** self-replicating merely because it visits equivalent shapes;
- a glider gun is not a replicator of *itself* merely because it emits gliders;
- a disjoint **formation** can count as one entity if its evolving components are causally linked.

This is a rigorous operational definition **within a deterministic binary CA**, not a universal definition of living reproduction. The paper limits primary detection to **exact copies of connected cell clusters**; it does **not** establish heredity of novel variants.

## 2. Causal method
1. For each CA tick, identify connected live-cell clusters under Moore adjacency; give each *cluster form* a CID and each *time/location instance* an UID.
2. For each newly alive cell, examine the previous tick's 3×3 neighborhood, finding which cells are **necessary** for that activation under the exact deterministic rule table.
3. Exclude redundant input cells; if multiple minimal cause sets occur in other CA rules, conservatively aggregate them. Authors report no ambiguity of this sort for Outlier.
4. Aggregate each necessary predecessor cell into its source cluster, create a directed ancestry edge to the recipient cluster instance.
5. Search this graph for **branching paths** in which two daughter instances of the same pattern depend on a parent but are not causally dependent on each other.
6. Trace *distributed developmental paths* through many apparently disconnected clusters and their mergers/splits.

**Major design assumption:** dead-cell histories are **excluded** from causal tracing. The authors reason that alive cells propagate live structure in Outlier; nevertheless this limits the genealogy to their particular positive-cause definition. Negative constraints and counterfactual absence may matter for other physics.

## 3. What they actually measured
| Quantity | Author result | Essential caveat |
|---|---:|---|
| Grid / method | 1024×1024 periodic torus, `c0` seed, 20,000 steps | Single selected initial pattern, not all random seeds |
| Full causal ancestry | **31,959,320 instance nodes**, **65,552,995 edges** | Cluster-instance graph, not proof of individual organisms in a biological sense |
| Distinct cluster patterns in full run | **966,208** | Visual/structural variety ≠ independent functional adaptive innovation |
| `c0` copies in first 10k ticks | **433**, no second-generation copy | Replication under formal criterion, weak lineage continuity |
| `c1` copies in first 10k | **1,677**, second generation late | Environment/boundary effects likely influence branching |
| `c2` appearances in first 10k | **2,439**, **15 generations** | Same cluster type and distinct developmental routes, not genetic evolution |
| `c2` reproducing instances shown in a tree | **344** | Tree tracks causal developmental paths, not different genome types |
| Replicator reproduction durations | 18 distinct observed times | Timing variation need not be heritable change in a new function |
| First 10-generation growth fit | **1.4955** estimated multiplicative factor | Finite pre-boundary fit, not perpetual exponential growth |

**Additional 75,000-tick analysis** on an effectively unbounded grid measures emergence of new cluster shapes and growth of maximum size. Fits favor power laws over one hyperbolic comparison. This is a finite-run model fit, **not a theorem of indefinite novelty**.

**Recombination result:** of **205 c2-like replicators** identified after tick 5,000 by the chosen search, **18** were not in the lineage of the original `c2`. They trace to collision debris and other replicator-derived material, indicating new *causal developmental combinations* inside the chosen universe—not novel ecological skills or a new genetic code.

## 4. The strongest conclusion
**Evidence-supported published finding:** Outlier's fixed, simple cellular rule can produce **causally branching, sometimes spatially disconnected replication processes**. Replication need not mean a continuously connected static object.

**What remains unverified:** endogenous metabolic upkeep, self-chosen behavior, learning within a lifespan, inherited new function, evolving instruction language, major transitions, or true open-ended biological-like innovation.

**Independent follow-up vs independent replication:** the Hintze/Bohm study is a separate peer-reviewed scientific analysis of the *same Outlier system*, providing corroborating and stronger mechanistic evidence. AI-Research **has not run** the authors' code or confirmed their numbers. Their causal graph was computed from a specific rule/seed.

## 5. Reproducibility inventory (source-only)
- [Zenodo data + full analysis package](https://doi.org/10.5281/zenodo.17904018), referenced by 2026 journal under data/code availability. Archive not downloaded or executed.
- [Hintzelab/RethinkingSelfReplication](https://github.com/Hintzelab/RethinkingSelfReplication) @ `20125a33db148a92d209e4485d2b59d3f2155cca` (main, inspected 2026-10-08). Root **MIT LICENSE** and README inspected. Repo includes `outlierJS.html` for browser visualization, **not the complete 31.9m-node published analysis**; core datasets and analysis are at Zenodo. No code run.
- [Yang's Outlier paper](20-outlier-original-2025-full-review.md) contains a LifeViewer lookup and seed, not a verified independent complete reproduction in this repo.

## 6. Discriminating next tests (future proposal only)
- **Branching vs cyclic recurrence:** exact causal DAG with independent offspring, compared against oscillator, glider and glider-gun negatives.
- **Disconnected selfhood:** allow causally dependent groups in separate spatial components; compare connected-component-only lineage tracker to graph tracker on blind examples.
- **Vary source rules:** swap CA rule, boundary conditions and initial density to test generality without overfitting to one selected Outlier seed.
- **Prove inherited difference:** introduce a controlled phenotype mutation and test whether daughter-specific behavior/affordance is transmitted to granddaughter under a novel environmental challenge. A different replication duration alone is insufficient.
- **Resource dependence and autopoiesis:** independent resource and repair accounting required; the fixed Outlier CA has no demonstrated metabolizing resource economy.

**Interpretation gate:** a verified causal branching graph proves **replication under a defined criterion**, not **life** or **open-ended evolution**.
