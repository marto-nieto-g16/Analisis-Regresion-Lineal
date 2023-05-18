# Análisis de Regresión Lineal

Este código en Python utiliza la librería yfinance para descargar los datos de precio de cierre para Bitcoin (BTC-USD) desde Yahoo Finance. Los datos son procesados y limpiados utilizando las librerías pandas y numpy para ser usados en el entrenamiento y prueba de un modelo de regresión lineal. Finalmente, el modelo es utilizado para predecir futuros precios de Bitcoin y un gráfico de dispersión es creado para visualizar los precios predichos.

## Librerías Utilizadas

- yfinance: Una librería en Python utilizada para descargar datos financieros desde Yahoo Finance.
- pandas: Una librería en Python utilizada para la manipulación y análisis de datos.
- numpy: Una librería en Python utilizada para computación científica.
- sklearn.linear_model: Una librería en Python que contiene varios modelos de regresión.
- matplotlib.pyplot: Una librería en Python utilizada para la visualización de datos.

## Preprocesamiento de los Datos

Los datos descargados son almacenados en un dataframe de pandas y la columna 'Close' es seleccionada como variable objetivo para la predicción. La columna 'Date' es convertida a un tipo compatible con float64. Los datos son luego divididos en conjuntos de entrenamiento y prueba utilizando la librería sklearn.

## Entrenamiento del Modelo

Un modelo de regresión lineal es entrenado en los datos de entrenamiento utilizando el método LinearRegression() de la librería sklearn.

## Prueba del Modelo

El modelo es probado en los datos de prueba y los precios predichos son almacenados en la variable 'y_pred'.

## Visualización de los Datos

Un gráfico de dispersión es creado para visualizar los precios predichos. Los datos de entrenamiento y prueba son graficados en colores azul y verde respectivamente y los precios predichos son graficados como una línea roja.

## Cómo Utilizar

Para utilizar este código, simplemente copie y pegue en un ambiente de Python, como Jupyter Notebook o Spyder. Asegúrese de instalar las librerías requeridas antes de ejecutar el código. Puede cambiar la variable 'symbol' para analizar diferentes activos financieros y ajustar las fechas 'start' y 'end' para modificar el período de tiempo de los datos.
