from blockchain import Blockchain
from block import Block

the_blockchain = Blockchain(20)

data = ''
while data != "False":
    data = input("Enter transactions to add to block: ")
    if data == "False":
        continue
    results = data.split(',')
    the_blockchain.add_to_transactions(results[0], results[1], results[2])
    the_blockchain.mine_transactions()
    print(the_blockchain)
   
    
print("\n")
print(Blockchain.validate_chain(the_blockchain))
print(type(the_blockchain.chain[-1]) == Block)
