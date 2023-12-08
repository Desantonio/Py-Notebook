from polygon import RESTClient
client = RESTClient("DaJzs8CmmpJ1xPsSXxoTzpk3wkpm_yaU")
apple = client.get_aggs("AAPL", 1, "day", "2023-01-30", "2023-03-30")
close = list(apple.close)
print(close)