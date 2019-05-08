# Fisher linear discriminant
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

def compute_projection(data, cardinals):
    m1 = data[:, :cardinals[0]].mean(axis = 1)
    m2 = data[:, cardinals[0]:].mean(axis = 1)
    s1 = np.cov(data[:, :cardinals[0]])
    s2 = np.cov(data[:, cardinals[0]:])
    sw = s1 + s2
    return np.linalg.solve(sw, m2 - m1)

def compute_cut(data, cardinals, w, m1, m2):
    N = np.sum(cardinals)
    p1 = cardinals[0] / N
    p2 = cardinals[1] / N
    data_proj = w.T.dot(data)
    m1_proj = w.T.dot(m1)
    m2_proj = w.T.dot(m2)
    sigma1_cuad = np.var(data_proj[:cardinals[0]])
    sigma2_cuad = np.var(data_proj[cardinals[0]:])
    sigma1 = np.sqrt(sigma1_cuad)
    sigma2 = np.sqrt(sigma2_cuad)
    a = (sigma1_cuad + sigma2_cuad) / (2 * sigma1_cuad * sigma2_cuad)
    b = -(m1_proj * sigma2_cuad + m2_proj * sigma1_cuad) / (sigma1_cuad * sigma2_cuad)
    c = (((m1_proj ** 2) * sigma2_cuad + (m2_proj ** 2) * sigma1_cuad) / (2 * sigma1_cuad * sigma2_cuad)) + np.log(p1 / sigma1) + np.log(p2 / sigma2)
    roots = np.roots(np.array([a,b,c]))
    if derivative_evaluation(roots[0], a, b, c) >= 0:
        return np.real(roots[0])
    else:
        return np.real(roots[1])

def derivative_evaluation(x, a, b, c):
    return 2 * a * x + b

# ax + by + c=0 <=> y = (-ax - c) / b
def evaluate_line(a, b, c, x):
    return (-a * x - c) / b

def plot_cut(w, c, data, linestyle = None):
    a = np.min(data[0])
    b = np.max(data[0])
    plt.plot([a, b], [evaluate_line(w[0], w[1], c, a), evaluate_line(w[0], w[1], c, b)], linestyle = linestyle)

data, cardinals = generate_data(max_cluster_size = 100, centroid_dispersion = 2, same_deformation = True, plot = True)
plt.scatter(data[0, :cardinals[0]], data[1, :cardinals[0]])
plt.scatter(data[0, cardinals[0]:], data[1, cardinals[0]:])
m1 = data[:, :cardinals[0]].mean(axis = 1)
m2 = data[:, cardinals[0]:].mean(axis = 1)
w = compute_projection(data, cardinals)
c = compute_cut(data, cardinals, w, m1, m2)
d = w.T.dot(m1+m2) / 2
plot_cut(w, -c, data)
plot_cut(w, -d, data, linestyle = 'dashed')
plt.show()
