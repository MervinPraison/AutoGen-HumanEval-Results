# filename: complete_pairs_sum.py
from my_tests import run_tests

def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    >>> pairs_sum_to_zero([1, 3, 5, 0])
    False
    >>> pairs_sum_to_zero([1, 3, -2, 1])
    False
    >>> pairs_sum_to_zero([1, 2, 3, 7])
    False
    >>> pairs_sum_to_zero([2, 4, -5, 3, 5, 7])
    True
    >>> pairs_sum_to_zero([1])
    False
    """
    seen = set()  # Keep track of elements seen in the list
    for el in l:
        if -el in seen:
            return True  # A pair sums to zero
        seen.add(el)
    return False  # No pair sums to zero

# Run the unit tests
run_tests(pairs_sum_to_zero)