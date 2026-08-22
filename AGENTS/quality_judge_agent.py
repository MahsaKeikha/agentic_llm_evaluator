from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from TOOLS.rubric import bounded_score


@dataclass(frozen=True)
class QualityJudgeAgent:
    name: str = "quality_judge_agent"

    def run(self, state: Any) -> dict[str, Any]:
        raw = state.case.get("dimension_scores", {})
        score = bounded_score(raw.get("quality", 0.0))
        result = {"dimension": "quality", "score": score, "rationale": state.case.get("quality_rationale", "deterministic reference score")}
        state.judgments[self.name] = result
        state.evidence.append({"source": self.name, "dimension": "quality", "score": score})
        state.record(self.name, "judged quality", result)
        return result
