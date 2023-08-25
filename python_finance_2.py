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
