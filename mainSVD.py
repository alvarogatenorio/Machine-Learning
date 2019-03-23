# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 20:22:54 2019

@author: Álvaro García, Belén Serrano

"""


import SVDio as classSVDio
import SVD as classSVD
import numpy as np
import matplotlib.pyplot as plt

eps = 0.8
D , N = 784, 70000

#Read data from file
myData = classSVDio.SVDio('C:\hlocal\mldata\mldata\mnist-original.mat')
myDigits = myData.importData()


#....
mySVD = classSVD.SVD(myDigits)
U, D2, Vt, Xmean = mySVD.computeSVD()

d = mySVD.computeDprime(D2,D,eps)

#mySVD.plotPoints(N,U,Xmean)

mySVD.plotGrid(N,U,Xmean)