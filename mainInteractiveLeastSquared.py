# main least squared  algorithm
# Álvaro García Tenorio, Belén Serrano Antón

import classIO
import classLeastSquared
import numpy as np
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
    ax.plot(Xprime[1, myprev:mynext], Xprime[2, myprev:mynext], classID[i])
    plt.draw()


#Classify new points
def onclick(event):
    global ix, iy
    
    ix, iy = event.xdata, event.ydata
    
    global coords
    coords = [ix, iy]
    newpoint = np.array([ix,iy])
    newClass = mySolutions.classify(newpoint, myW)
    print("La clase del punto ("+ str(ix) + "," + str(iy)  + ") es: " + str(newClass +1))
    ax.plot(ix,iy, classID[newClass])
    plt.draw()
    return coords

fig.canvas.mpl_connect('button_press_event', onclick)
    
plt.show()

