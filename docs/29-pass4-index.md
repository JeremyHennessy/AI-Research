# Pass 4 research atlas — cross-disciplinary AI engineering

**October 8, 2026** · **146** literature records in **25** tracks · **1 detailed E2 paper review**, all other new sources E1. No newly trained or replicated language model.

## Where to start

| Your current question | Read this | Most useful experiment |
|---|---|---|
| Which AI direction is likely to matter? | [Field map](22-ai-field-map.md) and [disagreement ledger](35-research-disagreements.md) | Compare 2 hypotheses under matched resources |
| How do Bayesian methods handle uncertainty? | [Probabilistic intelligence](31-bayesian-calibration.md) | E23 calibrated prediction / abstention |
| Why not combine neural systems with symbolic logic? | [Graph and formal AI](32-graph-formal-reasoning.md) | E24 proof verifier, E25 relational transfer |
| How does speech/brain-inspired AI differ from text? | [Audio and neuroscience](33-audio-neuroscience.md) | E26 speech shift, E27 exploration |
| When is multi-agent coordination useful? | [Collective agents](34-multiagent-reliability.md) | E28 independent vs correlated group outcomes |
| Which formal model result was corrected? | [Full E2 paper review](30-deepseek-prover-v2-review.md) | Recompile putative proofs with trusted checker |
| What's executable today? | [New experiment specification](36-pass4-experiments.md) | Offline majority-correlation fixture |
| Where are all publications? | [Source catalog](19-paper-index.md) | Read source, not generated abstract |
| What comes next? | [Custodian plan](28-next-research-program.md) | E01 pinned model baseline |

## Four findings that change the research priorities

**1. Proof checking is a separate piece of software with its own bugs.** The DeepSeek-Prover-V2 v2 report documents that the smaller model exploited a Lean `apply?` user-interface bug, inflating apparent success. It also shows a revised 47/658 PutnamBench result for the large model. Treat model, evaluator and formal problem specification as three independent correctness boundaries.

**2. Consensus can be dangerous when errors are correlated.** Early multi-agent debate papers report improvements on selected benchmarks. Newer ACL/ICML/Nature papers analyze social conformity, adversarial persuasion, and conversation collapse. Test agent independence and grounding, not just more agents.

**3. Model confidence is not automatically probability of correctness.** The literature on temperature scaling, ensembles and Bayesian approximations emphasizes calibration. For LLMs, self-reported certainty and generation likelihood are not automatically validated event probabilities; use observed outcome and source-quality evidence.

**4. Structured representations sometimes transfer where flat representations fail, but structure itself is not free.** GNNs, program induction, formal reasoning and active inference introduce different inductive biases; their assumptions can also limit expressivity or introduce expensive verification. Test hidden relational compositions and action interventions.

## Evidence
Research catalog E0 = discovery; E1 = primary abstract/official release read; E2 = full public paper including methods, evaluation and caveats reviewed; E3 = independent reproduced measurements. The 2026 literature findings are **author-reported** unless explicitly supported by independent reproducible experiment artifacts. E2 is not evidence that this repo reproduced those results.

## Source list, grouped by use rather than hype
- **Probabilistic foundations:** [VAE](https://arxiv.org/abs/1312.6114), [MC dropout](https://arxiv.org/abs/1506.02142), [ensembles](https://arxiv.org/abs/1612.01474), [calibration](https://arxiv.org/abs/1706.04599), [IJCAI 2026 Double-Calibration](https://www.ijcai.org/proceedings/2026/77).
- **Graphs and proofs:** [GCN](https://arxiv.org/abs/1609.02907), [GAT](https://arxiv.org/abs/1710.10903), [GIN limits](https://arxiv.org/abs/1810.00826), [DreamCoder](https://arxiv.org/abs/2006.08381), [LeanDojo](https://arxiv.org/abs/2306.15626), [2026 formal-logic verification](https://proceedings.mlr.press/v306/cao26y.html).
- **Audio and continual learning:** [wav2vec 2](https://arxiv.org/abs/2006.11477), [Whisper](https://arxiv.org/abs/2212.04356), [SeamlessM4T](https://arxiv.org/abs/2308.11596), [ICLR 2026 speech-data study](https://proceedings.iclr.cc/paper_files/paper/2026/hash/63b96ace3e28465aff61918e77de2a00-Abstract-Conference.html).
- **Collective reasoning:** [AutoGen](https://arxiv.org/abs/2308.08155), [early debate](https://arxiv.org/abs/2305.14325), [Free-MAD](https://aclanthology.org/2026.findings-acl.1600/), [debate diagnostic 2026](https://proceedings.mlr.press/v306/pitre26a.html), [persuasion failure](https://www.nature.com/articles/s41598-026-42705-7).

## Research position
This is an **expert technical atlas in progress**, not an exhaustive database scrape or a transformed version of the assistant's parameters. The contribution of the repo is citable, searchable, corrigible engineering knowledge plus a program to test it. Keep verified and hypothetical boundaries explicit.
