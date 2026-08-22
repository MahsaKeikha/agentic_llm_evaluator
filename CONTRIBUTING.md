# Contributing

Contributions should preserve the separation between planning, independent judging, adjudication, and finalization gates.

Before opening a pull request:

1. Run `ruff check .`.
2. Run `pytest -q`.
3. Run `python evals/run_benchmarks.py`.
4. Add tests for new behavior, including failure and adversarial cases.
5. Update relevant documentation and CHANGELOG.md.
6. Document any new external dependency, model judge, dataset, or network requirement.

Do not weaken safety or human-review gates merely to make a benchmark pass. New judge dimensions must have explicit score contracts and evidence provenance.