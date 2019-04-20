# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 20:22:54 2019

@author: Álvaro García, Belén Serrano

"""


import SVDio as classSVDio
import SVD as classSVD
import numpy as np
import matplotlib.pyplot as plt

#threshold to compute d (dimension of the proyection)
eps = 0.8
#dimension of the points and number of points
D , N = 784, 70000

#Read data from file
myData = classSVDio.SVDio('C:\hlocal\mldata\mldata\mnist-original.mat')
myDigits = myData.importData()


mySVD = classSVD.SVD(myDigits)
U, D2, Vt, Xmean = mySVD.computeSVD()

d = mySVD.computeDprime(D2,D,eps)

print("La mínima dimensión d es: " +  str(d) )
   
#mySVD.plotPoints(N,U,Xmean)

mySVD.plotGrid(N,U,Xmean)