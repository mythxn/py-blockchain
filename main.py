from blockchain import Blockchain
from transaction_pool import TransactionPool
from wallet import Wallet

if __name__ == '__main__':

    blockchain = Blockchain()
    pool = TransactionPool()

    alice = Wallet()
    bob = Wallet()
    exchange = Wallet()

    exchange_transaction = exchange.create_transaction(alice.pub_key_string(), 10, 'exchange')
    if not pool.transaction_exists(exchange_transaction):
        pool.add_transaction(exchange_transaction)

    # alice wants to send 5 tokens to bob
    transaction = alice.create_transaction(bob.pub_key_string(), 5, 'transfer')

    if not pool.transaction_exists(transaction):
        pool.add_transaction(transaction)

    covered_transactions = blockchain.get_covered_trasaction_set(pool.transactions)

    print(covered_transactions)
