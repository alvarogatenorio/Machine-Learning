# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 10:01:07 2019

@author: Belen Serrano y Álvaro García
"""
import classIO
import classLeastSquared
import numpy as np
from io import StringIO

#Read data from file
myData = classIO.myIO('minCuadradosPrueba.txt');

#Pair (numPoints, matrix with data)
points = myData.readData();

Xprime = np.transpose((points[1])[0:points[0]])
T = np.transpose((points[1])[points[0]:])

#print(Xprime)
#print(T)

#Compute W
mySolutions = classLeastSquared.LeastSquaresClassifier(Xprime,T)
myW = mySolutions.compute_classifier()

#plot
#import matplotlib.pyplot as plt
#Para plotear un punto: plt.plot(1,2,'bo')
#https://matplotlib.org/api/_as_gen/matplotlib.pyplot.plot.html


##########

#Classify new points
stop = "dontwanttostop"
while stop != "stp":
    print("Write the coordenates of the point you want to classify (""stp"" - exit):")
    print("example: write 1 3 to classify point (1,3)")
    newPoint = input()
    
    if (newPoint == "stp"):
        break
    
    newPoint = np.genfromtxt(StringIO(newPoint))
    newClass = mySolutions.classify(newPoint, myW)
    
    print(newClass)



