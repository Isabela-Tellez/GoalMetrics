<div align="center">
  <img src="assets/LogoNoFondo.png" alt="GoalMetrics Logo" width="420"/>
  <h1>GoalMetrics</h1>
  <p><b>Dashboard de Analítica para el Mundial FIFA · Histórico 1872–2024</b></p>

  <p style="line-height: 0;">
    <img src="https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
    <img src="https://img.shields.io/badge/Pandas-2.0-150458?style=for-the-badge&logo=pandas&logoColor=white"/>
    <img src="https://img.shields.io/badge/NumPy-1.24-013243?style=for-the-badge&logo=numpy&logoColor=white"/>
    <img src="https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white"/>
    <img src="https://img.shields.io/badge/VS_Code-Editor-007ACC?style=for-the-badge&logo=visual-studio-code&logoColor=white"/>
    <img src="https://img.shields.io/badge/Git-VCS-F05032?style=for-the-badge&logo=git&logoColor=white"/>
  </p>

  <p style="line-height: 0;">
    <img src="https://img.shields.io/badge/Madrid-121011?style=for-the-badge&logo=periscope&logoColor=white"/>
    <img src="https://img.shields.io/badge/Estado-Activo-00C5A4?style=for-the-badge"/>
    <img src="https://img.shields.io/badge/Versión-1.0.0-15315B?style=for-the-badge"/>
  </p>
</div>

---

## Fuente de Datos

