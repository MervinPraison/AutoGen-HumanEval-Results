# filename: complete_check_dict_case.py
from my_tests import run_tests

def check_dict_case(dict):
    """
    Given a dictionary, return True if all keys are strings in lower 
    case or all keys are strings in upper case, else return False.
    The function should return False is the given dictionary is empty.
    Examples:
    check_dict_case({"a":"apple", "b":"banana"}) should return True.
    check_dict_case({"a":"apple", "A":"banana", "B":"banana"}) should return False.
    check_dict_case({"a":"apple", 8:"banana", "A":"apple"}) should return False.
    check_dict_case({"Name":"John", "Age":"36", "City":"Houston"}) should return False.
    check_dict_case({"STATE":"NC", "ZIP":"12345" }) should return True.
    """
    if not dict:
        return False
    elif all(isinstance(key, str) and key.islower() for key in dict.keys()):
        return True
    elif all(isinstance(key, str) and key.isupper() for key in dict.keys()):
        return True
    else:
        return False

# Run the unit tests
run_tests(check_dict_case)