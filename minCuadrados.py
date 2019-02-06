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


# Let D be the dimension of our data column vectors.
# Let K be the number of classes.
# Let N be the number of training data.
class LeastSquaresClassifier:

    # x represents the training data by columns (dimension D+1 times N).
    # The first row of x the training data is entirely made by ones.

    # t represents the tags of the training data by columns
    # (dimension K times N).
    def __init__(self, x, t):
        self.x = x
        self.t = t
        # w is the matrix of the classifier, which is empty at first.
        self.w = np.array()

    # Computes a minimum square affine classifier
    # for the training data x and the tags t
    def compute_classifier(self):
        xt = self.x.transpose

	# solving without inverting
	return np.linalg.solve(self.w.dot(self.x.dot(xt)),self.t.dot(xt))

    # Classify the given data x according to the
    # previously computed classifier.
    # x must be a column vector
    def classify(self, x):
        x = np.append(x, np.array([1]))
        # Returns the maximum coordinate
        return np.amax(self.W.dot(x))

