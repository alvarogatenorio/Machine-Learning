# read data k-nn algorithm
# Álvaro García Tenorio, Belén Serrano Antón


import numpy as np
from io import StringIO
#import array as arr


class myIO:
    
    def __init__(self, nombreArch):
        self.nombreArch = nombreArch
    
    def readData(self):
        f = open(self.nombreArch, 'r')
        numPuntos = int(f.readline())
        numClases = int(f.readline())
        numPuntosXclase = []
        
        for j in range(0, numClases):
            numPuntosXclase.append(int(f.readline()))
          
        matrizPuntos = []
        
        for i in range(0, numPuntos):
            linea = f.readline()
            #sobreentendemos que los delimitadores son espacios
            linea = np.genfromtxt(StringIO(linea))
            matrizPuntos.append(linea[0:])
                
        f.close()
        
        return (numPuntos, matrizPuntos,numClases,numPuntosXclase)
    

