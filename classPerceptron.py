# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 22:50:12 2019

@author: Belén Serrano, Álvaro García
"""

import numpy as np
# Let D be the dimension of our data column vectors.
# Let K be the number of classes.
# Let N be the number of training data.
class Perceptron:

    # x represents the training data by columns.
    def __init__(self,x,n):
        self.x = x
        self.n = n
        
    # w is the matrix of the classifier, which is 0 at first.
        

    # Computes one step of the perceptron algorithm
    # for the training data x, tag t and classifier W from the 
    # previous iteration
    def compute_classifier_oneStep(self,x,t,W):
        #Point is well classified
        if(np.dot(np.transpose(W), x)*t > 0):
            return W
        else:
            return (W + x*t)
        

    # Classify the given data x according to the
    # previously computed classifier.
    # x must be a column vector
    def classify(self, myx, myw):
        # Returns 1 if x in C1 or -1 if x in C2
        if(np.dot(np.transpose(myw), myx) > 0):
            return 1
        else:
            return -1

