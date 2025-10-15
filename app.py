import streamlit as st
import math
st.balloons()
st.snow()
st.title("Calculadora de Figuras y Relaciones Trigonometricas")
# Widget para ingresar el radio
radio = st.slider ("Selecciona el radio", 0.0, 10.0, 5.0)
# Calculo del área
area = math.pi * radio**2
# Mostrar resultado
st.write (f"El área del círculo con radio {radio} es: {area: .2f}")
# Calculo del perimetro
perimetro = math.pi *2 * radio
st.write (f"El perímetro del círculo es: {perimetro}")
