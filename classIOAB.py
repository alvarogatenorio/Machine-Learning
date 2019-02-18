# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 17:56:41 2019

@author: MRS
"""

import numpy as np
from io import StringIO
#import array as arr


class myIOAB:
    
    def __init__(self, nombreArch):
        self.nombreArch = nombreArch
        
    
    def readData(self):
        f = open(self.nombreArch, 'r')
        numPuntos = int(f.readline())
        numPuntosXclase = []
        
        for j in range(0, 2):
            numPuntosXclase.append(int(f.readline()))
         
        matrizPuntos = []
        
        for i in range(0, numPuntos):
            linea = f.readline()
            #sobreentendemos que los delimitadores son espacios
            linea = np.genfromtxt(StringIO(linea))
            matrizPuntos.append(linea[0:])
                
        alpha = int(f.readline())
        beta = int(f.readline())
        
        f.close()
        
        return (numPuntos, matrizPuntos,numPuntosXclase,alpha,beta)
        