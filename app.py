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

# Cargamos la llave (ya sabemos que funciona, Amy!)
if "api_key" in st.secrets:
    llave = st.secrets["api_key"].strip().replace('"', '')
    genai.configure(api_key=llave)
else:
    st.error("Falta la clave")

def traducir(texto):
    try:
        # Este es el nombre exacto que pide la version v1beta
        model = genai.GenerativeModel('models/gemini-1.5-flash-latest')
        res = model.generate_content(f"Traduce al español de España: {texto}")
        return res.text
    except Exception as e:
        # Si ese falla, probamos con este otro nombre oficial
        try:
            model = genai.GenerativeModel('gemini-1.5-flash')
            res = model.generate_content(f"Traduce: {texto}")
            return res.text
        except Exception as e2:
            return f"Error de modelo: {e2}"

frase = st.text_input("¿Qué te dijo?")
if st.button("Descifrar"):
    if frase:
        st.write(traducir(frase)) 
