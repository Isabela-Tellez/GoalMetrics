<div align="center">

# GoalMetrics - Analítica de Fútbol Internacional

<img src="assets/LogoNoFondo.png" alt="GoalMetrics Logo" width="420"/>

<br><br>

![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-2.0-150458?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-1.24-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Git](https://img.shields.io/badge/Git-VCS-F05032?style=for-the-badge&logo=git&logoColor=white)

<br>

![Ubicación](https://img.shields.io/badge/Madrid-121011?style=for-the-badge&logo=periscope&logoColor=white)
![Estado](https://img.shields.io/badge/Estado-Activo-00C5A4?style=for-the-badge)
![Versión](https://img.shields.io/badge/Versión-1.0.0-15315B?style=for-the-badge)

</div>

---

## 🔍 Reporte de Auditoría inicial (Fase 0 - Sanity Check)
Tras ejecutar el motor de diagnóstico profundo sobre los datos brutos ('data/raw'), se han extraído los siguientes hallazgos críticos e historias iniciales:

* **⚽ 'results.csv' (47,126 filas | 9 columnas)**
    * **Calidad:** Se detectaron 15 registros corruptos sin nombre de equipo ('home_team'/'away_team') y 51 partidos sin marcador númerico ('home_score'/'away_score').
    * **Outliers:** El método IQR detecta 6,059 partidos atípicos en casa y 661 como visitante (Marcadores fuera del rango tradicional). El análisis Z-Score ($|Z| > 3$) aisla con precisión para el negocio del fútbol, aislando goleadas extremas históricas (585 partidos en casa y 661 fuera).
    * **Storytelling:** Los datos revelan que 'brazil' (600) y 'argentina' (585) dominan la localía histórica, pero 'united states' es el mayor anfitrión global con 1,353 partidos disputados. Los partidos 'friendly' (17,902) duplican a las eliminatorias mundialistas (8,052).

* **🏃🏻‍♂️ 'goalscorers.csv' (44,110 filas| 8 columnas)**
    * **Integridad:** Se detectaron **119 filas duplicadas** quq deben ser purgadas para no inflar las estadísticas.
    * **Nulos:** Existen 50 goles sin autor ('scorer') y 263 registros sin el minuto exacto del gol ('minute').
    * **Outliers:** 0 atípicos en la columna 'minute' (Rango conherente de 1 a 122 minutos en prórrogas).
    * **Storytelling:** Los datos coronan a 'cristiano ronaldo' con 111 goles en el dataset, imponiéndose estadísticamente sobre 'robert lewandowski' (62) y 'lionel messi' (54). 

* **🎯 'shootouts.csv' (636 filas | 5 columnas)**
    * **Estado:** No representa duplicados. Las variables de los equipos y el ganador ('winner') están 100% integros.
    * **Nulos:** La columna 'first_shooter' tiene 414 nulos estructurales por falta de registro en trasmisiones antiguas.
    * **Storytelling:** 'south korea' aparece como una de las selecciones con mayor peso histórico y frecuencia en el drama de las tandas de penaltis.

---

## 📈 Reporte de Análisis Estadístico (Fase 1)
Tras ejecutar el motor estádistico en 'src/fase1_analisis.py', los datos brutos han sido transformados en las siguientes conclusiones e historias clave:

* **📊 Análisis Descriptivo:** El partido promedio tiene 2.94 goles (mediana de 3.0), concentrados en marcadores cortos pero con un sesgo a la derecha debido a goleadas atípicas aisladas.
* **⏳ Segentación por Épocas:** El gol tocó fondo en los 80 (2.52 goles/partido) y repuntó en los 2000 (2.80), destacando que en los 90/2000 la mediana en campos neutrales subió a (3.0).
* **🔗 Análisis de factores:** Los campos neutrales promedian más goles (3.05) que los de localía real (2.91), y la probabilidad de ver > 4 goles es casi idéntica en amistosos (128.46%) que en oficiales (19.19%).
* **🎯 Validación de hipótesis:** Se confirma la ventaja en casa (local gana el 49.04% vs 28.23% visitante), pero el test ANOVA (P-Value: 0.3758) demuestra que el torneo no influye en el promedio global. 