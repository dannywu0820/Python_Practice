#https://openhome.cc/Gossip/DesignPattern/ThreadPerMessage.htm

import time
import thread

class RequestHandler:
    def __init__(self):
        pass
    
    def process_request(self, data):
        print("-----[Start Processing Data %d]-----" % data)
        time.sleep(3*data)
        print("-----[Finish Processing Data %d]-----" % data)

class Server:
    def __init__(self):
        self.handler = RequestHandler()
        
    def accept_request(self, data):
        thread.start_new_thread(lambda: self.handler.process_request(data), ())

if __name__ == '__main__':
    test_server = Server()
    for i in range(1, 6):
        print("-----[Send Request]----")
        test_server.accept_request(i)
        print("-----[Request Has Been Sent]")

    time.sleep(20)