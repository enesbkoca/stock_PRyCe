import time
import rpyc
from string import ascii_uppercase
from random import choices

conn = rpyc.connect("localhost", 18861)
print("Connected")

while True:
    index = "".join(choices(ascii_uppercase, k=3))
    price = conn.root.get_price(index)
    print(f"Price of {index} is ${price:.2f}", flush=True)
    time.sleep(5)
