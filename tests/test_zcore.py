import numpy as np
import pandas as pd

from src.carga import zscore


def test_zscore_cada_columna_media_cero_desviacion_uno():
    df = pd.DataFrame({
        "Age": [22.0, 38.0, 26.0, 35.0, 28.0],
        "Fare": [7.25, 71.28, 7.92, 53.1, 8.05],
    })

    df_z = zscore(df)

    assert np.allclose(df_z.mean(), 0, atol=1e-8)
    assert np.allclose(df_z.std(), 1, atol=1e-8)
