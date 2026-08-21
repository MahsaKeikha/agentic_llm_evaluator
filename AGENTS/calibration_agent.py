from TOOLS.calibration_tool import expected_calibration_error


class CalibrationAgent:
    name = "calibration"

    def run(self, case: dict) -> dict:
        pairs = [(float(s.get("confidence", 0.0)), bool(s.get("correct", False))) for s in case.get("samples", [])]
        return {"agent": self.name, "ece": expected_calibration_error(pairs), "samples": len(pairs)}
