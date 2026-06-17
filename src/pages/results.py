import streamlit as st
from src import fase2_estadistica as fase2
from src import fase3_sesgos as fase3

def render(df):
    st.title("⚽ Resultados y Rendimiento")

    # Usamos contenedores para evitar el problema de los bordes y mejorar la legibilidad
    with st.container(border=True):
        st.subheader("⚽ ¿Cómo se distribuyen los resultados?")
        # Llamamos a la función de fase2 que ya tenías diseñada
        st.plotly_chart(fase2.obtener_grafico_localia(df), use_container_width=True, key="grafico_localia_results")
        st.markdown('<div style="margin: 15px 0; padding: 15px; background: #0B1220; border-radius: 8px; border-left: 4px solid #F59E0B;"><b>Insight:</b> Los equipos locales mantienen una ventaja histórica consistente.</div>', unsafe_allow_html=True)

    with st.container(border=True):
        st.subheader("📊 Correlación de marcadores")
        # Llamamos a la función de fase3
        st.plotly_chart(fase3.grafico_correlacion(df), use_container_width=True, key="grafico_corr_results")
        st.markdown('<div style="margin: 15px 0; padding: 15px; background: #0B1220; border-radius: 8px; border-left: 4px solid #F59E0B;"><b>Insight:</b> Análisis de la densidad de resultados entre local y visitante.</div>', unsafe_allow_html=True)