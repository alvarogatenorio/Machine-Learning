# Perceptron
# Álvaro García Tenorio, Belén Serrano Antón

import numpy as np
import matplotlib.pyplot as plt

# Generates rotation + stretching matrixes (2, 2, classes)
def generate_deformations(classes = 2, deformation_range = 1):
    distorsions = np.random.randn(2, classes) * deformation_range + 1 # (2, classes)
    angles = np.random.rand(classes) * np.pi # (classes, )
    cos = np.cos(angles)[np.newaxis, np.newaxis, :] # (1, 1, classes)
    sin = np.sin(angles)[np.newaxis, np.newaxis, :] # (1, 1, classes)
    cossin = np.vstack((cos, sin)) * distorsions[0] # (2, 1, classes)
    msincos = np.vstack((sin * (-1), cos)) * distorsions[1] # (2, 1, classes)
    return np.hstack((cossin, msincos)) # (2, 2, classes)



def generate_data(dimension = 2, classes = 2, max_cluster_size = 100, centroid_dispersion = 5, no_deformation = False, same_deformation = False, plot = False):
    # Setting the number of elements in each cluster...
    cardinals = np.random.randint(max_cluster_size - 1, size = classes) + 1 # (classes, )
    N = np.sum(cardinals)

    # Generating the dispersions of the clusters...
    dispersions = np.random.randn(classes) # (classes, )
    # Generating the centroids...
    centroids = np.random.randn(classes, dimension).T * centroid_dispersion # (dimension, classes)

    if plot:
        plt.scatter(centroids[0, :], centroids[1, :], marker = 'x')

    # Generating the distorsions (only available for dimension 2)...
    distorsions = None
    if no_deformation or dimension != 2:
        distorsions = np.eye(dimension, dimension)[:, :, np.newaxis] # (2, 2, 1)
    elif same_deformation:
        distorsions = generate_deformations(classes = 1) # (2, 2, 1)
    else:
        distorsions = generate_deformations(classes = classes) # (2, 2, classes)


    # Generating data (by columns)...
    data = np.random.randn(N, dimension).T
    # Multiplying by the dispersion, deformating and adding the centroids
    previous = 0
    for k in range(0, classes):
        s = None
        if no_deformation or dimension != 2 or same_deformation:
            s = 0
        else:
            s = k
        data[:, previous : previous + cardinals[k]] = distorsions[:,:,s].dot(data[:, previous : previous + cardinals[k]]) * dispersions[k] + centroids[:, k, np.newaxis]
        previous = previous + cardinals[k]

    return data, cardinals

# ax + by + c = 0 <=> y = (-ax - c) / b
def evaluate_line(a, b, c, x):
    return (-a * x - c) / b

# Plots the line ax + by + c = 0
def plot_line(w, c, data, linestyle = None):
    a = np.min(data[0])
    b = np.max(data[0])
    plt.plot([a, b], [evaluate_line(w[0], w[1], c, a), evaluate_line(w[0], w[1], c, b)], linestyle = linestyle)

# Add the ones to the data
def add_ones(data): #(2, N)
    ones = np.ones(data.shape[1])[np.newaxis, :] #(1, N)
    return np.vstack((data, ones)) #(3, N)

# Compute labels
def compute_labels(cardinals):
    labels1 = np.ones(cardinals[0]) #(C1, )
    labels2 = -1 * np.ones(cardinals[1]) #(C2, )
    return np.hstack((labels1, labels2))[:, np.newaxis] #(N, 1)

# Generating data...
data, cardinals = generate_data(max_cluster_size = 100, centroid_dispersion = 2, same_deformation = True, plot = True)
print(cardinals)
plt.scatter(data[0, :cardinals[0]], data[1, :cardinals[0]], color = 'red')
plt.scatter(data[0, cardinals[0]:], data[1, cardinals[0]:], color = 'blue')
labels = compute_labels(cardinals)
data = add_ones(data)

# Perceptron initilization, the weights vector will be a row...
w = np.zeros(3)[np.newaxis, :] #(1, 3)

# Perceptron loop (this may take a while)...
changes_in_epoch = True
iter = 0
while changes_in_epoch and iter < 500:
    changes_in_epoch = False
    for n in range(0, data.shape[1]):
        if labels[n] * w.dot(data[:, n]) <= 0:
            # Perceptron refresh...
            w = np.add(w,(data[:, n] * labels[n]).T)
            plot_line(w[0,:2], w[0,2], data, linestyle='dashed')
            changes_in_epoch = True
    iter = iter + 1
plot_line(w[0,:2], w[0,2], data)
if iter == 500:
    print("Maybe non linear separable")
plt.show()
