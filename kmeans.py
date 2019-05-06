# k-means algorithm
# Álvaro García Tenorio, Belén Serrano Antón

# Importing stuff...
import numpy as np
import matplotlib.pyplot as plt

# Generates K normal clusters of data
def generate_data(D, K, max_cluster_size, centroid_dispersion):
    # cardinals[i] represents the number of elements in the i-th cluster
    cardinals = np.random.randint(max_cluster_size - 1, size = K) + 1

    # The i-th row represents (dispersion, mean_1, mean_2) of the i-th cluster
    dispersions = np.random.rand(K)[:, np.newaxis]
    means = np.random.randn(K, D) * centroid_dispersion
    offsets = np.hstack((dispersions, means))

    # Plots the means (for debugging purposes)
    if D == 2:
        plt.scatter(offsets[:, 1], offsets[:, 2], marker = 'x')
        plt.draw()

    # Generate the normal clusters
    data = np.random.randn(D, cardinals[0]) * offsets[0, 0] + offsets[0, 1:][:, np.newaxis]
    for k in range(1, K):
        aux = np.random.randn(D, cardinals[k]) * offsets[k, 0] + offsets[k, 1:][:, np.newaxis]
        data = np.hstack((data, aux))
    return data

# Plots the data
def plot_data(data):
    plt.scatter(data[0,:], data[1,:])

# First initialitation of the cluster vectors...
def random_initialization(data, K, plot):
    data_copy = data.copy()
    np.random.shuffle(data_copy.T)

    # Plot the initial centroids (for debugging purposes)
    if plot:
        plt.scatter(data_copy[0, :K], data_copy[1, :K], marker = '*')
        plt.draw()

    return data_copy[:, :K]

# Assign tags
def assign_tags(data, mu):
    # DARK BROADCASTING MAGIC
    sqr_norms = np.sum((data.T - mu[:,np.newaxis].T) ** 2, axis = 2)
    return np.argmin(sqr_norms, axis = 0)

# Update centroids
def update_centroids(data, r):
    # another python dark trick...
    return np.array([data[:,r == k].mean(axis = 1) for k in range(0, K)]).T

# Main flow
def k_means(K, data, plot):
    mu = random_initialization(data, K, False) # D x K
    changed = True
    r = assign_tags(data, mu)
    while (changed):
        mu = update_centroids(data, r)
        if plot:
            plt.scatter(mu[0,:], mu[1,:], marker = '^')
            plt.draw()
        old = r.copy()
        r = assign_tags(data, mu)
        changed = not np.array_equal(r, old)
    if plot:
        plt.scatter(mu[0,:], mu[1,:], marker = 'D')
        plt.draw()
    for k in range (0, K):
        plt.scatter(data[0, r == k], data[1, r == k])
        plt.draw()

def clk_k_means(event):
    global K
    global data
    k_means(K, data, False)

fig = plt.figure()
fig.canvas.mpl_connect('button_press_event', clk_k_means)
D = 2
K = 4
data = generate_data(D, K, 100, 2) # D x N
N = data.shape[1]
plot_data(data)
plt.show()
