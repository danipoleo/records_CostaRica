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

# -----------------------------------------
# Utilidades
# -----------------------------------------
# Meses: número (dos dígitos), nombre_lower (para URLs distritales), nombre_title (para UI)
_MESES = [
    ("01", "enero", "Enero"),
    ("02", "febrero", "Febrero"),
    ("03", "marzo", "Marzo"),
    ("04", "abril", "Abril"),
    ("05", "mayo", "Mayo"),
    ("06", "junio", "Junio"),
    ("07", "julio", "Julio"),
    ("08", "agosto", "Agosto"),
    ("09", "septiembre", "Septiembre"),
    ("10", "octubre", "Octubre"),
    ("11", "noviembre", "Noviembre"),
    ("12", "diciembre", "Diciembre"),
]

# -----------------------------------------
# Pestañas principales existentes
# -----------------------------------------
variables = {
    "Lluvia": {
        "carpeta": "Lluvia",
        "archivos": [f"PCP_{str(i).zfill(2)}_{mes}_Records.jpg" for i, mes in enumerate(
            [m[2] for m in _MESES], 1)],
        "titulos": [m[2] for m in _MESES],
    },
    "Ráfagas": {
        "carpeta": "Ráfagas",
        "archivos": [f"VVmax_{str(i).zfill(2)}{mes}.jpeg" for i, mes in enumerate(
            [m[2] for m in _MESES], 1)],
        "titulos": [m[2] for m in _MESES],
    },
    "Temperatura Máxima": {
        "carpeta": "Temperatura Máxima",
        "archivos": [f"Record_Tmax_{str(i).zfill(2)}_{mes}_corregido.jpg" for i, mes in enumerate(
            [m[2] for m in _MESES], 1)],
        "titulos": [m[2] for m in _MESES],
    },
    "Temperatura Mínima": {
        "carpeta": "Temperatura Mínima",
        "archivos": [f"{str(i).zfill(2)}_Record_Tmin_{mes}.jpg" for i, mes in enumerate(
            [m[2] for m in _MESES], 1)],
        "titulos": [m[2] for m in _MESES],
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

# -----------------------------------------
# NUEVA PESTAÑA: Distritales (carga desde GitHub raw)
# -----------------------------------------
def construir_url_distrital(variable: str, num: str, mes_lower: str) -> str:
    """
    Construye la URL RAW de GitHub para la imagen distrital según variable, número de mes y nombre de mes en minúscula.
    Usa exactamente las rutas de ejemplo compartidas (incluyendo la carpeta 'R%C3%A1gafas').
    """
    base = "https://raw.githubusercontent.com/danipoleo/records_CostaRica/main/distritales"

    if variable == "Ráfagas":
        # Ejemplo dado: .../distritales/R%C3%A1gafas/VVmax01_enero.jpg
        carpeta = "R%C3%A1gafas"
        filename = f"VVmax{num}_{mes_lower}.jpg"
    elif variable == "Lluvia":
        # Ejemplo dado: .../distritales/lluvia/PCP01_enero.jpg
        carpeta = "lluvia"
        filename = f"PCP{num}_{mes_lower}.jpg"
    elif variable == "Temperatura Máxima":
        # Ejemplo dado: .../distritales/Temperatura_Maxima/Tmax01_enero.jpg
        carpeta = "Temperatura_Maxima"
        filename = f"Tmax{num}_{mes_lower}.jpg"
    elif variable == "Temperatura Mínima":
        # Ejemplo dado: .../distritales/Temperatura_Minima/Tmin01_enero.jpg
        carpeta = "Temperatura_Minima"
        filename = f"Tmin{num}_{mes_lower}.jpg"
    else:
        return ""

    return f"{base}/{carpeta}/{filename}"

# Inserta la nueva pestaña "Distritales" al inicio
variables_con_distritales = {"Distritales": {}} | variables

tabs_principales = st.tabs(list(variables_con_distritales.keys()))

for nombre_var, tab in zip(variables_con_distritales.keys(), tabs_principales):
    with tab:
        if nombre_var != "Distritales":
            # -----------------------------
            # Comportamiento original
            # -----------------------------
            st.subheader(f"Mapas de {nombre_var}")
            carpeta = variables[nombre_var]["carpeta"]
            archivos = variables[nombre_var]["archivos"]
            titulos = variables[nombre_var]["titulos"]

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
                img_path = os.path.join(carpeta, archivos[0])
                if os.path.exists(img_path):
                    st.image(img_path, caption=titulos[0])
                else:
                    st.warning(f"No se encontró la imagen: {archivos[0]}")

        else:
            # -----------------------------
            # NUEVA PESTAÑA "Distritales"
            # -----------------------------
            st.subheader("Mapas Distritales")
            st.caption("Las imágenes se cargan desde el repositorio de GitHub (rama main).")

            # Subpestañas por variable
            sub_tabs = st.tabs(["Ráfagas", "Lluvia", "Temperatura Máxima", "Temperatura Mínima"])

            for nombre_sub, sub_tab in zip(["Ráfagas", "Lluvia", "Temperatura Máxima", "Temperatura Mínima"], sub_tabs):
                with sub_tab:
                    st.write(f"**{nombre_sub}** · Selecciona el mes:")

                    # Selector de mes (muestra el nombre con mayúscula pero usa el código y minúscula para URL)
                    opciones_ui = [m[2] for m in _MESES]  # títulos
                    sel = st.selectbox("Mes", opciones_ui, key=f"sel_{nombre_sub}")
                    # Encuentra el tuple correspondiente
                    num, mes_lower, mes_title = next(m for m in _MESES if m[2] == sel)

                    url_img = construir_url_distrital(nombre_sub, num, mes_lower)

                    # Muestra la imagen y un enlace de respaldo
                    cols = st.columns([3, 1])
                    with cols[0]:
                        #st.image(url_img, caption=f"{nombre_sub} - {mes_title} (Distrital)", use_column_width=True)
                        st.image(url_img, caption=f"{nombre_sub} - {mes_title} (Distrital)", use_container_width=True)

                    with cols[1]:
                        st.markdown(f"[Abrir imagen en nueva pestaña]({url_img})")

                    st.divider()
                    st.caption(f"Fuente: {url_img}")

