#  MarketData
from kucoin.client import Market
import requests
base_url='https://api.kucoin.com'
client = Market(url=base_url)

# get symbol kline
klines = client.get_kline('BTC-USDT','1min')

# get symbol ticker
server_time = client.get_server_timestamp()

api_key = '643acfa9e7c6660001b1e577'
api_secret = '3c864e59-7633-48a2-a045-708495b84f84'
api_passphrase = '@Werfen2023!'

from kucoin.client import User
client = User(api_key, api_secret, api_passphrase)

address = client