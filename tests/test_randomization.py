import unittest
from datetime import date

from planetearthing.randomization import DEFAULT_CONDITIONS, generate_schedule


class RandomizationTests(unittest.TestCase):
    def test_schedule_is_balanced_within_plant_week(self):
        rows = generate_schedule(
            plants=["P001"],
            start_date=date(2026, 8, 1),
            weeks=2,
            seed=123,
        )
        self.assertEqual(len(rows), len(DEFAULT_CONDITIONS) * 2)
        for week in ["W01", "W02"]:
            conditions = [row.condition_code for row in rows if row.date_block == week]
            self.assertEqual(sorted(conditions), sorted(DEFAULT_CONDITIONS))

    def test_schedule_is_deterministic_for_seed(self):
        first = generate_schedule(
            plants=["P001", "P002"],
            start_date=date(2026, 8, 1),
            weeks=1,
            seed=456,
        )
        second = generate_schedule(
            plants=["P001", "P002"],
            start_date=date(2026, 8, 1),
            weeks=1,
            seed=456,
        )
        self.assertEqual(first, second)


if __name__ == "__main__":
    unittest.main()

