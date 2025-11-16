import streamlit as st
import joblib
import numpy as np
#import os


# -----------------------------
# Cargar modelo entrenado
# -----------------------------
# solo funciona para ver desde consola
#modelo = joblib.load(r"C:\Users\kleve\Downloads\proyecto\modelo_regresion.pkl")
#para lo publico ponemos en github
modelo = joblib.load("modelo_regresion.pkl")

#modelo = joblib.load("modelo_regresion.pkl")

st.title("Predicción del Valor de Casa 🏡")
st.write("Ingresa los datos y el modelo regresión lineal predecirá el valor de la vivienda.")

# ----------------------------------
# Crear entradas para cada variable
# ----------------------------------

Ingreso = st.number_input("Ingreso promedio en cuadra ", min_value=0.0, value=10000.0)
EdadCasa = st.number_input(
    "Edad de la casa (HouseAge)",
    min_value=0.0,
    max_value=51.0,      
    value=20.0,
    step=1.0
)
Habita = st.number_input("habitaciones tienen en promedio las viviendas del área ", min_value=0.0, value=5.0)
Dormi = st.number_input("Dormitorios promedio ", min_value=0.0, value=1.0)
Pobla = st.number_input("Población del área en la cuadra o bloque ", min_value=0.0, value=1500.0)
Ocup = st.number_input("Promedio de ocupantes por casa ", min_value=0.0, value=3.0)
Lati = st.number_input("Latitud", value=34.0)
Long = st.number_input("Longitud", value=-118.0)

# Crear un array con los valores en el mismo orden que usaste en X
valores = np.array([[Ingreso, EdadCasa, Habita, Dormi, Pobla, Ocup, Lati, Long]])

# -----------------------------
# Botón para predecir
# -----------------------------
if st.button("Predecir Valor de Casa"):
    pred = modelo.predict(valores)[0]
    st.success(f"El valor estimado de la casa es: **${pred:,.2f} USD**")




# Run the app with:
# Step 1: Open your terminal
# Step 2: Install Streamlit if you haven't already:
#    pip install streamlit
# Step 3: Navigate to the directory containing this app.py file
# Step 4: Run the app with the command:
# streamlit run r"C:\Users\kleve\Downloads\proyecto\app.py"