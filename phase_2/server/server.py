import rpyc
import socket
import time
from api import get_price


class StockPrice(rpyc.Service):
    def on_connect(self, conn):
        pass

    def on_disconnect(self, conn):
        pass

    def exposed_get_price(self, stock):
        # time.sleep(10)

        stock_price = 10, "23:34"
        # stock_price = get_price(stock)
        return stock_price


if __name__ == "__main__":
    from rpyc.utils.server import ThreadedServer

    hostname = socket.gethostname()  # Get the hostname of the server
    ip_address = socket.gethostbyname(hostname)  # Get the IP address corresponding to the hostname
    print(f"Server starting on {hostname} ({ip_address})")  # Print or log the IP address
    t = ThreadedServer(StockPrice, port=18861)
    print("Server running at port", t.port)

    t.start()
