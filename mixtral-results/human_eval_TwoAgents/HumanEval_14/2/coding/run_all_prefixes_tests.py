# filename: run_all_prefixes_tests.py

from my_tests import run_tests

from typing import List

def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    prefixes = []
    for i in range(len(string)):
        prefix = string[:i+1]
        prefixes.append(prefix)
    return prefixes

# Run the unit tests
run_tests(all_prefixes)