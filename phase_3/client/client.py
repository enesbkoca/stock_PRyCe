import time
import rpyc
import random

def send_request(symbol,cnt):
    try:
        conn = rpyc.connect('localhost', 8080)

        before_request = time.time()

        # print("Sending request")
        price, timestamp = conn.root.get_price(symbol)
        after_request = time.time()

        duration = after_request - before_request

        if price:
            print(f"Latest open price for {random_symbol} is ${price:.2f} | ({timestamp}) | {duration}", flush=True)
        else:
            print(f"Stock {random_symbol} not found or APIs not available", flush=True)

        conn.close()

    except Exception as e:
        if cnt < 3:
            print(f"Interface retrying to connect and search for the price of ",symbol)
            send_request(symbol,cnt+1)
        else:
            print(f"System is down!")


def app(symbol):
    send_request(symbol,0)


while True:
    symbols = [
            "AAPL", "GOOGL", "MSFT", "AMZN", "META", "TSLA", "NVDA", "JPM", "GS", "JNJ",
            "WMT", "PG", "DIS", "CSCO", "INTC", "ADBE", "NFLX", "CRM", "VZ",
            "KO", "PEP", "PFE", "MRK", "NKE", "BA", "GE", "IBM", "COST"
        ]
    random_symbol = random.choice(symbols)

    app(random_symbol)

    time.sleep(10)

    # try:
    #     conn = rpyc.connect('localhost', 8080)
    #
    #     symbols = [
    #         "AAPL", "GOOGL", "MSFT", "AMZN", "META", "TSLA", "NVDA", "JPM", "GS", "JNJ",
    #         "WMT", "PG", "DIS", "CSCO", "INTC", "ADBE", "NFLX", "CRM", "VZ",
    #         "KO", "PEP", "PFE", "MRK", "NKE", "BA", "GE", "IBM", "COST"
    #     ]
    #
    #     random_symbol = random.choice(symbols)
    #
    #     before_request = time.time()
    #
    #
    #     # print("Sending request")
    #     price, timestamp = conn.root.get_price(random_symbol)
    #     after_request = time.time()
    #
    #     duration = after_request - before_request
    #
    #     if price:
    #         print(f"Latest open price for {random_symbol} is ${price:.2f} | ({timestamp}) | {duration}", flush=True)
    #     else:
    #         print(f"Stock {random_symbol} not found or APIs not available", flush=True)
    #
    #     conn.close()
    #     time.sleep(15)
    #
    # except Exception as e:
    #     print(f"Client retrying to connect!")
