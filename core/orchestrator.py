"""Simple orchestration logic linking all agents together."""

from agents.requirement_agent import RequirementAnalysisAgent
from agents.coding_agent import CodingAgent
from agents.review_agent import CodeReviewAgent
from agents.documentation_agent import DocumentationAgent
from agents.testing_agent import TestCaseAgent
from agents.deployment_agent import DeploymentAgent
from agents.ui_agent import StreamlitUIAgent
from core.utils import write_file


class Orchestrator:
    """Coordinates the multi-agent workflow."""

    def __init__(self) -> None:
        self.requirement_agent = RequirementAnalysisAgent()
        self.coding_agent = CodingAgent()
        self.review_agent = CodeReviewAgent()
        self.documentation_agent = DocumentationAgent()
        self.testing_agent = TestCaseAgent()
        self.deployment_agent = DeploymentAgent()
        self.ui_agent = StreamlitUIAgent()

    def run(self, user_input: str) -> dict:
        """Execute the agents sequentially until review passes."""

        requirements = self.requirement_agent.run(user_input)

        while True:
            code = self.coding_agent.run(requirements)
            review = self.review_agent.run(code)
            if review["approved"]:
                break
            # In a real system, feedback would influence regeneration
            requirements["feedback"] = review["issues"]

        documentation = self.documentation_agent.run(code)
        tests = self.testing_agent.run(code)
        deploy_script = self.deployment_agent.run()
        ui = self.ui_agent.run()

        # Write artifacts to disk
        write_file("generated/code/generated_code.py", code)
        write_file("generated/tests/test_generated.py", tests)
        write_file("generated/docs/documentation.md", documentation)
        write_file("generated/deployment/deploy.sh", deploy_script)
        write_file("generated/code/ui.py", ui)

        return {
            "requirements": requirements,
            "code": code,
            "documentation": documentation,
            "tests": tests,
            "deploy_script": deploy_script,
            "ui": ui,
        }
