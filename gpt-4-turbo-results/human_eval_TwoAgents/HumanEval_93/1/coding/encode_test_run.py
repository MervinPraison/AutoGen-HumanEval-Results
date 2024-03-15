# filename: encode_test_run.py
from my_tests import run_tests

def encode(message):
    """
    Write a function that takes a message, and encodes in such a 
    way that it swaps case of all letters, replaces all vowels in 
    the message with the letter that appears 2 places ahead of that 
    vowel in the english alphabet. 
    Assume only letters. 
    
    Examples:
    >>> encode('test')
    'TGST'
    >>> encode('This is a message')
    'tHKS KS C MGSSCGG'
    """
    vowels = 'aeiouAEIOU'
    # Dictionary to map each vowel to two places ahead
    vowel_map = {'a': 'c', 'e': 'g', 'i': 'k', 'o': 'q', 'u': 'w',
                 'A': 'C', 'E': 'G', 'I': 'K', 'O': 'Q', 'U': 'W'}
    
    encoded_msg = ''
    
    for char in message:
        # Swap case using swapcase() method
        swapped_char = char.swapcase()
        # Replace vowel if it's in the vowels list
        if swapped_char in vowels:
            encoded_msg += vowel_map[swapped_char]
        else:
            encoded_msg += swapped_char
            
    return encoded_msg

# Run the unit tests
run_tests(encode)