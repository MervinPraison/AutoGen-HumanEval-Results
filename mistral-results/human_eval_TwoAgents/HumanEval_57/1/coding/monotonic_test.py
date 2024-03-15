# filename: monotonic_test.py

from my_tests import run_tests
import pdb

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing."""
    if len(l) < 2:
        return True
    elif all(x <= y for x, y in zip(l, l[1:])) or all(x >= y for x, y in zip(l, l[1:])): # Handle both increasing and decreasing sequences
        return True
    else:
        return False
        
if __name__ == "__main__":
    run_tests(monotonic)