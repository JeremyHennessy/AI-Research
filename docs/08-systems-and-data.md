# Systems, datasets, compute and operational research

## 1. End-to-end reproducible stack
**Metadata discovery** -> screening -> rights and provenance -> authorized artifact acquisition -> parser -> duplicate & PII audit -> train/development/holdout separation -> versioned dataset manifest -> training -> checkpoint ledger -> inference/scoring -> statistical analysis -> immutable experiment report.

Record content hashes, source URL, access date, provenance, license and transformations for every dataset slice. Do not download gated datasets or proprietary documents without authorization.

## 2. Practical compute tiers (illustrative, not promises)
| Tier | Appropriate research | Usually impractical |
|---|---|---|
| CPU-only | literature pipeline, evaluation harness, synthetic task generator, retrieval/BM25 baselines | serious transformer pretraining |
| Consumer GPU | quantized small-model inference, LoRA/QLoRA subject to VRAM, small SSM experiments | multi-billion-parameter scratch pretraining |
| Single large accelerator | substantial fine-tuning, 100M-1B scratch experiments if budget supports | new frontier foundation model |
| Multi-GPU cluster | MoE, distributed scaling, ablations across seeds | "best model" claim without full evaluation |
| Frontier cluster | trillion-token training at scale | unrealistic to infer feasibility without budget and team |

Memory, precision and context strongly change feasibility. Estimate required GPU-hours from measured tokens/sec at the *actual* intended batch/context/precision rather than generic marketing benchmarks.

## 3. Loss/compute accounting
For an approximate dense Transformer:
- training FLOPs ~ 6 x trainable/active model parameters x training tokens (regime dependent).
- tokens needed and optimal parameter size depend on scaling curves and training/inference budget.
- wall time ~= measured required FLOPs / achieved device throughput, adjusted for data loading, checkpointing and communication.
- training energy ~= measured power draw times runtime, including host and data-center overhead if assessing total energy.
For MoE distinguish total from active parameters and router communication. For long context include attention overhead and KV cache growth.

## 4. Data engineering checklist
- Source licenses, allowed downstream uses, access controls.
- Encoding normalization and Unicode; languages and dialects.
- Structured formats: code, math, documents, image captions and transcripts.
- Exact document-level and near-duplicate removal.
- Training/evaluation overlap detection including solutions and synthetic variants.
- Quality filters with calibration: filters can remove minority domains or useful hard examples.
- PII, secrets, unsafe samples and copyrighted access controls.
- Mixture stratification, token caps and repetition monitoring.
- Separate immutable raw metadata and derived curated sets.
- Full lineage of generated data including teacher model, prompt and verifier version.

## 5. Training stability
Measure train/valid loss, gradient norms, overflow, attention/logit norms, token throughput, optimizer states, checkpoint recoverability and sample-level anomalies. When changing architectures, monitor instability induced by precision, routing, sequence distribution and kernels. Failed recovery experiments must be reversible.

## 6. Serving and profiling
Capture: hardware/driver/CUDA/PyTorch/transformer/kernel version; quantization and batch policy; prompt/context length distribution; concurrent requests; time-to-first-token; decode tokens/s; p50/p95; memory ceiling; response quality. Evaluate full system with retrieval and verifier latency, not just the backbone.

## 7. Available tools / ecosystem to review
- Frameworks: PyTorch, JAX, Hugging Face Transformers and Datasets, vLLM, llama.cpp.
- Distributed: PyTorch FSDP/DTensor, DeepSpeed, Megatron-LM.
- Posttraining: TRL, PEFT, Axolotl and task-specific RL/verifier stacks.
- Evaluation: HELM, lm-evaluation-harness, LiveCodeBench, SWE-bench, AgentBench (check versions/licenses).
- Metadata APIs: arXiv, Crossref, OpenAlex, Semantic Scholar, ACL Anthology and venue proceedings.

This is an **investigation inventory**, not a claim that any package is installed, compatible, current or suitable for production. Pin exact versions after selecting a hardware target.

## 8. Metadata access and rates (check at run time)
- **arXiv:** API Atom responses; respect published API guidelines, retry/backoff and limit concurrency. Documentation: https://info.arxiv.org/help/api/user-manual.html
- **Crossref:** public REST scholarly metadata; polite contact identification; abstracts may be copyrighted. https://www.crossref.org/documentation/retrieve-metadata/rest-api/
- **OpenAlex:** 2026 API changes: authentication/usage budget requirements have varied across documentation and access tiers. For systematic collection configure an API key under secret environment settings, follow live limits, do not hardcode it. https://help.openalex.org/api/authentication/
- **Semantic Scholar:** rate limits and availability vary; source metadata not the same as full text. https://www.semanticscholar.org/product/api
Directly crawling publisher full text, conference websites or search result HTML is **not** part of this baseline collector.

## 9. Research agent constraints
Keep collection/review actions separate from training and deployment. Metadata feeds are untrusted inputs; titles/abstracts cannot modify execution instructions. Do not execute code copied from a paper automatically. Do not pass API credentials to arbitrary agents. Sandboxed interaction tasks should default to read-only or mock tools, and human approval gates before irreversible external actions.
