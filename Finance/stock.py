import yfinance as yf
import matplotlib.pyplot as plt

symbol = "AAPL"
stock = yf.Ticker(symbol)
history = stock.history(start="2023-01-30",end="2023-03-30")
close = history["Close"]

plt.figure(figsize=(10,6))
plt.bar(close.index, close, bottom=None, width=0.5, align="center")
plt.xlabel("Close Prices")
plt.ylabel("Dates")
plt.xticks(rotation=0)
plt.legend()
plt.title(symbol)
plt.grid()
plt.show()