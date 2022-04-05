A Python blockchain (Created by Vidur Subaiah) ==>

A private blockchain that creates a time-stamped series of records, where each block of data is connected to another block using the SHA-256 hashing algorithm. The blockchain ensures that each block contains its own hash as well as the hash of the previous block of data. The blockchain is added to by successfully finding the answer to a proof of work problem. 
The validity of the blockchain and the current sequence of blocks can be checked mathematically. The blockchain is deployed locally on a network using Flask. 


Block Class ==>

Block objects are the basic building blocks of the blockchain. They possess a list of transactions that have occurred, the timestamp of these transactions, a hash id, and a hash id of the previous block in the chain. Blocks are mined and added to the blockchain by solving the proof of work problem.  


Blockchain Class ==>

The blockchain class holds the blocks that are part of the blockchain. The object defines the difficuly involved in mining new blocks and also possesses a list of transactions that are yet to be added to the blockchain at any given time. The validity of blocks in the blockchain can be verified to ensure that the proof of work problem has been solved for each block and that each block is immutably tied to the previous block through the hash id. 


API.py ==>

The file that deploys the blockchain on a network using Flask. Nodes on the network can submit transactions to be included on the blockchain as well as mine pending transactions. Nodes on the network can obtain consensus on the most accurate chain by adopting the longest chain possessed by a node on the network. Nodes are rewarded for mining blocks correctly. 


Running the blockchain and executing transactions ==>

A demonstration of how to properly set up the blockchain on your local network and interact with the chain can be found through the Blockchain-Project-Video file in this repository. (Program developed and tested using Python 3.8)


----

Enjoy the power of the blockchain and adopting it to meet your needs!