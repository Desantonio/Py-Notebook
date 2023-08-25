import yfinance as yf

print("This is a stock data screener for the past month of entire stock data")

def stock_function(stock_symbol):
    stock = yf.Ticker(stock_symbol)
    stock_data = stock.history(period="1mo")
    print(stock_data)

input_stock_symbol = str(input("Enter the Stock Symbol: "))
result = stock_function(input_stock_symbol)
print(result)