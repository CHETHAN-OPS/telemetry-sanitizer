"""
Module: NullValueTelemetrySanitizer
Description: Ingests time-series metric lists and sanitizes None values to system baseline floats.
"""

from typing import List, Optional


def sanitize_telemetry(payload: List[Optional[float]]) -> List[float]:
    """Scans incoming telemetry payload and replaces any None entries with baseline 0.0."""
    return [0.0 if value is None else float(value) for value in payload]


def main():
    metric_timeline = [45.2, None, 48.7, None, 51.3]
    sanitized_timeline = sanitize_telemetry(metric_timeline)
    print(
        f"SanitizationPipelineComplete. Cleaned output array timeline: {sanitized_timeline}"
    )


if __name__ == "__main__":
    main()
