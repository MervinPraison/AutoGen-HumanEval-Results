# filename: full_code.py

def check_dict_case(dict):
    """
    Given a dictionary, return True if all keys are strings in lower case or
    all keys are strings in upper case, else return False. If the given
    dictionary is empty, then return False.
    Examples:
    check_dict_case({"a":"apple", "b":"banana"}) should return True.
    check_dict_case({"a":"apple", "A":"banana", "B":"banana"}) should return False.
    check_dict_case({"a":"apple", 8:"banana", "a":"apple"}) should return False.
    check_dict_case({"Name":"John", "Age":"36", "City":"Houston"}) should return False.
    check_dict_case({"STATE":"NC", "ZIP":"12345" }) should return True.
    """
    if not dict:
        return False
    elif all(isinstance(key, str) for key in dict.keys()) and (all(key.islower() for key in dict.keys()) or all(key.isupper() for key in dict.keys())):
        return True
    else:
        return False

from my_tests import run_tests

if __name__ == "__main__":
    check_dict_case_result = check_dict_case({"STATE":"NC", "ZIP":"12345" })
    print("check_dict_case result:", check_dict_case_result)
    run_tests(check_dict_case)