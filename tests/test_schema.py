import unittest

from planetearthing.schema import validate_session_metadata


class SchemaTests(unittest.TestCase):
    def test_accepts_valid_minimal_metadata(self):
        errors = validate_session_metadata(
            {
                "session_id": "S001",
                "plant_id": "P001",
                "condition_code": "HOST_TOUCH_VOICE",
                "scheduled_start_iso": "2026-07-04T09:00:00+05:30",
                "actual_start_iso": "2026-07-04T09:00:10+05:30",
                "operator_id": "OP001",
                "participant_id": "H001",
                "protocol_version": "0.1.0",
            }
        )
        self.assertEqual(errors, [])

    def test_rejects_unknown_condition(self):
        errors = validate_session_metadata(
            {
                "session_id": "S001",
                "plant_id": "P001",
                "condition_code": "MAGIC",
                "scheduled_start_iso": "2026-07-04T09:00:00+05:30",
                "actual_start_iso": "2026-07-04T09:00:10+05:30",
                "operator_id": "OP001",
                "participant_id": "H001",
                "protocol_version": "0.1.0",
            }
        )
        self.assertIn("unknown condition_code: MAGIC", errors)


if __name__ == "__main__":
    unittest.main()

