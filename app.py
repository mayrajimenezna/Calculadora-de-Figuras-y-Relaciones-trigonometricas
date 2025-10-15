import streamlit as st
import math
st.balloons()
st.snow()
st.title("Calculadora de Figuras y Relaciones Trigonometricas")
st.image("https://www.google.com/search?sca_esv=df783cd413716f53&rlz=1C1SLLM_enMX1173MX1173&udm=2&fbs=AIIjpHx4nJjfGojPVHhEACUHPiMQht6_BFq6vBIoFFRK7qchKG1cRgcE0P7z3SNizmlu0QnAo31FcWSm9PsQnW8mPH21fKIudaD3R16fQoIwc62HTyRj27qBoUIERDy8P489-vZVHT3YgfUdKrHQzpOtOnKZzzeaiXgW-F8WVpZ8bbTvWPgZLzdm-07U-UwGgRxm2ySqyjNatAOlKqcjic1pVX_CyDc9Pw&q=triangulo&sa=X&ved=2ahUKEwirva-BvKaQAxXcLEQIHQy6JosQtKgLegQIJxAB&biw=1920&bih=953&dpr=1#vhid=EWqZBKuQj-atGM&vssid=mosaic")


# Widget para ingresar el radio
radio = st.slider ("Selecciona el radio", 0.0, 10.0, 5.0)
# Calculo del área
area = math.pi * radio**2
# Mostrar resultado
st.write (f"El área del círculo con radio {radio} es: {area: .2f}")
# Calculo del perimetro
perimetro = math.pi *2 * radio
st.write (f"El perímetro del círculo es: {perimetro}")
