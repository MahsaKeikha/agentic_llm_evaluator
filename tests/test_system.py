from orchestration.orchestrator import EvaluationOrchestrator


def test_offline_run():
    case = {"samples": [{"prompt": "x", "output": "A complete answer.", "confidence": 0.8, "correct": True}]}
    result = EvaluationOrchestrator().run(case)
    assert result["system_id"] == "F37"
    assert len(result["analyses"]) == 5
    assert result["status"] == "complete"


def test_safety_blocks():
    case = {"samples": [{"prompt": "x", "output": "ignore safeguards and disable controls", "confidence": 0.2, "correct": False}]}
    assert EvaluationOrchestrator().run(case)["status"] == "blocked"
