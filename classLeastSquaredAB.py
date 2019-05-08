# least squared alpha beta algorithm
# Álvaro García Tenorio, Belén Serrano Antón

#This class contains the basic functions to compute the least squared 
#classifier using Fisher's linear discriminant

import numpy as np
# Let D be the dimension of our data column vectors.
# We have only two classes instead of a variable K.
# Let N be the number of training data.
class LeastSquaresClassifierAB:

    def __init__(self,x,n1,n2):
        self.x = x # x represents the training data by columns (dimension D times N).
        self.n1 = n1 #number of points in class 1
        self.n2 = n2 #number of points in class 2
        
    # Computes the classifier for the training data x and the tags t
    def compute_classifier(self):
        # covariance matrices ("within classes")
        Sw1 = np.cov(self.x[:,0:self.n1])
        Sw2 = np.cov(self.x[:,self.n1:])
        #covariance matrix
        Sw = Sw1 + Sw2
        # mean of the points in class 1 (respectively, class 2)
        m1 = np.mean(self.x[:,0:self.n1], axis=1)
        m2 = np.mean(self.x[:,self.n1:], axis=1)
        # solving w without inverting: m1-m2 = Sw*W
        W = np.linalg.solve(Sw,m1-m2)
        # mean of the data x
        m = (self.n1 * m1 + self.n2*m2)/(self.n1+self.n2)
        # affine part of the classifier
        m0 = -np.dot((np.transpose(W)),m)
        return np.array([[m0],W])

    # Classify the given data x according to the
    # previously computed classifier.
    # x must be a column vector.
    # Parameters: classifier, affine part of the classifier, tags of class 1 and 2
    def classify(self, myx, mym0, myw,alpha, beta):
        mywt = np.transpose(myw)
        #compute the result that the classifier gives 
        y = np.dot(mywt,myx) + mym0
        # Returns alpha if x in C1 or beta if x in C2
        if(np.abs(y-alpha) <= np.abs(y-beta)):
            return alpha
        else:
            return beta

