#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 30 00:55:56 2026

@author: amy
"""

import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Traductor Argento", page_icon="🧉")

# --- CONFIGURACIÓN DE SEGURIDAD ---
if "api_key" in st.secrets:
    # Limpiamos la clave de cualquier símbolo extraño
    key_limpia = st.secrets["api_key"].strip().replace('"', '').replace("'", "")
    genai.configure(api_key=key_limpia)
else:
    st.error("❌ La clave no está en los Secrets de Streamlit.")

def realizar_traduccion(frase):
    # Intentamos todos los nombres conocidos, del más nuevo al más compatible
    modelos = [
        'gemini-1.5-flash', 
        'models/gemini-1.5-flash', 
        'gemini-1.5-pro', 
        'gemini-pro'
    ]
    
    for nombre in modelos:
        try:
            model = genai.GenerativeModel(nombre)
            # El prompt más simple para probar conexión
            response = model.generate_content(f"Traduce al español de España: {frase}")
            return response.text
        except Exception:
            continue # Si este falla, salta al siguiente sin avisar
            
    return "❌ Error persistente: Google rechaza la API Key. Por favor, genera una NUEVA llave en Google AI Studio y pégala en Secrets."

# --- INTERFAZ ---
st.title("🇦🇷 Traductor Argento 🇪🇸")
entrada = st.text_input("¿Qué te dijo?")

if st.button("Traducir ahora"):
    if entrada:
        with st.spinner('Peleando con Google...'):
            resultado = realizar_traduccion(entrada)
            st.write(resultado)
