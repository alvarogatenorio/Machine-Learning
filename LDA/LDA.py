# importing stuff...
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import loadmat

# loading the mnist database...
print("Loading the MNIST database...")
mnist = loadmat("./mnist-original.mat")

# getting input data with labels...
data = mnist["data"]
label = mnist["label"]
original_dim = data.shape[0]

# sorting the labels...
print("Sorting the labels...")
sorted_label = np.argsort(label)
sorted_label = sorted_label.flatten()

# get each class elements
print("Getting the number of elements of every class...")
unique_counts = np.unique(label, return_counts = True)[1]
classes = unique_counts.shape[0]
reduced_dim = classes - 1

# computing dispersion between classes...
print("Computing dispersion between classes...")
# computing each class mean...
# meter los data_k en un array
data_k = data[:, sorted_label[ 0 : unique_counts[0] ] ]
mks = np.mean(data_k, axis = 1)
mks = mks[:, np.newaxis]
acum1 = unique_counts[0]
acum2 = 0
for k in range(1, classes):
    data_k = data[:, sorted_label[acum2 + unique_counts[ k - 1 ] : acum1 + unique_counts[ k ] ] ]
    mk = np.mean(data_k, axis = 1)
    mk = mk[:, np.newaxis]
    mks = np.hstack((mks, mk))
    acum1 += unique_counts[k]
    acum2 += unique_counts[k-1]

# actually computing dispersion between classes...
sb = np.cov(mks, bias = True, fweights = unique_counts)

# computing dispersion within classes...
print("Computing dispersion within classes... ")
data_k = data[:, sorted_label[ 0 : unique_counts[0] ] ]
sw = np.cov(data_k, bias = True)
acum1 = unique_counts[0]
acum2 = 0
for k in range(1, classes):
    data_k = data[:, sorted_label[acum2 + unique_counts[ k - 1 ] : acum1 + unique_counts[ k ] ] ]
    sk = np.cov(data_k, bias = True)
    sw = np.add(sw, sk)
    acum1 += unique_counts[k]
    acum2 += unique_counts[k-1]

# computing the auxiliary matrix
print("Computing the auxiliary matrix...")
sw_sb = np.linalg.lstsq(sw,sb, rcond = None)[0]

# computing the projection
print("Computing the projection matrix...")
values, vectors = np.linalg.eig(sw_sb)
values = np.array([v for v in values if np.imag(v) == 0])
values = values.real
idx = np.argsort(values)[::-1]
values = values[idx]
vectors = vectors[:,idx].real
wt = vectors[:,:reduced_dim].T
wt_full = np.vstack((wt, np.zeros((original_dim-reduced_dim,original_dim))))
print(wt_full.shape)

# probando
print("LDA (random testing)")

# mostrar 5 de cada reducidos (por hacer)
proj1 = wt.dot(data[:,0])
proj2 = wt.dot(data[:,1])
plt.imshow(proj1.reshape(3, 3), cmap='gray')
plt.show()

plt.imshow(proj2.reshape(3, 3), cmap='gray')
plt.show()
