# filename: cycpattern_complete.py
from my_tests import run_tests

def cycpattern_check(a, b):
    """Checks if the second word or any of its rotations is a substring of the first word."""
    for i in range(len(b)):
        rotated_b = b[i:] + b[:i]  # Rotate `b` by `i` positions
        if rotated_b in a:  # Check if rotated `b` is a substring of `a`
            return True
    return False

# Run the unit tests
run_tests(cycpattern_check)