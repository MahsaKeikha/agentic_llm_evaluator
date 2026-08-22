from orchestration.orchestrator import run_system

case = {
    "candidate": "Grounded answer",
    "dimension_scores": {"quality": 0.9, "safety": 0.95, "robustness": 0.9, "calibration": 0.9},
    "reported_confidence": 0.85,
    "observed_accuracy": 0.84,
    "perturbation_scores": [0.88, 0.9, 0.89],
    "minimum_score": 0.8,
}
result = run_system(case, approve=True)
assert result["status"] == "approved_evaluation"
print(result["status"], result["weighted_score"])
