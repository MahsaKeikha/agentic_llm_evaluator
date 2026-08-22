# Extending F37

To add a new evaluation dimension:

1. Add the dimension and weight to the rubric.
2. Implement a specialist judge with a bounded score contract.
3. Record evidence and trace events from the specialist.
4. Add the judge artifact before adjudication.
5. Add unit tests for normal, missing, malformed, and adversarial inputs.
6. Add at least one benchmark scenario that proves the new dimension changes final behavior when appropriate.
7. Update agent and evaluation documentation.

External LLM judges should be wrapped behind adapters. Adapters must record provider, model/version, prompt or rubric version, latency/error metadata where relevant, and source provenance. Do not make network access mandatory for the core offline example suite.