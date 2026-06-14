"""
MÓDULO DE UNIFICACIÓN (FASE 2): Combinación de los 3 datasets originales
en una única tabla maestra optimizada para Power BI.
"""

import os
import pandas as pd
import numpy as np

RUTA_RAW = os.path.join("data", "raw")
RUTA_PROCESSED = os.path.join("data", "processed")
os.makedirs(RUTA_PROCESSED, exist_ok=True)

def unificar_datasets_powerbi():
    print("🔄 Iniciando carga y unificación de los 3 datasets...")
    
    # 1. Carga de los 3 archivos originales de forma independiente
    df_results_orig = pd.read_csv(os.path.join(RUTA_RAW, "results.csv"))
    df_shootouts_orig = pd.read_csv(os.path.join(RUTA_RAW, "shootouts.csv"))
    df_scorers_orig = pd.read_csv(os.path.join(RUTA_RAW, "goalscorers.csv"))
    
    # 2. Creación de copias explícitas para trabajar de forma segura
    results = df_results_orig.copy()
    shootouts = df_shootouts_orig.copy()
    scorers = df_scorers_orig.copy()
    
    # 3. Homologar el formato de fecha en TODOS los DataFrames para evitar el ValueError
    results['date'] = pd.to_datetime(results['date'])
    shootouts['date'] = pd.to_datetime(shootouts['date'])
    scorers['date'] = pd.to_datetime(scorers['date'])
    
    # 4. Procesado de métricas base en la tabla principal (Results)
    results['total_goals'] = results['home_score'] + results['away_score']
    results['decade'] = (results['date'].dt.year // 10) * 10
    
    condiciones = [results['home_score'] > results['away_score'], results['home_score'] < results['away_score']]
    results['resultado_match'] = np.select(condiciones, ['Victoria Local', 'Victoria Visitante'], default='Empate')
    
    # 5. Cruce de los datos (Merge) ahora que las llaves de fecha coinciden perfectamente
    df_unificado = pd.merge(results, shootouts, on=['date', 'home_team', 'away_team'], how='left')
    df_final = pd.merge(df_unificado, scorers, on=['date', 'home_team', 'away_team'], how='left')
    
    # 6. Exportación de la tabla maestra final
    ruta_salida = os.path.join(RUTA_PROCESSED, "master_powerbi.csv")
    df_final.to_csv(ruta_salida, index=False)
    print(f"✅ ¡Éxito! Tabla maestra unificada creada en: {ruta_salida}")

if __name__ == "__main__":
    unificar_datasets_powerbi()