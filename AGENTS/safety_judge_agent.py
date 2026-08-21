from TOOLS.safety_scan_tool import scan_safety


class SafetyJudgeAgent:
    name = "safety_judge"

    def run(self, case: dict) -> dict:
        findings = [scan_safety(sample.get("output", "")) for sample in case.get("samples", [])]
        return {"agent": self.name, "findings": findings, "blocked": any(item["blocked"] for item in findings)}
