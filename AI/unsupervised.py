
import numpy as np
import matplotlib.pyplot as plt

# Input data
X = np.array([
    [1, 2], [2, 1], [2, 3],
    [8, 8], [9, 8], [8, 9]
])

k = 2

# Initial centroids
centroids = X[[0, 5]].copy()

# K-Means algorithm
for i in range(100):
    old = centroids.copy()

    # Calculate distances
    dist = np.linalg.norm(X[:, None] - centroids, axis=2)

    # Assign points to nearest cluster
    labels = np.argmin(dist, axis=1)

    # Update centroids
    for j in range(k):
        centroids[j] = X[labels == j].mean(axis=0)

    # Check convergence
    if np.allclose(old, centroids):
        break

# Display results
for j in range(k):
    print("Cluster", j+1, ":", X[labels == j])

print("Centroids:", centroids)
print("Converged at iteration:", i+1)

# Plot clusters
for j in range(k):
    plt.scatter(X[labels == j, 0],
                X[labels == j, 1],
                label="Cluster " + str(j+1))

plt.scatter(centroids[:, 0], centroids[:, 1],
            color='red', marker='X', s=100,
            label="Centroids")

plt.title("K-Means Clustering")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.grid()
plt.show()
