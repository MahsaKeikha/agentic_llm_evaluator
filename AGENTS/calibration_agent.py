from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from TOOLS.rubric import bounded_score


@dataclass(frozen=True)
class CalibrationAgent:
    name: str = "calibration_agent"

    def run(self, state: Any) -> dict[str, Any]:
        raw = state.case.get("dimension_scores", {})
        score = bounded_score(raw.get("calibration", 0.0))
        confidence = bounded_score(state.case.get("reported_confidence", score))
        expected = bounded_score(state.case.get("observed_accuracy", score))
        error = abs(confidence - expected)
        result = {"dimension": "calibration", "score": score, "confidence": confidence, "observed_accuracy": expected, "calibration_error": round(error, 6)}
        state.judgments[self.name] = result
        state.evidence.append({"source": self.name, **result})
        if error > 0.2:
            state.risks.append("Calibration error exceeds 0.20")
        state.record(self.name, "checked calibration", result)
        return result
