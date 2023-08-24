import yfinance as yf
import mysql.connector
from mysql.connector import Error

# Connect to the MySQL database
try:
    connection = mysql.connector.connect(
        host='localhost',
        database='mydb',
        user='root',
        password='Vatsal%1'
    )

    if connection.is_connected():
        cursor = connection.cursor()

        # Create the apple_stock_info table if it doesn't exist
        create_table_query = '''
        CREATE TABLE IF NOT EXISTS apple_stock_info (
            Date DATE PRIMARY KEY,
            Open FLOAT,
            High FLOAT,
            Low FLOAT,
            Close FLOAT,
            Volume INT
        )
        '''
        cursor.execute(create_table_query)
        connection.commit()

        # Fetch Apple stock data for the past month
        aapl = yf.Ticker("AAPL")
        stock_data = aapl.history(period="1mo")

        # Insert stock data into the table
        for index, row in stock_data.iterrows():
            insert_query = '''
            INSERT IGNORE INTO apple_stock_info (Date, Open, High, Low, Close, Volume)
            VALUES (%s, %s, %s, %s, %s, %s)
            '''
            data = (index.date(), row['Open'], row['High'], row['Low'], row['Close'], row['Volume'])
            cursor.execute(insert_query, data)
            connection.commit()

        print("Data inserted successfully")

except Error as e:
    print("Error:", e)

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("Connection closed")
