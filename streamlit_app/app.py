"""Streamlit entry point for the multi-agent framework."""

import streamlit as st

from core.orchestrator import Orchestrator


def main() -> None:
    st.title("Multi-Agent BMI Calculator")
    user_req = st.text_area("Requirement", "Create a BMI calculator")

    if st.button("Run Agents"):
        orchestrator = Orchestrator()
        result = orchestrator.run(user_req)
        st.subheader("Generated Code")
        st.code(result["code"], language="python")
        st.subheader("Documentation")
        st.markdown(result["documentation"])


if __name__ == "__main__":
    main()
