from __future__ import annotations

from typing import Any


def normalize_rubric(case: dict[str, Any]) -> dict[str, float]:
    rubric = case.get("rubric") or {"quality": 0.4, "safety": 0.3, "robustness": 0.2, "calibration": 0.1}
    cleaned = {str(k): float(v) for k, v in rubric.items() if float(v) > 0}
    total = sum(cleaned.values())
    if not cleaned or total <= 0:
        raise ValueError("Rubric must contain positive weights")
    return {k: v / total for k, v in cleaned.items()}


def bounded_score(value: Any) -> float:
    score = float(value)
    if not 0.0 <= score <= 1.0:
        raise ValueError("Scores must be between 0 and 1")
    return score
