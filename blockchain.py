"""
Seeding blockhain with an initial value of 1
"""
blockchain = [[1]]

def add_value():
    """
    Adding new block to the chain, which contains
    details of previous block
    In this case each block is said to contain just
    a single digit
    """
    blockchain.append([blockchain[-1],2])
    print(blockchain)
    
add_value()
add_value()

 