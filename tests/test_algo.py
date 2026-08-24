# tests/test_ejemplo.py
import numpy as np
import pandas as pd
import pytest

from src.analysis import (
    filtrar,
    recta_minimos_cuadrados,
    resumen_por_grupo,
    top_k,
    zscore,
)


def test_filtrar_deja_solo_los_mayores():
    # 1. PREPARAR: datos de entrada que ustedes controlan
    df = pd.DataFrame({"edad": [10, 25, 40]})
    # 2. EJECUTAR: llamar a la funcion que se quiere probar
    resultado = filtrar(df, "edad", 20)
    # 3. VERIFICAR: comparar contra lo que deberia salir
    assert len(resultado) == 2
    assert resultado["edad"].min() > 20, "No es mayor de 20"

@pytest.fixture # <- df_mini Reutilizable en varios tests
def df_mini():
    return pd.DataFrame({
        "grupo": ["a", "a", "b", "b"],
        "valor": [10.0, 20.0, 30.0, 40.0],   
    })

def test_resumen_por_grupo_calcula_la_media(df_mini):
    r = resumen_por_grupo(df_mini, "grupo", ["valor"])
    assert r.loc["a", ("valor", "mean")] == pytest.approx(15.0)# <- La media de 10 y 20 es 15

def test_zscore_tiene_media_cero(df_mini):
    z = zscore(df_mini[["valor"]].to_numpy())# <- se define una sola vez
    assert z.mean() == pytest.approx(0.0, abs=1e-9)# <- La media de los zscores es cero

def test_top_k_devuelve_los_mas_grandes(df_mini):
    r = top_k(df_mini, "valor", 2)
    assert r["valor"].min() > 20# <- El valor mínimo de los 2 más grandes debe ser mayor que 20

def test_recta_minimos_cuadrados_devuelve_coeficientes():
    x = np.array([0, 1, 2, 3])
    y = np.array([-1, 0.2, 0.9, 2.1])
    m, b = recta_minimos_cuadrados(x, y)
    assert m > 0# <- La pendiente debe ser positiva
    assert b < 0# <- El intercepto debe ser negativo