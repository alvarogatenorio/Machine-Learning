#  least squared algorithm
# Álvaro García Tenorio, Belén Serrano Antón

#This class contains the basic functions to compute the least squared 
#classifier 

import numpy as np
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

    # Computes a minimum square affine classifier
    # for the training data x and the tags t
    def compute_classifier(self):
        xt = np.transpose(self.x)
        tt = np.transpose(self.t)
        #The gradient of our error function (Wt*X - T)Xt = 0
        # solving the equation (W) without inverting:
        return np.linalg.solve(np.dot(self.x,xt),np.dot(self.x,tt))

    # Classify the given data x according to the previously computed classifier
    # (myw).
    # x must be a column vector
    def classify(self, myx,myw):
        myx = np.append(1, myx) 
        mywt = np.transpose(myw)
        # Returns the class of the given point (the index of the maximum
        # coordinate)
        return np.argmax(np.dot(mywt,myx))

