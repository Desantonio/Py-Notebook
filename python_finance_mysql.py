import yfinance as yf
import mysql.connector
from mysql.connector import Error

# MySQL database configuration
db_config = {
    'host': 'localhost',
    'database': 'stock_data',
    'user': 'root',
    'password': 'Vatsal%1'
}

# Connect to MySQL database
try:
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()

    # Get stock symbols from the user
    stock_symbols = input("Enter stock symbols (comma-separated): ").split(',')

    # Fetch stock data for the last month and store in individual tables
    for symbol in stock_symbols:
        # Create a table for the stock symbol if it doesn't exist
        create_table_query = (
            f"CREATE TABLE IF NOT EXISTS {symbol}_data ("
            "id INT AUTO_INCREMENT PRIMARY KEY,"
            "date DATE NOT NULL,"
            "open FLOAT,"
            "high FLOAT,"
            "low FLOAT,"
            "close FLOAT,"
            "volume BIGINT,"
            "UNIQUE KEY unique_date (date)"
            ")"
        )
        cursor.execute(create_table_query)
        connection.commit()

        stock = yf.Ticker(symbol.strip())
        data = stock.history(period="1mo")
        for index, row in data.iterrows():
            insert_query = (
                f"INSERT IGNORE INTO {symbol}_data "
                "(date, open, high, low, close, volume) "
                "VALUES (%s, %s, %s, %s, %s, %s)"
            )
            values = (index.date(), row['Open'], row['High'], row['Low'], row['Close'], row['Volume'])
            cursor.execute(insert_query, values)
            connection.commit()

except Error as e:
    print("Error:", e)

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
