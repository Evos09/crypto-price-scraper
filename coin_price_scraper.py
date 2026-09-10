import requests
import json

def get_crypto_price(symbol, exchange):
    url = f'https://api.example.com/v1/price?symbol={symbol}&exchange={exchange}'
    response = requests.get(url)
    data = response.json()
    if 'price' in data:
        price = data['price']
    else:
        print('Price key not found, using fallback method.')
        price = 'N/A'
    return price

def main():
    symbol = 'BTC'
    exchange = 'Coinbase'
    price = get_crypto_price(symbol, exchange)
    print(f'The price of {symbol} on {exchange} is: {price}')

if __name__ == '__main__':
    main()