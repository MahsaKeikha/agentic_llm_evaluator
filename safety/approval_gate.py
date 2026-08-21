from __future__ import annotations


def can_finalize(*, risks: list[str], disagreements: list[str], minimum_score_met: bool, human_review_required: bool, approve: bool) -> bool:
    if risks or disagreements or not minimum_score_met:
        return False
    if human_review_required and not approve:
        return False
    return True
