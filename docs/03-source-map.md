# Primary source map and databases
Updated 2026-10-08. This is a deliberately **selected** starting map. Listed claims reflect publication abstracts/metadata, not replications conducted here.

## Literature and citation infrastructure
| Collection | URL | Useful for | Access and cautions |
|---|---|---|---|
| arXiv | https://arxiv.org | Fast-moving preprints; category/date API | Preprints may not be peer-reviewed; versions change |
| OpenAlex | https://openalex.org | Works, authors, concepts, citation links | Coverage, attribution and API limits require review |
| Semantic Scholar | https://www.semanticscholar.org | Citation graphs, TLDR/metadata | API key/rate limits, incomplete fields |
| Crossref | https://www.crossref.org | DOI and publisher metadata | Incomplete titles/licenses on some records |
| ACL Anthology | https://aclanthology.org | NLP peer-reviewed conference proceedings | Check the actual publication and revisions |
| OpenReview | https://openreview.net | ICLR and other peer review/submissions | Submissions and accepted versions differ |
| NeurIPS proceedings | https://proceedings.neurips.cc | Peer-reviewed ML research | Coverage tied to venue |
| PMLR | https://proceedings.mlr.press | ICML and other ML proceedings | Metadata varies |
| AAAI Digital Library | https://ojs.aaai.org | AI research venues | Usage rights vary |
| ACM Digital Library | https://dl.acm.org | Systems, HCI, ML papers | Full text can be paywalled |
| IEEE Xplore | https://ieeexplore.ieee.org | Hardware, robotics and AI systems | Usually licensed access |
| PubMed | https://pubmed.ncbi.nlm.nih.gov | AI in biomedical applications | Not a general LLM catalog |
| Papers on Hugging Face | https://huggingface.co/papers | Models, datasets and associated papers | Check primary sources, card licenses |
| GitHub | https://github.com | Implementation and issue history | Check license, commit and supply chain |
| MLCommons | https://mlcommons.org | Standardized hardware/model benchmarks | Version and submission-specific comparability |
| Stanford HELM | https://crfm.stanford.edu/helm | Multi-metric model evaluation | Coverage and prompt policies change |

Use APIs and metadata feeds with documented rate limits. Public lab recipes, equations, configurations and research implementation details should be documented thoroughly. Legally permitted copies of papers may be archived for private study with provenance and rights metadata; neither a private repository nor noncommercial purpose automatically bypasses copyright, access restrictions or third-party dataset licenses. See [private materials policy](16-private-research-materials.md).

## Must-read foundation, by engineering task

### Pretraining / scale / data
- 2017 — **Attention Is All You Need**: Transformer and attention mechanism. https://arxiv.org/abs/1706.03762
- 2022 — **Training Compute-Optimal Large Language Models**: model and token tradeoffs under compute. https://arxiv.org/abs/2203.15556
- 2025 — **Demystifying Synthetic Data in LLM Pre-training**: conditional effects of synthetic mixtures; experiments across many training runs. https://arxiv.org/abs/2510.01631
- 2026 — **Scaling Laws for Mixture Pretraining Under Data Constraints**: repetition-aware mixtures on constrained target data. https://arxiv.org/abs/2605.12715

### Architecture / acceleration
- 2021 — **Switch Transformers**: sparse expert routing. https://arxiv.org/abs/2101.03961
- 2022 — **FlashAttention**: IO-aware exact attention. https://arxiv.org/abs/2205.14135
- 2023 — **FlashAttention-2**: improved parallelism and work partitioning. https://arxiv.org/abs/2307.08691
- 2023 — **Mamba**: selective state spaces. https://arxiv.org/abs/2312.00752
- 2024 — **Transformers are SSMs / Mamba-2**: structured state-space duality. https://arxiv.org/abs/2405.21060
- 2024 — **DeepSeek-V3 Technical Report**: mixture-of-experts and attention/system co-design. https://arxiv.org/abs/2412.19437
- 2024 — **LongRoPE**: context extension, but verify useful recall vs advertised length. https://arxiv.org/abs/2402.13753

### Reasoning and post-training
- 2023 — **Direct Preference Optimization**: simplified preference training objective. https://arxiv.org/abs/2305.18290
- 2024 — **Quiet-STaR**: learning to generate latent deliberative text for harder predictions. https://arxiv.org/abs/2403.09629
- 2025 — **DeepSeek-R1**: large-scale reasoning RL with verifiable outcomes and cold starts. https://arxiv.org/abs/2501.12948
- 2025 — **s1: Simple test-time scaling**: small selected dataset and budget-forced reasoning. https://arxiv.org/abs/2501.19393
- 2025 — **Scaling Up RL**: prolonged RL stability and domain-diverse reasoning tasks. https://arxiv.org/abs/2507.12507

### Agents, memory and world models
- 2020 — **Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks**: parametric + non-parametric memory. https://arxiv.org/abs/2005.11401
- 2022 — **ReAct**: interleaved reasoning and action. https://arxiv.org/abs/2210.03629
- 2023 — **AgentBench**: interactive evaluation across multiple environments. https://arxiv.org/abs/2308.03688
- 2023 — **DreamerV3 / Mastering Diverse Domains through World Models**: learned dynamics for imagined behavior. https://arxiv.org/abs/2301.04104
- 2024 — **Genie: Generative Interactive Environments**: action-controllable generative world model. https://proceedings.mlr.press/v235/bruce24a.html

### Multimodal
- 2023 — **DINOv2**: robust self-supervised visual representations. https://arxiv.org/abs/2304.07193
- 2024 — **OpenVLA**: vision-language-action robotic control with released artifacts. https://arxiv.org/abs/2406.09246

### Evaluation
- 2022 — **Holistic Evaluation of Language Models (HELM)**: accuracy plus bias, robustness, calibration and efficiency. https://arxiv.org/abs/2211.09110
- 2023 — **SWE-bench**: real GitHub issue resolution rather than isolated coding snippets. https://arxiv.org/abs/2310.06770
- 2024 — **LiveCodeBench**: time-stamped coding tasks and contamination mitigation. https://arxiv.org/abs/2403.07974

## Source verification policy
The entries above were selected using primary arXiv/venue metadata and paper abstract searches. This is **not** evidence that every PDF, appendix, implementation, licensing term or claimed result was checked. Our [catalog](../data/papers.jsonl) labels review level, date and follow-up work. Dates are original-publication years, not necessarily version or conference years. Always inspect retractions, revisions, code and reported benchmarks before implementing a paper.

## Pass 2 deep research
- [2026 research decision map](10-pass2-index.md)
- [Reproduction-grade public recipes](11-open-training-recipes.md)
- [New architecture research](12-architectures.md)
- [Agent memory and world models](13-memory-world.md)

## High-value expansion searches
- Benchmark leakage + synthetic chain-of-thought + verification
- 2026 reasoning RL generalization, reward hacking and proof checking
- 2026 mixture routing / active parameters / memory bandwidth
- Long-context *effective recall* rather than advertised token limit
- Differential privacy and dataset governance
- Model-based agent learning and compositional transfer
- Diffusion language models, energy-based models, neural algorithmic reasoning
- Causal representation learning, mechanistic interpretability and representation steering
- Speech/audio/video/3D-native multimodal models
- Evaluation of autonomy, corrigibility, calibration and human control

The metadata collector in [scripts](../scripts/collect_arxiv.py) is for **discovery**. Every new result must be reviewed before being promoted to a substantive technical claim.
