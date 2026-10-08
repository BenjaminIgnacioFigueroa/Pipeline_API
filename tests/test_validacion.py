import pandas as pd
import pytest

class ValidacionError(Exception):
    pass

def validar_posts(df):
    errores = []
    if df.empty:
        errores.append("DataFrame vacío")
    columnas_requeridas = {'post_id', 'title', 'body', 'user_id'}
    faltantes = columnas_requeridas - set(df.columns)
    if faltantes:
        errores.append(f"Columnas faltantes: {faltantes}")
    if 'post_id' in df.columns and df['post_id'].duplicated().sum() > 0:
        errores.append("Duplicados en post_id")
    if errores:
        raise ValidacionError("\n".join(errores))

def test_df_vacio_lanza_error():
    with pytest.raises(ValidacionError, match="vacío"):
        validar_posts(pd.DataFrame())

def test_columna_faltante_lanza_error():
    df = pd.DataFrame({'post_id': [1], 'title': ['A']})  
    with pytest.raises(ValidacionError, match="faltantes"):
        validar_posts(df)

def test_duplicados_lanza_error():
    df = pd.DataFrame({
        'post_id': [1, 1, 2],
        'title': ['A', 'B', 'C'],
        'body': ['x', 'y', 'z'],
        'user_id': [1, 1, 2]
    })
    with pytest.raises(ValidacionError, match="Duplicados"):
        validar_posts(df)

def test_datos_validos_no_lanza_error():
    df = pd.DataFrame({
        'post_id': [1, 2, 3],
        'title': ['A', 'B', 'C'],
        'body': ['x', 'y', 'z'],
        'user_id': [1, 2, 3]
    })
    validar_posts(df)  