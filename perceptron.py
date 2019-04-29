import numpy as np
import matplotlib.pyplot as plt
from numpy import arange
from numpy import meshgrid

print("perceptron")

# Data is given by columns (in this case just random)...
data1 = np.random.randn(2,100)-1.9
data2 = np.random.randn(2,100)+1.9
data = np.hstack((data1, data2))
N = data.shape[1]

# Plotting the data...
def plot_data(data, style):
    if data.shape[0] == 2:
        for n in range(0, data.shape[1]):
            plt.plot(data[0, n], data[1, n], style)
            plt.draw()
    else:
        print("The dimension of the data is too high, so it could not be shown... ")

plot_data(data[:, :100], 'or')
plot_data(data[:, 100:], 'ob')

# Add the ones to the data...
ones = np.ones(N)
ones = ones[np.newaxis, :]
data = np.vstack((data, ones))
D = data.shape[0]

# The labels are given by a single row...
labels1 = np.ones(100)
labels2 = -1 * np.ones(100)
labels = np.hstack((labels1, labels2))

# Plotting stuff
delta = 0.025
xrange = arange(-10.0, 10.0, delta)
yrange = arange(-10.0, 10.0, delta)
X, Y = meshgrid(xrange,yrange)

def plot_line(X, Y, w, style):
    plt.contour(X, Y, np.add(np.add(w[:,0]*X, w[:,1]*Y),w[:,2]), [0], linestyles = style)

# Perceptron initilization, the weights vector will be a row...
w = np.zeros(D)
w = w[np.newaxis, :]

# Perceptron loop (this may take a while)...
changes_in_epoch = True
while changes_in_epoch:
    changes_in_epoch = False
    for n in range(0,N):
        if w.dot(data[:, n]) * labels[n] <= 0:
            # Perceptron refresh...
            w = np.add(w,(data[:, n] * labels[n]).T)
            plot_line(X, Y, w, 'dotted')
            changes_in_epoch = True

print(w)
plot_line(X, Y, w, None)
plt.show()
