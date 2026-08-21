def design_evaluation(criteria: list[str]) -> dict:
    return {"criteria": list(dict.fromkeys(criteria)), "requires_human_review": "safety" in criteria}
