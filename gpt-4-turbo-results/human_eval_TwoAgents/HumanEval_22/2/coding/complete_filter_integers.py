# filename: complete_filter_integers.py
from my_tests import run_tests
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any Python values, returning only integers
    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {}, []])
    [1, 2, 3]
    """
    # Return only items that are instances of int
    return [item for item in values if isinstance(item, int)]

# Run the unit tests
run_tests(filter_integers)