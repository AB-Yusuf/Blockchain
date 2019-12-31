"""
Seeding blockhain with an initial value of 1
"""
blockchain = []

def get_last_block_details():
    if len(blockchain) < 1:
        return None
    return blockchain[-1]

def add_transaction(transaction_amount, last_transaction=[1]):
    """
    Adding new block to the chain, which contains
    details of previous block
    In this case each block is said to contain just
    a single digit
    """
    if last_transaction == None:
        last_transaction = [1]
    blockchain.append([last_transaction, transaction_amount])
    

def get_transaction_amount():
    user_input = float(input('Your transaction amount please: '))
    return user_input

def get_user_choice():
    user_choice  = input('Your choice: ')
    return user_choice

def print_blockchain_elements():
    for block in blockchain:
            print('Outputting Block')
            print(block)
    

while True:
    print('Pleasechoose')
    print('1. Add a new transaction value')
    print('2. Display each block in the blockchain')
    print('q: Quit')
    
    user_choice = get_user_choice()
    if user_choice == '1':
        amount = get_transaction_amount()
        add_transaction(last_transaction=get_last_block_details(), transaction_amount=amount)
    elif user_choice == '2':
        print_blockchain_elements()
    elif user_choice == 'q':
        break
    else:
        print('Invalid input, pick a value from the list.')

print('Session Ended')