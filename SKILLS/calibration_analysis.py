def calibration_grade(ece: float) -> str:
    if ece <= 0.1:
        return "strong"
    if ece <= 0.25:
        return "moderate"
    return "weak"
