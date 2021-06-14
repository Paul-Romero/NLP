# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 10:43:10 2021

Prueba de los módulos de scikit learning

@author: PARA
"""

# Importación de librerias
from sklearn import datasets, linear_model
import numpy as np
import matplotlib.pyplot as plt

# Importar los datos de la librerias
boston = datasets.load_boston()
# Mostrar los datos del dataset
print("Información en el dataset: \n", boston.keys())
print("Características del dataset: \n", boston.DESCR)
print("Cantidad de datos \n", boston.data.shape)
print("Nombres columnas \n", boston.feature_names)

# Seleccionamos la columna 5 del dataset
X = boston.data[:,np.newaxis,5]
# Definimos los datos correspondientes a las etiquetas
y = boston.target

# Graficar los datos para visualizar su distribución
plt.scatter(X,y)
plt.xlabel("Número de habitaciones")
plt.ylabel("Valor medio")
plt.show()

# Importar el modelo de regresión lineal simple
from sklearn.model_selection import train_test_split
# Separar los datos de entrenamiento y de prueba del algoritmo
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
# Definir el algoritmo
lr = linear_model.LinearRegression()
# Entrenar el modelo
lr.fit(X_train, y_train)
# Realizar la predicción
Y_pred = lr.predict(X_test)

# Graficar los datos con el modelo
plt.scatter(X_test, y_test)
plt.plot(X_test, Y_pred, color='red', linewidth=3)
plt.title("Regresión Lineal Simple")
plt.xlabel("Número de habitaciones")
plt.ylabel("Valor medio")
plt.show()

# Datos del modelo de Regresión Lineal Simple
print("Valor de la pendiente o coeficiente a: ", lr.coef_)
print("Valor de la intersección o coeficiente b: ", lr.intercept_)
print(f"La ecuación del modelo es: y = {lr.coef_} + x {lr.intercept_}")
print("Precisión del modelo: ", lr.score(X_train, y_train))

