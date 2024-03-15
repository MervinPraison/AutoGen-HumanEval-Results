# filename: main.py
from my_tests import run_tests
from typing import List
import operator

def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    """
    if len(string) == 0:
        return []
    else:
        return [''] + list(map(lambda i: string[:i+1], range(1, len(string)+1))) + all_prefixes(string[len(string)-1:])

if __name__ == "__main__":
    run_tests(all_prefixes)