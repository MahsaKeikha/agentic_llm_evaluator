# Evaluation Methodology

The reference implementation uses deterministic bounded scores so behavior is reproducible offline. A rubric is normalized to sum to 1.0. Independent judge scores are recorded with provenance and combined by adjudication into a weighted score.

A passing weighted score is necessary but not sufficient for finalization. Safety risks, robustness instability, calibration error, missing dimensions, or explicit disagreements force review even when the aggregate score is high.

The benchmark suite includes a clean high-quality case, an unsafe high-quality case, and a perturbation-unstable case. CI runs unit tests and the deterministic benchmark runner.

For L3 promotion, future evaluation should add larger held-out suites, inter-rater agreement studies, judge-bias tests, prompt-injection resistance, multilingual cases, long-context cases, regression baselines, and independently reproduced benchmark results.