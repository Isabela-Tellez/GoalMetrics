import streamlit as st

def render(df):
    st.title("🎯 Recomendaciones Estratégicas")
    st.markdown("### 📌 Hoja de ruta para optimizar el negocio basado en datos")

    insights = [
        ("Segmentación Temporal", "Priorizar el análisis por décadas para ajustar modelos de predicción a la evolución del juego."),
        ("Factor Localía", "Integrar la ventaja de campo como variable crítica en cualquier algoritmo de probabilidades."),
        ("Enriquecimiento de Datos", "Incorporar métricas externas como rankings FIFA y factores climáticos para mayor precisión.")
    ]

    for title, desc in insights:
        st.markdown(f"""
        <div style="background: #0B1220; padding: 20px; border-radius: 10px; border-left: 5px solid #F59E0B; margin-bottom: 15px;">
            <h4 style="margin: 0; color: #F59E0B;">{title}</h4>
            <p style="margin: 10px 0 0 0;">{desc}</p>
        </div>
        """, unsafe_allow_html=True)