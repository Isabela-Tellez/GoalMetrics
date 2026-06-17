import streamlit as st
import plotly.express as px
from src import fase2_estadistica as fase2

def render(df):
    st.title("📅 Evolución Histórica")

    with st.container(border=True):
        st.subheader("Goles por década")
        st.plotly_chart(fase2.obtener_grafico_evolucion_goles(df), use_container_width=True, key="evolucion_goles_evo")
        st.markdown('<div style="margin: 10px 0 20px 0; padding: 15px; background: #0B1220; border-radius: 8px; border-left: 4px solid #F59E0B;"><b>Análisis:</b> Se observa una estabilización en el promedio de goles, lo que sugiere una mayor madurez táctica.</div>', unsafe_allow_html=True)

    with st.container(border=True):
        st.subheader("Dominio de Victorias Locales por Década")
        st.plotly_chart(fase2.obtener_grafico_dominio_por_decada(df), use_container_width=True, key="dominio_decada")
        st.markdown('<div style="margin-top: 15px; margin-bottom: 5px; padding: 15px; background: #0B1220; border-radius: 8px; border-left: 4px solid #F59E0B;"><b>Análisis:</b> Identifica qué periodos históricos presentaron una mayor ventaja competitiva para los locales.</div>', unsafe_allow_html=True)