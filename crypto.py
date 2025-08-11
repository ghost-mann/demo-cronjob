import pandas as pd
import requests

base_url = 'https://api.binance.com'

def get_latest_prices():
    url = f'{base_url}/api/v3/ticker/price'
    response = requests.get(url)
    data = response.json()
    df = pd.DataFrame(data)
    print(df)
    return df

if __name__ == "__main__":
    get_latest_prices()
    