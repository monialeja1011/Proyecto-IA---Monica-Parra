# Predicción de la Producción de Café en Cartago, Valle del Cauca

## 1. Nombre del proyecto

**Predicción de la Producción de Café en Cartago, Valle del Cauca**

---

## 2. Descripción del proyecto

Este proyecto de Inteligencia Artificial tiene como propósito analizar el comportamiento histórico de la producción de café en el municipio de **Cartago, Valle del Cauca**, y desarrollar un modelo de Machine Learning capaz de realizar estimaciones de producción.

Para ello se utilizan datos agrícolas reales del departamento del Valle del Cauca, los cuales son cargados, limpiados, organizados y analizados mediante Python.

El proyecto incluye una etapa de **análisis exploratorio de datos (EDA)** utilizando Pandas, listas, diccionarios, NumPy y Matplotlib, seguida de una etapa de **Machine Learning** utilizando Scikit-learn.

El modelo desarrollado utiliza información histórica sobre el año, las hectáreas sembradas, las hectáreas cosechadas y el municipio para estimar la producción de café en toneladas.

---

# 3. Problemática

La producción agrícola puede presentar variaciones importantes entre diferentes años. Estas variaciones pueden estar relacionadas con factores como el área sembrada, el área cosechada y las condiciones propias de la actividad agrícola.

En **Cartago, Valle del Cauca**, analizar el comportamiento histórico de la producción de café permite identificar cambios y tendencias que pueden utilizarse como información de apoyo para la planificación de futuras cosechas.

Por esta razón, el proyecto busca analizar los datos históricos disponibles y utilizar esta información para construir un sistema de **estimación de la producción de café mediante Machine Learning**.

---

# 4. Objetivo general

Desarrollar un sistema de análisis y Machine Learning que permita **estimar la producción de café en Cartago, Valle del Cauca**, utilizando información histórica agrícola.

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
* Preparar las variables utilizadas por el modelo.
* Entrenar un modelo de Machine Learning.
* Evaluar el modelo mediante métricas de rendimiento.
* Realizar estimaciones de producción para Cartago.

---

# 5. Datos utilizados

El proyecto utiliza información agrícola real del **Valle del Cauca**.

El conjunto de datos contiene información histórica de diferentes cultivos y municipios del departamento. Para este proyecto se seleccionaron los registros correspondientes al cultivo de **café** y posteriormente se identificaron los registros correspondientes al municipio de **Cartago**.

### Fuente de los datos

**Gobernación del Valle del Cauca – Datos Abiertos**

Dataset:

**Consolidado agrícola por municipios de los cultivos permanentes del Valle del Cauca**

Los datos contienen información relacionada con cultivos permanentes registrados en diferentes municipios del departamento.

---

# 6. Estructura de los datos

El archivo principal utilizado es un archivo **CSV**.

Entre las variables utilizadas en el proyecto se encuentran:

| Variable                          | Descripción                            |
| --------------------------------- | -------------------------------------- |
| `Año`                             | Año del registro agrícola              |
| `Municipio`                       | Municipio donde se registra el cultivo |
| `Cultivo`                         | Tipo de cultivo                        |
| `Hectareas_sembradas`             | Área sembrada en hectáreas             |
| `Hectareas_cosechadas`            | Área cosechada en hectáreas            |
| `Produccion_toneladas`            | Producción obtenida en toneladas       |
| `Rendimiento_toneladas/hectareas` | Rendimiento de producción por hectárea |

El archivo utilizado para el análisis es:

```text
data/cafe_valle_limpio.csv
```

---

# 7. Cantidad de datos

Después del proceso de carga y limpieza se obtuvieron los siguientes resultados:

* **969 registros** correspondientes al cultivo de café en el Valle del Cauca.
* **39 municipios** representados en los datos de café.
* **25 registros** correspondientes al cultivo de café en Cartago.
* Periodo analizado en Cartago: **2000 a 2024**.
* El archivo contiene **11 columnas**.

Estos datos permiten analizar el comportamiento histórico de la producción de café y utilizar la información para entrenar un modelo de Machine Learning.

---

# 8. Tecnologías utilizadas

El proyecto utiliza las siguientes herramientas:

* **Python:** lenguaje principal del proyecto.
* **Pandas:** carga, limpieza y manipulación de datos.
* **NumPy:** cálculo de estadísticas.
* **Matplotlib:** generación de gráficos.
* **Scikit-learn:** desarrollo del modelo de Machine Learning.
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

El dataset original utiliza `;` como separador y codificación `latin1`.

Ejemplo:

```python
import pandas as pd

datos = pd.read_csv(
    "data/produccion_cafetera_valle.csv",
    sep=";",
    encoding="latin1"
)
```

Durante el procesamiento también se genera el archivo limpio:

```text
data/cafe_valle_limpio.csv
```

---

# 10. Limpieza y filtrado de los datos

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

Posteriormente se identifican los registros correspondientes al municipio de Cartago:

