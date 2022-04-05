from hashlib import sha256
from datetime import datetime 

class Block:
    def __init__(self, block_number, transactions, previous_hash, nonce = 0):
        '''
        Inputs: Block_number as an int, transactions as any hashable data type,
        previous_hash as a hexadecimal number, and the nonce as an int. 
        Output: Does not return anything. 

        The constructor initializes a block object using a block number, the transactions to be
        included in the block, the hash of the previous block, and a default nonce of 0. 
        '''
        self.block_number = block_number
        self.transactions = transactions 
        self.previous_hash = previous_hash
        self.nonce = nonce
        self.hashid = sha256() # creates a sha256 object which we can feed data into 
        self.timestamp = datetime.now() # sets the timestamp on the block to be the time of creation

    def mine(self, difficulty):
        '''
        Input: Takes in the difficulty of mining a block as an int. 
        Output: Returns the hashid of the block as a hexadecimal number.

        This method takes in the difficulty of mining a block as an integer
        and then uses this difficulty to calculate a valid hash (mining).
        Once a valid hash has been calculated, it is set as the hashid 
        of the block and then returned. 
        '''
        self.hashid.update( # we pass in several of the attributes of the block into the sha256 object 
             str(self.nonce).encode('utf-8')+ # convert each attribute to a string and encode it to utf-8
             str(self.transactions).encode('utf-8')+
             str(self.previous_hash).encode('utf-8')+
             str(self.timestamp).encode('utf-8')+
             str(self.block_number).encode('utf-8')
             )
        while int(self.hashid.hexdigest(), 16) > 2**(256 - difficulty): # while resulting hash does not meet requirements it is recalculated
            self.nonce += 1 # nonce updated to obtain new hash value from sha256 object 
            self.hashid = sha256()
            self.hashid.update(
             str(self.nonce).encode('utf-8')+
             str(self.transactions).encode('utf-8')+
             str(self.previous_hash).encode('utf-8')+
             str(self.timestamp).encode('utf-8')+
             str(self.block_number).encode('utf-8')
             )
        self.hashid = self.hashid.hexdigest() # set hashid as the valid hash in hexadecimal format 
        return self.hashid

    def __str__(self):
        '''
        Input: Nothing.
        Output: Prints a string representation of the block and its contents.

        This special method defines how to convert the block object to a string. 
        The hash of the block and the the number of the block are printed out. 
        '''
        return f"Block Hash: {str(self.hashid)} \nBlock Number: {str(self.block_number)}\n"
