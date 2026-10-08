import unittest
from experiments.temporal_memory import Event, Query, TimelineMemory, generate_fixture, score


class TemporalMemoryTests(unittest.TestCase):
    def test_current_vs_past_and_retraction(self):
        e = [
            Event("A", "city", "Old", 1, 2, "a"),
            Event("A", "city", "New", 5, 6, "b"),
            Event("A", "city", None, 9, 10, "c"),
        ]
        t = TimelineMemory(reversed(e))
        self.assertIsNone(t.resolve("A", "city", 0))
        self.assertEqual(t.resolve("A", "city", 3), "Old")
        self.assertEqual(t.resolve("A", "city", 7), "New")
        self.assertIsNone(t.resolve("A", "city", 11))
        self.assertIsNone(t.resolve("B", "city", 7))

    def test_conflicts_resolve_by_observation_order(self):
        t = TimelineMemory([Event("A", "x", "updated", 3, 8, "late"),
                            Event("A", "x", "previous", 3, 4, "early")])
        self.assertEqual(t.resolve("A", "x", 6), "updated")

    def test_fixture_repeatable_and_baselines_distinct(self):
        first = generate_fixture(20, 71)
        second = generate_fixture(20, 71)
        self.assertEqual(first, second)
        s = score(*first)
        self.assertEqual(s["score"]["temporal_ledger"]["correct"], 80)
        self.assertEqual(s["status"], "synthetic_fixture_only_not_llm_evaluation")
        self.assertLess(s["score"]["first_observed"]["correct"], 80)
        self.assertLess(s["score"]["most_recent_observation"]["correct"], 80)

    def test_trial_limits(self):
        with self.assertRaises(ValueError):
            generate_fixture(0)
        with self.assertRaises(ValueError):
            generate_fixture(1001)


if __name__ == "__main__":
    unittest.main()
