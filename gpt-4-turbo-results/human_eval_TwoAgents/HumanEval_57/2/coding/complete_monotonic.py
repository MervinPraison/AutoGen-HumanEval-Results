# filename: complete_monotonic.py
from my_tests import run_tests

def monotonic(l: list):
    """Return True if list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    if not l:  # Empty list case
        return True
    increasing = None
    for i in range(1, len(l)):
        if l[i] > l[i - 1]:  # Current element is greater than the previous
            if increasing == False:
                return False
            increasing = True
        elif l[i] < l[i - 1]:  # Current element is less than the previous
            if increasing == True:
                return False
            increasing = False
    return True

# Run the unit tests
run_tests(monotonic)