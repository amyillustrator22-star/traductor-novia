#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 30 00:55:56 2026

@author: amy
"""

import streamlit as st
import google.generativeai as genai

# --- CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(
    page_title="Traductor Argento", 
    page_icon="🧉", 
    layout="centered"
)

# Estilos para que se vea bien en móvil
st.markdown("""
    <style>
    .main {
        background-color: #f5f7f9;
    }
    .stButton>button {
        width: 100%;
        border-radius: 20px;
        height: 3em;
        background-color: #0083B0;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🇦🇷 Traductor Argento 🇪🇸")
st.subheader("Entiende a tu novia en segundos")

# --- CONFIGURACIÓN DE SEGURIDAD (API KEY) ---
# Intentamos leer la clave desde los Secrets de Streamlit (para la nube)
# Si no existe, avisamos al usuario.
try:
    if "api_key" in st.secrets:
        API_KEY = st.secrets["api_key"]
    else:
        # Esto es solo por si pruebas localmente antes de subirlo
        API_KEY = "TU_API_KEY_DE_PRUEBA_AQUI" 
    
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error("⚠️ Error de configuración: Asegúrate de poner la 'api_key' en los Secrets de Streamlit.")

# --- LÓGICA DE TRADUCCIÓN ---
def realizar_traduccion(frase):
    prompt = f"""
    Actúa como un mediador lingüístico experto en la relación Argentina-España.
    Tu objetivo es ayudar a un español a entender a su novia argentina.
    
    Analiza la siguiente frase: "{frase}"
    
    Devuelve la respuesta con este formato:
    - 🇪🇸 **TRADUCCIÓN AL ESPAÑOL:** (Significado en España con jerga local)
    - ⚠️ **NIVEL DE BARDO:** (1 al 5)
    - 🎭 **CONTEXTO:** (Si es broma, cariño o enfado real)
    - 💡 **CONSEJO:** (Qué responder para quedar bien)
    """
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error al consultar a la IA: {e}"

# --- INTERFAZ DE USUARIO ---
st.write("Introduce la frase que te ha dejado descolocado:")
frase_novia = st.text_area("Mensaje de ella:", placeholder="Ej: Me re colgué, no seas tan denso...", height=100)

if st.button("¡Descifrar ya!"):
    if frase_novia.strip():
        with st.spinner('Analizando el bardo...'):
            resultado = realizar_traduccion(frase_novia)
            st.markdown("---")
            st.markdown(resultado)
    else:
        st.warning("Escribe algo primero, ¡che!")

st.markdown("---")
st.caption("Creado para sobrevivir al amor sin fronteras. 💙")