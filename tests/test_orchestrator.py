import unittest
from pathlib import Path

from core.orchestrator import Orchestrator

class OrchestratorTest(unittest.TestCase):
    def test_run(self):
        orch = Orchestrator()
        result = orch.run("Create a BMI calculator")
        self.assertIn("calculate_bmi", result["code"])
        self.assertTrue(result["deploy_script"].startswith("#!/bin/bash"))
        self.assertTrue(Path("generated/code/generated_code.py").exists())


if __name__ == "__main__":
    unittest.main()
