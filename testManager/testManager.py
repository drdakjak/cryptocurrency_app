import django.models
import testExpertAdvisor as tEA
def testManager(from_, to_):
      
      trader_ = Trader_()
      tEA.init(trader_)
      
      # loop
      tEA.event(trader_)
      
      
      tEA.deinit(trader_)
      
      
class Pubticker_:
   def __init__(self, mid=None, bid=None, ask=None,last_price=None,low=None,high=None,volume=None,timestamp=None):
        self.mid = mid
        self.bid = bid
        self.ask = ask
        self.last_price = last_price
        self.low = low
        self.high = high
        self.volume = volume
        self.timestamp = timestamp   

'''
Basic interface class for testExpertAdvisor
'''
class Trader_:
      pubticker_ = None
      broker_ = None
      order_id_ = None
      orders_ = {}
            
      def buy_(self):
            self.orders_[self.order_id_] = Order_()
            self.order_id_ += 1
            pass
      def sell_(self):
            self.orders_[self.order_id_] = Order_()
            self.order_id_ += 1      
            pass
      def close_(self):
            pass

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
      
      def __init__(self,open_price_,open_time_):
            self.open_price_ = open_price_
            self.open_time_ = open_time_


    
