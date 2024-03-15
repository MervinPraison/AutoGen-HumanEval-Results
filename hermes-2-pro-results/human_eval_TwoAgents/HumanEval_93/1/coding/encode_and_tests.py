# filename: encode_and_tests.py

from my_tests import run_tests


def encode(message):
    """
    Write a function that takes a message, and encodes in such a way that it swaps case of all letters,
    replaces all vowels in the message with the letter that appears 2 places ahead of that vowel in the
    English alphabet. Assume only letters.
    """
    result = ""
    for char in message:
        if char.isalpha():
            char_code = ord(char)
            new_char_code = ((char_code + 7) % 26) + ord('A')
            result += chr(new_char_code)
        else:
            result += char
    vowels = 'AEIOUaeiou'
    encoded_vowels = ''
    for vowel in vowels:
        new_vowel = chr(((ord(vowel) - ord('A') + 2) % 26) + ord('A'))
        encoded_vowels += new_vowel
    message_vowels = ''.join([c for c in message.upper() if c in vowels])
    result = result.replace(message_vowels, encoded_vowels)
    return result


# Define the encode function completely
run_tests(encode)