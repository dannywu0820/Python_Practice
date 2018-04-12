#https://openhome.cc/Gossip/DesignPattern/WorkerThread.htm

import threading
import time
import random

class Worker(threading.Thread):
    def __init__(self, index, queue):
        threading.Thread.__init__(self)
        self.index = index
        self.queue = queue
    
    def run(self):
        while True:
            self.queue.popRequest(self.index)
    
class RequestQueue:
    def __init__(self, num_of_workers):
        self.requests = []
        self.condition = threading.Condition()
        for i in range(num_of_workers):
            Worker(i, self).start() #self is RequestQueue itself
    
    def pushRequest(self, request):
        self.condition.acquire()
        print("-----[Client acquire for lock]-----")
        
        self.requests.append(request) #produce an item
        print("-----[Client push request]-----")
        
        self.condition.notify()
        print("-----[Client notify Worker]-----")
        
        self.condition.release()
        print("-----[Client release lock]-----")
    
    def popRequest(self, worker_index):
        self.condition.acquire() #acquire the lock
        print("-----[Worker%d acquire for lock]-----" % (worker_index))
        
        while not self.requests: #queue is not avaliable
            self.condition.wait() #wait until notified or a timeout occurs
        print("-----[Worker%d notified by client]-----" % (worker_index))
        request = self.requests.pop(0) #consume an item
        print("-----[Worker%d pop request]-----" % (worker_index))
        
        self.condition.release()
        print("-----[Worker%d Release Lock]-----" % (worker_index))
        
        print("-----[Worker%d start processing request%s]-----" % (worker_index, request))
        time.sleep(5)
        print("-----[Worker%d finish processing request%s]-----" % (worker_index, request))
        
        return request
    
class Client(threading.Thread):
    def __init__(self, index, queue):
        threading.Thread.__init__(self)
        self.index = index
        self.queue = queue
    
    def run(self):
        content = 1
        
        while True:
            request = (str(self.index) + "-" + str(content))
            content = content+1
            self.queue.pushRequest(request)
            
            sleep_second = 1 #int(random.random() * 3)
            time.sleep(sleep_second)
            print("Client sleep %d second" % sleep_second)

def main():
    number_of_workers = 5
    number_of_clients = 2
    test_queue = RequestQueue(number_of_workers)
    for i in range(number_of_clients): #simulate clients
        Client(i, test_queue).start()

    while True:
        try:
            time.sleep(10)
            print("zzz")
        except KeyboardInterrupt:
            exit()
            
if __name__ == '__main__':
    main()