import numpy as np


def filtrar(df, columna, umbral):
    resultado = df[df[columna] > umbral]
    return resultado

def resumen_por_grupo(df, col_grupo, cols_num):
    groupsum = df.groupby(col_grupo)[cols_num].agg(['mean','std','count'])
    return groupsum

def zscore(m):
    return (m - m.mean(axis=0)) / m.std(axis=0)

def top_k(df, columna, k):
    idx = np.argsort(df[columna].values)[-k:]
    return df.iloc[idx]

def recta_minimos_cuadrados(x, y):
    A = np.vstack([x, np.ones(len(x))]).T
    return np.linalg.lstsq(A, y)[0]