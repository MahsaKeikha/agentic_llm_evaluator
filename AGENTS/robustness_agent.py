from TOOLS.perturbation_tool import build_perturbations


class RobustnessAgent:
    name = "robustness"

    def run(self, case: dict) -> dict:
        prompts = [sample.get("prompt", "") for sample in case.get("samples", [])]
        perturbations = [build_perturbations(prompt) for prompt in prompts]
        return {"agent": self.name, "perturbations": perturbations, "coverage": sum(len(x) for x in perturbations)}
