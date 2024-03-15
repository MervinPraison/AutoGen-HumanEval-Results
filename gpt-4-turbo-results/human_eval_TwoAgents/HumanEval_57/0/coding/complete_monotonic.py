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
    if not l:  # Handles the empty list case
        return True
    
    # Determine the direction using the first two distinct elements
    direction = 0  # 1 for increasing, -1 for decreasing
    for i in range(1, len(l)):
        if l[i] > l[i-1]:
            direction = 1  # Increasing
            break
        elif l[i] < l[i-1]:
            direction = -1  # Decreasing
            break
            
    # Check monotonicity according to the determined direction
    for i in range(1, len(l)):
        if direction == 1 and l[i] < l[i-1]:
            return False  # Not increasing
        elif direction == -1 and l[i] > l[i-1]:
            return False  # Not decreasing
        
    return True

# Run the unit tests
run_tests(monotonic)