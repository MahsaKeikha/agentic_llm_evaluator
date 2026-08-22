# Architecture

F37 uses a staged evaluation graph:

1. Evaluation Planner validates the candidate and normalizes the rubric.
2. Quality Judge scores task quality.
3. Safety Judge scores safety and emits blocking flags.
4. Robustness Agent measures sensitivity across perturbation runs.
5. Calibration Agent compares reported confidence with observed accuracy.
6. Adjudication Agent computes the weighted score and checks missing dimensions.
7. The orchestrator applies minimum-score, risk, disagreement, and human-review gates.

Shared `EvaluationState` stores plan, judgments, evidence, disagreements, risks, and a chronological trace. Judge outputs are independent artifacts rather than one monolithic score. The design is deterministic offline so the reference benchmarks can be reproduced without an external model provider.

Production adapters can replace deterministic inputs with model or human judges, but they must preserve the same contracts and provenance fields.