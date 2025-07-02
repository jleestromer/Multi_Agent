"""Agent that generates a simple Streamlit UI."""


class StreamlitUIAgent:
    """Create Streamlit code for interacting with the generated module."""

    def run(self) -> str:
        """Return a Streamlit app as a string."""

        return (
            "import streamlit as st\n"
            "from generated_code import calculate_bmi\n\n"
            "st.title('BMI Calculator')\n"
            "weight = st.number_input('Weight (kg)', 0.0)\n"
            "height = st.number_input('Height (cm)', 0.0)\n"
            "if st.button('Compute BMI'):\n"
            "    bmi = calculate_bmi(weight, height)\n"
            "    st.write(f'BMI: {bmi:.2f}')\n"
        )
