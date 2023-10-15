import time
import rpyc
import random

response_times = []

conn = rpyc.connect('localhost', 80)
print("Connected")

while True:
    symbols = [
        "AAPL", "GOOGL", "MSFT", "AMZN", "META", "TSLA", "NVDA", "JPM", "GS", "JNJ",
        "WMT", "PG", "DIS", "CSCO", "INTC", "ADBE", "NFLX", "CRM", "VZ",
        "KO", "PEP", "PFE", "MRK", "NKE", "BA", "GE", "IBM", "COST"
    ]

    random_symbol = random.choice(symbols)

    before_request = time.time()
    price, timestamp = conn.root.get_price(random_symbol)
    after_request = time.time()

    duration = after_request - before_request

    response_times.append(duration)
    avg = sum(response_times)/len(response_times)


    if price:
        print(f"Latest open price for {random_symbol} is ${price:.2f} | ({timestamp}) | {avg}", flush=True)
    else:
        print(f"Stock {random_symbol} not found or APIs not available", flush=True)

    time.sleep(5)
 