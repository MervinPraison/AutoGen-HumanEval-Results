# filename: complete_modp_montgomery.py

from my_tests import run_tests
from math import log2

def montgomery_reduce(n: int, REDUCE_BY: int):
    """Reduce a number to a smaller representation using Montgomery reduction"""
    bit_length = len(bin(abs(n))[2:])
    mask = 1 << (bit_length - 1)
    r = 0
    n_masked = (n << log2(REDUCE_BY) | (n & ~((1 << bit_length) - 1))) & ((1 << bit_length) - 1)

    while n_masked != 0:
        q, n_masked = divmod(n_masked, REDUCE_BY)
        r |= q << (log2(REDUCE_BY) + i)
        i += 1

    result = r * ((1 << bit_length) // REDUCE_BY) % ((1 << bit_length) // REDUCE_BY)
    return result if n >= 0 else -result

def modp(n: int, p: int):
    """Return 2^n modulo p using Montgomery reduction"""
    if p <= 0 or (n % 2 == 0 and p % 2 != 0):
        raise ValueError("Invalid input values")

    REDUCE_BY = 2 ** int(log2(p))
    result = montgomery_reduce(1, REDUCE_BY) * montgomery_reduce(2, REDUCE_BY) ** (n >> 1) % p

    return result if n >= 0 else -result

# Run the unit tests
run_tests(modp)