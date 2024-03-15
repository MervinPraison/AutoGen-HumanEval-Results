# filename: enhanced_encode_v2.py
from my_tests import run_tests

def encode(message):
    """
    Takes a message, swaps case of all letters, replaces vowels with the letter two places ahead in the alphabet.
    """
    # Correcting vowel replacement rules and ensuring proper case swapping
    def swap_case_and_replace_vowel(letter):
        # Vowels to be replaced; indexed for finding the next vowel
        vowels_lower = 'aeiou'
        vowels_upper = 'AEIOU'
        # Check if the letter is a vowel and replace it accordingly
        if letter in vowels_lower:
            # Replace with next vowel (2 steps ahead), maintaining lowercase
            return vowels_lower[(vowels_lower.index(letter) + 2) % len(vowels_lower)]
        elif letter in vowels_upper:
            # Replace with next vowel (2 steps ahead), maintaining uppercase
            return vowels_upper[(vowels_upper.index(letter) + 2) % len(vowels_upper)]
        elif letter.isalpha():
            # Swap case for non-vowel letters
            return letter.lower() if letter.isupper() else letter.upper()
        # Return non-alphabetic characters as is
        return letter
    
    # Encoding each letter using a comprehensive approach for clarity and reliability
    encoded = "".join(swap_case_and_replace_vowel(char) for char in message)
    return encoded

# Run the unit tests on the corrected encode function
run_tests(encode)