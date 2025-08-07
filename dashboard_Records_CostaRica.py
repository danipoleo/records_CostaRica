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

# Definir pestañas principales y su estructura de archivos
variables = {
    "Lluvia": {
        "carpeta": "Lluvia",
        "archivos": [f"PCP_{str(i).zfill(2)}_{mes}_Records.jpg" for i, mes in enumerate(
            ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"], 1)],
        "titulos": ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    },
    "Ráfagas": {
        "carpeta": "Ráfagas",
        "archivos": [f"VVmax_{str(i).zfill(2)}{mes}.jpeg" for i, mes in enumerate(
            ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"], 1)],
        "titulos": ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    },
    "Temperatura Máxima": {
        "carpeta": "Temperatura Máxima",
        "archivos": [f"Record_Tmax_{str(i).zfill(2)}_{mes}.jpg" for i, mes in enumerate(
            ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"], 1)],
        "titulos": ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    },
    "Temperatura Mínima": {
        "carpeta": "Temperatura Mínima",
        "archivos": [f"{str(i).zfill(2)}_Record_Tmin_{mes}.jpg" for i, mes in enumerate(
            ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"], 1)],
        "titulos": ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    },
    "Composite": {
        "carpeta": "Composites Anual",
        "archivos": [
            "Records_lluvia_meses.jpg",
            "Tmax.jpg",
            "VVmax.jpg",
            "Tmin.jpg"
        ],
        "titulos": [
            "Lluvia Anual",
            "Temperatura Máxima Anual",
            "Ráfagas Anual",
            "Temperatura Mínima Anual"
        ]
    }
}

# Crear pestañas principales
tabs_principales = st.tabs(list(variables.keys()))

for nombre_var, tab in zip(variables.keys(), tabs_principales):
    with tab:
        st.subheader(f"Mapas de {nombre_var}")
        carpeta = variables[nombre_var]["carpeta"]
        archivos = variables[nombre_var]["archivos"]
        titulos = variables[nombre_var]["titulos"]

        # Si hay varios meses (subpestañas)
        if len(archivos) > 1:
            tabs_meses = st.tabs(titulos)
            for i, tab_mes in enumerate(tabs_meses):
                with tab_mes:
                    img_path = os.path.join(carpeta, archivos[i])
                    if os.path.exists(img_path):
                        st.image(img_path, caption=f"{nombre_var} - {titulos[i]}")
                    else:
                        st.warning(f"No se encontró la imagen: {archivos[i]}")
        else:
            # Solo hay un archivo
            img_path = os.path.join(carpeta, archivos[0])
            if os.path.exists(img_path):
                st.image(img_path, caption=titulos[0])
            else:
                st.warning(f"No se encontró la imagen: {archivos[0]}")


