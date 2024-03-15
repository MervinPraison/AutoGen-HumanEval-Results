# filename: complete_code.py
from my_tests import run_tests

def is_prime(n):
    """Check if a number is a prime number."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def words_in_sentence(sentence):
    """
    You are given a string representing a sentence,
    the sentence contains some words separated by a space,
    and you have to return a string that contains the words from the original sentence,
    whose lengths are prime numbers,
    the order of the words in the new string should be the same as the original one.
    """
    words = sentence.split(' ')
    prime_length_words = [word for word in words if is_prime(len(word))]
    return ' '.join(prime_length_words)

# Run the unit tests
run_tests(words_in_sentence)