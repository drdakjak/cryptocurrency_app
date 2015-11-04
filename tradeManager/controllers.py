import threading
import time

from trader.controllers import Pubticker
from trader.controllers import Trader
from expertAdvisor.expertAdvisor import Manager


class Tasks:
    task_id = 0
    tasks = {}

class PeriodicTask(object):
    task_id = None
    symbol = None
    period = None
    trader = None
    
    period_thread = None
    worker_thread = None
    stop = False
    
    
    sem_event_ready = threading.Semaphore(0)
    sem_period_ready = threading.Semaphore(0)
    

    def __init__ (self, symbol, period, broker):
        self.task_id = Tasks.task_id
        self.threads = []
        self.symbol = symbol
        self.period = period
        self.trader = Trader(broker)

        Tasks.task_id += 1 
        
        PeriodicTask.task(self,symbol,period)

    def task(self,symbol,period):
        try:
            self.period_thread = threading.Thread(target=self.period_worker,args=(symbol,period))
            self.worker_thread = threading.Thread(target=self.event_worker,args=(symbol,period))
            
            self.period_thread.start()
            self.worker_thread.start()
  
        except:
            return False
        return True
        
    
    def period_worker(self,symbol,period):
        while not self.stop:
            self.sem_period_ready.acquire()
            self.sem_event_ready.release()
            
            time.sleep(period)
            
        
        print("Thread PERIOD-WORKER END")
            
            
    def event_worker(self,symbol,period):
        Manager.init(self.trader)
        while not self.stop:
            print ("--------------------------EVENT "+str(period)+ " --------------------------")
            self.sem_period_ready.release()
            self.sem_event_ready.acquire()
            
            self.trader.pubticker = self.trader.get_pubticker(symbol)
            Manager.event(self.trader)
        
        self.sem_period_ready.release()
        print("Thred EVENT-WORKER END")
        Manager.deinit(self.trader)
        
    def stop_threads(self):
        self.stop = True