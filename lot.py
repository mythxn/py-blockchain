from chain_utils import ChainUtils


class Lot:

    def __init__(self, pub_key, iteration, prev_block_hash):
        self.pub_key = pub_key
        self.iteration = iteration
        self.prev_block_hash = prev_block_hash

    def lot_hash(self):
        hash_data = self.pub_key + self.prev_block_hash
        for _ in range(self.iteration):
            hash_data = ChainUtils.hash(hash_data).hexdigest()
        return hash_data
