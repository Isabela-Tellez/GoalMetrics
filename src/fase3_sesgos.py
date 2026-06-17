"""
MÓDULO DE ÉTICA Y SESGOS (FASE 3): Auditoría crítica de representatividad.
Análisis de sesgos geográficos, integridad competitiva y cumplimiento normativo.
"""

import plotly.express as px

TEMPLATE = "plotly_dark"


def grafico_correlacion(df):
    # Scatter plot para ver la relación entre goles locales y visitantes
    fig = px.scatter(
        df, 
        x="home_score", 
        y="away_score", 
        opacity=0.5,
        template="plotly_dark",
        trendline="ols",
        color_discrete_sequence=["#c63637"]
    )
    return fig

def grafico_localia_area(df):
    df_temp = df.copy()
    df_temp["diff"] = df_temp["home_score"] - df_temp["away_score"]
    df_area = df_temp.groupby("decade")["diff"].mean().reset_index()
    
    fig = px.area(df_area, x="decade", y="diff", template="plotly_dark")
    fig.update_traces(line_color='#F2E205', fillcolor='rgba(242, 226, 5, 0.3)')
    return fig

def grafico_outliers_burbuja(df):
    fig = px.scatter(df, x="total_goals", y="home_score", size="away_score", 
                    color="total_goals", color_continuous_scale="Viridis", template="plotly_dark")
    return fig


def grafico_top_equipos(df):
    top = df['home_team'].value_counts().head(10).reset_index()
    top.columns = ["team", "wins"]

    fig = px.bar(
        top,
        x="wins",
        y="team",
        orientation="h",
        template=TEMPLATE,
        color_discrete_sequence=["#c63637"]
    )
    return fig