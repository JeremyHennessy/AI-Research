# Implementation playbook — from papers to a real result

## Start here, even without a GPU
1. Read [atlas](00-atlas.md), choose one track and create hypothesis record.
2. Run Python catalog validation and unit tests (commands below).
3. Run a bounded *metadata-only* discovery query and inspect unreviewed JSONL output.
4. Screen papers into E1/E2 records with provenance, version, license and limitations.
5. Freeze a representative open model revision and datasets; create baseline E01.
6. Commit experiment config, source hashes, before/after metrics and failure traces.
7. Only promote a result after independent hidden holdout and replication.

## Repository commands (Python 3.10+)
No package installation is needed for the metadata collector/validator/test harness.

    python3 scripts/validate_catalog.py
    python3 -m unittest discover -s tests -v
    python3 scripts/collect_arxiv.py --query "reasoning language models" --limit 20 --output data/discovered/arxiv-reasoning.jsonl

The arXiv command sends a live network request and should be run from a machine with access; CI tests are offline. Scraper logs/errors are not evidence that papers were downloaded or reviewed. Collector stores *short metadata, not full articles.*

### Other databases
Crossref and OpenAlex are mapped in [systems and data](08-systems-and-data.md) for subsequent connector implementations. OpenAlex large-scale use may require an API key and has usage-based policies as of 2026. No need to create or share keys for this pass.

## Recommended research branching workflow
1. Leave verified baseline and prior research records immutable.
2. Create small branch for one experiment or source batch.
3. Write setup and design before modifying baseline.
4. Run code/static tests and reproducibility checks.
5. Review diff and run before/after evaluations.
6. Merge only validated work; preserve negative results and provenance.

## Experiment folder convention (not created until a real run)
    runs/
      E02-YYYYMMDD-seed42/
        manifest.json
        predictions.jsonl
        scores.json
        failures.md
        interpretation.md

Include commit SHA, model/dataset hashes, hardware, prompt and permissions. For large or licensed data, store hashes and permitted artifact links, never proprietary bytes.

## First four build deliverables
1. **Evaluable baseline (E01):** model interface, dataset loader, exact grader, comprehensive log; no claim of improvement.
2. **Reasoning controller (E02):** compare direct, fixed compute, and adaptively verified answer at matched budget.
3. **Temporal memory (E03):** timestamped inserts/updates/deletions and provenance; test synthetic contradiction fixtures.
4. **Data study (E04):** where hardware permits, contrast filtered, natural and mixed data under equal token/training budget.

## Research pass checklist
- [ ] Literature search cutoff and database logged
- [ ] Duplicates collapsed across arXiv/DOI/OpenAlex identifiers
- [ ] Changes in API policy and paper version checked
- [ ] Opposing research and methodological criticisms included
- [ ] Extracted claim separately linked from method and benchmark
- [ ] License and data-source rights logged
- [ ] Experiments graded with untouched heldouts and costs
- [ ] README/atlas updated with validated, not speculative, progress
- [ ] Failure modes and uncertainties retained

## Definition of done for an improved model
A frozen baseline and independently assessed variant, equivalent resource budgets, precommitted metric, clean test split, uncertainty estimates, reproducible artifacts, and no unacceptable safety regression. Until then describe as **idea** or **experimental signal**, never **next best AI**.
