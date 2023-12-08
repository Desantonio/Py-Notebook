import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Get user input for stock symbol
stock_symbol = input("Enter the stock symbol (e.g., AAPL): ")

# Get user input for the start and end dates
start_date = input("Enter the start date (YYYY-MM-DD): ")
end_date = input("Enter the end date (YYYY-MM-DD): ")

# Download historical stock price data using yfinance
df = yf.download(stock_symbol, start=start_date, end=end_date)

# Define MACD parameters
short_window = 12
long_window = 26
signal_window = 9

# Calculate the short-term and long-term EMAs
short_ema = df['Close'].ewm(span=short_window, adjust=False).mean()
long_ema = df['Close'].ewm(span=long_window, adjust=False).mean()

# Calculate the MACD line
macd = short_ema - long_ema

# Calculate the signal line
signal_line = macd.ewm(span=signal_window, adjust=False).mean()

# Calculate the MACD histogram
macd_histogram = macd - signal_line

# Plot the MACD indicator
plt.figure(figsize=(12, 6))
plt.plot(df.index, macd, label='MACD', color='blue')
plt.plot(df.index, signal_line, label='Signal Line', color='orange')
plt.bar(df.index, macd_histogram, label='MACD Histogram', color='green', alpha=0.5)
plt.legend()
plt.title(f'MACD Indicator for {stock_symbol}')
plt.xlabel('Date')
plt.ylabel('MACD Value')
plt.show()
