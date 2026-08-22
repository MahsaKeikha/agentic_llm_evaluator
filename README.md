# F37 Agentic LLM Evaluator

**Maturity:** L3 Gold Standard  
**Version:** 1.0.0

A reproducible multi-agent reference implementation for evaluating language-model outputs with explicit rubrics, independent judges, robustness testing, calibration checks, evidence provenance, adjudication, and human review gates.

## Architecture

The evaluation pipeline separates planning, quality judgment, safety judgment, robustness analysis, calibration analysis, and adjudication. Each role writes traceable artifacts into shared evaluation state. Finalization is controlled by explicit score, safety, disagreement, and human-review gates.

## Agents

- Evaluation Planner
- Quality Judge
- Safety Judge
- Robustness Agent
- Calibration Agent
- Adjudication Agent

## Core quality controls

- rubric weights are normalized and validated
- scores are bounded to 0 through 1
- safety flags cannot be overridden by approval
- perturbation instability is surfaced as a review risk
- calibration error is measured explicitly
- missing candidate content stops substantive judging
- minimum-score failure cannot be overridden by human approval
- cross-judge disagreement forces adjudication or review
- all agent decisions and evidence are traceable

## Reproduce

```bash
python -m pip install -e .[dev]
ruff check .
pytest -q
python evals/run_benchmarks.py
python evals/heldout_suite.py
python examples/minimal.py
python examples/complete.py
python run.py
```

CI runs the full gate on Python 3.10, 3.11, and 3.12 and publishes the held-out result artifact from Python 3.12.

## L3 meaning

L3 means this repository is an independently reviewable and reproducible reference implementation under the Agentic AI Library Gold Standard. It does not claim universal evaluator correctness, perfect alignment with every policy framework, or autonomous authority over consequential model deployment decisions.

## Documentation

See `docs/ARCHITECTURE.md`, `docs/AGENTS.md`, `docs/EVALUATION.md`, `docs/SAFETY.md`, `docs/EXTENDING.md`, and `docs/L3_AUDIT.md`.

## License

MIT. See `LICENSE`.
