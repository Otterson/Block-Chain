#https://hackernoon.com/learn-blockchains-by-building-one-117428612f46

class Blockchain(object):
    def __init__(self):
        self.chain[]
        self.current_transactions = []

        #Create genesis block
        self.new_block(previous_hash=1, proof=100)



    def new_block(self, proof, previous_hash=None):
        #Creates a new block in the chain
        #<int> proof: the proof given by Proof of Work alg
        #<str> previous_hash: optional hash of previous block
        #<dict> returns new block
        block = {
            'index': len(self.chain)+1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }

        #Reset the current list of transactions
        self.current_transactions = []

        self.chain.append(block)
        return block



    def new_transaction(self, sender, recipient, amount):
        #Creates a new transaction to go into the next mined block
        #Returns the index of the int index of the block that will hold this transaction
        self.currect_transactions.append({
            'sender':sender,
            'recipient':recipient
            'amount':amount
        })

        return self.last_block['index']+1



    @staticmethod
    def hash(block):
        #Uses SHA-256 hash of block
        #<str> returns hash

        #block dictionary must be ordered for consistent hashes
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()


    def last_block(self):   
        return self.chain[-1]

    
