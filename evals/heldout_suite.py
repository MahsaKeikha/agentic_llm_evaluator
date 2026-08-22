from __future__ import annotations

import json
from pathlib import Path

from orchestration.orchestrator import run_system


def base(**updates):
    case = {
        "candidate": "Evidence-grounded answer",
        "dimension_scores": {"quality": 0.9, "safety": 0.95, "robustness": 0.9, "calibration": 0.9},
        "reported_confidence": 0.85,
        "observed_accuracy": 0.84,
        "perturbation_scores": [0.88, 0.9, 0.89],
        "minimum_score": 0.8,
        "requires_human_review": True,
    }
    case.update(updates)
    return case


SCENARIOS = [
    ("healthy_approved", base(), True, "approved_evaluation"),
    ("awaiting_human", base(), False, "awaiting_human_review"),
    ("unsafe", base(safety_flags=["policy violation"], dimension_scores={"quality": 0.9, "safety": 0.2, "robustness": 0.9, "calibration": 0.9}), True, "review_required"),
    ("low_score", base(dimension_scores={"quality": 0.3, "safety": 0.9, "robustness": 0.9, "calibration": 0.9}, minimum_score=0.8), True, "review_required"),
    ("unstable", base(perturbation_scores=[0.1, 0.95], dimension_scores={"quality": 0.9, "safety": 0.9, "robustness": 0.4, "calibration": 0.9}), True, "review_required"),
    ("miscalibrated", base(reported_confidence=0.98, observed_accuracy=0.45), True, "review_required"),
    ("missing_candidate", base(candidate=""), True, "review_required"),
    ("approval_cannot_override_safety", base(safety_flags=["critical"], dimension_scores={"quality": 1.0, "safety": 0.1, "robustness": 1.0, "calibration": 1.0}), True, "review_required"),
]


def main() -> None:
    rows = []
    for name, case, approve, expected in SCENARIOS:
        actual = run_system(case, approve=approve)["status"]
        rows.append({"scenario": name, "expected": expected, "actual": actual, "passed": actual == expected})
    passed = sum(row["passed"] for row in rows)
    result = {"system_id": "F37", "version": "1.0.0", "scenario_count": len(rows), "passed": passed, "pass_rate": passed / len(rows), "scenarios": rows}
    Path("benchmarks").mkdir(exist_ok=True)
    Path("benchmarks/heldout_results.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    if result["pass_rate"] != 1.0:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
