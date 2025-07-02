import unittest
from pathlib import Path

from core.orchestrator import Orchestrator
from core.llm import LLMClient


class FailingLLM(LLMClient):
    """LLM client used for testing iterative improvement."""

    def __init__(self):
        super().__init__()
        self.calls = 0

    def generate(self, prompt: str) -> str:
        self.calls += 1
        if self.calls == 1:
            # First attempt returns incomplete code that fails review
            return "def foo():\n    pass"
        return super().generate(prompt)

class OrchestratorTest(unittest.TestCase):
    def test_run(self):
        orch = Orchestrator()
        result = orch.run("Create a BMI calculator")
        self.assertIn("calculate_bmi", result["code"])
        self.assertTrue(result["deploy_script"].startswith("#!/bin/bash"))
        self.assertTrue(Path("generated/code/generated_code.py").exists())

    def test_iteration_on_review_failure(self):
        llm = FailingLLM()
        orch = Orchestrator(llm=llm)
        result = orch.run("Create a BMI calculator")
        self.assertGreaterEqual(result["attempts"], 2)
        self.assertIn("calculate_bmi", result["code"])


if __name__ == "__main__":
    unittest.main()
