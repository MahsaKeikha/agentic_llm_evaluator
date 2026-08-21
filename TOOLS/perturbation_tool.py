def build_perturbations(prompt: str) -> list[str]:
    prompt = prompt.strip()
    if not prompt:
        return []
    return [prompt, prompt.upper(), f"Please answer carefully: {prompt}"]
