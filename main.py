from pprint import pprint

from blockchain import Blockchain
from chain_utils import ChainUtils
from transaction_pool import TransactionPool
from wallet import Wallet

if __name__ == '__main__':
    sender = 'sender'
    receiver = 'receiver'
    amount = 1
    type = 'transfer'

    wallet = Wallet()
    fraud_wallet = Wallet()
    pool = TransactionPool()

    transaction = wallet.create_transaction(receiver, amount, type)

    if not pool.transaction_exists(transaction):
        pool.add_transaction(transaction)

    blockchain = Blockchain()

    prev_hash = ChainUtils.hash(blockchain.blocks[-1].payload()).hexdigest()
    block_count = len(blockchain.blocks)

    block = wallet.create_block(pool.transactions, prev_hash, block_count)

    if not blockchain.prev_block_hash_valid(block):
        print('Previous block hash is invalid')

    if not blockchain.block_count_valid(block):
        print('Block count is invalid')

    if blockchain.prev_block_hash_valid(block) and blockchain.block_count_valid(block):
        blockchain.add_block(block)

    pprint(blockchain.to_json())
