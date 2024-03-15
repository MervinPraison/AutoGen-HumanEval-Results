# filename: test_filter_integers.py
from my_tests import run_tests

def filter_integers(values: list) -> list:
    """ Filter given list of any python values only for integers
    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {}, []])
    [1, 2, 3]
    """
    return [i for i in values if type(i) is int]

if __name__ == "__main__":
    run_tests(filter_integers)