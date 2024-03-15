# filename: complete_compare_one.py
from my_tests import run_tests

def compare_one(a, b):
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if the values are equal.
    Note: If a real number is represented as a string, the floating point might be . or ,
    """
    def to_float(x):
        if isinstance(x, str):
            return float(x.replace(',', '.'))
        return float(x)

    def to_original_format(x, original):
        if isinstance(original, str):
            return str(x).replace('.', ',') if ',' in original else str(x)
        return original.__class__(x)

    a_float, b_float = to_float(a), to_float(b)

    if a_float > b_float:
        return to_original_format(a_float, a)
    elif b_float > a_float:
        return to_original_format(b_float, b)
    else:
        return None

# Run the unit tests
run_tests(compare_one)