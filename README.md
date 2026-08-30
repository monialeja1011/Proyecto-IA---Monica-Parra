# Sistema de Inteligencia Artificial para la Predicción de la Producción Cafetera

## 1. Nombre del proyecto

**Sistema de Inteligencia Artificial para la Predicción de la Producción Cafetera**

## 2. Problemática

La producción de café puede variar de una cosecha a otra debido a diferentes factores, como las condiciones climáticas, la cantidad de lluvia, la temperatura, el área cultivada, la altitud y la producción obtenida anteriormente.

Esta variación puede dificultar que los productores conozcan con anticipación la cantidad aproximada de café que podrán obtener en una cosecha, lo que puede afectar la planificación de recursos, mano de obra, costos y comercialización.

Por esta razón, se propone desarrollar un sistema de Inteligencia Artificial que permita analizar datos relacionados con los cultivos de café y utilizar esta información para realizar una predicción aproximada de la producción.

## 3. Datos

Para desarrollar el proyecto se necesitarán datos relacionados con la producción y las características de los cultivos cafeteros.

Los principales datos que se podrían utilizar son:

- Área cultivada.
- Temperatura promedio.
- Cantidad de precipitación o lluvia.
- Altitud del cultivo.
- Producción de café de cosechas anteriores.
- Año o periodo de cosecha.
- Cantidad de café producido.

Los datos podrán obtenerse de fuentes de datos abiertos, información agrícola disponible públicamente y conjuntos de datos utilizados con fines académicos.

La información será organizada en archivos CSV para posteriormente ser procesada mediante Python.

## 4. Objetivo

### Objetivo general

Desarrollar un sistema de Inteligencia Artificial utilizando Python y Machine Learning que permita predecir la cantidad aproximada de café que puede producirse en una cosecha, utilizando datos históricos y características del cultivo.

### Objetivos específicos

- Recopilar y organizar datos relacionados con la producción cafetera.
- Analizar los datos para identificar posibles relaciones entre las características del cultivo y su producción.
- Preparar los datos utilizando herramientas de Python.
- Entrenar un modelo de Machine Learning para realizar predicciones.
- Evaluar el desempeño del modelo.
- Mostrar los resultados mediante gráficos y predicciones.

## 5. Modelo de Inteligencia Artificial

Para realizar la predicción se propone utilizar el algoritmo **Random Forest Regressor**, perteneciente a la biblioteca Scikit-learn.

Este modelo será utilizado porque el objetivo del proyecto es predecir un valor numérico, que corresponde a la cantidad aproximada de café producido en kilogramos.

El funcionamiento esperado será:

**Datos del cultivo → Modelo de IA → Producción estimada**

Ejemplo:

```text
Área cultivada: 3 hectáreas
Temperatura: 21 °C
Precipitación: 200 mm
Altitud: 1500 m
Producción anterior: 2200 kg

              ↓

       MODELO DE IA

              ↓

Producción estimada: 2350 kg