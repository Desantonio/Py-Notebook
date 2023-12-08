a = 50
def func():
    if a == 50:
        print("Yes")
    else: 
        print("No")
    return
func()

num1 = float(input("Enter your first value: "))
num2 = float(input("Enter your second value: "))
operator = input("Enter the operation to perform: ")

def func_operator(operator):
    if operator == "+":
        print(num1+num2)
    elif operator == "-":
        print(num1-num2)
    elif operator == "*":
        print(num1*num2)
    elif operator == "/":
        print(num1/num2)
    return
operator_input = operator
print(func_operator(operator_input))

array = []
array_input = int(input("Enter total no. of your datapoints: "))

for x in range(array_input):
    data_points_individual = float(input(f"Enter the data point{x+1}: "))
    array.append(data_points_individual)

print("Your array is: ", array)

for x in range(array_input):
    x = (f"{array_input+1}")

import matplotlib.pyplot as plt
x_values = list(range(1, array_input + 1))
plt.figure(figsize=(6,3))
plt.plot(x_values,array,marker='o')
plt.xlabel("")
plt.ylabel("")
plt.title("")
plt.legend()
plt.grid()
plt.show()