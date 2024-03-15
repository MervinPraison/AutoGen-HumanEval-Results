# filename: greatest_common_divisor.py
from my_tests import run_tests

def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b using Euclidean algorithm
        >>> greatest_common_divisor(3, 5)
        1
        >>> greatest_common_divisor(25, 15)
        5
    """
    while b != 0:
        a, b = b, a % b
    return abs(a)

if __name__ == "__main__":
    run_tests(greatest_common_divisor)