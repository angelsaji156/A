
import matplotlib.pyplot as plt

# Triangular membership function
def tri(x, a, b, c):
    if a == b and x <= b:
        return 1
    elif b == c and x >= b:
        return 1
    elif x <= a or x >= c:
        return 0
    elif x == b:
        return 1
    elif x < b:
        return (x-a)/(b-a)
    else:
        return (c-x)/(c-b)

# Input
load = float(input("Enter Load (0-100): "))
dirt = float(input("Enter Dirt (0-100): "))

# 1. Fuzzification
L = [tri(load, 0, 0, 50),
     tri(load, 25, 50, 75),
     tri(load, 50, 100, 100)]

D = [tri(dirt, 0, 0, 50),
     tri(dirt, 25, 50, 75),
     tri(dirt, 50, 100, 100)]

# 2. Rule Evaluation
short = min(L[0], D[0])
normal = min(L[1], D[1])
long = max(min(L[2], D[2]), min(L[1], D[2]))

# 3. Aggregation and Defuzzification
num = den = 0

for x in range(61):
    s = tri(x, 0, 0, 30)
    n = tri(x, 15, 30, 45)
    l = tri(x, 30, 60, 60)

    mu = max(min(short, s),
             min(normal, n),
             min(long, l))

    num += x * mu
    den += mu

if den == 0:
    print("No rule activated")
    result = 0
else:
    result = num / den
    print("Washing Time:", round(result, 2), "minutes")

# 4. Plot Membership Functions
x = range(101)

plt.subplot(1, 2, 1)
plt.plot(x, [tri(i, 0, 0, 50) for i in x], label="Light")
plt.plot(x, [tri(i, 25, 50, 75) for i in x], label="Medium")
plt.plot(x, [tri(i, 50, 100, 100) for i in x], label="Heavy")
plt.title("Load Membership Functions")
plt.xlabel("Load")
plt.ylabel("Membership")
plt.legend()
plt.grid()

x = range(61)

plt.subplot(1, 2, 2)
plt.plot(x, [tri(i, 0, 0, 30) for i in x], label="Short")
plt.plot(x, [tri(i, 15, 30, 45) for i in x], label="Normal")
plt.plot(x, [tri(i, 30, 60, 60) for i in x], label="Long")
plt.axvline(result, color="black", linestyle="--", label="Output")
plt.title("Washing Time Membership Functions")
plt.xlabel("Time (minutes)")
plt.ylabel("Membership")
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()
