# -*- coding: utf-8 -*-
"""
Created on Wed Aug  6 09:26:15 2025

@author: Daniel Poleo
"""
import streamlit as st
import os

st.set_page_config(page_title="Mapas Climáticos Mensuales", layout="wide")

st.title("Mapas Climáticos Mensuales")
st.write("Haz clic en cada pestaña para ver los mapas correspondientes a los récords de cada variable y mes.")

# Nombres y rutas de las variables
variables = {
    "Lluvia": "Lluvia",
    "Viento": "Viento",
    "Temperatura Máxima": "Tmax",
    "Temperatura Mínima": "Tmin",
    "Composite": "Composite"
}

# Archivos y títulos por mes
mapas = [
    "01_Enero_Records.jpg",
    "02_Febrero_Records.jpg",
    "03_Marzo_Records.jpg",
    "04_Abril_Records.jpg",
    "05_Mayo_Records.jpg",
    "06_Junio_Records.jpg",
    "07_Julio_Records.jpg",
    "08_Agosto_Records.jpg",
    "09_Septiembre_Records.jpg",
    "10_Octubre_Records.jpg",
    "11_Noviembre_Records.jpg",
    "12_Diciembre_Records.jpg"
]

titulos = [
    "Enero",
    "Febrero",
    "Marzo",
    "Abril",
    "Mayo",
    "Junio",
    "Julio",
    "Agosto",
    "Septiembre",
    "Octubre",
    "Noviembre",
    "Diciembre"
]

# Pestañas principales (una por variable)
tab_var = st.tabs(list(variables.keys()))

for v, tab in zip(variables.keys(), tab_var):
    with tab:
        st.subheader(f"Récords Mensuales de {v}")
        ruta = variables[v]
        tabs_mes = st.tabs(titulos)
        for i, tab_mes in enumerate(tabs_mes):
            with tab_mes:
                # Nombre de imagen por convención: Carpeta/PCP_01_Enero_Records.jpg, etc.
                # Si tienes diferentes prefijos por variable, ajusta aquí
                if v == "Lluvia":
                    img_name = f"PCP_{mapas[i]}"
                elif v == "Viento":
                    img_name = f"VNT_{mapas[i]}"
                elif v == "Temperatura Máxima":
                    img_name = f"TMAX_{mapas[i]}"
                elif v == "Temperatura Mínima":
                    img_name = f"TMIN_{mapas[i]}"
                elif v == "Composite":
                    img_name = f"CMP_{mapas[i]}"
                else:
                    img_name = mapas[i]  # fallback

                img_path = os.path.join(ruta, img_name)
                if os.path.exists(img_path):
                    st.image(img_path, caption=f"{v} - {titulos[i]}")
                else:
                    st.warning(f"No se encontró la imagen: {img_name}")


