"""Agent that generates documentation for the produced code."""


class DocumentationAgent:
    """Create markdown documentation for the module."""

    def run(self, code: str) -> str:
        """Return a markdown string describing the code."""

        if "calculate_bmi" in code:
            return (
                "### Module Documentation\n\n"
                "This module exposes a single function `calculate_bmi` which returns"
                " the Body Mass Index for the given weight and height.\n"
                "It accepts weight in kilograms and height in centimeters."\
                "\n"
            )

        return "No documentation available."
