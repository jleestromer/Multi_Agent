# Multi-Agentic Coding Framework

This project demonstrates a simple multi-agent workflow implemented in Python.
Agents collaborate to turn a natural language requirement into runnable code,
documentation, tests, a deployment script and a Streamlit UI.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Running

Execute the orchestrator directly:

```bash
python main.py "Create a BMI calculator"
```

Launch the Streamlit interface:

```bash
streamlit run streamlit_app/app.py
```

Run the automated tests:

```bash
pytest -q
```

You can also use the generated deployment script after running the agents:

```bash
bash generated/deployment/deploy.sh "Create a BMI calculator"
```

Generated artifacts will be saved in the `generated/` directory after running
the orchestrator. To enable LLM-powered code generation, set the environment
variable `OPENAI_API_KEY` with your OpenAI credentials. Without the key, the
system falls back to deterministic example output useful for testing.
