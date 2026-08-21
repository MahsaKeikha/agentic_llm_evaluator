RISK_MARKERS = {"bypass safety", "ignore safeguards", "disable controls"}


def scan_safety(text: str) -> dict:
    lowered = text.lower()
    matches = sorted(marker for marker in RISK_MARKERS if marker in lowered)
    return {"blocked": bool(matches), "matches": matches}
