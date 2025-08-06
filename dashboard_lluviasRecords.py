# -*- coding: utf-8 -*-
"""
Created on Wed Aug  6 09:26:15 2025

@author: dpoleo
"""
import streamlit as st
import os

st.set_page_config(page_title="Mapas de Récords de Lluvias Mensuales", layout="wide")

st.title("Mapas de Récords de Lluvias Mensuales")
st.write("Haz clic en cada pestaña para ver el mapa correspondiente al mes")

# Ruta RELATIVA (no cambies esto)
ruta = "Lluvia"

mapas = [
    "PCP_01_Enero_Records.jpg",
    "PCP_01_febrero_Records.jpg",
    "PCP_01_Marzo_Records.jpg",
    "PCP_04_Abril_Records.jpg",
    "PCP_05_Mayo_Records.jpg",
    "PCP_06_Junio_Records.jpg",
    "PCP_07_Julio_Records.jpg",
    "PCP_08_Agosto_Records.jpg",
    "PCP_09_Septiembre_Records.jpg",
    "PCP_10_Octubre_Records.jpg",
    "PCP_11_Noviembre_Records.jpg",
    "PCP_12_Diciembre_Records.jpg"
]

titulos = [
    "Enero (Versión 1)",
    "Enero (Versión 2)",
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

tabs = st.tabs(titulos)

for i, tab in enumerate(tabs):
    with tab:
        img_path = os.path.join(ruta, mapas[i])
        if os.path.exists(img_path):
            st.image(img_path, caption=titulos[i])
        else:
            st.warning(f"No se encontró la imagen: {mapas[i]}")



