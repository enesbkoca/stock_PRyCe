import rpyc
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

            # Check if 'Time Series (1min)' key exists and has data
            if 'Time Series (1min)' in data and data['Time Series (1min)']:
                # Get the latest open price
                latest_open_price = data['Time Series (1min)'][list(data['Time Series (1min)'].keys())[0]]['1. open']
                print(f"Latest Open Price for {stock}: {latest_open_price}")
            else:
                latest_open_price = -1
                print("API calls limit")
            return float(latest_open_price)
        except Exception as e:
            print(f"Error retrieving stock price for {stock}: {e}")
            return None


if __name__ == "__main__":
    from rpyc.utils.server import ThreadedServer

    hostname = socket.gethostname()  # Get the hostname of the server
    ip_address = socket.gethostbyname(hostname)  # Get the IP address corresponding to the hostname
    print(f"Server starting on {hostname} ({ip_address})")  # Print or log the IP address
    t = ThreadedServer(StockPrice, port=18861)
    print("Server running at port", t.port)

    t.start()
