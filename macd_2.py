import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle
from kivy.properties import ObjectProperty

class MACDIndicatorApp(App):
    def build(self):
        # Get user input for stock symbol
        stock_symbol = input("Enter the stock symbol (e.g., AAPL): ")

        # Get user input for the start and end dates
        start_date = input("Enter the start date (YYYY-MM-DD): ")
        end_date = input("Enter the end date (YYYY-MM-DD): ")

        # Download historical stock price data using yfinance
        df = yf.download(stock_symbol, start=start_date, end=end_date)

        # Define MACD parameters
        short_window = 12
        long_window = 26
        signal_window = 9

        # Calculate the short-term and long-term EMAs
        short_ema = df['Close'].ewm(span=short_window, adjust=False).mean()
        long_ema = df['Close'].ewm(span=long_window, adjust=False).mean()

        # Calculate the MACD line
        macd = short_ema - long_ema

        # Calculate the signal line
        signal_line = macd.ewm(span=signal_window, adjust=False).mean()

        # Initialize buy and sell signals lists
        buy_signals = []
        sell_signals = []

        # Determine buy and sell signals
        for i in range(1, len(df)):
            if macd[i] > signal_line[i] and macd[i - 1] <= signal_line[i - 1]:
                buy_signals.append(df.index[i])
            elif macd[i] < signal_line[i] and macd[i - 1] >= signal_line[i - 1]:
                sell_signals.append(df.index[i])

        # Create a Kivy layout
        layout = BoxLayout(orientation='vertical')

        # Add a title label
        title_label = Label(
            text=f'MACD Indicator with Buy/Sell Signals for {stock_symbol}',
            font_size=18,
            size_hint=(1, 0.1)
        )
        layout.add_widget(title_label)

        # Create a custom Kivy widget to display the Matplotlib plot
        plot_widget = PlotWidget(df.index, macd, signal_line, buy_signals, sell_signals)
        layout.add_widget(plot_widget)

        # Display the Kivy app
        return layout

class PlotWidget(Widget):
    def __init__(self, date, macd, signal_line, buy_signals, sell_signals, **kwargs):
        super().__init__(**kwargs)
        self.date = date
        self.macd = macd
        self.signal_line = signal_line
        self.buy_signals = buy_signals
        self.sell_signals = sell_signals

    def on_touch_down(self, touch):
        # Handle touch events (e.g., display buy/sell information)
        if self.buy_signals and self.collide_point(*touch.pos):
            for x, y in self.buy_signals:
                if x - 0.01 <= touch.pos[0] <= x + 0.01 and y - 0.01 <= touch.pos[1] <= y + 0.01:
                    print(f"Buy Signal at {x.strftime('%Y-%m-%d')}")
        elif self.sell_signals and self.collide_point(*touch.pos):
            for x, y in self.sell_signals:
                if x - 0.01 <= touch.pos[0] <= x + 0.01 and y - 0.01 <= touch.pos[1] <= y + 0.01:
                    print(f"Sell Signal at {x.strftime('%Y-%m-%d')}")

    def on_size(self, instance, value):
        # Update the widget size and position
        self.pos = (self.center_x - self.width / 2, self.center_y - self.height / 2)

    def on_touch_move(self, touch):
        pass

if __name__ == '__main__':
    MACDIndicatorApp().run()
