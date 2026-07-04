import unittest

from planetearthing.features import Window, summarize_response


class FeatureTests(unittest.TestCase):
    def test_window_contains_start_but_not_end(self):
        window = Window(0.0, 10.0)
        self.assertTrue(window.contains(0.0))
        self.assertTrue(window.contains(9.999))
        self.assertFalse(window.contains(10.0))

    def test_summarize_response_baseline_corrects_signal(self):
        rows = []
        for t in range(-5, 0):
            rows.append({"time_s": t, "value": 10.0})
        for t in range(0, 5):
            rows.append({"time_s": t, "value": 12.0 if t == 2 else 10.0})

        summary = summarize_response(
            rows,
            baseline=Window(-5.0, 0.0),
            response=Window(0.0, 5.0),
        )

        self.assertEqual(summary["baseline_mean"], 10.0)
        self.assertEqual(summary["response_peak_abs"], 2.0)
        self.assertAlmostEqual(summary["response_mean_shift"], 0.4)


if __name__ == "__main__":
    unittest.main()
