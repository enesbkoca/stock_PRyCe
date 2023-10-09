import rpyc
import sys
import random
import socket
import requests


class StockPrice(rpyc.Service):
    ALPHA_VANTAGE_API_KEY = '5LPFOU26RW6ESOZN'

    def on_connect(self, conn):
        pass

    def on_disconnect(self, conn):
        pass

    def exposed_get_price(self, stock):
        try:
            url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={stock}&interval=1min&apikey={self.ALPHA_VANTAGE_API_KEY}'
            response = requests.get(url)
            data = response.json()
            latest_close_price = data['Time Series (1min)'][list(data['Time Series (1min)'].keys())[0]]['4. close']
            return float(latest_close_price)
        except Exception as e:
            print(f"Error retrieving stock price for {stock}: {e}")
            return None
        # stock_price = random.uniform(0, 150)
        # print(f"Price of {stock} at ${stock_price:.2f}", flush=True)
        # return stock_price


if __name__ == "__main__":
    from rpyc.utils.server import ThreadedServer

    hostname = socket.gethostname()  # Get the hostname of the server
    ip_address = socket.gethostbyname(hostname)  # Get the IP address corresponding to the hostname
    print(f"Server starting on {hostname} ({ip_address})")  # Print or log the IP address
    t = ThreadedServer(StockPrice, port=18861)
    print("Server running at port", t.port)
    # Redirect logs to stdout
    sys.stdout = sys.stderr = open("/dev/stdout", "w")

    t.start()
