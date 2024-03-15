# filename: check_dict_case.py

from my_tests import run_tests
import operator

def is_all_keys_same_case(dct, expected_case):
    """
    Given a dictionary and a case (either 'lower' or 'upper'), return True if all keys have the same case as specified.
    Examples: is_all_keys_same_case({"a":"apple", "b":"banana"}, 'lower') should return True.
             is_all_keys_same_case({"A":"apple", "B":"banana"}, 'upper') should return True.
             is_all_keys_same_case({"a":"apple", "b":"banana", "C":"carrot"}, 'lower') should return False.
             is_all_keys_same_case({"Name":"John", "Age":"36", "City":"Houston"}, None) should raise a TypeError.
             is_all_keys_same_case({},'lower') should raise an EmptySetError.
    """
    if not dct or isinstance(dct, str):
        raise EmptySetError()
    if expected_case is None:
        raise TypeError("expected_case should be either 'lower' or 'upper'")
    keys = dct.keys()
    return all(map(lambda k: operator.eq(k[0].lower(), k[0].upper()) if expected_case == 'upper' else operator.eq(k[0].lower(), k[0]), keys))

def check_dict_case(dct):
    """
    Given a dictionary, return True if all keys are strings in lower case or all keys are strings in upper case,
    else return False. The function should return False is the given dictionary is empty.
    Examples: check_dict_case({"a":"apple", "b":"banana"}) should return True.
              check_dict_case({"A":"apple", "B":"banana"}) should return False.
              check_dict_case({"a":"apple", 8:"banana", "a":"apple"}) should return False.
              check_dict_case({"STATE":"NC", "ZIP":"12345" }) should return True.
    """
    if not dct:
        return False
    keys = list(dct.keys())[0]
    return is_all_keys_same_case(dct, keys[0].lower() if len(keys) > 0 else None)

if __name__ == "__main__":
    # Run the unit tests
    run_tests(check_dict_case)