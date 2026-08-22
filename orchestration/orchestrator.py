from __future__ import annotations

from typing import Any

from AGENTS.adjudication_agent import AdjudicationAgent
from AGENTS.calibration_agent import CalibrationAgent
from AGENTS.evaluation_planner_agent import EvaluationPlannerAgent
from AGENTS.quality_judge_agent import QualityJudgeAgent
from AGENTS.robustness_agent import RobustnessAgent
from AGENTS.safety_judge_agent import SafetyJudgeAgent
from orchestration.state import EvaluationState
from safety.approval_gate import can_finalize

SYSTEM_ID = "F37"
SYSTEM_NAME = "Agentic LLM Evaluator"
VERSION = "1.0.0"


def run_system(case: dict[str, Any], approve: bool = False) -> dict[str, Any]:
    state = EvaluationState(case=case)
    state.record("orchestrator", "evaluation started", {"system_id": SYSTEM_ID, "version": VERSION})

    EvaluationPlannerAgent().run(state)
    if not state.risks:
        QualityJudgeAgent().run(state)
        SafetyJudgeAgent().run(state)
        RobustnessAgent().run(state)
        CalibrationAgent().run(state)
    adjudication = AdjudicationAgent().run(state)

    minimum = float(case.get("minimum_score", 0.7))
    minimum_score_met = float(adjudication.get("weighted_score", 0.0)) >= minimum
    human_review_required = bool(case.get("requires_human_review", True))
    finalized = can_finalize(
        risks=state.risks,
        disagreements=state.disagreements,
        minimum_score_met=minimum_score_met,
        human_review_required=human_review_required,
        approve=approve,
    )

    if finalized:
        status = "approved_evaluation"
    elif state.risks or state.disagreements or not minimum_score_met:
        status = "review_required"
    else:
        status = "awaiting_human_review"

    state.record("orchestrator", "finalization gate evaluated", {
        "minimum_score": minimum,
        "minimum_score_met": minimum_score_met,
        "human_review_required": human_review_required,
        "approve": approve,
        "status": status,
    })

    return {
        "system_id": SYSTEM_ID,
        "system_name": SYSTEM_NAME,
        "version": VERSION,
        "maturity": "L3 Gold Standard",
        "run_id": state.run_id,
        "plan": state.plan,
        "judgments": state.judgments,
        "evidence": state.evidence,
        "disagreements": state.disagreements,
        "risks": state.risks,
        "weighted_score": adjudication.get("weighted_score", 0.0),
        "status": status,
        "trace": state.trace,
    }
