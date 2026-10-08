# Evaluation and validation cookbook

## 1. Principles
A benchmark is a test fixture, not the goal of intelligence. Never evaluate only on a single static benchmark with a long history of public solutions. Hold model, harness, tool access, compute and tuning effort constant. Audit contamination. Report costs, failures and uncertainty alongside point scores.

## 2. Multi-dimensional scorecard
| Dimension | Measurement | Typical pitfalls |
|---|---|---|
| Correctness | exact, unit-test, or trusted domain-specific outcome | Prompt/answer leakage |
| Calibration | confidence vs observed correctness; ECE/Brier when meaningful | Self-reported confidence not probabilities |
| Abstention | risk-coverage curve and severe-error frequency | Always refusing "wins" risk metric |
| Robustness | rephrasing, distractors, domain shift, adversarial examples | Generated variants too similar |
| Long-horizon | success by steps; tool recovery; planning resets | Partial successes mistaken for completion |
| Memory | retrieval recall, freshness, temporal supersession, deletion | Future data leaked into past |
| Efficiency | quality per joule, latency, token and dollar cost | Hardware and batch confounds |
| Security/safety | prompt injection, boundary crossing, policy adherence | Judge accepts persuasive unsafe text |
| Transfer | unseen generator/task family and future data | Hyperparameters tuned to hidden test |

## 3. Benchmark families and appropriate use
- **HELM:** broad, multi-metric scenarios; useful for a scorecard, not a proof of general intelligence. https://arxiv.org/abs/2211.09110
- **LiveCodeBench:** timestamped coding tasks; freeze exact release and ensure no test in training. https://arxiv.org/abs/2403.07974
- **SWE-bench:** realistic repo issues and executed tests; check versions, contamination and environment setup; expensive. https://arxiv.org/abs/2310.06770
- **AgentBench:** interactive tasks across environments; validate that the harness and tools have not been modified. https://arxiv.org/abs/2308.03688
- **Custom procedural tests:** best for hidden rule transfer, but establish face validity with human review and avoid overly simple toy success.

## 4. Pairwise comparison
For each of n common tasks compute diff_i = metric_B_i - metric_A_i. For binary correctness, report mean(diff), wins/losses/ties and a paired bootstrap confidence interval resampling task IDs. Cluster by problem family if examples are correlated. Random seeds capture optimizer/sampling variation; show both across-seed and across-example variability. Predeclare primary metric and number of comparisons.

An example acceptance rule (must be chosen before looking at holdout): require lower bound of a 95% paired confidence interval to exceed 0 **and** point estimate to exceed an application-specific minimum useful effect, with no unacceptable severe safety failures. A single favorable p-value is not sufficient. Small samples may be inconclusive.

## 5. Cost matching
Compare at equal average response budgets AND report tails; alternative curves should display quality against **actual** generation tokens, evaluator calls and end-to-end time. For an architecture compare actual training FLOPs, active parameters and data mixture plus serving load. If model size changes, make it a measured experimental axis, not a hidden confound.

## 6. Anti-leakage program
1. Hash exact content and normalize near-duplicates of training/development/evaluation inputs.
2. Split by author, project, time, source, or latent task generator as appropriate.
3. Exclude both questions *and solutions* from train, retrieval cache, few-shot examples and feedback logs.
4. For online agents, freeze tools/memory and all derived content before hidden test.
5. If a test influenced engineering decisions, retire it to development.
6. For stochastic outputs, commit to seeds and aggregation method.

## 7. Threat and failure tests
- **Prompt injection:** malicious tool/web/document strings attempting to override instructions.
- **Tool errors:** timeouts, corrupted payloads, changed schemas, stale response.
- **Memory failure:** false memory, outdated facts, unauthorized recall, deletion not propagated.
- **Reward hacking:** passing superficial verifier without satisfying the real objective.
- **Distribution shift:** new entity, layout, language, sequence length, unseen action affordance.
- **Model uncertainty:** ambiguous problems, no solution, or evidence conflict.
- **Safe autonomy:** halt when action outside approved sandbox or irreversible side effect.

## 8. Review and incident records
Tag errors: reasoning, retrieval, execution, interface, data quality, judge flaw, environment nondeterminism, safety, instrumentation. Root cause must be supported by traces. Negative and neutral outcomes are retained. Never alter an approved presentation/UX solely to conceal model or data failures.

## 9. What not to conclude
- An author's published improvement implies replication here.
- High chain-of-thought length guarantees better reasoning.
- More environment steps imply more learning.
- High benchmark pass rate means robustness to unseen tasks.
- A large context window proves effective memory.
- More total MoE parameters mean greater runtime cost than a dense model.
