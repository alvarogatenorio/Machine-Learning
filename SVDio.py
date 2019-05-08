# read data SVD algorithm
# Álvaro García Tenorio, Belén Serrano Antón

from scipy.io import loadmat

class SVDio:
    
    
    def __init__(self, filename):
        self.file = filename
    
    def importData(self):
        mnist = loadmat(self.file)
        #digits = mnist['data']
        return mnist['data']
    
    