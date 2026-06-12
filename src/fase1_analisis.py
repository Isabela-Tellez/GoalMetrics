import os
import pandas as pd
import numpy as np
from scipy import stats

"""
MÓDULO DE ANÁLISIS ESTADÍSTICO (FASE 1): Análisis integral del gol internacional.
Combina métricas descriptivas históricas con estadística inferencial avanzada (ANOVA y Probabilidad Condicional).
"""

# Ruta estándar
RUTA_RAW = os.path.join("data", "raw")

def carga_y_limpieza_datos():
    """Carga de los datos y aplicación de normalización de la Fase 0"""
    df_results = pd.read_csv(os.path.join(RUTA_RAW, "results.csv"))
    df_goalscorers = pd.read_csv(os.path.join(RUTA_RAW, "goalscorers.csv"))

    columnas_futbol = ['home_team', 'away_team', 'tournament', 'country']
    for col in columnas_futbol:
        if col in df_results.columns:
            df_results[col] = df_results[col].astype(str).str.lower().str.strip()
            df_results[col] = df_results[col].str.replace('á', 'a').str.replace('é', 'e')\
                                            .str.replace('í', 'i').str.replace('ó', 'o')\
                                            .str.replace('ú', 'u')
            
    df_results = df_results.dropna(subset=['home_score', 'away_score'])
    return df_results, df_goalscorers

def ejecucion_fase1_estadistica():
    df_results, df_goalscorers = carga_y_limpieza_datos()

    print("=" * 80)
    print("📈 FASE 1: ANÁLISIS ESTADÍSTICO Y DATA STORYTELLING CONSOLIDADO - GOALMETRICS")
    print("=" * 80)

    # Variables base
    df_results['total_goals'] = df_results['home_score'] + df_results['away_score']
    df_results['date'] = pd.to_datetime(df_results['date'])
    df_results['year'] = df_results['date'].dt.year
    df_results['decade'] = (df_results['year'] // 10) * 10

    # -------------------------------------------------------------------------
    # 1. ANÁLISIS DESCRIPTIVO GENERAL Y FORMA DE LA DISTRIBUCIÓN
    # -------------------------------------------------------------------------
    print("\n📊 1. ANÁLISIS DESCRIPTIVO GENERAL DE ANOTACIONES")
    print(f"   • Promedio histórico de goles por partido: {df_results['total_goals'].mean():.2f}")
    print(f"   • Mediana de goles por partido: {df_results['total_goals'].median():.1f}")
    print(f"   • Dispersión (Desviación Estándar): {df_results['total_goals'].std():.2f} goles")
    
    skewness = df_results['total_goals'].skew()
    kurtosis = df_results['total_goals'].kurt()
    print(f"   • Tendencia de la gráfica: Sesgo a la derecha (Skewness): ({skewness:.2f}) debido a goleadas atípicas aisladas.")
    print(f"   • Concentración de los datos: Pico alto ({kurtosis:.2f}) porque la mayoría de partidos se clavan 2 o 3 goles")

    # -------------------------------------------------------------------------
    # 2. SEGMENTACIÓN HISTÓRICA POR ÉPOCAS (Promedios reales + Matriz Pivote)
    # -------------------------------------------------------------------------
    print("\n⏳ 2. SEGMENTACIÓN HISTÓRICA: Evolución del gol por décadas (Top 5 épocas)")
    goles_por_decada = df_results.groupby('decade')['total_goals'].agg(['mean', 'count']).tail(5)
    print(goles_por_decada)
    
    print("\n📍 Matriz Pivote: Mediana de Goles por Década según Neutralidad")
    goles_pivot = df_results.pivot_table(values='total_goals', index='decade', columns='neutral', aggfunc='median').tail(5)
    print(goles_pivot)

    # -------------------------------------------------------------------------
    # 3. ANÁLISIS DE FACTORES Y PROBABILIDADES CONDICIONALES
    # -------------------------------------------------------------------------
    print("\n🔗 3. ANÁLISIS DE FACTORES: (Correlación y Neutralidad)")
    goles_neutralidad = df_results.groupby('neutral')['total_goals'].mean()
    print("   • Promedio de goles según neutralidad del campo (Mitos vs Realidad):")
    print(goles_neutralidad.to_string())
    
    print("\n🎯 Probabilidad Condicional: Partidos de Alta Anotación (Top 25%)")
    high_goals_threshold = df_results['total_goals'].quantile(0.75)
    df_results['is_high_scoring'] = df_results['total_goals'] > high_goals_threshold
    df_results['is_friendly'] = df_results['tournament'] == 'friendly'
    prob_friendly = df_results[df_results['is_friendly']]['is_high_scoring'].mean() * 100
    prob_official = df_results[~df_results['is_friendly']]['is_high_scoring'].mean() * 100
    print(f"   • Umbral para 'Partido de Locura' (Q3): > {high_goals_threshold:.0f} goles")
    print(f"   • P(Goleada Alta | Partido Amistoso): {prob_friendly:.2f}%")
    print(f"   • P(Goleada Alta | Partido Oficial): {prob_official:.2f}%")

    # Correlación simple
    print("\n🔗 Correlación de Variables con el Total de Goles:")
    numeric_cols = df_results[['home_score', 'away_score', 'total_goals', 'year']]
    print(numeric_cols.corr()['total_goals'].sort_values(ascending=False).to_string())

    # -------------------------------------------------------------------------
    # 4. VALIDACIÓN DE HIPÓTESIS: La Localía y Test Científico ANOVA
    # -------------------------------------------------------------------------
    print("\n🎯 4. VALIDACIÓN DE HIPÓTESIS: ¿Existe la ventaja de ser local?")
    condiciones = [
        (df_results['home_score'] > df_results['away_score']),
        (df_results['home_score'] < df_results['away_score']),
        (df_results['home_score'] == df_results['away_score'])
    ]
    opciones = ['Victoria Local', 'Victoria Visitante', 'Empate']
    df_results['resultado'] = np.select(condiciones, opciones, default='Otro')
    distribucion_resultados = df_results['resultado'].value_counts(normalize=True) * 100
    
    print("   • Distribución porcentual histórica de resultados:")
    for res, porcentaje in distribucion_resultados.items():
        print(f"   - {res}: {porcentaje:.2f}%")

    print("\n🧪 5. PRUEBA DE HIPÓTESIS FORMAL (ANOVA): ¿El tipo de torneo influye?")
    top_tournaments = df_results['tournament'].value_counts().head(3).index
    df_anova = df_results[df_results['tournament'].isin(top_tournaments)]
    groups = [group['total_goals'].values for name, group in df_anova.groupby('tournament')]
    f_stat, p_value = stats.f_oneway(*groups)

    print(f"   • Estadístico F: {f_stat:.2f}")
    print(f"   • P-Value: {p_value:.4f}")
    if p_value < 0.05:
        print("   • Conclusión: El tipo de torneo SÍ influye significativamente en los goles (Rechazamos H0).")
    else:
        print("   • Conclusión: Las diferencias de goles globales entre torneos masivos son por azar (No rechazamos H0).")

    print("\n" + "=" * 80)

if __name__ == "__main__":
    ejecucion_fase1_estadistica()