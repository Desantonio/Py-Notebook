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