# filename: complete_modp_with_tests.py
from my_tests import run_tests

def modp(n: int, p: int):
    """Return 2^n modulo p (be aware of numerics).
    >>> modp(3, 5)
    3
    >>> modp(1101, 101)
    2
    >>> modp(0, 101)
    1
    >>> modp(3, 11)
    8
    >>> modp(100, 101)
    1
    """
    # Implementing the function using efficient exponentiation by squaring
    result = 1
    base = 2
    while n > 0:
        if n % 2 == 1:
            result = (result * base) % p
        base = (base * base) % p
        n //= 2
    return result

# Run the unit tests
run_tests(modp)