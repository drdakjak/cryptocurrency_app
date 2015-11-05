from cryptocurrency_app.models import Pubticker
import testExpertAdvisor as tEA
class TestManager:
      
      wallet = {'USD':400,'BTC':1}
      
      def run_tester(self,from_, to_):
            
            pubticker_history = Pubticker.objects.all().filter(import_date_lte = to_).filter(import_date_gte=from_)
            trader_ = Trader_(self.wallet)
            tEA.init(trader_)
            
            for ticker in pubticker_history:
                  trader_.pubticker_ = ticker
                  tEA.event(trader_)
            
            
            tEA.deinit(trader_)
            
            return self.wallet
      

'''
Basic interface class for testExpertAdvisor
'''
class Trader_:
      pubticker_ = None
      order_id_ = None
      orders_ = {}
      wallet = None
      
      def __init__(self,wallet):
            self.wallet = wallet
            
      def buy_(self,amount):
            price = self.pubticker_.bid
            time = self.pubticker_.timestamp
            self.orders_[self.order_id_] = Order_(price,time,"buy")
            self.wallet['USD'] -= amount*price
            self.wallet['BTC'] += amount
            self.order_id_ += 1
            
      def sell_(self,amount):
            price = self.pubticker_.ask
            time = self.pubticker_.timestamp
            self.orders_[self.order_id_] = Order_(price,time,"sell")
            self.wallet['USD'] += amount*price
            self.wallet['BTC'] -= amount
            self.order_id_ += 1      
            
      def close_(self,order_id_):
            pass
            # o = self.orders_[order_id_]
            # o.active_ = False
            # if(o.order_type_ == "buy"):
            #       self.orders_[order_id_].close_price_ = pubticker_.ask
            # if(o.order_type_ == "sell")
            #       self.orders_[order_id_].close_price_ = pubticker_.bid
            # self.orders_[order_id_].diff_price_
            # self.orders_[order_id_].close_time_
            # self.orders_[order_id_].diff_time_
            
'''
Order class
'''
class Order_:
      open_price_ = None
      close_price_ = None
      diff_price_ = None
      
      open_time_ = None
      close_time_ = None
      diff_time_ = None
      
      ##
      # buy / sell
      # {String}
      order_type_ = None
      
      active_ = True
      
      def __init__(self,open_price_,open_time_,order_type_):
            self.open_price_ = open_price_
            self.open_time_ = open_time_
            self.order_type_ = order_type_


    
# class Pubticker_:
#    def __init__(self, mid=None, bid=None, ask=None,last_price=None,low=None,high=None,volume=None,timestamp=None):
#         self.mid = mid
#         self.bid = bid
#         self.ask = ask
#         self.last_price = last_price
#         self.low = low
#         self.high = high
#         self.volume = volume
#         self.timestamp = timestamp   