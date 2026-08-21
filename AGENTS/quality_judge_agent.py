from TOOLS.scoring_tool import score_text_quality


class QualityJudgeAgent:
    name = "quality_judge"

    def run(self, case: dict) -> dict:
        scores = [score_text_quality(sample.get("output", "")) for sample in case.get("samples", [])]
        average = sum(scores) / len(scores) if scores else 0.0
        return {"agent": self.name, "scores": scores, "average": round(average, 4)}
