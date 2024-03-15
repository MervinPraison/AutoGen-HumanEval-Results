# filename: complete_monotonic.py
from my_tests import run_tests

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    if len(l) < 2:
        return True  # A list with 0 or 1 element is trivially monotonic
    
    # Determine if the sequence is increasing or decreasing based on the first two elements
    is_increasing = None
    for i in range(1, len(l)):
        if l[i] != l[i-1]:  # Find the first non-equal consecutive elements to determine direction
            is_increasing = (l[i] > l[i-1])
            break
    
    if is_increasing is None:  # If all elements are the same, the list is monotonic
        return True

    if is_increasing:
        for i in range(1, len(l)):
            if l[i] < l[i-1]:  # If the list decreases at any point, it's not monotonic
                return False
    else:
        for i in range(1, len(l)):
            if l[i] > l[i-1]:  # If the list increases at any point, it's not monotonic
                return False
    
    return True

# Run the unit tests
run_tests(monotonic)