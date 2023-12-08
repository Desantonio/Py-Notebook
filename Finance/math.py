import numpy as np
import matplotlib.pyplot as plt

a = []
input_a = int(input("How many data points do you want to enter: "))
for i in range(input_a):
    individual = float(input(f"Enter data point {i+1}: "))
    a.append(individual)

print("Your array is here", a)


x = np.array(list(range(1, input+1)))
y = np.array(a)

plt.figure(figsize=(8,6))
plt.bar(x, height=y, bottom=None, align="center", width=0.8)
plt.legend()
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.title("Plot/Graph")
plt.grid()
plt.show()