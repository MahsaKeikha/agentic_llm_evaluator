def expected_calibration_error(pairs: list[tuple[float, bool]]) -> float:
    if not pairs:
        return 0.0
    error = sum(abs(max(0.0, min(1.0, c)) - float(ok)) for c, ok in pairs) / len(pairs)
    return round(error, 4)
