"""Agent responsible for code quality assurance."""


class CodeReviewAgent:
    """Simple static checks on generated code."""

    def run(self, code: str) -> dict:
        """Return approval status and list of issues found."""

        issues = []
        if not code.strip():
            issues.append("Empty code generated")

        if "def calculate_bmi" not in code:
            issues.append("calculate_bmi function missing")

        approved = len(issues) == 0
        return {"approved": approved, "issues": issues}
