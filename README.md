# Predicción de la Producción de Café en Cartago, Valle del Cauca

## 1. Nombre del proyecto

**Predicción de la Producción de Café en Cartago, Valle del Cauca**

## 2. Descripción del proyecto

Este proyecto de Inteligencia Artificial tiene como propósito analizar el comportamiento histórico de la producción de café en el municipio de Cartago, Valle del Cauca.

Se utilizan datos agrícolas reales para realizar un proceso de carga, limpieza, organización, análisis exploratorio y visualización mediante Python.

El análisis realizado en este primer avance permitirá establecer una base para desarrollar posteriormente un modelo capaz de predecir la producción de café.

## 3. Problema

La producción de café puede presentar variaciones importantes entre diferentes años debido a cambios en las áreas sembradas, áreas cosechadas y otros factores relacionados con la actividad agrícola.

En Cartago, Valle del Cauca, contar con una estimación de la producción futura puede ser útil para apoyar la planificación de las actividades relacionadas con la producción agrícola.

Por esta razón, este proyecto busca analizar los datos históricos de producción de café de Cartago y utilizar esta información como base para desarrollar posteriormente un sistema que permita realizar predicciones.

## 4. Objetivo general

Desarrollar una base de análisis de datos que permita posteriormente construir un sistema capaz de predecir la producción de café en Cartago, Valle del Cauca, utilizando información histórica agrícola.

### Objetivos específicos

- Obtener y organizar datos reales de producción agrícola.
- Identificar los registros correspondientes al cultivo de café.
- Filtrar los datos correspondientes al municipio de Cartago.
- Manipular los datos utilizando Python.
- Convertir los registros procesados en una lista de diccionarios.
- Calcular estadísticas utilizando NumPy.
- Representar gráficamente la producción histórica utilizando Matplotlib.
- Identificar patrones y hallazgos importantes en los datos.
- Utilizar los resultados como base para desarrollar posteriormente un modelo de Machine Learning.


# 5. Datos utilizados

Para el proyecto se utiliza información agrícola real del Valle del Cauca.

El conjunto de datos contiene información histórica de diferentes cultivos y municipios del departamento.

Para este proyecto se seleccionaron los registros correspondientes al cultivo de **café** y posteriormente se filtraron los registros del municipio de **Cartago**.

### Fuente de los datos

**Gobernación del Valle del Cauca – Datos abiertos**

Dataset:
**Consolidado agrícola por municipios de los cultivos permanentes del Valle del Cauca**

El conjunto de datos contiene información sobre cultivos permanentes registrados en diferentes municipios del departamento.

## 6. Estructura de los datos

El archivo utilizado es un archivo **CSV**.

Entre las principales variables utilizadas se encuentran:

| Variable | Descripción |
|---|---|
| Año | Año del registro agrícola |
| Municipio | Municipio donde se registra el cultivo |
| Cultivo | Tipo de cultivo |
| Hectareas_sembradas | Área sembrada en hectáreas |
| Hectareas_cosechadas | Área cosechada en hectáreas |
| Produccion_toneladas | Producción obtenida en toneladas |
| Rendimiento_toneladas/hectareas | Rendimiento de producción por hectárea |


## 7. Cantidad de datos

Después de realizar la carga y filtrado de los datos se obtuvieron:

- **969 registros de café** en el Valle del Cauca.
- **25 registros de café en Cartago**.
- Periodo analizado en Cartago: **2000 - 2024**.
- El archivo contiene **11 columnas**.


# 8. Tecnologías utilizadas

El proyecto utiliza las siguientes herramientas:

- **Python:** lenguaje principal del proyecto.
- **Pandas:** carga, limpieza y manipulación de datos.
- **NumPy:** cálculo de estadísticas.
- **Matplotlib:** creación de gráficos.
- **Scikit-learn:** desarrollo posterior del modelo de Machine Learning.
- **Git:** control de versiones.
- **GitHub:** almacenamiento y seguimiento del proyecto.
- **Docker:** configuración del entorno de ejecución.



# 9. Carga del archivo CSV

El archivo CSV es cargado utilizando Pandas.

Ejemplo utilizado en el proyecto:

```python
import pandas as pd

datos = pd.read_csv(
    "data/cafe_valle_limpio.csv",
    sep=";",
    encoding="utf-8"
)
```


