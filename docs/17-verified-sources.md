# Pass 2 source ledger
**Inspected on 2026-10-08.** Sources are primary lab release pages, arXiv abstracts, peer-reviewed conference abstract/proceedings pages and journal article webpages. “Inspected” means the referenced public metadata/description was reviewed; it does **not** mean complete papers, appendices or code were audited and replicated.

| ID | Source / dated work | What we extracted | Evidence boundary |
|---|---|---|---|
| S01 | [Olmo 3 official training scripts](https://github.com/allenai/Olmo-core/blob/main/src/scripts/official/OLMo3/README.md) (released 2025) | Stage sequence, model shapes, public configs, data mixtures, training accelerators | Primary implementation documentation; not executed |
| S02 | [Olmo 3 model card](https://huggingface.co/allenai/Olmo-3-1025-7B/blob/main/README.md) | Source data mixtures and model flow | Model publisher documentation |
| S03 | [Olmo-core 3, Oct 1 2026](https://allenai.org/blog/olmocore3) | Resident MoE expert strategy and report-specific throughput | Lab-reported hardware comparison |
| S04 | [DeepSeek-V3](https://arxiv.org/abs/2412.19437) | MLA, MoE, FP8, multi-token objective and scale | Author technical report / abstract |
| S05 | [Qwen3](https://arxiv.org/abs/2505.09388) | Dense/MoE family, think/no-think, budget modes | Author technical report / abstract |
| S06 | [Kimi K2](https://arxiv.org/abs/2507.20534) | MuonClip, agent data and RL, model scale | Author technical report / abstract |
| S07 | [DAPO, NeurIPS 2025](https://proceedings.neurips.cc/paper_files/paper/2025/hash/a4277440d50f1f15d2cb4c14f7e0c0d2-Abstract-Conference.html) | Open RL system and described optimization | Conference abstract; official code not executed |
| S08 | [Bolmo, Nature Oct 7 2026](https://www.nature.com/articles/s41586-026-11111-4) | Two-stage byteification, patching and architecture | Journal article webpage; not reproduced |
| S09 | [Retrieval-aware distillation, ICML 2026](https://proceedings.mlr.press/v306/bick26a.html) | Preserving sparse retrieval heads in Transformer→SSM conversion | Conference abstract; 2% result study-specific |
| S10 | [Hybrid expressivity, ICML 2026](https://proceedings.mlr.press/v306/cooper26a.html) | Hybrid theoretical tasks and separation results | Conference abstract/theory summary |
| S11 | [Sigma continuous DLM, Oct 2026](https://arxiv.org/abs/2610.02665) | Warm-start, ODE/SDE trajectory approach | Preprint and abstract; costly decoding caveat |
| S12 | [Clock Diffusion, Oct 2026](https://arxiv.org/abs/2610.00894) | Semi-AR windows, cache/grab heuristics | Preprint abstract, no runtime replication |
| S13 | [DLM empirical study](https://arxiv.org/abs/2606.19475) | Denoising/block/inference-budget comparison | Preprint abstract and bibliographic validation |
| S14 | [AMA-Bench, ICML 2026](https://proceedings.mlr.press/v306/zhao26bs.html) | Long-horizon event/action memory benchmark | Conference abstract and author-reported score |
| S15 | [Memora, ACL 2026](https://aclanthology.org/2026.findings-acl.1337/) | Memory forgetting/correction evaluation | ACL abstract |
| S16 | [Mem2ActBench, ACL 2026](https://aclanthology.org/2026.acl-long.370/) | Memory applied to tool argument grounding | ACL abstract |
| S17 | [AgeMem, ACL 2026](https://aclanthology.org/2026.acl-long.981/) | Train short/long-term memory controls as actions | ACL abstract |
| S18 | [MemoPilot, ICML 2026](https://proceedings.mlr.press/v306/cai26b.html) | RL for memory updater serving frozen LM | ICML abstract, gaming environments |
| S19 | [World model task-sufficient, ICML 2026](https://proceedings.mlr.press/v306/feng26aa.html) | Structured active environment probing | ICML abstract |
| S20 | [AWM, ICML 2026](https://proceedings.mlr.press/v306/wang26jh.html) | Deterministic code/database-backed synthetic worlds | ICML abstract |
| S21 | [WebWorld, ICML 2026](https://proceedings.mlr.press/v306/xiao26o.html) | Training agent environment and model | ICML abstract; benchmark claims unverified |
| S22 | [Synthetic mixture study](https://arxiv.org/abs/2510.01631) | Empirical source/mixture tradeoffs | arXiv abstract; no raw data audit |
| S23 | [Target mixture constrained data](https://arxiv.org/abs/2605.12715) | Repetition-aware model of mixtures | arXiv abstract |
| S24 | [Model collapse critique, ICML 2026](https://proceedings.mlr.press/v306/schaeffer26a.html) | Alternative interpretation of collapse evidence | Position paper, not consensus |
| S25 | [Selection bias collapse, ICML 2026](https://proceedings.mlr.press/v306/qiao26c.html) | Verification data-silo bias risks | Conference abstract, countervailing result |
| S26 | [RLP ICLR 2026](https://proceedings.iclr.cc/paper_files/paper/2026/hash/44a45e27879b8fbab6e123ad8b93afc2-Abstract-Conference.html) | RL-inspired objective in late pretraining | Conference abstract |
| S27 | [BRIDGE, ICML 2026](https://proceedings.mlr.press/v306/chen26an.html) | Cooperative SFT+RL | Conference abstract, author-reported gain |
| S28 | [Latent exploration decoding, ICML 2026](https://proceedings.mlr.press/v306/tan26d.html) | Posttraining exploration collapse and internal-layer sampling | Conference abstract |
| S29 | [BenchMIRT, Sep 1 2026](https://allenai.org/blog/benchmirt) | Benchmark skill decomposition | Primary lab announcement |
| S30 | [Nature Bolmo release, Oct 7 2026](https://allenai.org/blog/bolmo-nature) | New Qwen/Llama byteified checkpoints | Primary lab announcement |
| S31 | [OpenAlex auth, 2026](https://help.openalex.org/api/authentication/) | API key for sustained use, rate/credit policies | Current service documentation; recheck at execution |
| S32 | [Crossref REST API](https://www.crossref.org/documentation/retrieve-metadata/rest-api/) | Scholarly metadata and polite API behavior | Publisher metadata service docs |

## Claims we do **not** make
- Access to any undisclosed proprietary model recipe or data.
- An exhaustive crawl or systematic review of all 2026 papers.
- A verified breakthrough, superior model, or independent reproduction of publication numbers.
- That listed source licenses authorize bundling full texts or weights into a shared repository.
- That a successful metadata validator validates a scientific paper.

## Evidence progression
For each promising source, advance **E1 → E2** only after reviewing full methods, evaluated tasks, costs, caveats, numerical ablations and updates/corrections. Advance to **E3** only after reproducing the effect with exact experimental artifacts. See [evidence standards](05-evidence-standards.md).
