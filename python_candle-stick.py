import yfinance as yf
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Define the stock symbol (AAPL) and the date range
symbol = "AAPL"
start_date = "2022-08-31"
end_date = "2023-08-31"

# Fetch the stock data from Yahoo Finance
df = yf.download(symbol, start=start_date, end=end_date)

# Create a figure and axis for the candlestick chart
fig, ax = plt.subplots(figsize=(12, 6))

# Convert date index to numerical format required by matplotlib
df['Date'] = mdates.date2num(df.index.to_pydatetime())

# Plot candlestick chart
candlestick = ax.vlines(df['Date'], df['Low'], df['High'], color='black', linewidth=2)
ohlc = ax.vlines(df['Date'], df['Open'], df['Close'], color='blue', linewidth=8)

# Format x-axis as dates
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))

# Set labels and title
ax.set_xlabel("Date")
ax.set_ylabel("Price")
ax.set_title(f"Candlestick Chart for {symbol}")

# Show the chart
plt.show()


import yfinance as yf
import matplotlib.pyplot as plt
import mplfinance as mpf

# Define the period for which you want to fetch Apple stock data (1 year)
start_date = '2022-09-04'
end_date = '2023-09-04'

# Fetch Apple stock data using yfinance
apple_data = yf.download('AAPL', start=start_date, end=end_date)

# Create the candlestick chart
mpf.plot(apple_data, type='candle', title='Apple Inc. Candlestick Chart', style='charles')

# Display the candlestick chart
plt.show()


import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Define the period for historical data
start_date = '2022-09-04'
end_date = '2023-09-04'

# Fetch Apple stock data using yfinance
apple_data = yf.download('AAPL', start=start_date, end=end_date)

# Prepare the data
apple_data['Date'] = apple_data.index
apple_data.reset_index(drop=True, inplace=True)
apple_data['Date'] = apple_data['Date'].apply(lambda x: x.toordinal())

# Use the 'Close' prices as the target variable
y = apple_data['Close']

# Use the 'Date' as the feature for prediction
X = apple_data[['Date']]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train a linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict stock prices
y_pred = model.predict(X_test)

# Calculate the Mean Squared Error (MSE) to evaluate the model
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")

# Create a beautiful chart to visualize the results
plt.figure(figsize=(12, 6))
plt.scatter(X_test, y_test, color='blue', label='Actual Prices', alpha=0.6)
plt.plot(X_test, y_pred, color='red', linewidth=2, label='Predicted Prices')
plt.title('Apple Stock Price Prediction')
plt.xlabel('Date (Ordinal)')
plt.ylabel('Stock Price (USD)')
plt.legend()
plt.grid(True)
plt.show()




import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Define the period for historical data
start_date = '2022-09-04'
end_date = '2023-09-04'

# Fetch Apple stock data using yfinance
apple_data = yf.download('AAPL', start=start_date, end=end_date)

# Prepare the data
apple_data['Date'] = apple_data.index
apple_data.reset_index(drop=True, inplace=True)
apple_data['Date'] = apple_data['Date'].apply(lambda x: x.toordinal())

# Use the 'Close' prices as the target variable
y = apple_data['Close']

# Use the 'Date' as the feature for prediction
X = apple_data[['Date']]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train a linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict stock prices
y_pred = model.predict(X_test)

# Calculate the Mean Squared Error (MSE) to evaluate the model
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")

# Calculate the residuals (differences between actual and predicted prices)
residuals = y_test - y_pred

# Create a beautiful chart to visualize the results
plt.figure(figsize=(12, 6))
plt.scatter(X_test, y_test, color='blue', label='Actual Prices', alpha=0.6)
plt.plot(X_test, y_pred, color='red', linewidth=2, label='Predicted Prices')
plt.title('Apple Stock Price Prediction')
plt.xlabel('Date (Ordinal)')
plt.ylabel('Stock Price (USD)')
plt.legend()
plt.grid(True)

