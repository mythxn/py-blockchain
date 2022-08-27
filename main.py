from transaction import Transaction
from wallet import Wallet

if __name__ == '__main__':

    sender = 'sender'
    receiver = 'receiver'
    amount = 1
    type = 'transfer'

    transaction = Transaction(sender, receiver, amount, type)

    wallet = Wallet()
    signature = wallet.sign(transaction.to_json())

    transaction.sign(signature)
    print(transaction.to_json())