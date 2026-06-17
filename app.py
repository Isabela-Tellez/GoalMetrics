import streamlit as st
import pandas as pd
from src import fase1_analisis as fase1
from src import fase2_estadistica as fase2
from src.pages import home, evolution, results, governance, recommendations, conclusions

df_results, df_goalscorers, df_shootouts = fase1.carga_y_limpieza_datos()

# ================= CONFIG =================
st.set_page_config(
    page_title="Football BI Dashboard",
    layout="wide",
    page_icon="⚽"
)

# ================= CSS GLOBAL =================
st.markdown("""
    <style>
    /* Asegura una sola línea, centra los elementos y añade separación fija */
    [data-testid="stHorizontalBlock"] { flex-wrap: nowrap !important; justify-content: center !important; gap: 60px !important; }
    /* Estilo del texto */
    button p { font-size: 18px !important; font-weight: 700 !important; }
    </style>
""", unsafe_allow_html=True)

# ================= DATA =================
@st.cache_data
def load_data():
    return pd.read_csv("data/processed/master_dataset.csv")
df = load_data()

# ================= SIDEBAR =================
st.sidebar.markdown("<br>", unsafe_allow_html=True)
col_a, col_b, col_c = st.sidebar.columns([0.5, 10, 0.5])
col_b.image("assets/LogoNoFondo.png", use_container_width = True)

st.sidebar.title("⚙️ EDICIÓN (AÑO)")
years = sorted(df["decade"].unique())
colA, colB = st.sidebar.columns(2)

start_year = colA.selectbox("Desde", years, index=0)
end_year = colB.selectbox("Hasta", years, index=len(years)-1)

filtered_tmp = df[(df["decade"] >= start_year) & (df["decade"] <= end_year)]

# KPI CARD
st.sidebar.markdown(f"""
<div class="kpi-box">
    <div style="display:flex; justify-content:space-between; align-items:center;">
        <div><div style="color:#F59E0B; font-size:18px; font-weight:bold;">{start_year}</div><div style="font-size:10px;">DESDE</div></div>
        <div>⚽</div>
        <div><div style="color:#F59E0B; font-size:18px; font-weight:bold;">{end_year}</div><div style="font-size:10px;">HASTA</div></div>
        <div style="border-left:1px solid #2d3748; padding-left:10px;"><div style="font-size:16px; font-weight:bold;">{len(filtered_tmp)}</div><div style="font-size:10px;">PARTIDOS</div></div>
    </div>
</div>
""", unsafe_allow_html=True)

def get_label(selected, all_items):
    return "Todos" if len(selected) == len(all_items) else ", " .join(selected[:2]) + "..."

# TORNEOS
st.sidebar.markdown("### 🏆 FASE DE TORNEO")
all_tournaments = df["tournament"].unique()
tournaments = st.sidebar.multiselect(
    "Fase de Torneo", 
    options=all_tournaments,
    default=all_tournaments,
    label_visibility="hidden",
    key="t_selector"
)

# PAISES
st.sidebar.markdown("### 🌍 PAISES")
all_countries = df["country"].unique()
countries = st.sidebar.multiselect(
    "Paises", 
    options=all_countries,
    default=all_countries,
    label_visibility="hidden",
    key="c"
)
st.sidebar.caption(f"Seleccionado: {get_label(countries, all_countries)}")

# ================= FILTER FINAL =================
df = df[
    (df["decade"].between(start_year, end_year)) &
    (df["tournament"].isin(tournaments)) &
    (df["country"].isin(countries))
]

# ================= NAVIGATION =================

tabs = st.tabs([
    "🏠 Inicio",
    "📅 Evolución",
    "⚽ Resultados",
    "🔍 Sesgos",
    "🎯 Recomendaciones",
    "📌 Conclusiones"
])

with tabs[0]:
    home.render(df)

with tabs[1]:
    evolution.render(df)

with tabs[2]:
    results.render(df)

with tabs[3]:
    governance.render(df)

with tabs[4]:
    recommendations.render(df)

with tabs[5]:
    conclusions.render(df)