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

# Configuración
if "api_key" in st.secrets:
    genai.configure(api_key=st.secrets["api_key"].strip().replace('"', ''))
else:
    st.error("Falta la clave en Secrets")

def traducir(texto):
    # Forzamos el modelo 'gemini-pro' que es el más compatible del mundo
    try:
        model = genai.GenerativeModel('gemini-pro')
        res = model.generate_content(f"Traduce de argentino a español de España: {texto}")
        return res.text
    except Exception as e:
        return f"Error real de Google: {e}"

frase = st.text_input("¿Qué te dijo?")
if st.button("Descifrar"):
    if frase:
        resultado = traducir(frase)
        st.write(resultado) 
