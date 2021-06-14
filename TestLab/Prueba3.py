# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 14:52:06 2021

Prueba Máquina Vectores se Soporte SVM Clasificación

@author: PARA
"""

# Importar las librerias
from sklearn import datasets
# Importar los datos de la libreria
dataset = datasets.load_breast_cancer()
# Ver la info en el dataset
print("Información del dataset: \n", dataset.keys())
print("Características del dataset: \n", dataset.DESCR)
# Seleccionar las columnas
X = dataset.data
# Definir los datos correspondientes a las etiquetas
y = dataset.target

# Separar los datos de entrenamiento y de prueba del algoritmo
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
SVM = SVC(kernel='linear')
# Entrenar el modelo
SVM.fit(X_train, y_train)
# Realizar prediccion
y_pred = SVM.predict(X_test)

# Importar matriz de confusión
from sklearn.metrics import confusion_matrix, precision_score
matriz = confusion_matrix(y_test, y_pred)
precision = precision_score(y_test, y_pred)
# Visualizar matriz de confusión y precisión
print("Matriz de confusión: \n", matriz)
print("Precisión del modelo: \n", precision)
