# filename: paired_sum.py
from my_tests import run_tests

def pairs_sum_to_zero(lst):
    """
    pairs_sum_to_zero takes a list as an input and returns True if there are two distinct elements in the list that sum to zero, False otherwise.
    """
    lst = set(lst)  # convert the list to a set to remove duplicates while iterating through pairs
    for i in lst:
        j = -i
        if j in lst and i != j:
            return True
    return False

if __name__ == "__main__":
    run_tests(pairs_sum_to_zero)