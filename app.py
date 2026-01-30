#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 30 00:55:56 2026

@author: amy
"""

import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Traductor Argento")

# Intentamos cargar la clave de los Secrets
if "api_key" in st.secrets:
    actual_key = st.secrets["api_key"]
    # Limpiamos la clave por si tiene espacios o comillas extra
    actual_key = actual_key.strip().replace('"', '').replace("'", "")
    genai.configure(api_key=actual_key)
else:
    st.error("No hay clave en Secrets")

def traducir(texto):
    # Intentamos con el modelo más común
    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
        res = model.generate_content(f"Traduce esto de argentina a españa: {texto}")
        return res.text
    except Exception as e:
        return f"Error de conexión: {e}"

st.title("Traductor Argento 🧉")
frase = st.text_input("Escribe aquí:")

if st.button("Traducir"):
    if frase:
        resultado = traducir(frase)
        st.write(resultado) 
