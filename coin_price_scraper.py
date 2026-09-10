import requests
import csv

# Function to fetch and format cryptocurrency price data

def get_crypto_price(symbol='BTC', exchange='Binance'):
    url = f'https://api.{exchange.lower()}.com/api/v3/ticker/price?symbol={symbol}{exchange[:-1].upper()}'
    response = requests.get(url)
    data = response.json()
    price = data['price']
    return price

# Function to write data into CSV file
def write_csv(data, symbol, exchange, filename='prices.csv'):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Exchange', 'Symbol', 'Price'])
        writer.writerow([exchange, symbol, data])

    print(f'CSV file has been saved as {filename}')

# Fetch and write Bitcoin price from Binance
symbol = 'BTC'
exchange = 'Binance'
price = get_crypto_price(symbol, exchange)
write_csv(price, symbol, exchange)