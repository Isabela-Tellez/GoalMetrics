import plotly.express as px
import pandas as pd

# CONFIGURACIÓN DE ESTILO PARA LAS GRÁFICAS (Mantiene la coherencia visual)
TEMPLATE = "plotly_dark"
COLOR_GOLD = "#F59E0B"
COLOR_AMBER = "#D97706"

def obtener_grafico_localia(df):
    data = df['resultado_match'].value_counts().reset_index()
    data.columns = ['Resultado', 'Cantidad']

    fig = px.pie(
        data,
        values='Cantidad',
        names='Resultado',
        hole=0.5,
        template=TEMPLATE,
        color_discrete_sequence=['#F2BC57', '#c63637', '#5ac15d'] 
    )
    return fig

def obtener_grafico_evolucion_goles(df):
    df_evo = df.groupby('decade')['total_goals'].mean().reset_index()

    fig = px.line(
        df_evo,
        x='decade',
        y='total_goals',
        markers=True,
        template=TEMPLATE,
        color_discrete_sequence=["#5ac15d"]
    )
    return fig

def obtener_grafico_dominio_por_decada(df):
    df_dom = df[df['resultado_match'] == 'Victoria Local'] \
        .groupby('decade').size().reset_index(name='victorias')
    fig = px.bar(df_dom, x='decade', y='victorias', template="plotly_dark", 
                color_discrete_sequence=['#F2BC57'])
    return fig

def obtener_grafico_potencia(df):
    df_top = df[df['resultado_match'] == 'Victoria Local'] \
        .groupby('home_team').size().reset_index(name='victorias')

    df_top = df_top.sort_values('victorias', ascending=False).head(10)

    fig = px.bar(
        df_top,
        x='victorias',
        y='home_team',
        orientation='h',
        template=TEMPLATE
    )
    return fig


def obtener_grafico_outliers(df):
    fig = px.scatter(
        df,
        x='date',
        y='total_goals',
        color='total_goals',
        template=TEMPLATE
    )
    return fig