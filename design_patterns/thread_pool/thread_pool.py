#https://openhome.cc/Gossip/DesignPattern/ThreadPool.htm

import threading
import time
import random

class WorkerThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.condition = threading.Condition()
        self.status = True
        self.request = None
    
    def setStatus(self, new_status):
        self.status = new_status
    
    def isRunning(self):
        return (self.status == True)
    
    def setRequest(self, new_request):
        self.condition.acquire()
        if self.isIdle():
            self.request = new_request
        self.condition.notify()
        self.condition.release()
    
    def isIdle(self):
        return (self.request == None)
    
    def run(self):
        while self.isRunning():
            self.condition.acquire()
            self.condition.wait()
            #pop request from request queue
            self.condition.release()
            
            #handle request
            self.request()
            self.request = None
        print('terminated')
            
    def terminate(self):
        self.setStatus(False)
        self.setRequest(lambda: None)
    
class WorkerThreadPool:
    def __init__(self):
        self.worker_threads = []
        
    def create_new_worker(self):
        new_worker = WorkerThread()
        new_worker.start()
        self.worker_threads.append(new_worker)
        time.sleep(1)
        
        return new_worker
    
    def clean_idle_workers(self):
        for worker in self.worker_threads:
            if worker.isIdle():
                self.worker_threads.remove(worker)
                worker.terminate()
    
    def handle_request(self, request):
        no_idle_worker = True
        for worker in self.worker_threads:
            if worker.isIdle():
                print('Found an idle worker')
                worker.setRequest(request)
                no_idle_work = False
                break
                
        if no_idle_worker:
            print('Create a new worker')
            new_worker = self.create_new_worker()
            new_worker.setRequest(request)

class Server:
    def __init__(self):
        self.thread_pool = None
        self.request_queue = None
    
class Client(threading.Thread):
    def __init__(self):
        pass
    
    def run(self):
        pass
    
def doRequest():
    print('start')
    time.sleep(5)
    print('finish')
    
def main():
    '''test_thread = WorkerThread()
    test_thread.start()
    time.sleep(5)
    test_thread.setRequest(doRequest)
    time.sleep(10)
    test_thread.terminate()'''
    test_pool = WorkerThreadPool()
    for i in range(15):
        test_pool.handle_request(doRequest)
    
    while True:
        try:
            time.sleep(10)
            print("zzz")
        except KeyboardInterrupt:
            test_pool.clean_idle_workers()
            exit()
            
if __name__ == '__main__':
    main()