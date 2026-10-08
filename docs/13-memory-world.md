# Learning across interactions: memory, agent skills and world models
Pass 2 synthesis from 2026 primary proceedings and ACL publication pages. **Published claims are not locally replicated.**

## 1. Memory is a state-management problem, not just a long context window
Separate **observed event**, **derived belief**, **current valid fact**, **outdated/superseded fact**, **agent intent**, **action taken**, and **outcome**. A retrieval system that confuses those categories creates confident errors even with perfect keyword recall.

### 2026 evidence
| Paper | Reported contribution | What it specifically exposes | Limits |
|---|---|---|---|
| [AMA-Bench](https://proceedings.mlr.press/v306/zhao26bs.html) | Tests agent memory over action/observation trajectories, not just chats | Temporal and causal relationships, long horizons | A benchmark cannot by itself prove general cognition |
| [Memora](https://aclanthology.org/2026.findings-acl.1337/) | Tests memory updates, including forgetting invalidated facts | Penalty for stale memories via FAMA | User-like synthetic/data assumptions |
| [Mem2ActBench](https://aclanthology.org/2026.acl-long.370/) | Tests using prior memory to choose tools and parameters | Memory for actions, not just Q&A | Depends on tool schemas and generated tasks |
| [AgeMem](https://aclanthology.org/2026.acl-long.981/) | Memory store/retrieve/update/summarize/discard as policy actions | Learned management of short/long-term context | RL credit assignment, transfer and high training cost |
| [MemoPilot](https://proceedings.mlr.press/v306/cai26b.html) | Train memory updater to improve frozen model through sequential tasks | Memory-writing is itself a decision problem | Reported examples are game-like; broader transfer unproven |
| [Interdependent Multi-Session](https://proceedings.mlr.press/v306/he26am.html) | Evaluates memory-action coupling across sessions | What is remembered must help future task choices | Benchmark generation and setup matter |

**Research inference:** stronger memory retrieval alone is unlikely to guarantee useful *behavior*. Evaluate if retrieved information changes the agent's choice correctly, and whether it can replace outdated beliefs without resurrecting them. Research results vary by tasks and reward quality.

## 2. Proposed event-sourced memory
```
Event { id, observed_at, valid_from, valid_to, entity_id, claim, evidence_ids,
        source_type, certainty, action_id?, outcome_id?, supersedes?, sensitivity }
CurrentView(entity, time) := reconcile validated, non-revoked events valid at time
Retrieval(query, time) := recall sources + explain why each fact is valid at requested time
MemoryControl := [store, update, supersede, retrieve, summarize, discard, defer]
```
This is an original **candidate design**, not a published standard. Keep raw observations immutable for scientific audit, while making access-control/deletion behavior able to remove personal data appropriately. Do not assume immutable storage means never delete sensitive material.

**Baseline ladder:** no memory → last-window transcript → keyword retrieval → dense retrieval → provenance/temporal ledger → learned memory controller. Compare at same input budget. Remember that storing every observation is not necessarily better.

**E03b tasks:** update a person's location, then ask past/current location after distractors; revoke a prior policy; tool parameter chosen from evolving preference; conflicting sources with timestamps; deletion request; cause-vs-correlation question from action outcomes. Grade exact values and decisions. Output both answer and *evidence IDs*.

## 3. Planning with predictive dynamics
Given state s, action a, observation o and reward r, learn an approximate transition `P(s',o,r|s,a)`, then plan over imagined outcomes. Under partial observation, learn a **belief state** and uncertainty. World models should be graded on *decision usefulness* and calibration, not low pixel loss alone.

**2026 publications:**
- [Task-Sufficient World Models](https://proceedings.mlr.press/v306/feng26aa.html): seeks minimally sufficient representations via informative exploration and structured modeling. Hypothesis for us: learn only state variables needed for actions rather than a huge unconstrained latent vector.
- [Agent World Model (AWM)](https://proceedings.mlr.press/v306/wang26jh.html): authors describe generating ~1,000 code- and database-backed synthetic environments for agent RL, highlighting reliable transitions rather than model-invented outcomes.
- [WebWorld](https://proceedings.mlr.press/v306/xiao26o.html): models web state transitions as a simulated learning/search environment; benchmark outcomes remain author reports.
- [V-JEPA 2](https://arxiv.org/abs/2506.09985): video latent representation and action-conditioned planning; useful for grounded agents but not evidence of general text reasoning transfer.

**Key design tension:** a generative model can produce plausible imaginary observations while being wrong about mechanics. For training agents, ground “world truth” in a deterministic simulator/database, and use learned world model only to plan/test predictions. Compare against a reactive or search-based controller.

## 4. Active exploration and curriculum
An exploration step should have a prospective purpose: discriminate between competing transition hypotheses, collect reusable state-action examples, or reduce task uncertainty. Novelty and movement count are **not** proof of learning.

**Original hypothesis H11:** a small structured dynamics model with active probes can outperform both random exploration and a large unconstrained trajectory summarizer on *compositional new mechanisms*, when interaction budgets are limited.

**Falsifiers:** transition accuracy improves but task success does not; learned planner exploits model errors; recurrent probes collect similar data; apparent generalization disappears under hidden rule combinations.

**Minimal sandbox experiment:** generated 8×8 environments with moving blocks, locked doors, keys, delayed timers, uncertain action affordances, and hidden event rules. Training environments draw from a subset of rule combinations; tests draw from unseen combinations. Run randomized, reactive, heuristic, symbolic learned state and neural latent baseline at matched action budgets. Preserve immutable environment seed and action/reward traces.

## 5. Memory and agent-control interface
Tool interaction protocol:
```
Observe -> parse evidence -> update valid beliefs -> choose goal/next action
        -> approve action scope -> act (sandbox) -> inspect result
        -> compare expected/actual -> learn only from externally verified outcomes
```
Avoid reflexively promoting unverified tool outputs into long-term facts. Build injection and failure tests for malformed tool returns. For unsafe/irreversible effects use external approval. Models must not invent that an action occurred when there is no execution receipt.

## 6. Suggested research sequence
1. Deterministic state fixture and exact validator (no LLM needed).
2. Benchmark naive retrieval errors and stale-memory false positives.
3. Add temporal semantics and contradiction handling.
4. Evaluate use of memory for **tool arguments**, not just Q&A.
5. Build generated world with ground-truth transitions and fresh held-out mechanics.
6. Only then test learned memory policies / planning and optimize reward.

This route is cheaper and scientifically more informative than starting with a large multi-agent system.
