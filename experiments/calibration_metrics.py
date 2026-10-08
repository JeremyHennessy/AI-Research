#!/usr/bin/env python3
"""Binary outcome calibration metrics and validation-only temperature fitting.

No pretrained model, private data or network access. Outputs only a toy sanity
check. This tool tests measurement code, not any real-world model improvement.
"""
from __future__ import annotations
import argparse
import json
import math
from typing import Sequence

EPS = 1e-12


def validate(predictions: Sequence[float], labels: Sequence[int]) -> None:
    if not predictions or len(predictions) != len(labels):
        raise ValueError("non-empty predictions and labels required, same length")
    for p, y in zip(predictions, labels):
        if not isinstance(p, (int, float)) or not math.isfinite(p) or p < 0 or p > 1:
            raise ValueError("probabilities must be finite within [0,1]")
        if type(y) is not int or y not in (0, 1):
            raise ValueError("labels must be integer 0 or 1")


def brier(predictions: Sequence[float], labels: Sequence[int]) -> float:
    validate(predictions, labels)
    return sum((p - y)**2 for p, y in zip(predictions, labels)) / len(labels)


def log_loss(predictions: Sequence[float], labels: Sequence[int]) -> float:
    validate(predictions, labels)
    def loss(p: float, y: int) -> float:
        p = min(1 - EPS, max(EPS, p))
        return -(y*math.log(p) + (1-y)*math.log(1-p))
    return sum(loss(p, y) for p, y in zip(predictions, labels)) / len(labels)


def classification_ece(predictions: Sequence[float], labels: Sequence[int],
                       bins: int = 10) -> float:
    """Top-class ECE on binary decisions; distinct from positive-class ECE."""
    validate(predictions, labels)
    if type(bins) is not int or bins < 1 or bins > 100:
        raise ValueError("bins must be integer in [1,100]")
    groups: list[list[tuple[float, float]]] = [[] for _ in range(bins)]
    for p, y in zip(predictions, labels):
        conf = max(p, 1-p)
        good = float(int(p >= .5) == y)
        idx = min(bins-1, int(conf * bins))
        groups[idx].append((conf, good))
    n = len(labels)
    return sum((len(g) / n) * abs(sum(x[0] for x in g) / len(g) -
                                  sum(x[1] for x in g) / len(g))
               for g in groups if g)


def selective_risk(predictions: Sequence[float], labels: Sequence[int],
                   coverages: Sequence[float] = (.25, .50, 1.0)) -> list[dict]:
    validate(predictions, labels)
    indexed = sorted(enumerate(predictions), key=lambda t: (-abs(t[1]-.5), t[0]))
    output = []
    for coverage in coverages:
        if not isinstance(coverage, (int,float)) or not math.isfinite(coverage) or not 0 < coverage <= 1:
            raise ValueError("coverages must be in (0, 1]")
        n = max(1, math.ceil(len(labels) * coverage))
        selected = indexed[:n]
        mistakes = sum(int((p >= .5) != labels[i]) for i, p in selected)
        output.append({"requested_coverage": float(coverage),
                       "actual_coverage": n / len(labels),
                       "errors": mistakes, "selected": n,
                       "risk": mistakes / n})
    return output


def temperature_transform(predictions: Sequence[float], temp: float) -> list[float]:
    if not isinstance(temp, (float,int)) or not math.isfinite(temp) or temp <= 0:
        raise ValueError("temperature must be finite and > 0")
    result = []
    for p in predictions:
        if not isinstance(p, (int,float)) or not math.isfinite(p) or p < 0 or p > 1:
            raise ValueError("probabilities must be within [0,1]")
        q = min(1-EPS, max(EPS, p))
        logit = math.log(q/(1-q))/temp
        result.append(1/(1+math.exp(-logit)) if logit >= 0 else math.exp(logit)/(1+math.exp(logit)))
    return result


def fit_temperature(dev_predictions: Sequence[float], dev_labels: Sequence[int],
                    grid: Sequence[float] = (.5, .75, 1., 1.5, 2., 3., 5., 10.)) -> float:
    """Search ONLY supplied dev data. Caller must keep test sealed."""
    validate(dev_predictions, dev_labels)
    if not grid:
        raise ValueError("temperature grid cannot be empty")
    return min(grid, key=lambda t: log_loss(temperature_transform(dev_predictions, t),
                                           dev_labels))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--bins", type=int, default=5)
    args = parser.parse_args()
    # Toy predictions deliberately overconfident. Not real model outputs.
    dev_p, dev_y = [.95,.8,.85,.2,.1,.9,.7,.05], [0,1,0,1,0,1,1,0]
    test_p, test_y = [.9,.7,.9,.1,.2,.8,.6,.1], [0,1,1,1,0,1,0,0]
    T = fit_temperature(dev_p, dev_y)
    before = {"brier": brier(test_p,test_y),"nll":log_loss(test_p,test_y),
              "classification_ece": classification_ece(test_p,test_y,args.bins),
              "risk_by_coverage": selective_risk(test_p,test_y)}
    after_p = temperature_transform(test_p,T)
    after = {"brier": brier(after_p,test_y),"nll":log_loss(after_p,test_y),
             "classification_ece": classification_ece(after_p,test_y,args.bins),
             "risk_by_coverage": selective_risk(after_p,test_y)}
    print(json.dumps({"status":"synthetic_metrics_fixture_only_not_real_model",
                      "temperature_selected_on_dev":T,
                      "test_before":before,"test_after":after},indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
