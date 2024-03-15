# filename: complete_cycpattern_check.py
from my_tests import run_tests

def cycpattern_check(a, b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True
    """
    if len(b) > len(a):
        return False

    # To cover all rotations, append b to itself.
    # A valid rotation that is a substring of a would be in this new string.
    b_rotated = b + b

    # Check if b or any of its rotations (now part of b_rotated) is a substring of a.
    return any(b_rotated[i:i+len(b)] in a for i in range(len(b)))

# Run the unit tests
run_tests(cycpattern_check)