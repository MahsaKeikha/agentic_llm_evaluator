from __future__ import annotations

from orchestration.orchestrator import run_system

CASES = [
    {
        "name": "high_quality_safe",
        "case": {
            "candidate": "Evidence-grounded answer",
            "dimension_scores": {"quality": 0.92, "safety": 0.96, "robustness": 0.88, "calibration": 0.9},
            "reported_confidence": 0.86,
            "observed_accuracy": 0.84,
            "perturbation_scores": [0.88, 0.86, 0.9],
            "minimum_score": 0.8,
        },
        "expected": "approved_evaluation",
    },
    {
        "name": "unsafe_candidate",
        "case": {
            "candidate": "Unsafe output",
            "dimension_scores": {"quality": 0.9, "safety": 0.2, "robustness": 0.8, "calibration": 0.8},
            "safety_flags": ["policy violation"],
            "minimum_score": 0.7,
        },
        "expected": "review_required",
    },
    {
        "name": "unstable_candidate",
        "case": {
            "candidate": "Brittle output",
            "dimension_scores": {"quality": 0.85, "safety": 0.9, "robustness": 0.4, "calibration": 0.8},
            "perturbation_scores": [0.15, 0.85],
            "minimum_score": 0.7,
        },
        "expected": "review_required",
    },
]


def main() -> None:
    failures = []
    for scenario in CASES:
        result = run_system(scenario["case"], approve=True)
        ok = result["status"] == scenario["expected"]
        print(f"{scenario['name']}: {'PASS' if ok else 'FAIL'} | {result['status']} | score={result['weighted_score']}")
        if not ok:
            failures.append(scenario["name"])
    if failures:
        raise SystemExit("Benchmark failures: " + ", ".join(failures))


if __name__ == "__main__":
    main()
