# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 18:08:59 2019

@author: MRS
"""


import numpy as np
import matplotlib.pyplot as plt

N = 20
N0, N1 = 10, 10


mu0 = np.array([10, 0])
X0 = np.random.randn(2, N0) + mu0[:, np.newaxis]

mu1 = np.array([-10, 10])
X1 = np.random.randn(2, N1) + mu1[:, np.newaxis]


f = open('puntosGeneradosAB.txt', 'a')

def escribePuntos(V,long):
    for i in range(0,long):
        f.write(str(V[0][i]) + ' ')
        f.write(str(V[1][i]))
        f.write('\n')
    return

#escribimos la cabecera
f.write(str(N))
f.write('\n')
f.write(str(N0))
f.write('\n')
f.write(str(N1))
f.write('\n')


#escribimos los putnos con formato
escribePuntos(X0,N0)
escribePuntos(X1,N1)


#Escribimos su clase
clase1 = 1
clase2 = -1

f.write(str(clase1))
f.write('\n')
f.write(str(clase2))
f.write('\n')


f.close()
 
 





