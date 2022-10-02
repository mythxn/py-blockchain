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
        transaction_in_block = self.blockchain.transaction_exists(transaction)
        if not transaction_exists and not transaction_in_block and signature_valid:
            self.transaction_pool.add_transaction(transaction)
            message = Message(self.p2p.socket_connector, 'transaction', transaction)
            encoded_msg = ChainUtils.encode(message)
            self.p2p.broadcast(encoded_msg)
            if self.transaction_pool.forger_required():
                self.forge()

    def handle_block(self, block):
        forger = block.forger
        block_hash = block.payload()
        signature = block.signature

        block_count_valid = self.blockchain.block_count_valid(block)
        prev_block_hash_valid = self.blockchain.prev_block_hash_valid(block)
        forger_valid = self.blockchain.forger_valid(block)
        transactions_valid = self.blockchain.transaction_valid(block)
        signature_valid = Wallet.signature_valid(block_hash, signature, forger)

        if prev_block_hash_valid and forger_valid and transactions_valid and signature_valid and block_count_valid:
            self.blockchain.add_block(block)
            self.transaction_pool.remove_from_pool(block.transactions)
            message = Message(self.p2p.socket_connector, 'block', block)
            encoded_msg = ChainUtils.encode(message)
            self.p2p.broadcast(encoded_msg)

    def forge(self):
        forger = self.blockchain.next_forger()
        if forger == self.wallet.pub_key_string():
            block = self.blockchain.create_block(self.transaction_pool, self.wallet)
            self.transaction_pool.remove_from_pool(block.transactions)
            message = Message(self.p2p.socket_connector, 'block', block)
            encoded_msg = ChainUtils.encode(message)
            self.p2p.broadcast(encoded_msg)
        else:
            print('im not the next forger')
