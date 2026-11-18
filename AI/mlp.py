
import numpy as np
import matplotlib.pyplot as plt

# Sigmoid activation function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# XOR dataset
X = np.array([[0,0], [0,1], [1,0], [1,1]])
Y = np.array([[0], [1], [1], [0]])

# Initialize weights and biases
np.random.seed(1)
W1 = np.random.randn(2,4) * 0.5
W2 = np.random.randn(4,1) * 0.5
b1 = np.zeros((1,4))
b2 = np.zeros((1,1))

lr = 0.5
epochs = 10000
losses = []

# Training
for i in range(epochs):

    # Forward propagation
    h = sigmoid(X @ W1 + b1)
    out = sigmoid(h @ W2 + b2)

    # Calculate error
    loss = np.mean((Y - out)**2)
    losses.append(loss)

    # Backpropagation
    d2 = (out - Y) * out * (1 - out)
    d1 = (d2 @ W2.T) * h * (1 - h)

    # Update weights and biases
    W2 -= lr * (h.T @ d2) / 4
    b2 -= lr * d2.mean(axis=0, keepdims=True)

    W1 -= lr * (X.T @ d1) / 4
    b1 -= lr * d1.mean(axis=0, keepdims=True)

    if (i+1) % 2000 == 0:
        print("Epoch:", i+1, "Loss:", round(loss, 6))

# Prediction
h = sigmoid(X @ W1 + b1)
out = sigmoid(h @ W2 + b2)

pred = (out >= 0.5).astype(int)

print("Predicted:", pred.flatten())
print("Expected :", Y.flatten())

# Plot loss graph
plt.plot(losses)
plt.xlabel("Epochs")
plt.ylabel("Loss")
plt.title("MLP Training Loss")
plt.grid()
plt.show()
