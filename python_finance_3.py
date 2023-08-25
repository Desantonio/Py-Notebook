import yfinance as yf
import matplotlib.pyplot as plt

def stock_function(start, end):
    stock = input("Enter the stock symbol: ")
    stock_data = yf.download(stock, start=start, end=end)
    
    dates = stock_data.index
    open_prices = stock_data['Open']

    plt.figure(figsize=(10, 6))
    plt.plot(dates, open_prices, label='Open Price')
    plt.xlabel('Date')
    plt.ylabel('Open Price')
    plt.title(f'Open Prices of {stock} from {start} to {end}')
    plt.legend()
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.show()

start_date = input("Enter the start date (YYYY-MM-DD): ")
end_date = input("Enter the end date (YYYY-MM-DD): ")
stock_function(start_date, end_date)
