from dataclasses import dataclass


@dataclass
class EvaluationPlannerAgent:
    name: str = "evaluation_planner"

    def run(self, case: dict) -> dict:
        criteria = case.get("criteria") or ["quality", "safety", "robustness", "calibration"]
        return {"agent": self.name, "criteria": criteria, "sample_count": len(case.get("samples", []))}
