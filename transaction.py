import copy
import time
import uuid


class Transaction():

    def __init__(self, sender_pub_key, receiver_pub_key, amount, type):
        self.sender_pub_key = sender_pub_key
        self.recipient = receiver_pub_key
        self.amount = amount
        self.type = type
        self.id = uuid.uuid1().hex
        self.timestamp = time.time()
        self.signature = ''

    def to_json(self):
        return self.__dict__

    def sign(self, signature):
        self.signature = signature

    def payload(self):
        json_repr = copy.deepcopy(self.to_json())
        json_repr['signature'] = ''
        return json_repr

    def __eq__(self, other):
        return self.id == other.id