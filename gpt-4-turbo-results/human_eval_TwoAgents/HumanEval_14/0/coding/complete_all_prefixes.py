# filename: complete_all_prefixes.py
from my_tests import run_tests
from typing import List

def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    return [string[:i+1] for i in range(len(string))]

# Run the unit tests
run_tests(all_prefixes)