# -*- coding: utf-8 -* -
"""
Created on Thu Feb  7 09:51:09 2019

@author: Belen Serrano, Álvaro García

"""

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
        # w is the matrix of the classifier, which is empty at first.
        #self.w = np.array()

    # Computes a minimum square affine classifier
    # for the training data x and the tags t
    def compute_classifier(self):
        xt = np.transpose(self.x)
        tt = np.transpose(self.t)
        # solving without inverting
        return np.linalg.solve(np.dot(self.x,xt),np.dot(self.x,tt))

    # Classify the given data x according to the
    # previously computed classifier.
    # x must be a column vector
    def classify(self, myx,myw):
        myx = np.append(1, myx)
        mywt = np.transpose(myw)
        # Returns the index of the maximum coordinate
        return np.argmax(np.dot(mywt,myx))

