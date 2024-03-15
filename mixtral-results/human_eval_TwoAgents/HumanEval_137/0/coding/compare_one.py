# filename: compare_one.py

import re
from my_tests import run_tests

def compare_one(a, b):
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if the values are equal.
    Note: If a real number is represented as a string, the floating point might be . or ,

    compare_one(1, 2.5) ➞ 2.5
    compare_one(1, "2,3") ➞ "2,3"
    compare_one("5,1", "6") ➞ "6"
    compare_one("1", 1) ➞ None
    """
    # Convert input to a common type (float) for comparison
    a = to_float(a)
    b = to_float(b)

    if a > b:
        return type(b)(a)
    elif a < b:
        return type(a)(b)
    else:
        return None

def to_float(n):
    if isinstance(n, float):
        return n
    elif isinstance(n, str):
        return float(re.sub(',', '.', n))
    else:
        return float(n)

# Custom comparison function
def custom_compare(x, y):
    if isinstance(x, float) and isinstance(y, str):
        return float(y.replace(',', '.')) > x
    if isinstance(x, str) and isinstance(y, float):
        return float(x.replace(',', '.')) > y
    return x > y

# Run the unit tests
run_tests(compare_one)