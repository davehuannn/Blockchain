# Simple Blockchain in Python

Welcome to the Simple Blockchain project! This project demonstrates the fundamental concepts of blockchain technology using Python. It provides a basic but complete example of how a blockchain operates and how you can implement one from scratch.

## 🧩 What is a Blockchain?

A blockchain is a decentralized, distributed ledger that records transactions across many computers. It ensures that the data cannot be altered retroactively without altering all subsequent blocks and the consensus of the network. This technology underpins cryptocurrencies like Bitcoin, but its applications extend far beyond.

**Key Features of Blockchain:**
- **Decentralization**: Data is not controlled by a single entity.
- **Immutability**: Once data is added, it cannot be changed.
- **Security**: Uses cryptographic hashing to secure data.

## 🚀 How It Works

In our implementation, a blockchain is a chain of blocks where each block contains:
- **Index**: Position of the block in the chain.
- **Timestamp**: The time when the block was created.
- **Data**: The actual content or transactions stored in the block.
- **Previous Hash**: A reference to the hash of the previous block.
- **Hash**: A unique identifier generated from the block's content.

### Block Structure

Each block in our blockchain contains:
1. An index number to indicate its position.
2. A timestamp to record when it was created.
3. The data it holds.
4. The hash of the previous block to ensure continuity.
5. Its own hash, computed from its contents.

### Blockchain Structure

The blockchain:
1. Starts with a genesis block (the first block).
2. Adds new blocks with data and a reference to the previous block’s hash.
3. Validates the chain to ensure that it has not been tampered with.

## 💻 Implementation

Here’s a step-by-step guide to understand and run the code:

### 1. Define the Block

The `Block` class creates a new block with the given data and calculates its hash.

```python
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
```

### 2. Define the Blockchain

The `Blockchain` class manages the chain, creates blocks, and ensures its validity.

```python
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
```

### 3. Run and Test

The main script demonstrates how to create a blockchain, add blocks, and check its validity.

```python
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
```

## 🛠️ Installation and Usage

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/simple-blockchain.git
   ```

2. **Navigate to the project directory:**
   ```bash
   cd simple-blockchain
   ```

3. **Run the script:**
   ```bash
   python blockchain.py
   ```

## 🔍 Explore Further

This project is a simplified model of a blockchain. For more advanced features, consider exploring:
- **Proof of Work**: Implement a mining mechanism to secure blocks.
- **Consensus Algorithms**: Learn about different ways to achieve agreement across a network.
- **Smart Contracts**: Explore how smart contracts can be integrated into a blockchain.

## 🤝 Contributing

Feel free to contribute to this project by opening issues or submitting pull requests. Your feedback and improvements are welcome!
