# Expert reading guide — how to turn 146 research records into usable knowledge

This is a **research curriculum and retrieval guide**, not an assertion that any individual—or the assistant's base model—has mastered or memorized all of AI. Read, test and challenge the papers; keep uncertainties visible.

## The nine questions an effective AI researcher must answer
| Question | First idea | Next technical read | Decisive practical check |
|---|---|---|---|
| 1. What does a neural network learn? | Optimization shapes statistical representations; labels/traces are proxies | [Transformer](https://arxiv.org/abs/1706.03762), [causal representation](https://arxiv.org/abs/2102.11107) | Train tiny model; compare fitting, transfer, causal intervention |
| 2. Where do improvements come from? | Data, parameters, compute, posttraining and tools affect results differently | [Chinchilla](https://arxiv.org/abs/2203.15556), [ICLR 2026 architecture scaling](https://proceedings.iclr.cc/paper_files/paper/2026/hash/dd2eb5250696753ea37141bbd89bb569-Abstract-Conference.html) | Matched FLOPs and training data |
| 3. Which representation is right? | Attention, recurrence, sparse routing, diffusion and byte-level patches trade costs | [Mamba-2](https://arxiv.org/abs/2405.21060), [hybrid distillation](https://proceedings.mlr.press/v306/bick26a.html), [Bolmo](https://arxiv.org/abs/2512.15586) | Matched-quality latency/context tests |
| 4. Can a model really reason? | True external outcomes differ from plausible verbal explanations | [DeepSeek-R1](https://arxiv.org/abs/2501.12948), [DAPO](https://arxiv.org/abs/2503.14476) | Hidden exact verifier and time/cost curves |
| 5. Can learning persist? | Weights, context and external event memory are different | [EWC](https://arxiv.org/abs/1612.00796), [AMA-Bench](https://proceedings.mlr.press/v306/zhao26bs.html) | Retention, correction, deletion and tool use |
| 6. Can an AI understand a world? | Observations may support predictive states; actions reveal mechanics | [DreamerV3](https://arxiv.org/abs/2301.04104), [Genie 3](https://deepmind.google/blog/genie-3-a-new-frontier-for-world-models/) | Unseen transition and intervention combinations |
| 7. Can it explain its behavior? | Probes are associations; interventions test mechanisms | [2026 causal critique](https://proceedings.mlr.press/v306/joshi26a.html), [circuit tracing](https://www.anthropic.com/research/open-source-circuit-tracing) | Hidden causal intervention prediction |
| 8. Can it act safely? | Objective, permission and evaluation failures need distinct controls | [Constitutional AI](https://arxiv.org/abs/2212.08073), [METR monitorability](https://metr.org/blog/2026-01-19-early-work-on-monitorability-evaluations/) | Monitor recall at fixed false positives; verified action receipts |
| 9. Can it discover new knowledge? | Candidate generation needs independent proof/test and novelty check | [AlphaEvolve](https://deepmind.google/blog/alphaevolve-a-gemini-powered-coding-agent-for-designing-advanced-algorithms/), [OpenAI math research](https://openai.com/index/sharing-ai-progress-in-mathematics/) | Executable correctness + reproducible result + prior-art review |

## Digest format: 90-second research cards
For each paper, make a concise record:
- **Question** (what problem and assumptions?).
- **Mechanism** (algorithm, loss, architecture, formula or data process).
- **Evidence** (source, methods, benchmark and cost, author-reported vs replicated).
- **Limits** (regressions, hidden costs, negative/contradictory work).
- **Application** (when would this improve our AI or research process?).
- **Discriminator** (smallest feasible counterexample or ablation).
- **What we know / don't know** (do not fill gaps by guesswork).

## Six controversial claims to investigate, not memorize as truths
1. **More reasoning tokens always improves correctness.** Counterexample: costly loops or poorly calibrated sampling can worsen accuracy.
2. **Long context equals long-term memory.** Counterexample: "lost in the middle", stale histories and update failures.
3. **Recurrent architectures fully replace attention.** Counterexample: exact associative recall requiring select heads.
4. **Synthetic data necessarily collapses models.** Counterexample: benefit from carefully mixed/rephrased data; contrary evidence around selection bias.
5. **Interpretable feature labels mean causal understanding.** Counterexample: correlated probes without transportable interventions.
6. **AI-discovered proof is automatically correct and new.** Counterexample: unformalized steps, invalid assumptions and known equivalent results.

## Reading triage rules
A source goes from **E0 discovery → E1 checked metadata/abstract → E2 complete methods + limitations review → E3 independent measured replication**. Prioritize contradictions and missing-source details over raw paper count. A public blog can supply a valuable training technique but is not a peer-reviewed replication. An independently verified result may still not transfer outside its evaluation distribution.

## A reproducible daily scan (manual or future scheduled)
1. Compare new dates/revisions in arXiv, ACL, PMLR, OpenReview, official lab technical reports, MLCommons and METR.
2. De-duplicate DOI/arXiv/OpenAlex identities and flag source conflicts (no automatic paper promotion).
3. Sample across underrepresented tracks; don't let reasoner hype displace safety, hardware, robotics and causality.
4. Select 1–3 meaningful sources for actual review, extracting architecture/formulas, assumptions and adverse results.
5. Add falsifiable next steps, update reading map, run offline CI.
6. Report exact commit, validation receipt, what changed scientifically and what remains unverified.
Never promote a paper based solely on counts or machine-generated abstract summaries.

## Two possible objectives—do not confuse them
**Becoming better informed** means a high-quality living knowledge base plus honest reasoning from documented evidence. **Building a better model** requires new reproducible training or inference experiments, costs and transfer success. The first makes the second possible; it does not imply it happened.
