import sqlite3
from pathlib import Path
import pandas as pd
import logging

logger = logging.getLogger('pipeline.exportar')


def exportar(df: pd.DataFrame, carpeta: str = 'output') -> None:
    destino = Path(carpeta)
    destino.mkdir(exist_ok=True)

    df.to_parquet(destino / 'posts_enriquecidos.parquet', index=False)
    df.to_csv(destino / 'posts_enriquecidos.csv', index=False)
    
    with sqlite3.connect(destino / 'posts.db') as conn:
        df.to_sql('posts_enriquecidos', conn, if_exists='replace', index=False)
        conn.commit()      
    
    logger.info(f"Exportados {len(df)} posts a {destino}/ (parquet, csv, sqlite)")