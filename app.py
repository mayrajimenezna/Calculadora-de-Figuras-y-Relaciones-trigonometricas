import streamlit as st
import math
st.balloons()
st.snow()
st.title("Calculadora de Figuras y Relaciones Trigonometricas")
st.image("https://www.google.com/search?sca_esv=df783cd413716f53&rlz=1C1SLLM_enMX1173MX1173&q=figura+triangulo&uds=AOm0WdE2fekQnsyfYEw8JPYozOKzrviPc2SkCy_EbmLwj3UWfI9lr2Dlj2AFsns6Hlc7uwoepRUWi7ulyv-wiUMKW8UUfsmffB8cyfZcjxte-YbXmu5VA66Q2VO56MbGkzlk__5qMhzDabe2o9lsHyCDtiHvK8TAEg&udm=2&sa=X&ved=2ahUKEwisz86CvKaQAxVuNEQIHcAmGIUQxKsJKAF6BAgUEAE&ictx=0&biw=1920&bih=953&dpr=1#vhid=Avr4a2nQbbf_9M&vssid=mosaic")


# Widget para ingresar el radio
radio = st.slider ("Selecciona el radio", 0.0, 10.0, 5.0)
# Calculo del área
area = math.pi * radio**2
# Mostrar resultado
st.write (f"El área del círculo con radio {radio} es: {area: .2f}")
# Calculo del perimetro
perimetro = math.pi *2 * radio
st.write (f"El perímetro del círculo es: {perimetro}")
