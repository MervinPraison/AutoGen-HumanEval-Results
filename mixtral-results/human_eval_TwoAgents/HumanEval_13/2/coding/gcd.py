# filename: gcd.py

from my_tests import run_tests

def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    # Modified Euclidean algorithm
    while b:
        a, b = b, a % b
    return a

# Run the unit tests
run_tests(greatest_common_divisor)