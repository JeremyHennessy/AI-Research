# Three incompatible "open-endedness" measures: technical comparison

**Cross-paper synthesis from full-public-text E2 reviews, 2026-10-08.** These papers have different model families and objectives, and **their scores cannot be numerically compared to each other**. This table is designed to prevent misleading rankings.

| Question | Flow-Lenia 2025 | PBT-NCA 2026 | ToLSim 2026 |
|---|---|---|---|
| Primary substrate | Conservative spatial mass-flow cellular automata with local parameter field | Differentiable competing NCAs; outer population of trained worlds | Individual agent genes, energy, predation, reproduction and lineages |
| What is actually optimized? | Directed tasks explicitly optimize external fitness; intrinsic-evolution arm depends on mass competition, mutation beams and engineered food/dissipation | **Inner territorial gain** (explicit differentiable loss) and **outer designed `novelty + DINOv2 visual diversity`** | No outer novelty optimizer in examined evaluation; organism behavior follows designed survival/reproduction rules |
| Mechanism of variation | Spatial mutation beam `N(0,1)` on parameter field and stochastic mass-based rule selection | Copies full elite world state + optimizer + hyperparameters, then hyperparameter/weight mutation | Cloned descendants, per-gene mutation probabilities |
| Unit called species/organism | **Exact parameter vector** despite arbitrarily small difference | Competing alive-mask "agents" **and** outer "world lineages" | Heritable gene component for OEE statistic (agent/sensor units not assessed) |
| Raw novelty/evolution metric | Mass-weighted count and non-neutral EA plus parameter diversity and PCA | Archive descriptor kNN novelty plus DINOv2 cosine difference and derived spatial complexity | Cumulative gene-component evolutionary activity |
| Main correction / neutralization | Divide raw EA by **total system mass** to address food/dissipative inflow; **ranking reverses** | Compare to fixed-PD-NCA and equal-budget random search, **but primary score is the selection target** | Random neutral shadow model with periodic reset; normalized activity bounded, **new activity null all 20 runs** |
| Long-horizon published budget | 500,000 steps, 5 seeds | 500 meta-iterations, 30 worlds, world horizon 12, 3 seed runs for plotted aggregate | 20 runs × 2,000,000 steps |
| Evidence supported | Localized patterns, changing param populations; EA varies by conditions | Outer optimizer produces visually differentiated morphologies and stable multichannel coexistence under chosen scores | A particular gene-level Tokyo T1 OEE test does **not** pass in any of 20 trials |
| Not demonstrated | Genuine species/offspring lineage with inherited new function; infinite novelty | Independent inner organismal evolution without novelty objective; general intelligence | Absence of OEE under all component definitions or time horizons; digital consciousness |

## Three forms of metric leakage
**Resource leakage (Flow-Lenia):** if activity counts scale with material throughput, a larger resource supply can appear like more adaptation. A normalization can reverse interpretation. But normalization is also a model choice: don't simply divide *all* metrics by mass.

**Objective leakage (PBT-NCA):** when the selection target is the novelty metric, improved novelty score is evidence of optimization on the metric. To claim *organismal innovation*, use a separate held-out functional-organization measure and remove external feedback.

**Component/neutral-baseline leakage (ToLSim):** if components are gene values rather than ecological organisms, novelty conclusions may be highly sensitive to segmentation; neutral-shadow corrections can cause raw-positive trends to disappear. Define comparison units and neutral process beforehand.

## A shared minimal scientific panel (future experiment only)
1. **Causal maintenance:** constituent turnover and recovery with a critical repair link knocked out.
2. **Resource accounting:** actual conservation/reservoir inflow/waste rather than free "energy" score.
3. **Lineage validity:** parent-linked new entity, demonstrated inherited behavior, no engine copy-only shortcuts.
4. **Functional novelty:** a new independently assayed ecological resource/interaction affordance over an unseen condition.
5. **Ecological inheritance:** niche construction/competition/symbiosis persist after suppressing external novelty or fixed-task rewards.
6. **Open-ended hallmarks:** per-world sustained *new functional* event rate and organizational transitions, with neutral controls and preselected finite time windows.
7. **Compute balance:** compare each method to within-substrate controls first, avoid comparing 500 meta-iterations with 2m steps or T4 GPU microseconds.

## Highest-information proposal
**A research hypothesis, not a claim:** *hereditary, causally validated functional innovation per conserved resource budget* may be a more robust long-horizon measure than parameter count, visual novelty or raw evolutionary activity alone.

**Falsifier:** such a measure can be gamed by externally injected behaviors, cannot reliably identify offspring, or is uncorrelated with hidden adaptation. If this happens, abandon the metric rather than using it to proclaim progress.

## References
- [Flow-Lenia full review](16-flow-lenia-2025-full-review.md); [primary full text](https://arxiv.org/html/2506.08569v1).
- [PBT-NCA full review](17-pbt-nca-2026-full-review.md); [primary full text](https://arxiv.org/html/2604.11248v2).
- [ToLSim full review](18-tolsim-2026-full-review.md); [primary full text](https://arxiv.org/html/2603.01701v1).
- [Earlier chemical model full review](12-chemical-replication-full-review.md).
- [ALife evaluation framework](05-evaluation-framework.md).
- [Counterevidence](14-negative-results-and-measurement-disagreements.md).

**No organism, training, simulation or offline paper metrics recalculation occurred in this pass.**
