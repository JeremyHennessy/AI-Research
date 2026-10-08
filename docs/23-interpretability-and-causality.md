# Mechanistic interpretability, causal learning and faithful explanations
**Source-backed engineering synthesis; no internal model experiment executed here.**

## 1. What we actually need to explain
A model can give a good final answer, a persuasive explanation of its answer, or an answer caused by a specific internal computation. Those are three different propositions. **An association between a hidden feature and a concept does not by itself establish causation or faithfulness.**

A useful chain is: **observe activation** → discover candidate representation → intervene on it → measure targeted and collateral effects → test on out-of-distribution prompts → decide whether the feature is useful for auditing.

### Common techniques
| Tool | What it measures | What it does *not* establish | First experiment |
|---|---|---|---|
| Attention maps | Which positions received high attention weights | That high attention caused the output | Counterfactual token patching |
| Linear probes | Whether a property can be decoded from activations | That the model used the decoded information | Activation intervention after probe |
| Sparse autoencoders | A sparse dictionary approximating layer activations | Unique true model features | Reconstruction vs intervention audit |
| Activation patching | Effect on output of swapping activation from different run | All causal pathways or generalization | Paired minimal examples |
| Attribution graphs | Candidate flow of influence among learned features | Complete faithful causal explanation | Retest under changed prompts/tasks |
| Feature steering | Effect of amplifying/suppressing feature directions | Robust safe intervention without collateral harm | Paired benign tasks and shift |
| Natural-language autoencoders | Model-generated description of internal activity | Complete introspective access or consciousness | Faithfulness on hidden activation labels |
| Model diffing | Differences between versions/models | Reason for an observed difference by itself | Inject known change and test detection |

**Source foundations:**
- [Scaling and evaluating sparse autoencoders (2024)](https://arxiv.org/abs/2406.04093) studies k-sparse dictionaries and quantitative interpretability metrics.
- [Circuit-tracing tools (Anthropic, 2025)](https://www.anthropic.com/research/open-source-circuit-tracing) includes attribution graphs and feature interventions.
- [Natural Language Autoencoders (Anthropic, May 2026)](https://www.anthropic.com/research/natural-language-autoencoders) attempts to render internal activations in language; quality must be measured externally.
- [A global workspace in language models (Anthropic, July 2026)](https://www.anthropic.com/research/global-workspace) reports a relatively small shared internal neural workspace. Do **not** equate resemblance to a cognitive theory with demonstrated machine consciousness.
- [Cross-architecture model diffing (Anthropic, March 2026)](https://www.anthropic.com/research/diff-tool) uses learned features to surface changed behavior across models.
- [Retrieval-aware hybrid attention (ICML 2026)](https://proceedings.mlr.press/v306/bick26a.html) shows that a small selected subset of heads can be disproportionally important for associative recall under studied tasks.

## 2. Causal representation: mathematical model
Structural causal model:
```
X_i := f_i(Pa_i, U_i)
```
where parents Pa_i and exogenous factors U_i determine state variables. Three levels of claim require different evidence:
- **Association:** observational `P(Y|X=x)` — a correlate can predict without controlling Y.
- **Intervention:** `P(Y|do(X=x))` — change X and test consequent change in Y under controlled conditions.
- **Counterfactual:** “had X differed for *this same unit*, would Y have changed?” This generally requires stronger identifiability assumptions.

Original work [Towards Causal Representation Learning (2021)](https://arxiv.org/abs/2102.11107) highlights the challenge: relevant causal variables are not given as labels in raw pixels or tokens. The 2026 [Causality Is Key for Interpretability Claims to Generalise](https://proceedings.mlr.press/v306/joshi26a.html) warns against inferring intervention and out-of-distribution causal behavior from correlational feature alignment alone. [Interpretability Can Be Actionable](https://proceedings.mlr.press/v306/orgad26a.html) argues explanations should lead to validated decisions.

## 3. E14 — intervention-based feature audit
**Question:** does an explanation feature actually control a specific model behavior robustly?

**Accessible base:** small open-weight model under compatible license; publicly released attribution/SAE tools if supported; otherwise a simple local probe/patching implementation.

**Dev data:** minimally paired prompts differing only in a target concept (e.g., output JSON vs prose, topic, retrieved source position). **Hidden data:** unseen templates/topics/lengths. **Interventions:** suppress feature, amplify feature, patch from control run, randomized direction, matched-norm null direction.

**Metrics:** intervention causal effect on intended outcome, collateral regression on unrelated tasks, calibration, reconstruction fidelity, stability across seeds/layers, effectiveness under unseen prompts.

**Falsifier:** beautiful/high-accuracy probe labels do not predict causal interventions or fail under distribution shift.

## 4. E15 — learning causal state for unseen mechanisms
**Question:** does a compact representation predict interventions more robustly than one trained solely for next-observation prediction?

Build a small procedural dynamical environment with independent latent variables (object identity, friction, blockage, key possession) and intervention API. Exclude certain mechanism combinations from training. Compare observational sequence model, hand-coded state estimator, contrastive/structured latent model and an explicitly intervention-trained representation at matched data and compute.

**Metrics:** interventional transition accuracy, new-task success, calibration, intervention-effect prediction; measure model-size/latency cost. **Falsifier:** strong in-distribution predictions but no transfer on hidden mechanism interventions.

## 5. Common overclaims to avoid
- “One neuron means concept X” without tests for polysemantic features and correlated effects.
- “The reasoning trace is the model's true chain of thought” without causal validity tests.
- “Feature steering is a robust safety guarantee” without adversarial and collateral evaluation.
- “Global workspace implies consciousness” without an operational and broadly accepted consciousness test.
- “Sparse reconstruction loss low” means explanations are human-useful; it often does not.

## 6. Source map for next full-paper read
[2026 causal critique](https://proceedings.mlr.press/v306/joshi26a.html), [2026 actionable critique](https://proceedings.mlr.press/v306/orgad26a.html), [2026 frozen-model adapters](https://proceedings.mlr.press/v306/pepper26a.html), [2026 system-level interpretability](https://proceedings.mlr.press/v306/zhu26bk.html).

**Status:** abstracts and public lab releases reviewed, not all full PDF sections or appendices. No local experimental results.
