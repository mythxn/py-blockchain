class AccountModel():
    def __init__(self):
        self.accounts = []
        self.balances = {}

    def add_account(self, pub_key_string):
        if pub_key_string not in self.accounts:
            self.accounts.append(pub_key_string)
            self.balances[pub_key_string] = 0

    def get_balance(self, pub_key_string):
        if pub_key_string not in self.balances:
            self.add_account(pub_key_string)
        return self.balances[pub_key_string]

    def update_balance(self, pub_key_string, amount):
        if pub_key_string not in self.accounts:
            self.add_account(pub_key_string)
        self.balances[pub_key_string] += amount
