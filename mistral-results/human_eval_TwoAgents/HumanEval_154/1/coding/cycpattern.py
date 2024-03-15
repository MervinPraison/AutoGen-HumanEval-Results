# filename: cycpattern.py

from my_tests import run_tests
import itertools

def rotate(string):
    """Return all rotations of given string."""
    return [s + s[1:] for s in itertools.cycle([string])]

def cycpattern_check(a, b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word."""
    if len(a) < len(b):
        return cycpattern_check(b, a)

    # Check if the given string `b` is a substring of `a`
    for i in range(len(a)):
        if a[i:i+len(b)] == b:
            return True

    # Check if any rotation of `b` is a substring of `a`
    rotations = rotate(b)
    for rotation in rotations:
        if a.find(rotation) != -1:
            return True

    return False

if __name__ == "__main__":
    run_tests(cycpattern_check)