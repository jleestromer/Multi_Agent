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
