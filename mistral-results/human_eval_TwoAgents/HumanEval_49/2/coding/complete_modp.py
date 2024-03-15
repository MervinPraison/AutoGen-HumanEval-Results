# filename: complete_modp.py

from my_tests import run_tests
import math

def powmod(x, y, p):
    """Calculate x ^ y % p using fast exponentiation method"""
    if y == 0:
        return 1
    if y % 2 != 0:
        # If y is odd, we can use the following property: (x * x) ^ (y / 2) % p = ((x ^ (y / 2)) ^ 2) % p
        result = powmod(x, y // 2, p)
        return (result * result) % p
    # If y is even, we calculate (x ^ (y / 2)) ^ 2 % p and take the square root using modular inverse to get x ^ y % p
    result = powmod(x, y // 2, p)
    return (result * result) % p if y > 0 else pow(pow(result, 2), math.floor(math.log(p, 2)), p)

def modp(n: int, p: int):
    """Return 2^n modulo p"""
    return powmod(2, n, p)

# Run the unit tests
run_tests(modp)