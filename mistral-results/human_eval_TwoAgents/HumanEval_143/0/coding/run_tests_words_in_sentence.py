# filename: run_tests_words_in_sentence.py
from my_tests import run_tests
import string

def is_prime(number):
    if number <= 1:
        return False

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False

    return True

def prime_numbers_up_to(limit):
    primes = []
    for number in range(2, limit + 1):
        if is_prime(number):
            primes.append(number)
    return primes

# Find prime numbers up to 100
prime_numbers = prime_numbers_up_to(100)

def words_in_sentence(sentence):
    words = sentence.split()

    result = ''
    for word in words:
        if len(word) in prime_numbers:
            result += ' ' + word

    return result

if __name__ == "__main__":
    sentences = [
        "This is a test",
        "lets go for swimming"
    ]

    for sentence in sentences:
        print(f'Input: {sentence}')
        output = words_in_sentence(sentence)
        print(f'Output: {output}\n')
        
    # Run the unit tests
    run_tests(words_in_sentence)