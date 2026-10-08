# AI Research — Toward Better Language Models and Intelligent Systems

**Research foundation date:** 2026-10-08  
**Current stage:** Pass 2 — 63 curated research records, 24 source-linked claim records, architecture/training/memory dossiers, and offline-validated research tooling. **No new model trained, independently replicated or demonstrated as superior.**

## Mission
Build a rigorous, source-backed knowledge base and executable experimental program for developing next-generation AI: language models, reasoning systems, world models, multimodal intelligence, agents, and alternatives to conventional LLM scaling.

### Research standards
- Separate **published evidence**, **engineering inference**, **original hypothesis**, and **experimentally verified result**.
- Give each claim a traceable primary source; prefer papers, original technical reports, source code, datasets, and reproducible benchmarks.
- Record publication date, access date, license, data provenance, version, and retraction/correction status.
- Never equate benchmark improvements with general intelligence; evaluate out-of-distribution behavior, efficiency, reliability, and safety.
- For this private, noncommercial research library, preserve complete publicly disclosed methods, configurations, formulas and recipes. Legally permitted personal/research copies of papers and artifacts may be archived with source/rights metadata. A private repository does **not** confer blanket permission to reproduce or redistribute protected work.
- Include detailed recipes labs **publicly disclose**, with original-source attribution and version. Do not claim access to confidential trade secrets, nonpublic lab recipes, gated publications, or undisclosed data without proper authorization.
- Protect independent holdouts against benchmark contamination; do not optimize on test data.
- Treat agentic autonomy, open-ended self-modification, and self-improvement as hypotheses requiring sandboxed tests and explicit deployment gates.

## Navigation
- [Research strategy and model design](docs/01-research-strategy.md)
- [Technical handbook](docs/02-technical-handbook.md)
- [Source map and paper reading list](docs/03-source-map.md)
- [Research experiments and evaluation](docs/04-experiments.md)
- [Evidence conventions](docs/05-evidence-standards.md)
- [Private research source policy](docs/16-private-research-materials.md)
- [Pass 2: research decision map](docs/10-pass2-index.md)
- [Browse the 63-paper index](docs/19-paper-index.md)
- [Evidence-qualified claim ledger](data/claims.jsonl)
- [Literature discovery pipeline](docs/20-collection-pipeline.md)
- [Pass 3 prioritized handoff](docs/21-pass3-backlog.md)
- [Open laboratory training recipes](docs/11-open-training-recipes.md)
- [Architecture and tokenizer alternatives](docs/12-architectures.md)
- [Memory, agents and world models](docs/13-memory-world.md)
- [Literature catalog](data/papers.jsonl)
- [Metadata collector](scripts/collect_arxiv.py)

## Major research tracks
1. **Data and pretraining:** high-quality data, tokenization, mixture control, deduplication, provenance, scaling laws, compute-optimal training.
2. **Architectures:** Transformers, sparse MoE, state-space models, recurrent and hybrid models, long-context methods.
3. **Post-training and reasoning:** instruction tuning, preferences, RLHF/RLAIF, RL with verifiable rewards, process supervision, self-correction.
4. **Tool use and agents:** function interfaces, planning, constrained execution, environment feedback, memory, hierarchical control.
5. **World models and learning by doing:** predictive state, interactive environments, curiosity, causal transfer, active learning.
6. **Multimodal and embodied AI:** vision, audio, video, sensor/action streams, robotics and grounded learning.
7. **Efficiency:** FlashAttention, quantization, distillation, speculative decoding, KV management, low-rank adaptation.
8. **Safety, reliability and evaluation:** robustness, calibrated abstention, reward hacking, controllability, auditability and reproducibility.

## Recommended development philosophy
A frontier-scale general-purpose LLM requires enormous compute, carefully licensed data, sophisticated infrastructure, and a large research team. The **first practical objective** is instead to beat a well-matched open baseline on a narrow, independently evaluated capability at a fixed compute budget.

Initial focus: **verifiable reasoning plus persistent structured memory and environment interaction**. This combination is promising but **not proven** to outperform scaling on general benchmarks. Compare it against data quality improvements, stronger post-training, inference-time search, retrieval, and alternative architectures. Prefer simple baselines before exotic systems.

## Proposed program
**Stage 0:** build evidence catalog, collect metadata, document licenses and benchmark provenance.  
**Stage 1:** reproduce a small open baseline, instrument training/inference cost, freeze evaluation set.  
**Stage 2:** controlled ablations of reasoning, tool use, and memory separately.  
**Stage 3:** transfer tests on unseen tasks, multi-step environments, noisy observations, adversarial cases.  
**Stage 4:** only advance experimentally superior systems, including rollback and safety reviews.

This repository supports an ongoing scientific process. Literature review and automated validation are not evidence of model improvement. No novel system has been trained, evaluated or demonstrated to be superior in this repository.
