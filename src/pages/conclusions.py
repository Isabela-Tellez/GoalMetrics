import streamlit as st

def render(df):
    st.title("📌 Conclusiones")
    
    st.markdown("""
    <div style="background: #0B1220; padding: 20px; border-radius: 10px; border-left: 5px solid #F59E0B; margin-bottom: 20px;">
        <h4 style="color: #F59E0B; margin-top: 0;">📊 Aprendizajes Clave</h4>
        <ul style="margin-bottom: 0;">
            <li><b>Ventaja de localía:</b> Identificada como un factor consistente históricamente.</li>
            <li><b>Sesgos de datos:</b> Representación desigual en los registros históricos.</li>
            <li><b>Evolución táctica:</b> Cambios significativos en el comportamiento de goles por década.</li>
        </ul>
    </div>
    
    <div style="background: #0B1220; padding: 20px; border-radius: 10px; border-left: 5px solid #F59E0B; margin-bottom: 20px;">
        <h4 style="color: #F59E0B; margin-top: 0;">🚀 Roadmap Futuro</h4>
        <ul style="margin-bottom: 0;">
            <li>Implementación de <b>modelos predictivos</b> de resultados.</li>
            <li>Integración de <b>datos externos</b> (FIFA, clima, localía).</li>
            <li>Análisis granular por <b>torneo</b> y contexto geográfico.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)