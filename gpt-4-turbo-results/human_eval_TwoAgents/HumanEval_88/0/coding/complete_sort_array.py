# filename: complete_sort_array.py
from my_tests import run_tests

def sort_array(array):
    """
    Given an array of non-negative integers, return a copy of the given array after sorting,
    you will sort the given array in ascending order if the sum(first index value, last index value) is odd,
    or sort it in descending order if the sum(first index value, last index value) is even.

    Note:
    * don't change the given array.

    Examples:
    * sort_array([]) => []
    * sort_array([5]) => [5]
    * sort_array([2, 4, 3, 0, 1, 5]) => [0, 1, 2, 3, 4, 5]
    * sort_array([2, 4, 3, 0, 1, 5, 6]) => [6, 5, 4, 3, 2, 1, 0]
    """
    if not array:  # handles empty array
        return []

    sorted_array = sorted(array)  # sorting in ascending order
    if (array[0] + array[-1]) % 2 == 0:  # if sum of first and last element is even
        sorted_array = sorted_array[::-1]  # reverse the array for descending order
        
    return sorted_array

# Run the unit tests
run_tests(sort_array)