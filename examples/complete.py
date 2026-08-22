from orchestration.orchestrator import run_system

case = {
    "candidate": "A careful answer with explicit uncertainty and evidence boundaries.",
    "dimension_scores": {"quality": 0.94, "safety": 0.97, "robustness": 0.91, "calibration": 0.92},
    "reported_confidence": 0.86,
    "observed_accuracy": 0.84,
    "perturbation_scores": [0.89, 0.91, 0.9],
    "minimum_score": 0.82,
    "requires_human_review": True,
}
result = run_system(case, approve=True)
assert result["status"] == "approved_evaluation"
assert len(result["evidence"]) >= 4
assert len(result["trace"]) >= 7
print(result["status"], result["weighted_score"], len(result["evidence"]))
