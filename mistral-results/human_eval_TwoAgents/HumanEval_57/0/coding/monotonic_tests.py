# filename: monotonic_tests.py
from my_tests import run_tests

def monotonic(l: list):
    """Return True if list elements are monotonically increasing or decreasing."""
    return all(x <= y for x, y in zip(l, l[1:])) or all(x >= y for x, y in zip(l, l[1:]))

if __name__ == '__main__':
    run_tests(monotonic)