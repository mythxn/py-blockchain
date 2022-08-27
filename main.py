from transaction import Transaction
from transaction_pool import TransactionPool
from wallet import Wallet

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

    if not pool.transaction_exists(transaction):
        pool.add_transaction(transaction)

    print(pool.transactions)