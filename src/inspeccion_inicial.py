import pandas as pd
import numpy as np
import os

"""
MÓDULO DE INSPECCIÓN INICIAL (FASE 0): Realizado el control de calidad (Sanity Check) analizando 
dimensiones, nulos, duplicados y outliers (IQR vs Z-Score) en los 3 datasets brutos.
"""

# Definimos la ruta estándar hacia la carpeta de datos brutos
RUTA_RAW = os.path.join("data", "raw")

def inspeccion_profunda_futbol(nombre_archivo):
    ruta_completa = os.path.join(RUTA_RAW, nombre_archivo)
    
    # Validación de seguridad por si algún archivo no está en su sitio
    if not os.path.exists(ruta_completa):
        print(f"⚠️ Archivo '{nombre_archivo}' no encontrado en {RUTA_RAW}. Saltando...\n")
        return
    
    # 1. CARGA DE LA FUENTE BRUTA
    df = pd.read_csv(ruta_completa)
    
    print("\n" + "="*80)
    print(f"⚽ DIAGNÓSTICO PROFUNDO: {nombre_archivo}")
    print("="*80)
    
    # Muestra de Dimensiones reales
    print(f"\n📊 DIMENSIONES: {df.shape[0]} filas | {df.shape[1]} columnas")
    
    # Vista previa de registros (.head)
    print("\n=== 📋 PRIMEROS REGISTROS (.head) ===")
    print(df.head(3))
    
    # Información estructural de los tipos de datos (.info)
    print("\n=== 🧬 INFORMACIÓN ESTRUCTURAL (.info) ===")
    df.info()
    
    # Resumen estadístico inicial (.describe)
    print("\n=== 📈 RESUMEN ESTADÍSTICO (.describe) ===")
    print(df.describe(include='all'))
    
    # Auditoría de filas duplicadas
    print("\n=== 👥 REGISTROS DUPLICADOS ===")
    print(f"Filas duplicadas detectadas: {df.duplicated().sum()}")
    
    # 2. ANÁLISIS DE CATEGORÍAS Y TOP 10 (.value_counts)
    print("\n=== 🗂️ DISTRIBUCIÓN DE CATEGORÍAS CLAVE (Top 10) ===")
    cols_futbol = ['home_team', 'away_team', 'tournament', 'country', 'team', 'scorer']
    
    for col in cols_futbol:
        if col in df.columns:
            print(f"\n--- [Top 10] Frecuencias para la columna: '{col}' (Incluye Nulos) ---")
            print(df[col].value_counts(dropna=False).head(10))
            
    # 3. DETECCIÓN AVANZADA DE OUTLIERS (IQR vs. Z-SCORE)
    print("\n=== 🚨 AUDITORÍA DE OUTLIERS (VALORES ATÍPICOS) ===")
    columnas_numericas = df.select_dtypes(include=[np.number]).columns
    
    for col in columnas_numericas:
        if 'id' in col.lower() or 'year' in col.lower():
            continue
            
        print(f"\nAnálisis estadístico de atípicos para: '{col}'")
        
        # --- Método A: Rango Intercuartílico (IQR) ---
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        limite_inferior_iqr = Q1 - 1.5 * IQR
        limite_superior_iqr = Q3 + 1.5 * IQR
        
        outliers_iqr = df[(df[col] < limite_inferior_iqr) | (df[col] > limite_superior_iqr)]
        
        # --- Método B: Z-Score con NumPy y Desviación Estándar ---
        media = df[col].mean()
        desviacion = df[col].std()
        
        if desviacion > 0:
            z_scores = (df[col] - media) / desviacion
            outliers_z = df[np.abs(z_scores) > 3]
        else:
            outliers_z = pd.DataFrame()
            
        print(f"   • [IQR] Límites de aceptación: [{limite_inferior_iqr:.2f} a {limite_superior_iqr:.2f}] | Outliers: {len(outliers_iqr)}")
        print(f"   • [Z-Score] Media: {media:.2f} | Desviación Estándar: {desviacion:.2f} | Outliers (|Z| > 3): {len(outliers_z)}")

    print("\n" + "="*80)

if __name__ == "__main__":
    print("🚀 Iniciando el diagnóstico oficial de los activos de fútbol...\n")
    inspeccion_profunda_futbol("results.csv")
    inspeccion_profunda_futbol("goalscorers.csv")
    inspeccion_profunda_futbol("shootouts.csv")