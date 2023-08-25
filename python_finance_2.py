import yfinance as yf

def to_know_open_price(stock_symbol):
    stock = yf.Ticker(stock_symbol)
    current_open_price = stock.info["open"]
    print(f"The Current Opening price of {stock_symbol} is: {current_open_price}")

def know_about_close_price(stock_symbol):
    stock = yf.Ticker(stock_symbol)
    current_close_price = stock.history(period="1d")['Close'][0]
    print(f"The Current Close Price of {stock_symbol} stock is: {current_close_price}")

def invest(stock_symbol, money):
    stock = yf.Ticker(stock_symbol)
    current_close = stock.history(period="1d")['Close'][0]
    total_investment = money * current_close
    print(f"Your Total Investment in Stock {stock_symbol} is: {total_investment}")

# Get opening price
symbol_input = input("Enter the Stock Symbol to get opening price: ")
to_know_open_price(symbol_input)

# Get closing price
symbol_input = input("Enter the Stock Symbol to get closing price: ")
know_about_close_price(symbol_input)

# Calculate investment
symbol_input = input("Enter the Stock Symbol to invest in: ")
capital = float(input("Enter the Capital to invest: "))
invest(symbol_input, capital)


import yfinance as yf
import matplotlib.pyplot as plt

# Fetch AAPL stock data for the specified period
start_date = "2023-06-01"
end_date = "2023-06-30"
aapl = yf.Ticker("AAPL")
data = aapl.history(start=start_date, end=end_date)

# Visualize the data using matplotlib
plt.figure(figsize=(10, 6))
plt.plot(data['Close'], label='AAPL Close Price')
plt.title('AAPL Stock Price - June 2023')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.legend()
plt.grid()
plt.show()

import matplotlib
import numpy as np

x = np.arange(1, 11)
y = np.array([1000, 1330, 1200, 1340, 1500, 1678, 950, 1570, 2000, 2020])

plt.figure(figsize=(8, 6))
plt.plot(x, y, marker='o')
plt.title("Data Visualization of a Shop's Daily Revenue")
plt.xlabel("No. of Days")
plt.ylabel("Daily Revenue")
plt.grid(True)
plt.show()

import matplotlib 
import numpy as np

x = np.arange(1, 6)
y = np.array([1000, 1200, 1500, 2000, 1900])

plt.figure(figsize=(8,8))
plt.plot(x, y, marker='o')
plt.title("Daily Profit on Algorithmic Trading")
plt.xlabel("Days")
plt.ylabel("Daily Profit")
plt.grid(True)
plt.show()