# F37 Agentic LLM Evaluator

A multi-agent reference implementation for evaluating language-model outputs with explicit rubrics, independent judges, robustness testing, calibration checks, evidence provenance, adjudication, and human review gates.

## Architecture

The evaluation pipeline separates planning, quality judgment, safety judgment, robustness analysis, calibration analysis, and adjudication. Each role writes traceable artifacts into shared evaluation state. Finalization is controlled by explicit score, safety, disagreement, and human-review gates.

## Agents

- [Evaluation Planner](AGENTS/evaluation_planner_agent.py)
- [Quality Judge](AGENTS/quality_judge_agent.py)
- [Safety Judge](AGENTS/safety_judge_agent.py)
- [Robustness Agent](AGENTS/robustness_agent.py)
- [Calibration Agent](AGENTS/calibration_agent.py)
- [Adjudication Agent](AGENTS/adjudication_agent.py)

## Core quality controls

- rubric weights are normalized and validated
- scores are bounded to 0 through 1
- safety flags cannot be overridden by approval
- perturbation instability is surfaced as a review risk
- calibration error is measured explicitly
- missing candidate content stops substantive judging
- minimum-score failure cannot be overridden by human approval
- all agent decisions and evidence are traceable

## Run

```bash
python -m pip install -e .[dev]
python run.py
pytest -q
python evals/run_benchmarks.py
```

## Maturity

**L2 candidate** under the Agentic AI Library Gold Standard. L3 is intentionally not claimed until CI, benchmark reproducibility, broader adversarial suites, and independent validation are demonstrated.

## Documentation

- [Architecture](docs/ARCHITECTURE.md)
- [Agent contracts](docs/AGENTS.md)
- [Evaluation methodology](docs/EVALUATION.md)
- [Safety and review](docs/SAFETY.md)
- [Extending the evaluator](docs/EXTENDING.md)

## License

MIT. See [LICENSE](LICENSE).
