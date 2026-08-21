import json
from orchestration.orchestrator import EvaluationOrchestrator


if __name__ == "__main__":
    case = {"samples": [{"prompt": "Explain recursion", "output": "Recursion is a function calling itself with a stopping condition.", "confidence": 0.9, "correct": True}]}
    print(json.dumps(EvaluationOrchestrator().run(case), indent=2))
