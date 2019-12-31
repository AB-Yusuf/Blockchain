"""
Seeding blockhain with an initial value of 1
"""
blockchain = []

def get_last_block_details():
    return blockchain[-1]

def add_value(transaction_amount, last_transaction=[1]):
    """
    Adding new block to the chain, which contains
    details of previous block
    In this case each block is said to contain just
    a single digit
    """
    blockchain.append([last_transaction, transaction_amount])
    

def get_user_input():
    return float(input('Your transaction amount please: '))


amount = get_user_input()
add_value(amount) 

while True:
    amount = get_user_input()
    add_value(last_transaction=get_last_block_details(), transaction_amount=amount)

    for block in blockchain:
        print('Outputting Block')
        print(block)