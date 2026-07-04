from __future__ import annotations

from dataclasses import dataclass
from statistics import mean, median, pstdev
from typing import Iterable, Mapping


@dataclass(frozen=True)
class Window:
    """Time window in seconds relative to the marked interaction start."""

    start_s: float
    end_s: float

    def contains(self, value_s: float) -> bool:
        return self.start_s <= value_s < self.end_s


DEFAULT_BASELINE = Window(-300.0, 0.0)
DEFAULT_RESPONSE = Window(0.0, 300.0)


def extract_window(
    rows: Iterable[Mapping[str, str | float | int]],
    *,
    time_key: str,
    value_key: str,
    window: Window,
) -> list[tuple[float, float]]:
    values: list[tuple[float, float]] = []
    for row in rows:
        time_s = float(row[time_key])
        if window.contains(time_s):
            values.append((time_s, float(row[value_key])))
    return values


def estimate_sample_interval(samples: list[tuple[float, float]]) -> float:
    if len(samples) < 2:
        return 0.0
    deltas = [
        later[0] - earlier[0]
        for earlier, later in zip(samples, samples[1:])
        if later[0] > earlier[0]
    ]
    return median(deltas) if deltas else 0.0


def summarize_response(
    rows: Iterable[Mapping[str, str | float | int]],
    *,
    time_key: str = "time_s",
    value_key: str = "value",
    baseline: Window = DEFAULT_BASELINE,
    response: Window = DEFAULT_RESPONSE,
    threshold_sd: float = 3.0,
) -> dict[str, float | None]:
    materialized = list(rows)
    baseline_samples = extract_window(
        materialized, time_key=time_key, value_key=value_key, window=baseline
    )
    response_samples = extract_window(
        materialized, time_key=time_key, value_key=value_key, window=response
    )

    if not baseline_samples or not response_samples:
        return {
            "baseline_mean": None,
            "baseline_sd": None,
            "response_peak_abs": None,
            "response_auc_abs": None,
            "response_mean_shift": None,
            "latency_s": None,
            "n_baseline": float(len(baseline_samples)),
            "n_response": float(len(response_samples)),
        }

    baseline_values = [value for _, value in baseline_samples]
    response_values = [value for _, value in response_samples]
    baseline_mean = mean(baseline_values)
    baseline_sd = pstdev(baseline_values) if len(baseline_values) > 1 else 0.0
    centered = [(time_s, value - baseline_mean) for time_s, value in response_samples]
    centered_values = [value for _, value in centered]
    dt = estimate_sample_interval(response_samples)
    threshold = threshold_sd * baseline_sd

    latency_s: float | None = None
    if threshold > 0:
        for time_s, value in centered:
            if abs(value) >= threshold:
                latency_s = time_s
                break

    return {
        "baseline_mean": baseline_mean,
        "baseline_sd": baseline_sd,
        "response_peak_abs": max(abs(value) for value in centered_values),
        "response_auc_abs": sum(abs(value) for value in centered_values) * dt,
        "response_mean_shift": mean(response_values) - baseline_mean,
        "latency_s": latency_s,
        "n_baseline": float(len(baseline_samples)),
        "n_response": float(len(response_samples)),
    }

