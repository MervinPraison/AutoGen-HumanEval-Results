# filename: complete_code_with_gcd_and_tests.py
from my_tests import run_tests

def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b.
    """
    while b != 0:
        a, b = b, a % b
    return a

# Run the unit tests
run_tests(greatest_common_divisor)