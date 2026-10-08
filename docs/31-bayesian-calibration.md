# Probabilistic intelligence: how a model should represent not knowing

**Research status:** primary papers and venue abstracts examined; all numbers are author-reported; no local calibration benchmark run.

## The central mistake to avoid

Three quantities often get collapsed into one confidence score:
- **Predictive probability**: a model's probability of a specific next token or class conditional on its inputs;
- **Epistemic uncertainty**: uncertainty because model/data lacks knowledge about the relation or mechanism;
- **Evidence reliability**: whether an external document/measurement is likely to be correct and relevant.

Those are different. In particular, a fluent language-model sentence about confidence is not by itself a calibrated probability that a multi-clause answer is true.

## Mathematical entry points

**Bayesian update:** `p(θ|D) ∝ p(D|θ)p(θ)`; predictions average over possible parameters: `p(y*|x*,D) = ∫ p(y*|x*,θ)p(θ|D)dθ`. Exactly computing these posteriors is typically intractable for large neural nets.

**Variational inference / ELBO:** `log p(x) ≥ E_{q(z|x)}[log p(x,z) - log q(z|x)]`. Reparameterization writes `z = μ(x) + σ(x) ⊙ ε`, `ε∼N(0,I)`, making Monte Carlo differentiation practical for certain continuous latent families. See [Kingma & Welling](https://arxiv.org/abs/1312.6114).

**Deep ensembles:** train multiple genuinely distinct parameter estimates/seeds; aggregate predictive distributions and evaluate their spread. Independence is imperfect; cost scales with model count. See [Lakshminarayanan et al.](https://arxiv.org/abs/1612.01474).

**Monte Carlo dropout:** keep dropout active at inference, average multiple predictions; interpretable as one form of approximate Bayesian inference under specific assumptions—not an exact posterior and not a universal uncertainty oracle. See [Gal & Ghahramani](https://arxiv.org/abs/1506.02142).

**Temperature scaling:** `p_T(k|x)=softmax(z_k/T)`; choose T using **development outcomes**, then evaluate on a separate sealed test. It changes probabilities, not class ranking for a fixed multiclass logit vector. It may fail under dataset shift. See [Guo et al.](https://arxiv.org/abs/1706.04599).

## Diagnostic metrics

| Score | Definition/meaning | Misinterpretation |
|---|---|---|
| Accuracy | Fraction of correctly graded outputs | Doesn't say whether confidence is justified |
| Brier score | Mean squared probabilistic error for binary outcomes | Can improve by changing prevalence or task mixture |
| Log loss / NLL | Penalizes confident wrong predictions strongly | Undefined at exact 0/1 without careful clipping |
| ECE | Difference between mean confidence and empirical accuracy in bins | Depends on bins and sample count; not a single complete metric |
| Risk vs coverage | Error rate among predictions not abstained from | Can appear good by refusing everything |
| Selective accuracy | Accuracy on accepted predictions at a fixed coverage | Depends on comparable task and threshold |
| Source-confidence score | Probability externally supplied evidence is accurate | Cannot be treated as model correctness without calibration |

## A useful 2026 convergence

[IJCAI Double-Calibration](https://www.ijcai.org/proceedings/2026/77) describes separately calibrating structured knowledge-graph evidence and confidence in the downstream reasoning step. That suggests a testable design principle: don't let a language model simply reuse a source's reported certainty as its own answer confidence. The [2026 uncertainty survey](https://doi.org/10.1007/s11390-026-6426-z) highlights broader predictive calibration challenges.

**Original hypothesis H12:** combining an independently calibrated retrieval/source reliability score with separately calibrated inference confidence reduces severe confident factual errors in changing-source tasks relative to a one-number LM self-rating. Falsifier: no improvement at matched risk/coverage or the improvement disappears under a different source domain.

## E23 implementation plan
1. Generate binary ground-truth tasks with known/unknown answers and independently controlled source errors; **do not** put test labels in controller features.
2. Use an existing model's frozen outputs, scores and retrieved citations (or synthetic predictive scores for a *metrics-only harness*).
3. Compare raw confidence, temperature scaling, ensemble disagreement, and two-stage source+answer calibration with matched validation set.
4. On held-out tasks report Brier, NLL, ECE (with uncertainty), selective risk, false refusal and answer accuracy.
5. Shift source reliability after fitting. Calibration quality under shift must be measured, not presumed.
6. Record per-item probabilities, bin edges, sample size, costs and model identity.

## Why it matters for next-generation AI
For tool-using agents, uncertainty guides **whether to act, gather new evidence, run a verifier or abstain**. Good calibration may improve safety and resource allocation even if the backbone's raw benchmark accuracy never changes.

## Evidence limits
Classical calibration papers often use image/document classification; their assumptions do not automatically extend to generative factual claims, unknown answer space or composite tool outcomes. No source here proves that a particular confidence threshold transfers between models or applications.
