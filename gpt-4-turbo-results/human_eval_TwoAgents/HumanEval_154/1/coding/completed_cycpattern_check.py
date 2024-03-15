# filename: completed_cycpattern_check.py
from my_tests import run_tests

def cycpattern_check(a, b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word."""
    length_b = len(b)
    for i in range(length_b):
        b_rotated = b[i:] + b[:i]  # Rotate b
        if b_rotated in a:  # Check if rotation of b is a substring of a
            return True
    return False

# Run the unit tests
run_tests(cycpattern_check)