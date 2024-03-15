# filename: my_tests.py
import sys
from main import modp

def run_tests(candidate):
    tests = [
        (3, 5),
        (1101, 101),
        (0, 101),
        (3, 11),
        (100, 101),
        (-4, 13),
        (2 ** 31, 2 ** 32)  # Test large powers of 2
    ]
    print("Running tests:")
    for test_case in tests:
        n, p = test_case
        result = candidate(n, p)
        correct_result = pow(2, n, p) if p else 1
        print(f"Test case: {n}, {p}\tResult: {result}\tExpected: {correct_result}")
        assert result == correct_result or (test_case[-1] is not None and result is test_case[-1])
    print("All tests passed.")

tests = [(3, 5), (1101, 101), (0, 101), (3, 11), (100, 101)]
run_tests(modp)