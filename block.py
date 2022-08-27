import copy
import time


class Block():
    def __init__(self, transactions, prev_hash, forger, block_count):
        self.transactions = transactions
        self.prev_hash = prev_hash
        self.forger = forger
        self.block_count = block_count
        self.timestamp = time.time()
        self.signature = ''

    def to_json(self):
        data = {
            'prev_hash': self.prev_hash,
            'forger': self.forger,
            'block_count': self.block_count,
            'timestamp': self.timestamp,
            'signature': self.signature
        }
        json_transactions = [transaction.to_json() for transaction in self.transactions]
        data['transactions'] = json_transactions
        return data

    def payload(self):
        json_repr = copy.deepcopy(self.to_json())
        json_repr['signature'] = ''
        return json_repr

    def sign(self, signature):
        self.signature = signature
