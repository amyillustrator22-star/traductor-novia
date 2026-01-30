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
    key = st.secrets["api_key"].strip().replace('"', '').replace("'", "")
    genai.configure(api_key=key)
else:
    st.error("Falta la clave en Secrets")

# 2. Función con "Supervivencia" (Prueba varios nombres)
def traducir(texto):
    # Lista de nombres que Google acepta según la versión
    nombres_modelos = [
        'gemini-1.5-flash-latest', 
        'models/gemini-1.5-flash', 
        'gemini-1.5-pro'
    ]
    
    for nombre in nombres_modelos:
        try:
            model = genai.GenerativeModel(nombre)
            prompt = f"Traduce de argentino a español de España: {texto}. Sé gracioso y breve."
            res = model.generate_content(prompt)
            return res.text
        except Exception:
            continue # Si falla este nombre, intenta el siguiente
            
    return "❌ Error: Google no acepta ninguno de los nombres de modelo. Revisa tu API Key."

# 3. Interfaz
st.title("Traductor Argento 🧉")
frase = st.text_input("Escribe lo que te dijo:")

if st.button("Descifrar"):
    if frase:
        with st.spinner('Buscando significado...'):
            resultado = traducir(frase)
            st.success(resultado) 
