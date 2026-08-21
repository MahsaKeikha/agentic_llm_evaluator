def summarize_safety(findings: list[dict]) -> dict:
    blocked = [item for item in findings if item.get("blocked")]
    return {"blocked_count": len(blocked), "pass": not blocked}
