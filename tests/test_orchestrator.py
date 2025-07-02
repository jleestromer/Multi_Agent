import unittest

from core.orchestrator import Orchestrator

class OrchestratorTest(unittest.TestCase):
    def test_run(self):
        orch = Orchestrator()
        result = orch.run("Create a BMI calculator")
        self.assertIn("calculate_bmi", result["code"])
        self.assertTrue(result["deploy_script"].startswith("#!/bin/bash"))


if __name__ == "__main__":
    unittest.main()
