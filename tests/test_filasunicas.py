import pandas as pd
import pytest

from src.carga import limpiar


@pytest.fixture
def df_con_duplicados():
    fila = {
        "Name": ["ana"],
        "Age": [30.0],
        "Embarked": ["s"],
        "Cabin": ["c85"],
    }
    return pd.DataFrame({col: valores * 2 for col, valores in fila.items()})


def test_limpiar_elimina_filas_duplicadas(df_con_duplicados):
    assert len(df_con_duplicados) == 2

    df_limpio = limpiar(df_con_duplicados)

    assert len(df_limpio) == 1
