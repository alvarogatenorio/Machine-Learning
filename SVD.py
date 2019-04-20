# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 19:35:21 2019

@author: Álvaro García, Belén Serrano
"""
import numpy as np
import matplotlib.pyplot as plt

class SVD:
    
    
    #digits represents our matrix of images
    def __init__(self,digits):
        self.digits = digits
        
    #computes the SVD of our matrix of images
    def computeSVD(self):
       #mean of our data 
       Xmean = np.mean(self.digits, axis = 1)
       X = self.digits - Xmean[:, np.newaxis]
       #compute the SVD of X = points - meanOfPoints
       U, D2, Vt = np.linalg.svd(X, full_matrices=False)
       return U, D2, Vt,Xmean

    #compute d = the smallest dimension such that the amount of information 
    #that is discarded is less than eps
    def computeDprime(self,D2, dim,eps):
        threshold = 1 - eps
        for d in range(dim):
            if(sum(D2[0:d]) / np.sum(D2) > threshold):
                return d
    
    #compute the projection of the point num_image (number of the image)
    def reduccionDim(self,d,num_image,U,Xmean):
        # dim(P) = dxd -> dimension reduction
        P = U[:,:d].dot(U[:,:d].T)
        #point 
        img = self.digits[:,num_image]
        #poroyection of the point
        img_proj = Xmean + P.dot(img-Xmean)
        return [img,img_proj]
    
    #prints the given point
    def show_digit(self,dgt):
        return plt.imshow(dgt.reshape((28,28)),cmap='gray')
    
    #plots a sequence of 10 random numbers. The first row has the proyection
    #of the numbers in the second row. The dimension of the proyection starts in
    #10 and doubles its value in each iteration
    def plotPoints(self,N,U,Xmean):
        fig = plt.figure() #la caja que recoge todas las imágenes que ponemos dentro 
        fig_size = 10
        rnd_numbers = np.random.randint(0,N,fig_size)
        d = 10
        for k in range(1,fig_size +1):
            ax = fig.add_subplot(1,10,k)
            solu = self.reduccionDim(d,rnd_numbers[k-1],U,Xmean)
            self.show_digit(solu[0])
            ax = fig.add_subplot(2,10,k)
            self.show_digit(solu[1])
            d = d+d
    
    #plots a 6x10 grid. Each colum has the proyection of a random number, 
    #the dimension of the proyection inscreases from top to bottom
    def plotGrid(self, N,U,Xmean):
        fig = plt.figure()
        fig.subplots_adjust(hspace=0.4, wspace=0.4)
        d = 10
        rnd_numbers = np.random.randint(0,N,10)
        for i in range(1, 61):
            ax = fig.add_subplot(6, 10, i)
            solu = self.reduccionDim(d,rnd_numbers[i%10],U,Xmean)
            self.show_digit(solu[1])
            d = d+5
            
            