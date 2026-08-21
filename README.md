# F37 Agentic LLM Evaluator

A standalone multi-agent reference implementation for evaluating large language model behavior with explicit metrics, adversarial testing, calibration checks, evidence tracking, and human review gates.

## Visible architecture

The repository exposes real executable modules directly in `AGENTS/`, `TOOLS/`, and `SKILLS/` so readers can inspect each component without searching through a monolithic source file.

## Agent team

- Evaluation Planner Agent
- Quality Judge Agent
- Safety Judge Agent
- Robustness Agent
- Calibration Agent
- Evaluation Orchestrator

## Execution

```bash
python run.py
pytest -q
```

The default example runs offline with deterministic fixtures and no model API key.

## Maturity

Reference implementation. Production use requires task-specific benchmark validation, provider integration testing, security review, and independent evaluation.

## AI Engineering Handbook Series

Companion books by Mahsa Keikha:

- https://a.co/d/0cbZnSMi
- https://a.co/d/07HnRY7H

## License

MIT.
