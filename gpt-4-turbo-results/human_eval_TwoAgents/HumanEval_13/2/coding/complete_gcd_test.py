# filename: complete_gcd_test.py
from my_tests import run_tests

def greatest_common_divisor(a: int, b: int) -> int:
    """Return the greatest common divisor of two integers a and b."""
    while b:
        a, b = b, a % b
    return a

# Run the unit tests
run_tests(greatest_common_divisor)