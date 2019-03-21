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
       Xmean = np.mean(self.digits, axis = 1)
       X = self.digits - Xmean[:, np.newaxis]
       U, D2, Vt = np.linalg.svd(X, full_matrices=False)
       return U, D2, Vt,Xmean

    #compute min d such that (....)
    def computeDprime(self,D2, dim,eps):
        for d in range(dim):
            if(sum(D2[0:d]) / np.sum(D2) > 0.8):
                return d
    
    #compute the projection of the point point (number of the image)
    #def computeProjection(point,Dprime,U,Xmean):
     #   P = U[:,:Dprime].dot(U[:,:Dprime].T)
     #   img = self.digits[:,point]
     #   img_proj = Xmean + P.dot(img-Xmean)
     #   return img_proj
    
    def reduccionDim(self,d,num_image,U,Xmean):
        P = U[:,:d].dot(U[:,:d].T)
        #num_image = 56745
        img = self.digits[:,num_image]
        img_proj = Xmean + P.dot(img-Xmean)
        return [img,img_proj]
    
    def show_digit(self,dgt):
        return plt.imshow(dgt.reshape((28,28)),cmap='gray')
    
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