```python
cartago = cafe[
    cafe["Municipio"].astype(str).str.strip() == "Cartago"
].copy()
```

De esta manera se obtienen los registros históricos correspondientes al cultivo de café en Cartago.

---

# 11. Lista de diccionarios

Como parte de los requisitos del proyecto, los datos procesados se convierten en una **lista de diccionarios** utilizando Pandas:

```python
lista_diccionarios = cartago.to_dict(
    orient="records"
)
```

Cada elemento representa un registro mediante un diccionario.

Ejemplo:

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

Para el análisis exploratorio se creó una función propia llamada:

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

Estas funciones permiten analizar estadísticamente la variable:

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
| Desviación estándar |  **277.80 toneladas** |

### Interpretación

La producción promedio registrada durante el periodo analizado fue de aproximadamente **385.50 toneladas**.

La producción máxima registrada fue de **1431 toneladas**, mientras que la mínima fue de **80 toneladas**.

La desviación estándar de aproximadamente **277.80 toneladas** evidencia una variación importante entre los valores históricos de producción.

---

# 14. Visualización con Matplotlib

Para visualizar el comportamiento histórico de la producción se utiliza **Matplotlib**.

El gráfico representa la producción de café en Cartago entre los años 2000 y 2024.

Ejemplo del código utilizado:

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

### Hallazgo 3: Variación histórica

Los datos muestran cambios importantes en la producción durante el periodo 2000–2024.

La diferencia entre la producción máxima y mínima evidencia que el comportamiento de la producción no es constante.

Esta variabilidad justifica el uso de técnicas de Machine Learning para estudiar la relación entre las variables disponibles y la producción.

---

# 16. Modelo de Machine Learning

Después del análisis exploratorio se desarrolló un modelo de Machine Learning utilizando:

**Random Forest Regressor**

El objetivo del modelo es estimar:

```text
Produccion_toneladas
```

a partir de diferentes variables de entrada.

Las variables utilizadas como características son:

* `Año`
* `Hectareas_sembradas`
* `Hectareas_cosechadas`
* `Municipio`

La variable `Municipio` se transforma mediante **One-Hot Encoding**, generando variables binarias para los municipios presentes en el conjunto de datos.

El modelo final utiliza **42 características de entrada**.

---

# 17. Entrenamiento del modelo

El entrenamiento se realiza en:

```text
src/entrenar_modelo.py
```

Para evitar utilizar datos futuros durante el entrenamiento, se realizó una división temporal:

* Datos de **2000 a 2021:** entrenamiento.
* Datos de **2022 a 2024:** evaluación.

El conjunto de entrenamiento contiene:

**852 registros**

El conjunto de prueba contiene:

**117 registros**

El modelo entrenado se almacena en:

```text
data/modelo_cafetero.pkl
```

El archivo contiene tanto el modelo entrenado como las columnas utilizadas durante el entrenamiento.

---

# 18. Evaluación del modelo

El modelo Random Forest fue evaluado utilizando tres métricas:

### MAE

**350.20 toneladas**

El MAE representa el error absoluto medio de las predicciones.

### RMSE

**679.06 toneladas**

El RMSE penaliza con mayor intensidad los errores grandes.

### R²

**0.7157**

El R² indica el nivel de variabilidad de la variable objetivo explicado por el modelo sobre el conjunto de prueba utilizado.

Los resultados corresponden al conjunto de prueba utilizado durante la evaluación y no exclusivamente a los registros de Cartago.

---

# 19. Predicción para Cartago

La predicción se realiza mediante:

```text
src/predecir.py
```

El programa solicita:

* Municipio.
* Año.
* Hectáreas sembradas.
* Hectáreas cosechadas.

Para realizar una demostración se utilizó el siguiente escenario:

```text
Municipio: Cartago
Año: 2025
Hectáreas sembradas: 305.76
Hectáreas cosechadas: 266.05
```

Las hectáreas utilizadas corresponden a los valores registrados para Cartago en 2024 y se utilizan como referencia para construir el escenario de estimación.

Con estos datos, el modelo obtuvo:

**Producción estimada: 274.88 toneladas**

Es importante aclarar que este valor corresponde a una **estimación generada por el modelo bajo las condiciones de entrada indicadas**, y no representa un dato real observado de producción para 2025.

El gráfico de la predicción se guarda en:

```text
data/prediccion_cartago.png
```

---

# 20. Estructura del proyecto

La estructura principal del proyecto es:

