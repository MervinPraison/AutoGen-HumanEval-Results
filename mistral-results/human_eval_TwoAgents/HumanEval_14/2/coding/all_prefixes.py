# filename: all_prefixes.py

import itertools
from my_tests import run_tests

def all_prefixes(string: str) -> list:
    """ Return list of all prefixes from shortest to longest of the input string
        >>> all_prefixes('abc')
        ['a', 'ab', 'abc']
    """
    return [""] + list(string) + list(itertools.product(string, repeat=len(string)))

if __name__ == "__main__":
    run_tests(all_prefixes)