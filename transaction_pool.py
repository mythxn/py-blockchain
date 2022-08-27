class TransactionPool():
    def __init__(self):
        self.transactions = []

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def transaction_exists(self, transaction):
        return transaction in self.transactions

    def remove_from_pool(self, transactions):
        new_pool_transactions = []

        for cur_pool_transaction in self.transactions:
            if cur_pool_transaction not in transactions:
                new_pool_transactions.append(cur_pool_transaction)

        self.transactions = new_pool_transactions
