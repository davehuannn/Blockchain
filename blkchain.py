import hashlib
import json
from time import time

class Block:
    def __init__(self, index, timestamp, data, previous_hash=''):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.compute_hash()
    
    def compute_hash(self):
        block_string = json.dumps(self.__dict__, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_block(previous_hash='1')  # Create the genesis block

    def create_block(self, data, previous_hash=''):
        index = len(self.chain) + 1
        timestamp = time()
        block = Block(index, timestamp, data, previous_hash)
        self.chain.append(block)
        return block

    def get_last_block(self):
        return self.chain[-1]

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            previous_block = self.chain[i - 1]
            current_block = self.chain[i]

            if current_block.previous_hash != previous_block.hash:
                return False

            if current_block.hash != current_block.compute_hash():
                return False

        return True

# Create blockchain instance
blockchain = Blockchain()

# Add blocks to the blockchain
blockchain.create_block(data="First block data")
blockchain.create_block(data="Second block data")

# Print blockchain information
for block in blockchain.chain:
    print(f"Index: {block.index}")
    print(f"Timestamp: {block.timestamp}")
    print(f"Data: {block.data}")
    print(f"Previous Hash: {block.previous_hash}")
    print(f"Hash: {block.hash}")
    print("-" * 30)

# Check if the blockchain is valid
print(f"Is blockchain valid? {blockchain.is_chain_valid()}")
