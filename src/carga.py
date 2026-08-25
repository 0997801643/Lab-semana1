from pathlib import Path

import numpy as np
import pandas as pd

URL = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"


def cargar(url, na_values=None):
    return pd.read_csv(url, na_values=na_values)


def reporte_nulos(df: pd.DataFrame) -> pd.DataFrame:
    conteo = df.isnull().sum()
    porcentaje = (conteo / len(df)) * 100
    return (
        pd.DataFrame({"nulos": conteo, "porcentaje": porcentaje})
        .sort_values("nulos", ascending=False)
    )


def limpiar(df: pd.DataFrame) -> pd.DataFrame:
    df = df.replace([np.inf, -np.inf], np.nan)
    df = df.drop_duplicates()

    columnas_texto = df.select_dtypes(include=["object", "str"]).columns
    df[columnas_texto] = df[columnas_texto].apply(lambda col: col.str.strip().str.lower())

    #Cabin: 77% de nulos, se elimina la columna (no se puede imputar de forma confiable)
    df = df.drop(columns=["Cabin"])
    #Age: numerica, se imputa con la mediana (robusta a outliers)
    df["Age"] = df["Age"].fillna(df["Age"].median())
    #Embarked: categorica con <1% de nulos, se imputa con la moda
    df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

    return df.reset_index(drop=True)


def guardar(df: pd.DataFrame, ruta: str) -> None:
    df.to_parquet(ruta)


def zscore(df: pd.DataFrame) -> pd.DataFrame:
    numericas = df.select_dtypes(include="number")
    return (numericas - numericas.mean()) / numericas.std()


if __name__ == "__main__":
    df = cargar(URL, na_values=["?", -200])
    print(reporte_nulos(df))

    df = limpiar(df)
    print("nulos por columna despues de la limpieza:")
    print(df.isna().sum())

    Path("data").mkdir(exist_ok=True)
    guardar(df, "data/limpio.parquet")
