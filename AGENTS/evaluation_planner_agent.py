from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from TOOLS.rubric import normalize_rubric


@dataclass(frozen=True)
class EvaluationPlannerAgent:
    name: str = "evaluation_planner_agent"

    def run(self, state: Any) -> dict[str, Any]:
        rubric = normalize_rubric(state.case)
        candidate = str(state.case.get("candidate", "")).strip()
        plan = {"rubric": rubric, "candidate_present": bool(candidate), "dimensions": list(rubric)}
        state.plan = plan
        state.record(self.name, "planned evaluation", plan)
        if not candidate:
            state.risks.append("Candidate output is missing")
        return plan
