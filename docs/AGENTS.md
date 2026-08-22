# Agent Contracts

## Evaluation Planner Agent
Mission: establish the evaluation contract before judging. Input: candidate, rubric, thresholds. Output: normalized rubric and planned dimensions. Escalates when the candidate is missing or the rubric is invalid.

## Quality Judge Agent
Mission: assess output quality against the declared rubric. Input: candidate and quality evidence. Output: bounded quality score and rationale. Must not silently invent missing evidence.

## Safety Judge Agent
Mission: independently assess safety. Input: candidate and safety signals. Output: safety score and blocking flags. Any substantive safety flag is preserved as a risk for adjudication.

## Robustness Agent
Mission: test stability under perturbation. Input: candidate and perturbation scores. Output: robustness score and observed spread. Large spread triggers review.

## Calibration Agent
Mission: test confidence calibration. Input: reported confidence and observed accuracy. Output: calibration score and absolute calibration error. Large error triggers review.

## Adjudication Agent
Mission: synthesize independent judgments without erasing disagreement or risk. Input: rubric and judge artifacts. Output: weighted score, missing dimensions, and review decision.

Agents may not bypass the finalization gate or overwrite another judge's evidence.