# filename: my_tests_solution.py

from my_tests import run_tests


def check_dict_case(dictionary):
    """
    Given a dictionary, return True if all keys are strings in lower 
    case or all keys are strings in upper case, else return False.
    The function should return False is the given dictionary is empty.
    """
    if not dictionary:
        return False
    case_ok = all(isinstance(key, str) and (key.islower() or key.isupper()) for key in dictionary)
    return case_ok


# Run the unit tests
run_tests(check_dict_case)