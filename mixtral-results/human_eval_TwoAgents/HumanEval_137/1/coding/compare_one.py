# filename: compare_one.py

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
    # Check if both a and b are of the same type
    if type(a) == type(b):
        if a == b:
            return None
        elif isinstance(a, (int, float)):
            return a if a > b else b
        else:
            # Convert strings to float and compare
            return a if float(a) > float(b) else b
    else:
        # If types are different, convert strings to float and compare
        if isinstance(a, str) and isinstance(b, (int, float)):
            return b
        elif isinstance(a, (int, float)) and isinstance(b, str):
            return a
        elif isinstance(a, str):
            a = float(a.replace(',', '.'))
        elif isinstance(b, str):
            b = float(b.replace(',', '.'))

        return a if a > b else b


# Run the unit tests
run_tests(compare_one)