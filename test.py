from proof_of_stake import ProofOfStake

if __name__ == '__main__':
    pos = ProofOfStake()
    pos.update('alice', 10)
    pos.update('bob', 20)

    print(pos.get('alice'))
    print(pos.get('bob'))
    print(pos.get('carol'))