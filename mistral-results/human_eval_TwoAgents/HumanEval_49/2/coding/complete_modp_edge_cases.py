# filename: complete_modp_edge_cases.py

from my_tests import run_tests

def gcd(a, b):
    """Return the greatest common divisor of a and b using Euclidean algorithm"""
    while b != 0:
        a, b = b, a % b
    return abs(a)

def modp(n: int, p: int):
    """Return 2^n modulo p. Only supports n >= 0 and p > 0"""
    if n < 0 or p <= 0:
        raise ValueError("Invalid input values (n should be non-negative and p should be positive)")

    # Calculate 2^n using recursion with bitwise shifting
    result = 1
    while n > 0:
        if n % 2 == 1:
            result *= 2 % p
        n //= 2

    return result

# Run the unit tests
run_tests(modp)