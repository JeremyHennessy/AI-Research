# Pass 3 experimental portfolio — E14 through E22
**All experiments are proposals; none have been executed or verified here.** See [experiment protocol](04-experiments.md) and [evaluation cookbook](06-evaluation.md) for pre-registration and cost matching.

| ID | Hypothesis / independent variable | Baseline | Primary metric (hidden test) | Most informative falsifier | Resource tier |
|---|---|---|---|---|---|
| E14 | Causal feature intervention helps detect/model behaviors | Correlation-only activation probe | Held-out targeted intervention accuracy with collateral score | Probes look meaningful but interventions fail | Small open LM / GPU |
| E15 | Action-structured causal state improves OOD transitions | Observation-only dynamics learner | Success under held-out intervention combinations | Accuracy only on seen causal graph | CPU/GPU simulator |
| E16 | Continual adaptation can retain skills after changing data | Naive sequential fine-tune | Retention × new-task gain curve | Catastrophic forgetting not improved at same compute | Small net |
| E17 | Data curation reduces synthetic memorization exposure | Unfiltered controlled corpus | Synthetic canary reproduction rate vs utility | Utility drops without leakage reduction | Small LM |
| E18 | Independent monitoring+evaluation catches noncompliant agent effects | Prompt-only / same-model judge | False-negative rate at fixed false-positive level | Monitor misses unexpected error modes | Sandbox tools |
| E19 | World-grounded planning transfers to new embodied tasks | Hand-coded controller / plain imitation | OOD task success and safety violations | Simulation gain disappears with changed dynamics | Physics simulator |
| E20 | Adapter choice improves utility per GPU-hour | Frozen prompt/full fine-tune | Task score vs actual train+deploy cost | Quantization/rank breaks rare tasks | Consumer GPU |
| E21 | Verifier-guided candidate search discovers better algorithms | Random and rule-based search | Independently checked correctness and speed at matched total budget | Reported gain relies on weak tests or excessive search | CPU / code harness |
| E22 | Architecture-aware model serving improves cost/performance | Reference inference stack | Quality-normalized throughput / latency / energy frontier | Benefit vanishes at different batch or prompts | Serving GPU |

## Detailed run card (use for every idea)
- **Mechanism:** write why the independent variable should matter before coding.
- **Baseline and control:** same data, compute, model revision, optimizer/hardware and tuning rights wherever applicable.
- **Hidden test:** freeze task generator and constraints before tuning; record its hash.
- **Instrument:** exact tasks, sampled outputs, model revision, costs, time, cache settings, random seeds.
- **Outcome:** report point estimate and interval plus failure categories and uncertainty; **no headline win** from a cherry-picked subset.
- **Security & rights:** only lawful data, sandbox tools, no unapproved external actions.
- **Decision:** retain, reject or investigate with a new hypothesis; preserve negative runs.

## Candidate "small but decisive" sequence
1. **E16** toy continual-learning EWC vs replay vs adapters: first get metrics without huge training.
2. **E14** probe/feature causality on tiny open model: known intervention benchmark, controlled null features.
3. **E20** LoRA/QLoRA adaptation using pinned open weights if GPU available.
4. **E21** bounded program optimizer with exact independent tests and measured search cost.
5. **E15/E19** environment-transfer experiment with rules hidden by generator family.
6. **E22** measure real serving bottleneck before attempting MoE/low-bit rewrites.

## Fail-safe interpretations
- Mechanism not reproduced → record negative and recheck source assumptions.
- Accuracy gain with large extra cost → it is a cost-performance tradeoff, not free intelligence.
- Better retrieval/tool use, same weights → system capability improved; backbone not trained.
- Better benchmark after repeated tests → holdout contaminated; acquire new test set.
- Benchmark hacked → metric invalid, not a verified win.

Links: [Interpretability & causality](23-interpretability-and-causality.md), [alignment & security](24-alignment-and-security.md), [embodied science and hardware](25-embodied-science-hardware.md).
