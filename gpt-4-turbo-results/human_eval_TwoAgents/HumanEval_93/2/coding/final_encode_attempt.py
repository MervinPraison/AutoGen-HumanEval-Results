# filename: final_encode_attempt.py
from my_tests import run_tests

def encode(message):
    """
    Encode a message by swapping case and replacing vowels with the letter 
    two steps ahead in the alphabet.
    """
    # Define the transformations: vowels and their replacements
    vowels = 'aeiou'
    replacements = {v: chr(((ord(v) - 97 + 2) % 26) + 97) for v in vowels}  # For lowercase
    replacements.update({v.upper(): chr(((ord(v.upper()) - 65 + 2) % 26) + 65) for v in vowels})  # For uppercase

    encoded_message = []
    for char in message:
        if char in replacements.keys():
            encoded_message.append(replacements[char])
        elif char.isalpha():
            encoded_message.append(char.lower() if char.isupper() else char.upper())
        else:
            encoded_message.append(char)

    return ''.join(encoded_message)

# Run the unit tests
run_tests(encode)