import math
import unittest
from experiments.calibration_metrics import (
    brier, log_loss, classification_ece, selective_risk,
    temperature_transform, fit_temperature,
)


class CalibrationTests(unittest.TestCase):
    def test_perfect_predictions(self):
        self.assertEqual(brier([0.,1.],[0,1]),0)
        self.assertEqual(classification_ece([0.,1.],[0,1]),0)
        self.assertLess(log_loss([0.,1.],[0,1]), 1e-8)
        self.assertEqual(selective_risk([0.,1.],[0,1], [1])[0]["risk"],0)

    def test_known_brier_and_logloss(self):
        self.assertAlmostEqual(brier([.5,.5],[0,1]),.25)
        self.assertAlmostEqual(log_loss([.5,.5],[0,1]),math.log(2))
        self.assertGreater(log_loss([.99],[0]),log_loss([.7],[0]))

    def test_temperature_one_identity(self):
        x=[.1,.3,.5,.7,.9]
        for a,b in zip(temperature_transform(x,1.),x):
            self.assertAlmostEqual(a,b)
        hot=temperature_transform([.9,.1],5)
        self.assertLess(hot[0],.9)
        self.assertGreater(hot[1],.1)

    def test_temperature_is_selected_only_from_dev(self):
        # Confidently wrong examples -> larger T favored.
        T=fit_temperature([.99,.99,.01,.01],[0,0,1,1],grid=(.5,1.,3.,10.))
        self.assertEqual(T,10.)
        self.assertLess(log_loss(temperature_transform([.99],10.),[0]),
                        log_loss([.99],[0]))

    def test_selective_risk_respects_coverage(self):
        r=selective_risk([.9,.4,.3,.1],[1,1,0,0],[.5,1.])
        self.assertEqual(r[0]["selected"],2)
        self.assertAlmostEqual(r[1]["actual_coverage"],1.)
        self.assertEqual(r[1]["errors"],1)

    def test_invalid_inputs(self):
        bad=[([.2],[0,1]),([math.nan],[1]),([1.1],[1]),([.2],[2]),([],[])]
        for ps,ys in bad:
            with self.assertRaises(ValueError): brier(ps,ys)
        with self.assertRaises(ValueError): classification_ece([.2],[0],0)
        with self.assertRaises(ValueError): fit_temperature([.2],[0],grid=[])
        with self.assertRaises(ValueError): temperature_transform([.2],0)


if __name__ == "__main__":
    unittest.main()
