# F37 Agentic LLM Evaluator

A standalone multi-agent reference implementation for evaluating large language model behavior with explicit metrics, adversarial testing, calibration checks, evidence tracking, and human review gates.

## Direct agent links

- [Evaluation Planner Agent](AGENTS/evaluation_planner_agent.py)
- [Quality Judge Agent](AGENTS/quality_judge_agent.py)
- [Safety Judge Agent](AGENTS/safety_judge_agent.py)
- [Robustness Agent](AGENTS/robustness_agent.py)
- [Calibration Agent](AGENTS/calibration_agent.py)

## Core implementation

- [All agents](AGENTS/)
- [All tools](TOOLS/)
- [All skills](SKILLS/)
- [Orchestration](orchestration/)
- [Documentation](docs/)
- [Tests](tests/)

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
