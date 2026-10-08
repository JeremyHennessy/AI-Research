# Reasoning, data quality, reward and scientific evaluation — 2026 pass
**Review depth:** official primary abstracts, proceedings descriptions and publicly disclosed model notes, not independent full-scale replication.

## A. "Reasoning" is not one operation
Four distinct interventions frequently blur together:
1. **Pretraining representation:** the model learns to predict diverse sequences.
2. **Instruction and process demonstrations:** supervised trace imitation.
3. **Reinforcement learning:** choices are pushed toward reward by an optimization process.
4. **Inference-time compute:** generate, sample, search, verify and stop; base model weights do not change.

The experimental question is which layer causes the gain at the same data and compute budget. Long verbal chains may be irrelevant, misleading, or merely reflect more sampling.

### 2026 work and what to test
- [RLP — ICLR 2026](https://proceedings.iclr.cc/paper_files/paper/2026/hash/44a45e27879b8fbab6e123ad8b93afc2-Abstract-Conference.html): explores introducing reinforcement-style, information-gain-driven exploration near the end of pretraining, instead of treating RL only as posttraining. **Experiment:** compare equally long next-token-only continuation against mixed exploratory auxiliary objective; evaluate future-token loss and independent reasoning, not reward alone.
- [BRIDGE — ICML 2026](https://proceedings.mlr.press/v306/chen26an.html): proposes learning when SFT assists RL through a lightweight adapter and cooperative-gain signal. Authors report ~3+ points improvement on their math benchmark average over selected baselines. **Experiment:** SFT→RL vs naive SFT+RL blend vs cooperative scheduling at matched updates; check domain transfer and noisily rewarded problems.
- [Latent Exploration Decoding — ICML 2026](https://proceedings.mlr.press/v306/tan26d.html): reports some reasoning posttraining collapses sampling diversity; uses intermediate-layer distributions during decoding and reports modest pass@1/pass@16 improvements. **Experiment:** temperature sweep before/after posttraining with independently graded pass@k; test whether gains survive at equal verifier/sampling cost.
- [How Reasoning Evolves from Post-Training Data — ICML 2026](https://proceedings.mlr.press/v306/dionisopoulos26a.html): chess study distinguishes move correctness from **faithful reasoning**. **Experiment:** verify whether a rationale matches the actual action/action-quality; grade claims against independent symbolic state.

**Synthesis:** optimizing the answer alone can encourage reasoning-looking text unfaithful to the actual selected action. Use independently checkable actions or proof steps and test explanation faithfulness as a separate metric.

## B. RL objective — engineering primer
Let policy `πθ(y|x)`, old policy `πold`, reward `R(x,y)`. Policy gradient generally estimates an expectation of reward-weighted log-prob gradients, often with a baseline/advantage to reduce variance. PPO-type methods clip large policy updates, and relative/group methods normalize rewards among sampled responses to the same prompt.

In LLM RL, major variables include:
- sequence vs token-level advantage; probability-ratio clipping bounds;
- KL pressure toward a reference model;
- reward normalization and zero-variance groups;
- length truncation and incomplete reasoning;
- invalid outputs and verifier errors;
- online data sampling vs fixed demonstrations.
Exact DAPO and GRPO formulas are model/paper-specific; reproduce equations from the original training package, not approximate them as identical.

### Minimum adversarial RL check
Construct a verifier with deliberately imperfect unit tests, and keep an **independent hidden checker**. If the trained policy learns to satisfy the visible checker while failing hidden semantics, this is reward hacking. Record it as a scientific failure, not a victory. Use deterministic action receipts and sandboxing.

## C. Pretraining data is an optimization target
**Source evidence:**
- [Demystifying Synthetic Data, 2025](https://arxiv.org/abs/2510.01631) reports 1,000+ training runs and conditional effects: some mixtures of rephrased data plus natural text help; synthetic-only is not universally superior. The authors report favorable proportions near ~30% in their studied regimes.
- [Scaling Laws for Mixture Pretraining Under Data Constraints, 2026](https://arxiv.org/abs/2605.12715) studies constrained target data and repetition, reporting benefits from mixing many passes of scarce data with generic corpora under particular conditions.
- [Position: Multiple Definitions & Unrealistic Assumptions of Model Collapse, 2026](https://proceedings.mlr.press/v306/schaeffer26a.html) questions whether common extreme model-collapse narratives generalize to realistic practices.
- [When Sample Selection Bias Precipitates Model Collapse, 2026](https://proceedings.mlr.press/v306/qiao26c.html) cautions that biased data-verifier selection can discard important distribution tails.

**Combined inference:** controlled synthetic mixing can be helpful, but quality selection itself may silently erase minority patterns, difficult edge cases or rare languages. Neither "synthetic data inevitably collapses" nor "synthetic data is safe" is justified universally.

### Experiment E04 additions
Use a 2×3 study if compute permits: **source** (natural only, rephrased synthetic) × **mixture fraction** (0, moderate, high). A second factorial axis controls **source-filter bias** (uniform or biased to frequent distribution). Hold tokens and optimization fixed. Measure validation loss by topic, dialect, rarer entity types and unseen tasks; diversity statistics alone are not outcome metrics.

## D. Benchmark scores can hide the measured ability
[BenchMIRT launch, September 1, 2026](https://allenai.org/blog/benchmirt) describes multidimensional item response theory applied to roughly 100 models, 16 benchmarks and >34,000 individual questions. Author-reported analysis found separable latent capabilities. This reinforces an experimental lesson: two benchmarks with equal total accuracy can differ in what they measure and how they mix underlying skills.

**Our evaluation hierarchy:**
1. Objective checker on hidden generated fixtures.
2. Independent exact outcome on varied input distributions.
3. Human-labeled ambiguity and explanation faithfulness.
4. Robustness to altered wording, format, tool schema and time.
5. Cost/reliability/safety measured with the same attention as accuracy.

Keep **task families** separate during train/test, not just examples. Record how test construction can advantage one architecture.

## E. Scientific controls we should enforce
- Pre-register what constitutes a meaningful win.
- Compare at equal train FLOPs for training claims or equal inference time/tokens for inference claims.
- Use paired task outcomes and bootstrap uncertainty rather than anecdotal cherry-picking.
- Add counterexamples and cases where a technique should not help.
- Publish **negative** results into the private ledger, not delete them.
- Distinguish final-answer quality from process/reasoning faithfulness.
- Maintain a seal on hidden task generators; repeated peeking invalidates the holdout.

## F. Questions for Pass 3
1. Is the best RL stage order dependent on model quality/architecture?
2. Does verification-based search retain gains after changing verifiers and problem templates?
3. Is model-size scaling or smarter data mixture a better use of the next incremental GPU-hour?
4. Does adaptive computation improve expected utility after tail latency and severe errors are priced in?
5. Can we identify true learned algorithmic generalization rather than memorized verbal solution patterns?

**Recommended first priority:** reproducible E01 + E03 task-memory fixture + E02 inference controller. These produce clear falsifiable comparisons without requiring frontier compute.
