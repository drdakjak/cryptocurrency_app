import requests
import hashlib
import json
import base64
import time
import hmac



class Authentication:
    # Your API key is:
    #     WU3fL2YNNChbf2EfUtGMQCPxyUHqaIn2MF0de4Yyki8

    # Your API key secret is:
    #     MhOjdNX3SL5QPWNDoEVIewsjKcPPBPEOa2mCrwbmkK9
    api_key = "WU3fL2YNNChbf2EfUtGMQCPxyUHqaIn2MF0de4Yyki8"
    api_secret = "MhOjdNX3SL5QPWNDoEVIewsjKcPPBPEOa2mCrwbmkK9"
    url = 'https://api.bitfinex.com/v1'

class Order:
    state = None
    order_id = None
    symbol = None
    amount = None
    price = None
    exchange = None
    side = None
    trade_type = None
    is_hidden = None
    
    def __init__(self, state, order_id, symbol, amount, price, exchange, side, order_type, is_hidden):
        self.state = state
        self.order_id = order_id
        self.symbol = symbol
        self.amount = amount
        self.price = price
        self.exchange = exchange
        self.side = side
        self.order_type = order_type
        self.is_hidden = is_hidden

class Calls(object):
    
    
    def buy(self,amount,price):
        amount = '0'
        price = '0'
        exchange = 'bitfinex'
        side = 'buy'
        trade_type = ''
        is_hidden = False
        payload_object = {
          'request':'/order/new',
          'nonce':str(time.time()),
          'symbol':'btcusd',
          'amount':amount,
          'price':price,
          'exchange':exchange,
          'side':side,
          'type':trade_type,
          'is_hidden': is_hidden,
        }
        payload = base64.b64encode(json.dumps(payload_object))

        m = hmac.new(Authentication.api_secret, payload, hashlib.sha384).hexdigest()

        headers = {
               'X-BFX-APIKEY' : Authentication.api_key,
               'X-BFX-PAYLOAD' : payload,
               'X-BFX-SIGNATURE' : m
               }
    
        return requests.post(Authentication.url+payload_object['request'], data={}, headers=headers).json(),payload_object
        
    def sell(self,amount,price):
        amount = amount
        price = price
        exchange = 'bitfinex'
        side = 'sell'
        trade_type = ''
        is_hidden = False
        payload_object = {
          'request':'/order/new',
          'nonce':str(time.time()),
          'symbol':'btcusd',
          'amount':amount,
          'price':price,
          'exchange':exchange,
          'side':side,
          'type':trade_type,
          'is_hidden': is_hidden,
        }
        payload = base64.b64encode(json.dumps(payload_object))

        m = hmac.new(Authentication.api_secret, payload, hashlib.sha384).hexdigest()

        headers = {
               'X-BFX-APIKEY' : Authentication.api_key,
               'X-BFX-PAYLOAD' : payload,
               'X-BFX-SIGNATURE' : m
               }
    
        return requests.post(Authentication.url+payload_object['request'], data={}, headers=headers).json(),payload_object
        
   
    def get_pubticker(self,symbol):
        
        r = requests.get('https://api.bitfinex.com/v1'+'/pubticker/'+ symbol)
        print('https://api.bitfinex.com/v1/pubticker/'+ symbol)
        return r.json()
        
  
    # def call(self,payload_object):
       
    #     payload = base64.b64encode(json.dumps(payload_object))
    
    #     m = hmac.new(Authentication.api_secret, payload, hashlib.sha384).hexdigest()
    
    #     headers = {
    #               'X-BFX-APIKEY' : Authentication.api_key,
    #               'X-BFX-PAYLOAD' : payload,
    #               'X-BFX-SIGNATURE' : m
    #               }
        
    #     return requests.post(Authentication.url+payload_object['request'], data={}, headers=headers).json()
        