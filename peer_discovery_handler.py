import threading
import time

from chain_utils import ChainUtils
from message import Message


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

    def handshake(self, connected_node):
        self.socket_communication.send(connected_node, self.handshake_message())

    def handshake_message(self):
        own_connector = self.socket_communication.socket_connector
        own_peers = self.socket_communication.peers
        data = own_peers
        message_type = 'discovery'
        message = Message(own_connector, message_type, data)
        return ChainUtils.encode(message)
