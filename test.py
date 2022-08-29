import random
import string

from proof_of_stake import ProofOfStake


def get_random_string(length_of_str):
    return ''.join(random.choice(string.ascii_letters) for _ in range(length_of_str))


if __name__ == '__main__':
    pos = ProofOfStake()
    pos.update('alice', 100)
    pos.update('bob', 100)

    bob_wins = alice_wins = 0

    for i in range(100):
        forger = pos.forger(get_random_string(i))
        if forger == 'alice':
            alice_wins += 1
        elif forger == 'bob':
            bob_wins += 1

    print(f'Alice wins {alice_wins} times')
    print(f'Bob wins {bob_wins} times')
