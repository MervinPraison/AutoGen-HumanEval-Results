# filename: my_tests.py

class TestCase:
    def __init__(self, name, expected):
        self.name = name
        self.expected_output = expected

def run_tests(func):
    cases = [TestCase("test", "TGST"),
             TestCase("This is a message", "tHKS KS C MGSSCGG")]

    for test in cases:
        print(f'Test input: {test.name}')
        actual_output = func(test.name)
        if test.expected_output != actual_output:
            print(f"Test failed: Expected Output: '{test.expected_output}', Actual output: '{actual_output}'")
            raise AssertionError('Test failed')
        print("Test passed")