# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 17:33:06 2019

@author: MRS
"""

import numpy as np
from io import StringIO
import array as arr

#cargare los vectores y las etiquetas de un archivo, es más cómodo
#que irlo escribiendo cada vez en la entrada

print("Introduce el nombre del archivo donde tienes tus puntos de prueba")
nombreArch = input()

#esto se supone que llama a close
#with open(nombreArch) as f:

f = open(nombreArch, 'r')

numPuntos = int(f.readline())
filas = 2*numPuntos
print(filas)

matrizPuntos = []

for i in range(0, filas):
    linea = f.readline()
    #sobreentendemos que los delimitadores son espacios
    linea = np.genfromtxt(StringIO(linea))
    #ñadimos el 1 para la Xgusano
    if i < numPuntos:
        linea = np.append(1, linea)
        matrizPuntos.append(linea[0:])
    #leemos las etiquetas
    else:
        matrizPuntos.append(linea[0:])
        
f.close()

Xgusano = matrizPuntos[0:numPuntos]
T = matrizPuntos[numPuntos:]

print(Xgusano)
print(T)

#para hacer la multiplicación
#B = np.transpose(Xgusano).dot(T)
#print(B)



