"""Requirement analysis agent for transforming user input to structured requirements."""


class RequirementAnalysisAgent:
    """Parses natural language requirements into structured form."""

    def run(self, input_text: str) -> dict:
        """Return a simple requirements dictionary.

        Parameters
        ----------
        input_text : str
            Raw requirement from the user.

        Returns
        -------
        dict
            Structured requirement information.
        """

        lowered = input_text.lower()
        if "bmi" in lowered:
            return {
                "title": "BMI Calculator",
                "description": "Calculate Body Mass Index from weight and height.",
                "inputs": ["weight", "height"],
            }

        # Fallback generic requirement
        return {
            "title": "Generic Requirement",
            "description": input_text,
            "inputs": [],
        }
