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

    def __init__(self, llm=None) -> None:
        self.requirement_agent = RequirementAnalysisAgent()
        self.coding_agent = CodingAgent(llm)
        self.review_agent = CodeReviewAgent()
        self.documentation_agent = DocumentationAgent()
        self.testing_agent = TestCaseAgent()
        self.deployment_agent = DeploymentAgent()
        self.ui_agent = StreamlitUIAgent()

    def run(self, user_input: str) -> dict:
        """Execute the agents sequentially until the review agent approves.

        If the review fails, feedback is sent back to the coding agent and the
        generation process is repeated with the additional context.
        """

        requirements = self.requirement_agent.run(user_input)

        # Iterate until the review agent approves the generated code
        attempts = 0
        while True:
            attempts += 1
            code = self.coding_agent.run(requirements)
            review = self.review_agent.run(code)
            if review["approved"]:
                break
            # Feedback is fed back into the requirements for another iteration
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
            "attempts": attempts,
        }
