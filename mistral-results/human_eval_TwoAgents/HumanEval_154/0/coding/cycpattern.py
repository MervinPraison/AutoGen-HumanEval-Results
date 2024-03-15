# filename: cycpattern.py
from my_tests import run_tests

MOD = 10**9 + 7
POWER = 32

def hash_function(s):
    """
    Computes the hash value of a substring s using the Rabin-Karp Algorithm
    """
    hash_value = 0
    power_of_two = 1
    
    for char in reversed(s):
        hash_value += ord(char) * power_of_two
        power_of_two *= POWER

    return hash_value % MOD

def rabin_karp_match(pattern, text):
    """
    Returns the index at which the pattern is found in the text using Rabin-Karp Algorithm, or -1 if not found
    """
    if len(text) < len(pattern):
        return -1
    
    pattern_hash = hash_function(pattern)
    
    for i in range(len(text)):
        substring_hash = hash_function(text[i:i+len(pattern)])
        
        if substring_hash == pattern_hash and text[i:i+len(pattern)] == pattern:
            return i
            
        if i >= len(pattern) - 1:
            text_slice = text[:i]
            text_hash = hash_function(text_slice[-len(pattern):])
            text_slice += text[i:i+len(pattern)]
            text_slice = text_slice[len(pattern):]
            
            diff_hash = (text_hash - pattern_hash * POWER + MOD) % MOD
            
            if abs(diff_hash) <= (POWER ** 2):
                for j in range(min(i, len(pattern)-1)):
                    if text[i-j] != text[j]:
                        break
                    
                else:
                    return i - len(pattern)
            
    return -1

def cycpattern_check(a):
    words = a.split()
    
    pattern = " ".join(words[::-1])
    pattern = [int(ord(char)) for char in pattern] + [0] * len(words[0])

    result = rabin_karp_match(pattern, ' '.join(words))
    
    return result != -1