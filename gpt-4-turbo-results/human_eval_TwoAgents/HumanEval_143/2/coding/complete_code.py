# filename: complete_code.py
from my_tests import run_tests

def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def words_in_sentence(sentence):
    """
    Given a string representing a sentence, returns a string that contains the words from the original sentence,
    whose lengths are prime numbers. The order of the words in the new string should be the same as the original one.
    """
    # Split the sentence into words
    words = sentence.split()
    
    # Filter words where word length is prime
    prime_length_words = [word for word in words if is_prime(len(word))]
    
    # Join and return those words
    return " ".join(prime_length_words)

# Run the unit tests
run_tests(words_in_sentence)