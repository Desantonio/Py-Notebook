import yfinance as yf
import firebase_admin
from firebase_admin import credentials, db

# Initialize Firebase
cred = credentials.Certificate("python-ee2b0-firebase-adminsdk-qj2a4-8771ae3964.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://python-ee2b0-default-rtdb.firebaseio.com/'
})

# Get user input for stock symbol
stock_symbol = input("Enter stock symbol: ")

# Fetch stock data
stock = yf.Ticker(stock_symbol)
stock_data = stock.history(period="1mo")

# Store stock data in Firebase
ref = db.reference(f'stock_data/{stock_symbol}')
existing_dates = ref.get()
if existing_dates:
    existing_dates = existing_dates.keys()
else:
    existing_dates = []

for index, row in stock_data.iterrows():
    date_str = index.strftime('%Y-%m-%d')
    
    if date_str not in existing_dates:
        data_to_store = {
            "Date": date_str,
            "Open": row['Open'],
            "High": row['High'],
            "Low": row['Low'],
            "Close": row['Close'],
            "Volume": row['Volume']
        }
        ref.child(date_str).set(data_to_store)
    else:
        print(f"Data for {date_str} already exists, skipping...")
