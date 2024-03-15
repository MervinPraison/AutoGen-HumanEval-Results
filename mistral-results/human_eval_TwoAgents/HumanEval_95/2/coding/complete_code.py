# filename: complete_code.py

def check_dict_case(dict):
    """
    Given a dictionary, return True if all keys are strings in lower case or all keys are strings in upper case, else return False.
    The function should return False is the given dictionary is empty.
    """
    if len(dict) == 0:
        return False

    key_values = dict.items()
    for key_value in key_values:
        if not isinstance(key_value[0], (str)):
            return False
        if (isinstance(key_value[0], str) and not all(c.islower() for c in key_value[0])) or \
           (isinstance(key_value[0], str) and not all(c.isupper() for c in key_value[0])):
            return False

    return True

from my_tests import run_tests

run_tests(check_dict_case)