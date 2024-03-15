# filename: complete_sort_array.py

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
    # Copy the array to avoid modifying the original array
    sorted_array = array.copy()
    
    if not sorted_array:
        return sorted_array
    elif (sorted_array[0] + sorted_array[-1]) % 2 == 0:
        # Sum is even, sort in descending order
        sorted_array.sort(reverse=True)
    else:
        # Sum is odd, sort in ascending order
        sorted_array.sort()

    return sorted_array

# Run the unit tests
run_tests(sort_array)