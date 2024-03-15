# filename: run_tests_for_check_dict_case.py

from my_tests import run_tests

def check_dict_case(dictionary):
    """
    Given a dictionary, return True if all keys are strings and either in lower
    or upper case, else return False. The function should return False if the
    given dictionary is empty.
    Examples:
    check_dict_case({"a":"apple", "b":"banana"}) should return True.
    check_dict_case({"a":"apple", "A":"banana", "B":"banana"}) should return False.
    check_dict_case({"a":"apple", 8:"banana", "a":"apple"}) should return False.
    check_dict_case({"Name":"John", "Age":"36", "City":"Houston"}) should return False.
    check_dict_case({"STATE":"NC", "ZIP":"12345" }) should return True.
    """

    if len(dictionary) == 0:
        return False

    keys = dictionary.keys()
    is_lower_or_upper = all([isinstance(key, str) and (key.islower() or key.isupper()) for key in keys])

    return is_lower_or_upper

# Run the unit tests
run_tests(check_dict_case)