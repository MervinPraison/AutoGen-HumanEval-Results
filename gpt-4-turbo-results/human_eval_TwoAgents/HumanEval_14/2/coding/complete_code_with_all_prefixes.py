# filename: complete_code_with_all_prefixes.py
from typing import List

def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    return [string[:i+1] for i in range(len(string))]

# Assuming the my_tests.py exists in the same directory and has run_tests function ready to use
# Importing run_tests
from my_tests import run_tests

# Run the unit tests
run_tests(all_prefixes)