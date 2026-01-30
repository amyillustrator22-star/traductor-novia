#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 30 00:55:56 2026

@author: amy
"""

import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Traductor Argento", page_icon="🧉")

# 1. Configuración de la llave
if "api_key" in st.secrets:
    # Limpiamos la clave por si acaso
    key = st.secrets["api_key"].strip().replace('"', '').replace("'", "")
    genai.configure(api_key=key)
else:
    st.error("Falta la clave en Secrets")

# 2. Función con el nombre de modelo que NO falla
def traducir(texto):
    try:
        # Usamos el nombre que la API v1beta reconoce oficialmente
        model = genai.GenerativeModel('models/gemini-1.5-flash-latest')
        
        prompt = f"Traduce de argentino a español de España: {texto}. Sé gracioso."
        res = model.generate_content(prompt)
        return res.text
    except Exception as e:
        # Si falla el anterior, probamos el nombre básico
        try:
            model = genai.GenerativeModel('gemini-1.5-flash')
            res = model.generate_content(prompt)
            return res.text
        except Exception as e2:
            return f"Error de modelo: {e2}"

# 3. Interfaz
st.title("Traductor Argento 🧉")
frase = st.text_input("Dime qué te ha dicho:")

if st.button("Descifrar"):
    if frase:
        with st.spinner('Traduciendo...'):
            st.write(traducir(frase)) 
