# Safety and Human Review

F37 treats evaluation as decision support rather than unquestionable ground truth. Aggregate scores never override explicit safety flags or unresolved review conditions.

The finalization gate blocks approval when risks or disagreements remain, when the minimum score is not met, or when required human review has not been granted. Human approval is therefore an additional condition, not a mechanism for bypassing failed criteria.

Production deployments should document judge model identity and version, evaluation-data provenance, conflict-of-interest controls, sensitive-data handling, escalation ownership, and appeal or re-review procedures. Evaluator outputs should be interpreted with known limitations, especially when used for consequential model release or procurement decisions.