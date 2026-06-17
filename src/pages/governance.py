import streamlit as st
from src import fase3_sesgos as f3

def render(df):
    st.title("🔍 Sesgos y Gobernanza")

    with st.container(border=True):
        st.subheader("⚖️ Evolución de la Ventaja de Localía")
        st.plotly_chart(f3.grafico_localia_area(df), use_container_width=True)
        st.markdown('<div style="margin: 10px 0 20px 0; padding: 15px; background: #0B1220; border-radius: 8px; border-left: 4px solid #F59E0B;"><b>Análisis:</b> La tendencia temporal de la diferencia de goles revela variaciones en el impacto del factor local sobre la integridad competitiva.</div>', unsafe_allow_html=True)

    with st.container(border=True):
        st.subheader("🚀 Distribución de Anomalías (Outliers)")
        st.plotly_chart(f3.grafico_outliers_burbuja(df), use_container_width=True)
        st.markdown('<div style="margin: 10px 0 20px 0; padding: 15px; background: #0B1220; border-radius: 8px; border-left: 4px solid #F59E0B;"><b>Análisis:</b> La escala de burbujas destaca partidos extremos frente a la media, permitiendo detectar posibles errores o hitos históricos.</div>', unsafe_allow_html=True)

    with st.container(border=True):
        st.subheader("🏆 Top Equipos")
        st.plotly_chart(f3.grafico_top_equipos(df), use_container_width=True)
        st.markdown('<div style="margin: 10px 0 20px 0; padding: 15px; background: #0B1220; border-radius: 8px; border-left: 4px solid #F59E0B;"><b>Análisis:</b> Este ranking evidencia qué naciones dominan el registro histórico, exponiendo posibles sesgos de mayor frecuencia en la recopilación de datos.</div>', unsafe_allow_html=True)