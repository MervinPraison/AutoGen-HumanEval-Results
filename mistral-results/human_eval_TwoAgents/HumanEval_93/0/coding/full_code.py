# filename: full_code.py
import my_tests

def encode(message):
    vowels = 'aeiou'
    encoded_message = ''
    for char in message:
        if char in vowels:
            next_vowel_index = vowels.find(char) + 1
            encoded_message += vowels[next_vowel_index]
        else:
            if char.islower():
                encoded_message += char.upper()
            else:
                encoded_message += char.lower()
    return encoded_message

if __name__ == '__main__':
    my_tests.run_tests(encode)