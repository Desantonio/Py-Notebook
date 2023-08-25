import yfinance as yf

a = yf.Ticker("ORCL")

b = a.info["open"]

print("The Current Opening Price of Oracle Stock is: ", b)

#This is a stock price screener on a terminal

def to_know_open_price(open_price):
    stock_symbol = yf.Ticker(open_price)
    current_open_price_st = stock_symbol.info["open"]
    print(f"The Current Opening price of {open_price} is: ", current_open_price_st)

input_symbol = str(input("Enter the Stock Symbol: "))
final_result = to_know_open_price(input_symbol)
print(final_result)

def know_about_close_price(close_price):
    stock_symbol = yf.Ticker(close_price)
    current_close_price = stock_symbol.history(period="1d")
    current_info = current_close_price['Close'][0]
    print(f"The Current Close Price of {close_price} stock is: ", current_info)
input = str(input("Enter the Stock Symbol in which you would want to invest your Total Capital in: "))
result = know_about_close_price(input)
print(result)


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