# 10. Filtrado de los datos

Después de cargar el archivo CSV se identificaron los registros correspondientes al cultivo de café.

Se utilizaron los siguientes criterios:
- **Cultivo:** Café.
- **Municipio:** Cartago.
- **Periodo:** 2000 a 2024.

Para seleccionar los registros de café se utilizó:

```python
cafe = datos[
    datos["Cultivo"].astype(str).str.contains(
        "Caf",
        case=False,
        na=False
    )
].copy()
```

Posteriormente se filtraron los registros de Cartago:

```python
cartago = cafe[
    cafe["Municipio"].astype(str).str.strip() == "Cartago"
].copy()
```

Como resultado se obtuvieron 25 registros históricos de producción de café en Cartago.


# 11. Lista de diccionarios

Como parte del manejo de estructuras de datos en Python, los registros procesados de Cartago fueron convertidos en una lista de diccionarios.

Se utilizó:

```python
lista_diccionarios = cartago.to_dict(
    orient="records"
)
```

La lista contiene 25 diccionarios, correspondientes a los registros históricos de producción de café de Cartago.

Cada diccionario representa un registro y contiene información como:

```json
{
    "Año": 2000,
    "Municipio": "Cartago",
    "Cultivo": "Café",
    "Hectareas_sembradas": 1301.0,
    "Hectareas_cosechadas": 1301.0,
    "Produccion_toneladas": 1431.0
}
```

Esto permite trabajar los datos utilizando estructuras propias de Python.


# 12. Función creada

Para cumplir con el manejo de funciones en Python, se creó una función propia llamada `calcular_estadisticas`.

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

La función recibe una lista de valores de producción y utiliza NumPy para calcular:
- Producción promedio.
- Producción máxima.
- Producción mínima.
- Desviación estándar.

La función es utilizada dentro del análisis exploratorio del proyecto.

# 13. Análisis exploratorio con NumPy

Para analizar el comportamiento de la producción de café en Cartago se utilizó la biblioteca NumPy.

Las funciones utilizadas fueron:
- `np.mean()`
- `np.max()`
- `np.min()`
- `np.std()`

Los resultados obtenidos fueron:

| Estadística | Resultado |
| :--- | :--- |
| **Producción promedio** | 385.50 toneladas |
| **Producción máxima** | 1431.00 toneladas |
| **Producción mínima** | 80.00 toneladas |
| **Desviación estándar** | 272.18 toneladas |

### Interpretación
La producción promedio durante el periodo analizado fue de 385.50 toneladas. 

La desviación estándar de 272.18 toneladas indica que existe una variación considerable entre los diferentes registros de producción.


# 14. Visualización con Matplotlib

Para observar visualmente el comportamiento de la producción histórica se utilizó la biblioteca Matplotlib.

El gráfico representa la producción de café de Cartago entre los años 2000 y 2024.

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
```

El gráfico se guarda automáticamente en: `data/eda_cartago_produccion.png`



# 15. Hallazgos principales

A partir del análisis exploratorio se identificaron los siguientes hallazgos:

- **Hallazgo 1: Producción máxima**
  La mayor producción registrada en Cartago fue en el año 2000, con **1431 toneladas** de café.
- **Hallazgo 2: Producción mínima**
  La menor producción registrada fue en el año 2023, con **80 toneladas** de café.

### Interpretación
La diferencia entre la producción máxima y mínima muestra que la producción de café presenta variaciones importantes entre los años analizados. 

Este comportamiento demuestra que existe información histórica que puede ser utilizada posteriormente para desarrollar un modelo de predicción.


# 16. Script principal del análisis

El análisis exploratorio se encuentra en: `src/eda.py`

Este archivo realiza las siguientes actividades:
- Carga el archivo CSV.
- Identifica los registros de café.
- Filtra los registros de Cartago.
- Convierte los datos numéricos.
- Crea una lista de diccionarios.
- Utiliza una función propia.
- Calcula estadísticas con NumPy.
- Identifica los valores máximo y mínimo.
- Genera un gráfico con Matplotlib.
- Guarda el gráfico en la carpeta data.

Para ejecutar el análisis use el comando:
```bash
python src/eda.py
```

# 17. Estructura del proyecto

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
