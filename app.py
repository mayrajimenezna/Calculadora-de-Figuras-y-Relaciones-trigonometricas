import streamlit as st
import math
st.balloons()
st.snow()
st.title("Calculadora de Figuras y Relaciones Trigonometricas")
st.image("https://www.google.com/search?q=figura+circulo&sca_esv=df783cd413716f53&rlz=1C1SLLM_enMX1173MX1173&udm=2&biw=1920&bih=953&ei=OrjvaJxiu9WQ8g--9KPJBA&ved=0ahUKEwic58ymvaaQAxW7KkQIHT76KEkQ4dUDCBE&uact=5&oq=figura+circulo&gs_lp=Egtnd3Mtd2l6LWltZyIOZmlndXJhIGNpcmN1bG8yBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBBAAGB4yBBAAGB4yBBAAGB4yBBAAGB5IiRlQ6QlYsRZwAngAkAEAmAGgAaAB6QiqAQMwLji4AQPIAQD4AQGYAgmgArcIwgIKEAAYgAQYQxiKBcICBhAAGAcYHpgDAIgGAZIHAzIuN6AHvyqyBwMwLje4B6gIwgcFMi01LjTIB0w&sclient=gws-wiz-img#vhid=EZWe-cszj17KAM&vssid=mosaic")


# Widget para ingresar el radio
radio = st.slider ("Selecciona el radio", 0.0, 10.0, 5.0)
# Calculo del área
area = math.pi * radio**2
# Mostrar resultado
st.write (f"El área del círculo con radio {radio} es: {area: .2f}")
# Calculo del perimetro
perimetro = math.pi *2 * radio
st.write (f"El perímetro del círculo es: {perimetro}")


# Widget para ingresar la base
