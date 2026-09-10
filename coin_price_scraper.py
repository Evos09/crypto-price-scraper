#!/usr/bin/env python3
import requests


BASE_URL = 'https://api.coinpaprika.com/v1'


def get_crypto_price(symbol: str, exchange: str) -> float:
    url = f'{BASE_URL}/ticker/{symbol}/ohlcv?interval=daily&exchange={exchange}'
    response = requests.get(url)
    data = response.json()
    if data and 'price' in data:
        price = data['price']
    else:
        price = None
    return price


def main():
    symbol = 'btc-bitcoin'  # Symbol for BTC
    exchange = 'Coinbase'  # Exchange name

    print(f'Fetching the price of {symbol} on {exchange}...')
    price = get_crypto_price(symbol, exchange)
    if price is not None:
        print(f'Price: {price}')
    else:
        print(f'Failed to fetch the price of {symbol} on {exchange}.')


if __name__ == '__main__':
    main()
