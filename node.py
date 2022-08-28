from blockchain import Blockchain
from node_api import NodeAPI
from socket_communication import SocketCommunication
from transaction_pool import TransactionPool
from wallet import Wallet


class Node():

    def __init__(self, ip, port):
        self.api = None
        self.p2p = None
        self.ip = ip
        self.port = port
        self.transaction_pool = TransactionPool()
        self.wallet = Wallet()
        self.blockchain = Blockchain()

    def start_p2p(self):
        self.p2p = SocketCommunication(self.ip, self.port)
        self.p2p.start_socket()

    def start_api(self, api_port):
        self.api = NodeAPI()
        self.api.inject_node(self)
        self.api.start(api_port)
