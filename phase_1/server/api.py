import requests
import datetime as dt

ALPHA_VANTAGE_API_KEY = '128O8QIAV37G1SE0'  # '5LPFOU26RW6ESOZN'

def price_alpha(symbol):
    try:
        url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=1min&apikey={ALPHA_VANTAGE_API_KEY}'
        response = requests.get(url)

        data = response.json()

        # Check if 'Time Series (1min)' key exists and has data
        if 'Time Series (1min)' in data and data['Time Series (1min)']:
            latest_open_price = float(data['Time Series (1min)'][list(data['Time Series (1min)'].keys())[0]]['1. open'])
            timestamp = list(data['Time Series (1min)'].keys())[0]
            print(f"Returning latest open price for {symbol}:  ${latest_open_price:.2f} | Vantage Alpha | ({timestamp})")
            return latest_open_price, timestamp

        else:
            return None, None

    except Exception as e:
        print(f"Error retrieving stock price for {symbol}: {e}")
        return None, None


def price_yahoo(symbol):
    try:
        url = f"https://query1.finance.yahoo.com/v8/finance/chart/{symbol}"
        params = {
            "period1": "0",
            "period2": "9999999999",
            "interval": "1d",
            "events": "history"
        }
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}

        response = requests.get(url, params=params, headers=headers)
        data = response.json()

        if "chart" in data and "result" in data["chart"] and data["chart"]["result"]:
            stock_data = data["chart"]["result"][0]
            timestamps = stock_data["timestamp"]
            prices = stock_data["indicators"]["quote"][0]["close"]

            # Get the latest closing price and corresponding timestamp
            latest_price = prices[-1]
            timestamp = dt.datetime.utcfromtimestamp(timestamps[-1]).strftime("%Y-%m-%d %H:%M:%S")

            print(f"Returning latest open price for {symbol}:  ${latest_price:.2f} | Yahoo Finance | ({timestamp})")
            return latest_price, timestamp
        else:
            return None, None

    except Exception as e:
        print(f"Error retrieving stock price for {symbol}: {e}")

        return None, None


def get_price(symbol):
    price, timestamp = price_alpha(symbol)

    if not price or not timestamp:
        price, timestamp = price_yahoo(symbol)

    if not price or not timestamp:
        print("Failed to retreive price of ", symbol)

    return price, timestamp
