# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 17:31:44 2019

@author: MRS
"""


import numpy as np
# Let D be the dimension of our data column vectors.
# Let K be the number of classes.
# Let N be the number of training data.
class LeastSquaresClassifierAB:

    # x represents the training data by columns (dimension D+1 times N).
    # The first row of x the training data is entirely made by ones.

    # t represents the tags of the training data by columns
    # (dimension K times N).
    def __init__(self,x,n1,n2):
        self.x = x
        self.n1 = n1
        self.n2 = n2
        # w is the matrix of the classifier, which is empty at first.
        #self.w = np.array()

    # Computes a minimum square affine classifier
    # for the training data x and the tags t
    def compute_classifier(self):
        Sw1 = np.cov(self.x[:,0:self.n1])
        Sw2 = np.cov(self.x[:,self.n1:])
        Sw = Sw1 + Sw2
        m1 = np.mean(self.x[:,0:self.n1], axis=1)
        m2 = np.mean(self.x[:,self.n1:], axis=1)
        # solving w without inverting
        W = np.linalg.solve(Sw,m1-m2)
        m = (self.n1 * m1 + self.n2*m2)/(self.n1+self.n2)
        m0 = np.dot((np.transpose(W)),m)
        return np.array([[m0],W])

    # Classify the given data x according to the
    # previously computed classifier.
    # x must be a column vector
    def classify(self, myx, mym0, myw,alpha, beta):
       # myx = np.append(1, myx)
        mywt = np.transpose(myw)
        y = np.dot(mywt,myx) + mym0
        # Returns alpha if x in C1 or beta if x in C2
        if(np.abs(y-alpha) <= np.abs(y-beta)):
            return alpha
        else:
            return beta

