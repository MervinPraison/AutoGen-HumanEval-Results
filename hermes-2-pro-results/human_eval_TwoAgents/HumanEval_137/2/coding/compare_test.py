# filename: compare_test.py
from my_tests import run_tests

def compare_one(a, b):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return max(a, b)
    elif isinstance(a, str) and isinstance(b, (float, int)):
        a = float(a) # Added line to convert string a into float before comparison
        return max(a, b)
    elif isinstance(a, (float, int)) and isinstance(b, str):
        b = float(b) # Added line to convert string b into float before comparison
        return max(a, b)
    else:
        return None

# Run the unit tests
run_tests(compare_one)