```text
prediccion-cafetera/

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

# 21. Organización de los archivos principales

## Carpeta `data/`

Contiene los datos utilizados y algunos resultados generados durante el proyecto.

### `produccion_cafetera_valle.csv`

Dataset original utilizado como fuente de información.

### `cafe_valle_limpio.csv`

Dataset procesado y utilizado para el análisis y desarrollo del modelo.

### `modelo_cafetero.pkl`

Modelo Random Forest entrenado junto con las columnas utilizadas durante el entrenamiento.

### `eda_cartago_produccion.png`

Gráfico correspondiente al análisis exploratorio de la producción histórica.

### `prediccion_cartago.png`

Gráfico generado a partir de la estimación realizada para Cartago.

### `produccion_cartago.png`

Gráfico complementario utilizado para visualizar información de producción de Cartago.

---

# 22. Organización de los scripts

### `limpiar_datos.py`

Realiza el procesamiento y limpieza inicial de los datos.

### `revisar_datos.py`

Permite revisar la estructura y contenido del dataset.

### `analizar_datos.py`

Realiza análisis sobre los datos procesados.

### `eda.py`

Realiza el análisis exploratorio, estadísticas y visualización de los datos de Cartago.

### `preparar_datos.py`

Prepara las variables necesarias para el desarrollo del modelo.

### `entrenar_modelo.py`

Entrena y evalúa el modelo Random Forest.

### `predecir.py`

Carga el modelo entrenado y realiza estimaciones de producción.

### `graficar_produccion.py`

Genera visualizaciones relacionadas con la producción.

### `main.py`

Archivo reservado para la integración principal del proyecto.

---

# 23. Control de versiones

El proyecto utiliza **Git y GitHub** para llevar el control de versiones.

Durante el desarrollo se realizaron commits para registrar avances importantes, como:

* Organización inicial del proyecto.
* Incorporación y limpieza de los datos.
* Desarrollo del análisis exploratorio.
* Generación de estadísticas y gráficos.
* Preparación de las variables del modelo.
* Entrenamiento del modelo de Machine Learning.
* Evaluación del modelo.
* Implementación de la predicción.

Repositorio:

```text
Proyecto-IA---Monica-Parra
```

---

# 24. Ejecución del proyecto

Para ejecutar el proyecto localmente se deben instalar las dependencias.

### Instalar dependencias

```bash
pip install -r requirements.txt
```

### Ejecutar análisis exploratorio

```bash
python src/eda.py
```

### Entrenar el modelo

```bash
python src/entrenar_modelo.py
```

### Realizar una predicción

```bash
python src/predecir.py
```

El programa solicita los datos de entrada y posteriormente muestra la producción estimada.

---

# 25. Resultados principales del proyecto

Los principales resultados obtenidos son:

| Resultado                    |                Valor |
| ---------------------------- | -------------------: |
| Registros de café            |              **969** |
| Registros de Cartago         |               **25** |
| Periodo analizado            |        **2000–2024** |
| Producción promedio          | **385.50 toneladas** |
| Producción máxima            |   **1431 toneladas** |
| Producción mínima            |     **80 toneladas** |
| Desviación estándar          | **277.80 toneladas** |
| Registros de entrenamiento   |              **852** |
| Registros de prueba          |              **117** |
| Características del modelo   |               **42** |
| MAE                          | **350.20 toneladas** |
| RMSE                         | **679.06 toneladas** |
| R²                           |           **0.7157** |
| Estimación de escenario 2025 | **274.88 toneladas** |

---

# 26. Próximos pasos

Para continuar mejorando el sistema se plantean las siguientes actividades:

1. Analizar nuevas variables que puedan aportar información al modelo.
2. Evaluar otros algoritmos de Machine Learning.
3. Comparar diferentes modelos mediante las mismas métricas.
4. Realizar ajuste de hiperparámetros.
5. Analizar con mayor profundidad los errores de las predicciones.
6. Incorporar nuevas variables agrícolas si se encuentran disponibles.
7. Mejorar la interfaz de entrada y presentación de resultados.
8. Continuar validando el modelo con nuevos datos.

---

# 27. Conclusión

En este proyecto se trabajó con **datos agrícolas reales del Valle del Cauca** para analizar el comportamiento histórico de la producción de café en Cartago.

Inicialmente se realizó la carga, limpieza y organización de los datos mediante Python. Posteriormente se filtraron los registros correspondientes al cultivo de café y al municipio de Cartago.

Durante el análisis exploratorio se utilizaron **listas, diccionarios, Pandas, NumPy y Matplotlib**, permitiendo obtener estadísticas y visualizar el comportamiento histórico de la producción.

Posteriormente se desarrolló un modelo de **Random Forest Regressor**, utilizando información relacionada con el año, las hectáreas sembradas, las hectáreas cosechadas y el municipio.

El modelo obtuvo un **MAE de 350.20 toneladas, un RMSE de 679.06 toneladas y un R² de 0.7157** sobre el conjunto de prueba utilizado.

Finalmente, se implementó una etapa de estimación para Cartago. Utilizando como escenario para 2025 las variables de 305.76 hectáreas sembradas y 266.05 hectáreas cosechadas, el modelo estimó una producción de **274.88 toneladas**.

Estos resultados constituyen una primera versión del sistema y permiten continuar trabajando en la mejora del modelo, la incorporación de nuevas variables y la evaluación de diferentes algoritmos de Machine Learning.
