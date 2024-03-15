# filename: complete_sorting.py

from my_tests import run_tests

def is_odd(num):
    """
    Determines if given number is odd or not.
    :param num: an integer number
    :return: True if the number is odd, False otherwise
    """
    return num % 2 == 1

def sort_array(array):
    """
    Given an array of non-negative integers, returns a copy of the given array after sorting.
    Sorts the given array in ascending order if the sum (first index value, last index value) is odd,
    or sorts it in descending order if the sum (first index value, last index value) is even.

    Note:
    * don't change the given array
    """
    if is_odd(sum(array[0], array[-1])):
        array.sort()
    else:
        array.reverse()
    
    return array

if __name__ == "__main__":
    # Run the unit tests
    run_tests(sort_array)