from account_model import AccountModel
from block import Block
from chain_utils import ChainUtils


class Blockchain():
    def __init__(self):
        self.blocks = [Block.genesis()]
        self.account_model = AccountModel()

    def add_block(self, block):
        self.blocks.append(block)

    def to_json(self):
        return {'blocks': [block.to_json() for block in self.blocks]}

    def block_count_valid(self, block):
        return block.block_count == len(self.blocks)

    def prev_block_hash_valid(self, block):
        latest_blockchain_hash = ChainUtils.hash(self.blocks[-1].payload()).hexdigest()
        return latest_blockchain_hash == block.prev_hash

    def transaction_covered(self, transaction):
        sender_bal = self.account_model.get_balance(transaction.sender_pub_key)
        return sender_bal >= transaction.amount

    def get_covered_trasaction_set(self, transactions):
        covered_transactions = []
        for transaction in transactions:
            if self.transaction_covered(transaction):
                covered_transactions.append(transaction)
            else:
                print('Transaction not covered')
        return covered_transactions
