"""Coding agent responsible for turning requirements into Python code."""

from core.llm import LLMClient


class CodingAgent:
    """Implementation that leverages an LLM to generate Python code."""

    def __init__(self, llm: LLMClient | None = None) -> None:
        self.llm = llm or LLMClient()

    def run(self, requirements: dict) -> str:
        """Generate Python code implementing the requested functionality.

        Any feedback from previous review cycles is appended to the prompt so
        the LLM can attempt to address the issues.
        """

        title = requirements.get("title", "")
        description = requirements.get("description", "")
        prompt = (
            f"Write a Python function that satisfies the following requirement:\n"
            f"Title: {title}\nDescription: {description}"
        )

        feedback = requirements.get("feedback")
        if feedback:
            prompt += f"\nPlease address the following review feedback: {feedback}"

        return self.llm.generate(prompt)
