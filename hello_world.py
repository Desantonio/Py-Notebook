import math
from statistics import mean
def sin_function(start, end):
    result = []
    for x in range (start, end+1):
        result.append(math.sin(x))
    return result

start_range = 0
end_range = 1
final_result = sin_function(start_range, end_range)
print(final_result)
print("Hello World")

def function(t):
    return 1000 * math.exp(0.30 * t)

value_of_t = int(input("Enter the value of t: "))

print(function(value_of_t),"$")

def is_one_to_one(function_dict):
    # Collect the images (values) of the function
    values = list(function_dict.values())
    # If there are no duplicates, it's one-to-one
    return len(values) == len(set(values))

def is_onto(function_dict, codomain):
    # Check if all codomain elements are covered by the function
    return set(function_dict.values()) == set(codomain)

# Example: f(x) = 2x
function = {1: 2, 2: 4, 3: 6}
domain = [1, 2, 3]
codomain = [2, 4, 6, 8]

# Check if the function is one-to-one
one_to_one = is_one_to_one(function)
print("Is the function one-to-one:", one_to_one)

# Check if the function is onto
onto = is_onto(function, codomain)
print("Is the function onto:", onto)

# Create an empty array to store data points
data_points = []

# Get the number of data points from the user
num_data_points = int(input("Enter the number of data points: "))

# Get the data points from the user
for i in range(num_data_points):
    data_point = float(input(f"Enter data point {i+1}: "))
    data_points.append(data_point)

# Print the array of data points
print("Data points:", data_points)
print(mean(data_points))

import yfinance as yf

def invest(money):
    stock_symbol = str(input("Enter the Stock Symbol: "))
    stock_data = yf.Ticker(stock_symbol)
    current_close = stock_data.history(period="1d")
    close_info = current_close['Close'][0]
    invest_amount = money * close_info
    print(f"Your Total Investment in Stock {stock_symbol} is: {invest_amount}")

input_money = int(input("Enter the Capital to invest: "))
invest(input_money)