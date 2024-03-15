# filename: pairs_sum_to_zero.py
from my_tests import run_tests

def pairs_sum_to_zero(lst):
    """
    Check if there exist any two numbers in the list such that their sum is zero.
    :param lst: A list of numbers
    :return: True if there are two distinct elements in the list that sum to zero, False otherwise.
    """

    unique_nums = set(lst)
    
    for num1 in unique_nums:
        complement = 0 - num1
        if complement in unique_nums and num1 != complement:
            return True

    return False

def main():
    test_cases = [
        ([1, 3, 5, 0]),
        ([1, 3, -2, 1]),
        ([1, 2, 3, 7])
    ]
    
    for test_case in test_cases:
        print(f"Test case input: {test_case}")
        result = pairs_sum_to_zero(test_case)
        expected = (2 if sum(test_case) == 0 else False)
        
        print(f"\tExpected output: {expected}")
        print(f"\tOutput: {result}\n")
        
        assert result == expected, f"Test case failed: Output is not as expected. Expected: {expected}, got: {result}"

if __name__ == "__main__":
    main()