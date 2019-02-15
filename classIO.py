import numpy as np
from io import StringIO
#import array as arr


class myIO:
    
    def __init__(self, nombreArch):
        self.nombreArch = nombreArch
        
    #cargare los vectores y las etiquetas de un archivo, es más cómodo
    #que irlo escribiendo cada vez en la entrada
    #def inputFromFile:
        #print("Introduce el nombre del archivo donde tienes tus puntos de prueba")
       # nombreArch = input()
    
    #esto se supone que llama a close
    #with open(nombreArch) as f:
    
    def readData(self):
        f = open(self.nombreArch, 'r')
        numPuntos = int(f.readline())
        numClases = int(f.readline())
        numPuntosXclase = []
        
        for j in range(0, numClases):
            numPuntosXclase.append(int(f.readline()))
          
        filas = 2*numPuntos
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
        return (numPuntos, matrizPuntos,numClases,numPuntosXclase)
    
    #Xgusano = matrizPuntos[0:numPuntos]
    #T = matrizPuntos[numPuntos:]




