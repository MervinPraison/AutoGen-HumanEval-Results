# filename: cycpattern_check.py
from my_tests import run_tests

def rotation(word, n):
    """Function to find the nth rotation of a given string."""
    return word[-n:] + word[:-n]

def cycpattern_check(a, b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word"""
    return any((rotation(b, i) in a for i in range(len(b)))) or (b in a)

if __name__ == "__main__":
    run_tests(cycpattern_check)