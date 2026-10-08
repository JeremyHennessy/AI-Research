import math
import unittest
from experiments.ensemble_correlation import (
    analyze, independent_majority, correlated_majority, persuaded_majority
)


class SyntheticEnsembleTests(unittest.TestCase):
    def test_single_agent_always_matches_p(self):
        for p in (0.0, .3, .5, .7, 1.0):
            self.assertAlmostEqual(independent_majority(1, p), p)

    def test_independent_majority_five_agents(self):
        p = .7
        expected = 10*p**3*(1-p)**2 + 5*p**4*(1-p) + p**5
        self.assertAlmostEqual(independent_majority(5, p), expected)
        self.assertGreater(expected, p)

    def test_shared_failure_preserves_marginal_accuracy(self):
        p = .7
        self.assertAlmostEqual(correlated_majority(5, p, 1), p)
        self.assertAlmostEqual(correlated_majority(5, p, 0),
                               independent_majority(5, p))
        self.assertGreater(correlated_majority(5, p, .8), p)
        self.assertLess(correlated_majority(5, p, .8),
                        independent_majority(5, p))

    def test_persuasion_is_explicit_assumption(self):
        base = correlated_majority(5, .7, .8)
        self.assertAlmostEqual(persuaded_majority(5, .7, .8, .15), base*.85)
        self.assertLess(persuaded_majority(5, .7, .8, .15), .7)
        self.assertEqual(analyze()["type"],
                         "exact_analytic_synthetic_scenario_not_LLM_measurement")

    def test_invalid_input_rejected(self):
        for n in (0, -1, 2, 4):
            with self.assertRaises(ValueError):
                independent_majority(n, .7)
        for v in (-.1, 1.1, math.nan, math.inf):
            with self.assertRaises(ValueError):
                correlated_majority(5, .7, v)
            with self.assertRaises(ValueError):
                independent_majority(5, v)


if __name__ == "__main__":
    unittest.main()
