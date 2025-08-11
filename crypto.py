import pandas
import requests

base_url = 'https://api.binance.com'

def get_latest_prices():
    url = f'{base_url}/api/v3/ticker/price'
    