from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from TOOLS.rubric import bounded_score


@dataclass(frozen=True)
class AdjudicationAgent:
    name: str = "adjudication_agent"
    disagreement_tolerance: float = 0.15

    def run(self, state: Any) -> dict[str, Any]:
        rubric = state.plan.get("rubric", {})
        by_dimension = {item.get("dimension"): item for item in state.judgments.values() if item.get("dimension")}
        missing = [name for name in rubric if name not in by_dimension]
        if missing:
            state.disagreements.append("Missing judgments: " + ", ".join(missing))

        reviewer_scores = state.case.get("reviewer_scores", {})
        disagreement_details: list[dict[str, Any]] = []
        for dimension, reviewer_score in reviewer_scores.items():
            if dimension not in by_dimension:
                continue
            primary = float(by_dimension[dimension]["score"])
            secondary = bounded_score(reviewer_score)
            gap = abs(primary - secondary)
            if gap > self.disagreement_tolerance:
                detail = {
                    "dimension": dimension,
                    "primary": primary,
                    "reviewer": secondary,
                    "gap": round(gap, 6),
                }
                disagreement_details.append(detail)
                state.disagreements.append(
                    f"Judge disagreement on {dimension}: gap {gap:.3f} exceeds {self.disagreement_tolerance:.2f}"
                )

        weighted = sum(float(by_dimension[name]["score"]) * weight for name, weight in rubric.items() if name in by_dimension)
        result = {
            "weighted_score": round(weighted, 6),
            "missing_dimensions": missing,
            "judge_disagreements": disagreement_details,
            "decision": "review_required" if missing or state.risks or state.disagreements else "complete",
        }
        state.judgments[self.name] = result
        state.record(self.name, "adjudicated evaluation", result)
        return result
