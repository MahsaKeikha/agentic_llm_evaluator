from orchestration.orchestrator import run_system


def good_case():
    return {
        "candidate": "A grounded answer with citations and uncertainty.",
        "dimension_scores": {"quality": 0.9, "safety": 0.95, "robustness": 0.85, "calibration": 0.9},
        "reported_confidence": 0.85,
        "observed_accuracy": 0.82,
        "perturbation_scores": [0.86, 0.84, 0.87],
        "minimum_score": 0.8,
        "requires_human_review": True,
    }


def test_good_case_waits_for_human_review():
    result = run_system(good_case())
    assert result["status"] == "awaiting_human_review"
    assert result["weighted_score"] >= 0.8


def test_human_approval_finalizes_clean_case():
    assert run_system(good_case(), approve=True)["status"] == "approved_evaluation"


def test_safety_flags_force_review():
    case = good_case()
    case["safety_flags"] = ["unsafe instruction detected"]
    assert run_system(case, approve=True)["status"] == "review_required"


def test_low_score_cannot_be_overridden_by_approval():
    case = good_case()
    case["dimension_scores"]["quality"] = 0.1
    assert run_system(case, approve=True)["status"] == "review_required"


def test_missing_candidate_blocks_judging():
    case = good_case()
    case["candidate"] = ""
    result = run_system(case, approve=True)
    assert result["status"] == "review_required"
    assert "Candidate output is missing" in result["risks"]


def test_high_perturbation_spread_forces_review():
    case = good_case()
    case["perturbation_scores"] = [0.1, 0.9]
    result = run_system(case, approve=True)
    assert "High sensitivity to perturbations" in result["risks"]


def test_calibration_error_forces_review():
    case = good_case()
    case["reported_confidence"] = 0.95
    case["observed_accuracy"] = 0.4
    result = run_system(case, approve=True)
    assert "Calibration error exceeds 0.20" in result["risks"]


def test_judge_disagreement_forces_review():
    case = good_case()
    case["reviewer_scores"] = {"quality": 0.55}
    result = run_system(case, approve=True)
    assert result["status"] == "review_required"
    assert result["disagreements"]


def test_invalid_score_is_rejected():
    case = good_case()
    case["dimension_scores"]["quality"] = 1.5
    try:
        run_system(case)
    except ValueError as exc:
        assert "between 0 and 1" in str(exc)
    else:
        raise AssertionError("Expected invalid score to raise ValueError")


def test_trace_contains_all_specialists_and_gate():
    result = run_system(good_case())
    actors = {item["actor"] for item in result["trace"]}
    expected = {
        "evaluation_planner_agent", "quality_judge_agent", "safety_judge_agent",
        "robustness_agent", "calibration_agent", "adjudication_agent", "orchestrator",
    }
    assert expected <= actors


def test_evidence_has_one_record_per_judge():
    result = run_system(good_case())
    sources = {item["source"] for item in result["evidence"]}
    assert {"quality_judge_agent", "safety_judge_agent", "robustness_agent", "calibration_agent"} <= sources
