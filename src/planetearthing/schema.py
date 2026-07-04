from __future__ import annotations

from collections.abc import Mapping


REQUIRED_SESSION_FIELDS = {
    "session_id",
    "plant_id",
    "condition_code",
    "scheduled_start_iso",
    "actual_start_iso",
    "operator_id",
    "participant_id",
    "protocol_version",
}

RECOMMENDED_SESSION_FIELDS = {
    "pressure_glove_file",
    "electrical_file",
    "vibration_file",
    "microclimate_file",
    "audio_video_file",
    "randomization_block",
    "blind_label",
    "soil_moisture_pre",
    "soil_moisture_post",
    "notes",
}


def validate_session_metadata(metadata: Mapping[str, object]) -> list[str]:
    errors: list[str] = []
    for field in sorted(REQUIRED_SESSION_FIELDS):
        value = metadata.get(field)
        if value is None or value == "":
            errors.append(f"missing required field: {field}")

    condition = metadata.get("condition_code")
    if condition and condition not in {
        "HOST_TOUCH_VOICE",
        "REPEATED_NONHOST_TOUCH_VOICE",
        "NOVEL_STRANGER_TOUCH_VOICE",
        "VOICE_PLAYBACK_ONLY",
        "OBJECT_TOUCH",
        "ROBOT_TOUCH",
        "NO_TOUCH_BASELINE",
    }:
        errors.append(f"unknown condition_code: {condition}")

    return errors

