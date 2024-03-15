# filename: complete_encode.py
from my_tests import run_tests

def encode(message):
    """
    Write a function that takes a message, and encodes in such a 
    way that it swaps case of all letters, replaces all vowels in 
    the message with the letter that appears 2 places ahead of that 
    vowel in the English alphabet. 
    Assume only letters. 
    
    Examples:
    >>> encode('test')
    'TGST'
    >>> encode('This is a message')
    'tHKS KS C MGSSCGG'
    """
    vowel_map = {
        'a': 'c',
        'e': 'g',
        'i': 'k',
        'o': 'q',
        'u': 'w',
        'A': 'C',
        'E': 'G',
        'I': 'K',
        'O': 'Q',
        'U': 'W'
    }
    
    encoded_message = []
    
    for character in message:
        if character.isalpha():
            swapped_case = character.swapcase()
            encoded_message.append(vowel_map.get(swapped_case, swapped_case))
        else:
            encoded_message.append(character)
            
    return ''.join(encoded_message)

# Run the unit tests
run_tests(encode)