import yfinance as yf

a = yf.Ticker("ORCL")

b = a.info["open"]

print("The Current Opening Price of Oracle Stock is: ", b)