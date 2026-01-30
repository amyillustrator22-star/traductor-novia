#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 30 00:55:56 2026

@author: amy
"""

import streamlit as st
import google.generativeai as genai

# --- CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(page_title="Traductor Argento", page_icon="🧉")

st.title("🇦🇷 Traductor Argento 🇪🇸")
st.markdown("---")

# --- CONEXIÓN SEGURA ---
try:
    # Busca la clave en la "caja fuerte" de Streamlit
    API_KEY = st.secrets["api_key"]
    genai.configure(api_key=API_KEY)
except Exception:
    st.error("❌ Error: No se encontró la 'api_key' en los Secrets de Streamlit.")

# --- FUNCIÓN DE TRADUCCIÓN MAESTRA ---
def realizar_traduccion(frase):
    # Probamos todos los nombres posibles para evitar el error 404
    modelos_a_probar = [
        'gemini-1.5-flash', 
        'models/gemini-1.5-flash', 
        'gemini-1.5-pro', 
        'models/gemini-1.5-pro'
    ]
    
    for nombre in modelos_a_probar:
        try:
            model = genai.GenerativeModel(nombre)
            prompt = (
                f"Eres un experto en cultura argentina y española. "
                f"Traduce esta frase de una chica argentina a su novio español: '{frase}'. "
                f"Usa jerga española de España. Indica NIVEL DE PELIGRO (1-5) "
                f"y una RESPUESTA RECOMENDADA para evitar el bardo."
            )
            response = model.generate_content(prompt)
            return response.text
        except Exception:
            continue # Si falla, salta al siguiente modelo
            
    return "❌ Error: Ningún modelo respondió. Por favor, genera una nueva API Key en Google AI Studio."

# --- INTERFAZ ---
frase_input = st.text_area("¿Qué te ha dicho ahora?", placeholder="Ej: Me tenés re podrida...")

if st.button("Descifrar"):
    if frase_input.strip():
        with st.spinner('Consultando a la IA...'):
            resultado = realizar_traduccion(frase_input)
            st.info(resultado)
    else:
        st.warning("⚠️ Escribe algo primero, ¡che!")

st.markdown("---")
st.caption("Versión estable 2026. Lista para usar en iPhone y Android.")
