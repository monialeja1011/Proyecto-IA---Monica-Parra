# Predicción de la Producción de Café en Cartago, Valle del Cauca

## 1. Nombre del proyecto

**Predicción de la Producción de Café en Cartago, Valle del Cauca**

---

## 2. Descripción del proyecto

Este proyecto de Inteligencia Artificial tiene como propósito analizar el comportamiento histórico de la producción de café en el municipio de **Cartago, Valle del Cauca**.

Para ello se utilizan datos agrícolas reales del departamento, los cuales son cargados, limpiados, organizados y analizados mediante Python.

En este primer avance se realiza el **manejo de datos y análisis exploratorio (EDA)** utilizando listas, diccionarios, NumPy y Matplotlib. Los resultados obtenidos servirán como base para desarrollar posteriormente un modelo de Machine Learning capaz de realizar predicciones sobre la producción de café.

---

## 3. Problemática

La producción agrícola puede presentar variaciones importantes entre diferentes años. Estas variaciones pueden estar relacionadas con factores como el área sembrada, el área cosechada y las condiciones propias de la actividad agrícola.

En **Cartago, Valle del Cauca**, analizar el comportamiento histórico de la producción de café permite identificar cambios y tendencias que pueden ser utilizados como información de apoyo para la planificación de futuras cosechas.

Por esta razón, el proyecto busca analizar los datos históricos disponibles y establecer una base de información que posteriormente permita construir un sistema de **predicción de la producción de café**.

---

## 4. Objetivo general

Desarrollar una base de análisis de datos que permita posteriormente construir un sistema capaz de **predecir la producción de café en Cartago, Valle del Cauca**, utilizando información histórica agrícola.

### Objetivos específicos

* Obtener y organizar datos reales de producción agrícola.
* Identificar los registros correspondientes al cultivo de café.
* Filtrar los registros correspondientes al municipio de Cartago.
* Cargar y manipular archivos CSV utilizando Python.
* Convertir los registros procesados en una lista de diccionarios.
* Crear y utilizar una función propia en Python.
* Calcular estadísticas utilizando NumPy.
* Generar visualizaciones utilizando Matplotlib.
* Identificar hallazgos relevantes en los datos.
* Utilizar los resultados del análisis como base para desarrollar posteriormente un modelo de Machine Learning.

---

# 5. Datos utilizados

El proyecto utiliza información agrícola real del **Valle del Cauca**.

El conjunto de datos contiene información histórica de diferentes cultivos y municipios del departamento. Para este proyecto se seleccionaron los registros correspondientes al cultivo de **café** y posteriormente se filtraron los registros correspondientes al municipio de **Cartago**.

### Fuente de los datos

**Gobernación del Valle del Cauca – Datos Abiertos**

Dataset:

**Consolidado agrícola por municipios de los cultivos permanentes del Valle del Cauca**

Los datos contienen información relacionada con cultivos permanentes registrados en diferentes municipios del departamento.

---

# 6. Estructura de los datos

El archivo principal utilizado es un archivo **CSV**.

Entre las variables utilizadas en el análisis se encuentran:

| Variable                          | Descripción                            |
| --------------------------------- | -------------------------------------- |
| `Año`                             | Año del registro agrícola              |
| `Municipio`                       | Municipio donde se registra el cultivo |
| `Cultivo`                         | Tipo de cultivo                        |
| `Hectareas_sembradas`             | Área sembrada en hectáreas             |
| `Hectareas_cosechadas`            | Área cosechada en hectáreas            |
| `Produccion_toneladas`            | Producción obtenida en toneladas       |
| `Rendimiento_toneladas/hectareas` | Rendimiento de producción por hectárea |

El archivo utilizado para el análisis exploratorio es:

```text
data/cafe_valle_limpio.csv
```

---

# 7. Cantidad de datos

Después del proceso de carga y filtrado se obtuvieron los siguientes resultados:

* **969 registros** correspondientes al cultivo de café en el Valle del Cauca.
* **25 registros** correspondientes al cultivo de café en Cartago.
* Periodo analizado en Cartago: **2000 a 2024**.
* El archivo contiene **11 columnas**.

Estos datos permiten analizar el comportamiento histórico de la producción de café en el municipio.

---

# 8. Tecnologías utilizadas

El proyecto utiliza las siguientes herramientas:

* **Python:** lenguaje principal del proyecto.
* **Pandas:** carga, limpieza y manipulación de datos.
* **NumPy:** cálculo de estadísticas.
* **Matplotlib:** generación de gráficos.
* **Scikit-learn:** desarrollo posterior del modelo de Machine Learning.
* **Git:** control de versiones.
* **GitHub:** almacenamiento y seguimiento del código.
* **Docker:** configuración del entorno de ejecución.

Las principales dependencias de Python se encuentran en:

```text
requirements.txt
```

---

# 9. Carga del archivo CSV

