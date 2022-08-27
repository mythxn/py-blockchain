from pprint import pprint

from block import Block
from blockchain import Blockchain
from chain_utils import ChainUtils
from transaction_pool import TransactionPool
from wallet import Wallet

if __name__ == '__main__':

    blockchain = Blockchain()
    pool = TransactionPool()

    alice = Wallet()
    bob = Wallet()
    exchange = Wallet()
    forger = Wallet()

    exchange_transaction = exchange.create_transaction(alice.pub_key_string(), 10, 'exchange')
    if not pool.transaction_exists(exchange_transaction):
        pool.add_transaction(exchange_transaction)

    covered_transactions = blockchain.get_covered_trasaction_set(pool.transactions)
    prev_hash = ChainUtils.hash(blockchain.blocks[-1].payload()).hexdigest()
    block_count = len(blockchain.blocks)
    block_one = forger.create_block(covered_transactions, prev_hash, block_count)
    blockchain.add_block(block_one)

    # alice wants to send 5 tokens to bob
    transaction = alice.create_transaction(bob.pub_key_string(), 5, 'transfer')

    if not pool.transaction_exists(transaction):
        pool.add_transaction(transaction)

    covered_transactions = blockchain.get_covered_trasaction_set(pool.transactions)
    prev_hash = ChainUtils.hash(blockchain.blocks[-1].payload()).hexdigest()
    block_count = len(blockchain.blocks)
    block_two = forger.create_block(covered_transactions, prev_hash, block_count)
    blockchain.add_block(block_two)

    pprint(blockchain.to_json())
