import os
import pandas as pd
import numpy as np

"""
MÓDULO DE ANÁLISIS ESTADÍSTICO (FASE 1): Extracción de conocimiento histórico mediante el cálcuo de
tendencias, evolución de gol por décadas, análisis de factores del partido y validación empírica del mito
de la localía
"""

# Ruta estándar
RUTA_RAW = os.path.join("data" , "raw")

def carga_y_limpieza_datos():
    """Carga de los datos y aplicación de normalización consolidada en la Fase 0"""
    df_results = pd.read_csv(os.path.join(RUTA_RAW , "results.csv"))
    df_goalscorers = pd.read_csv(os.path.join(RUTA_RAW , "goalscorers.csv"))

    # Aplicación de normalización básica estilo pandas
    columnas_futbol = ['home_team', 'away_team', 'tournament', 'country', 'team', 'scorer']
    for col in columnas_futbol:
        if col in df_results.columns:
            df_results[col] = df_results[col].astype(str).str.lower().str.strip()
            df_results[col] = df_results[col].str.replace('á' , 'a').str.replace('é' , 'e')\
                                        .str.replace('í' , 'i').str.replace('ó' , 'o')\
                                        .str.replace('ú' , 'u')
            
    # Eliminación de filas corruptas detectadas en la Fase 0 (sin marcador)
    df_results = df_results.dropna(subset = ['home_score' , 'away_score'])

    return df_results , df_goalscorers

def ejecucion_fase1_estadistica():
    df_results , df_goalscorers = carga_y_limpieza_datos()

    print("=" * 80)
    print("📈 FASE 1: ANÁLISIS ESTADÍSTICO Y DATA STORYTELLING - GOALMETRICS")
    print("=" * 80)

    # Creación de variables necesarias para la historia
    df_results['total_goals'] = df_results['home_score'] + df_results['away_score']
    df_results['date'] = pd.to_datetime(df_results['date'])
    df_results['year'] = df_results['date'].dt.year
    df_results['decade'] = (df_results['year'] // 10) * 10

    # -------------------------------------------------------------------------
    # 1. ANÁLISIS DESCRIPTIVO (Medias, Medianas y Dispersión de Goles)
    # -------------------------------------------------------------------------
    print("\n📊 1. ANÁLISIS DESCRIPTIVO GENERAL DE ANOTACIONES")
    media_goles = df_results['total_goals'].mean()
    mediana_goles = df_results['total_goals'].median()
    desviacion_goles = df_results['total_goals'].std()

    print(f"   • Promedio histórico de goles por partido: {media_goles:.2f}")
    print(f"   • Mediana de goles por partido: {mediana_goles:.1f}")
    print(f"   • Dispersión (Desviación Estándar): {desviacion_goles:.2f} goles")

    # -------------------------------------------------------------------------
    # 2. SEGMENTACIÓN POR ÉPOCA (Impacto de las Décadas en la Remuneración de Goles)
    # -------------------------------------------------------------------------
    print("\n⏳ 2. SEGMENTACIÓN HISTÓRICA: Evolución del gol por décadas (Top 5 épocas)")
    goles_por_decada = df_results.groupby('decade')['total_goals'].agg(['mean' , 'count']).tail(5)
    print(goles_por_decada)

    # -------------------------------------------------------------------------
    # 3. ANÁLISIS DE CORRELACIONES (Efecto del Torneo y Neutralidad en el Marcador)
    # -------------------------------------------------------------------------
    print("\n🔗 3. ANÁLISIS DE FACTORES: (Correlación de condiciones del partido)")
    
    # Se evalua si jugar en campo neutral reduce o aumenta los goles promedio
    goles_neutralidad = df_results.groupby('neutral')['total_goals'].mean()
    print("   • Promedio de goles según neutralidad del campo")
    print(goles_neutralidad.to_string())

    # -------------------------------------------------------------------------
    # 4. VALIDACIÓN DE HIPÓTESIS: ¿Influye la ubicación geográfica?(Localía)
    # -------------------------------------------------------------------------
    print("\n🎯 4. VALIDACIÓN DE HIPÓTESIS: ¿Existe la ventaja de ser local?")

    # Definición de las condiciones de victoria
    condiciones = [
        (df_results['home_score'] > df_results['away_score']),
        (df_results['home_score'] < df_results['away_score']),
        (df_results['home_score'] == df_results['away_score'])
    ]

    opciones = ['Victoria Local', 'Victoria Visitante', 'Empate']
    df_results['resultado'] = np.select(condiciones, opciones, default = 'Otro')

    distribucion_resultados = df_results['resultado'].value_counts(normalize = True) * 100
    print("   • Distribución porcentual histórica de resultados:")
    for res, porcentaje in distribucion_resultados.items():
        print(f"   - {res}: {porcentaje:.2f}%")

    print("\n" + "=" * 80)

if __name__ == "__main__":
    ejecucion_fase1_estadistica() 