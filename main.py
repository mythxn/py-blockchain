from transaction import Transaction
from wallet import Wallet

if __name__ == '__main__':
    sender = 'sender'
    receiver = 'receiver'
    amount = 1
    type = 'transfer'

    transaction = Transaction(sender, receiver, amount, type)

    wallet = Wallet()
    fraud_wallet = Wallet()

    transaction = wallet.create_transaction(receiver, amount, type)
    signature_valid = Wallet.signature_valid(transaction.payload(), transaction.signature, fraud_wallet.public_key_string())

    print(signature_valid)