# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 10:01:07 2019

@author: Belen Serrano y Álvaro García
"""

import classIO
import classLeastSquared
import numpy as np
from io import StringIO
import matplotlib.pyplot as plt

#Read data from file
myData = classIO.myIO('puntosGenerados.txt');

#Pair (numPoints, matrix with data)
points = myData.readData();

Xprime = np.transpose((points[1])[0:points[0]])
T = np.transpose((points[1])[points[0]:])
K = points[2]

#Compute W
mySolutions = classLeastSquared.LeastSquaresClassifier(Xprime,T)
myW = mySolutions.compute_classifier()

#plot
#import matplotlib.pyplot as plt
#Para plotear un punto: plt.plot(1,2,'bo')
#https://matplotlib.org/api/_as_gen/matplotlib.pyplot.plot.html

myprev = 0
mynext = 0

fig = plt.figure()
ax = fig.add_subplot(111)
#p = ax.plot(x_points, y_points, 'b')

#we assume K <= 6
classID = ['o','^','*','+','x','h']

for i in range(0,K):
    myprev = mynext
    mynext = mynext + points[3][i]
   # plt.plot(Xprime[1, myprev:mynext], Xprime[2, myprev:mynext], classID[i])
    ax.plot(Xprime[1, myprev:mynext], Xprime[2, myprev:mynext], classID[i])
    plt.draw()


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
    
    print("La clase del nuevo punto es: " + str(newClass +1))
    #plt.plot(newPoint[0], newPoint[1], classID[newClass])
    ax.plot(newPoint[0], newPoint[1], classID[newClass])
    plt.draw()
plt.show()

