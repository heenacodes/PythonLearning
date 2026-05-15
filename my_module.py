print("This is an imported module")

test = 'test string'

def find_index(to_search, target):
    '''Find index of a value in sequence'''
    for i, value in enumerate(target):
        if value==to_search:
            return i
        
    return -1
    
