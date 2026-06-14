"""
MÓDULO DE ÉTICA Y SESGOS (FASE 3): Abálisis crítico de representatividad.
Sesgos geográficos y auditoría de privacidad sobre la tabla maestra
"""

import os
import pandas as pd

RUTA_PROCESSED = os.path.join("data","processed")

def carga_datos_maestros():
    ruta_archivo = os.path.join(RUTA_PROCESSED, "master_powerbi.csv")
    if not os.path.exists(ruta_archivo):
        raise FileExistsError(f"⚠️ No se encontró lla tabla maestra en: {ruta_archivo}.")
    return pd.read_csv(ruta_archivo)

def ejecucion_auditoria_fase3():

    # 1. Carga de datos de forma segura mediante una copia
    df_master = carga_datos_maestros()
    df = df_master.copy()

    print("=" * 80)
    print("⚖ FASE 3: AUDITORÍA ÉTICA, SESGOS Y PRIVACIDAD - GOALMETRICS")
    print("=" * 80)

    # 2. Análisis de Sesgo Geográfico
    print("\n🌍 1. DETECCIÓN DE SESGOS GEOGRÁFICOS (Dominio de países)")
    top_paises = df['country'].value_counts(normalize = True).head(5) * 100
    print("   • Porcentaje de partidos disputados por país (Top 5)")
    for pais, porc in top_paises.items():
        print(f"   - {pais}: {porc:.2f}%")
    print("   📣 Reflexión: Si el Top 5 acumula un porcentaje muy alto, el modelo tendrá un sesgo eurocentrista o regional.")

    # 3. Análisis de Representatividad (Contexto de los partidos)
    print("\n🏆 2. AUDITORÍA DE REPRESENTATIVIDAD (Peso de Torneos")
    total_partidos = len(df)
    amistosos = len(df[df['tournament'].str.lower() == 'friendly'])
    porc_amistosos = (amistosos / total_partidos) * 100
    print(f"   • Partidos Amistosos analizados: {amistosos} ({porc_amistosos:.2f}%)")
    print(f"   • Partidos Oficiales analizados: {total_partidos - amistosos} ({(100 - porc_amistosos):.2f}%)")
    print("   📣 Reflexión: Los partidos  amistosos pueden alterar las métricas de rendimiento real al no tener cáracter competitivo.")

    # 4. Verificación de Privacidad (GDPR / Cumplimiento Normativo)
    print("\n🔒 CONTROL DE PRIVACIDAD Y DATOS SENSIBLES")
    
    #Se busca si existen columnas que expongan datos personales de los usuarios o árbitros sin anonimizar
    columnas_sensibles = ['referee', 'referee_name', 'attendance_emails', 'player_id']
    encontradas = [col for col in columnas_sensibles if col in df.columns]

    if not encontradas:
        print("   • Estado: ✅ Éxito. El dataset no expone columnas críticas con datos personales directos.")
    else:
        print(f"   • Estado: ⚠ Alerta de Privacidad. Se detectaron columnas con riesgo: {encontradas}")
        print("    Sugerencia: Se recomienda anonimizar o eliminar estas variables en producción.")

    print("\n" + "=" * 80)

if __name__ == "__main__":
    ejecucion_auditoria_fase3()