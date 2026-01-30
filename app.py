#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 30 00:55:56 2026

@author: amy
"""

import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Traductor Argento", page_icon="🧉")
st.title("🇦🇷 Traductor Novia 🇪🇸")

# Cargamos la llave que ya sabemos que funciona
if "api_key" in st.secrets:
    llave = st.secrets["api_key"].strip().replace('"', '')
    genai.configure(api_key=llave)
else:
    st.error("Falta la clave en Secrets")

def traducir(texto):
    # Probamos los 3 nombres técnicos que acepta la v1beta actualmente
    nombres_tecnicos = [
        'models/gemini-1.5-flash-latest',
        'models/gemini-pro',
        'models/gemini-1.0-pro'
    ]
    
    for nombre in nombres_tecnicos:
        try:
            model = genai.GenerativeModel(nombre)
            res = model.generate_content(f"Traduce al español de España: {texto}")
            return res.text
        except Exception:
            continue # Si falla uno, salta al siguiente
            
    return "Google está actualizando sus modelos. Inténtalo en un minuto o revisa si tu API Key tiene permisos de 'Generative AI'."

frase = st.text_input("¿Qué te dijo?")
if st.button("Descifrar"):
    if frase:
        with st.spinner('Buscando el modelo correcto...'):
            resultado = traducir(frase)
            st.write(resultado)    
