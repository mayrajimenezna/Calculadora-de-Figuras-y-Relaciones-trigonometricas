import streamlit as st
import math
st.balloons()
st.snow()
st.title("Mi aplicación: 🖩 Calculadora del Área de un Círculo ⭕")
# Widget para ingresar el radio
radio = st.slider ("Selecciona el radio", 0.0, 10.0, 5.0)
# Calculo del área
area = math.pi * radio**2
# Mostrar resultado
st.write (f"El área del círculo con radio {radio} es: {area: .2f}")
