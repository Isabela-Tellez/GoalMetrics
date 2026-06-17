import pandas as pd

def generar_insights_automaticos(df):
    # Cálculo de métricas dinámicas
    total_matches = len(df)
    home_win_pct = (df['resultado_match'] == 'Victoria Local').mean() * 100
    
    # Equipo con mayor Win Rate (local, min 50 partidos)
    home_wins = df[df['resultado_match'] == 'Victoria Local'].groupby('home_team').size()
    total_home_matches = df.groupby('home_team').size()
    win_rates = (home_wins / total_home_matches * 100)
    top_team = win_rates[total_home_matches > 50].idxmax().capitalize()
    top_rate = win_rates[total_home_matches > 50].max()
    
    # Equipo con más tandas de penales ganadas
    shootouts = df[df['winner'].notnull()]
    top_shootout_team = shootouts['winner'].value_counts().idxmax()
    top_shootout_wins = shootouts['winner'].value_counts().max()
    
    # Máximo goleador
    top_scorer = df['scorer'].value_counts().idxmax()
    
    return [
        f"**Dominio Local:** {top_team} destaca con una tasa de victoria del {top_rate:.1f}% en casa.",
        f"**Especialistas:** {top_shootout_team} es el equipo con más victorias en tandas de penales ({top_shootout_wins} registros).",
        f"**Élite Goleadora:** {top_scorer} lidera el histórico de anotaciones del dataset.",
        f"**Tendencia Global:** El {home_win_pct:.1f}% de los partidos internacionales favorece al anfitrión.",
        f"**Volumen:** Analizando un total de {total_matches:,} registros históricos."
    ]