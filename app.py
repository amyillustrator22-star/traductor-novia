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

if "api_key" in st.secrets:
    llave = st.secrets["api_key"].strip().replace('"', '')
    genai.configure(api_key=llave)

def traducir_final(texto):
    try:
        # TRUCO MAESTRO: Le preguntamos a Google qué modelos tienes ACTIVOS hoy
        modelos_disponibles = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
        
        if not modelos_disponibles:
            return "Tu API Key aún no tiene modelos activos. Google tarda unas horas en activarlos la primera vez."
        
        # Usamos el primero que aparezca en tu lista
        model = genai.GenerativeModel(modelos_disponibles[0])
        res = model.generate_content(f"Traduce al español de España: {texto}")
        return res.text
    except Exception as e:
        return f"Error de Google: {e}"

frase = st.text_input("Dime qué te ha dicho:")
if st.button("Descifrar"):
    if frase:
        st.write(traducir_final(frase)) 
