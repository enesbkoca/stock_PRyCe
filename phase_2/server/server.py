import rpyc
import socket
import os
from api import get_price
from rpyc.utils.server import ThreadedServer


class StockPrice(rpyc.Service):
    def on_connect(self, conn):
        print("Client Connected")
        pass

    def on_disconnect(self, conn):
        print("Client Disconnected")
        pass

    def exposed_get_price(self, stock):
        stock_price = get_price(stock)
        return stock_price


if __name__ == "__main__":
    hostname = socket.gethostname()  # Get the hostname of the server
    ip_address = socket.gethostbyname(hostname)  # Get the IP address corresponding to the hostname
    print(f"Server starting on {hostname} ({ip_address})")  # Print or log the IP address

    port = int(os.environ.get("PORT", 18861))
    t = ThreadedServer(StockPrice, port=port)
    print("Server running at port", t.port)

    t.start()
