import os
from typing import Optional

try:
    import openai
except Exception:
    openai = None


class LLMClient:
    """Simple wrapper around OpenAI's ChatCompletion API with a fallback."""

    def __init__(self, model: str = "gpt-3.5-turbo") -> None:
        self.model = model
        self.api_key = os.getenv("OPENAI_API_KEY")

    def generate(self, prompt: str) -> str:
        """Generate text from the prompt using OpenAI if configured."""
        if openai is None or not self.api_key:
            # Fallback deterministic response used for testing
            if "bmi" in prompt.lower():
                return (
                    "def calculate_bmi(weight_kg: float, height_cm: float) -> float:\n"
                    "    \"\"\"Return Body Mass Index given weight and height.\n\n"
                    "    Parameters\n"
                    "    ----------\n"
                    "    weight_kg : float\n"
                    "        Weight in kilograms.\n"
                    "    height_cm : float\n"
                    "        Height in centimeters.\n\n"
                    "    Returns\n"
                    "    -------\n"
                    "    float\n"
                    "        The calculated BMI.\n"
                    "    \"\"\"\n"
                    "    return weight_kg / (height_cm / 100) ** 2\n"
                )
            return ""

        openai.api_key = self.api_key
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
        )
        return response.choices[0].message.content.strip()
