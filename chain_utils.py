import json

import jsonpickle
from Crypto.Hash import SHA256


class ChainUtils():

    @staticmethod
    def hash(data):
        dataString = json.dumps(data)
        dataBytes = dataString.encode('utf-8')
        return SHA256.new(dataBytes)

    @staticmethod
    def encode(obj):
        return jsonpickle.encode(obj)

    @staticmethod
    def decode(obj):
        return jsonpickle.decode(obj)