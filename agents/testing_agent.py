"""Agent that produces unit tests for generated code."""


class TestCaseAgent:
    """Generate Python unit tests."""

    def run(self, code: str) -> str:
        """Return a string containing unit tests."""

        if "calculate_bmi" in code:
            return (
                "import unittest\n\n"
                "from generated_code import calculate_bmi\n\n"
                "class TestBMI(unittest.TestCase):\n"
                "    def test_positive(self):\n"
                "        self.assertAlmostEqual(calculate_bmi(70, 175), 22.86, places=2)\n\n"
                "if __name__ == '__main__':\n"
                "    unittest.main()\n"
            )

        return ""
