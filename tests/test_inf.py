import numpy as np
import pandas as pd

from src.carga import limpiar


def test_limpiar_sin_inf_ni_nulos_en_numericas():
    df = pd.DataFrame({
        "Name": ["ana", "beto", "caro"],
        "Age": [30.0, np.inf, -np.inf],
        "Fare": [10.5, 20.0, 15.0],
        "Embarked": ["s", "c", None],
        "Cabin": ["c85", None, "e46"],
    })

    df_limpio = limpiar(df)
    columnas_numericas = df_limpio.select_dtypes(include="number")

    assert not np.isinf(columnas_numericas).to_numpy().any()
    assert not columnas_numericas.isna().to_numpy().any()
