import yfinance as yf
import statistics

def stock_signal(symbol):
    stock = yf.Ticker(symbol)
    history = stock.history(period="1y")
    close = history["Close"]
    mean = statistics.mean(close)
    fifty_day = mean/50
    two_hundred_day = mean/200
    three_hundred_day = mean/300
    if fifty_day >= two_hundred_day >= three_hundred_day:
        print("Buy Signal","for", symbol)
    else:
        print("Sell Signal", "for", symbol)

input_stock_symbol = str(input("Enter the stock symbol: "))
result = stock_signal(input_stock_symbol)
print(result)