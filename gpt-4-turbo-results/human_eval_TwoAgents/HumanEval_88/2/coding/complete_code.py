# filename: complete_code.py
from my_tests import run_tests

def sort_array(array):
    """
    Given an array of non-negative integers, return a copy of the given array after sorting,
    you will sort the given array in ascending order if the sum( first index value, last index value) is odd,
    or sort it in descending order if the sum( first index value, last index value) is even.
    
    Note:
    * don't change the given array.

    Examples:
    * sort_array([]) => []
    * sort_array([5]) => [5]
    * sort_array([2, 4, 3, 0, 1, 5]) => [0, 1, 2, 3, 4, 5]
    * sort_array([2, 4, 3, 0, 1, 5, 6]) => [6, 5, 4, 3, 2, 1, 0]
    """
    if len(array) == 0:
        return array
    else:
        array_to_sort = array.copy()
        if (array_to_sort[0] + array_to_sort[-1]) % 2 == 0:
            array_to_sort.sort(reverse=True)
        else:
            array_to_sort.sort()
        return array_to_sort

# Run the unit tests
run_tests(sort_array)