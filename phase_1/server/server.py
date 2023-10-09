import rpyc
import sys
import random
import socket


class StockPrice(rpyc.Service):
    def on_connect(self, conn):
        pass

    def on_disconnect(self, conn):
        pass

    def exposed_get_price(self, stock):
        stock_price = random.uniform(0, 150)
        print(f"Price of {stock} at ${stock_price:.2f}", flush=True)
        return stock_price


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
