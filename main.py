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

    block = wallet.create_block(pool.transactions, 'prev_hash', 1)
    signature_valid = Wallet.signature_valid(block.payload(), block.signature, wallet.public_key_string())

    print(signature_valid)
