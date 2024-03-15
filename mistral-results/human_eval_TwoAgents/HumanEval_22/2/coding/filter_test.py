# filename: filter_test.py

from my_tests import run_tests
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """ Filter given list of any python values only for integers

        Args:
            values (List[Any]): input list containing elements of any types

        Returns:
            List[int]: output list that contains only the integers from the input list
        """

    # Using list comprehension to filter integers
    return [i for i in values if isinstance(i, int)]

if __name__ == '__main__':
    run_tests(filter_integers)