import streamlit as st
from generated_code import calculate_bmi

st.title('BMI Calculator')
weight = st.number_input('Weight (kg)', 0.0)
height = st.number_input('Height (cm)', 0.0)
if st.button('Compute BMI'):
    bmi = calculate_bmi(weight, height)
    st.write(f'BMI: {bmi:.2f}')
