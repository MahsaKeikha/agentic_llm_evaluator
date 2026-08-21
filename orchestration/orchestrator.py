from AGENTS.evaluation_planner_agent import EvaluationPlannerAgent
from AGENTS.quality_judge_agent import QualityJudgeAgent
from AGENTS.safety_judge_agent import SafetyJudgeAgent
from AGENTS.robustness_agent import RobustnessAgent
from AGENTS.calibration_agent import CalibrationAgent


class EvaluationOrchestrator:
    def __init__(self):
        self.agents = [EvaluationPlannerAgent(), QualityJudgeAgent(), SafetyJudgeAgent(), RobustnessAgent(), CalibrationAgent()]

    def run(self, case: dict) -> dict:
        trace = []
        analyses = {}
        for step, agent in enumerate(self.agents, 1):
            result = agent.run(case)
            analyses[agent.name] = result
            trace.append({"step": step, "actor": agent.name, "event": "completed"})
        blocked = bool(analyses["safety_judge"].get("blocked"))
        return {"system_id": "F37", "system_name": "Agentic LLM Evaluator", "version": "0.1.0", "analyses": analyses, "status": "blocked" if blocked else "complete", "trace": trace}
