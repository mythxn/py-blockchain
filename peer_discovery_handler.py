import threading
import time


class PeerDiscoveryHandler():

    def __init__(self, node):
        self.socket_communication = node

    def start(self):
        threading.Thread(target=self.status).start()
        threading.Thread(target=self.discovery).start()

    def status(self):
        while True:
            print('status')
            time.sleep(10)

    def discovery(self):
        while True:
            print('discovery')
            time.sleep(10)