# main least squared alpha beta algorithm
# Álvaro García Tenorio, Belén Serrano Antón


import classIOAB
import classLeastSquaredAB
import numpy as np
import matplotlib.pyplot as plt

#Read data from file
myData = classIOAB.myIOAB('puntosGeneradosAB.txt');

#Pair (numPoints, matrix with data)
points = myData.readData();

Xprime = np.transpose(points[1])

N1 = (points[2])[0]
N2 = (points[2])[1]

alpha = points[3]
beta = points[4]


#Compute W
mySolutions = classLeastSquaredAB.LeastSquaresClassifierAB(Xprime,N1,N2)
sol = mySolutions.compute_classifier()

mu0 = sol[0][0]
myW = sol[1]



#plot

myprev = 0
mynext = 0

fig = plt.figure()
ax = fig.add_subplot(111)
#p = ax.plot(x_points, y_points, 'b')

#we assume K = 2
classID = ['o','+']

for i in range(0,2):
    myprev = mynext
    mynext = mynext + points[2][i]
    ax.plot(Xprime[0, myprev:mynext], Xprime[1, myprev:mynext], classID[i])
    plt.draw()


#Classify new points
def onclick(event):
    global ix, iy
    
    ix, iy = event.xdata, event.ydata
    
    global coords
    coords = [ix, iy]
    newpoint = np.array([ix,iy])
    #classify(self, myx, mym0, myw,alpha, beta)
    res = mySolutions.classify(newpoint,mu0,myW,alpha,beta)
    print("La clase del punto ("+ str(ix) + "," + str(iy)  + ") es: " + str(res))
    if res == 1:
        ax.plot(ix,iy, classID[0])
    else:
        ax.plot(ix,iy, classID[1])
    plt.draw()

    
#interactive part:
fig.canvas.mpl_connect('button_press_event', onclick)
    
plt.show()

    
    