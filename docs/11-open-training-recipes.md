# Public laboratory recipes: what is actually disclosed
**Pass 2, 2026-10-08.** Detailed engineering synthesis from official public reports, model cards and proceedings abstracts. Links lead to the original source. No proprietary confidential recipe was retrieved or inferred as fact.

## A. Ai2 Olmo 3: unusually transparent full training flow
**Primary materials:** [official training scripts and stage table](https://github.com/allenai/Olmo-core/blob/main/src/scripts/official/OLMo3/README.md), [Olmo 3 launch](https://allenai.org/blog/olmo3), [7B model card](https://huggingface.co/allenai/Olmo-3-1025-7B/blob/main/README.md).

**Published architectural examples:**
| | Olmo 3 7B | Olmo 3 32B |
|---|---:|---:|
| Decoder transformer blocks | 32 | 64 |
| Hidden width | 4096 | 5120 |
| Attention Q heads | 32 | 40 |
| KV heads | 32 | 8 |
| Advertised context | 65,536 tokens | 65,536 tokens |
| Main pretraining | 5.93 trillion tokens | 5.50 trillion tokens |

**Staged procedure:** (1) general pretrain on broad Dolma 3 mixture; (2) domain-intensified midtraining on higher quality math/code/science/instructions and reasoning material; (3) long-context extension with long documents; (4) different post-training branches for instruct vs think using SFT → DPO → RL with verifiable rewards.

**Public 7B stage figures:** main pretraining ~5.93T tokens using 512 H100s in the published training configurations; midtraining 100B tokens with 128 H100s; long-context 50B tokens with 256 H100s. These are **published training configurations**, not proposed home-lab hardware. The 7B model card lists the stage-2 mixture as 20% code, 28% web, 19% math, 14% question answering, 8% thinking, 6% instruction, 5% PDFs. For long context it lists 66% midtraining and 34% PDFs. Do not assume these percentages generalize to smaller or other-language models.

**Replication recipe, minimal study (ours):** select a licensed 50-150M decoder; fixed total training tokens; compare random-mix baseline against a 3-stage allocation (general→targeted reasoning/code→long-form documents), *and* a shuffled mixture with identical total content. Measure in-domain and out-of-domain loss, recall vs length, exact code/math grades, throughput. Use several seeds and a new hidden test split. Predeclare mixture and sequence schedules before the experiment.

**Important confound:** different corpora vs their order. Factorial ablation of curriculum × selected content avoids falsely attributing all gains to staging.

## B. Ai2 Olmo-core 3: 2026 MoE systems engineering
**Primary:** [October 1, 2026 official release](https://allenai.org/blog/olmocore3).

Public description: switches its earlier MoE stack from an FSDP approach that repeatedly gathers/reshards expert weights to DDP-style expert residency with token movement. The release reports, for a 47B-parameter MoE on eight B300s, 52,000 tokens/s/GPU in its new stack vs 19,400 before, around **2.7× in that preliminary comparison**. It also notes overlapping communication/computation *did not always help*. This is a lab-reported, hardware-specific result—**not** a general claim that DDP is universally 2.7× faster.

**Actionable profiling plan:** set a reproducible workload with constant sequence length, activation fraction, router top-k, microbatch and all-to-all constraints. Compare FSDP weight movement vs resident-expert token routing where hardware permits. Record NVLink/network utilization, tail stragglers, expert imbalance, end-to-end tokens/sec/GPU, GPU hours/step and validation loss. Do not reproduce the headline without equivalent accelerators and kernel versions.

## C. DeepSeek-V3: released large-scale MoE/attention recipe
**Primary:** [technical report](https://arxiv.org/abs/2412.19437), [official repository](https://github.com/deepseek-ai/DeepSeek-V3).

**Lab-reported headline:** ~671B total params with ~37B activated/token, ~14.8T training tokens, ~2.788 million H800 GPU-hours for full training. Not a feasible “one workstation” recipe and not a replicated result here.

**What the report discloses:**
- **Multi-head Latent Attention (MLA):** compresses key/value representations through lower-dimensional latent spaces to reduce KV-cache burden relative to naive full-head storage. Exact speed advantage depends on kernels/decoding and model.
- **DeepSeekMoE:** fine-grained routed experts plus shared experts; route only some experts per token. Compare active FLOPs, communication cost and quality against dense models.
- **Auxiliary-loss-free load balancing:** adjusts routing to manage expert skew without the same training objective pressure as traditional balancing auxiliary losses.
- **Multi-token prediction:** an additional predictive learning objective for future tokens, with potential inference/speculative benefit.
- **FP8 mixed-precision training:** controls memory and compute but demands careful numerical and distributed stability checks; published approach co-designs hardware and system.
- **Post-training SFT + RL:** do not attribute posttraining skills to base architecture.

**Cheap experiment:** build a *small* MoE (e.g. 4-8 experts; use available hardware) and compare router balancing via auxiliary penalty vs route-bias adjustment. Hold active parameter count, train tokens, kernels and seeds constant. Track expert load CV, token drop, quality, communication and loss spikes. Do **not** assume gains extrapolate to 671B-scale.

## D. Qwen3: unified think / non-think modes
**Primary:** [Qwen3 technical report](https://arxiv.org/abs/2505.09388).

Qwen3 publicly describes a model family with dense and MoE variants, multilingual training, explicit thinking and non-thinking modes, and a user-controllable thinking budget. The paper describes a 0.6B–235B family and Apache-2.0 release. Modes/format must be checked against the particular exact checkpoint and tokenizer; not all downstream model exports preserve them.

**Actionable:** compare (a) answer directly, (b) reason for fixed budget, (c) adaptive think-or-answer router at fixed total inference tokens and p95 latency. Training separate controllers is optional; first compare a trivial calibrated uncertainty threshold against budgeted search. Carefully grade final answers and latency, not chain-of-thought persuasiveness. Since Qwen3 has preexisting reasoner and fast mode, it is a useful *baseline* for our adaptive-compute hypothesis, not proof that our controller is novel.

## E. Kimi K2: optimization plus agentic environment data
**Primary:** [Kimi K2 report](https://arxiv.org/abs/2507.20534).

Kimi K2's public report describes ~1T total / 32B active MoE parameters, ~15.5T pretrain tokens and **MuonClip**: a Muon-family optimizer combined with QK-clipping for training stability. Post-training includes agent-oriented synthetic data and joint RL with real/simulated interactions. Strong benchmark numbers are **author reported** and may vary across agent harness, sampling and contamination controls.

**Buildable question:** do optimizer updates with QK stabilization improve repeated seed loss-spike rate compared with AdamW at equal wall time? Separate optimization gains from changed batch, LR schedule, precision and data. If experimental model lacks an equivalent architecture, record as conceptual rather than direct replication. For agents, independently compare trained tool schema transfer rather than “more trajectories = more intelligence.”

## F. DAPO: an open post-training reinforcement learning system
**Primary:** [NeurIPS 2025 proceedings](https://proceedings.neurips.cc/paper_files/paper/2025/hash/a4277440d50f1f15d2cb4c14f7e0c0d2-Abstract-Conference.html), [official code/data](https://github.com/BytedTsinghua-SIA/DAPO).

Public method is **Decoupled Clip and Dynamic sAmpling Policy Optimization**. Its publicly documented components include modified clipping, dynamic sampling of groups with informative rewards, token-level policy-gradient scaling, and an overlong-sequence reward mechanism. The paper reports performance on math verification from a Qwen2.5-32B base model; **this is not a recipe to copy blindly onto arbitrary tasks or an open-ended reward**.

**Reproduction roadmap:**
1. Start with a verifiable environment: arithmetic proofs, program unit tests, or independently checked equation solving.
2. Reproduce baseline GRPO with identical model, dataset, train budget and verifier.
3. Add DAPO components **one at a time**: clip variants; dynamic sample selection; token-level loss; overlong/length handling.
4. Monitor per-group reward variance, valid completion rate, KL drift, length growth, reward hacking, pass@1 on hidden generators.
5. Stop training if model finds grader loopholes, reclassify exploited examples and repair the verifier before further claims.

## G. Other fully disclosed pieces to inventory
- [Bolmo / byteifying](https://allenai.org/blog/bolmo): pretrained global transformer reuse, local byte encoder/decoder, learnable boundaries and two-stage adaptation. See [architecture dossier](12-architectures.md).
- [Meta Llama 4 release](https://ai.meta.com/blog/llama-4-multimodal-intelligence/): MoE variants, multimodal fusion and context design, with more limited full-reproduction disclosure than Olmo; do **not** assume the released blog covers every training dataset/setting.
- [V-JEPA 2](https://arxiv.org/abs/2506.09985): self-supervised video prediction plus action-conditioned planning; useful for grounded world representations.
- [BRIDGE, ICML 2026](https://proceedings.mlr.press/v306/chen26an.html): author-reported cooperative SFT+RL optimization rather than indiscriminate loss mixing.

## Parameter recovery checklist for every lab recipe
**Identity** (paper/model revision); **architecture** (layers, hidden, heads, KV, vocab, experts/top-k, norm, rotary/positions); **objective** (loss equations, coefficient schedules, RL reward/verifier); **data** (tokens, mixtures, dedup and licenses); **optimizer** (type, LR, betas, clipping, weight decay); **systems** (precision, kernels, GPU, parallelism, checkpoint); **posttrain** (SFT/prefs/RL stages); **evaluation** (exact released harness, prompts, scoring and cost); **gaps** (undisclosed parameters). Label every unavailable configuration field **undisclosed**, never fill it from inference.
