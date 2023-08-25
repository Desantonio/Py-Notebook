import matplotlib.pyplot as plt

# Your input commands
input_data = input("Enter data: ")
print("You entered:", input_data)

# Matplotlib plot
x = [1, 2, 3, 4, 5]
y = [10, 8, 6, 4, 2]
plt.plot(x, y, marker='o')
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Matplotlib Plot")
plt.show()
