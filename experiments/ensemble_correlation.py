#!/usr/bin/env python3
"""Exact synthetic illustration of multi-agent majority reliability.

This is a probability model, NOT a real LLM experiment. Assumes odd number of
binary agents with identical marginal correctness p; with probability rho all
agents share one correctness draw, otherwise draws are independent. Optional
persuasion override converts some correct majority decisions to incorrect ones
under a stipulated rate; this is a scenario parameter, not measured evidence.
"""
from __future__ import annotations
import argparse
import json
import math


def check_probability(v: float, name: str) -> float:
    if not math.isfinite(v) or not 0 <= v <= 1:
        raise ValueError(f"{name} must be finite and between 0 and 1")
    return v


def independent_majority(n: int, p: float) -> float:
    if type(n) is not int or n < 1 or n % 2 != 1:
        raise ValueError("n must be a positive odd integer")
    check_probability(p, "p")
    return sum(math.comb(n, k) * p**k * (1 - p)**(n - k)
               for k in range(n // 2 + 1, n + 1))


def correlated_majority(n: int, p: float, rho: float) -> float:
    check_probability(rho, "rho")
    # Marginal correctness of each agent remains p in both mixture branches.
    return (1 - rho) * independent_majority(n, p) + rho * p


def persuaded_majority(n: int, p: float, rho: float, override: float) -> float:
    check_probability(override, "override")
    # A deliberately simple stress model: on a fraction override of correctly
    # resolved cases a convincing wrong group member overturns consensus.
    # It does not represent a measured or realistic adversarial attack rate.
    return correlated_majority(n, p, rho) * (1 - override)


def analyze(n: int = 5, p: float = 0.70, rho: float = 0.80,
            override: float = 0.15) -> dict:
    iid = independent_majority(n, p)
    corr = correlated_majority(n, p, rho)
    persuaded = persuaded_majority(n, p, rho, override)
    return {
        "type": "exact_analytic_synthetic_scenario_not_LLM_measurement",
        "assumptions": {"agents": n, "individual_correctness": p,
                        "shared_draw_probability": rho,
                        "correct_majority_overturned_fraction": override},
        "single_agent_accuracy": p,
        "independent_majority_accuracy": round(iid, 6),
        "correlated_majority_accuracy": round(corr, 6),
        "persuaded_majority_accuracy": round(persuaded, 6),
        "model_calls_if_one_call_per_agent": n,
        "note": "Scenarios depend on stipulated assumptions; no system capability established."
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--agents", type=int, default=5)
    ap.add_argument("--p", type=float, default=0.70)
    ap.add_argument("--rho", type=float, default=0.80)
    ap.add_argument("--override", type=float, default=0.15)
    args = ap.parse_args()
    print(json.dumps(analyze(args.agents, args.p, args.rho, args.override), indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
