
import numpy as np
import matplotlib.pyplot as plt

def step(z):
    return 1 if z >= 0 else 0

X = np.array([[0,0], [0,1], [1,0], [1,1]])
Y = np.array([0,0,0,1])

w = np.zeros(2)
b = 0
lr = 0.5

print("=== Perceptron Training: AND Gate ===")

for epoch in range(20):
    errors = 0

    for x, y in zip(X, Y):
        pred = step(np.dot(x, w) + b)
        err = y - pred

        w += lr * err * x
        b += lr * err

        if err != 0:
            errors += 1

    print(f"Epoch {epoch+1}: Errors={errors}, w={w}, b={b:.2f}")

    if errors == 0:
        break

predictions = [step(np.dot(x, w) + b) for x in X]

print("\nPredictions:", predictions)
print("Expected:   ", Y)

x_line = np.linspace(-0.5, 1.5, 100)
y_line = -(w[0] * x_line + b) / w[1]

plt.scatter(X[:,0], X[:,1], c=Y)
plt.plot(x_line, y_line, 'r-', label="Decision Boundary")
plt.xlabel("X1")
plt.ylabel("X2")
plt.title("SLP - AND Gate")
plt.legend()
plt.grid()
plt.show()
