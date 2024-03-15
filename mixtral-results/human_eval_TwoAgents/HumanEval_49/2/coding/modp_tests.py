# filename: modp_tests.py

import math
from my_tests import run_tests

def modp(n: int, p: int):
    """Return 2^n modulo p (be aware of numerics)."""
    if n == 0:
        return 1
    result = 2
    for _ in range(1, n):
        result = (result * 2) % p
    return result

if __name__ == "__main__":
    # Run the unit tests
    run_tests(modp)