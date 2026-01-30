#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 30 00:55:56 2026

@author: amy
"""

import streamlit as st
import google.generativeai as genai

# --- CONFIGURACIÓN DE LA PÁGINA PARA MÓVIL ---
st.set_page_config(page_title="Traductor Argento", page_icon="🧉")

st.title("🇦🇷 Traductor de Novia 🇪🇸")
st.markdown("---")

# --- CONEXIÓN SEGURA ---
try:
    # Leemos la clave desde los Secrets de Streamlit
    API_KEY = st.secrets["api_key"]
    genai.configure(api_key=API_KEY)
except Exception:
    st.error("❌ Error: No se encontró la API Key en los Secrets de Streamlit.")

# --- FUNCIÓN DE TRADUCCIÓN (CON PARCHE PARA ERROR 404) ---
def realizar_traduccion(frase):
    # Lista de nombres de modelos para probar cuál acepta Google hoy
    nombres_a_probar = ['gemini-1.5-flash', 'models/gemini-1.5-flash']
    
    for nombre in nombres_a_probar:
        try:
            model = genai.GenerativeModel(nombre)
            prompt = (
                f"Eres un experto en cultura argentina y española. "
                f"Analiza esta frase de una chica argentina: '{frase}'. "
                f"Tradúcela al español de España (usando jerga de allí), "
                f"indica el NIVEL DE PELIGRO (1-5) y una RESPUESTA RECOMENDADA."
            )
            response = model.generate_content(prompt)
            return response.text
        except Exception:
            # Si falla uno, el bucle intenta con el siguiente nombre
            continue
            
    return "❌ Error: Google no reconoce los modelos. Revisa si tu API Key tiene permisos para Gemini 1.5 Flash."

# --- INTERFAZ ---
frase_input = st.text_area("¿Qué te ha dicho ahora?", placeholder="Ej: No seas un pollerudo...")

if st.button("Descifrar"):
    if frase_input:
        with st.spinner('Traduciendo...'):
            resultado = realizar_traduccion(frase_input)
            st.info(resultado)
    else:
        st.warning("⚠️ Escribe algo, ¡che!")

st.markdown("---")
st.caption("Hecho con paciencia para relaciones a distancia.")
