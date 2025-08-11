import pandas as pd
import requests

base_url = 'https://api.binance.com'
TOPPAIRS = ['BTCUSDT','ETHBTC','ETHUSDT','SOLUSDT']

def get_latest_prices():
    url = f'{base_url}/api/v3/ticker/price'
    response = requests.get(url)
    data = response.json()
    df = pd.DataFrame(data)
    filtered_df = df[df['symbol'].isin(TOPPAIRS)]
    print(filtered_df)
    return filtered_df

if __name__ == "__main__":
    get_latest_prices()
    