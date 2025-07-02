"""Coding agent responsible for turning requirements into Python code."""


class CodingAgent:
    """Simple implementation that generates code from a requirement dict."""

    def run(self, requirements: dict) -> str:
        """Generate Python code implementing the requested functionality."""

        title = requirements.get("title", "").lower()
        if "bmi" in title:
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

        # Fallback: no code generated
        return ""
