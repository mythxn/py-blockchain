from blockchain import Blockchain
from socket_communication import SocketCommunication
from transaction_pool import TransactionPool
from wallet import Wallet


class Node():
    def __init__(self, ip, port):
        self.p2p = None
        self.ip = ip
        self.port = port
        self.transaction_pool = TransactionPool()
        self.wallet = Wallet()
        self.blockchain = Blockchain()

    def start_p2p(self):
        self.p2p = SocketCommunication(self.ip, self.port)
        self.p2p.start_socket()