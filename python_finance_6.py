import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
import math

billion = 10**9

# Define the companies and their tickers
companies = {
    "Apple": "AAPL",
    "Google": "GOOGL",
    "Microsoft": "MSFT",
    "Meta": "META"
}

# Initialize a list to store company data
company_data = []

# Fetch and process data for each company
for company_name, ticker_symbol in companies.items():
    company = yf.Ticker(ticker_symbol)
    marketcap_data = company.history(period="10y")["Close"] / billion
    company_data.append((company_name, marketcap_data))

# Create the plot
plt.figure(figsize=(12, 8))
for company_name, marketcap_data in company_data:
    plt.plot(marketcap_data, label=company_name)

# Adding dots for each year
for year in range(marketcap_data.index[0].year, marketcap_data.index[-1].year + 1):
    year_data = marketcap_data[marketcap_data.index.year == year]
    plt.scatter(year_data.index, year_data, color='gray', s=40, alpha=0.6)

plt.title("Market Capitalization over the Years")
plt.xlabel("Years")
plt.ylabel("Market Capitalization (in billions)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.xticks(rotation=45)
plt.show()
