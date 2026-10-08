# PBT-NCA (2026) — complete arXiv v2 methods, scoring, results and limitations review

**Evidence: E2 research-paper audit, not a model reproduction.** Primary [arXiv v2 HTML](https://arxiv.org/html/2604.11248v2) dated **22 June 2026**; authors Uljad Berdica, Jakob Foerster, Frank Hutter, Arber Zela. Licensed CC BY 4.0 for manuscript. Public implementation [arberzela/pbt-nca](https://github.com/arberzela/pbt-nca), inspected Git head `7eb61b6a240db6ae53fd044d8906c2633af0503c`, root code LICENSE **MIT**; optional models/datasets carry separate rights. **Nothing was run or trained.**

## Executive result: the "openness" driver is a designed optimizer

The system is a population of differentiable competitive Petri-Dish neural cellular automata, selected by an **explicit outer objective** `F_i = N_i + D_i`:
- `N_i` = *archive novelty*: hand-authored descriptors of agent occupancy, temporal variation and turnover, with k-nearest-neighbor distance to the archive.
- `D_i` = *contemporary visual diversity*: frozen **DINOv2** features of trajectory frames, using median cosine distance to other worlds at the same time step.

The substrate's **inner objective** is also explicit: agents optimize their territorial "aliveness" via gradient descent on negative log total alive mass. The outer process copies good world's parameters and state and mutates them to keep producing behaviors pleasing the two novelty signals.

**Interpretation:** PBT-NCA demonstrates that externally guided meta-evolutionary search can find varied emergent-looking cellular dynamics. The results do **not** demonstrate a goal-free internally evolved organism, an inherited organismal genome, or independently rising functional repertoire after removal of the designed novelty objective.

Source: [§3 population and composite scoring](https://arxiv.org/html/2604.11248v2#S3).

## 1. Two separate time scales and objectives
### Inner world / local territorial adaptation
A world contains several NCAs plus environment represented in spatial grid. At each pixel, competing proposals are weighted by softmax of pairwise interaction strengths, and resulting state is clipped. **Alive mask threshold `α=.4`** means an NCA occupies the cell only if its contribution exceeds the threshold; otherwise its local alive status is 0. This *aliveness* is a designer-defined signal, not evidence of cellular metabolism.

NCA parameter update `θ_k ← θ_k − η_k ∇_θ [−log Σ_{u,v} A_k(u,v)]` explicitly seeks to grow its grid territory. This is reinforcement-like training within a sandbox, not evolution of a previously unknown survival objective.

### Outer PBT population search
A world checkpoint includes: NCA parameters, **optimizer state**, grid state, and hyperparameters. Each meta-iteration rolls out `T_world` steps, calculates novelty and visual diversity, appends elite behavior descriptors to a **FIFO** history, and replaces poor worlds with modified copies of high-scoring worlds.

Hyperparameter crossover retains copied parent value with probability `0.5` or the previous child's value otherwise; mutation scales chosen hyperparameters by `0.8` or `1.2` with probability `0.1`, then clips valid ranges; independent Gaussian weight perturbations explore nearby systems. This is a **Lamarckian copying operation across researcher-managed worlds**, not organism-level reproduction.

Source: [§3 algorithm and exploit/explore](https://arxiv.org/html/2604.11248v2#S3).

## 2. What the scores encode
**Behavior descriptor** computed from alive-mass faction trajectories (agents plus environment):
- Mean occupancy `μ`,
- Temporal standard deviation `σ`,
- Turnover `δ`.

**Archive novelty `N`:** Euclidean distance to `k=8` nearest historical descriptors; after each iteration add `m=2` elite descriptors; FIFO archive has finite capacity, and clearing/reset may be enabled.

**Visual diversity `D`:** DINOv2 embeds sampled frames from each world and measures `1−cosine_similarity`; world score is median distance to contemporaneous worlds, then average across frames. This rewards **different appearance and dynamics by pretrained representation**, not experimentally tested new ecological function.

**Consequences:** a world can improve `F` while never producing a reproducible descendant with new function; evolutionary selection deliberately pushes novel patterns; ranking may be susceptible to visual artifacts or population-comparison artifacts. Paper's authors themselves caution about DINOv2 **natural-image biases**.

## 3. Published experimental parameters and comparisons
| Field | Paper v2 | Replication implication |
|---|---|---|
| Meta population `P` | **30 worlds** | "World" is optimizer unit, not biologically descended organism |
| Meta-iterations `T` | **500** | Finite budget, cannot demonstrate endless novelty |
| Inner rollout `T_world` | **12** | Cumulative up to 6000 inner updates/world under author account |
| Exploit interval `K` | **5** meta-iterations | Selection/replacement cadence externally set |
| Fraction replaced `ρ` | **0.25** | Bottom 25% replaced |
| Agent count | Usually **3**; includes 5 and 7 in scalability | Compare worlds with identical agent count |
| Runs | **3 independent PBT runs** for Figure 9 mean & SD | Need world-level uncertainty; no E3 here |
| Optimizer | Adam, LR and batch size adapted | Learning occurs by gradient objectives |
| Param search | LR 1e-6..1, batch size 1..8, steps/update 1..64; extended temp and fraction-update | Different architecture/hyperparam budgets must be matched |
| Baselines in §4 | Fixed-hyperparameter original PD-NCA and **Random Search** with P=30 and equal total 6000 inner iterations | These are useful controls but **not** an organismal function/lineage verifier |

Authors report higher composite scores and novel visual regimes relative to those controls. This is **author-reported, task and score-specific**; a novel image descriptor is not proof of "true open-endedness" independent of external novelty incentives.

**Code-vs-paper distinction:** the inspected public `configs/slurm_h100_pbt_scale_small.json` includes `n_seeds=4` (a **within-world initialization setting**, not the count of independent paper runs); README's SLURM scripts use three separate experiment array seeds `--array=0-2`. Public source snapshot has `pbt_vlm_enabled=false` in one combined-selection config; the main v2 paper evaluates DINOv2, not an always-enabled VLM. Do not confuse these settings.

Source: [§4 Experiment/Results](https://arxiv.org/html/2604.11248v2#S4) and [official code README](https://github.com/arberzela/pbt-nca).

## 4. Reported numerical observations vs what they measure
For **7-agent PBT-NCA**, the article reports:
- **Ecological persistence EP ≈ 1.0** defined as fraction of frames where pixel-level species-entropy `H_t` exceeds `ε=0.1 log₂(N)`. This measures **multi-agent coexistence by a chosen entropy threshold** within fixed rollouts, not organisms surviving beyond experimental intervention.
- Mean species entropy `≈2.3 bits`, around 82% of maximum `log₂ 7`, indicating diversity under the chosen metric.
- **Effective complexity `≈0.21±0.05`**, defined as normalized spatial entropy multiplied by `(1 − LZ77 compression ratio)`. The score is constructed to be low for both ordered and nearly incompressible random patterns.
- Images show "shooter," "glider," "amoeba" and ejected clusters. These are **phenomenological descriptors**, not a verified separate offspring with inherited new ecological function.
- Increasing number of NCA agents (3,5,7) was associated with higher later-stage novelty by the report's own score.
- The composite objective and novelty improve after early decline; score trajectories were averaged over **three runs**, not an unlimited-duration test.

Source: [§4 effective complexity](https://arxiv.org/html/2604.11248v2#S4), Figure 12, and [§5 discussion](https://arxiv.org/html/2604.11248v2#S5).

## 5. Important limitations from the primary authors
- Two-dimensional physics omits real thermodynamic and ecological constraints.
- Visual DINOv2 can inject **anthropocentric/natural-image bias** into what counts as novel.
- Persistent phenomenological diversity over **500 meta-iterations** is not evidence of asymptotically unbounded functional innovation.
- Worlds have **explicit reward/learning objectives and researcher-managed population copy/mutation**; true within-world heredity and metabolic independence are not measured.
- Reported "spore-like" dispersal may be spatial colonization without independent viable offspring identity.
- The article does not establish consciousness or independently evolved generalized cognition.

## 6. What should be tested in a future separately authorized project
**Primary proposed discriminator:** freeze the evolved worlds and turn off the *outer* novelty/diversity selection (no further PBT) under matched resource/physics conditions. Track whether **new inherited functions** continue emerging *inside the world* rather than during researcher-managed replacement. Compare:
- Combined `N+D` (paper),
- `N` alone,
- `D` alone,
- Random-resampling with equal compute,
- Fixed PD-NCA,
- No outer-selection continuation,
- Independently measured environmental viability and offspring reproduction.

**To falsify intrinsic-life claims:** if "open-endedness" tracks external DINO/descriptor improvements but not new functional capabilities or individual descendants, report **novelty-optimized morphological discovery**, not organismal life. If external optimizer is removed and developments stop, attribute discoveries to it honestly.

**Scope:** entire public v2 main text read (algorithm, methods, examples, quantitative results, discussion/limitations); repo README, license and one JSON config inspected but **no full code security audit or execution**. Therefore E2 literature review, not replicated E3.
