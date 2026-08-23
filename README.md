# Lab Semana 1 - <Titanic>
- Persona A: <Mateo Velastegui>
- Persona B: <Elias Pogo>
- Dataset: <raw.githubusercontent.com/datascience
dojo/datasets/master/titanic.csv>
- Tarea: <clasificacion> Variable objetivo: <Survived>
## Como correr
uv sync
uv run pytest -q
uv run python main.py
## Hallazgos
¿por qué uv sync puede reconstruir el entorno aunque .venv/ no esté versionado en el repositorio? ¿Qué archivo se
lo permite y qué guarda exactamente ese archivo? Dos líneas bastan.
Debido a que toda la información del entorno se encuentra en el uv.lock, lo que permite al uv.sync recrear el .venv

## Decisiones de limpieza
Eliminar columna Cabin debido a un 77% de nulos: no se puede imputar de forma confiable un porcentaje tan alto de datos faltantes, así que se elimina la columna en vez de las filas.
La columna Age (≈20% de nulos) se imputa con la mediana, por ser una variable numérica y más robusta a valores atípicos que la media.
La columna Embarked (≈0.2% de nulos, solo 2 filas) se imputa con la moda, por ser una variable categórica.
