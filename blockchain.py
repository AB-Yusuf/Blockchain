#Stopped at video 54

#now at video 57
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
    else:
        print('Blocks display complete', end="\n\n")
        print(blockchain)
        
            
def verify_chain():
    block_index = 0
    is_valid = True
    
    for block_index in range(len(blockchain)):
        if block_index == 0:
            block_index += 1
            continue
        elif blockchain[block_index][0] == blockchain[block_index-1]:
            is_valid = True
        else:
            is_valid = False
            break
    return is_valid

sentinel = True    

while sentinel:
    print('Please choose')
    print('1. Add a new transaction value')
    print('2. Display each block in the blockchain')
    print('m: Manipulate the chain')
    print('v: verify chain')
    print('q: Quit')
    
    user_choice = get_user_choice()
    if user_choice == '1':
        amount = get_transaction_amount()
        add_transaction(last_transaction=get_last_block_details(), transaction_amount=amount)
    elif user_choice == '2':
        print_blockchain_elements()
    elif user_choice == 'm':
        if len(blockchain) >= 1:
            blockchain[0] = 2
    elif user_choice == 'v':
        verify_chain()
    elif user_choice == 'q':
        sentinel = False
    else:
        print('Invalid input, pick a value from the list.')
    
    #if not verify_chain():
    #   print('Invalid blockchain')
    #   break

else:
    print('User Left')
    
print('Session Ended')