El archivo CSV se carga utilizando Pandas.

En el análisis exploratorio se utiliza:

```python
import pandas as pd

datos = pd.read_csv(
    "data/cafe_valle_limpio.csv",
    sep=";",
    encoding="utf-8"
)
```

También se contempla la codificación `latin1` en caso de que el archivo presente problemas de codificación:

```python
try:
    datos = pd.read_csv(
        archivo,
        sep=";",
        encoding="utf-8"
    )
except UnicodeDecodeError:
    datos = pd.read_csv(
        archivo,
        sep=";",
        encoding="latin1"
    )
```

---

# 10. Filtrado de los datos

Primero se identifican los registros correspondientes al cultivo de café.

```python
cafe = datos[
    datos["Cultivo"].astype(str).str.contains(
        "Caf",
        case=False,
        na=False
    )
].copy()
```

Posteriormente se filtran los registros correspondientes al municipio de Cartago:

```python
cartago = cafe[
    cafe["Municipio"].astype(str).str.strip() == "Cartago"
].copy()
```

De esta manera se obtienen los registros históricos del cultivo de café en Cartago.

---

# 11. Lista de diccionarios

Como parte de los requisitos del proyecto, los datos procesados se convierten en una **lista de diccionarios** utilizando Pandas:

```python
lista_diccionarios = cartago.to_dict(
    orient="records"
)
```

La lista contiene los registros históricos de café correspondientes a Cartago.

Cada elemento representa un registro mediante un diccionario. Por ejemplo:

```python
{
    "Año": 2000,
    "Municipio": "Cartago",
    "Cultivo": "Café",
    "Hectareas_sembradas": 1301.0,
    "Hectareas_cosechadas": 1301.0,
    "Produccion_toneladas": 1431.0
}
```

Esta estructura permite trabajar los registros utilizando estructuras de datos propias de Python.

---

# 12. Función creada

Para el análisis se creó una función propia llamada:

```python
calcular_estadisticas()
```

La función recibe los valores de producción y utiliza NumPy para calcular diferentes estadísticas:

```python
import numpy as np

def calcular_estadisticas(producciones):
    producciones = np.array(producciones)

    estadisticas = {
        "media": np.mean(producciones),
        "maximo": np.max(producciones),
        "minimo": np.min(producciones),
        "desviacion": np.std(producciones)
    }

    return estadisticas
```

La función permite obtener:

* Promedio de producción.
* Producción máxima.
* Producción mínima.
* Desviación estándar.

Esta función es utilizada directamente en el análisis exploratorio del proyecto.

---

# 13. Análisis exploratorio de datos (EDA)

Para realizar el análisis exploratorio se utiliza **NumPy**.

Las principales funciones utilizadas son:

```python
np.mean()
np.max()
np.min()
np.std()
```

Estas funciones permiten analizar estadísticamente la columna:

```text
Produccion_toneladas
```

correspondiente a los registros de café en Cartago.

## Resultados obtenidos

| Estadística         |             Resultado |
| ------------------- | --------------------: |
| Producción promedio |  **385.50 toneladas** |
| Producción máxima   | **1431.00 toneladas** |
| Producción mínima   |   **80.00 toneladas** |
| Desviación estándar |  **272.18 toneladas** |

### Interpretación

La producción promedio registrada durante el periodo analizado fue de **385.50 toneladas**.

La producción máxima registrada fue de **1431 toneladas**, mientras que la mínima fue de **80 toneladas**.

La desviación estándar de **272.18 toneladas** muestra que existen diferencias importantes entre los valores de producción registrados durante los años analizados.

---

# 14. Visualización con Matplotlib

Para visualizar el comportamiento histórico de la producción se utiliza **Matplotlib**.

El gráfico representa la producción de café en Cartago entre los años 2000 y 2024.

El código utilizado incluye:

```python
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))

plt.plot(
    cartago["Año"],
    cartago["Produccion_toneladas"],
    marker="o",
    label="Producción de café"
)

plt.title(
    "Producción de Café en Cartago, Valle del Cauca"
)

plt.xlabel("Año")
plt.ylabel("Producción (toneladas)")

plt.grid(True)
plt.legend()

plt.tight_layout()
```

El gráfico se guarda en:

```text
data/eda_cartago_produccion.png
```

---

# 15. Hallazgos principales

A partir del análisis exploratorio se identificaron los siguientes hallazgos:

### Hallazgo 1: Producción máxima

La mayor producción registrada en los datos de Cartago corresponde al año **2000**, con:

**1431 toneladas de café.**

### Hallazgo 2: Producción mínima

La menor producción registrada corresponde al año **2023**, con:

**80 toneladas de café.**

### Interpretación

La diferencia entre el valor máximo y el mínimo evidencia una variación importante de la producción de café entre los años analizados.

