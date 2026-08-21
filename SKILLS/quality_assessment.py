def summarize_quality(scores: list[float]) -> dict:
    return {"mean": round(sum(scores) / len(scores), 4) if scores else 0.0, "count": len(scores)}