# Add residual sticks (vertical lines)
for i in range(len(X_test)):
    plt.vlines(X_test.iloc[i], y_test.iloc[i], y_test.iloc[i] - residuals.iloc[i], color='green', alpha=0.6)

plt.show()



import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Define the period for historical data
start_date = '2022-09-04'
end_date = '2023-09-04'

# Fetch Apple stock data using yfinance
apple_data = yf.download('AAPL', start=start_date, end=end_date)

# Prepare the data
apple_data['Date'] = apple_data.index
apple_data.reset_index(drop=True, inplace=True)
apple_data['Date'] = apple_data['Date'].apply(lambda x: x.toordinal())

# Use the 'Close' prices as the target variable
y = apple_data['Close']

# Use the 'Date' as the feature for prediction
X = apple_data[['Date']]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train a linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict stock prices
y_pred = model.predict(X_test)

# Calculate the Mean Squared Error (MSE) to evaluate the model
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")

# Calculate the residuals (differences between actual and predicted prices)
residuals = y_test - y_pred

# Create a DataFrame to display the data
results_df = pd.DataFrame({'Actual Prices': y_test, 'Predicted Prices': y_pred, 'Residuals': residuals})
print(results_df)

# Create a beautiful chart to visualize the results
plt.figure(figsize=(12, 6))
plt.scatter(X_test, y_test, color='blue', label='Actual Prices', alpha=0.6)
plt.plot(X_test, y_pred, color='red', linewidth=2, label='Predicted Prices')
plt.title('Apple Stock Price Prediction')
plt.xlabel('Date (Ordinal)')
plt.ylabel('Stock Price (USD)')
plt.legend()
plt.grid(True)

# Add residual sticks (vertical lines)
for i in range(len(X_test)):
    plt.vlines(X_test.iloc[i], y_test.iloc[i], y_test.iloc[i] - residuals.iloc[i], color='green', alpha=0.6)

plt.show()





import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Define the period for historical data
start_date = '2022-09-04'
end_date = '2023-09-04'

# Fetch Apple stock data using yfinance
apple_data = yf.download('AAPL', start=start_date, end=end_date)

# Prepare the data
apple_data['Date'] = apple_data.index
apple_data.reset_index(drop=True, inplace=True)
apple_data['Date'] = apple_data['Date'].apply(lambda x: x.toordinal())

# Use the 'Close' prices as the target variable
y = apple_data['Close']

# Use the 'Date' as the feature for prediction
X = apple_data[['Date']]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train a linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict stock prices
y_pred = model.predict(X_test)

# Calculate the Mean Squared Error (MSE) to evaluate the model
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")

# Calculate the residuals (differences between actual and predicted prices)
residuals = y_test - y_pred

# Create a DataFrame to display the data
results_df = pd.DataFrame({'Date': X_test['Date'], 'Actual Price': y_test, 'Predicted Price': y_pred, 'Residuals': residuals})

# Create a beautiful chart to visualize the results
plt.figure(figsize=(12, 6))
plt.scatter(X_test, y_test, color='blue', label='Actual Prices', alpha=0.6)
plt.plot(X_test, y_pred, color='red', linewidth=2, label='Predicted Prices')
plt.title('Apple Stock Price Prediction')
plt.xlabel('Date (Ordinal)')
plt.ylabel('Stock Price (USD)')
plt.legend()
plt.grid(True)

# Add residual sticks (vertical lines)
for i in range(len(X_test)):
    plt.vlines(X_test.iloc[i], y_test.iloc[i], y_test.iloc[i] - residuals.iloc[i], color='green', alpha=0.6)

# Display the table
print(results_df)
plt.show()


import math

def even_odd(number):
    if number % 2:
        return f"{number} is even"
    else:
        return f"{number} is odd"
    return

number = int(input("Enter: "))
print(even_odd(number))

import math
def func(n):
    return (4**n*math.factorial(n+1))/n**(n+1)
input_n = int(input("Enter the value of n: "))
result = func(input_n) 
print(result)