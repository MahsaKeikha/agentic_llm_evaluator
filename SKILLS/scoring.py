from __future__ import annotations

from statistics import mean
from typing import Any

from TOOLS.rubric import bounded_score


def score_dimensions(raw: dict[str, Any], rubric: dict[str, float]) -> dict[str, Any]:
    missing = [name for name in rubric if name not in raw]
    if missing:
        raise ValueError(f"Missing rubric dimensions: {', '.join(missing)}")
    scores = {name: bounded_score(raw[name]) for name in rubric}
    weighted = sum(scores[name] * rubric[name] for name in rubric)
    return {"scores": scores, "weighted_score": round(weighted, 6)}


def agreement(judgments: list[dict[str, Any]], tolerance: float = 0.15) -> dict[str, Any]:
    values = [float(item["weighted_score"]) for item in judgments]
    if not values:
        return {"mean": 0.0, "spread": 1.0, "agreed": False}
    spread = max(values) - min(values)
    return {"mean": round(mean(values), 6), "spread": round(spread, 6), "agreed": spread <= tolerance}
