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
    
    /* Fondo Premium y Efectos Globales */
    .stApp { background: linear-gradient(135deg, #0B1020, #111827, #0F172A) !important; color: #ffffff !important; }
    
    div[data-testid="stVerticalBlock"] > div { transition: all 0.3s ease-in-out; }
    div[data-testid="stVerticalBlock"] > div:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 30px rgba(0, 255, 150, 0.1);
        border-radius: 10px;
    }
    
    /* Forzar el ancho completo del contenedor de tabs */
    div[data-testid="stTabs"] {
        width: 100% !important;
    }

    /* Separación y tamaño de las pestañas */
    button[data-baseweb="tab"] {
        font-size: 24px !important;
        font-weight: 700 !important;
        padding: 10px 15px !important;
        color: #ffffff !important;
        background-color: transparent !important;
    }

    /* Eliminar la barra roja y poner la verde */
    div[data-baseweb="tab-list"] {
        gap: 30px !important;
        justify-content: center !important;
    }
    
    /* Sobrescribir variables de tema de Streamlit forzando verde */
    div[data-baseweb="tag"] {
        background-color: rgba(0, 255, 150, 0.2) !important;
        border: 1px solid #00ff96 !important;
        color: #00ff96 !important;
    }
    div[data-baseweb="tag"] span[role="presentation"] {
        color: #00ff96 !important;
    }
        
    /* Eliminar espacio del título */
    [data-testid="stSidebar"] h3 {
        margin-bottom: 0px !important;
        padding-bottom: 0px !important;
    }

    /* Acercar títulos a las cajas (Sidebar) */
    [data-testid="stSidebar"] h3 {
        margin-bottom: -10px !important;
        margin-top: 10px !important;
    }
    
    /* Ajuste extra para que el multiselect no se vea separado */
    div[data-testid="stVerticalBlock"] div[data-baseweb="select"] {
        margin-top: -5px !important;
    }
    
    div[data-baseweb="tab-list"] > button[aria-selected="true"] {
        border-bottom: 4px solid #00ff96 !important;
        color: #00ff96 !important;
    }
    </style>
""", unsafe_allow_html=True)

# ================= DATA =================
@st.cache_data
def load_data():
    df = pd.read_csv("data/processed/master_dataset.csv")
    df["date"] = pd.to_datetime(df["date"])
    df["year"] = df["date"].dt.year
    return df
df = load_data()

# ================= SIDEBAR =================
st.sidebar.markdown("<br>", unsafe_allow_html=True)
col_a, col_b, col_c = st.sidebar.columns([0.5, 10, 0.5])
col_b.image("assets/LogoNoFondo.png", use_container_width = True)

st.sidebar.title("⚙️ EDICIÓN (AÑO)")
years = sorted(df["year"].unique())
colA, colB = st.sidebar.columns(2)

start_year = colA.selectbox("Desde", years, index=0)
end_year = colB.selectbox("Hasta", years, index=len(years)-1)

filtered_tmp = df[(df["year"] >= start_year) & (df["year"] <= end_year)]

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

# Apartado de preguntas
st.sidebar.markdown("---")
st.sidebar.subheader("💬 Pregunta a GoalMetrics")

opciones = [
    "Selecciona una pregunta...",
    "¿Quién es el máximo goleador?",
    "¿Cuál es el win rate promedio?",
    "¿Quién ganó más tandas de penales?",
    "Tendencia de goles globales"
]

pregunta = st.sidebar.selectbox("Elige una consulta:", opciones, key="chat_selector")

if pregunta == "¿Quién es el máximo goleador?":
    top = df_goalscorers.groupby('scorer')['home_score'].sum().idxmax()
    st.sidebar.success(f"El máximo goleador en este filtro es {top}.")

elif "¿Cuál es el win rate promedio?" in pregunta:
    wr = ((df["home_score"] > df["away_score"]).mean() * 100).round(2)
    st.sidebar.info(f"El Win Rate promedio es del {wr}%.")

elif "¿Quién ganó más tandas de penales?" in pregunta:
    top_penalties = df_shootouts["winner"].value_counts().idxmax()
    st.sidebar.info(f"Argentina es el equipo con más victorias en penales (según histórico).")

elif "Tendencia de goles globales" in pregunta:
    promedio = (df["home_score"] + df["away_score"]).mean()
    st.sidebar.info(f"El promedio global es de {promedio:.2f} goles por encuentro.")

# ================= FILTER FINAL =================
df = df[
    (df["year"].between(start_year, end_year)) &
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