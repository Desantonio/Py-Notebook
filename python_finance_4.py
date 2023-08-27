import yfinance as yf

print("This is a stock data screener for the past month of entire stock data")

def stock_function(stock_symbol):
    stock = yf.Ticker(stock_symbol)
    stock_data = stock.history(period="1mo")
    print(stock_data)

input_stock_symbol = str(input("Enter the Stock Symbol: "))
result = stock_function(input_stock_symbol)
print(result)

aapl = yf.Ticker("AAPL")
price = aapl.history(period='1wk')
close = price['Close']
print(close)

import matplotlib.pyplot as plt

plt.figure(figsize=(10,6))
plt.plot(close, marker="o",label='Close Price')
plt.title("Plotting")
plt.xlabel("Dates")
plt.ylabel("Price $")
plt.legend()
plt.grid()
plt.show()

import yfinance as yf
import matplotlib.pyplot as plt

# Define the ticker symbols
aapl_symbol = "AAPL"
intc_symbol = "INTC"

# Create Ticker objects
aapl_ticker = yf.Ticker(aapl_symbol)
intc_ticker = yf.Ticker(intc_symbol)

# Get historical data for the past 1 month
aapl_data = aapl_ticker.history(period="1mo")
intc_data = intc_ticker.history(period="1mo")

# Plotting
plt.figure(figsize=(10, 6))

# Plot AAPL closing prices
plt.plot(aapl_data.index, aapl_data["Close"], label="AAPL")

# Plot INTC closing prices
plt.plot(intc_data.index, intc_data["Close"], label="INTC")

# Customize plot
plt.xlabel("Date")
plt.ylabel("Closing Price")
plt.title("AAPL vs INTC Closing Prices")
plt.xticks(rotation=45)
plt.legend()

# Show plot
plt.tight_layout()
plt.show()
