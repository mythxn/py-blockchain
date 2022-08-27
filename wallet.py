from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5

from chain_utils import ChainUtils


class Wallet():

    def __init__(self):
        self.key_pair = RSA.generate(2048)

    def sign(self, data):
        dataHash = ChainUtils.hash(data)
        signature_scheme_obj = PKCS1_v1_5.new(self.key_pair)
        signature = signature_scheme_obj.sign(dataHash)
        return signature.hex()