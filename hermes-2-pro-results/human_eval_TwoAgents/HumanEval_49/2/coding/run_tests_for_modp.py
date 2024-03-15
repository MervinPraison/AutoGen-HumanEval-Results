# filename: run_tests_for_modp.py

from my_tests import run_tests

def fast_exponentiate(base, exponent, modulus):
    result = 1
    base = base % modulus
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        exponent = exponent // 2
        base = (base * base) % modulus
    return result

def modp(n: int, p: int):
    return fast_exponentiate(2, n, p)

# Test cases for modp function
TEST_MODP = [(3, 5), (1101, 101), (0, 101), (3, 11), (100, 101)]

def run_tests_modp(func, *args):
    return run_tests(func, *args)

# Run the tests with different p values
for t in TEST_MODP:
    run_tests_modp(modp, *t)