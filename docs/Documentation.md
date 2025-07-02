# Multi-Agentic Framework Documentation

## Agents
- **RequirementAnalysisAgent**: parses natural language input into structured requirements.
- **CodingAgent**: generates Python code from the structured requirements.
- **CodeReviewAgent**: performs static checks and approves or returns issues.
- **DocumentationAgent**: creates markdown documentation for the generated code.
- **TestCaseAgent**: produces unit tests.
- **DeploymentAgent**: outputs a simple deployment script.
- **StreamlitUIAgent**: builds a Streamlit interface.

Each agent focuses on a single responsibility which keeps the implementation
modular and easy to extend.

## Workflow
1. The Orchestrator sends the user's requirement to the RequirementAnalysisAgent.
2. The CodingAgent produces code based on the structured requirements.
3. CodeReviewAgent validates the code and may trigger regeneration.
4. Documentation, tests, deployment script and UI are produced.

The Orchestrator continues looping between the CodingAgent and CodeReviewAgent
until the generated code passes the review stage. Feedback from the reviewer is
passed back to the coding agent so it can refine the output.

## Running
Use `python main.py "Create a BMI calculator"` to run the pipeline or
`streamlit run streamlit_app/app.py` for an interactive UI. Artifacts are saved
under the `generated/` directory.

## Testing
Run `pytest -q` to execute the unit tests. A successful run should output
something similar to:

```
$ pytest -q
..........  [100%]
10 passed in <time>
```
