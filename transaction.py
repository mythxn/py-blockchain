import time

import uuid


class Transaction():

    def __init__(self, senderPubKey, receiverPubKey, amount, type):
        self.sender = senderPubKey
        self.recipient = receiverPubKey
        self.amount = amount
        self.type = type
        self.id = uuid.uuid1().hex
        self.timestamp = time.time()
        self.signature = ''

    def to_json(self):
        return self.__dict__
