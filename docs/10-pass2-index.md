# Pass 2 — Research decision atlas (2026-10-08)
**Status:** topical screening and detailed *public release / primary abstract* review; **no independent replication or model trained**.

Start here, then follow one technical dossier. A model is **not** uniformly best: architectural trade-offs depend on task, resource, runtime and safety constraints.

## Fast decision map

| Your question | Evidence-rich direction | Where to inspect | Cheapest useful experiment |
|---|---|---|---|
| How do open labs actually pretrain? | Ai2 Olmo 3 three-stage curriculum and transparent code | [Open training recipes](11-open-training-recipes.md) | E04: 3-stage curriculum on 50-100M model, equal-token baseline |
| How do large MoEs work? | DeepSeek-V3 MLA/MoE/FP8, Qwen3 dense vs MoE, Kimi K2 MuonClip | [Lab recipes](11-open-training-recipes.md) | E07: route/load and memory traffic profiler |
| Could byte-level models replace fixed tokenizers? | Bolmo byteification from pretrained model | [Architecture alternatives](12-architectures.md) | E10: rare-string/Unicode quality vs byte throughput |
| Which attention heads matter for recall? | Retrieval-aware Transformer→SSM distillation, ICML 2026 | [Architecture alternatives](12-architectures.md) | E07b: head ablation on key/value retrieval |
| Is diffusion better than autoregression? | LangFlow, Sigma, Clock Diffusion, 2026 DLM comparisons | [Architecture alternatives](12-architectures.md) | E11: accuracy vs actual decoding time/NFEs |
| Can a memory system truly learn from history? | AMA-Bench, Memora, Mem2ActBench, AgeMem, MemoPilot | [Agents, memory, world models](13-memory-world.md) | E03b: temporal revisions and action grounding |
| Can agents learn better environment representations? | Task-sufficient world models, Agent World Model, WebWorld | [Agents, memory, world models](13-memory-world.md) | E08: hold out unseen state-transition combinations |
| How should we train reasoning? | DAPO, Qwen3 thinking modes, RLP, BRIDGE, DeepSeek-R1 | [Lab recipes](11-open-training-recipes.md) and [research plan](14-reasoning-data-eval.md) | E02: adaptive thinking budget at fixed total time |
| Will synthetic data damage models? | Large-scale mixture study; competing 2026 model-collapse analyses | [Reasoning, data and evaluation](14-reasoning-data-eval.md) | E04: repetition and synthetic mixtures, held-out tails |
| Are benchmark scores meaningful? | HELM, LiveCodeBench, BenchMIRT, task/skill audits | [Reasoning, data and evaluation](14-reasoning-data-eval.md) | E12: stress via task-generator shifts and hidden holdout |

## What most deserves an independent test
These are **research hypotheses**, not claims of superiority.

1. **Memory control, not memory length:** temporal, provenance-aware state updates and action-grounding could produce more reliable long tasks than indiscriminate RAG. Related 2026 memory work reports persistent problems with stale memories.
2. **Hybrid retrieval heads:** retain precise content-addressable attention for retrieval while using recurrent layers for the rest. A 2026 ICML paper reports a much smaller retained head subset; this may enable speed/quality trade-offs that full recurrence cannot.
3. **Tokenizer and representation adaptability:** byteifying a competent subword model may improve rare-byte/character tasks without retraining the global backbone from scratch. Whether this is advantageous outside such tasks is unknown.
4. **Adaptive rather than fixed compute:** per-instance routing between fast answer, verification, retrieval, planning and abstention should be compared at equal average **and tail** cost.
5. **Data and curriculum are first-class architecture:** staged pretrain/midtrain/long context, measured data provenance and evaluation decontamination may be worth more than sophisticated extra layers for the same budget.

## Important contrary evidence
- 2026 model-collapse work **disagrees** on how likely synthetic-data degradation is. Treat mixture quality and tail coverage as test conditions, not a simple “synthetic good/bad” rule.
- 2026 hybrid-model theory and empirical distillation suggest some attention can be vital for exact retrieval; a fully recurrent architecture may lose capability despite impressive throughput.
- Diffusion has different parallelism opportunities but can spend many denoising steps. Compare *end-to-end* output speed and verified quality, not “parallel generation” slogans.
- Memory benchmarks suggest retrieving facts and **using them to ground actions** are separate capabilities; remembering alone is insufficient.

## Source confidence legend
- **Primary report/official page read:** the research author's public release or proceedings page was inspected; method statements refer to their own reports.
- **Abstract-level verified:** identity and abstract verified, full experimental results not independently checked.
- **Local evidence:** would require reproducible run artifacts; currently none.

## Complete Pass 2 navigation
- [Public training recipes](11-open-training-recipes.md)
- [Architectures and tokenization](12-architectures.md)
- [Memory and world models](13-memory-world.md)
- [Reasoning, data and evaluation](14-reasoning-data-eval.md)
- [Build-ready experiment designs](15-pass2-experiments.md)
- [Private source / rights policy](16-private-research-materials.md)
- [Source ledger](17-verified-sources.md)
- [Candidate integrated AI design](18-candidate-system-design.md)

## What a researcher should do next
Select **one** hypothesis and a baseline. Freeze the evaluation before tuning. Read the relevant primary paper, identify disclosed *and missing* parameters, then reproduce the smallest effect under fixed cost. Track results and nonresults; our technical descriptions **are not** training outcomes.
