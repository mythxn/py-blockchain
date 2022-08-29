from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5

from block import Block
from chain_utils import ChainUtils
from transaction import Transaction


class Wallet:

    def __init__(self):
        self.key_pair = RSA.generate(2048)

    def from_key(self, file):
        with open(file, 'r') as key_file:
            key = RSA.importKey(key_file.read())
        self.key_pair = key

    def sign(self, data):
        dataHash = ChainUtils.hash(data)
        signature_scheme_obj = PKCS1_v1_5.new(self.key_pair)
        signature = signature_scheme_obj.sign(dataHash)
        return signature.hex()

    @staticmethod
    def signature_valid(data, signature, pub_key_string):
        signature = bytes.fromhex(signature)
        dataHash = ChainUtils.hash(data)
        pub_key = RSA.import_key(pub_key_string)
        signature_scheme_obj = PKCS1_v1_5.new(pub_key)
        return signature_scheme_obj.verify(dataHash, signature)

    def pub_key_string(self):
        return self.key_pair.publickey().exportKey('PEM').decode('utf-8')

    def create_transaction(self, receiver_pub_key, amount, type):
        transaction = Transaction(self.pub_key_string(), receiver_pub_key, amount, type)
        signature = self.sign(transaction.payload())
        transaction.sign(signature)
        return transaction

    def create_block(self, transactions, prev_hash, block_count):
        block = Block(transactions, prev_hash, self.pub_key_string(), block_count)
        block.sign(self.sign(block.payload()))
        return block
