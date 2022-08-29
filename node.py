from blockchain import Blockchain
from chain_utils import ChainUtils
from message import Message
from node_api import NodeAPI
from socket_communication import SocketCommunication
from transaction_pool import TransactionPool
from wallet import Wallet


class Node:

    def __init__(self, ip, port, key=None):
        self.api = None
        self.p2p = None
        self.ip = ip
        self.port = port
        self.transaction_pool = TransactionPool()
        self.wallet = Wallet()
        self.blockchain = Blockchain()

        if key is not None:
            self.wallet.from_key(key)

    def start_p2p(self):
        self.p2p = SocketCommunication(self.ip, self.port)
        self.p2p.start_socket(self)

    def start_api(self, api_port):
        self.api = NodeAPI()
        self.api.inject_node(self)
        self.api.start(api_port)

    def handle_transaction(self, transaction):
        data = transaction.payload()
        signature = transaction.signature
        signer_pub_key = transaction.sender_pub_key
        signature_valid = Wallet.signature_valid(data, signature, signer_pub_key)
        transaction_exists = self.transaction_pool.transaction_exists(transaction)
        if not transaction_exists and signature_valid:
            self.transaction_pool.add_transaction(transaction)
            message = Message(self.p2p.socket_connector, 'transaction', transaction)
            encoded_msg = ChainUtils.encode(message)
            self.p2p.broadcast(encoded_msg)
            if self.transaction_pool.forger_required():
                self.forge()

    def forge(self):
        forger = self.blockchain.next_forger()
        if forger == self.wallet.pub_key_string():
            print('im the next forger')
        else:
            print('im not the next forger')
