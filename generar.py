# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal
"""


import numpy as np
import matplotlib.pyplot as plt

N = 40
N0, N1, N2, N3 = 10, 10, 10, 10
K = 4

mu0 = np.array([10, 0])
X0 = np.random.randn(2, N0) + mu0[:, np.newaxis]

mu1 = np.array([-10, 10])
X1 = np.random.randn(2, N1) + mu1[:, np.newaxis]

mu2 = np.array([-10, -0])
X2 = np.random.randn(2, N2) + mu2[:, np.newaxis]

mu3 = np.array([10, 10])
X3 = np.random.randn(2, N3) + mu3[:, np.newaxis]

f = open('puntosGenerados.txt', 'a')

def escribePuntos(V,long):
    for i in range(0,long):
        f.write(str(V[0][i]) + ' ')
        f.write(str(V[1][i]))
        f.write('\n')
    return

#escribimos la cabecera
f.write(str(N))
f.write('\n')
f.write(str(K))
f.write('\n')
f.write(str(N0))
f.write('\n')
f.write(str(N1))
f.write('\n')
f.write(str(N2))
f.write('\n')
f.write(str(N3))
f.write('\n')

#escribimos los putnos con formato
escribePuntos(X0,N0)
escribePuntos(X1,N1)
escribePuntos(X2,N2)
escribePuntos(X3,N3)

#Escribimos su clase
clase1 = np.array([1,0,0,0])
clase2 = np.array([0,1,0,0])
clase3 = np.array([0,0,1,0])
clase4 = np.array([0,0,0,1])

def escribeClase(V,long):
    for i in range(0,long):
       enStr = ' '.join(map(str, V))
       f.write(enStr)
       f.write('\n')
    return 

escribeClase(clase1, N0)
escribeClase(clase2, N1)
escribeClase(clase3, N2)
escribeClase(clase4, N3)

f.close()
 
 





