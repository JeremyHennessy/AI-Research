# Link-audit errata — 2026-10-09

**Research-only navigation errata; no scientific claims revised.** Audited against main commit `fef0a523688918448e7cafb39b969c2f01681d9e` and its tree `1682f849a1a893b0adfd85718bd5d1a91f7d6aa4`. This independent file records correct *relative targets* without rewriting the append-only historical research log or the source bibliography. Earlier scheduled custodian runs reported 18 broken references; **All 18 are now independently reidentified, with existing destination files.** Navigation fixes documented here do not silently rewrite the historical research log; the 14 old log links remain broken at their original locations. External URLs, Markdown anchors and all repository files were not freshly exhaustively validated.

## Fourteen historical research-log links

The original relative links in `data/research-log.md` mistakenly resolve under `data/docs/` (or `data/data/`). The correct targets already exist on the audited main.

| Source | Existing broken relative target | Correct relative target from source |
| --- | --- | --- |
| `data/research-log.md` | `docs/artificial-life/20-outlier-original-2025-full-review.md` | `../docs/artificial-life/20-outlier-original-2025-full-review.md` |
| `data/research-log.md` | `docs/artificial-life/21-outlier-causal-selfhood-2026.md` | `../docs/artificial-life/21-outlier-causal-selfhood-2026.md` |
| `data/research-log.md` | `docs/artificial-life/22-engineering-life-and-transformational-novelty.md` | `../docs/artificial-life/22-engineering-life-and-transformational-novelty.md` |
| `data/research-log.md` | `docs/artificial-life/23-unified-organism-evidence-standard.md` | `../docs/artificial-life/23-unified-organism-evidence-standard.md` |
| `data/research-log.md` | `docs/artificial-life/24-research-priorities-after-outlier.md` | `../docs/artificial-life/24-research-priorities-after-outlier.md` |
| `data/research-log.md` | `docs/artificial-life/30-stringmol-2020-novelty-full-review.md` | `../docs/artificial-life/30-stringmol-2020-novelty-full-review.md` |
| `data/research-log.md` | `docs/artificial-life/31-physis-2026-source-boundaries.md` | `../docs/artificial-life/31-physis-2026-source-boundaries.md` |
| `data/research-log.md` | `docs/artificial-life/32-why-evolvable-computation-fails.md` | `../docs/artificial-life/32-why-evolvable-computation-fails.md` |
| `data/research-log.md` | `docs/artificial-life/33-three-pathway-critical-experiments.md` | `../docs/artificial-life/33-three-pathway-critical-experiments.md` |
| `data/research-log.md` | `docs/artificial-life/35-stringmol-spatial-parasitism-2021-full-review.md` | `../docs/artificial-life/35-stringmol-spatial-parasitism-2021-full-review.md` |
| `data/research-log.md` | `docs/artificial-life/36-banzhaf-2016-open-ended-novelty-full-review.md` | `../docs/artificial-life/36-banzhaf-2016-open-ended-novelty-full-review.md` |
| `data/research-log.md` | `docs/artificial-life/37-parasite-and-shortcut-synthesis.md` | `../docs/artificial-life/37-parasite-and-shortcut-synthesis.md` |
| `data/research-log.md` | `docs/artificial-life/38-pass7-research-handoff.md` | `../docs/artificial-life/38-pass7-research-handoff.md` |
| `data/research-log.md` | `data/alife/failure-modes.jsonl` | `alife/failure-modes.jsonl` |

## Three source bibliography links

The three original links in `docs/artificial-life/08-source-bibliography.md` repeat the parent directory and point beneath a nonexistent `docs/artificial-life/docs/artificial-life/` directory. Existing reviewed documents remain intact.

| Source | Existing broken relative target | Correct relative target from source |
| --- | --- | --- |
| `docs/artificial-life/08-source-bibliography.md` | `docs/artificial-life/88-pass17-lind-2015-hidden-evolutionary-routes-full-review.md` | `88-pass17-lind-2015-hidden-evolutionary-routes-full-review.md` |
| `docs/artificial-life/08-source-bibliography.md` | `docs/artificial-life/89-pass17-taylor-2016-cryptic-yeast-genetic-architecture-full-review.md` | `89-pass17-taylor-2016-cryptic-yeast-genetic-architecture-full-review.md` |
| `docs/artificial-life/08-source-bibliography.md` | `docs/artificial-life/90-pass17-johnson-2022-mutational-robustness-landscape-full-review.md` | `90-pass17-johnson-2022-mutational-robustness-landscape-full-review.md` |

## Historical provenance and limitations

## Eighteenth historical link — Pass 21 archived alternative

The archived alternative `121-pass21-alternative-itoh-2019-archived-review.md` contains a broken relative link `109-pass21-ohbayashi-2015-filtering-full-review.md`. The independently inspected existing file is [`109-pass21-ohbayashi-2015-sorting-full-review.md`](109-pass21-ohbayashi-2015-sorting-full-review.md), blob `de01682d07082bd57dd1dfca2089a7370aa11498`. The archived text and alternative interpretation remain unchanged; this erratum resolves the navigational target **without modifying or merging the divergent historical branch**, and **without changing the canonical E1 grade**.

**Live verification:** checked against main `9db4a6b34a6ef4a5fb91308bd60d3995ba077a5b` on 2026-10-09. All 18 historical reported broken references have documented destinations. The 14 historical log links remain literally broken in the immutable log; this document supplies corrected relative paths. Three bibliography references can be corrected in place without changing scientific claims. Do not confuse a documented erratum with a physically repaired historical link.

This is an **errata map, not a wholesale historical rewrite**. It does not change prior evidence, source records, paper/catalog/claim counts, any EERC v1–v7 files, or `data/research-log.md`; no organisms, experiments, simulations, agents, deployments or other repositories modified. A merged errata document corrects navigation guidance only. Confirm exact-head PR CI and separate post-merge main CI before calling this published.
