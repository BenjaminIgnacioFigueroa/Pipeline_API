import pandas as pd
import logging

logger = logging.getLogger('pipeline.validacion')


class ValidacionError(Exception):
    pass


def validar_posts(df: pd.DataFrame) -> None:
    errores = []
    
    if df.empty:
        errores.append("DataFrame vacío")
    
    columnas_requeridas = {'post_id', 'title', 'body', 'user_id', 'autor_nombre'}
    faltantes = columnas_requeridas - set(df.columns)
    if faltantes:
        errores.append(f"Columnas faltantes: {faltantes}")
    
    if errores:
        msg = "Validación fallida:\n" + "\n".join(f"  - {e}" for e in errores)
        logger.error(msg)
        raise ValidacionError(msg)
    
    duplicados = df['post_id'].duplicated().sum()
    if duplicados > 0:
        errores.append(f"{duplicados} post_id duplicados")
    
    titulos_vacios = df['title'].str.strip().eq('').sum()
    if titulos_vacios > 0:
        errores.append(f"{titulos_vacios} títulos vacíos")
    
    if 'body_length' in df.columns:
        bodies_vacios = (df['body_length'] == 0).sum()
        if bodies_vacios > 0:
            errores.append(f"{bodies_vacios} posts con body vacío")
    
    if errores:
        msg = "Validación fallida:\n" + "\n".join(f"  - {e}" for e in errores)
        logger.error(msg)
        raise ValidacionError(msg)
    
    logger.info(f"Validación exitosa: {len(df)} posts pasan todas las reglas")