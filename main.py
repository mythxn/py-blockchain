from transaction import Transaction
from transaction_pool import TransactionPool
from wallet import Wallet
from block import Block

if __name__ == '__main__':
    sender = 'sender'
    receiver = 'receiver'
    amount = 1
    type = 'transfer'

    transaction = Transaction(sender, receiver, amount, type)

    wallet = Wallet()
    fraud_wallet = Wallet()
    pool = TransactionPool()

    transaction = wallet.create_transaction(receiver, amount, type)

    if not pool.transaction_exists(transaction):
        pool.add_transaction(transaction)

    block = Block(pool.transactions, 'prev_hash', 'forger', 0)

    print(block.to_json())