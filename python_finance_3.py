import sys
import yfinance as yf
import matplotlib.pyplot as plt

def stock_function(start, end, stock_symbol):
    stock_data = yf.download(stock_symbol, start=start, end=end)
    
    dates = stock_data.index
    open_prices = stock_data['Open']

    plt.figure(figsize=(10, 6))
    plt.plot(dates, open_prices, label='Open Price')
    plt.xlabel('Date')
    plt.ylabel('Open Price')
    plt.title(f'Open Prices of {stock_symbol} from {start} to {end}')
    plt.legend()
    plt.xticks(rotation=45)
    plt.grid(True)

    # Save the plot as an image file
    plt.savefig('/app/plot.png')

    plt.close()  # Close the plot to free up resources

if len(sys.argv) != 4:
    print("Usage: python python_finance_3.py <start_date> <end_date> <stock_symbol>")
    sys.exit(1)

start_date = sys.argv[1]
end_date = sys.argv[2]
stock_symbol = sys.argv[3]

stock_function(start_date, end_date, stock_symbol)
