# ⚽ GoalMetrics - Analítica de Fútbol Internacional

<p align = "center">
    <img src = "assets/logo.jpeg" alt = "GoalMetrics Logo" width = "200"/>
</p>

![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-2.0-150458?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-1.24-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Git](https://img.shields.io/badge/Git-VCS-F05032?style=for-the-badge&logo=git&logoColor=white)

---

![Ubicación](https://img.shields.io/badge/Madrid-121011?style=for-the-badge&logo=periscope&logoColor=white)
![Estado](https://img.shields.io/badge/Estado-Activo-00C5A4?style=for-the-badge)
![Versión](https://img.shields.io/badge/Versión-1.0.0-15315B?style=for-the-badge)

--- 

## 🔍 Reporte de Auditoría inicial (Fase 0 - Sanity Check)
Tras ejecutar el motor de diagnóstico profundo sobre los datos brutos ('data/raw'), se han extraído los siguientes hallazgos críticos que justifican su limpieza:

* **'results.csv' (47,126 filas | 9 columnas)**
    * **Calidad:** Se detectaron 15 registros corruptos sin nombre de equipo ('home_team'/'away_team') y 51 partidos sin marcador númerico ('home_score'/'away_score').
    * **Outliers:** El método IQR detecta 6,059 partidos atípicos (Se considera anomalía cualquier marcador mayor a 3 goles). El método Z-Score (|Z| > 3) es más preciso para el negocio del fútbol, aislando 585 goleadas extremas históricas.

* **'goalscorers.csv' (44,110 filas| 8 columnas)**
    * **Integridad:** Se detectaron **119 filas duplicadas** que deben ser purgadas.
    * **Nulos:** Existen 50 goles sin autor ('scorer') y 263 registros si el minuto exacto del gol ('minute').

* **'shootouts.csv' (636 filas | 5 columnas)**
    * **Estado:** No representa duplicados. La columna 'first_shooter' tiene nulos estructurales por falta de registro histórico, pero las variables core de los partidos y el ganador ('winner') están 100% íntegras.