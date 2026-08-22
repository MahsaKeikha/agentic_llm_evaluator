from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from TOOLS.rubric import bounded_score


@dataclass(frozen=True)
class SafetyJudgeAgent:
    name: str = "safety_judge_agent"

    def run(self, state: Any) -> dict[str, Any]:
        raw = state.case.get("dimension_scores", {})
        score = bounded_score(raw.get("safety", 0.0))
        flags = [str(x) for x in state.case.get("safety_flags", []) if str(x).strip()]
        result = {"dimension": "safety", "score": score, "flags": flags}
        state.judgments[self.name] = result
        state.evidence.append({"source": self.name, "dimension": "safety", "score": score, "flags": flags})
        if flags:
            state.risks.extend(flags)
        state.record(self.name, "judged safety", result)
        return result
