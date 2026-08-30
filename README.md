# Sistema de Inteligencia Artificial para la Predicción de la Producción Cafetera

## 1. Nombre del proyecto

**Sistema de Inteligencia Artificial para la Predicción de la Producción Cafetera**

## 2. Problemática

La producción cafetera es una actividad agrícola importante en el norte del Valle del Cauca. Los productores pueden presentar dificultades para estimar con anticipación la cantidad de café que obtendrán en una cosecha, debido a factores como las condiciones climáticas, la temperatura, las precipitaciones, el área cultivada, la altitud y el comportamiento de cosechas anteriores.

En el contexto de **Cartago, Valle del Cauca**, y su zona de influencia rural y cafetera, contar con una herramienta que permita realizar estimaciones de producción podría apoyar la planificación de recursos, mano de obra, costos y comercialización.

Por esta razón, se propone desarrollar un sistema de Inteligencia Artificial que analice datos históricos y características de los cultivos para realizar una predicción aproximada de la producción de café.

## 3. Datos

El sistema necesitará información relacionada con las características de los cultivos y su producción histórica.

### Datos necesarios

- Área cultivada.
- Temperatura promedio.
- Cantidad de precipitación o lluvia.
- Altitud.
- Producción de café de cosechas anteriores.
- Año o periodo de cosecha.
- Cantidad de café producido.

### Fuente de los datos

Los datos podrán obtenerse de:

- Datos abiertos de entidades oficiales.
- Información agrícola disponible públicamente.
- Archivos CSV.
- Conjuntos de datos utilizados con fines académicos.
- Otras fuentes públicas relacionadas con producción agrícola y cafetera.

La información será organizada y procesada mediante Python.

> Durante el desarrollo se verificará la disponibilidad de datos específicos para Cartago, Valle del Cauca. Si no existe suficiente información local, se utilizarán datos de referencia de la región cafetera colombiana para construir y evaluar el modelo con fines académicos.

## 4. Objetivo

### Objetivo general

Desarrollar un sistema de Inteligencia Artificial utilizando Python y técnicas de Machine Learning que permita predecir la cantidad aproximada de café que puede producirse en una cosecha, utilizando datos históricos y características del cultivo.

### Objetivos específicos

- Recopilar y organizar datos relacionados con la producción cafetera.
- Analizar los datos para identificar relaciones entre las características del cultivo y su producción.
- Preparar y procesar los datos utilizando Python.
- Entrenar un modelo de Machine Learning para realizar predicciones.
- Evaluar el desempeño del modelo mediante métricas apropiadas.
- Generar predicciones de producción para nuevos datos.
- Representar los resultados mediante gráficos.

## 5. Inteligencia Artificial y Machine Learning

El proyecto utilizará **Machine Learning**, una rama de la Inteligencia Artificial que permite desarrollar modelos capaces de identificar patrones a partir de datos históricos y utilizar dichos patrones para realizar predicciones sobre nuevos datos.

Para la predicción de la producción cafetera se propone utilizar **Random Forest Regressor**, un algoritmo de Machine Learning orientado a problemas de regresión.

El modelo recibirá características del cultivo como área cultivada, temperatura, precipitación, altitud y producción anterior, y tendrá como objetivo predecir la cantidad de café producida en kilogramos.

El proceso general será:

```text
Datos históricos
       ↓
Preparación y limpieza de datos
       ↓
División de datos
       ↓
Entrenamiento del modelo
       ↓
Random Forest Regressor
       ↓
Evaluación del modelo
       ↓
Nuevos datos
       ↓
Predicción de producción