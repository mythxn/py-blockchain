from account_model import AccountModel
from wallet import Wallet

if __name__ == '__main__':

    wallet = Wallet()
    account_model = AccountModel()

    account_model.update_balance(wallet.pub_key_string(), 5)
    account_model.update_balance(wallet.pub_key_string(), -15)
    print(account_model.balances)