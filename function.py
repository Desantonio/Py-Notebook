import math
from statistics import mean, median, mode, stdev, variance

data_points = []

input_values = int(input("Enter the total number of data points: "))

for i in range(input_values):
    data_points_individual = int(input(f"Enter data point{i+1}: "))
    data_points.append(data_points_individual)

print("Data Points: ", data_points)

print("The Mean is: ", mean(data_points))

print("The Median is: ", median(data_points))

try:
    mode_of = mode(data_points)
    print("The Mode is: ", mode_of)
except:
    print("Mode doesn't exist")

print("The Maximum value is: ", max(data_points))
print("The Minimum value is: ", min(data_points))


for i in range(data_points_individual):
    deviations = data_points[i] - mean(data_points)
    print(f"The Deviation for Data point{i+1} is: ", deviations)

print("The Variance is: ", variance(data_points))
print("The Standard Deviation is: ", stdev(data_points))

for i in range(data_points_individual):
    sin_of_data_points = math.sin(data_points[i])
    print(f"The sin of Data Point{i+1} is: ", sin_of_data_points)

def sin_sum_function(data_points):
    total = 0
    for i in range(len(data_points)):
        sin_sum = sin_of_data_points
        total += sin_sum
    return total
sin_sum_of_all_data_points = data_points
print(sin_sum_function(sin_sum_of_all_data_points))

for i in range(data_points_individual):
    cos_of_data_points = math.cos(data_points[i])
    print(f"The cos of Data Point{i+1} is: ", cos_of_data_points)

def cos_sum_function(data_points):
    total = 0
    for i in range(len(data_points)):
        cos_sum = cos_of_data_points
        total += cos_sum
    return total
cos_sum_of_all_data_points = data_points
print(cos_sum_function(cos_sum_of_all_data_points))

def function(i):
    variable = math.log(i)*math.sin(i)/math.cos(i)
    return variable
print(function(100))

def function_2(start, end):
    total = 0
    for i in range(start, end+1):
        total += function(i)
    return total
start_range = 100
end_range = 500
print(function_2(start_range, end_range))

def function_3(c):
    variable_c = (math.sin(c) + math.cos(c))
    return variable_c

def function_4(start, end):
    total = 0
    for i in range(start, end+1):
        total += function_3(i)
    return total
start_range_2 = -100
end_range_2 = 100
print(function_4(start_range_2, end_range_2))

def function_5(i):
    func_variable = math.sin(2*i)**2*math.cos(5*i)/math.log(2*i)
    return func_variable
input_value = float(input("Enter the value of i: "))
print(function_5(input_value))

enter_string = str(input("Enter your full name: "))
count_enter_string = len(enter_string)
print(count_enter_string)

def function_6(h):
    variable_h = math.sqrt(h)
    return variable_h
input_h = float(input("Enter the value of h: "))
print(function_6(input_h))

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter your operation: ")

if operator == '+':
    print(num1 + num2)
elif operator == '-':
    print(num1 - num2)
elif operator == '/':
    print(num1 / num2)
elif operator == '*':
    print(num1 * num2)

def check_even_or_odd(number):
    if number % 2 == 0:
        print(f"The {number} is Even")
    else:
        print(f"The {number} is Odd")


input_number = int(input("Enter your number: "))
check_even_or_odd(input_number)

def check_even_odd(start, end):
    for i in range(start, end+1):
        check_even_or_odd(i)

start_range = int(input("Enter the starting range number: "))
end_range = int(input("Enter the ending range number: "))
print(check_even_odd(start_range, end_range))

def basic_function(x):
    return math.sin(x)*math.tan(x)*(1/math.cos(x))
print(basic_function(10))