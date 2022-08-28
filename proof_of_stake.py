class ProofOfStake:

    def __init__(self):
        self.stakers = {}

    def update(self, pub_key_string, stake):
        if pub_key_string in self.stakers:
            self.stakers[pub_key_string] += stake
        else:
            self.stakers[pub_key_string] = stake

    def get(self, pub_key_string):
        return self.stakers.get(pub_key_string, None)