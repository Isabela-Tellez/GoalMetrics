import pandas as pd
import numpy as np
from src import fase1_analisis as fase1

df_results, df_goalscorers, df_shootouts = fase1.carga_y_limpieza_datos()

# 2. Unión (Join) principal
# Unimos resultados con shootouts y goleadores por fecha y equipos
df = df_results.merge(df_shootouts, on=['date', 'home_team', 'away_team'], how='left')
df = df.merge(df_goalscorers, on=['date', 'home_team', 'away_team'], how='left')

# 3. Creación de la columna decade
df['date'] = pd.to_datetime(df['date'])
df['decade'] = (df['date'].dt.year // 10) * 10

#4. Creación de la columna goles totales
df['total_goals'] = df['home_score'] + df['away_score']

# 5. Creación de la columna resultados del partido
df['resultado_match'] = np.where(df['home_score'] > df['away_score'], 'Victoria Local',
                    np.where(df['home_score'] < df['away_score'], 'Victoria Visitante', 'Empate'))

# 6. Guardado
df.to_csv("data/processed/master_dataset.csv", index=False)