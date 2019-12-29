"""
Seeding blockhain with an initial value of 1
"""
blockchain = [[1]]

def get_last_block_details():
    return blockchain[-1]

def add_value(transaction_amount):
    """
    Adding new block to the chain, which contains
    details of previous block
    In this case each block is said to contain just
    a single digit
    """
    blockchain.append([get_last_block_details(),transaction_amount])
    print(blockchain)
    
add_value(2)
add_value(3)

 