Esta variación es relevante para el proyecto porque demuestra que los datos históricos contienen cambios que posteriormente pueden ser estudiados mediante técnicas de Machine Learning para desarrollar un sistema de predicción.

---

# 16. Script principal del análisis

El análisis exploratorio se encuentra principalmente en:

```text
src/eda.py
```

Este archivo realiza las siguientes actividades:

1. Carga el archivo CSV.
2. Identifica la cantidad de registros y columnas.
3. Filtra los registros correspondientes al café.
4. Filtra los registros correspondientes a Cartago.
5. Convierte las variables numéricas.
6. Convierte los registros en una lista de diccionarios.
7. Utiliza la función propia `calcular_estadisticas()`.
8. Calcula promedio, máximo y mínimo con NumPy.
9. Calcula la desviación estándar.
10. Identifica los años de mayor y menor producción.
11. Genera un gráfico con Matplotlib.
12. Guarda el gráfico en la carpeta `data`.

Para ejecutar el análisis:

```bash
python src/eda.py
```

---

# 17. Estructura del proyecto

La estructura principal del proyecto es:

```text
prediccion-cafetera/
│
├── data/
│   ├── produccion_cafetera_valle.csv
│   ├── cafe_valle_limpio.csv
│   ├── modelo_cafetero.pkl
│   ├── eda_cartago_produccion.png
│   ├── prediccion_cartago.png
│   └── produccion_cartago.png
│
├── src/
│   ├── analizar_datos.py
│   ├── eda.py
│   ├── entrenar_modelo.py
│   ├── graficar_produccion.py
│   ├── limpiar_datos.py
│   ├── main.py
│   ├── predecir.py
│   ├── preparar_datos.py
│   └── revisar_datos.py
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .dockerignore
├── .gitignore
└── README.md
```

---

# 18. Organización de los archivos principales

### Carpeta `data/`

Contiene los datos utilizados por el proyecto y los resultados gráficos generados durante el análisis.

```text
produccion_cafetera_valle.csv
```

Dataset original utilizado como fuente de información.

```text
cafe_valle_limpio.csv
```

Datos procesados utilizados para el análisis.

```text
eda_cartago_produccion.png
```

Gráfico generado durante el análisis exploratorio.

Los archivos:

```text
prediccion_cartago.png
produccion_cartago.png
modelo_cafetero.pkl
```

corresponden a trabajos complementarios y avances del proyecto relacionados con la etapa posterior de predicción.

---

# 19. Control de versiones

El proyecto utiliza **Git y GitHub** para llevar el control de versiones.

Durante el desarrollo se realizan commits para registrar avances importantes del proyecto, como:

* Organización inicial del proyecto.
* Incorporación y limpieza de los datos.
* Desarrollo del análisis exploratorio.
* Generación de estadísticas y gráficos.
* Preparación de las siguientes etapas del modelo.

El repositorio del proyecto se encuentra en GitHub:

**Proyecto-IA---Monica-Parra**

---

# 20. Ejecución del proyecto

Para ejecutar el análisis localmente se deben instalar las dependencias del proyecto.

### Instalar dependencias

```bash
pip install -r requirements.txt
```

### Ejecutar el análisis exploratorio

```bash
python src/eda.py
```

Al ejecutar el script se muestran en la terminal:

* Cantidad de registros.
* Cantidad de columnas.
* Registros de café.
* Registros de café en Cartago.
* Lista de diccionarios.
* Promedio.
* Máximo.
* Mínimo.
* Desviación estándar.
* Hallazgos principales.

También se genera el gráfico:

```text
data/eda_cartago_produccion.png
```

---

# 21. Próximos pasos

Para el siguiente corte se continuará con el desarrollo del sistema de Inteligencia Artificial.

Los próximos pasos son:

1. Preparar las variables que serán utilizadas por el modelo.
2. Seleccionar las características más relevantes de los datos.
3. Dividir los datos para entrenamiento y evaluación.
4. Entrenar un modelo de Machine Learning.
5. Evaluar el rendimiento del modelo mediante métricas.
6. Comparar los resultados obtenidos.
7. Realizar predicciones de producción de café para Cartago.
8. Mejorar el modelo a partir de los resultados obtenidos.

La etapa de análisis exploratorio desarrollada en este primer avance constituye la base para estas siguientes fases.

---

# 22. Conclusión del primer avance

En este primer avance se logró trabajar con **datos agrícolas reales**, realizar su carga y procesamiento mediante Python, filtrar la información correspondiente al cultivo de café en Cartago, convertir los registros en una lista de diccionarios y crear una función propia para el cálculo de estadísticas.

También se realizó un análisis exploratorio utilizando **NumPy** y se generó una visualización mediante **Matplotlib**.

Los resultados permitieron identificar variaciones importantes en la producción histórica de café en Cartago, proporcionando una base para continuar con la construcción del modelo de Inteligencia Artificial en el siguiente corte.
