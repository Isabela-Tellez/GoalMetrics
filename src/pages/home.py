import country_converter as coco
import streamlit as st
from src import utils
import pandas as pd
import logging

def render(df):
    # CABECERA PERSONALIZADA PARA GoalMetrics
    # Asegurar formato fecha para el cálculo de años
    df['date'] = pd.to_datetime(df['date'])

    # CABECERA PERSONALIZADA
    st.markdown("""
    <div style="background-color: #0B1220; padding: 25px; border-radius: 15px; border-left: 5px solid #F59E0B; display: flex; justify-content: space-between; align-items: center;">
        <div>
            <div style="color: #F59E0B; font-size: 12px; font-weight: bold; letter-spacing: 2px;">FÚTBOL INTERNACIONAL · ANALYTICS PLATFORM</div>
            <h1 style="color: white; margin: 5px 0;">GoalMetrics</h1>
            <div style="color: #94a3b8;">Analítica avanzada histórica · <b>Registros desde inicios del fútbol</b></div>
        </div>
        <div style="font-size: 60px;">🌍</div>
    </div>
    <br>
    """, unsafe_allow_html=True)

    # MÉTRICAS EN CAJAS ESTILIZADAS
    cols = st.columns(4)
    metricas = [
        ("Partidos", len(df)),
        ("Paises", df["home_team"].nunique()),
        ("Goles Local", round(df["home_score"].mean(), 2)),
        ("Goles Visitante", round(df["away_score"].mean(), 2))
    ]

    for i, col in enumerate(cols):
        label, value = metricas[i]
        col.markdown(f"""
        <div style="background: #111827; padding: 15px; border-radius: 10px; border-left: 4px solid #F59E0B; text-align: center;">
            <div style="color: #F59E0B; font-size: 12px;">{label}</div>
            <div style="color: white; font-size: 24px; font-weight: bold;">{value}</div>
        </div>
        """, unsafe_allow_html=True)

    # Insights automáticos
    insights = utils.generar_insights_automaticos(df)
    items_html = ""
    for line in insights:
        line_clean = line.replace("**", "")
        if ":" in line_clean:
            titulo, resto = line_clean.split(":", 1)
            items_html += f'<div style="margin-bottom: 12px; color: #cbd5e1; display: flex; align-items: flex-start;"><span style="color: #F59E0B; margin-right: 8px; font-weight: bold;">•</span><div><b style="color: white;">{titulo}:</b>{resto}</div></div>'
        else:
            items_html += f'<div style="margin-bottom: 12px; color: #cbd5e1;">• {line_clean}</div>'

    # 2. IMPORTANTE: El st.markdown debe estar pegado al margen izquierdo del archivo
    st.markdown(f"""
    <div style="background: #111827; padding: 20px; border-radius: 15px; border-left: 5px solid #F59E0B; margin-top: 20px">
    <h3 style="color: white; margin-top: 0; margin-bottom: 15px;">🧠 GoalMetrics AI Insights</h3>
    {items_html}
    </div>
    """, unsafe_allow_html=True)

    # Resumen Ejecutivo
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
    <div style="background: #111827; padding: 20px; border-radius: 15px; border-left: 5px solid #F59E0B; margin-bottom: 20px;">
        <h3 style="color: white; margin-top: 0;">📋 Resumen Ejecutivo</h3>
        <p style="color: #cbd5e1; line-height: 1.6;">
            GoalMetrics analiza el comportamiento histórico del fútbol internacional. 
            Actualmente, el dataset procesa <b>{}</b> partidos, detectando patrones de rendimiento 
            tanto en localía como en la eficiencia goleadora global. La base de datos 
            se mantiene actualizada para ofrecer métricas precisas sobre la evolución del juego.
        </p>
    </div>
    """.format(len(df)), unsafe_allow_html=True)

    # Lógica de datos
    logging.getLogger("country_converter").setLevel(logging.ERROR)
    cc = coco.CountryConverter()
    resumen = df.groupby("home_team").apply(lambda x: pd.Series({
        "ISO": cc.convert(x.name, to='ISO2'),
        "WinRate": ((x["home_score"] > x["away_score"]).mean() * 100).round(2)
    })).reset_index().rename(columns = {"home_team": "Team"})

    if "WinRate" in resumen.columns:
        resumen = resumen.sort_values(by = "WinRate", ascending = False)
    else:
        st.error(f"Columnas disponibles: {resumen.columns.tolist()}")
    
    print(df.columns)

    # Renderizado de tarjetas
    cols = st.columns(3)
    for i, row in resumen.iterrows():
        iso = str(row['ISO']) if isinstance(row['ISO'], str) else "xx"
        cols[i % 3].markdown(f"""<div style="background: #111827; padding: 10px; border-radius: 8px; border-left: 4px solid #F59E0B; margin-bottom: 10px;">
        <img src="https://flagcdn.com/24x18/{iso.lower()}.png"> <b>{row['Team']}</b><br>
        <small>Win Rate: {row['WinRate']}%</small></div>""", unsafe_allow_html=True)