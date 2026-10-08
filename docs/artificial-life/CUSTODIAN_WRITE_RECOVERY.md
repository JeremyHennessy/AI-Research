# AI-Research custodian: safe write-failure recovery

**Scope:** research-only GitHub documentation/ledgers in `JeremyHennessy/AI-Research`. This is an operational checklist, not scientific evidence or authorization to run experiments.

## Before editing (every hourly pass)

1. Read the live `main` SHA, `docs/artificial-life/10-handoff.md`, append-only `data/research-log.md`, current Actions status, open PRs, and actively changing branches. Confirm that another researcher is not already working on the same question or files.
2. Inspect the intended new/modified file's existence and content at the exact target branch. Start a uniquely named, reversible research branch from the **rechecked** `main` SHA; reuse an active branch only when its owner and contents are known. Never write to default `main` as a workaround.
3. For GitHub Contents writes, use an **explicit branch** on every `create_file` or `update_file`. For updates fetch the target branch's current **blob SHA** and send that SHA, not the branch commit SHA; on stale state, refetch and inspect before retrying. Preserve other workers' text and all approved/canonical data.
4. Commit only meaningful, already-reviewed work. A successful branch creation or commit is **not** proof of publication.

## On a failed write: one hypothesis and one bounded recovery

Capture the attempted operation, error/status/message, repository, intended branch and exact base/head SHA **without exposing secrets**. Inspect the current branch, file and permission state before retrying; do not assume that a branch-creation success proves file-write permission.

- **401/403 / execution-context or approval gate:** classify the exact denied operation, distinguish GitHub ACL from a tool/scheduled-run approval gate, and **stop that mutation in this run**. Do not switch identities, create/request API keys, use production/main, disable checks, or bypass a connector/platform restriction. An interactive authorized session can investigate separately; do not promise that later scheduled writes will be allowed.
- **404:** distinguish missing path/ref from unavailable repo/access; do not invent a destination.
- **409/422 / stale SHA / conflicting edits:** refetch branch, file and main; preserve concurrent work. Resolve on a new branch or explicit nonconflicting edit; never overwrite or force push blindly.
- **429/5xx/timeout:** one conservative retry after checking status and whether the original write took effect; otherwise record the transient failure and proceed read-only. Do not spin or create repeated empty branches.
- **Any other failure:** preserve exact candidate text outside production, report the blocker and continue an independent read-only research/verification task.

If write failure persists, keep `main` untouched. The hourly report should say **WRITE_BLOCKED** with the error class, the last verified main SHA, candidate branch/head if any, what is already reviewed but unpublished, and the next safe recovery. If the repository handoff cannot be updated, do not falsely claim it was.

## CI, reconciliation and promotion

- Inspect full candidate diff; validate source identifiers, licenses/rights, independent-study assertions, new file links, canonical counts, JSON/JSONL integrity, existing EERC versions and append-only log. Run available offline tests without starting any organism, simulation, new world, training or experiment.
- Open/reuse one PR for the reviewed candidate. Require the exact PR **head SHA** to have successful relevant GitHub Actions; an earlier green SHA is not sufficient.
- Immediately before merge, re-read **both** `main` SHA and PR head/base. If another custodian moved main or owns overlapping paths, stop and reconcile first. Merge with an expected head SHA only after gates pass and main is unchanged since final review.
- Verify resulting `main` SHA and **separate** main-workflow result. If its run is pending, label post-merge verification pending, not passed.
- Retain failed attempts and negative scientific outcomes as evidence, but don't make commits or duplicate research solely to show activity. EERC v1–v7 and previous approved evidence/history are immutable unless separately authorized.

**Scope boundary:** do not modify Ora, AgentTest, Ora2 or other repositories or activate artificial organisms, simulations or experiments. No costs, API keys or production changes.
