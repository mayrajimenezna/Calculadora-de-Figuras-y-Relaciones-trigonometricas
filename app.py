import streamlit as st
import math
st.balloons()
st.snow()
st.title("Calculadora de Figuras y Relaciones Trigonometricas")
st.sidebar.header("Mayra Mariel Jimenez Navarrete 385869")
st.image("circulo.jpg")


# Widget para ingresar el radio
radio = st.slider ("Selecciona el radio", 0.0, 10.0, 5.0)
# Calculo del área
area = math.pi * radio**2
# Mostrar resultado
st.write (f"El área del círculo con radio {radio} es: {area: .2f}")
# Calculo del perimetro
perimetro = math.pi *2 * radio
st.write (f"El perímetro del círculo es: {perimetro}")

st.image("triangulo.jpg")
# Widget para ingresar la base del triangulo
a = st.slider ("Selecciona el lado 1", 0.0, 10.0, 5.0)
b = st.slider ("Selecciona el lado 2", 0.0, 10.0, 5.0)
c = st.slider ("Selecciona el lado 3", 0.0, 10.0, 5.0)
# Calculo del área
import math
s = (a + b + c) / 2
area1 = math.sqrt(s * (s - a) * (s - b) * (s - c))
# Mostrar resultado
st. write (f"El área del tríángulo es: {area1: .2f}")
# Calculo del perimetro
perimetro1 = a + b + c
st.write (f"El perímetro del triángulo es: {perimetro1}")
