import requests

from chain_utils import ChainUtils
from wallet import Wallet


def post_transaction(sender, recipient, amount, type):
    transaction = sender.create_transaction(recipient.pub_key_string(), amount, type)
    url = 'http://localhost:5000/transaction'
    package = {'transaction': ChainUtils.encode(transaction)}
    requests.post(url, json=package)

if __name__ == '__main__':
    bob = Wallet()
    alice = Wallet()
    alice.from_key('keys/stakerPrivateKey.pem')
    exchange = Wallet()

    # forger: genesis
    post_transaction(exchange, alice, 100, 'exchange')
    post_transaction(exchange, bob, 100, 'exchange')
    post_transaction(exchange, alice, 25, 'stake')

    # forger: probably alice
    post_transaction(alice, bob, 1, 'transfer')
