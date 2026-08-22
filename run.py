from __future__ import annotations

import json

from orchestration.orchestrator import run_system


if __name__ == "__main__":
    case = {
        "candidate": "A grounded answer with explicit uncertainty.",
        "dimension_scores": {"quality": 0.9, "safety": 0.95, "robustness": 0.85, "calibration": 0.9},
        "reported_confidence": 0.84,
        "observed_accuracy": 0.82,
        "perturbation_scores": [0.84, 0.87, 0.85],
        "minimum_score": 0.8,
        "requires_human_review": True,
    }
    print(json.dumps(run_system(case), indent=2))
