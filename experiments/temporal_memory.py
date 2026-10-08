#!/usr/bin/env python3
"""Deterministic temporal-memory scoring fixture: NO LLM training, no learned AI claims.

Exercises current/historical/unknown/revoked lookups with synthetic entities.
This is a correctness fixture for a future E03b model comparison, not evidence of
general improvement. Only stdlib; zero network and no personal data.
"""
from __future__ import annotations

import argparse
from dataclasses import dataclass
import json
import random
from typing import Iterable


@dataclass(frozen=True)
class Event:
    entity: str
    key: str
    value: str | None
    effective_at: int
    observed_at: int
    event_id: str


@dataclass(frozen=True)
class Query:
    entity: str
    key: str
    as_of: int
    expected: str | None


class TimelineMemory:
    """Stores external events; resolves by valid/effective time, then observation time."""

    def __init__(self, events: Iterable[Event] = ()) -> None:
        self.events = list(events)

    def resolve(self, entity: str, key: str, as_of: int) -> str | None:
        relevant = [event for event in self.events
                    if event.entity == entity and event.key == key
                    and event.effective_at <= as_of]
        if not relevant:
            return None
        chosen = max(relevant, key=lambda e: (e.effective_at, e.observed_at, e.event_id))
        return chosen.value


def first_seen(events: list[Event], q: Query) -> str | None:
    matching = [e for e in events if e.entity == q.entity and e.key == q.key]
    return min(matching, key=lambda e: e.observed_at).value if matching else None


def most_recent_observation(events: list[Event], q: Query) -> str | None:
    matching = [e for e in events if e.entity == q.entity and e.key == q.key]
    return max(matching, key=lambda e: e.observed_at).value if matching else None


def generate_fixture(trials: int = 50, seed: int = 41) -> tuple[list[Event], list[Query]]:
    if not 1 <= trials <= 1000:
        raise ValueError("trials must be between 1 and 1000")
    rnd = random.Random(seed)
    events: list[Event] = []
    queries: list[Query] = []
    for i in range(trials):
        entity = f"E{i:04d}-{rnd.randrange(10**6):06d}"
        old = f"V{rnd.randrange(10**8):08d}"
        new = f"V{rnd.randrange(10**8):08d}"
        # Guarantee a change, to exercise conflict resolution.
        if old == new:
            new = new + "R"
        events.extend([
            Event(entity, "location", old, 1, 1, f"{entity}-1"),
            Event(entity, "location", new, 5, 6, f"{entity}-2"),
            Event(entity, "location", None, 9, 10, f"{entity}-3"),
        ])
        queries.extend([
            Query(entity, "location", 0, None),
            Query(entity, "location", 3, old),
            Query(entity, "location", 7, new),
            Query(entity, "location", 11, None),
        ])
    # The event list is intentionally scrambled to ensure resolution relies
    # on effective timestamps rather than physical record order.
    rnd.shuffle(events)
    rnd.shuffle(queries)
    return events, queries


def score(events: list[Event], queries: list[Query]) -> dict:
    ledger = TimelineMemory(events)
    strategies = {
        "first_observed": lambda q: first_seen(events, q),
        "most_recent_observation": lambda q: most_recent_observation(events, q),
        "temporal_ledger": lambda q: ledger.resolve(q.entity, q.key, q.as_of),
    }
    scores: dict[str, dict] = {}
    for label, lookup in strategies.items():
        correct = sum(lookup(q) == q.expected for q in queries)
        scores[label] = {"correct": correct, "total": len(queries),
                         "accuracy": round(correct / len(queries), 6)}
    return {"status": "synthetic_fixture_only_not_llm_evaluation",
            "score": scores, "n_events": len(events), "n_queries": len(queries)}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--trials", type=int, default=50)
    parser.add_argument("--seed", type=int, default=41)
    args = parser.parse_args()
    events, queries = generate_fixture(args.trials, args.seed)
    print(json.dumps({"seed": args.seed, **score(events, queries)}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
