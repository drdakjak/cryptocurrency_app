class Manager(object):
    
    @staticmethod
    def init(trader):
        trader.test = 1
        
    @staticmethod
    def event(trader):
        print (trader.test)
        trader.test += 1
        
  
    @staticmethod
    def deinit(trader):
        print("deinit: ",trader.test)
        