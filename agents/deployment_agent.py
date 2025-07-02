"""Agent for generating deployment scripts."""


class DeploymentAgent:
    """Produce a simple bash script to run the project."""

    def run(self) -> str:
        """Return a bash script string.

        The script sets up a virtual environment, installs dependencies and
        executes the main entry point. It can be used for simple deployments or
        CI pipelines.
        """

        return (
            "#!/bin/bash\n"
            "python -m venv .venv\n"
            "source .venv/bin/activate\n"
            "pip install -r requirements.txt\n"
            "python main.py \"$@\"\n"
        )
