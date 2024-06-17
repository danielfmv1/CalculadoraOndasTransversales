#import streamlit.web.cli as stcli
import streamlit as st

import numpy as np
import matplotlib.pyplot as plt

# Título de la aplicación
st.title("Generador de Onda Transversal")

# Solicitar datos al usuario
amplitud = st.number_input("Ingrese la amplitud de la onda", min_value=0.0, step=0.1)
velocidad = st.number_input("Ingrese la velocidad de la onda (m/s)", min_value=0.0, step=0.1)
frecuencia = st.number_input("Ingrese la frecuencia de la onda (Hz)", min_value=0.0, step=0.1)

if amplitud > 0 and velocidad > 0 and frecuencia > 0:
    # Calcular la longitud de onda
    longitud_de_onda = velocidad / frecuencia
    st.write(f"Longitud de onda: {longitud_de_onda} metros")

    # Calcular el periodo de la onda
    periodo = 1 / frecuencia
    st.write(f"Periodo: {periodo} segundos")

    # Calcular la frecuencia
    frecuencia_calculada = velocidad / longitud_de_onda
    st.write(f"Frecuencia calculada: {frecuencia_calculada} Hz")

    # Crear el espacio para x
    x = np.linspace(0, 4 * longitud_de_onda, 1000)

    # Definir la función de la onda transversal
    def onda_transversal(x, t):
        return amplitud * np.sin(2 * np.pi * (x / longitud_de_onda - velocidad * t / longitud_de_onda))

    # Generar la gráfica de la onda en un tiempo específico
    tiempo = 0.0  # ver la onda en diferentes tiempos
    y = onda_transversal(x, tiempo)

    # Crear la figura
    fig, ax = plt.subplots()
    ax.plot(x, y, label=f't = {tiempo:.2f} s')
    ax.set_title('Onda Transversal')
    ax.set_xlabel('Posición (x) [m]')
    ax.set_ylabel('Desplazamiento (y) [m]')
    ax.legend()
    ax.grid(True)

    # Mostrar la gráfica
    st.pyplot(fig)
else:
    st.write("Por favor, ingrese valores válidos para amplitud, velocidad y frecuencia.")
