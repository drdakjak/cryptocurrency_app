#from django.db import models
import brokers.bitfinex.messenger as bf
import models as db 
import time
import datetime
import pytz

class Pubticker(object):
   def __init__(self, mid=None, bid=None, ask=None,last_price=None,low=None,high=None,volume=None,timestamp=None):
        self.mid = mid
        self.bid = bid
        self.ask = ask
        self.last_price = last_price
        self.low = low
        self.high = high
        self.volume = volume
        self.timestamp = timestamp


    
class Trader(object):
    pubticker = None
    broker = None
    order_id = None
    
    def __init__(self,broker):
        
        if(broker=='bitfinex'):
            self.broker = bf.Calls()

        self.trades = {}
        self.order_id = 0
        self.pubticker = Pubticker()
 
    def buy(self):
        self.trades[self.order_id] = "BUY"+datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.order_id += 1
        # bf->self.broker
        # Trader -> self
        # response, payload = bf.Calls.buy(0,0)
        # order = bf.Order("Open", response['order_id'], "btcusd", payload['amount'], payload['price'], payload['exchange'], payload['side'], payload['trade_type'], payload['is_hidden'])
        # Trader.trades[response['order_id']] = order.__dict__
        # TODO ulozeni obchodu do databaze
        pass
    

    def sell(self):
        self.trades[self.order_id] = "SELL"+datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.order_id += 1
        # response, payload = bf.Calls.sell(0,0)
        # order = bf.Order("Open", response['order_id'], "btcusd", payload['amount'], payload['price'], payload['exchange'], payload['side'], payload['trade_type'], payload['is_hidden'])
        # Trader.trades[response['order_id']] = order.__dict__
        # TODO ulozeni obchodu do databaze 
        pass
    
  
    def close(self,order_id):
        del self.trades[int(order_id)]
        # payload_object = {
        #     'request': '/order/cancel',
        #     'order_id': order_id
        # }
        # bf.call(payload_object)
        
        # payload_object = {
        #     'request': '/order/status',
        #     'order_id': order_id
        # }
        # r = bf.call(payload_object)
        # if(r['is_cancelled']):
        #     del Trader.trades[order_id]
        # # TODO zmena obchodu v databazi
        
    
    def get_pubticker(self, symbol):
        pubticker_json = self.broker.get_pubticker(symbol)
        pubticker_json['pair_id'] = symbol
        db.Pubticker(**pubticker_json).save()
        del pubticker_json['pair_id']
        return Pubticker(**pubticker_json)

    