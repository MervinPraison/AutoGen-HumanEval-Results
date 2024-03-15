# filename: final_code.py
from my_tests import run_tests

def is_prime(n):
    """Check if a number is a prime number."""
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def words_in_sentence(sentence):
    """
    Returns a string that contains the words from the input sentence,
    whose lengths are prime numbers.
    """
    # Split input sentence into words
    words = sentence.split()
    
    # Filter words where length of each word is a prime number
    prime_length_words = [word for word in words if is_prime(len(word))]
    
    # Join these words into a string and return
    return ' '.join(prime_length_words)

# Run the unit tests
run_tests(words_in_sentence)