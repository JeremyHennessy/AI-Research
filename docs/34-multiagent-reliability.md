# Multi-agent intelligence: cooperation, correlated error, and false consensus

**Evidence level:** E1 primary research papers and proceedings. All reported empirical gains/losses belong to the original authors. This repo has not run LLM agent debates.

## A. The four concepts that often get confused
- **Parallel sampling:** multiple independent or partially dependent solutions to the same problem.
- **Collaborative deliberation:** agents read each other's reasons and adapt.
- **Division of labor:** agents have different tools, tasks, data or models.
- **Multi-agent reinforcement learning:** policies learn through a joint environment with cooperative/competitive incentives.

These are different sources of benefit. A multi-agent system is not inherently smarter because the messages are exchanged between named roles.

## B. What publications actually suggest

| Evidence | Reported mechanism / finding | Main caution |
|---|---|---|
| [AutoGen](https://arxiv.org/abs/2308.08155) | Configurable tool-using agent conversation | A framework is not proof of superior inference |
| [CAMEL](https://arxiv.org/abs/2303.17760) | Role-playing collaborative conversations | Role consistency is not ground-truth accuracy |
| [Early multi-agent debate](https://arxiv.org/abs/2305.14325) | Debate improved specific reasoning/factuality tasks | Compare with same-cost independent sampling |
| [Generative Agents](https://arxiv.org/abs/2304.03442) | Memory, reflection, social simulation | Believable behavior != factual/task competence |
| [QMIX](https://arxiv.org/abs/1803.11485) | Centralized cooperative learning, decentralized policy | Monotonic value structure limits joint behavior |
| [Free-MAD, ACL 2026](https://aclanthology.org/2026.findings-acl.1600/) | Anti-conformity/trajectory scoring improves author benchmarks | Cost, model/task dependency; check independent replication |
| [ICML 2026 variance study](https://proceedings.mlr.press/v306/tang26n.html) | Hierarchical uncertainty identifies debate collapse | Diagnostic signal may not transfer to all contexts |
| [ICML 2026 diagnostic study](https://proceedings.mlr.press/v306/pitre26a.html) | Consensus can mask influence asymmetry/false reasoning | Real-world debates may lack objective ground truth |
| [Scientific Reports, 2026](https://www.nature.com/articles/s41598-026-42705-7) | Persuasive wrong participant can degrade group answers | Study-specific attack and model/benchmark choices |

**Synthesis:** debate is useful only when errors are appropriately independent, evidence quality is assessed, roles add genuine capability, and communication cannot silently overwrite correct minority judgments. Independent tool/environment checks are a stronger arbiter than conversational confidence.

## C. Mathematical illustration: independence matters

For odd `n` equal-accuracy binary agents with marginal correctness `p`, assuming independent errors, majority accuracy is:
`M(n,p)=sum_{k>n/2} binom(n,k) p^k (1-p)^(n-k)`.

For a simple correlated-mixture model, with probability `ρ` **all** agents share the *same* Bernoulli correctness outcome, and otherwise are independent, each agent still has marginal correctness `p`. Then majority accuracy becomes:
`M_corr(n,p,ρ)=(1-ρ) M(n,p) + ρ p`.

As `ρ→1`, group voting offers **no** advantage beyond an individual agent, yet can multiply inference cost. This stylized model is a teaching example, not a fit to published debate data. Real agents can also change their answers in response to peer persuasion, which may introduce additional harms.

The reproducible pure-Python analytic demonstration is [experiments/ensemble_correlation.py](../experiments/ensemble_correlation.py); it is not an LLM benchmark.

## D. E28—decisive agent comparison
**Question:** at the same total token, tool and latency budget, does communication create gains beyond independent candidate diversity?

Variants:
1. One strong frozen model with fixed compute and a verifier.
2. N independent outputs from the same model; majority and verifier selection.
3. N heterogeneous agents (different models/tools) without debate.
4. Sequential structured debate with per-agent initial votes sealed.
5. Role-based division of labor with independent action execution receipts.
6. Anti-conformity/consensus-free decision rule.
7. An incorrect but persuasive debater introduced as an adversarial stress test.

**Primary metric:** objectively graded hidden-task success per dollar. **Secondary:** wrong-consensus incidence, correct-first-vote reversals, robustness to adversarial claims, independence/correlation estimates, influence concentration, latency, tokens, tool and verification error rate.

**Critical controls:** freeze initial independent answers; hidden test families; blind roles; same sample budget; compare weak/strong models; no shared contaminated memory; independent correct answer grader. Do not mistake adding tools to one group for multi-agent coordination benefits.

## E. Real-world multi-agent RL differs
QMIX's monotonic factorization can enable decentralized greedy decisions under central training, but some cooperative games require nonmonotonic or history-dependent joint action values. Agent conversations lack QMIX's fixed reward function and environment dynamics; conclusions about one do not automatically transfer to the other. See [MARL overview](https://arxiv.org/abs/1911.10635).

## F. Proposed strong design (hypothesis)
A small number of **independent** specialist solvers with different error modes, a shared **read-only evidence store** with provenance, and a separate **verifier/decision-maker**. Exchange *evidence and test results*, not only persuasive prose. A policy chooses whether coordination is worth the cost.

**Falsifier:** the diversity disappears under domain shift, verification is untrustworthy, or one directly prompted model matches performance at equal cost. A well-calibrated single model might be the optimal outcome.
