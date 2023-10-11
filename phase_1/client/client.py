import time
import rpyc
import random

conn = rpyc.connect("localhost", 18861)
print("Connected")

while True:
    symbols = [
        "AAPL", "GOOGL", "MSFT", "AMZN", "META", "TSLA", "NVDA", "JPM", "GS", "JNJ",
        "WMT", "PG", "DIS", "CSCO", "INTC", "ADBE", "NFLX", "CRM", "VZ",
        "KO", "PEP", "PFE", "MRK", "NKE", "BA", "GE", "IBM", "COST"
    ]

    random_symbol = random.choice(symbols)
    price, timestamp = conn.root.get_price(random_symbol)

    if price is None:
        print(f"Stock {random_symbol} not found.", flush=True)
    elif price == -1:
        print(f"API limit reached.", flush=True)
    else:
        print(f"Latest open price for {random_symbol} is ${price:.2f} | ({timestamp})", flush=True)

    time.sleep(5)
 