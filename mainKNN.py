# main k-nn algorithm
# Álvaro García Tenorio, Belén Serrano Antón


import classIOKNN
import KNN
import numpy as np
import matplotlib.pyplot as plt

#Read data from file
myData = classIOKNN.myIO('puntosGeneradosKNN.txt');

#(numPuntos, matrizPuntos,numClases,numPuntosXclase)
#(numPoints, matrix with data,)
trainingPoints = myData.readData();
#K = trainingPoints[2]
K = 4
numPoints = trainingPoints[0]

mySolutions = KNN.KNN(trainingPoints[1],trainingPoints[2])


#plot

myprev = 0
mynext = 0

fig = plt.figure()
ax = fig.add_subplot(111)


#we assume K <= 6
classID = ['bo','go','ro','co','mo','ko']

matrizPuntos = trainingPoints[1]
pointX = matrizPuntos[1][0]
pointY = matrizPuntos[1][1]

for i in range(0,numPoints):
    pointClass = int(trainingPoints[1][i][2])
    ax.plot(trainingPoints[1][i][0], trainingPoints[1][i][1], classID[pointClass])
    plt.draw()


#Classify new points
def onclick(event):
    global ix, iy
    
    ix, iy = event.xdata, event.ydata
    
    global coords
    coords = [ix, iy]
    pointClass = 0 #initialization
    newpoint = np.array([ix,iy,pointClass])
    newClass = int(mySolutions.classify(newpoint))
    #comment this line if you don't want to add the new point into the data
    matrizPuntos.append(np.array([ix,iy,newClass]))
    print("La clase del punto ("+ str(ix) + "," + str(iy)  + ") es: " + str(newClass +1))
    ax.plot(ix,iy, classID[newClass])
    plt.draw()
    return coords

for i in range(0,1):

    cid = fig.canvas.mpl_connect('button_press_event', onclick)
    
plt.show()