# filename: complete_code_with_tests.py
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """ Filter given list of any python values only for integers """
    return [item for item in values if isinstance(item, int)]

from my_tests import run_tests

# Run the unit tests
run_tests(filter_integers)