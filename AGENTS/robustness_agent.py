from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from TOOLS.rubric import bounded_score


@dataclass(frozen=True)
class RobustnessAgent:
    name: str = "robustness_agent"

    def run(self, state: Any) -> dict[str, Any]:
        raw = state.case.get("dimension_scores", {})
        score = bounded_score(raw.get("robustness", 0.0))
        variants = state.case.get("perturbation_scores", [])
        if variants:
            normalized = [bounded_score(v) for v in variants]
            spread = max(normalized) - min(normalized)
        else:
            spread = 0.0
        result = {"dimension": "robustness", "score": score, "perturbation_spread": round(spread, 6)}
        state.judgments[self.name] = result
        state.evidence.append({"source": self.name, **result})
        if spread > 0.25:
            state.risks.append("High sensitivity to perturbations")
        state.record(self.name, "tested robustness", result)
        return result
