def score_text_quality(text: str) -> float:
    text = text.strip()
    if not text:
        return 0.0
    length_score = min(len(text) / 400.0, 1.0)
    structure_score = 1.0 if any(mark in text for mark in [".", ":", "\n"]) else 0.5
    return round((length_score + structure_score) / 2.0, 4)
