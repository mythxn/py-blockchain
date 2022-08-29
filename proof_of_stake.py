from chain_utils import ChainUtils
from lot import Lot


class ProofOfStake():

    def __init__(self):
        self.stakers = {}
        self.set_genesis_node_stake()

    def set_genesis_node_stake(self):
        genesis_pub_key = open('keys/genesisPublicKey.pem', 'r').read()
        self.stakers[genesis_pub_key] = 1

    def update(self, pub_key_string, stake):
        if pub_key_string in self.stakers.keys():
            self.stakers[pub_key_string] += stake
        else:
            self.stakers[pub_key_string] = stake

    def get(self, pub_key_string):
        return self.stakers.get(pub_key_string, None)

    def validator_lots(self, seed):
        lots = []
        for validator in self.stakers.keys():
            lots.extend(Lot(validator, stake + 1, seed) for stake in range(self.get(validator)))
        return lots

    def winner_lot(self, lots, seed):
        winner_lot = None
        least_offset = None
        reference_hash_int_value = int(ChainUtils.hash(seed).hexdigest(), 16)
        for lot in lots:
            lot_int_value = int(lot.lot_hash(), 16)
            offset = abs(lot_int_value - reference_hash_int_value)
            if least_offset is None or offset < least_offset:
                least_offset = offset
                winner_lot = lot
        return winner_lot

    def forger(self, last_blockHash):
        lots = self.validator_lots(last_blockHash)
        winner_lot = self.winner_lot(lots, last_blockHash)
        return winner_lot.pub_key
