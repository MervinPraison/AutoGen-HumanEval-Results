# filename: complete_modp_bitwise.py

from my_tests import run_tests

def modp(n: int, p: int):
    """Return 2^n modulo p using bitwise exponentiation"""
    if p == 0:
        return 0

    result = 1
    power = n
    while power > 0:
        if power % 2 == 1:
            result = (result * 2) % p
        power = power >> 1

    return result

# Run the unit tests
run_tests(modp)