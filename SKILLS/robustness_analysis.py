def robustness_coverage(perturbations: list[list[str]]) -> int:
    return sum(len(items) for items in perturbations)