**Dataset histórico:** [International football results from 1872 to 2026](https://www.kaggle.com/datasets/martj42/international-football-results-from-1872-to-2017?select=goalscorers.csv). Variables numéricas: `home_score`, `away_score` (marcadores), `minute` (tiempo de evento). Variables categóricas: `team`, `scorer`, `tournament`, `city`, `country`. Variables booleanas: `neutral`, `own_goal`, `penalty`.

Registro histórico de más de 46,000 partidos internacionales de fútbol masculino. Este dataset, mantenido por Mart Jürisoo, se actualiza regularmente para incluir los encuentros más recientes a nivel global.

> Los CSVs originales no se incluyen en el repositorio.

<div align="center">

| Archivo | Contenido |
| :--- | :--- |
| **`results.csv`** | Marcadores, sedes, países y torneos. |
| **`goalscorers.csv`** | Detalles por minuto, goleadores y tipos de anotación. |
| **`shootouts.csv`** | Resultados históricos de tandas de penaltis. |

</div>

---

## Descripción General

*GoalMetrics* es una plataforma de analítica interactiva diseñada para explorar la historia y evolución del fútbol internacional. A través de un análisis profundo de más de 46,000 partidos disputados entre 1872 y 2024, la herramienta permite a entusiastas y analistas deportivos visualizar patrones de rendimiento, eficacia goleadora y la dinámica de las tandas de penaltis a lo largo de más de un siglo de historia.

- **Rendimiento Táctico:** Evaluar la eficacia ofensiva y defensiva de las selecciones mediante el análisis granular de goleadores y minutos de anotación.

- **Evolución del Juego:** Detectar tendencias en el estilo de juego, efectividad de penaltis y patrones de resultados según el torneo y la sede.

- **Inteligencia de Datos:** Transformar registros históricos crudos en insights accionables, permitiendo comparativas históricas entre eras futbolísticas distintas.

---

## Tabs del Dashboard
<div align="center">

| Tab | Pregunta de negocio | Salida clave |
|:---|:---|:---|
| 📈 Visión Histórica | ¿Cómo ha evolucionado el fútbol desde 1872? | Tendencia de goles, crecimiento de torneos |
| ⚽ Eficacia Goleadora | ¿Quiénes son los máximos anotadores? | Ranking de goleadores, análisis de penaltis |
| 🏆 Análisis de Torneos | ¿Qué torneos registran mayor volumen? | Comparativa media de goles, top sedes |
| 🌍 Performance por País | ¿Qué naciones dominan históricamente? | Ranking ofensivo/defensivo, local vs visita |
| 🔍 Match & Penalty Explorer | ¿Qué partidos fueron más explosivos? | Tabla filtrable por marcador y tandas |
| 📊 Deep Insights | ¿Qué patrones marcan la historia? | Mapa de calor año/fase, frecuencia goleadora |

</div>

---

### KPIs Principales
<div align="center">

| KPI | Descripción |
|:---|:---|
| ⚽ Total Partidos | Número total de encuentros según los filtros aplicados |
| 🥅 Promedio de Goles | Media de goles anotados por partido |
| 🎯 Máximo Anotador | Jugador con mayor cantidad de goles registrados |
| 🛡️ Tandas de Penaltis | Total de partidos decididos desde el punto de penalti |
| 🔥 Diferencia Máxima | Victoria con el mayor margen de goles del periodo |

</div>

---

## Detalle de cada tab

<details>
<summary><strong>🏠 Inicio</strong></summary>

- **Cabecera** — Presentación visual de la plataforma GoalMetrics con branding institucional.
- **KPIs Globales** — Panel superior con 4 tarjetas de datos clave (Total partidos, países participantes y promedios de goles).
- **AI Insights** — Panel de inteligencia artificial que resume patrones automáticos detectados en el dataset mediante utils.py.
- **Resumen Ejecutivo** — Descripción narrativa del alcance histórico del proyecto y la capacidad de análisis de tendencias.
- **Informe Inteligente** — Funcionalidad bajo demanda que genera un reporte ejecutivo detallado sobre el rendimiento histórico.
- **Análisis Comparativo (WinRate)** — Procesamiento de datos de selecciones que calcula y visualiza un ranking de victorias mediante tarjetas interactivas con banderas.
</details>

<details>
<summary><strong>📅 Evolución</strong></summary>

- **Evolución de goles por década** — Gráfico de línea histórica con media móvil, destacando la transición en la eficacia goleadora y la estabilización táctica del siglo XXI.
- **Dominio de Victorias Locales** — Gráfico de tendencia temporal que cuantifica la ventaja competitiva de la localía, identificando décadas de mayor incidencia en el resultado para el equipo anfitrión.
</details>

<details>
<summary><strong>⚽ Resultados</strong></summary>

- **Distribución de localía** — Gráfico comparativo que cuantifica la ventaja histórica del equipo anfitrión, analizando la frecuencia de victorias, empates y derrotas.
- **Correlación de marcadores** — Matriz de densidad de resultados que evalúa la relación estadística entre los goles locales y visitantes, identificando patrones de paridad o dominancia.
</details>

<details>
<summary><strong>🔍 Sesgos</strong></summary>

- **Ventaja de localía** — Gráfico de área temporal que mide la variación de goles locales vs. visitantes, evaluando el impacto del factor cancha en la integridad competitiva.
- **Distribución de anomalías** — Diagrama de burbujas que destaca resultados extremos frente a la media, permitiendo identificar hitos históricos o errores de registro.
- **Ranking de equipos** — Gráfico comparativo de frecuencias históricas que expone qué naciones dominan el dataset y posibles sesgos de recopilación de datos.
</details>

<details>
<summary><strong>🎯 Recomendaciones</strong></summary>

- **Segmentación temporal** — Guía estratégica para aplicar filtros por décadas, permitiendo ajustar los modelos de predicción a la evolución táctica del juego.
- **Factor localía** — Directriz técnica para integrar la ventaja de campo como variable crítica y ponderada en cualquier algoritmo de probabilidades.
- **Enriquecimiento de datos** — Hoja de ruta para la escalabilidad, proponiendo la integración de rankings FIFA y factores externos para maximizar la precisión predictiva.
</details>

<details>
<summary><strong>📌 Conclusiones</strong></summary>

- **Aprendizajes clave** — Síntesis estratégica sobre el impacto histórico de la localía, la naturaleza de los sesgos en los registros y la evolución táctica global.
- **Roadmap futuro** — Visión de escalabilidad orientada a la implementación de modelos predictivos, integración de variables externas y análisis geográficos granulares.
</details>

---

## Instalación Local
```bash

# 1. Clonación el repositorio
git clone https://github.com/Isabela-Tellez/GoalMetrics.git
cd GOALMETRICS

# 2. Creación y activación del entorno virtual
python -m venv venv
venv\Scripts\activate         # Windows
source venv/bin/activate      # macOS / Linux

# 3. Instalación de dependencias
pip install -r requirements.txt

# 4. Lanzar la app
streamlit run app.py
```

---

<details>
<summary><strong>Estructura del Proyecto</strong></summary>

```
GoalMetrics/
├── assets/
|   |── logo.jpeg
|   └── LogoNoFondo.png                  # Elementos visuales
├── data/
│   ├── processed/
|   |   └── master_dataset.csv           # CSV conjunto listo para el dashboard (results, goalscorers, shootouts)
│   └── raw/
|       ├── goalscorers.csv              # CSV Detalle granular de eventos de gol, incluyendo minuto y tipo de anotación
|       ├── results.csv                  # CSV Histórico global de partidos con marcadores, sedes y fechas
|       └── shootuts.csv                 # CSV Registro de resoluciones de partidos desde el punto de penalti
├── src/
│   ├── __init__.py
|   ├── fase0_diagnostico.py             # Diagnóstico, limpieza inicial y detección de valores atípicos en datasets de fútbol
│   ├── fase1_analisis.py                # Automatiza la limpieza, cálculo de métricas descriptivas y validación de hipótesis
│   ├── fase2_estadistica.py             # Genera gráficos interactivos, analizando tendencias históricas, localía, dominio de equipos y valores atípicos
|   ├── fase3_sesgos                     # Audita sesgos estadísticos y patrones de juego para identificar anomalías y desequilibrios
│   ├── utils.py                         # Helpers: formateo, AI Insights, selectores
│   └── pages/                           # Componentes de renderizado por pestaña
│       ├── __init__.py
│       ├── home.py                      # Tab 1: Inicio y KPIs
│       ├── evolution.py                 # Tab 2: Tendencias temporales
│       ├── results.py                   # Tab 3: Performance y marcadores
│       ├── governance.py                # Tab 4: Análisis de sesgos
│       ├── recommendations.py           # Tab 5: Guía estratégica
│       └── conclusions.py               # Tab 6: Síntesis y roadmap
|── styles
|   └── global.css                       # Hoja de estilos centralizada
├── app.py                               # Entrypoint principal (main)
├── .gitignore                           # Excluye data/raw/, __pycache__/, .env
├── requirements.txt                     # Dependencias fijadas (streamlit, pandas, plotly, etc.)
└── README.md                            # Documentación del proyecto
```
</details>

<details>
<summary><strong>Stack Tecnológico y Datos</strong></summary>

### Stack

<div align="center">

| Capa | Tecnología | Versión |
|------|-----------|---------|
| Framework UI | [Streamlit](https://streamlit.io/) | 1.58.0 |
| Visualizaciones | [Plotly](https://plotly.com/python/) | 6.8.0 |
| Procesamiento de datos | [Pandas](https://pandas.pydata.org) | 3.0.3 |
| Álgebra numérica | [NumPy](https://numpy.org) | 2.4.6 |
| CI/CD | GitHub Actions → GitHub Pages | — |

</div>

### Esquema de datos

**Fuente histórica:** [International football results from 1872 to 2026]([https://www.kaggle.com/datasets/piterfm/fifa-football-world-cup](https://www.kaggle.com/datasets/martj42/international-football-results-from-1872-to-2017?select=goalscorers.csv))

<div align="center">

| Archivo | Registros | Columnas clave |
|---------|-----------|----------------|
| `results.csv` | 46,000+ | `date`, `home_team`, `away_team`, `home_score`, `away_score`, `attendance` |
| `goalscorers.csv` | 44,000+ | `date`, `home_team`, `team`, `scorer`, `minute` |
| `shootouts.csv` | 600+ | `date`, `home_team`, `winner`, `first_shooter` |
| `master_dataset.csv` | 46,000+ | Unión relacional de las fuentes con variables calculadas (`decade`, `total_goals`, `resultado_match`)|

</div>

</details>

---

## Licencia

Este proyecto es de uso interno / analítico. Los datos históricos históricos de fútbol de Kaggle se utilizan con fines educativos y analíticos.

---

<div align="center">
  Movida por la pasión y la fiebre del fútbol por <a href="https://github.com/Isabela-Tellez">Isabela-Tellez</a>
</div>
