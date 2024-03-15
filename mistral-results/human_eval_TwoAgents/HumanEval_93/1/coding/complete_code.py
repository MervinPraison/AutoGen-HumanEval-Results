# filename: complete_code.py
import string
import my_tests

def encode(message):
    vowels = "aeiouy"
    encoded_message = ""

    for char in message:
        if char == ' ':
            encoded_message += 'SS' if (prev_char in vowels or not prev_char) else ' '
            next_char = vowels[-1] if encoded_message[-1].isdigit() or (encoded_message and encoded_message[-1] != vowels[-1]) else ''
            encoded_message += next_char
            prev_char = char
        elif char in vowels:
            next_char = "qu" if char.isupper() else "qe"
            encoded_message += next_char
        elif char.isspace():
            encoded_message += ' '
        else:
            next_char = string.ascii_lowercase[::-1][string.find(string.ascii_lowercase, char) + 2] if char in vowels else (char if char.isupper() else char.lower())
            encoded_message += next_char
        prev_char = char
    return encoded_message

# Move the unit tests to a separate file named 'tests.py' in the same directory as 'complete_code.py'
# This file should start with the following lines:
# __all__ = ['run_tests']
# import unittest, sys, os
# sys.path.append(os.getcwd())

if __name__ == '__main__':
    my_tests.run_tests(encode)