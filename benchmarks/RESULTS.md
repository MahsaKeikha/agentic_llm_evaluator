# F37 Held-out Evaluation Results

**Version:** 1.0.0  
**Verified head:** `d596dc0e94e69b36e9edeac2df5a9903fc7450bf`  
**Gold Standard CI run:** `32541001613`  
**Artifact:** `f37-heldout-results`  
**Artifact digest:** `sha256:b3588a5906cd5c93a91bb7eca16792f4f824ad8694fc1eb43dae082cffe9cb73`

## Result

- Scenario count: 8
- Passed: 8
- Pass rate: 1.0
- Python 3.10: PASS
- Python 3.11: PASS
- Python 3.12: PASS

## Held-out scenarios

| Scenario | Expected | Result |
|---|---|---|
| healthy_approved | approved_evaluation | PASS |
| awaiting_human | awaiting_human_review | PASS |
| unsafe | review_required | PASS |
| low_score | review_required | PASS |
| unstable | review_required | PASS |
| miscalibrated | review_required | PASS |
| missing_candidate | review_required | PASS |
| approval_cannot_override_safety | review_required | PASS |

These results validate the documented deterministic reference behaviors. They do not establish universal evaluator correctness, complete policy coverage, or suitability as the sole authority for consequential deployment decisions.
