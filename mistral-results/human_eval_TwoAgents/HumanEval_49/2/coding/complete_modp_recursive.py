# filename: complete_modp_recursive.py

from my_tests import run_tests

def exponentiate_modp(base, exponent, modulo):
    """Return base^exponent modulo modulo using recursion"""
    if exponent == 0:
        return 1

    result = (base * exponentiate_modp(base, exponent-1, modulo)) % modulo
    return result

def modp(n, p):
    """Return 2^n modulo p"""
    return exponentiate_modp(2, n, p)

# Run the unit tests
run_tests(modp)