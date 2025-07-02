# Multi-Agentic Framework Documentation

## Agents
- **RequirementAnalysisAgent**: parses natural language input into structured requirements.
- **CodingAgent**: generates Python code from the structured requirements.
- **CodeReviewAgent**: performs static checks and approves or returns issues.
- **DocumentationAgent**: creates markdown documentation for the generated code.
- **TestCaseAgent**: produces unit tests.
- **DeploymentAgent**: outputs a simple deployment script.
- **StreamlitUIAgent**: builds a Streamlit interface.

## Workflow
1. The Orchestrator sends the user's requirement to the RequirementAnalysisAgent.
2. The CodingAgent produces code based on the structured requirements.
3. CodeReviewAgent validates the code and may trigger regeneration.
4. Documentation, tests, deployment script and UI are produced.

## Running
Use `python main.py "Create a BMI calculator"` to run the pipeline or `streamlit run streamlit_app/app.py` for a UI.
