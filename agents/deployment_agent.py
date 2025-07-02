"""Agent for generating deployment scripts."""


class DeploymentAgent:
    """Produce a simple bash script to run the project."""

    def run(self) -> str:
        """Return a bash script string."""

        return "#!/bin/bash\npython main.py"
