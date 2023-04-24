#  MarketData
import requests
import time
import json
from datetime import datetime

from pymongo import MongoClient

def create_database_connection():

   CONNECTION_STRING = "mongodb://localhost:27017/"
   client = MongoClient(CONNECTION_STRING)
   return client.kucoin_test

def check_last_time (currency, time):
    d = "2009-11-12 12:00:00"
    for data in market_data.find({'currency': currency,'time': {"$gt": time}}):
        print(data)
        
def call_process(collection):
    """
    Call just once and make a loop to get the currencies desired
    """
    crypto_currencies = ['BTC-USDT', 'ETH-USDT']
    base_url='https://api.kucoin.com'
    
    for currency in crypto_currencies:
        currency_data = requests.get(base_url + '/api/v1/market/stats?symbol=' + currency).json()['data']
        
        dt = datetime.fromtimestamp(currency_data['time'] / 1000 )
        formatted_time = dt.strftime('%Y-%m-%d %H:%M:%S')
        
        final_data =  {
            'currency' : currency,
            'time' : formatted_time,
            'current_price': currency_data['last'],
        }
    
        try:
            collection.insert_one(final_data)
        except Exception as e:
            print("Error inserting data into database", e)
  
def call_process_every_5_seconds(collection):
    """
    Function that calls the process every 5 seconds.
    """
    while True:
        call_process(collection)
        time.sleep(2)

if __name__ == "__main__":
    # Get the database
    db = create_database_connection()    
    market_data = db.market_data
    
    call_process_every_5_seconds(market_data)
    

        
        
    
    