#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 30 00:55:56 2026

@author: amy
"""

import streamlit as st
import google.generativeai as genai

# 1. Configuración visual rápida
st.set_page_config(page_title="Traductor Argento", page_icon="🧉")
st.title("🇦🇷 Traductor Novia (Versión Pro) 🇪🇸")

# 2. Conexión con tu cuenta (Usando tu secreto)
if "api_key" in st.secrets:
    # Limpiamos la clave de espacios o comillas rebeldes
    llave = st.secrets["api_key"].strip().replace('"', '').replace("'", "")
    genai.configure(api_key=llave)
else:
    st.error("⚠️ No has pegado la api_key en los Secrets de Streamlit.")

# 3. Función de traducción robusta
def traducir_frase(texto):
    # Probamos los nombres de los modelos de pago
    modelos_pro = ['gemini-1.5-pro', 'models/gemini-1.5-pro', 'gemini-1.5-flash']
    
    for nombre in modelos_pro:
        try:
            model = genai.GenerativeModel(nombre)
            # Prompt específico para que sea útil
            prompt = (
                f"Traduce esta frase de una argentina a español de España: '{texto}'. "
                f"Explica el tono (enfado, ironía, amor) y cómo debería responder el novio."
            )
            response = model.generate_content(prompt)
            return response.text
        except Exception:
            continue # Si uno falla, intenta el siguiente modelo Pro
            
    return "❌ Error: Google no reconoce tu suscripción o la clave está mal pegada. Verifica los Secrets."

# 4. Interfaz de usuario
frase_input = st.text_area("¿Qué te ha dicho?", placeholder="Escribe aquí la frase...")

if st.button("Descifrar"):
    if frase_input:
        with st.spinner('Consultando a la IA Pro...'):
            resultado = traducir_frase(frase_input)
            st.info(resultado)
    else:
        st.warning("Escribe algo primero.")

st.markdown("---")
st.caption("Usando tu suscripción Gemini Paid Tier.") 
