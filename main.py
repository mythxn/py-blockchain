from transaction import Transaction

if __name__ == '__main__':

    sender = 'sender'
    receiver = 'receiver'
    amount = 1
    type = 'transfer'

    transaction = Transaction(sender, receiver, amount, type)
    print(transaction.to_json())