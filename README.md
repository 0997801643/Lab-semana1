
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
  
## Hallazgos A
¿por qué uv sync puede reconstruir el entorno aunque .venv/ no esté versionado en el repositorio? ¿Qué archivo se
lo permite y qué guarda exactamente ese archivo? Dos líneas bastan.
Debido a que toda la información del entorno se encuentra en el uv.lock, lo que permite al uv.sync recrear el .venv
¿qué diferencia hay entre correr pytest a secas y uv run pytest?
Que al correr pytest a secas se referencia de lo que tengas activo en el PATH del terminal ya que estaria por fuera del entorno virtual, al correr uv run pytest se interpreta las versiones exactas gracias al .venv del proyecto y las versiones definidas en el uv.lock 

## Decisiones de limpieza
Eliminar columna Cabin debido a un 77% de nulos: no se puede imputar de forma confiable un porcentaje tan alto de datos faltantes, así que se elimina la columna en vez de las filas.
La columna Age (≈20% de nulos) se imputa con la mediana, por ser una variable numérica y más robusta a valores atípicos que la media.
La columna Embarked (≈0.2% de nulos, solo 2 filas) se imputa con la moda, por ser una variable categórica.

## Hallazgos B
(B) Al trabajar independientemente las funciones de análisis se realizó varios hallazgos

- Si en la carpeta src. o cualquiera que se vaya a usar como librería no está el archivo __init__.py el IDE no va a reconocer esta carpeta como librería y por lo tanto dará un error.
- Se debe tener en cuenta el tipo de variable y sus dimensiones a la hora de trabajar cono las funciones, en este caso de analysis.py
- Usar pytest es una de las mejores maneras de probar las funciones que se crean, lo mejor de todo es que es automático y también nos da un feedback en caso de tener un error, por lo cual es más facil corregir los errores.
