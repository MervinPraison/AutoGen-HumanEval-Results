# filename: enhanced_encode.py
from my_tests import run_tests

def encode(message):
    """
    Write a function that takes a message, and encodes it in such a 
    way that it swaps case of all letters, replaces all vowels in 
    the message with the letter that appears 2 places ahead of that 
    vowel in the English alphabet. 
    Assume only letters.
    """
    # Define a function to replace vowels and swap the case
    def encode_char(c):
        vowels = 'aeiouAEIOU'
        # Mapping for vowels to be replaced by the character 2 positions ahead
        replacement = {'a': 'c', 'e': 'g', 'i': 'k', 'o': 'q', 'u': 'w',
                       'A': 'C', 'E': 'G', 'I': 'K', 'O': 'Q', 'U': 'W'}
        if c in vowels:
            return replacement[c]
        elif c.isalpha():
            return c.lower() if c.isupper() else c.upper()
        return c

    # Use a list comprehension for efficiency and readability
    encoded_message = ''.join(encode_char(c) for c in message)
    return encoded_message

# Run the unit tests to verify the corrected implementation
run_tests(encode)