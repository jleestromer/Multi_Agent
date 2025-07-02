import unittest

from agents.requirement_agent import RequirementAnalysisAgent
from agents.coding_agent import CodingAgent
from agents.review_agent import CodeReviewAgent
from agents.testing_agent import TestCaseAgent
from agents.deployment_agent import DeploymentAgent
from agents.ui_agent import StreamlitUIAgent
from core.llm import LLMClient


class AgentTests(unittest.TestCase):
    def test_requirement_agent(self):
        agent = RequirementAnalysisAgent()
        res = agent.run("Create a BMI calculator")
        self.assertIn("title", res)

    def test_coding_agent(self):
        code = CodingAgent().run({"title": "BMI Calculator"})
        self.assertIn("def calculate_bmi", code)

    def test_review_agent(self):
        review = CodeReviewAgent().run("def calculate_bmi(x,y): return 0")
        self.assertTrue(review["approved"])

    def test_testing_agent(self):
        tests = TestCaseAgent().run("def calculate_bmi(x,y): return 0")
        self.assertIn("unittest", tests)

    def test_deployment_agent(self):
        script = DeploymentAgent().run()
        self.assertTrue(script.startswith("#!/bin/bash"))
        self.assertIn("pip install -r requirements.txt", script)

    def test_ui_agent(self):
        ui = StreamlitUIAgent().run()
        self.assertIn("streamlit", ui)

    def test_llm_fallback(self):
        llm = LLMClient()
        output = llm.generate("Write a BMI calculator")
        self.assertIn("calculate_bmi", output)


if __name__ == "__main__":
    unittest.main()
