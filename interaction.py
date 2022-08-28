import requests

from chain_utils import ChainUtils
from wallet import Wallet

if __name__ == '__main__':
    bob = Wallet()
    alice = Wallet()
    exchange = Wallet()

    transaction = exchange.create_transaction(alice.pub_key_string(), 10, 'exchange')

    url = 'http://localhost:5001/transaction'
    payload = {'transaction': ChainUtils.encode(transaction)}
    resp = requests.post(url, json=payload)
    print(resp.text)